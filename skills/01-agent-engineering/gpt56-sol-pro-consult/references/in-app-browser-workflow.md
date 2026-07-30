# Codex 侧边 Browser 工作流

本文件只描述 GPT 5.6 Sol Pro 咨询的业务步骤。浏览器控制细节以当前安装的 `browser:control-in-app-browser` Skill 和该 Browser binding 返回的完整 documentation 为准；不要复制过时的插件路径、DOM 选择器或独立 CLI 命令。

## 1. 连接侧边 Browser

1. 完整读取 `browser:control-in-app-browser` Skill。
2. 按该 Skill 发现并初始化 Browser runtime；复用仍有效的 runtime，不重复创建。
3. 选择独立持久的 in-app Browser 绑定：

   ```js
   if (globalThis.iab == null) {
     globalThis.iab = await agent.browsers.get("iab");
     nodeRepl.write(await iab.documentation());
   }
   ```

4. 在第一次交互前一次性完整读取 `iab.documentation()`。
5. 为每个新 Codex task 新建专用 tab 并导航到 `https://chatgpt.com/`。不得 claim 或复用其他 task 留下的 ChatGPT 对话、Project、草稿、附件或上传状态。只有当前 task 已有匹配 `task_run_id`、Browser session ID、tab ID 和 conversation ID 的 evidence ledger 时，才可继续原 tab。
6. 新 tab 加载后，用 fresh snapshot 确认它是非 Project 的新对话，composer 为空，附件区为空，也没有上传中、等待 file chooser 或错误重试状态。发现任何不属于本 task 的状态时，不要在该 tab 内删除后继续；关闭或放弃它，再创建另一个全新 tab并重复检查。

首次空白只算早期检查。ChatGPT 可能在模型菜单交互后延迟恢复另一任务或全局 composer 草稿，因此发送前还必须执行第 2 节的延迟净空门。

只通过 Browser Skill 指定的 `node_repl js` 与 `tab.playwright` API 操作该页面。不要改用 Chrome 扩展、外部 Playwright、Computer Use、OpenCLI 或浏览器 CLI。

真实 Browser 控制只能在触发咨询的当前主 Codex task 中执行。不要把连接、模型选择、上传、Send 或回复抽取委派给隔离子代理或 CLI worker；它们通常不拥有同一个 `iab` Browser surface。

取得 Browser 和 tab 后立即生成 `task_run_id`，并按 `session-evidence-template.json` 创建本任务唯一的 `iab-consultation-evidence.json`，写入 `executed_by: main-codex-task`、真实 `iab` 类型、Browser session ID、tab ID/URL、咨询轮次与时间。后续模型、packet、dispatch 和回复证据都只能追加到这同一对象；不得用单独日志或最终回答回填。

用 `iab.nameSession("sol-pro:<task_run_id>")` 命名本次 Browser session，便于识别但不把名称当作绑定证据。新 task 不得沿用旧 task 的 tab 变量或 conversation ID。

## 2. 确认登录和模型

用 fresh snapshot 判断是否已登录并能看到 composer。未登录时，请用户直接在 Codex 侧边 Browser 完成登录，然后继续复用同一个 `iab` 与 tab。

打开当前模型选择器，根据 snapshot 中的真实可见元素构造 locator。每次点击前确认 locator 唯一，点击后重新观察目标区域。

确认两个独立信号：

- 模型家族可见文本为 `GPT-5.6 Sol`；
- 精确 `Pro` 选项具有可观察的选中状态。

UI 文案或属性可能更新，因此不要依赖写死的旧 test id。无法同时确认两个信号时停止。

把发送前 fresh snapshot 的两个选中信号与当前 Browser session、tab 和观测时间写入 ledger。只看到 composer 附近的模糊 `Pro` 标签不算双信号证据。

### 延迟净空门（必须在写入本次内容前）

模型菜单关闭、精确 Sol + Pro 信号确认后，重新获取 composer 与附件区；不要沿用新 tab 初次加载时的 locator 或空白判断。把这次观测写入 ledger 的 `late_clean_gate`：

- `checked_after_model_menu` 必须为 `true`；
- rendered composer text 必须为空；
- 不得处于 Project；
- attachment cards、等待或失败的 file chooser、pending upload 都必须为空；
- 记录观测时间、tab 绑定和 `composer_text_sha256`（空字符串的 SHA-256）。

若旧草稿或附件在此时恢复，dispatch 保持 `NOT_SENT`。不要写入本次 packet、不要上传、不要点击 Send，也不要用 Temporary Chat 规避。关闭本 task 新建的污染 tab，最多新建一个 tab 重试；若第二个 tab 也在模型菜单交互后恢复旧内容，记为 `STALE_COMPOSER_BLOCKER`，直接进入 finalize。

除非用户明确要求清理残留，否则不要清空旧内容。获得清理授权时，先记录非敏感前缀和内容 hash；清空后必须再次打开/关闭模型菜单并重新执行本门。旧内容再次出现说明仍有其他会话或全局状态在恢复它，清理未成功。

