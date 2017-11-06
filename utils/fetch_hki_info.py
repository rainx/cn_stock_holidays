import requests
from datetime import datetime, date, timedelta
import logging
import re
import pprint
from bs4 import BeautifulSoup
import pickle


logging.getLogger().setLevel(logging.INFO)


"""
Post

curr_id:179
smlID:2030179
header:香港恒生指数 历史数据
st_date:2016/09/01
end_date:2016/10/15
interval_sec:Daily
sort_col:date
sort_ord:DESC
action:historical_data

request header

Accept:text/plain, */*; q=0.01
Accept-Encoding:gzip, deflate, br
Accept-Language:en-US,en;q=0.8,ja;q=0.6,zh-CN;q=0.4,zh-TW;q=0.2
AlexaToolbar-ALX_NS_PH:AlexaToolbar/alx-4.0.1
Connection:keep-alive
Content-Length:241
Content-Type:application/x-www-form-urlencoded
Cookie:PHPSESSID=99bi3ijfc6lr57g7ip0ucrp7t2; adBlockerNewUserDomains=1509586565; StickySession=id.79167722689.947.cn.investing.com; __gads=ID=3f05c6772412c678:T=1509586569:S=ALNI_Ma13aiOjNZi9cExUYo9oWr7qh-y0A; _VT_content_503663_2=1; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22179%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Findices%2Fhang-sen-40%22%3B%7D%7D%7D%7D; geoC=CN; billboardCounter_6=2; nyxDorf=NzMxfDFlZjpiNm1%2FNGUwNzNjZCE3MWVhMjE%3D; _ga=GA1.2.206550762.1509586569; _gid=GA1.2.1312498628.1509586569; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1509586569,1509615321,1509615504,1509687206; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1509687206
Host:cn.investing.com
Origin:https://cn.investing.com
Referer:https://cn.investing.com/indices/hang-sen-40-historical-data
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
X-Requested-With:XMLHttpRequest
"""


def fetch_hsi(start, end):
    """
    :param start:  2016/09/01
    :param end: 2016/10/15
    :return: a list of elements
        per element:
             {'amount': '1.47B',
              'chg': '-0.53%',
              'h': '28,356.10',
              'l': '28,098.83',
              'o': '28,232.62',
              'price': '28,154.97',
              'trade_date': '2017年10月24日'}
    """

    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    res = s.get("https://cn.investing.com/indices/hang-sen-40-historical-data")
    content = res.text

    ro = re.search(r"window.siteData.smlID = (\d+);", content)
    sml_id = ro.group(1)

    ro = re.search(r"pairId: (\d+),", content)
    curr_id = ro.group(1)

    start = parse_date(start)
    end = parse_date(end)

    post_data = {
        "curr_id": curr_id,
        "smlID": sml_id,
        "header": "香港恒生指数 历史数据",
        "st_date": start,
        "end_date": end,
        "interval_sec": "Daily",
        "sort_col": "date",
        "sort_ord": "ASC",
        "action": "historical_data",
    }

    # headers = {one.split(":")[0]:one.split(":")[1] for one in request_header.split("\n") if one.strip("") != ""}

    #logging.info("posting data")
    #pprint.pprint(post_data)
    s.headers['Referer'] = 'https://cn.investing.com/indices/hang-sen-40-historical-data'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'
    response = s.post("https://cn.investing.com/instruments/HistoricalDataAjax", data=post_data)
    result = response.text
    soup = BeautifulSoup(result, "lxml")
    tbody = soup.find("tbody")

    lines = []
    trade_dates = []

    for tr in tbody.find_all("tr"):
        if tr.name != 'tr':
            continue

        c = tr.find_all("td")

        # print(c)
        if c and len(c) >= 1 and c[0].has_attr("colspan"):
            # No results found...
            logging.info("no value ,skipping!!")
            break

        trade_date = c[0].string
        price = c[1].string
        o = c[2].string
        h = c[3].string
        l = c[4].string
        amount = c[5].string
        chg = c[6].string

        trade_dates.append(trade_date)

        lines.append({
            "trade_date": trade_date,
            "price": price,
            "o": o,
            "h": h,
            "l": l,
            "amount": amount,
            "chg": chg
        })

    return lines, trade_dates


def parse_date(d: datetime):
    if type(d) is datetime or type(d) is date:
        return d.strftime("%Y/%m/%d")
    else:
        return d


if __name__ == __name__:
    """
    找出历史行情中所有信息
    """
    start = date(2000, 1, 1)
    end = datetime.today().date()

    offset = start
    results = []
    trade_dates=[]
    while offset < end:
        offset_end = offset + timedelta(days=30)
        if offset_end > end:
            offset_end = end
        chunk, chunk_trade_dates = fetch_hsi(offset, offset_end)
        offset = offset_end
        results += chunk
        trade_dates += chunk_trade_dates
        logging.info("process 30 days , really data len is {} now offset to {}".format(len(chunk), offset))

    pickle.dump(trade_dates, open("./trade_dates", "wb"))
    pickle.dump(results, open("./hki.pickle", "wb"))




