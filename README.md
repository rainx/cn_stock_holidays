# cn_stock_holidays


[![Build Status](https://travis-ci.org/rainx/cn_stock_holidays.svg?branch=master)](https://travis-ci.org/rainx/cn_stock_holidays)

## 数据文件 (File Path)

沪深市场

```
cn_stock_holidays/data.txt
```

香港市场

```
cn_stock_holidays/data_hk.txt
```


Fetch Data via URL :

```
wget https://raw.githubusercontent.com/rainx/cn_stock_holidays/master/cn_stock_holidays/data.txt

or

curl https://raw.githubusercontent.com/rainx/cn_stock_holidays/master/cn_stock_holidays/data.txt
```


## 文件内容 ( File Content)

保存除了周六日休市之外，其它休市信息，换行分割

store all (even upcoming) holiday for china stock exchange (without regular market close date on Saturday Day and Sun Day ) , one date per line

## 格式(File Format)
```
YYYYMMDD
```

## Python version

```
pip install cn-stock-holidays
```

or

```
pip install git+https://github.com/rainx/cn_stock_holidays.git
```

### 导入

```python

# 针对沪深
import cn_stock_holidays.data as shsz

# 针对香港
import cn_stock_holidays.data_hk as hkex

```

### Functions

```python
Help on module cn_stock_holidays.data in cn_stock_holidays:

NAME
    cn_stock_holidays.data - Help functions for python to get china stock exchange holidays

FILE
    /Users/rainx/dev/cn_stock_holidays/cn_stock_holidays/data.py

FUNCTIONS
    check_expired()
        check if local or cached data need update
        :return: true/false

    date_to_int(da)

    date_to_str(da)

    get_cache_path()

    get_cached()
        get from cache version , if it is not exising , use txt file in package data
        :return: a list contains all holiday data, element with datatime.date format

    get_local()
        read data from package data file
        :return: a list contains all holiday data, element with datatime.date format

    get_remote_and_cache()
        get newest data file from network and cache on local machine
        :return: a list contains all holiday data, element with datatime.date format

    int_to_date(d)

    str_to_int(s)

    sync_data()


    is_trading_day(dt)
        param dt: datetime.datetime or datetime.date.
        is a trading day or not
        :returns: Bool

    previous_trading_day(dt):
        param dt: datetime.datetime or datetime.date.
        get previous trading day
        :returns: datetime.date

    next_trading_day(dt):
        param dt: datetime.datetime or datetime.date.
        get next trading day
        :returns: datetime.date

    trading_days_between(start, end):

        param start, end: start and end time , datetime.datetime or datetime.date
        get calendar data range
        :returns: a generator for available dates for chinese market included start and end date
```

### about function cache

from version 0.10 on, we used functools.lrucache on `get_cached` for getting more speech, 
if needed you can used the following syntax to clear cache.

```python
get_cached.cache_clear()  

```


### Keep it up-to-date

we had a script to check the expired of the data and fetch the data from web.

you could set it up on cron job

```crontab
0 0 * * * /usr/local/bin/cn-stock-holiday-sync > /tmp/cn_stock_holiday_sync.log
```

You could get the absolute path of cn-stock-holiday-sync by which command

沪深
```bash
which cn-stock-holiday-sync
```
香港
```bash
which cn-stock-holiday-sync-hk
```
