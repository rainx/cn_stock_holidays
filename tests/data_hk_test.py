# coding: utf-8

import unittest

from cn_stock_holidays.data_hk import *


class TestHkData(unittest.TestCase):
    def test_get_cached(self):
        """
        get cached related
        """
        data = get_cached()
        data2 = get_cached()

        self.assertEqual(str(data), str(data2), "get_cached 2 times give some results")

        self.assertGreater(len(data), 0, "is greater then 0")

        self.assertIsInstance(list(data)[0], datetime.date, "is a date")

        self.assertTrue(
            datetime.date(2000, 12, 25) in data,
            "get datetime.date(2000, 12, 25) in cached data",
        )

    def test_trading_days_between(self):
        is_trading_day.cache_clear()
        get_cached_with_half_day.cache_clear()

        # Debug: check what holidays and half_days contain
        holidays, half_days = get_cached_with_half_day()
        print("DEBUG holidays containing 20170126:", int_to_date(20170126) in holidays)
        print(
            "DEBUG half_days containing 20170126:", int_to_date(20170126) in half_days
        )

        data = list(trading_days_between(int_to_date(20170125), int_to_date(20170131)))

        print("DEBUG trading_days_between result:", data)
        print("DEBUG is_trading_day(20170125):", is_trading_day(int_to_date(20170125)))
        print("DEBUG is_trading_day(20170126):", is_trading_day(int_to_date(20170126)))
        print("DEBUG is_trading_day(20170127):", is_trading_day(int_to_date(20170127)))
        print("DEBUG is_trading_day(20170130):", is_trading_day(int_to_date(20170130)))
        print("DEBUG is_trading_day(20170131):", is_trading_day(int_to_date(20170131)))

        self.assertEqual(len(data), 3)
        self.assertTrue(int_to_date(20170125) in data)
        self.assertTrue(int_to_date(20170126) in data)
        self.assertTrue(int_to_date(20170127) in data)

    def test_is_trading_day(self):
        self.assertIsNotNone(is_trading_day(datetime.date.today()))

    def test_next_trading_day(self):
        data = next_trading_day(datetime.date.today())
        self.assertGreater(data, datetime.date.today())

    def test_previous_trading_day(self):
        data = previous_trading_day(datetime.date.today())
        self.assertLess(data, datetime.date.today())

    def test_cache_clear(self):
        data = get_cached()
        get_cached.cache_clear()
        data2 = get_cached()
        self.assertEqual(str(data), str(data2), "get_cached 2 times give some results")

    def test_loop_100000(self):
        trade_days = datetime.date.today()
        for i in range(100000):
            trade_days = previous_trading_day(trade_days)

        self.assertIsInstance(trade_days, datetime.date)

    def test_half_day_trading_functionality(self):
        """
        Test the new half-day trading functionality
        """
        import cn_stock_holidays.data_hk as data_hk

        self.assertTrue(hasattr(data_hk, "is_half_day_trading_day"))

        # Test with today's date
        result = is_half_day_trading_day(datetime.date.today())
        self.assertIsInstance(result, bool)

        # Test with a datetime object
        result = is_half_day_trading_day(datetime.datetime.now())
        self.assertIsInstance(result, bool)

        # Test that half-day trading days are also trading days
        holidays, half_days = get_cached_with_half_day()
        if half_days:
            sample_half_day = list(half_days)[0]
            print(f"DEBUG sample_half_day: {sample_half_day}")
            print(f"DEBUG is_trading_day meta info: {is_trading_day.__code__}")
            self.assertTrue(is_trading_day(sample_half_day))
            self.assertTrue(is_half_day_trading_day(sample_half_day))
