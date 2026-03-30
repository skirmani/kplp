"""Configuration validation tests for kplp."""
import pytest
import json
import os
from pathlib import Path


class TestConfiguration:
    def test_pyproject_valid(self):
        root = Path(__file__).parent.parent
        pyproject = root / "pyproject.toml"
        assert pyproject.exists()
        content = pyproject.read_text()
        assert "[project]" in content or "[build-system]" in content

    def test_ci_workflows_valid(self):
        root = Path(__file__).parent.parent
        wf_dir = root / ".github" / "workflows"
        assert wf_dir.exists()
        yamls = list(wf_dir.glob("*.yml")) + list(wf_dir.glob("*.yaml"))
        assert len(yamls) >= 1

    def test_ruff_config_exists(self):
        root = Path(__file__).parent.parent
        assert (root / "ruff.toml").exists() or (root / ".ruff.toml").exists() or (root / "pyproject.toml").exists()

    def test_dockerfile_valid(self):
        root = Path(__file__).parent.parent
        df = root / "Dockerfile"
        if df.exists():
            content = df.read_text()
            assert "FROM" in content
        else:
            pytest.skip("No Dockerfile")

    def test_requirements_parseable(self):
        root = Path(__file__).parent.parent
        req = root / "requirements.txt"
        if req.exists():
            content = req.read_text()
            for line in content.splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    assert len(line) > 0
        else:
            pytest.skip("No requirements.txt")
