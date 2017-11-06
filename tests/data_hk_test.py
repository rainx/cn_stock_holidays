#coding: utf-8

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

        self.assertTrue(datetime.date(2000, 12, 25) in data, "get datetime.date(2000, 12, 25) in cached data")


    def test_trading_days_between(self):
        data = list(trading_days_between(int_to_date(20170125), int_to_date(20170131)))

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