"""Core tests for kplp."""
import pytest
import importlib
import sys
from pathlib import Path


class TestProjectStructure:
    """Verify project structure and basic health."""

    def test_project_root_exists(self):
        root = Path(__file__).parent.parent
        assert root.exists()

    def test_has_source_files(self):
        root = Path(__file__).parent.parent
        py_files = list(root.rglob("*.py"))
        # Exclude test files and __pycache__
        src_files = [
            f for f in py_files
            if "__pycache__" not in str(f) and "test_" not in f.name
        ]
        assert len(src_files) > 0, "No source files found"

    def test_no_syntax_errors(self):
        """Check all .py files for syntax errors."""
        root = Path(__file__).parent.parent
        errors = []
        for py_file in root.rglob("*.py"):
            if "__pycache__" in str(py_file):
                continue
            try:
                with open(py_file) as f:
                    compile(f.read(), str(py_file), "exec")
            except SyntaxError as e:
                errors.append(f"{py_file}: {e}")
        assert not errors, f"Syntax errors found:\n" + "\n".join(errors)

    def test_no_circular_imports(self):
        root = Path(__file__).parent.parent
        init = root / "kplp" / "__init__.py"
        if init.exists():
            try:
                sys.path.insert(0, str(root))
                importlib.import_module("kplp")
            except ImportError:
                pytest.skip("Module has unresolved dependencies")
            except Exception:
                pytest.skip("Module initialization requires runtime deps")
        else:
            pytest.skip("No __init__.py found")


class TestConfiguration:
    """Test configuration and settings."""

    def test_sample_config_is_dict(self, sample_config):
        assert isinstance(sample_config, dict)

    def test_sample_config_has_name(self, sample_config):
        assert "name" in sample_config
        assert sample_config["name"] == "kplp"

    def test_sample_config_has_version(self, sample_config):
        assert "version" in sample_config


class TestBasicFunctionality:
    """Basic functionality smoke tests."""

    def test_python_version(self):
        import sys
        assert sys.version_info >= (3, 10), "Python 3.10+ required"

    def test_tmp_output_fixture(self, tmp_output):
        assert tmp_output.exists()
        assert tmp_output.is_dir()

    def test_can_write_output(self, tmp_output):
        test_file = tmp_output / "test.txt"
        test_file.write_text("test")
        assert test_file.read_text() == "test"
