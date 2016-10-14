from datetime import time
from ..data import get_cached
from pandas import Timestamp, date_range, DatetimeIndex
import pytz
from zipline.utils.memoize import remember_last, lazyval
import warnings

from zipline.utils.calendars import TradingCalendar
from zipline.utils.calendars.trading_calendar import days_at_time, NANOS_IN_MINUTE
import numpy as np
import pandas as pd

# lunch break for shanghai and shenzhen exchange
lunch_break_start = time(11, 30)
lunch_break_end = time(13, 1)

start_default = pd.Timestamp('1990-12-19', tz='UTC')
end_base = pd.Timestamp('today', tz='UTC')
end_default = end_base + pd.Timedelta(days=365)

class SHSZExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for Shanghai and Shenzhen (China Market)
    Open Time 9:31 AM, Asia/Shanghai
    Close Time 3:00 PM, Asia/Shanghai

    One big difference between china and us exchange is china exchange has a lunch break , so I handle it

    Sample Code in ipython:

    > from zipline.utils.calendars import *
    > from cn_stock_holidays.zipline.exchange_calendar_shsz import SHSZExchangeCalendar
    > register_calendar("SHSZ", SHSZExchangeCalendar(), force=True)
    > c=get_calendar("SHSZ")

    for the guy need to keep updating about holiday file, try to add `cn-stock-holiday-sync` command to crontab
    """

    def __init__(self, start=start_default, end=end_default):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            _all_days = date_range(start, end, freq=self.day, tz='UTC')

        self._lunch_break_starts = days_at_time(_all_days, lunch_break_start, self.tz, 0)
        self._lunch_break_ends = days_at_time(_all_days, lunch_break_end, self.tz, 0)

        TradingCalendar.__init__(self, start=start_default, end=end_default)


    @property
    def name(self):
        return "SHSZ"

    @property
    def tz(self):
        return pytz.timezone("Asia/Shanghai")

    @property
    def open_time(self):
        return time(9, 31)

    @property
    def close_time(self):
        return time(15, 00)

    @property
    def adhoc_holidays(self):
        return [Timestamp(t,tz=pytz.UTC) for t in get_cached()]


    @property
    @remember_last
    def all_minutes(self):
        """
            Returns a DatetimeIndex representing all the minutes in this calendar.
        """
        opens_in_ns = \
            self._opens.values.astype('datetime64[ns]')

        closes_in_ns = \
            self._closes.values.astype('datetime64[ns]')

        lunch_break_start_in_ns = \
            self._lunch_break_starts.values.astype('datetime64[ns]')
        lunch_break_ends_in_ns = \
            self._lunch_break_ends.values.astype('datetime64[ns]')

        deltas_before_lunch = lunch_break_start_in_ns - opens_in_ns
        deltas_after_lunch = closes_in_ns - lunch_break_ends_in_ns

        daily_before_lunch_sizes = (deltas_before_lunch / NANOS_IN_MINUTE) + 1
        daily_after_lunch_sizes = (deltas_after_lunch / NANOS_IN_MINUTE) + 1

        daily_sizes = daily_before_lunch_sizes + daily_after_lunch_sizes

        num_minutes = np.sum(daily_sizes).astype(np.int64)

        # One allocation for the entire thing. This assumes that each day
        # represents a contiguous block of minutes.
        all_minutes = np.empty(num_minutes, dtype='datetime64[ns]')

        idx = 0
        for day_idx, size in enumerate(daily_sizes):
            # lots of small allocations, but it's fast enough for now.

            # size is a np.timedelta64, so we need to int it
            size_int = int(size)

            before_lunch_size_int = int(daily_after_lunch_sizes[day_idx])
            after_lunch_size_int = int(daily_after_lunch_sizes[day_idx])

            all_minutes[idx:(idx + before_lunch_size_int)] = \
                np.arange(
                    opens_in_ns[day_idx],
                    lunch_break_start_in_ns[day_idx] + NANOS_IN_MINUTE,
                    NANOS_IN_MINUTE
                )

            all_minutes[(idx + before_lunch_size_int):(idx + size_int)] = \
                np.arange(
                    lunch_break_ends_in_ns[day_idx],
                    closes_in_ns[day_idx] + NANOS_IN_MINUTE,
                    NANOS_IN_MINUTE
                )

            idx += size_int
        return DatetimeIndex(all_minutes).tz_localize("UTC")