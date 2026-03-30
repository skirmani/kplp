"""Utility and helper tests for kplp."""
import pytest
import os
import json
from pathlib import Path


class TestFileStructure:
    """Validate file structure and conventions."""

    def test_has_readme(self):
        root = Path(__file__).parent.parent
        assert (root / "README.md").exists(), "README.md missing"

    def test_has_pyproject(self):
        root = Path(__file__).parent.parent
        assert (root / "pyproject.toml").exists(), "pyproject.toml missing"

    def test_has_ci_config(self):
        root = Path(__file__).parent.parent
        ci_dir = root / ".github" / "workflows"
        assert ci_dir.exists(), ".github/workflows/ missing"
        yamls = list(ci_dir.glob("*.yml")) + list(ci_dir.glob("*.yaml"))
        assert len(yamls) > 0, "No CI workflow files found"

    def test_no_secrets_committed(self):
        root = Path(__file__).parent.parent
        dangerous = [".env", "credentials.json", "secrets.yaml", "token.txt"]
        found = []
        for d in dangerous:
            if (root / d).exists():
                found.append(d)
        assert not found, f"Potential secrets found: {found}"

    def test_gitignore_exists(self):
        root = Path(__file__).parent.parent
        gi = root / ".gitignore"
        if gi.exists():
            content = gi.read_text()
            assert "__pycache__" in content or "*.pyc" in content
        else:
            pytest.skip("No .gitignore (not critical)")


class TestDataIntegrity:
    """Test data file integrity if applicable."""

    def test_json_configs_valid(self):
        root = Path(__file__).parent.parent
        for jf in root.rglob("*.json"):
            if "__pycache__" in str(jf) or "node_modules" in str(jf):
                continue
            try:
                with open(jf) as f:
                    json.load(f)
            except json.JSONDecodeError:
                pytest.fail(f"Invalid JSON: {jf}")

    def test_yaml_configs_valid(self):
        root = Path(__file__).parent.parent
        try:
            import yaml
        except ImportError:
            pytest.skip("PyYAML not installed")
        for yf in list(root.rglob("*.yml")) + list(root.rglob("*.yaml")):
            if "__pycache__" in str(yf) or "node_modules" in str(yf):
                continue
            try:
                with open(yf) as f:
                    yaml.safe_load(f)
            except Exception:
                pytest.fail(f"Invalid YAML: {yf}")
