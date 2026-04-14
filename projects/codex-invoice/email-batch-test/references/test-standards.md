# 跑批通过标准

## P0 — 漏票（Critical）

**定义**：truth_manifest 中 `truth_status=included` 的文档，在跑批输出目录中找不到对应文件。

**匹配方式**：
1. 优先用 `invoice_number` 精确匹配
2. 其次用 `sha256` 哈希匹配
3. 兜底用 `file_name` + `amount` + `seller` 组合匹配

**通过条件**：P0 = 0（零容忍）

**检测工具**：`strict_truth_audit.py` → `p0_conclusion.bad_rows`

## P1 — 人工过载（High）

**定义**：被分流到 Manual_Check 文件夹的文件数量过多，导致用户需要大量人工复核。

**计算**：`Manual_Check 数量 ÷ included 总数 × 100%`

**通过条件**：≤ 15%（即 41 张中最多 6 张进 Manual_Check）

**检测工具**：`strict_truth_audit.py` → `manual_check_rows`

## P2 — 分类命名错（Medium）

**定义**：文件已下载到输出目录，但归档路径或文件名与真值集预期不符。

**常见表现**：
- 打车发票被归档到餐饮文件夹
- 文件名中的日期、金额、卖方信息错误
- 行程单被当成发票归档

**通过条件**：允许少量，但需记录并跟踪

**检测工具**：`strict_truth_audit.py` → `kpi_rows` 中的 `naming_match` 字段
