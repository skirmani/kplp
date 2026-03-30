"""kplp utilities."""
from datetime import datetime, timezone


def now_utc():
    """Return current UTC timestamp."""
    return datetime.now(timezone.utc)


def format_signal(source, signal_type, payload):
    """Format a KSP signal."""
    return {
        "source": source,
        "signal_type": signal_type,
        "timestamp": now_utc().isoformat(),
        "payload": payload,
    }
