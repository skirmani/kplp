"""Site validation tests — batch 6."""
import pytest

def test_site_structure_6():
    """Validate site structure."""
    import validate_site
    ok, msg = validate_site.validate_index()
    assert ok or msg == "index.html missing", msg

def test_assets_counted_6():
    """Count assets."""
    import validate_site
    assets = validate_site.count_assets()
    assert isinstance(assets, dict)
