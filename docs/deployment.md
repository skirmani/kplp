# kplp — Deployment Guide

## Prerequisites

- Python 3.10+
- Docker (optional)
- Access to Kirmani ecosystem signal bus

## Local Development

```bash
git clone git@github.com:skirmani/kplp.git
cd kplp
pip install -e ".[dev]"
pre-commit install
pytest tests/ -v
```

## Docker

```bash
docker build -t kplp .
docker run -e ENV=production kplp
```

## CI/CD

Automated via GitHub Actions:
- **ci.yml**: Runs on every push (lint, type-check, test)
- **release.yml**: Creates GitHub release on version tags
- **daily-health.yml**: Scheduled health check (weekdays 10:00 UTC)

## Monitoring

Health checks emit to prod-monitor via KSP signal bus.
