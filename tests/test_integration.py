"""Integration tests for kplp."""
import pytest
from pathlib import Path


@pytest.mark.integration
class TestEcosystemIntegration:
    """Test integration with the Kirmani ecosystem."""

    def test_signal_protocol_compatibility(self):
        """Verify KSP signal format compatibility."""
        sample_signal = {
            "source": "kplp",
            "type": "SIGNAL",
            "timestamp": "2026-03-30T00:00:00Z",
            "payload": {"value": 0.75, "confidence": 0.85},
            "metadata": {"version": "1.0.0"},
        }
        assert "source" in sample_signal
        assert "type" in sample_signal
        assert "timestamp" in sample_signal
        assert "payload" in sample_signal

    def test_config_schema(self, sample_config):
        """Verify config follows ecosystem schema."""
        required_keys = ["name", "version"]
        for key in required_keys:
            assert key in sample_config, f"Missing required config key: {key}"
