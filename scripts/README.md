# Development Scripts

This directory contains various scripts to help with development and debugging of the `cn_stock_holidays` package.

## Quick Start

### 1. Setup Development Environment

```bash
# Install all development dependencies including IPython
./scripts/setup-dev.sh
```

### 2. Start Development Shell

```bash
# Start IPython with all modules pre-loaded
python scripts/dev_shell.py
# or
uv run python scripts/dev_shell.py
```

## Available Scripts

### `dev_shell.py` - Development Shell

The main development environment script that starts IPython with:

- All project modules pre-imported
- Auto-reload enabled for development
- Commonly used functions available
- Helpful examples and documentation

**Usage:**

```bash
python scripts/dev_shell.py
```

**Features:**

- Auto-reloads modules when you make changes
- Pre-imports all main functions
- Provides helpful examples
- Syntax highlighting and auto-completion

### `quick_test.py` - Quick Functionality Test

A simple script to quickly test the package functionality without starting IPython.

**Usage:**

```bash
python scripts/quick_test.py
```

**Tests:**

- Mainland China market functions
- Hong Kong market functions (including half-day trading)
- Cache management
- Common utilities

## IPython Configuration

### `ipython_config.py` - IPython Configuration

Advanced IPython configuration file with custom settings.

**Usage:**

```bash
# In IPython
exec(open('scripts/ipython_config.py').read())
```

**Features:**

- Custom aliases for common operations
- Syntax highlighting
- Auto-completion
- History search

## Common Debugging Tasks

### 1. Test Trading Day Functions

```python
# In IPython or debug shell
is_trading_day('2024-01-01')  # Mainland China
is_trading_day_hk('2024-12-24')  # Hong Kong
is_half_day_trading_day('2024-12-24')  # Hong Kong half-day
```

### 2. Check Cache Status

```python
get_cache_info()  # Main cache
get_half_day_cache_info()  # Half-day cache
clear_cache()  # Clear main cache
clear_half_day_cache()  # Clear half-day cache
```

### 3. Get Trading Days

```python
# Get trading days between dates
trading_days_between('2024-01-01', '2024-01-31')  # Mainland
trading_days_between_hk('2024-12-01', '2024-12-31')  # Hong Kong

# Get half-day trading days
get_half_day_trading_days('2024-12-01', '2024-12-31')
```

### 4. Test Date Utilities

```python
parse_date('2024-01-01')  # Parse date string
format_date(date(2024, 1, 1))  # Format date object
is_weekend('2024-01-06')  # Check if weekend
```

## Development Workflow

1. **Start Development Shell:**

   ```bash
   python scripts/dev_shell.py
   ```

2. **Test Functions:**

   ```python
   # Test basic functionality
   is_trading_day('2024-01-01')
   is_half_day_trading_day('2024-12-24')
   ```

3. **Make Changes:**

   - Edit source files
   - Changes auto-reload in IPython

4. **Run Quick Tests:**

   ```bash
   python scripts/quick_test.py
   ```

5. **Run Full Tests:**
   ```bash
   uv run pytest
   ```

## Troubleshooting

### IPython Not Found

If you get an error about IPython not being found:

```bash
# Install IPython
uv add --dev ipython

# Then run the script again
python scripts/dev_shell.py
```

### Import Errors

If you get import errors, make sure you're running from the project root:

```bash
cd /path/to/cn_stock_holidays
python scripts/dev_shell.py
```

### Auto-reload Issues

If auto-reload isn't working:

```python
# In IPython
%load_ext autoreload
%autoreload 2
```

## Tips

1. **Use Auto-reload:** The development shell automatically enables auto-reload, so your changes are immediately available.

2. **Check Cache:** Use `get_cache_info()` to see if data is cached and when it expires.

3. **Test Both Markets:** Remember to test both mainland China (`data`) and Hong Kong (`data_hk`) functions.

4. **Use Help:** In IPython, use `help(function_name)` to get detailed documentation.

5. **Quick Tests:** Use `python scripts/quick_test.py` for a quick sanity check before running full tests.
