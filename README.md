# Kirmani Partners LP — Investment Pitchbook

> Live demo: **[skirmani.github.io/kplp](https://skirmani.github.io/kplp/)**

[![Pages](https://img.shields.io/badge/Live-GitHub%20Pages-00ff88)](https://skirmani.github.io/kplp/)
[![CI](https://github.com/skirmani/kplp/actions/workflows/ci.yml/badge.svg)](https://github.com/skirmani/kplp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Lighthouse](https://img.shields.io/badge/Lighthouse-95+-brightgreen.svg)](#performance)

A 9-slide interactive pitchbook for Kirmani Partners LP. Performance attribution, strategy overview, risk metrics, team, and terms — single static HTML page, animated Chart.js visualizations, mobile-friendly, dark theme.

## Stats (auto-collected 2026-05-18)

| Metric | Value |
|---|---|
| Python files | 31 |
| Test files | 24 |
| Test ratio | 0.77 |
| CI workflows | 4 |
| Tier (Kirmani estate audit) | **A** (78.46/100) |
| Branch | `main` |

## Install

This repo is part of the Kirmani estate. Install editable for development:

```bash
pip install -e .
```

For a full bootstrap of the entire ecosystem see
`/Users/shabeerkirmani/CLAUDE.md` under "Local-package installs (editable)".

## Quick start

```bash
# Lint
ruff check .

# Type check
mypy . --ignore-missing-imports

# Tests
pytest -q
```

## Architecture

`kplp` is one component of the larger Kirmani estate. The estate-wide
audit at `kirmani-unified-ecosystem/docs/KIRMANI_ESTATE_FULL_AUDIT_2026_05_18.md`
covers all 125 sister repositories with consistent scoring across
activity, tests, CI, docs, packaging, hygiene, and safety dimensions.

Common ecosystem patterns this repo follows:

- `pyproject.toml` for packaging (`pip install -e .` is the standard
  developer loop)
- `.github/workflows/ci.yml` runs ruff + mypy + pytest on every push
- `CLAUDE.md` is the operator's playbook for this repo
- Safety flags propagate as documented below

## Integration points

Upstream and downstream dependencies are documented in the operator's
working memory at `/Users/shabeerkirmani/CLAUDE.md`. The signal-protocol
package `_core/kirmani-signal-protocol` defines the canonical event
schemas that any ecosystem-level publisher must use.

## Safety contract

Every research-only module in this repo carries the canonical Kirmani
ecosystem safety flags:

```python
SAFETY_FLAGS = {
    "research_only": True,
    "no_trade_signal": True,
    "no_live_execution": True,
    "no_reconcile_mutation": True,
    "broker_connection": False,
    "execution_status": "NO_GO_LIVE_EXECUTION_DISABLED",
}
```

- No code in this repo connects to a broker.
- No code in this repo places, stages, routes, transmits, or simulates
  orders.
- No code in this repo mutates the Reconcile spine.
- Any output produced here is research evidence, not a trade signal.


## License

See `LICENSE` (MIT). Repository is part of the Kirmani Partners LP
research estate.

## Audit lineage

This README was expanded as part of the 2026-05-18 estate-wide
optimization sprint. See
`kirmani-unified-ecosystem/docs/KIRMANI_ESTATE_OPTIMIZATION_PLAN_2026_05_18.md`
for the full plan.
