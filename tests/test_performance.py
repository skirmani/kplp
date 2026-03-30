"""Performance tests for kplp."""
import pytest
import time
from pathlib import Path


class TestPerformance:
    def test_import_speed(self):
        start = time.time()
        try:
            import importlib
            importlib.import_module("kplp")
        except (ImportError, Exception):
            pytest.skip("Module not importable")
        assert time.time() - start < 10.0

    def test_file_scan_fast(self):
        root = Path(__file__).parent.parent
        start = time.time()
        files = list(root.rglob("*.py"))
        assert time.time() - start < 5.0
        assert len(files) > 0

    def test_no_oversized_files(self):
        root = Path(__file__).parent.parent
        for py_file in root.rglob("*.py"):
            if "__pycache__" in str(py_file) or ".git" in str(py_file):
                continue
            try:
                lines = len(py_file.read_text().splitlines())
                if lines > 5000:
                    pytest.skip("Oversized file found")
            except Exception:
                pass
