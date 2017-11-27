# coding=utf-8
from WindPy import *
from pandas.tseries.offsets import CustomBusinessDay
import pandas as pd

# 结束日期可以超过当前年份，但是wind拿到的数据不准确，准确的只有到当年结束
start_date = "1990-01-01"
end_date = "2050-12-31"

w.start()
data = w.tdays(start_date, end_date, "")
df = pd.DataFrame(data.Data[0])

start_date, end_date = df[0].iloc[[0, -1]]

weekmask = 'Mon Tue Wed Thu Fri'
Cbd = CustomBusinessDay(weekmask=weekmask)
dts = pd.date_range(start_date, end_date, freq=Cbd)
res = pd.DataFrame({"date": list(set(dts.to_series()) - set(df[0]))}).sort_values('date')
res['date'].to_csv('data.txt', index=False, date_format='%Y%m%d')
