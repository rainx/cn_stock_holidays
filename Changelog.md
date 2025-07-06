# Changelog

Versions follow Semantic Versioning (<major>.<minor>.<patch>).

## cn-stock-holidays 2.0.0 (2024-12-19)

### New Features

- **Major Update**: Project modernization
  - Introduced uv as a modern Python package manager
  - Migrated to pyproject.toml configuration, removed setup.py
  - Added complete development toolchain: black, isort, mypy, flake8, pre-commit
  - Updated CI/CD workflows to use uv for testing, building and publishing
  - Renamed CI workflow file from test.yml to ci.yml for better clarity
  - Migrated to PyPI Trusted Publisher for secure automated publishing
  - Fixed deprecated GitHub Actions upload-artifact from v3 to v4
  - Added code quality checks and automated formatting
  - Support for modern Python packaging standards (PEP 517/518)
  - Improved project structure and documentation

## cn-stock-holidays 1.12 (2024-12-03)

### Improvements

- Updated 2024 domestic stock market holidays <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.11 (2023-12-25)

### Improvements

- Updated 2024 domestic stock market holidays <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.10 (2022-12-16)

### Improvements

- Updated 2023 domestic stock market holidays <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.9 (2021-12-30)

### Improvements

- Updated 2022 domestic stock market holidays <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.8 (2020-12-25)

### Improvements

- Updated 2021 domestic stock market holidays <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.7 (2020-01-31)

### Bug Fixes

- Changed 2020 stock market calendar due to 2019-nCoV impact, added 2020-01-31

## cn-stock-holidays 1.6 (2019-12-06)

### Bug Fixes

- Fixed an error: 20090101 -> 20190101, thanks @liuyug #8

## cn-stock-holidays 1.5 (2019-11-26)

### Improvements

- Updated 2020 China market holiday data ref: <https://www.tdx.com.cn/url/holiday/>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).join("\n")
```

- Updated 2019, 2020 Hong Kong stock market holiday data ref: <https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Calendar-and-Holiday-Schedule?sc_lang=en>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).filter(e=>e.includes("/")).map(e=> moment(e, "D/M/YYYY").format("YYYYMMDD")).join("\n")
```

## cn-stock-holidays 1.4 (2019-01-08)

### Improvements

- Updated 2019 China market holiday data

## cn-stock-holidays 1.3 (2018-04-17)

### Improvements

- Updated HK 2018 holiday data

## cn-stock-holidays 1.2 (2017-12-20)

### New Features

- Added get-day-list command for obtaining workday or holiday lists within a period

## cn-stock-holidays 1.1 (2017-11-27)

### New Features

- Merged PR #2 from @JaysonAlbert
- Added minutes per session
- Added code for obtaining holiday information from Wind

## cn-stock-holidays 1.0 (2017-11-06)

### New Features

- Added support for Hong Kong Exchange

## cn-stock-holidays 0.x

### Historical

- Prehistoric versions, historical records not yet organized
