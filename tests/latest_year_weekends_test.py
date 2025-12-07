# coding: utf-8

"""
Automated test to verify that the latest year in data.txt does
not contain weekend dates.

This test automatically detects the latest year in the data file
and validates:
1. All weekend dates in that year are NOT in data.txt
2. All weekend dates are correctly identified as non-trading days
3. No weekend dates were accidentally added to the data file

This ensures data integrity whenever new year data is added.
"""

import unittest
from datetime import date, timedelta
from typing import List, Set

from cn_stock_holidays.data import get_cached, is_trading_day


class TestLatestYearWeekends(unittest.TestCase):
    """Test that the latest year in data.txt contains no weekend dates."""

    @classmethod
    def setUpClass(cls):
        """Get the latest year from data.txt once for all tests."""
        # Read all dates from data.txt
        holidays = get_cached()

        if not holidays:
            raise ValueError("No holiday data found in data.txt")

        # Find the latest year
        cls.latest_year = max(d.year for d in holidays)

        # Get all dates from data.txt for the latest year
        cls.latest_year_dates: Set[date] = {
            d for d in holidays if d.year == cls.latest_year
        }

        # Generate all weekend dates for the latest year
        cls.weekend_dates: List[date] = []
        current_date = date(cls.latest_year, 1, 1)
        end_date = date(cls.latest_year, 12, 31)

        while current_date <= end_date:
            if current_date.weekday() >= 5:  # Saturday=5, Sunday=6
                cls.weekend_dates.append(current_date)
            current_date += timedelta(days=1)

        print(f"\n{'='*70}")
        print(f"Testing latest year: {cls.latest_year}")
        print(
            f"Total dates in data.txt for {cls.latest_year}: "
            f"{len(cls.latest_year_dates)}"
        )
        print(f"Total weekend dates in {cls.latest_year}: {len(cls.weekend_dates)}")
        print(f"{'='*70}\n")

    def test_no_weekends_in_data_file(self):
        """Verify that no weekend dates are in data.txt for the latest year."""
        weekends_in_data = []

        for weekend_date in self.weekend_dates:
            if weekend_date in self.latest_year_dates:
                weekends_in_data.append(weekend_date)

        if weekends_in_data:
            error_msg = (
                f"\n❌ Found {len(weekends_in_data)} weekend date(s) in data.txt "
                f"for year {self.latest_year}:\n"
            )
            for d in weekends_in_data:
                weekday_name = d.strftime("%A")
                error_msg += f"  - {d} ({weekday_name})\n"
            error_msg += (
                "\nWeekend dates should NOT be in data.txt as they are "
                "automatically handled by the code.\n"
                "Please remove these dates from cn_stock_holidays/data.txt"
            )
            self.fail(error_msg)
        else:
            print(f"✓ No weekend dates found in data.txt for {self.latest_year}")

    def test_all_weekends_are_non_trading_days(self):
        """Verify all weekend dates are non-trading days."""
        failed_dates = []

        for weekend_date in self.weekend_dates:
            if is_trading_day(weekend_date):
                failed_dates.append(weekend_date)

        if failed_dates:
            error_msg = (
                f"\n❌ {len(failed_dates)} weekend date(s) incorrectly identified "
                f"as trading days:\n"
            )
            for d in failed_dates:
                weekday_name = d.strftime("%A")
                error_msg += f"  - {d} ({weekday_name})\n"
            self.fail(error_msg)
        else:
            print(
                f"✓ All {len(self.weekend_dates)} weekend dates in {self.latest_year} "
                f"are correctly non-trading days"
            )

    def test_all_data_file_dates_are_weekdays(self):
        """Verify that all dates in data.txt for the latest year are weekdays."""
        weekend_dates_in_file = []

        for d in self.latest_year_dates:
            if d.weekday() >= 5:  # Saturday or Sunday
                weekend_dates_in_file.append(d)

        if weekend_dates_in_file:
            error_msg = (
                f"\n❌ Found {len(weekend_dates_in_file)} weekend date(s) "
                f"in data.txt for {self.latest_year}:\n"
            )
            for d in weekend_dates_in_file:
                weekday_name = d.strftime("%A")
                error_msg += f"  - {d.strftime('%Y%m%d')} ({weekday_name})\n"
            error_msg += (
                "\nAll dates in data.txt must be weekdays (Monday-Friday).\n"
                "Please remove weekend dates from cn_stock_holidays/data.txt"
            )
            self.fail(error_msg)
        else:
            print(
                f"✓ All {len(self.latest_year_dates)} dates in data.txt "
                f"for {self.latest_year} are weekdays"
            )

    def test_data_file_dates_are_non_trading(self):
        """Verify that all dates in data.txt are correctly non-trading days."""
        incorrectly_trading = []

        for d in self.latest_year_dates:
            if is_trading_day(d):
                incorrectly_trading.append(d)

        if incorrectly_trading:
            error_msg = (
                f"\n❌ Found {len(incorrectly_trading)} date(s) in data.txt "
                f"that are incorrectly identified as trading days:\n"
            )
            for d in incorrectly_trading:
                weekday_name = d.strftime("%A")
                error_msg += f"  - {d} ({weekday_name})\n"
            self.fail(error_msg)
        else:
            print(
                f"✓ All {len(self.latest_year_dates)} dates in data.txt "
                f"for {self.latest_year} are non-trading days"
            )

    def test_weekend_count_is_reasonable(self):
        """Verify the number of weekends is reasonable for a year."""
        # A year should have approximately 104 weekend days (52 weeks * 2 days)
        # Allow range of 102-106 to account for how the year starts/ends
        min_weekends = 102
        max_weekends = 106

        actual_count = len(self.weekend_dates)

        self.assertGreaterEqual(
            actual_count,
            min_weekends,
            f"Too few weekend dates detected ({actual_count}). "
            f"Expected at least {min_weekends}.",
        )
        self.assertLessEqual(
            actual_count,
            max_weekends,
            f"Too many weekend dates detected ({actual_count}). "
            f"Expected at most {max_weekends}.",
        )

        print(
            f"✓ Weekend count for {self.latest_year} is reasonable: "
            f"{actual_count} days ({min_weekends}-{max_weekends} expected)"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
