#coding: utf-8

import logging
import pickle
from functools import reduce

from cn_stock_holidays.common import date_to_str
from cn_stock_holidays.data import *

logging.getLogger().setLevel(logging.INFO)


data = pickle.load(open("./trade_dates", 'rb'))

simple_dates = [datetime.datetime.strptime(d, r"%Y年%m月%d日").date() for d in data]
start = reduce(lambda x, y: x if x < y else y, simple_dates)

today = datetime.date.today()


# 找出offset 开始所有的非周六日的假期
offset = start

holidays = []
while offset < today:

    current = offset
    offset = offset + datetime.timedelta(days=1)

    if current.weekday() == 5 or current.weekday() == 6:
        logging.info("{} is weekend".format(current))
        continue

    if current in simple_dates:
        logging.info("{} is in trade day".format(current))
        continue

    logging.info("{} is holiday".format(current))
    holidays.append(current)


holidays_str = [date_to_str(da) for da in holidays]

with open("data_hk.txt", "w") as hk:
    hk.write("\n".join(holidays_str))




