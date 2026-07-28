---
name: gpt56-sol-pro-consult
description: 凡需方案、Plan 或本地材料审查，均用 Codex 侧边 Browser 咨询 Sol Pro；点名或要求 Pro 编排循环时也触发。
---

# GPT 5.6 Sol Pro Consult

把 ChatGPT Web 的 GPT 5.6 Sol Pro 作为 Codex 的外部审查者或 Orchestrator：Pro 负责挑战方案、发现盲点和提出修订；Codex 负责读取本地证据、实施、运行验证并决定是否采纳。

## 执行位置与原生 Browser 路由

默认且唯一的执行面是 Codex 内置侧边 Browser（in-app Browser）。先完整读取并遵循 `browser:control-in-app-browser` Skill，再读取 [侧边 Browser 工作流](references/in-app-browser-workflow.md)。

- 实际 Browser 操作必须由触发本 Skill 的当前主 Codex task 执行。隔离子代理可整理材料或复审结果，但不得代替主 task 打开 ChatGPT、选模型、上传、发送或抽取回复；子代理报告 `iab` 不可用不能证明主 task 的侧边 Browser 不可用。
- 选择独立的 `iab` 绑定，在 Codex 侧边栏打开或复用 `https://chatgpt.com/`。
- 不调用 Chrome 扩展、Chrome CLI、OpenCLI、Playwright CLI 或外部浏览器自动化进程。
- 不检查 cookies、local storage、密码、浏览器配置或 session 文件。
- 如果当前会话没有 Browser Skill、无法取得 `iab` 绑定、未登录 ChatGPT，或账号没有 Pro，停止并准确说明缺少什么；不要静默换模型或换浏览器。

用户发起 Pro 咨询即授权把本次确认需要的上下文和附件发送到 ChatGPT Web；这不授权发送无关文件、凭据或额外消息。

## 两种咨询模式

### Reviewer（默认）

用于方案 Review、Plan 审查和一次性建议：

1. Codex 先写出自己的判断、证据和未知项。
2. 把最小但充分的上下文交给 Pro，请它优先指出最大漏洞、反例和必要修改。
3. Codex 核对 Pro 的意见，只采纳有证据支撑且符合用户目标的部分。
4. 把 Pro 观点和本地采纳决定合并成最终回答。

### Orchestrator loop（仅在复杂任务或用户明确要求时）

按同一 ChatGPT 对话循环：

1. **Pro 规划**：审查当前事实与目标，给出可执行计划和验收标准。
2. **Codex 执行**：在本地实现、运行测试并记录实际结果，不把 Pro 的建议当成已验证事实。
3. **Pro 复审**：把 diff、测试结果、剩余风险和失败证据送回同一对话，请 Pro 判定是否仍有关键缺口。
4. **Codex 收敛**：修订并复验；达到用户要求、没有新的实质问题或继续循环收益很低时停止。

默认最多进行 3 个“执行—复审”回合。若任务会产生外部写入、发布、付款、删除或其他需要新授权的动作，仍按 Codex 的权限边界停下请求用户决定；Pro 不能扩大权限。

## 硬门槛

### 模型真实性

发送前从当前可见模型选择器确认：

- 当前模型家族明确显示 `GPT-5.6 Sol`；
- 选中的精确档位是 `Pro`，并具有可观察的选中状态。

不要把 GPT 5.5 Pro、Pro Extended、基础 Sol、Extra High 或模型选择器之外的模糊 `Pro` 文本当成 GPT 5.6 Sol Pro。无法确认时停止。

### 材料真实性

ChatGPT Web 不能凭本地路径读取文件。需要文件内容时，必须上传真实文件、粘贴内容，或用 `scripts/build_attachment_bundle.py` 生成可审阅的 Markdown bundle。只给文件名、路径或摘要时，不得声称 Pro 看过原文件。

### 凭据卫生

不要发送 token、cookie、密码、API key、private key、OAuth header、浏览器 profile 或 session dump。公司名、金额、联系人等普通业务上下文可在确实影响判断且用户授权的前提下保留。

发送前运行：

```powershell
python <skill-dir>/scripts/check_packet_safety.py <packet.md>
```

扫描通过只表示未命中已知凭据模式；Codex 仍需人工式检查上下文是否最小、相关且获得授权。

### 会话绑定证据

不得用“我会使用侧边 Browser”“已选择 Pro”一类叙述性文字证明咨询完成。每次咨询开始时生成唯一 `task_run_id`，并在本次任务产物目录创建唯一的 `iab-consultation-evidence.json`。按 [evidence 模板](references/session-evidence-template.json) 在同一个主 task 的 Browser run 内追加事实，至少绑定：

- 所选 Browser 的真实类型为 `iab`、Browser session ID、tab ID/URL；
- 发送前 fresh snapshot 中 `GPT-5.6 Sol` 与 `Pro` 的独立选中信号；
- packet 的 distinctive prefix、sentinel、附件名与内容 hash；
- 一次 Send 的 dispatch state、时间与提交后可观察证据；
- 同一 tab 最新完整 assistant turn、生成完成信号与 assistant sentinel 校验。

