# SPDX-License-Identifier: Proprietary
"""KEC safety contract — research-only governance constants.

research_only=true  no_trade_signal=true  no_live_execution=true
no_reconcile_mutation=true  execution_status=NO_GO_LIVE_EXECUTION_DISABLED
"""

SAFETY_FLAGS = {
    "research_only": True,
    "no_trade_signal": True,
    "no_live_execution": True,
    "no_reconcile_mutation": True,
    "execution_status": "NO_GO_LIVE_EXECUTION_DISABLED",
}

NON_CLAIMS = [
    "no_bloomberg_equivalence",
    "no_aqr_equivalence",
    "no_allocator_ready",
    "no_proven_alpha",
    "grades_describe_code_surface_not_strategy_alpha",
]
