# 更新日志

版本遵循语义化版本控制 (<major>.<minor>.<patch>)。

## cn-stock-holidays 2.0.0 (2024-12-19)

### 新功能

- **重大更新**: 项目现代化改造
  - 引入 uv 作为现代化的 Python 包管理工具
  - 迁移到 pyproject.toml 配置，移除 setup.py
  - 添加完整的开发工具链：black, isort, mypy, flake8, pre-commit
  - 更新 CI/CD 工作流，使用 uv 进行测试、构建和发布
  - 将 CI 工作流文件从 test.yml 重命名为 ci.yml，提高清晰度
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
