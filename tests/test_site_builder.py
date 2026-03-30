"""Comprehensive tests for site builder."""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from site_builder import PageMetrics, SiteStructure, SEOChecker, ContentValidator


class TestPageMetrics:
    def test_quality_full(self):
        p = PageMetrics("idx.html", 5000, 200, 10, 5, True, True, True, 500)
        assert p.quality_score > 80

    def test_quality_empty(self):
        p = PageMetrics("empty.html")
        assert p.quality_score == 0

    def test_quality_partial(self):
        p = PageMetrics("p.html", 1000, 100, 3, 1, True, False, False, 2000)
        assert 20 < p.quality_score < 80


class TestSiteStructure:
    def test_scan_current(self):
        s = SiteStructure(root=".")
        s.scan()
        assert isinstance(s.assets, dict)

    def test_scan_missing(self):
        s = SiteStructure(root="/nonexistent_path_xyz")
        s.scan()
        assert len(s.errors) > 0

    def test_summary(self):
        s = SiteStructure(root=".")
        s.scan()
        summary = s.summary()
        assert "total_pages" in summary
        assert "asset_types" in summary

    def test_total_pages(self):
        s = SiteStructure(root=".")
        assert s.total_pages == 0
        s.scan()
        assert isinstance(s.total_pages, int)

    def test_avg_quality(self):
        s = SiteStructure(root=".")
        assert s.avg_quality == 0.0


class TestSEOChecker:
    def test_full_page(self):
        html = '<html lang="en"><head><title>T</title><meta name="description" content="D"><meta charset="utf-8"><meta name="viewport" content="w"></head><body><h1>H</h1><link rel="canonical" href="x"></body></html>'
        seo = SEOChecker()
        results = seo.check_page(html)
        assert results["has_h1"]
        assert results["has_title"]
        assert seo.score(results) > 70

    def test_empty_page(self):
        seo = SEOChecker()
        results = seo.check_page("")
        assert seo.score(results) == 0

    def test_score_empty_results(self):
        seo = SEOChecker()
        assert seo.score({}) == 0.0


class TestContentValidator:
    def test_valid(self):
        text = "About us. Contact info. Performance data. Strategy overview. " + "word " * 100
        v = ContentValidator()
        ok, issues = v.validate(text)
        assert ok

    def test_too_short(self):
        v = ContentValidator()
        ok, issues = v.validate("Short text")
        assert not ok
        assert any("Too few" in i for i in issues)

    def test_missing_sections(self):
        v = ContentValidator()
        ok, issues = v.validate("word " * 200)
        assert not ok
        assert any("Missing section" in i for i in issues)
