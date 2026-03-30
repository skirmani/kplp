"""Integration tests batch 2."""
import pytest

def test_imports_2():
    import site_builder
    assert site_builder.PageMetrics is not None

def test_seo_exists_2():
    from site_builder import SEOChecker
    checker = SEOChecker()
    assert callable(checker.check_page)

def test_validator_exists_2():
    from site_builder import ContentValidator
    v = ContentValidator()
    assert callable(v.validate)
