# Changelog

Versions follow Semantic Versioning (<major>.<minor>.<patch>).

## cn-stock-holidays 2.1.4 (2025-12-07)

### Improvements

- **Updated 2026 Stock Market Holidays**: Added complete holiday data for 2026 from TDX official source
  - New Year's Day: January 1-2
  - Spring Festival: February 16-20, 23
  - Qingming Festival: April 6
  - Labor Day: May 1, 4-5
  - Dragon Boat Festival: June 19
  - Mid-Autumn Festival: September 25
  - National Day: October 1-2, 5-7
  - Data source: <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 2.1.3 (2025-01-27)

### Improvements

- **Code Cleanup and Maintenance**: Removed outdated and unused code to improve project maintainability
  - Removed `wind_holidays.py` - outdated Wind API integration script
  - Removed temporary data processing tools in `tools/in/` directory
  - Removed deprecated `utils/` directory with unused data fetching scripts
  - Consolidated development scripts by merging `debug.py` into `dev_shell.py`
  - Simplified `ipython_config.py` configuration
  - Updated documentation and script references
  - Reduced codebase by ~500+ lines of unused code while maintaining 100% test coverage

## cn-stock-holidays 2.1.2 (2025-01-27)

### Bug Fixes

- Fixed historical data for 2019 Labor Day holiday arrangement - confirmed May 2nd and 3rd, 2019 were closed as per SSE announcement ([Issue #13](https://github.com/rainx/cn_stock_holidays/issues/13), [SSE Reference](https://www.sse.com.cn/disclosure/announcement/general/c/c_20190418_4771364.shtml))

## cn-stock-holidays 2.1.1 (2025-01-27)

### Bug Fixes

- Fixed historical data for 2024-02-09 (Chinese New Year's Eve) - updated to reflect that markets were closed on this date ([Issue #16](https://github.com/rainx/cn_stock_holidays/issues/16))

## cn-stock-holidays 2.1.0 (2024-12-19)

### New Features

- **Half-Day Trading Support for Hong Kong Market**: Added comprehensive support for Hong Kong stock exchange half-day trading
  - New `is_half_day_trading_day()` function to detect half-day trading days
  - Enhanced data format support with `,h` suffix for half-day trading dates (e.g., `20251225,h`)
  - Backward compatibility maintained for existing Shanghai/Shenzhen market data
  - Half-day trading days are still considered trading days by `is_trading_day()`, `next_trading_day()`, `previous_trading_day()`, and `trading_days_between()`
  - Updated Hong Kong market data to include half-day trading dates through 2025
  - Added comprehensive test suite for half-day trading functionality

### Improvements

- Extended Hong Kong market holiday data through 2025
- Added support for common half-day trading patterns:
  - Christmas Eve (December 24)
  - New Year's Eve (December 31)
  - Lunar New Year's Eve
  - Day before major holidays (Qingming Festival, National Day)
- Enhanced data parsing with `_get_from_file_with_half_day()` function
- Added new meta functions for half-day trading support while maintaining existing API compatibility

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
  - Fixed uv publish command by removing unsupported --yes flag and adding trusted-publishing
  - Fixed publish job by adding download-artifact step to access built packages
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
