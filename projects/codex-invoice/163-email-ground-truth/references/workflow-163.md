# 163 邮箱真值集工作流

## 与 QQ 工作流的差异

本流程基于 `qq-email-ground-truth/references/workflow.md`，仅列出 163 特殊步骤。

## 163 专属步骤

### 1. IMAP 连接

163 IMAP 登录后必须发送 RFC 2971 ID 命令，否则后续操作被拒绝：

```python
mail = imaplib.IMAP4_SSL("imap.163.com", 993)
mail.login(email_addr, auth_code)
# 163 必须的 ID 命令
tag = mail._new_tag()
mail.send(tag + b' ID ("name" "CodexInvoice" "version" "1.0")\r\n')
while True:
    line = mail.readline()
    if line.startswith(tag):
        break
```

### 2. 邮箱盘点

163 邮箱文件夹名使用 UTF-7 编码：
- `INBOX` → 收件箱
- `&g0l6P3ux-` → 草稿箱
- `&XfJT0ZAB-` → 已发送

确认只看 `INBOX`。

### 3. 日期过滤

与 QQ 相同：先取 ALL，再按 Date 头本地过滤。163 IMAP 的 SINCE/BEFORE 搜索同样不可靠。

### 4. 构建命令

```powershell
python build_truth_dataset.py `
  --email <your-163-email>@163.com `
  --auth-code <YOUR_163_AUTH_CODE> `
  --since 2026-03-01 `
  --before 2026-03-19 `
  --mailbox INBOX `
  --output-root test_dataset/163_20260301_20260319
```

### 5. 收口检查

同 QQ 标准：`finalized=true`, `pending_review_count=0`
