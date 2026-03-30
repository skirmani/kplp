"""Validate kplp pitchbook site structure."""
import os
import re

def validate_index():
    """Check index.html exists and has required structure."""
    if not os.path.exists("index.html"):
        return False, "index.html missing"
    with open("index.html") as f:
        content = f.read()
    if "<html" not in content.lower():
        return False, "Missing <html> tag"
    if "kirmani" not in content.lower():
        return False, "Missing Kirmani branding"
    return True, "OK"

def count_assets():
    """Count site assets."""
    exts = {".html": 0, ".css": 0, ".js": 0, ".png": 0, ".jpg": 0, ".svg": 0}
    for root, _, files in os.walk("."):
        if ".git" in root:
            continue
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in exts:
                exts[ext] += 1
    return exts