这些字段必须来自同一 Browser session 和同一对话。任何字段缺失、来源仅为代理自述、或无法与本次 dispatch 关联时，状态保持 `incomplete`；静态路由测试、模拟文本和子代理口头报告都不能替代真实 `iab` 证据。

咨询完成前运行：

```powershell
python <skill-dir>/scripts/validate_session_evidence.py <iab-consultation-evidence.json>
```

只有 validator 返回 `ok: true` 才允许 `Status: completed`。历史 preflight、截图或其他任务的 evidence 只能证明能力可用，不能证明当前咨询完成。

## 工作流

1. 明确要让 Pro 判断的具体问题、成功标准和期望输出。
2. 先形成 Codex 的本地判断：事实、证据、约束、方案、风险、尝试和未知项。
3. 按 [上下文包模板](references/context-packet-template.md) 生成 packet；普通 Review 保持紧凑，复杂架构或 Orchestrator 任务才使用更完整材料。
4. 选择最小充分证据集。结构、格式、源码或日志细节会影响结论时上传真实附件。
5. 运行安全扫描，再按 [侧边 Browser 工作流](references/in-app-browser-workflow.md) 在主 task 的真实 `iab` 中打开 ChatGPT、确认登录与模型，并建立 evidence ledger。
6. 在发送前把当前 Browser session、tab、模型信号、composer prefix、唯一 sentinel、内容 hash 和全部附件名写入同一 ledger；只发送一次。
7. 记录 dispatch state 和提交后证据，等待同一对话完整生成。仍在生成、只有开场白或没有 assistant sentinel 都不算完成。
8. 抽取同一 tab 的最新完整 assistant turn，验证 sentinel，完成 session-bound ledger，并由 Codex 对照本地证据给出 Adopt / Reject / Modify 决策。
9. 若为 Orchestrator loop，把实现差异和真实验证结果送回同一对话继续复审；每轮新增独立 dispatch 记录，不要开启重复咨询。

## 上下文要求

至少包含：

- 决策或问题本身
- 用户目标与成功标准
- 已验证事实、来源和真实附件
- Codex 咨询前的判断
- 约束、已尝试方法和原始错误
- 候选方案与主要权衡
- 风险、未知项和希望 Pro 输出的形式

要求 Pro 输出简洁的 reasoning brief（假设、判断框架、证据权重、最强反例和权衡），不要索取隐藏 chain-of-thought。

## 完成条件

只有以下条件全部满足，咨询才是 `completed`：

- 已确认 GPT 5.6 Sol Pro。
- session-bound evidence ledger 证明 Browser 类型、session、tab、模型、dispatch 和回复属于同一 `iab` run。
- 发送前已确认 prompt prefix、sentinel 与所需附件。
- 发送结果明确，且没有重复提交风险。
- Pro 已停止生成，完整 assistant turn 已抽取。
- assistant turn 内出现预期 `GPT56_SOL_PRO_RESULT_...` sentinel。

若用户说答案已在侧边栏显示，先从现有对话重新抽取；不要重复发送。若点击 Send 后连接中断且结果不明，恢复原对话，无法唯一确认时标记 incomplete。

## 返回格式

```markdown
## Pro Consultation Result
- Status: completed | incomplete | failed | skipped
- Evidence: <本任务的 iab-consultation-evidence.json 绝对路径> | unavailable
- Evidence binding verified: yes | no
- Model confirmed: yes | no
- Sentinel verified: yes | no
- Browser path: Codex in-app Browser
- Session-bound evidence: complete | incomplete
- Mode: Reviewer | Orchestrator loop

## What GPT 5.6 Sol Pro Said
<简洁总结>

## Local Adoption Decision
- Adopt:
- Reject:
- Modify:
- Reason:

## Final Answer
<Codex 核验后的最终建议或交付物>
```

`response.md`、普通执行日志、context packet、用户转述或最终回答中的文字都不能替代 Evidence。Evidence 不存在或 validator 未通过时，禁止输出 `Status: completed`。

## 故障处理

- **侧边 Browser 不可用**：报告 `iab` 连接缺失并停止，不切换 Chrome 或 CLI。
- **未登录**：请用户在 Codex 侧边 Browser 登录 ChatGPT，完成后继续同一任务。
- **Pro 不可用或无法确认**：停止，不静默选择其他模型。
- **附件失败**：重新获取当前 composer 与文件选择器；小文件可粘贴，多个文本文件可打成一个 Markdown bundle。没有可见附件证据就不得声称上传成功。
- **composer 为空**：重新获取可编辑区并验证 rendered text；未确认 prefix 和 sentinel 时不得发送。
- **发送结果不明**：恢复现有对话并检查用户 turn 或生成状态；不要创建新对话或重复发送。
- **仍在生成**：继续等待同一对话，不刷新、不发“继续”。
- **没有 sentinel**：完整抽取一次最新 assistant turn；仍缺失则标记 incomplete。
- **答案质量低**：只采纳有支持的部分；最终责任仍在 Codex。
