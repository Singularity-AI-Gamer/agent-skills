# QQ 真值集工作流

将本文件当作本项目内 QQ 邮箱真值集生成与审计的标准流程。

## 作用边界

- 只约束本项目内的 QQ 邮箱真值集工作。
- 不把当前案例数字当成未来任务的固定验收标准。
- 不假设当前已知发票类型已经穷尽。

## 使用现有入口

- 使用 `build_truth_dataset.py` 生成真值集。
- 使用 `audit_email_truth.py` 或 `build_truth_dataset.py` 自带的审计产物做邮箱盘点和窗口核对。
- 不新增平行 truth builder。

## 标准步骤

### 1. 固定任务范围

先明确：

- 邮箱账号
- 文件夹，例如 `INBOX`
- 时间窗口，例如 `YYYY-MM-DD` 到 `YYYY-MM-DD`
- 输出目录

时间过滤口径固定为邮件 `Date` 头本地时间，不以票面日期过滤。

### 2. 先做邮箱盘点

先确认窗口邮件数，再开始构建真值。

最低要求：

- 有 `mailbox_inventory.json`
- 能说明当前窗口邮件数
- 能说明当前只看哪个文件夹

### 3. 运行真值构建

命令模板：

```powershell
python build_truth_dataset.py `
  --email <qq_email> `
  --auth-code <auth_code> `
  --since YYYY-MM-DD `
  --before YYYY-MM-DD `
  --mailbox INBOX `
  --output-root test_dataset\qq_<since>_<before>_final
```

输出目录名可变，但必须显式指定，避免覆盖旧案例。

### 4. 检查输出物

最低应包含：

- `truth_manifest.json`
- `ground_truth_report.md`
- `review_ledger.csv`
- `comparison_report.md`
- `mailbox_inventory.json`
- `email_truth_audit.json`
- `raw_documents/`

### 5. 做最终收口

只有满足下列条件，才能把结果称为最终真值集：

- `summary.finalized = true`
- `pending_review_count = 0`
- 每条 included 记录都有：
  - `truth_type`
  - `document_role`
  - `invoice_date`
  - `seller`
  - `amount`
  - `source_email_id`
  - `file_name`
- 每条 included 记录都能回溯到原始文件和来源邮件

### 6. 做结果对比

如果用户要对比人工清单或程序跑批输出，优先用：

- `truth_manifest.json` 作为机器比对入口
- `ground_truth_report.md` 作为人工核对入口

逐条比对时，至少看这些字段：

- `truth_type`
- `document_role`
- `invoice_date`
- `seller`
- `purchaser`
- `amount`
- `source_email_id`
- `file_name`

## 未知类型或新结构的处理

以下情况都不能直接排除：

- 新发票类型
- 新开票平台
- 新附件结构
- 新链接型发票样式
- 新的自转发采购场景

正确处理：

1. 保留原始文件与来源邮件
2. 写入审查台账
3. 进入 review 或 pending 状态
4. 只有证据足够后再 included 或 excluded

## 当前已知报销类型

将以下类型只视为当前项目内已验证过的参考范围：

- 餐饮
- 火车票
- 打车发票
- 打车行程单
- 住宿发票
- 住宿水单
- 通讯费

这不是封闭枚举。未来出现新类型时，默认进入 review。
