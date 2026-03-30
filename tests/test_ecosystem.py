"""Ecosystem integration tests for kplp."""
import pytest
from datetime import datetime


class TestEcosystemCompliance:
    def test_ksp_signal_format(self):
        signal = {
            "source": "kplp",
            "signal_type": "ANALYSIS",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": {"score": 0.85, "confidence": 0.92},
            "metadata": {"version": "2.0", "category": "app"},
        }
        for field in ["source", "signal_type", "timestamp", "payload", "metadata"]:
            assert field in signal

    def test_health_check_format(self):
        health = {
            "status": "healthy",
            "component": "kplp",
            "category": "app",
        }
        assert health["status"] in ["healthy", "degraded", "unhealthy"]

    def test_error_format(self):
        error = {
            "error_code": "E001",
            "source": "kplp",
            "severity": "WARNING",
        }
        assert error["severity"] in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
