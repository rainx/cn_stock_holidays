# Produced by

1. Use Chrome to open this page: https://www.tdx.com.cn/url/holiday/ and Select "中国"
2. Open developer tool's console
3. Type the following code in console
```
console.log([...document.getElementById("month_holiday_td").querySelectorAll("tr td:first-child")].map(e=>e.innerText.replaceAll(".","-")).join("\n"))
```
4. Copy and store the result to 2023_holidays_includes_weekends.innerText
5. Use `python cn_stock_holidays/tools/remove_weekend_from_day_list.py cn_stock_holidays/tools/in/2023_holidays_includes_weekends.txt out.txt` to generate the result to append to data.txt


Since the result in TDX's website has already excluded all weekend result, so we could using the following console script directly and without the following python script run

```
console.log([...document.getElementById("month_holiday_td").querySelectorAll("tr td:first-child")].map(e=>e.innerText.replaceAll(".","")).join("\n"))
```