# coding:utf-8

"""
Help functions for python to get Hongkong stock exchange holidays
"""

from cn_stock_holidays.meta_functions import *

DATA_FILE_FOR_HK = "data_hk.txt"

get_local = meta_get_local(data_file_name=DATA_FILE_FOR_HK)
get_cache_path = meta_get_cache_path(data_file_name=DATA_FILE_FOR_HK)

# Half-day trading support
get_local_with_half_day = meta_get_local_with_half_day(data_file_name=DATA_FILE_FOR_HK)


@function_cache
def get_cached(use_list=False):
    return meta_get_cached(get_local=get_local, get_cache_path=get_cache_path)(
        use_list=False
    )


@function_cache
def get_cached_with_half_day(use_list=False):
    return meta_get_cached_with_half_day(
        get_local_with_half_day=get_local_with_half_day, get_cache_path=get_cache_path
    )(use_list=False)


get_remote_and_cache = meta_get_remote_and_cache(
    get_cached=get_cached, get_cache_path=get_cache_path
)
check_expired = meta_check_expired(get_cached=get_cached)
sync_data = meta_sync_data(
    check_expired=check_expired, get_remote_and_cache=get_remote_and_cache
)
is_trading_day = meta_is_trading_day(get_cached=get_cached)
previous_trading_day = meta_previous_trading_day(is_trading_day=is_trading_day)
next_trading_day = meta_next_trading_day(is_trading_day=is_trading_day)

# Half-day trading functions
get_remote_and_cache_with_half_day = meta_get_remote_and_cache_with_half_day(
    get_cached_with_half_day=get_cached_with_half_day,
    get_cache_path=get_cache_path,
    data_file_name=DATA_FILE_FOR_HK,
)
check_expired_with_half_day = meta_check_expired_with_half_day(
    get_cached_with_half_day=get_cached_with_half_day
)
sync_data_with_half_day = meta_sync_data_with_half_day(
    check_expired_with_half_day=check_expired_with_half_day,
    get_remote_and_cache_with_half_day=get_remote_and_cache_with_half_day,
)
is_half_day_trading_day = meta_is_half_day_trading_day(
    get_cached_with_half_day=get_cached_with_half_day
)


# Override is_trading_day for HK to treat both normal and half-day trading days as trading days
def is_trading_day(dt):
    if type(dt) is datetime.datetime:
        dt = dt.date()
    if dt.weekday() >= 5:
        return False
    holidays, _half_days = get_cached_with_half_day()
    if dt in holidays:
        return False
    return True


is_trading_day.cache_clear = lambda: get_cached_with_half_day.cache_clear()


# Override trading_days_between for HK to treat both normal and half-day trading days as trading days
def trading_days_between(start, end):
    if type(start) is datetime.datetime:
        start = start.date()
    if type(end) is datetime.datetime:
        end = end.date()
    holidays, _half_days = get_cached_with_half_day()
    if start > end:
        return
    curdate = start
    while curdate <= end:
        if curdate.weekday() < 5 and curdate not in holidays:
            yield curdate
        curdate = curdate + datetime.timedelta(days=1)


if __name__ == "__main__":
    data = check_expired()

    print("get datetime.date(1991, 2, 15) in cached data")
    data = get_cached()
    print_result(datetime.date(1991, 2, 15) in data)

    print("test trading_days_between 20170125 to 20170131")
    data = list(trading_days_between(int_to_date(20170125), int_to_date(20170131)))
    print_result(data)

    print("is trading day today?")
    data = is_trading_day(datetime.date.today())
    print_result(data)

    print("next trading day after today?")
    data = next_trading_day(datetime.date.today())
    print_result(data)

    print("previous trading day before today?")
    data = previous_trading_day(datetime.date.today())
    print_result(data)

    print("Test loop 100000")
    trade_days = datetime.date.today()
    for i in range(100000):
        trade_days = previous_trading_day(trade_days)

    # Test half-day trading functionality
    print("test half-day trading functionality")
    holidays, half_days = get_cached_with_half_day()
    print_result(f"Total holidays: {len(holidays)}, Total half-days: {len(half_days)}")

    if half_days:
        sample_half_day = list(half_days)[0]
        print(f"Sample half-day: {sample_half_day}")
        print_result(is_half_day_trading_day(sample_half_day))
