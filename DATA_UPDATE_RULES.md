# Data Update Rules for cn_stock_holidays

This document defines the rules for updating holiday data in this project. It is designed to be read by both humans and LLMs for automated updates.

## Core Principles

### 1. Data File Format

- **File**: `cn_stock_holidays/data.txt`
- **Format**: One date per line in `YYYYMMDD` format
- **Encoding**: UTF-8
- **Line Ending**: Unix style (LF)
- **No Trailing Content**: Each line contains only the date, no comments or metadata

### 2. What to Include

**ONLY include dates that meet ALL of these criteria:**

1. ✅ **Non-trading days** (stock market is closed)
2. ✅ **Weekdays only** (Monday-Friday)
3. ✅ **Statutory holidays and their makeup days** (法定节假日及调休日)

**DO NOT include:**

1. ❌ **Weekends** (Saturday and Sunday) - These are automatically handled by the code
2. ❌ **Regular weekdays** - Only include special non-trading weekdays
3. ❌ **Duplicate dates**

### 3. Why Weekends Are Excluded

The stock market is always closed on weekends. The code automatically identifies weekends using `datetime.date.weekday()`:
- If `weekday() >= 5` (Saturday=5, Sunday=6), it's automatically a non-trading day
- No need to store weekends in data.txt
- This keeps the data file small and focused on exceptional non-trading days

## Data Sources

### Primary Source
- **TDX (通达信)**: https://www.tdx.com.cn/url/holiday/
- Look for "中国" (China) tab for Shanghai/Shenzhen market data
- This is the official and most reliable source

### Backup Sources
- Shanghai Stock Exchange: https://www.sse.com.cn/
- Shenzhen Stock Exchange: https://www.szse.cn/

## Annual Update Process

### When to Update
- **Timing**: December of each year (when next year's official calendar is announced)
- **Trigger**: Check TDX website for next year's holiday arrangements

### Step-by-Step Process

1. **Fetch Data**
   ```
   Visit: https://www.tdx.com.cn/url/holiday/
   Select: 中国 (China) tab
   Extract: All holiday dates for the target year
   ```

2. **Filter Weekend Dates**
   ```python
   # Pseudo-code for validation
   for each date in new_dates:
       if date.weekday() >= 5:  # Saturday or Sunday
           REJECT - "Weekend dates must not be included"
       else:
           ACCEPT
   ```

3. **Verify Data Structure**
   - Each holiday period should include all non-trading weekdays
   - Example: If Spring Festival is Feb 10-16 (Mon-Sun):
     - Include: Feb 10, 11, 12, 13, 14 (Mon-Fri)
     - Exclude: Feb 15, 16 (Sat-Sun) - automatically handled
   - Include makeup working days if they fall on normally-closed days

4. **Validate Format**
   - All dates must be 8 digits: YYYYMMDD
   - All dates must be in chronological order
   - No blank lines or comments
   - File must end with the last date (no trailing newline after last date)

5. **Run Tests**
   ```bash
   uv run pytest tests/
   uv run pytest tests/test_latest_year_weekends.py  # Automated weekend check
   ```

6. **Update Metadata**
   - Update version in `pyproject.toml`
   - Update both `Changelog.md` and `Changelog-zh_CN.md`
   - Document data source URL

## Chinese Stock Market Holidays

Typical annual holidays (dates vary each year):

1. **元旦 (New Year's Day)**: Usually Jan 1 + makeup days
2. **春节 (Spring Festival / Chinese New Year)**: 7 days, including makeup days
3. **清明节 (Qingming Festival / Tomb Sweeping Day)**: Usually 1-3 days
4. **劳动节 (Labor Day)**: Usually May 1 + makeup days
5. **端午节 (Dragon Boat Festival)**: Usually 1-3 days
6. **中秋节 (Mid-Autumn Festival)**: Usually 1-3 days
7. **国庆节 (National Day)**: Usually 7 days (Oct 1-7), including makeup days

### Makeup Days (调休)
- When holidays fall near weekends, the government may:
  - Extend the holiday by converting adjacent weekdays to holidays
  - Require working on adjacent weekends to compensate
- **Only include the weekdays that become holidays** in data.txt
- Do NOT include the makeup working days (those are just regular weekends becoming workdays)

## Validation Rules

### Automated Checks (in tests)

1. **No Weekends**: All dates in data.txt must be weekdays (Mon-Fri)
2. **Chronological Order**: Dates must be sorted in ascending order
3. **Valid Dates**: All dates must be valid calendar dates
4. **Format Check**: All dates must match `\d{8}` pattern
5. **Trading Day Logic**: All dates in data.txt must return `False` for `is_trading_day()`

### Manual Checks

1. **Cross-reference**: Compare with official announcements
2. **Complete Coverage**: Ensure all announced holidays are included
3. **No Duplicates**: Each date appears only once
4. **Year Completeness**: Verify all major holidays for the year are present

## Example: Adding 2027 Data (Template)

```python
# Step 1: Fetch from TDX
# Visit https://www.tdx.com.cn/url/holiday/
# Extract dates for 2027

# Step 2: Filter (pseudo-code)
dates_2027 = [
    "20270101",  # New Year - Friday ✓
    "20270211",  # Spring Festival - Thursday ✓
    # ... more dates
]

# Step 3: Validate each date is a weekday
for date_str in dates_2027:
    date_obj = datetime.strptime(date_str, "%Y%m%d")
    assert date_obj.weekday() < 5, f"{date_str} is a weekend!"

# Step 4: Append to data.txt (in chronological order)
# Step 5: Run tests
# Step 6: Update version and changelog
```

## Common Mistakes to Avoid

1. ❌ **Including Saturdays/Sundays**: Weekend dates should NEVER be in data.txt
2. ❌ **Missing makeup holidays**: If a weekday is declared a holiday, include it
3. ❌ **Wrong format**: Must be YYYYMMDD, not YYYY-MM-DD or other formats
4. ❌ **Unsorted data**: Dates must be in chronological order
5. ❌ **Trailing newlines**: File should end immediately after the last date

## Testing Your Changes

After updating data.txt, always run:

```bash
# Run all tests
uv run pytest

# Specifically test the latest year
uv run pytest tests/test_latest_year_weekends.py -v

# Verify specific dates
uv run python -c "
from cn_stock_holidays import data
import datetime
# Test a specific holiday
print(data.is_trading_day(datetime.date(2026, 1, 1)))  # Should be False
print(data.is_trading_day(datetime.date(2026, 1, 6)))  # Should be True (if not holiday)
"
```

## Version Update Guidelines

When adding a new year's data:
- Increment patch version (e.g., 2.1.3 → 2.1.4)
- Update changelog with:
  - All holiday dates added
  - Data source reference
  - Date of update

---

**Last Updated**: 2025-12-07
**For Questions**: https://github.com/rainx/cn_stock_holidays/issues
