#coding:utf-8

"""
Help functions for python to get Hongkong stock exchange holidays
"""
from cn_stock_holidays.meta_functions import *

DATA_FILE_FOR_HK = "data_hk.txt"

get_local = meta_get_local(data_file_name=DATA_FILE_FOR_HK)
get_cache_path = meta_get_cache_path(data_file_name=DATA_FILE_FOR_HK)

@function_cache
def get_cached(use_list=False):
    return meta_get_cached(get_local=get_local, get_cache_path=get_cache_path)(use_list=False)

get_remote_and_cache = meta_get_remote_and_cache(get_cached=get_cached, get_cache_path=get_cache_path)
check_expired = meta_check_expired(get_cached=get_cached)
sync_data = meta_sync_data(check_expired=check_expired, get_remote_and_cache=get_remote_and_cache)
is_trading_day = meta_is_trading_day(get_cached=get_cached)
previous_trading_day = meta_previous_trading_day(is_trading_day=is_trading_day)
next_trading_day = meta_next_trading_day(is_trading_day=is_trading_day)
trading_days_between = meta_trading_days_between(get_cached=get_cached)


if __name__ == '__main__':
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

    print("previous trading day after today?")
    data = previous_trading_day(datetime.date.today())
    print_result(data)

    print("Test loop 100000")
    trade_days = datetime.date.today()
    for i in range(100000):
        trade_days = previous_trading_day(trade_days)
