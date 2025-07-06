#!/usr/bin/env python3
"""
Quick test script for cn_stock_holidays development.

This script provides a simple way to test the package functionality
without starting a full IPython session.

Usage:
    python scripts/quick_test.py
    # or
    uv run python scripts/quick_test.py
"""

import sys
from pathlib import Path
from datetime import datetime, date, timedelta

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_mainland_china():
    """Test mainland China market functions."""
    print("=== Testing Mainland China Market ===")

    from cn_stock_holidays.data import (
        is_trading_day,
        trading_days_between,
    )

    # Test dates
    test_dates = [
        date(2024, 1, 1),  # New Year's Day (holiday)
        date(2024, 1, 2),  # Regular trading day
        date(2024, 1, 6),  # Saturday (weekend)
        date(2024, 1, 7),  # Sunday (weekend)
        date(2024, 2, 10),  # Chinese New Year (holiday)
        date(2024, 5, 1),  # Labor Day (holiday)
    ]

    for test_date in test_dates:
        is_trading = is_trading_day(test_date)
        print(f"{test_date}: Trading Day={is_trading}")

    # Test trading days between
    start_date = date(2024, 1, 1)
    end_date = date(2024, 1, 31)
    trading_days = list(trading_days_between(start_date, end_date))
    print(
        f"\nTrading days between {start_date} and {end_date}: {len(trading_days)} days"
    )
    print(f"First 5 trading days: {trading_days[:5]}")


def test_hong_kong():
    """Test Hong Kong market functions."""
    print("\n=== Testing Hong Kong Market ===")

    from cn_stock_holidays.data_hk import (
        is_trading_day,
        is_half_day_trading_day,
        trading_days_between,
    )

    # Test dates
    test_dates = [
        date(2024, 1, 1),  # New Year's Day (holiday)
        date(2024, 1, 2),  # Regular trading day
        date(2024, 1, 6),  # Saturday (weekend)
        date(2024, 1, 7),  # Sunday (weekend)
        date(2024, 2, 9),  # Chinese New Year Eve (half-day)
        date(2024, 2, 10),  # Chinese New Year (holiday)
        date(2024, 12, 24),  # Christmas Eve (half-day)
        date(2024, 12, 25),  # Christmas (holiday)
        date(2024, 12, 31),  # New Year's Eve (half-day)
    ]

    for test_date in test_dates:
        is_trading = is_trading_day(test_date)
        is_half = is_half_day_trading_day(test_date)
        print(f"{test_date}: Trading Day={is_trading}, Half-day={is_half}")

    # Test half-day trading days
    start_date = date(2024, 12, 1)
    end_date = date(2024, 12, 31)
    # Get half-day trading days manually
    half_days = []
    current = start_date
    while current <= end_date:
        if is_half_day_trading_day(current):
            half_days.append(current)
        current += timedelta(days=1)
    print(f"\nHalf-day trading days in December 2024: {half_days}")


def test_cache():
    """Test cache management functions."""
    print("\n=== Testing Cache Management ===")

    from cn_stock_holidays.data import get_cached, check_expired
    from cn_stock_holidays.data_hk import (
        get_cached_with_half_day,
        check_expired_with_half_day,
    )

    # Test main cache
    try:
        main_data = get_cached()
        main_expired = check_expired()
        print(f"Main cache: {len(main_data)} holidays, expired: {main_expired}")
    except Exception as e:
        print(f"Main cache error: {e}")

    # Test half-day cache
    try:
        hk_holidays, hk_half_days = get_cached_with_half_day()
        hk_expired = check_expired_with_half_day()
        print(
            f"HK cache: {len(hk_holidays)} holidays, {len(hk_half_days)} half-days, expired: {hk_expired}"
        )
    except Exception as e:
        print(f"HK cache error: {e}")


def test_common_utils():
    """Test common utility functions."""
    print("\n=== Testing Common Utilities ===")

    from cn_stock_holidays.common import int_to_date, date_to_str, date_to_int

    # Test date conversion functions
    test_date_int = 20240101
    test_date = date(2024, 1, 1)

    # Test int_to_date
    converted_date = int_to_date(test_date_int)
    print(f"Int {test_date_int} -> Date: {converted_date}")

    # Test date_to_str
    date_str = date_to_str(test_date)
    print(f"Date {test_date} -> String: {date_str}")

    # Test date_to_int
    date_int = date_to_int(test_date)
    print(f"Date {test_date} -> Int: {date_int}")

    # Test weekend check
    weekend_date = date(2024, 1, 6)  # Saturday
    weekday_date = date(2024, 1, 8)  # Monday
    print(f"{weekend_date} is weekend: {weekend_date.weekday() >= 5}")
    print(f"{weekday_date} is weekend: {weekday_date.weekday() >= 5}")


def main():
    """Run all tests."""
    print("cn_stock_holidays Quick Test")
    print("=" * 50)

    try:
        test_mainland_china()
        test_hong_kong()
        test_cache()
        test_common_utils()

        print("\n" + "=" * 50)
        print("All tests completed successfully!")

    except Exception as e:
        print(f"\nError during testing: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
