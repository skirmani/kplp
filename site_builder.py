# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Kirmani Partners

"""Site builder and validator for Kirmani Partners pitchbook.

Provides tools for building, validating, and analyzing the
static site structure, content quality, and SEO metrics.
"""
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
from pathlib import Path
import os
import re
import json
from datetime import datetime


@dataclass
class PageMetrics:
    """Metrics for a single HTML page."""
    path: str
    size_bytes: int = 0
    word_count: int = 0
    link_count: int = 0
    image_count: int = 0
    has_title: bool = False
    has_meta_desc: bool = False
    has_og_tags: bool = False
    load_time_ms: float = 0.0

    @property
    def quality_score(self) -> float:
        """Compute quality score 0-100."""
        score = 0.0
        score += 20 if self.has_title else 0
        score += 15 if self.has_meta_desc else 0
        score += 10 if self.has_og_tags else 0
        score += min(20, self.word_count / 50)
        score += min(15, self.link_count * 3)
        score += min(10, self.image_count * 5)
        score += 10 if self.load_time_ms < 1000 else 5 if self.load_time_ms < 3000 else 0
        return min(score, 100.0)


@dataclass
class SiteStructure:
    """Represents the full site structure."""
    root: str
    pages: List[PageMetrics] = field(default_factory=list)
    assets: Dict[str, int] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def scan(self) -> None:
        """Scan the site directory for pages and assets."""
        self.pages = []
        self.assets = {}
        root = Path(self.root)
        if not root.exists():
            self.errors.append(f"Root directory not found: {self.root}")
            return

        ext_count: Dict[str, int] = {}
        for path in root.rglob("*"):
            if ".git" in str(path) or "__pycache__" in str(path):
                continue
            if path.is_file():
                ext = path.suffix.lower()
                ext_count[ext] = ext_count.get(ext, 0) + 1
                if ext in (".html", ".htm"):
                    self.pages.append(self._analyze_page(str(path)))
        self.assets = ext_count

    def _analyze_page(self, path: str) -> PageMetrics:
        """Analyze a single HTML page."""
        try:
            content = open(path).read()
        except (OSError, UnicodeDecodeError):
            return PageMetrics(path=path)

        size = os.path.getsize(path)
        text = re.sub(r"<[^>]+>", " ", content)
        words = len(text.split())
        links = len(re.findall(r"<a\s", content, re.I))
        images = len(re.findall(r"<img\s", content, re.I))
        has_title = bool(re.search(r"<title>", content, re.I))
        has_meta = bool(re.search(r'<meta\s+name="description"', content, re.I))
        has_og = bool(re.search(r'<meta\s+property="og:', content, re.I))

        return PageMetrics(
            path=path, size_bytes=size, word_count=words,
            link_count=links, image_count=images,
            has_title=has_title, has_meta_desc=has_meta, has_og_tags=has_og,
        )

    @property
    def total_pages(self) -> int:
        return len(self.pages)

    @property
    def avg_quality(self) -> float:
        if not self.pages:
            return 0.0
        return sum(p.quality_score for p in self.pages) / len(self.pages)

    @property
    def total_size(self) -> int:
        return sum(p.size_bytes for p in self.pages)

    def summary(self) -> Dict[str, object]:
        return {
            "total_pages": self.total_pages,
            "total_size_kb": self.total_size / 1024,
            "avg_quality": round(self.avg_quality, 1),
            "asset_types": self.assets,
            "errors": self.errors,
        }


@dataclass
class SEOChecker:
    """SEO validation for pitchbook pages."""
    required_meta: List[str] = field(default_factory=lambda: [
        "description", "viewport", "charset"
    ])

    def check_page(self, content: str) -> Dict[str, bool]:
        results: Dict[str, bool] = {}
        results["has_h1"] = bool(re.search(r"<h1", content, re.I))
        results["has_title"] = bool(re.search(r"<title>", content, re.I))
        results["has_canonical"] = bool(re.search(r'rel="canonical"', content, re.I))
        results["has_lang"] = bool(re.search(r'<html\s+lang=', content, re.I))
        for meta in self.required_meta:
            results[f"meta_{meta}"] = bool(
                re.search(rf'<meta\s[^>]*{meta}', content, re.I)
            )
        return results

    def score(self, results: Dict[str, bool]) -> float:
        if not results:
            return 0.0
        return sum(results.values()) / len(results) * 100


@dataclass
class ContentValidator:
    """Validate content quality."""
    min_words: int = 100
    max_words: int = 5000
    required_sections: List[str] = field(default_factory=lambda: [
        "about", "contact", "performance", "strategy"
    ])

    def validate(self, text: str) -> Tuple[bool, List[str]]:
        issues: List[str] = []
        words = text.lower().split()
        if len(words) < self.min_words:
            issues.append(f"Too few words: {len(words)} < {self.min_words}")
        if len(words) > self.max_words:
            issues.append(f"Too many words: {len(words)} > {self.max_words}")
        for section in self.required_sections:
            if section not in text.lower():
                issues.append(f"Missing section: {section}")
        return len(issues) == 0, issues
