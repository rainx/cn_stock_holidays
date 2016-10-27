"""
Help functions for python to get china stock exchange holidays
"""


import os
import datetime
import requests



def get_local():
    """
    read data from package data file
    :return: a list contains all holiday data, element with datatime.date format
    """
    datafilepath = os.path.join(os.path.dirname(__file__), 'data.txt')
    return _get_from_file(datafilepath)

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
        print("trying to fetch data...")
        get_remote_and_cache()
        print("done")
    else:
        print("local data is not exipired, do not fetch new data")

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

if __name__ == '__main__':
    data = check_expired()
    #data = get_cached()

    print(data)