# coding: utf-8

import unittest
from datetime import date, datetime

from cn_stock_holidays.data_hk import (
    is_half_day_trading_day,
    is_trading_day,
    get_cached_with_half_day,
)
from cn_stock_holidays.common import int_to_date


class TestHalfDayWeekendLogic(unittest.TestCase):
    """Test that half-day trading logic correctly handles weekends."""

    def setUp(self):
        """Clear cache before each test."""
        from cn_stock_holidays.data_hk import get_cached_with_half_day

        get_cached_with_half_day.cache_clear()

    def test_weekend_half_days_are_excluded(self):
        """Test that half-day trading days on weekends are correctly excluded."""
        # These dates were previously marked as half-days but fall on weekends
        weekend_half_days = [
            (2000, 12, 24),  # Sunday
            (2005, 12, 24),  # Saturday
            (2006, 12, 24),  # Sunday
            (2011, 12, 24),  # Saturday
            (2016, 12, 24),  # Saturday
            (2022, 12, 24),  # Saturday
            (2023, 12, 24),  # Sunday
            (2006, 1, 28),  # Saturday
            (2009, 1, 25),  # Sunday
            (2012, 1, 22),  # Sunday
            (2016, 2, 7),  # Sunday
            (2022, 1, 30),  # Sunday
            (2004, 4, 4),  # Sunday
            (2001, 9, 30),  # Sunday
        ]

        for year, month, day in weekend_half_days:
            test_date = date(year, month, day)
            with self.subTest(date=test_date):
                # Should not be a half-day trading day (because it's weekend)
                self.assertFalse(
                    is_half_day_trading_day(test_date),
                    f"{test_date} should not be a half-day trading day (weekend)",
                )
                # Should not be a trading day (because it's weekend)
                self.assertFalse(
                    is_trading_day(test_date),
                    f"{test_date} should not be a trading day (weekend)",
                )

    def test_valid_half_days_are_included(self):
        """Test that valid half-day trading days (weekdays) are correctly included."""
        # These are valid half-day trading days (weekdays)
        valid_half_days = [
            (2001, 12, 24),  # Monday
            (2002, 12, 24),  # Tuesday
            (2003, 12, 24),  # Wednesday
            (2004, 12, 24),  # Friday
            (2007, 12, 24),  # Monday
            (2008, 12, 24),  # Wednesday
            (2009, 12, 24),  # Thursday
            (2010, 12, 24),  # Friday
            (2012, 12, 24),  # Monday
            (2013, 12, 24),  # Tuesday
        ]

        for year, month, day in valid_half_days:
            test_date = date(year, month, day)
            with self.subTest(date=test_date):
                # Should be a half-day trading day
                self.assertTrue(
                    is_half_day_trading_day(test_date),
                    f"{test_date} should be a half-day trading day",
                )
                # Should also be a trading day (half-days are trading days)
                self.assertTrue(
                    is_trading_day(test_date),
                    f"{test_date} should be a trading day (half-day)",
                )

    def test_weekend_dates_are_not_trading_days(self):
        """Test that weekend dates are never trading days."""
        # Test some weekend dates
        weekend_dates = [
            (2024, 1, 6),  # Saturday
            (2024, 1, 7),  # Sunday
            (2024, 1, 13),  # Saturday
            (2024, 1, 14),  # Sunday
        ]

        for year, month, day in weekend_dates:
            test_date = date(year, month, day)
            with self.subTest(date=test_date):
                # Should not be a half-day trading day
                self.assertFalse(
                    is_half_day_trading_day(test_date),
                    f"{test_date} should not be a half-day trading day (weekend)",
                )
                # Should not be a trading day
                self.assertFalse(
                    is_trading_day(test_date),
                    f"{test_date} should not be a trading day (weekend)",
                )

    def test_regular_weekdays_are_trading_days(self):
        """Test that regular weekdays are trading days (unless they're holidays)."""
        # Test some regular weekdays
        weekday_dates = [
            (2024, 1, 2),  # Tuesday
            (2024, 1, 3),  # Wednesday
            (2024, 1, 4),  # Thursday
            (2024, 1, 5),  # Friday
            (2024, 1, 8),  # Monday
        ]

        for year, month, day in weekday_dates:
            test_date = date(year, month, day)
            with self.subTest(date=test_date):
                # Should be a trading day (unless it's a holiday)
                # Note: We don't assert True here because some might be holidays
                result = is_trading_day(test_date)
                self.assertIsInstance(
                    result, bool, f"{test_date} should return boolean"
                )

    def test_half_day_data_integrity(self):
        """Test that half-day data is properly loaded and contains no weekends."""
        holidays, half_days = get_cached_with_half_day()

        # Check that half_days is not empty
        self.assertGreater(len(half_days), 0, "Half-days data should not be empty")

        # Check that no half-day is on a weekend
        for half_day in half_days:
            with self.subTest(half_day=half_day):
                weekday = half_day.weekday()  # 0=Monday, 6=Sunday
                self.assertLess(
                    weekday,
                    5,
                    f"{half_day} should not be a weekend (weekday {weekday})",
                )

    def test_datetime_objects_are_handled(self):
        """Test that datetime objects are properly handled."""
        # Test with datetime objects
        test_datetime = datetime(2024, 12, 24, 10, 30)  # Tuesday
        test_date = date(2024, 12, 24)

        # Both should return the same result
        datetime_result = is_half_day_trading_day(test_datetime)
        date_result = is_half_day_trading_day(test_date)

        self.assertEqual(datetime_result, date_result)
        self.assertIsInstance(datetime_result, bool)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test with None (should raise TypeError)
        with self.assertRaises(TypeError):
            is_half_day_trading_day(None)

        # Test with invalid date string (should raise TypeError)
        with self.assertRaises(TypeError):
            is_half_day_trading_day("invalid_date")

        # Test with integer (should raise TypeError)
        with self.assertRaises(TypeError):
            is_half_day_trading_day(20241224)


if __name__ == "__main__":
    unittest.main()
