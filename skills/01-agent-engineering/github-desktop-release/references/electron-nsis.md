# Electron / electron-builder / NSIS adapter

只在 preflight 和项目配置同时证明 Electron、electron-builder 与 NSIS 时使用本页。先核对当前 electron-builder、Electron、Node、包管理器与 NSIS 配置的官方文档；这些版本与命令不是跨项目常量。

## Qualification 顺序

1. 从冻结 commit 的 lockfile 解析包管理器和依赖版本，执行项目的 locked install。
2. 在 Windows runner 上执行项目的 build/package 入口，并把实际 runner/toolchain 写入 ledger。
3. 若项目共享原生 Node 模块，验证 Electron ABI 所需 rebuild、打包后的 smoke，以及回到开发 Node ABI 后的 restore/verify。不要因打包成功而假设开发 ABI 仍可用。
4. 对生成的 NSIS installer 做真实 install、launch、quiet-window、error-dialog、uninstall 和升级数据保留验证。离线或 local-only fixture 应避免浏览器/网络依赖。
5. 仅上传 contract 中列出的 installer、blockmap、updater metadata、manifest 和 acceptance evidence。

## 进程与窗口证据

一次进程观察至少绑定：

```text
PID + creation/start-time + canonical executable path + parent PID/start-time/path
```

仅 PID 会被重用；仅 exe 名称会碰撞；仅父 PID 也可能重用。采集失败、链路循环、父链过深或 path 无法确认时 fail closed。监视器要先启动并公布 ready 状态，launcher 要先写入 armed record，监视器确认根进程身份后才能放行目标命令。目标在 handshake 前快退即使返回 0 也不能视为验收成功。

Windows acceptance 要保存启动前后产品错误对话框快照，并且在被测树完全退出后保持有限 quiet window。quiet window 内新进程、错误对话框或身份不匹配都会重置或失败；不能只等待顶层 installer 返回。

## NSIS helper 的窄分类

electron-builder 的 NSIS 模板可能调用 PowerShell、`cmd.exe` 或 `find.exe` 做进程/能力 probe，其中 **精确** 的 no-match 分支会产生 `exit 1`。这不是全局成功码。

仅当以下条件全部成立时，才允许把 code 1 归为预期 probe：

1. code 确实为 1，且进程的 PID/start time/path/command line 已捕获；
2. image 是系统 PowerShell、`cmd.exe` 或 `find.exe` 的规范路径，不是同名任意文件；
3. command line 与项目已验证的 NSIS 模板 probe 完全匹配，而不是仅包含某个关键字；
4. 父链的每一边都由 PID、start time 和 path 匹配，且终止于同一次 armed installer/uninstaller root；
5. `cmd.exe` 与 `find.exe` 之间的关联也按精确父身份验证。

任何普通 PowerShell、任意 `find.exe`、未知命令行、缺失身份、另一个 Job Object 成员或非 1 的 exit 都是失败。不要添加“所有 helper exit 1 忽略”或按文件名/目录的宽泛 allowlist。

## TEMP 与 8.3 路径

NSIS uninstaller 可能复制到当前 TEMP 下的 `~nsu*.tmp` helper。`QueryFullProcessImageName` 有时给出 8.3 路径，因此只在以下狭窄情形规范化：文件仍可解析、解析后的完整路径位于可信的当前 TEMP 祖先内、名称与已验证的 NSIS helper 模式匹配、并且完整父链回到 armed root。不要因为路径字符串包含 `Temp`、`~` 或 `RUNNER~1` 就接受它，也不要为任意 TEMP executable 开豁免。

## 升级与卸载

升级验收应在安装前 seed 隔离的真实用户数据 fixture，在新版本安装/启动后验证预期 schema、项目、资产、recent-state 或其它 contract 列出的数据仍存在，再运行 uninstaller 并检查产品范围的残留。fixture 内容、旧版来源和断言写入 evidence；不要用“安装命令成功”替代数据保留证明。

## 常见边界

- 调整 NSIS、per-machine/per-user 或静默参数前先读项目配置与官方文档。
- 代码签名、自动更新、portable ZIP 和 release asset set 是独立决策；不要把 portable 文件混进 updater assets。
- 如 helper 分类要改动，先写 synthetic process-event 测试，覆盖合法 probe、相同名称但错误父链、PID reuse、未知 command line、8.3 非 TEMP 路径及 capture-before-exit 竞态。
