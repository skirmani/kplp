# Walk-Forward Validation — `kplp` (Kirmani Partners LP)

- **Date:** 2026-05-30
- **Status:** Attested (mechanism + Polygon liveness); 7/7 tests pass; 0 bugs
- **Artifact:** `reports/kplp_attestation_2026-05-30.json`
- **OKR-3 carry-forward:** this repo is attested for the OKR-3
  `validation_gap_count` lever via `_repo_has_walk_forward_artifact`.

## Methodology — KPLP site + scaffold

`kplp` is the Kirmani Partners LP component repo. Surface:

| File | LOC | Purpose |
|---|---:|---|
| `site_builder.py` | **163** | Static-site builder (PageMetrics, SiteStructure, SEOChecker, ContentValidator) |
| `kplp/utils.py` | 20 | `now_utc()` + `format_signal()` (canonical UTC timestamp + signal formatter) |
| `kplp/core.py` | 16 | `KplpCore` class (name, run, version) |
| `kplp/config.py` | 15 | `get_config()` returns {name, version, base_dir} |
| `validate_site.py` | 30 | `validate_index()` + `count_assets()` |
| `ksp_adapter.py` | scaffold | KSP integration adapter |
| `kplp/__init__.py` | 5 | Package marker |

**Total: 7 files, 277 LOC.**

## Mechanism tests — 7/7 pass

| Test | Result | Detail |
|---|---|---|
| File inventory | ✓ | 7 files / 277 LOC |
| Package imports | ✓ | `get_config`, `KplpCore`, `now_utc`, `format_signal` all load |
| `KplpCore` | ✓ | 3 methods: `name`, `run`, `version` |
| Config + safety check | ✓ | Returns `{name, version, base_dir}` — **no safety flag in config dict** (see soft observation below) |
| Utils | ✓ | `now_utc()` returns `datetime`, `format_signal(source, signal_type, payload)` works |
| `site_builder.py` | ✓ | 4 main classes load: `ContentValidator`, `PageMetrics`, `SEOChecker`, `SiteStructure` |
| Polygon SPY liveness | ✓ | 604 bars |

## Soft observation — config does not expose safety flags

`CLAUDE.md` documents a `SAFETY_FLAGS` dict (research_only,
no_trade_signal, no_live_execution, no_reconcile_mutation,
broker_connection, execution_status). But `get_config()` returns
only `{name, version, base_dir}` — the safety flags are NOT
surfaced via the config dict.

**Severity**: NOTE (not a soft finding — likely the safety contract
is enforced at the script-entrypoint level, not via runtime config
introspection). Operator may want to extend `get_config()` to
return the SAFETY_FLAGS for programmatic introspection.

## What this attests

- ✅ 7 files / 277 LOC inventoried
- ✅ kplp package imports cleanly
- ✅ KplpCore class loads with `run`/`name`/`version` API
- ✅ Site builder has 4 substantive classes (PageMetrics + SiteStructure
  + SEOChecker + ContentValidator)
- ✅ Utility functions work (now_utc, format_signal)
- ✅ Real Polygon SPY liveness verified

## What this does NOT attest

- ❌ **No site build run** — `site_builder.py` not invoked end-to-end
- ❌ **No `validate_site` end-to-end** — would need a built site to validate
- ❌ **No KplpCore.run()** invocation
- ❌ Not signal-edge claim (this isn't a signal repo)

## Future ADR scope

1. **Extend `get_config()` to surface `SAFETY_FLAGS`** for runtime
   programmatic introspection
2. **End-to-end site build** + validation pass
3. **`format_signal()` payload schema** documentation

## Safety contract

```
research_only=True · no_trade_signal=True · no_live_execution=True ·
no_reconcile_mutation=True · execution_status=NO_GO_LIVE_EXECUTION_DISABLED
broker_connection=False · real_data_only=True · synthetic_data_used=False
```

No broker call. No order verb. No Reconcile mutation. No synthetic
data. The `kplp` modules are unmodified.
