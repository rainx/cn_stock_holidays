# cn_stock_holidays

![CI Status](https://github.com/rainx/cn_stock_holidays/actions/workflows/ci.yml/badge.svg)

一个全面的 Python 包，为中国大陆（沪深）和香港股票交易所提供节假日数据。该包为需要确定交易日的金融应用程序提供可靠的数据源和实用工具库。

## 功能特性

- **双市场支持**：涵盖中国大陆和香港市场
- **多数据源**：本地文件、缓存数据和远程获取
- **Zipline 集成**：为算法交易提供交易所日历
- **命令行工具**：数据提取的命令行实用工具
- **缓存机制**：LRU 缓存优化性能
- **全面的 API**：交易日计算函数

## 数据文件

### 沪深市场

```
cn_stock_holidays/data.txt
```

### 香港市场

```
cn_stock_holidays/data_hk.txt
```

### 通过 URL 获取数据

```bash
# 沪深数据
wget https://raw.githubusercontent.com/rainx/cn_stock_holidays/main/cn_stock_holidays/data.txt

# 或使用 curl
curl https://raw.githubusercontent.com/rainx/cn_stock_holidays/main/cn_stock_holidays/data.txt
```

## 数据格式

数据文件存储中国股票交易所的所有节假日（不包括周六周日的常规休市），每行一个日期，格式为：

```
YYYYMMDD
```

## 安装

### 使用 uv（推荐）

本项目支持 [uv](https://github.com/astral-sh/uv)，一个快速的 Python 包安装器：

```bash
# 首先安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装包
uv pip install cn-stock-holidays
```

### 使用 pip

```bash
pip install cn-stock-holidays
```

### 从源码安装

```bash
git clone https://github.com/rainx/cn_stock_holidays.git
cd cn_stock_holidays
uv sync --dev  # 使用 uv 安装
# 或
pip install -e .  # 使用 pip 安装
```

## 使用方法

### 导入

```python
# 沪深市场
import cn_stock_holidays.data as shsz

# 香港市场
import cn_stock_holidays.data_hk as hkex
```

### 核心函数

```python
# 获取节假日数据
holidays = shsz.get_cached()  # 从缓存或本地文件获取
holidays = shsz.get_local()   # 从包数据文件读取
holidays = shsz.get_remote_and_cache()  # 从网络获取并缓存

# 交易日操作
is_trading = shsz.is_trading_day(date)  # 检查是否为交易日
prev_day = shsz.previous_trading_day(date)  # 获取前一个交易日
next_day = shsz.next_trading_day(date)  # 获取下一个交易日

# 获取日期范围内的交易日
for trading_day in shsz.trading_days_between(start_date, end_date):
    print(trading_day)

# 数据同步
shsz.sync_data()  # 如果过期则同步数据
shsz.check_expired()  # 检查数据是否需要更新
```

### 函数详情

```python
Help on module cn_stock_holidays.data:

FUNCTIONS
    check_expired()
        检查本地或缓存数据是否需要更新
        :return: True/False

    get_cached()
        从缓存版本获取，如果不存在，使用包数据中的 txt 文件
        :return: 包含所有节假日数据的集合/列表，元素为 datetime.date 格式

    get_local()
        从包数据文件读取数据
        :return: 包含所有节假日数据的列表，元素为 datetime.date 格式

    get_remote_and_cache()
        从网络获取最新数据文件并在本地机器上缓存
        :return: 包含所有节假日数据的列表，元素为 datetime.date 格式

    is_trading_day(dt)
        :param dt: datetime.datetime 或 datetime.date
        :return: 如果是交易日返回 True，否则返回 False

    next_trading_day(dt)
        :param dt: datetime.datetime 或 datetime.date
        :return: 下一个交易日，格式为 datetime.date

    previous_trading_day(dt)
        :param dt: datetime.datetime 或 datetime.date
        :return: 前一个交易日，格式为 datetime.date

    sync_data()
        如果过期则同步数据

    trading_days_between(start, end)
        :param start, end: 开始和结束时间，datetime.datetime 或 datetime.date
        :return: 中国市场可用交易日的生成器
```

### 缓存管理

从版本 0.10 开始，我们在 `get_cached` 上使用 `functools.lru_cache` 以获得更好的性能。如果需要，可以使用以下方式清除缓存：

```python
get_cached.cache_clear()
```

## 命令行工具

### 数据同步

```bash
# 同步沪深数据
cn-stock-holiday-sync

# 同步香港数据
cn-stock-holiday-sync-hk
```

### 获取交易日列表

```bash
# 获取日期范围内的交易日
get-day-list --start 2024-01-01 --end 2024-01-31 --daytype workday

# 获取日期范围内的节假日
get-day-list --start 2024-01-01 --end 2024-01-31 --daytype holiday

# 香港市场
get-day-list --market hk --start 2024-01-01 --end 2024-01-31 --daytype workday
```

## 保持数据更新

该包包含检查数据过期并从网络获取更新的脚本。您可以使用 cron 设置自动更新：

```crontab
# 每天午夜同步
0 0 * * * /usr/local/bin/cn-stock-holiday-sync > /tmp/cn_stock_holiday_sync.log
```

查找同步命令的绝对路径：

```bash
# 沪深
which cn-stock-holiday-sync

# 香港
which cn-stock-holiday-sync-hk
```

## Zipline 集成

用于 Zipline 算法交易：

```python
from cn_stock_holidays.zipline import SHSZExchangeCalendar, HKExchangeCalendar

# 在 Zipline 中使用
calendar = SHSZExchangeCalendar()  # 沪深
calendar = HKExchangeCalendar()     # 香港
```

## 开发

### 设置开发环境

```bash
# 克隆并设置
git clone https://github.com/rainx/cn_stock_holidays.git
cd cn_stock_holidays

# 使用 uv 安装（推荐）
uv sync --dev

# 或使用 pip
pip install -e .[dev]
```

### 运行测试

```bash
# 运行所有测试
uv run pytest

# 运行覆盖率测试
uv run pytest --cov=cn_stock_holidays

# 格式化代码
uv run black .

# 类型检查
uv run mypy cn_stock_holidays/
```

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 运行测试并确保代码质量
5. 提交拉取请求

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 链接

- [GitHub 仓库](https://github.com/rainx/cn_stock_holidays)
- [PyPI 包](https://pypi.org/project/cn-stock-holidays/)
- [UV 包管理器](https://github.com/astral-sh/uv)
