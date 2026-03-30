# kplp — API Reference

## Signal Interface (KSP-2.0)

### Emitted Signals

| Signal Type | Payload | Frequency |
|-------------|---------|-----------|
| `ANALYSIS` | `{score: float, confidence: float}` | On demand |
| `HEALTH_CHECK` | `{status: str, checks: dict}` | Every 60s |
| `STATUS` | `{state: str, metrics: dict}` | Every 300s |

### Consumed Signals

| Signal Type | Source | Action |
|-------------|--------|--------|
| `REGIME_STATE` | project-chimera | Adjust parameters |
| `RISK_LEVEL` | sentinel8 | Apply risk gates |
| `MARKET_DATA` | kirmani-adapters | Process updates |

## Configuration

See `configs/config.yaml` for all available settings.

## Health Endpoint

```json
{
  "status": "healthy",
  "component": "kplp",
  "uptime": 86400,
  "checks": {
    "config": true,
    "dependencies": true,
    "signal_bus": true
  }
}
```
