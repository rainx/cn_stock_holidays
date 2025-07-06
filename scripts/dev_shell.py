#!/usr/bin/env python3
"""
Development shell for cn_stock_holidays.

A simple script to start IPython with all project modules pre-loaded
for convenient development and debugging.

Usage:
    python scripts/dev_shell.py
    # or
    uv run python scripts/dev_shell.py
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def main():
    """Start IPython with project modules pre-loaded."""
    try:
        from IPython import start_ipython

        # Pre-import modules
        import cn_stock_holidays
        import cn_stock_holidays.data
        import cn_stock_holidays.data_hk
        import cn_stock_holidays.common
        import cn_stock_holidays.meta_functions

        # Import commonly used functions
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
            is_half_day_trading_day,
            trading_days_between as trading_days_between_hk,
            get_half_day_trading_days,
            sync_data as sync_data_hk,
        )

        from cn_stock_holidays.common import (
            int_to_date,
            date_to_str,
            date_to_int,
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

        # Start IPython with comprehensive configuration
        start_ipython(
            argv=[],
            user_ns={
                # Mainland China functions
                "is_trading_day": is_trading_day,
                "is_holiday": is_holiday,
                "trading_days_between": trading_days_between,
                "get_trading_days": get_trading_days,
                "get_holidays": get_holidays,
                "sync_data": sync_data,
                # Hong Kong functions
                "is_trading_day_hk": is_trading_day_hk,
                "is_half_day_trading_day": is_half_day_trading_day,
                "trading_days_between_hk": trading_days_between_hk,
                "get_half_day_trading_days": get_half_day_trading_days,
                "sync_data_hk": sync_data_hk,
                # Common utilities
                "int_to_date": int_to_date,
                "date_to_str": date_to_str,
                "date_to_int": date_to_int,
                "parse_date": parse_date,
                "format_date": format_date,
                "is_weekend": is_weekend,
                # Cache management
                "get_cache_info": get_cache_info,
                "clear_cache": clear_cache,
                "is_cache_expired": is_cache_expired,
                "get_half_day_cache_info": get_half_day_cache_info,
                "clear_half_day_cache": clear_half_day_cache,
                "is_half_day_cache_expired": is_half_day_cache_expired,
            },
        )

    except ImportError:
        print("IPython not found. Installing...")
        print("Run: uv add --dev ipython")
        print("Then run this script again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
