# SPDX-License-Identifier: Proprietary
# Copyright (c) 2026 Kirmani Partners

"""kplp configuration."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CONFIG_DIR = BASE_DIR / "configs"
DEFAULT_CONFIG = CONFIG_DIR / "config.yaml"


def get_config():
    """Load configuration."""
    return {"name": "kplp", "version": "1.0.0", "base_dir": str(BASE_DIR)}
