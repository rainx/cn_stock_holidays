#coding: utf-8
"""
Help functions for python to get china stock exchange holidays
"""


import os
import datetime
import requests
import logging
import sys
from functools import wraps


# make a function_cache for both 2 and 3
if sys.version_info.major == 2:
    def function_cache(function):
        memo = {}

        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv

        return wrapper

else: # suppose it is 3 or larger
    from functools import lru_cache
    function_cache = lru_cache(None)


def get_local():
    """
    read data from package data file
    :return: a list contains all holiday data, element with datatime.date format
    """
    datafilepath = os.path.join(os.path.dirname(__file__), 'data.txt')
    return _get_from_file(datafilepath)

@function_cache
def get_cached():
    """
    get from cache version , if it is not exising , use txt file in package data
    :return: a list contains all holiday data, element with datatime.date format
    """
    cache_path = get_cache_path()

    if (os.path.isfile(cache_path)):
        return _get_from_file(cache_path)
    else:
        return get_local()

def get_remote_and_cache():
    """
    get newest data file from network and cache on local machine
    :return: a list contains all holiday data, element with datatime.date format
    """
    response = requests.get('https://raw.githubusercontent.com/rainx/cn_stock_holidays/master/cn_stock_holidays/data.txt')
    cache_path = get_cache_path()

    with open(cache_path, 'wb') as f:
        f.write(response.content)

    return get_cached()

def check_expired():
    """
    check if local or cached data need update
    :return: true/false
    """
    data = get_cached()
    now = datetime.datetime.now().date()
    for d in data:
        if d > now:
            return False
    return True

def sync_data():
    if check_expired():
        logging.info("trying to fetch data...")
        get_remote_and_cache()
        logging.info("done")
    else:
        logging.info("local data is not exipired, do not fetch new data")

def _get_from_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        return [int_to_date(str_to_int(i.rstrip('\n'))) for i in data]
    return []

def get_cache_path():
    usr_home = os.path.expanduser('~')
    cache_dir = os.path.join(usr_home, '.cn_stock_holidays')
    if not(os.path.isdir(cache_dir)):
        os.mkdir(cache_dir)
    return os.path.join(cache_dir, 'data.txt')

def int_to_date(d):
    d = str(d)
    return datetime.date(int(d[:4]), int(d[4:6]), int(d[6:]))

def date_to_str(da):
    return da.strftime("%Y%m%d")

def str_to_int(s):
    return int(s)

def date_to_int(da):
    return str_to_int(date_to_str(da))

def is_trading_day(dt):
    if type(dt) is datetime.datetime:
        dt = dt.date()

    if dt.weekday() >= 5:
        return False
    holidays = get_cached()
    if dt in holidays:
        return False
    return True

def previous_trading_day(dt):
    if type(dt) is datetime.datetime:
        dt = dt.date()

    while True:
        dt = dt - datetime.timedelta(days=1)
        if is_trading_day(dt):
            return dt

def next_trading_day(dt):
    if type(dt) is datetime.datetime:
        dt = dt.date()

    while True:
        dt = dt + datetime.timedelta(days=1)
        if is_trading_day(dt):
            return dt


def trading_days_between(start, end):
    # 为了更快的遍历，我们使用 set 结构
    if type(start) is datetime.datetime:
        start = start.date()

    if type(end) is datetime.datetime:
        end = end.date()

    dataset = set(get_cached())
    if start > end:
        return
    curdate = start
    while curdate <= end:
        if curdate.weekday() < 5 and not(curdate in dataset):
            yield curdate
        curdate = curdate + datetime.timedelta(days=1)


if __name__ == '__main__':
    data = check_expired()

    def print_result(s):
        print("-" * 20)
        print("*" + str(s) + "*")
        print("-" * 20)
        print("")

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
