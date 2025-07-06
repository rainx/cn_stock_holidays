# 更新日志

版本遵循语义化版本控制 (<major>.<minor>.<patch>)。

## cn-stock-holidays 2.1.3 (2025-01-27)

### 改进

- **代码清理和维护**: 移除过时和无用的代码以提高项目可维护性
  - 移除 `wind_holidays.py` - 过时的 Wind API 集成脚本
  - 移除 `tools/in/` 目录中的临时数据处理工具
  - 移除已废弃的 `utils/` 目录及其无用的数据获取脚本
  - 通过将 `debug.py` 合并到 `dev_shell.py` 来整合开发脚本
  - 简化 `ipython_config.py` 配置
  - 更新文档和脚本引用
  - 在保持 100% 测试覆盖率的同时减少约 500+ 行无用代码

## cn-stock-holidays 2.1.2 (2025-01-27)

### 错误修复

- 修复了 2019 年劳动节假期安排的历史数据 - 确认 2019 年 5 月 2 日和 3 日休市，符合上交所公告 ([Issue #13](https://github.com/rainx/cn_stock_holidays/issues/13), [上交所参考](https://www.sse.com.cn/disclosure/announcement/general/c/c_20190418_4771364.shtml))

## cn-stock-holidays 2.1.1 (2025-01-27)

### 错误修复

- 修复了 2024-02-09（除夕）的历史数据 - 更新为反映该日期市场休市 ([Issue #16](https://github.com/rainx/cn_stock_holidays/issues/16))

## cn-stock-holidays 2.1.0 (2024-12-19)

### 新功能

- **香港市场半日交易支持**: 为香港证券交易所添加了全面的半日交易支持
  - 新增 `is_half_day_trading_day()` 函数用于检测半日交易日
  - 增强数据格式支持，使用 `,h` 后缀标记半日交易日期（例如：`20251225,h`）
  - 保持对现有上海/深圳市场数据的向后兼容性
  - 半日交易日仍被 `is_trading_day()`、`next_trading_day()`、`previous_trading_day()` 和 `trading_days_between()` 视为交易日
  - 更新香港市场数据，包含截至 2025 年的半日交易日期
  - 添加了半日交易功能的综合测试套件

### 改进

- 将香港市场节假日数据扩展至 2025 年
- 添加对常见半日交易模式的支持：
  - 平安夜（12 月 24 日）
  - 除夕（12 月 31 日）
  - 农历除夕
  - 主要节假日前一天（清明节、国庆节）
- 通过 `_get_from_file_with_half_day()` 函数增强数据解析
- 添加新的元函数以支持半日交易，同时保持现有 API 兼容性

## cn-stock-holidays 2.0.0 (2024-12-19)

### 新功能

- **重大更新**: 项目现代化改造
  - 引入 uv 作为现代化的 Python 包管理工具
  - 迁移到 pyproject.toml 配置，移除 setup.py
  - 添加完整的开发工具链：black, isort, mypy, flake8, pre-commit
  - 更新 CI/CD 工作流，使用 uv 进行测试、构建和发布
  - 将 CI 工作流文件从 test.yml 重命名为 ci.yml，提高清晰度
  - 迁移到 PyPI Trusted Publisher 实现安全的自动化发布
  - 修复已弃用的 GitHub Actions upload-artifact，从 v3 升级到 v4
  - 修复 uv publish 命令，移除不支持的 --yes 标志并添加 trusted-publishing
  - 修复发布作业，添加 download-artifact 步骤以访问构建的包
  - 添加代码质量检查和自动化格式化
  - 支持现代 Python 打包标准 (PEP 517/518)
  - 改进项目结构和文档

## cn-stock-holidays 1.12 (2024-12-03)

### 改进

- 更新了 2024 年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.11 (2023-12-25)

### 改进

- 更新了 2024 年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.10 (2022-12-16)

### 改进

- 更新了 2023 年国内的股市节假日 <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.9 (2021-12-30)

### 改进

- 更新了 2022 年国内股市节假日 <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.8 (2020-12-25)

### 改进

- 更新了 2021 年国内股市节假日 <https://www.tdx.com.cn/url/holiday/>

## cn-stock-holidays 1.7 (2020-01-31)

### 错误修复

- 受 2019-nCoV 影响，变更 2020 年的股市日历, 追加 2020 年 1 月 31 日

## cn-stock-holidays 1.6 (2019-12-06)

### 错误修复

- 修复一处错误 20090101 -> 20190101, thanks @liuyug #8

## cn-stock-holidays 1.5 (2019-11-26)

### 改进

- 更新 2020 年中国市场休假数据 ref: <https://www.tdx.com.cn/url/holiday/>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).join("\n")
```

- 更新 2019，2020 年香港股市休市数据 ref: <https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Calendar-and-Holiday-Schedule?sc_lang=en>

```
$("table.table tr td:first-child").map((i, e)=>e.innerText).toArray().filter(e => /[\d.]/.test(e)).map(e=>e.replace(/\./g, "")).filter(e=>e.includes("/")).map(e=> moment(e, "D/M/YYYY").format("YYYYMMDD")).join("\n")
```

## cn-stock-holidays 1.4 (2019-01-08)

### 改进

- 更新 2019 年中国市场假期数据

## cn-stock-holidays 1.3 (2018-04-17)

### 改进

- update hk 2018 holiday data

## cn-stock-holidays 1.2 (2017-12-20)

### 新功能

- 增加 get-day-list 命令，用于获取一段周期内的工作日或者休息日列表

## cn-stock-holidays 1.1 (2017-11-27)

### 新功能

- merge pr #2 from @JaysonAlbert
- 增加 minutes per session
- 从 wind 获取假日信息代码

## cn-stock-holidays 1.0 (2017-11-06)

### 新功能

- 增加对香港交易所的支持

## cn-stock-holidays 0.x

### 历史版本

- 史前版本，历史记录还未整理
