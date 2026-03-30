"""Site validation tests — batch 1."""
import pytest

def test_site_structure_1():
    """Validate site structure."""
    import validate_site
    ok, msg = validate_site.validate_index()
    assert ok or msg == "index.html missing", msg

def test_assets_counted_1():
    """Count assets."""
    import validate_site
    assets = validate_site.count_assets()
    assert isinstance(assets, dict)
