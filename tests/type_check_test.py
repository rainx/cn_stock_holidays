# coding: utf-8
"""
Tests for strict type checking in trading day functions.
Ensures that only exact datetime.date and datetime.datetime types are accepted,
and subclasses (e.g., pd.Timestamp) are rejected with TypeError.
See: https://github.com/rainx/cn_stock_holidays/pull/20
"""

import datetime
import unittest

from cn_stock_holidays.data import (
    is_trading_day,
    next_trading_day,
    previous_trading_day,
    trading_days_between,
)
from cn_stock_holidays.data_hk import (
    is_half_day_trading_day as hk_is_half_day_trading_day,
)
from cn_stock_holidays.data_hk import is_trading_day as hk_is_trading_day
from cn_stock_holidays.data_hk import next_trading_day as hk_next_trading_day
from cn_stock_holidays.data_hk import previous_trading_day as hk_previous_trading_day
from cn_stock_holidays.data_hk import trading_days_between as hk_trading_days_between


class DateTimeSubclass(datetime.datetime):
    """Simulates pd.Timestamp or other datetime.datetime subclasses."""

    pass


class DateSubclass(datetime.date):
    """Simulates subclasses of datetime.date."""

    pass


# A known trading day (Wednesday)
KNOWN_TRADING_DATE = datetime.date(2024, 1, 3)
KNOWN_TRADING_DATETIME = datetime.datetime(2024, 1, 3, 10, 30, 0)


class TestStrictTypeCheckSHSZ(unittest.TestCase):
    """Strict type checking for Shanghai/Shenzhen market functions."""

    def test_is_trading_day_accepts_date(self):
        result = is_trading_day(KNOWN_TRADING_DATE)
        self.assertTrue(result)

    def test_is_trading_day_accepts_datetime(self):
        result = is_trading_day(KNOWN_TRADING_DATETIME)
        self.assertTrue(result)

    def test_is_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            is_trading_day(dt)

    def test_is_trading_day_rejects_date_subclass(self):
        dt = DateSubclass(2024, 1, 3)
        with self.assertRaises(TypeError):
            is_trading_day(dt)

    def test_is_trading_day_rejects_none(self):
        with self.assertRaises(TypeError):
            is_trading_day(None)

    def test_is_trading_day_rejects_string(self):
        with self.assertRaises(TypeError):
            is_trading_day("2024-01-03")

    def test_is_trading_day_rejects_int(self):
        with self.assertRaises(TypeError):
            is_trading_day(20240103)

    def test_previous_trading_day_accepts_date(self):
        result = previous_trading_day(KNOWN_TRADING_DATE)
        self.assertIsInstance(result, datetime.date)
        self.assertLess(result, KNOWN_TRADING_DATE)

    def test_previous_trading_day_accepts_datetime(self):
        result = previous_trading_day(KNOWN_TRADING_DATETIME)
        self.assertIsInstance(result, datetime.date)

    def test_previous_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            previous_trading_day(dt)

    def test_next_trading_day_accepts_date(self):
        result = next_trading_day(KNOWN_TRADING_DATE)
        self.assertIsInstance(result, datetime.date)
        self.assertGreater(result, KNOWN_TRADING_DATE)

    def test_next_trading_day_accepts_datetime(self):
        result = next_trading_day(KNOWN_TRADING_DATETIME)
        self.assertIsInstance(result, datetime.date)

    def test_next_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            next_trading_day(dt)

    def test_trading_days_between_accepts_date(self):
        start = datetime.date(2024, 1, 2)
        end = datetime.date(2024, 1, 5)
        result = list(trading_days_between(start, end))
        self.assertGreater(len(result), 0)

    def test_trading_days_between_accepts_datetime(self):
        start = datetime.datetime(2024, 1, 2, 9, 0)
        end = datetime.datetime(2024, 1, 5, 15, 0)
        result = list(trading_days_between(start, end))
        self.assertGreater(len(result), 0)


class TestStrictTypeCheckHK(unittest.TestCase):
    """Strict type checking for Hong Kong market functions."""

    def test_is_trading_day_accepts_date(self):
        result = hk_is_trading_day(KNOWN_TRADING_DATE)
        self.assertIsInstance(result, bool)

    def test_is_trading_day_accepts_datetime(self):
        result = hk_is_trading_day(KNOWN_TRADING_DATETIME)
        self.assertIsInstance(result, bool)

    def test_is_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            hk_is_trading_day(dt)

    def test_is_trading_day_rejects_date_subclass(self):
        dt = DateSubclass(2024, 1, 3)
        with self.assertRaises(TypeError):
            hk_is_trading_day(dt)

    def test_is_half_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            hk_is_half_day_trading_day(dt)

    def test_is_half_day_rejects_date_subclass(self):
        dt = DateSubclass(2024, 1, 3)
        with self.assertRaises(TypeError):
            hk_is_half_day_trading_day(dt)

    def test_previous_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            hk_previous_trading_day(dt)

    def test_next_trading_day_rejects_datetime_subclass(self):
        dt = DateTimeSubclass(2024, 1, 3, 10, 30, 0)
        with self.assertRaises(TypeError):
            hk_next_trading_day(dt)


if __name__ == "__main__":
    unittest.main()
