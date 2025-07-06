#!/usr/bin/env python3
"""
Debug script for cn_stock_holidays development.

This script provides an IPython environment with all the main modules
pre-imported for convenient debugging and development.

Usage:
    python scripts/debug.py
    # or
    uv run python scripts/debug.py
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import all main modules
import cn_stock_holidays
import cn_stock_holidays.data
import cn_stock_holidays.data_hk
import cn_stock_holidays.common
import cn_stock_holidays.meta_functions

# Import commonly used functions for convenience
from cn_stock_holidays.data import (
    is_trading_day,
    is_holiday,
    trading_days_between,
    get_trading_days,
    get_holidays,
    sync_data,
)

from cn_stock_holidays.data_hk import (
    is_trading_day as is_trading_day_hk,
    is_holiday as is_holiday_hk,
    is_half_day_trading_day,
    trading_days_between as trading_days_between_hk,
    get_trading_days as get_trading_days_hk,
    get_holidays as get_holidays_hk,
    get_half_day_trading_days,
    sync_data as sync_data_hk,
)

from cn_stock_holidays.common import (
    parse_date,
    format_date,
    is_weekend,
)

from cn_stock_holidays.meta_functions import (
    get_cache_info,
    clear_cache,
    is_cache_expired,
    get_half_day_cache_info,
    clear_half_day_cache,
    is_half_day_cache_expired,
)


def main():
    """Start IPython with pre-imported modules."""
    try:
        from IPython import start_ipython

        # Set up IPython configuration
        config = {
            "InteractiveShellApp": {
                "exec_lines": [
                    'print("=== cn_stock_holidays Debug Environment ===")',
                    'print("Available modules and functions:")',
                    'print("- cn_stock_holidays.data: Mainland China market functions")',
                    'print("- cn_stock_holidays.data_hk: Hong Kong market functions")',
                    'print("- cn_stock_holidays.common: Common utilities")',
                    'print("- cn_stock_holidays.meta_functions: Cache management")',
                    "print()",
                    'print("Quick examples:")',
                    "print(\"- is_trading_day('2024-01-01')  # Check if date is trading day\")",
                    "print(\"- is_half_day_trading_day('2024-12-24')  # Check half-day trading\")",
                    "print(\"- get_trading_days('2024-01-01', '2024-01-31')  # Get trading days\")",
                    'print("- get_cache_info()  # Check cache status")',
                    "print()",
                ]
            }
        }

        start_ipython(argv=[], config=config)

    except ImportError:
        print("IPython not found. Installing...")
        print("Run: uv add --dev ipython")
        print("Then run this script again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