## 3. 上传所需文件

先阅读当前 `iab` documentation 中的 file upload 说明。使用真实 file chooser，并把“等待 chooser、点击上传入口、选择文件、setFiles”放在同一次 `node_repl js` 调用中，避免跨调用遗失 pending promise。

上传后用 fresh snapshot 验证每个必需文件名都在 composer 附件区域可见。多个文本文件不稳定时，用 `scripts/build_attachment_bundle.py` 合并成一个 Markdown 文件；较小文本在延迟净空门通过后可直接粘贴完整内容。不要把二进制、缓存、依赖、构建输出、`.git` 或无关材料打包。

file chooser 超时或 Browser runtime 重置时，若没有提交证据，dispatch 仍为 `NOT_SENT`；重新连接后必须从新 tab 和延迟净空门开始，不能假定原 composer 仍干净。

## 4. 写入并核对 context packet

附件 UI 会让旧 locator 失效，上传后重新获取 composer。

1. 使用 documentation 支持的文本输入方式写入完整 packet。
2. 从新 locator 读取 rendered text。
3. 必须同时看到 distinctive prefix 和唯一 `GPT56_SOL_PRO_RESULT_...` sentinel。
4. 缺少任一信号时停止并修复草稿；不要在未验证内容时点击 Send。

附件卡片或文件名不能替代 prompt 正文。

发送前在 ledger 记录 packet 内容 hash、prefix、sentinel 和可见附件名。eval 或审计时必须保留 Browser-side snapshot/截图或等价的工具证据；单独的代理输出文本不构成 proof。

## 5. 只发送一次并安全恢复

本地记录 dispatch state：

- `NOT_SENT`：确定未点击 Send。
- `SENT`：观察到用户 turn、清空的 composer 或 active generation。
- `UNKNOWN`：点击期间/之后连接中断，尚无提交证据。

发送前最后核对模型、prefix、sentinel 和附件名。点击一次 Send，只有观察到提交证据才记为 `SENT`。

在同一次 Browser run 的 ledger 中记录点击次数、时间、点击前后的 dispatch state 和提交后证据。不得只写“发送成功”而没有 Browser-side 观测。

`NOT_SENT` 时可恢复草稿后再发送；`SENT` 或 `UNKNOWN` 时只能恢复原 ChatGPT 对话并等待或抽取。无法唯一找到原对话时标记 incomplete，不冒险重复提交。

若恢复时看到的 tab 带有其他 task 的 Project、草稿或附件，即使 URL 属于 ChatGPT，也不视为原对话。只有 ledger 中的 Browser session、tab、conversation、prefix 与 sentinel 可唯一绑定时才允许恢复。

## 6. 等待、抽取与循环复审

在同一 tab 中观察生成状态。存在 stop control、thinking 状态或未完成 assistant turn 时继续等待，不刷新、不发送“继续”。

生成结束后只抽取最新完整 assistant turn，校验 sentinel 出现在 assistant 输出而不是用户 prompt。

完成前确认 assistant turn、sentinel、tab 与本轮 dispatch 都可关联到同一个 Browser session。无法关联时标记 `incomplete`，即使页面上存在看似正确的回复也不能宣称完成。

先记录 response 证据，不要在 finalize 前运行最终 validator。

Reviewer 模式到此返回本地采纳决策。Orchestrator loop 模式把 Codex 的实际 diff、测试、失败与剩余风险整理成下一轮 packet，发送到同一对话；每一轮仍执行安全扫描、模型核验、single-send 和 sentinel 验证。

## 7. 强制清理与释放

在所有需要的 Browser 读取完成后执行一次 `iab.tabs.finalize({ keep })`，并把它作为本 turn 的最后一个 Browser 动作；finalize 后不要再观察、截图或操作 Browser。

- 默认传入空 `keep`，关闭并释放本 task 创建的所有 tab。
- 只有用户需要查看已完成对话时，才把唯一成品 tab 标为 `deliverable`。
- 只有同一 task 明确暂停等待登录或人工操作，并且 tab 中没有草稿、附件或上传任务时，才可把唯一 tab 标为 `handoff`。
- 上传失败、附件残留、Project 污染、异常中断、超时、`UNKNOWN`、模型不可用和普通失败路径都必须 finalize；不得把污染 tab 保留为 handoff。
- 不要 claim、关闭或修改无法证明属于本 task 的用户 tab。隔离靠新建专用 tab，清理由本 task finalize 自己创建的 tab。

如果 Browser 调用已经中断而无法 finalize，明确记录 cleanup incomplete，并在下一次能连接同一 task Browser 时把清理作为第一动作；不得继续新的咨询发送。

finalize 返回后不再调用 Browser。把 finalize 结果、本次保留策略和发送前已确认的污染检查写入 ledger 的 `cleanup` 字段，再运行 `scripts/validate_session_evidence.py`。validator 未返回 `ok: true` 时，状态必须保持 `incomplete` 或 `failed`。
