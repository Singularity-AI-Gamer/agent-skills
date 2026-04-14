# 项目内 QQ 真值集参考产物

将本文件中的路径视为仓库根目录相对路径。

这些产物用于找证据、看样例、理解输出格式和对照旧结果。它们不是未来任务的固定标准答案。

## 当前权威案例产物

- `test_dataset/qq_20260201_20260311_final/truth_manifest.json`
  - 机器比对入口
- `test_dataset/qq_20260201_20260311_final/ground_truth_report.md`
  - 人工核对入口
- `test_dataset/qq_20260201_20260311_final/review_ledger.csv`
  - 审查台账
- `test_dataset/qq_20260201_20260311_final/comparison_report.md`
  - 新旧自动结果与人工案例的差异说明
- `test_dataset/qq_20260201_20260311_final/mailbox_inventory.json`
  - 邮箱盘点结果
- `test_dataset/qq_20260201_20260311_final/email_truth_audit.json`
  - 窗口邮件审计结果
- `test_dataset/qq_20260201_20260311_final/raw_documents/`
  - 原始材料和 sidecar 证据
- `test_dataset/qq_20260201_20260311_final/ground_truth_batch_summary.md`
  - 面向跑批对比的摘要文档

## 经验总结产物

- `diagnostics/lessons_for_163_mailbox_truth_validation.md`
  - 跨邮箱可借鉴的经验总结，尤其适合新线程快速看常见坑

## 代码入口

- `build_truth_dataset.py`
  - 真值集生成主入口
- `audit_email_truth.py`
  - 邮箱盘点与窗口审计辅助入口

## 使用提醒

- 这些路径提供的是当前项目中已经验证过的样例和证据。
- 不要把样例中的邮件数、真值数、类型分布直接套用为未来 QQ 任务的固定标准。
- 如果未来真值任务出现新的类型、平台或附件结构，优先保留证据并进入 review。
