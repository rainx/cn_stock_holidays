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

else:  # suppose it is 3 or larger
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
    with open(filename, "r") as f:
        data = f.readlines()
        # Filter out empty lines and comments
        filtered_data = [
            i.rstrip("\n") for i in data if i.strip() and not i.strip().startswith("#")
        ]
        # Process dates, handling both regular and half-day format
        processed_data = []
        for i in filtered_data:
            if i.endswith(",h"):
                # For half-day trading days, treat them as regular holidays for backward compatibility
                processed_data.append(i[:-2])  # Remove ',h' suffix
            else:
                processed_data.append(i)

        if use_list:
            return [int_to_date(str_to_int(i)) for i in processed_data]
        else:
            return set([int_to_date(str_to_int(i)) for i in processed_data])
    if use_list:
        return []
    else:
        return set([])


def _get_from_file_with_half_day(filename, use_list=False):
    """
    Read data from file with support for half-day trading format.
    Lines with 'h' suffix (e.g., '20251225,h') indicate half-day trading days.
    Returns a tuple: (holidays_set, half_day_set)
    """
    holidays = set()
    half_days = set()

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if line.endswith(",h"):
                    # Half-day trading day
                    date_str = line[:-2]  # Remove ',h' suffix
                    half_days.add(int_to_date(str_to_int(date_str)))
                else:
                    # Regular holiday
                    holidays.add(int_to_date(str_to_int(line)))
    except FileNotFoundError:
        pass

    if use_list:
        return list(holidays), list(half_days)
    else:
        return holidays, half_days
