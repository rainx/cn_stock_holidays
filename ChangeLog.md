1.12 2024年12月3日
--
* 更新了2024年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>

1.11 2023年12月25日
--
* 更新了2024年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>
 
1.10 2022年12月16日
--
* 更新了2023年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>

1.9 2021年12月30日
---

* 更新了2022年国内股市节假日 <https://www.tdx.com.cn/url/holiday/>

1.8 2020年12月25日
---

* 更新了2021年国内股市节假日 <https://www.tdx.com.cn/url/holiday/>

1.7 2020年1月31日
---

* 受2019-nCoV影响，变更2020年的股市日历, 追加 2020年1月31日

1.6 2019年12月6日
---

* 修复一处错误20090101 -> 20190101, thanks @liuyug #8
  
1.5 2019年11月26日
---

* 更新2020年中国市场休假数据 ref: <https://www.tdx.com.cn/url/holiday/>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).join("\n")
```

* 更新2019，2020年香港股市休市数据 ref: <https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Calendar-and-Holiday-Schedule?sc_lang=en>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).filter(e=>e.includes("/")).map(e=> moment(e, "D/M/YYYY").format("YYYYMMDD")).join("\n")
```

1.4 2019年1月8日
---

* 更新2019年中国市场假期数据

1.3 2018年4月17日
---

* update hk 2018 holiday data

1.2 2017年12月20日
---

* 增加get-day-list命令，用于获取一段周期内的工作日或者休息日列表

1.1 2017年11月27日
---

* merge pr #2 from @JaysonAlbert
* 增加minutes per session
* 从wind获取假日信息代码

1.0 2017年11月6日
---

* 增加对香港交易所的支持

0.x
---

* 史前版本，历史记录还未整理
