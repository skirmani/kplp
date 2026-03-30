# kplp — Architecture

## System Context

kplp is a **app**-tier component in the Kirmani Partners LP
quantitative trading ecosystem. It participates in the KDE (Kirmani Decision Engine)
pipeline via the KSP (Kirmani Signal Protocol) universal signal bus.

## Integration Points

| System | Protocol | Direction |
|--------|----------|-----------|
| kirmani-signal-protocol | KSP-2.0 | Bidirectional |
| prod-monitor | gRPC/REST | Emits health |
| sentinel8 | KSP-2.0 | Receives risk |
| kirmani-agent-mesh | WebSocket | Agent coordination |

## Data Flow

```
Market Data → kplp → KSP Signal Bus → KDE Pipeline → Execution
                ↑                                       |
                └───── Feedback (regime, risk) ─────────┘
```

## Quality Standards

- **CI/CD**: GitHub Actions (lint, type-check, test, release, daily health)
- **Testing**: pytest with conftest fixtures, module-level and integration tests
- **Linting**: ruff (E, F, W, I, N, UP, B, SIM rules)
- **Typing**: mypy with py.typed marker
- **Hooks**: pre-commit (ruff, trailing whitespace, YAML check)
- **Container**: Dockerfile for production deployment
