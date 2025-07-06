# cn_stock_holidays

![CI Status](https://github.com/rainx/cn_stock_holidays/actions/workflows/ci.yml/badge.svg)

A comprehensive Python package providing China stock exchange holiday data for both Shanghai/Shenzhen (SHSZ) and Hong Kong (HKEX) markets. This package serves as a reliable data source and utility library for financial applications that need to determine trading days.

## Features

- **Dual Market Support**: Covers both mainland China and Hong Kong markets
- **Multiple Data Sources**: Local files, cached data, and remote fetching
- **Zipline Integration**: Provides exchange calendars for algorithmic trading
- **CLI Tools**: Command-line utilities for data extraction
- **Caching Mechanism**: LRU cache for performance optimization
- **Comprehensive API**: Functions for trading day calculations

## Data Files

### Shanghai/Shenzhen Market

```
cn_stock_holidays/data.txt
```

### Hong Kong Market

```
cn_stock_holidays/data_hk.txt
```

### Fetch Data via URL

```bash
# Shanghai/Shenzhen data
wget https://raw.githubusercontent.com/rainx/cn_stock_holidays/main/cn_stock_holidays/data.txt

# Or using curl
curl https://raw.githubusercontent.com/rainx/cn_stock_holidays/main/cn_stock_holidays/data.txt
```

## Data Format

The data files store all holidays for China stock exchanges (excluding regular weekend closures on Saturday and Sunday), with one date per line in the format:

```
YYYYMMDD
```

## Installation

### Using uv (Recommended)

This project supports [uv](https://github.com/astral-sh/uv), a fast Python package installer:

```bash
# Install uv first
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package
uv pip install cn-stock-holidays
```

### Using pip

```bash
pip install cn-stock-holidays
```

### From source

```bash
git clone https://github.com/rainx/cn_stock_holidays.git
cd cn_stock_holidays
uv sync --dev  # Install with uv
# or
pip install -e .  # Install with pip
```

## Usage

### Import

```python
# For Shanghai/Shenzhen market
import cn_stock_holidays.data as shsz

# For Hong Kong market
import cn_stock_holidays.data_hk as hkex
```

### Core Functions

```python
# Get holiday data
holidays = shsz.get_cached()  # Get from cache or local file
holidays = shsz.get_local()   # Read from package data file
holidays = shsz.get_remote_and_cache()  # Fetch from network and cache

# Trading day operations
is_trading = shsz.is_trading_day(date)  # Check if date is a trading day
prev_day = shsz.previous_trading_day(date)  # Get previous trading day
next_day = shsz.next_trading_day(date)  # Get next trading day

# Get trading days in range
for trading_day in shsz.trading_days_between(start_date, end_date):
    print(trading_day)

# Data synchronization
shsz.sync_data()  # Sync data if expired
shsz.check_expired()  # Check if data needs update
```

### Function Details

```python
Help on module cn_stock_holidays.data:

FUNCTIONS
    check_expired()
        Check if local or cached data needs update
        :return: True/False

    get_cached()
        Get from cache version, if not existing, use txt file in package data
        :return: A set/list contains all holiday data, elements with datetime.date format

    get_local()
        Read data from package data file
        :return: A list contains all holiday data, elements with datetime.date format

    get_remote_and_cache()
        Get newest data file from network and cache on local machine
        :return: A list contains all holiday data, elements with datetime.date format

    is_trading_day(dt)
        :param dt: datetime.datetime or datetime.date
        :return: True if trading day, False otherwise

    next_trading_day(dt)
        :param dt: datetime.datetime or datetime.date
        :return: Next trading day as datetime.date

    previous_trading_day(dt)
        :param dt: datetime.datetime or datetime.date
        :return: Previous trading day as datetime.date

    sync_data()
        Synchronize data if expired

    trading_days_between(start, end)
        :param start, end: Start and end time, datetime.datetime or datetime.date
        :return: A generator for available trading dates in Chinese market
```

### Cache Management

From version 0.10 onwards, we use `functools.lru_cache` on `get_cached` for better performance. If needed, you can clear the cache using:

```python
get_cached.cache_clear()
```

## Command Line Tools

### Data Synchronization

```bash
# Sync Shanghai/Shenzhen data
cn-stock-holiday-sync

# Sync Hong Kong data
cn-stock-holiday-sync-hk
```

### Get Trading Days List

```bash
# Get trading days between dates
get-day-list --start 2024-01-01 --end 2024-01-31 --daytype workday

# Get holidays between dates
get-day-list --start 2024-01-01 --end 2024-01-31 --daytype holiday

# For Hong Kong market
get-day-list --market hk --start 2024-01-01 --end 2024-01-31 --daytype workday
```

## Keeping Data Up-to-Date

The package includes scripts to check data expiration and fetch updates from the web. You can set up automatic updates using cron:

```crontab
# Daily sync at midnight
0 0 * * * /usr/local/bin/cn-stock-holiday-sync > /tmp/cn_stock_holiday_sync.log
```

Find the absolute path of sync commands:

```bash
# Shanghai/Shenzhen
which cn-stock-holiday-sync

# Hong Kong
which cn-stock-holiday-sync-hk
```

## Zipline Integration

For algorithmic trading with Zipline:

```python
from cn_stock_holidays.zipline import SHSZExchangeCalendar, HKExchangeCalendar

# Use in Zipline
calendar = SHSZExchangeCalendar()  # Shanghai/Shenzhen
calendar = HKExchangeCalendar()     # Hong Kong
```

## Development

### Setup Development Environment

```bash
# Clone and setup
git clone https://github.com/rainx/cn_stock_holidays.git
cd cn_stock_holidays

# Install with uv (recommended)
uv sync --dev

# Or with pip
pip install -e .[dev]
```

### Run Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=cn_stock_holidays

# Format code
uv run black .

# Type checking
uv run mypy cn_stock_holidays/
```

### Publishing

This project uses [PyPI Trusted Publisher](https://docs.pypi.org/trusted-publishers/) for secure automated publishing. The CI workflow automatically publishes to PyPI when a new tag is pushed.

**To publish a new version:**

1. Update version in `pyproject.toml`
2. Create and push a new tag:
   ```bash
   git tag v2.0.1
   git push origin v2.0.1
   ```
3. The CI workflow will automatically test, build, and publish to PyPI

**Security Benefits:**

- No need to manage long-lived API tokens
- Short-lived authentication tokens (15 minutes)
- Repository-specific permissions
- Automated OIDC authentication

See [Trusted Publisher Setup](docs/TRUSTED_PUBLISHER_SETUP.md) for detailed configuration instructions.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [GitHub Repository](https://github.com/rainx/cn_stock_holidays)
- [PyPI Package](https://pypi.org/project/cn-stock-holidays/)
- [UV Package Manager](https://github.com/astral-sh/uv)
