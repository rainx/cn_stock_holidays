import datetime
from functools import wraps
import sys



if sys.version_info.major == 2:
    def function_cache(function):
        memo = {}

        @wraps(function)
        def wrapper(*args, **kwargs):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args, **kwargs)
                memo[args] = rv
                return rv

        def cache_clear():
            global memo
            memo = {}

        wrapper.cache_clear = cache_clear
        return wrapper
else: # suppose it is 3 or larger
    from functools import lru_cache
    function_cache = lru_cache(None, typed=True)


def int_to_date(d):
    d = str(d)
    return datetime.date(int(d[:4]), int(d[4:6]), int(d[6:]))

def date_to_str(da):
    return da.strftime("%Y%m%d")

def str_to_int(s):
    return int(s)

def date_to_int(da):
    return str_to_int(date_to_str(da))


def print_result(s):
    print("-" * 20)
    print("*" + str(s) + "*")
    print("-" * 20)
    print("")


def _get_from_file(filename, use_list=False):
    with open(filename, 'r') as f:
        data = f.readlines()
        if use_list:
            return [int_to_date(str_to_int(i.rstrip('\n'))) for i in data]
        else:
            return set([int_to_date(str_to_int(i.rstrip('\n'))) for i in data])
    if use_list:
        return []
    else:
        return set([])