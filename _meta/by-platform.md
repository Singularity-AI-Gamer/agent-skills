# 按技术栈 / 平台索引

按“用什么技术”聚合检索。同一技能可能出现在多个相关章节（交叉引用），因此本索引的总行数会高于技能总数。

## 目录

- [Python 生态](#python-生态)
- [Kotlin / JVM 生态](#kotlin--jvm-生态)
- [Swift / Apple 生态](#swift--apple-生态)
- [Go 生态](#go-生态)
- [Rust 生态](#rust-生态)
- [C++ 生态](#c-生态)
- [Perl 生态](#perl-生态)
- [.NET / C# 生态](#net--c-生态)
- [PHP / Laravel 生态](#php--laravel-生态)
- [前端 / Web](#前端--web)
- [Flutter / Dart](#flutter--dart)
- [飞书（Lark）生态](#飞书lark生态)
- [Google Workspace](#google-workspace)
- [浏览器自动化](#浏览器自动化)
- [视频 / 影像生成](#视频--影像生成)
- [文档处理](#文档处理)
- [数据与研究](#数据与研究)
- [数据库](#数据库)
- [DevOps / 基础设施](#devops--基础设施)
- [测试与质量](#测试与质量)
- [Web3 / 区块链](#web3--区块链)
- [ECC / Harness 工具链](#ecc--harness-工具链)
- [AI API / LLM 平台](#ai-api--llm-平台)
- [Agent 工程与自治编排](#agent-工程与自治编排)
- [行业与业务](#行业与业务)
- [写作 / 营销 / 融资](#写作--营销--融资)
- [办公自动化 / 协作](#办公自动化--协作)
- [架构与编码规范](#架构与编码规范)
- [项目：Codex Invoice（发票识别）](#项目codex-invoice发票识别)
- [项目：ALK Plus Tracker](#项目alk-plus-tracker)

## Python 生态

Python 语言、测试、Django 全家桶、PyTorch、数据处理与 Python 驱动的内容生成工具。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **python-patterns** | [skills/02-coding-languages/python/python-patterns/](../skills/02-coding-languages/python/python-patterns/) | Python 的 Pythonic 惯用法、PEP 8、类型注解与工程最佳实践。 |
| **python-testing** | [skills/02-coding-languages/python/python-testing/](../skills/02-coding-languages/python/python-testing/) | Python 测试策略：pytest、TDD、fixtures、mock、参数化、覆盖率。 |
| **django-patterns** | [skills/03-frameworks/django/django-patterns/](../skills/03-frameworks/django/django-patterns/) | Django 架构模式、DRF REST 设计、ORM、缓存、signals、中间件、生产级实践。 |
| **django-tdd** | [skills/03-frameworks/django/django-tdd/](../skills/03-frameworks/django/django-tdd/) | Django 测试：pytest-django、TDD、factory_boy、mock、DRF API 测试。 |
| **django-security** | [skills/03-frameworks/django/django-security/](../skills/03-frameworks/django/django-security/) | Django 安全实践：认证、授权、CSRF、SQL/XSS 防护、安全部署配置。 |
| **django-verification** | [skills/03-frameworks/django/django-verification/](../skills/03-frameworks/django/django-verification/) | Django 项目的验证循环：迁移、lint、测试覆盖率、安全扫描、发布就绪检查。 |
| **pytorch-patterns** | [skills/02-coding-languages/general/pytorch-patterns/](../skills/02-coding-languages/general/pytorch-patterns/) | PyTorch 深度学习模式与最佳实践，构建稳定高效可复现的训练流水线。 |
| **pdf** | [skills/07-media-content/pdf/](../skills/07-media-content/pdf/) | 读写/审阅 PDF，倾向 Poppler 渲染做可视校验，用 reportlab/pdfplumber/pypdf。 |
| **docx** | [skills/07-media-content/docx/](../skills/07-media-content/docx/) | 全面处理 .docx：创建、编辑、修订跟踪、评论、格式保留与文本提取。 |
| **pptx** | [skills/07-media-content/pptx/](../skills/07-media-content/pptx/) | 演示文稿 .pptx 的创建、编辑、布局、评论与演讲者备注。 |
| **xlsx** | [skills/07-media-content/xlsx/](../skills/07-media-content/xlsx/) | 电子表格 .xlsx/.csv 等创建、编辑、公式、格式、数据分析与可视化。 |
| **manim-video** | [skills/07-media-content/manim-video/](../skills/07-media-content/manim-video/) | 构建可复用的 Manim 技术讲解动画，覆盖概念图、系统图、产品走查。 |
| **data-scraper-agent** | [skills/06-data-search/data-scraper-agent/](../skills/06-data-search/data-scraper-agent/) | 构建全自动 AI 数据采集 Agent：按计划抓取公开源并用 LLM 富化入库。 |

## Kotlin / JVM 生态

Kotlin 语言、Ktor、Exposed、协程与 Spring Boot、JPA、Java 规范等 JVM 栈。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **kotlin-patterns** | [skills/02-coding-languages/kotlin/kotlin-patterns/](../skills/02-coding-languages/kotlin/kotlin-patterns/) | Kotlin 惯用模式：协程、空安全、DSL 构建器，构建健壮可维护应用。 |
| **kotlin-testing** | [skills/02-coding-languages/kotlin/kotlin-testing/](../skills/02-coding-languages/kotlin/kotlin-testing/) | Kotlin 测试：Kotest、MockK、协程测试、属性测试、Kover 覆盖率，遵循 TDD。 |
| **kotlin-coroutines-flows** | [skills/02-coding-languages/kotlin/kotlin-coroutines-flows/](../skills/02-coding-languages/kotlin/kotlin-coroutines-flows/) | Android 与 KMP 的 Kotlin 协程和 Flow 模式：结构化并发、StateFlow、测试。 |
| **kotlin-ktor-patterns** | [skills/02-coding-languages/kotlin/kotlin-ktor-patterns/](../skills/02-coding-languages/kotlin/kotlin-ktor-patterns/) | Ktor 服务端模式：路由 DSL、插件、认证、Koin DI、序列化、WebSocket、testApplication。 |
| **kotlin-exposed-patterns** | [skills/02-coding-languages/kotlin/kotlin-exposed-patterns/](../skills/02-coding-languages/kotlin/kotlin-exposed-patterns/) | JetBrains Exposed ORM 模式：DSL、DAO、事务、HikariCP、Flyway、仓储。 |
| **compose-multiplatform-patterns** | [skills/03-frameworks/flutter/compose-multiplatform-patterns/](../skills/03-frameworks/flutter/compose-multiplatform-patterns/) | Compose Multiplatform 与 Jetpack Compose 的 KMP 模式：状态、导航、主题、性能、平台 UI。 |
| **android-clean-architecture** | [skills/03-frameworks/flutter/android-clean-architecture/](../skills/03-frameworks/flutter/android-clean-architecture/) | Android/KMP 的 Clean Architecture：模块划分、依赖规则、UseCase、Repository。 |
| **springboot-patterns** | [skills/03-frameworks/springboot/springboot-patterns/](../skills/03-frameworks/springboot/springboot-patterns/) | Spring Boot 架构：REST、分层服务、数据访问、缓存、异步、日志实践。 |
| **springboot-security** | [skills/03-frameworks/springboot/springboot-security/](../skills/03-frameworks/springboot/springboot-security/) | Spring Security 最佳实践：认证授权、校验、CSRF、机密、头、限流、依赖安全。 |
| **springboot-tdd** | [skills/03-frameworks/springboot/springboot-tdd/](../skills/03-frameworks/springboot/springboot-tdd/) | Spring Boot TDD：JUnit 5、Mockito、MockMvc、Testcontainers、JaCoCo。 |
| **springboot-verification** | [skills/03-frameworks/springboot/springboot-verification/](../skills/03-frameworks/springboot/springboot-verification/) | Spring Boot 项目验证循环：构建、静态分析、测试覆盖率、安全扫描、diff 审查。 |
| **jpa-patterns** | [skills/03-frameworks/springboot/jpa-patterns/](../skills/03-frameworks/springboot/jpa-patterns/) | JPA/Hibernate 实体设计、关联、查询优化、事务、审计、索引、分页与连接池。 |
| **java-coding-standards** | [skills/02-coding-languages/java/java-coding-standards/](../skills/02-coding-languages/java/java-coding-standards/) | Java/Spring Boot 的编码规范：命名、不可变、Optional、异常、泛型、目录布局。 |

## Swift / Apple 生态

Swift 语言与 Apple 平台（SwiftUI、端侧 FoundationModels、iOS 26 Liquid Glass）。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **swift-actor-persistence** | [skills/02-coding-languages/swift/swift-actor-persistence/](../skills/02-coding-languages/swift/swift-actor-persistence/) | 用 actor 实现线程安全的数据持久化：内存缓存加文件存储，从设计上消除竞态。 |
| **swift-concurrency-6-2** | [skills/02-coding-languages/swift/swift-concurrency-6-2/](../skills/02-coding-languages/swift/swift-concurrency-6-2/) | Swift 6.2 Approachable Concurrency：默认单线程、@concurrent 显式后台。 |
| **swift-protocol-di-testing** | [skills/02-coding-languages/swift/swift-protocol-di-testing/](../skills/02-coding-languages/swift/swift-protocol-di-testing/) | 基于协议的依赖注入，用聚焦协议和 Swift Testing 做可测试代码。 |
| **swiftui-patterns** | [skills/02-coding-languages/swift/swiftui-patterns/](../skills/02-coding-languages/swift/swiftui-patterns/) | SwiftUI 架构、@Observable 状态、视图组合、导航、性能优化、现代 UI 实践。 |
| **foundation-models-on-device** | [skills/02-coding-languages/swift/foundation-models-on-device/](../skills/02-coding-languages/swift/foundation-models-on-device/) | Apple FoundationModels 端侧 LLM：文本生成、@Generable、工具调用、快照流。 |
| **liquid-glass-design** | [skills/02-coding-languages/swift/liquid-glass-design/](../skills/02-coding-languages/swift/liquid-glass-design/) | iOS 26 Liquid Glass 设计系统：SwiftUI/UIKit/WidgetKit 的玻璃材质与交互。 |

## Go 生态

Go 语言的惯用模式与测试实践。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **golang-patterns** | [skills/02-coding-languages/golang/golang-patterns/](../skills/02-coding-languages/golang/golang-patterns/) | Go 的惯用模式与最佳实践，用于构建健壮高效的 Go 应用。 |
| **golang-testing** | [skills/02-coding-languages/golang/golang-testing/](../skills/02-coding-languages/golang/golang-testing/) | Go 测试：表驱动、subtest、基准测试、fuzzing、覆盖率，遵循 TDD。 |

## Rust 生态

Rust 语言的所有权模式、错误处理、并发与测试实践。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **rust-patterns** | [skills/02-coding-languages/rust/rust-patterns/](../skills/02-coding-languages/rust/rust-patterns/) | Rust 的惯用模式：所有权、错误处理、trait、并发，构建安全高性能应用。 |
| **rust-testing** | [skills/02-coding-languages/rust/rust-testing/](../skills/02-coding-languages/rust/rust-testing/) | Rust 测试：单元、集成、异步、属性测试、mock 与覆盖率，遵循 TDD。 |

## C++ 生态

现代 C++ 编码规范与测试实践。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **cpp-coding-standards** | [skills/02-coding-languages/cpp/cpp-coding-standards/](../skills/02-coding-languages/cpp/cpp-coding-standards/) | 基于 C++ Core Guidelines 的编码规范，强化现代、安全、地道的 C++ 写法。 |
| **cpp-testing** | [skills/02-coding-languages/cpp/cpp-testing/](../skills/02-coding-languages/cpp/cpp-testing/) | C++ 测试：GoogleTest/CTest 配置、诊断 flaky 测试、覆盖率与 sanitizer。 |

## Perl 生态

现代 Perl 5.36+ 的惯用法、安全与测试。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **perl-patterns** | [skills/02-coding-languages/perl/perl-patterns/](../skills/02-coding-languages/perl/perl-patterns/) | 现代 Perl 5.36+ 惯用法与最佳实践，构建健壮可维护的 Perl 应用。 |
| **perl-security** | [skills/02-coding-languages/perl/perl-security/](../skills/02-coding-languages/perl/perl-security/) | Perl 安全：taint 模式、输入校验、DBI 参数化、Web 安全、perlcritic 策略。 |
| **perl-testing** | [skills/02-coding-languages/perl/perl-testing/](../skills/02-coding-languages/perl/perl-testing/) | Perl 测试：Test2::V0、Test::More、prove、mock、Devel::Cover 覆盖率。 |

## .NET / C# 生态

.NET 惯用模式与 C# 测试实践。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **dotnet-patterns** | [skills/02-coding-languages/dotnet/dotnet-patterns/](../skills/02-coding-languages/dotnet/dotnet-patterns/) | .NET 惯用模式：依赖注入、async/await、构建健壮可维护的 .NET 应用。 |
| **csharp-testing** | [skills/02-coding-languages/csharp/csharp-testing/](../skills/02-coding-languages/csharp/csharp-testing/) | C#/.NET 测试：xUnit、FluentAssertions、mock、集成测试与组织实践。 |

## PHP / Laravel 生态

Laravel 框架的架构、安全、TDD、验证与插件发现。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **laravel-patterns** | [skills/03-frameworks/laravel/laravel-patterns/](../skills/03-frameworks/laravel/laravel-patterns/) | Laravel 架构：路由控制器、Eloquent、服务层、队列、事件、缓存、API Resource。 |
| **laravel-security** | [skills/03-frameworks/laravel/laravel-security/](../skills/03-frameworks/laravel/laravel-security/) | Laravel 安全：认证授权、校验、CSRF、批量赋值、文件上传、限流与部署。 |
| **laravel-tdd** | [skills/03-frameworks/laravel/laravel-tdd/](../skills/03-frameworks/laravel/laravel-tdd/) | Laravel TDD：PHPUnit/Pest、factories、数据库测试、fakes、覆盖率。 |
| **laravel-verification** | [skills/03-frameworks/laravel/laravel-verification/](../skills/03-frameworks/laravel/laravel-verification/) | Laravel 验证循环：env 检查、lint、静态分析、测试覆盖率、安全扫描。 |
| **laravel-plugin-discovery** | [skills/03-frameworks/laravel/laravel-plugin-discovery/](../skills/03-frameworks/laravel/laravel-plugin-discovery/) | 通过 LaraPlugins.io MCP 发现与评估 Laravel 包及兼容性。 |

## 前端 / Web

React、Next.js、Nuxt、NestJS、React Native 与前端设计/切图工作流。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **frontend-patterns** | [skills/03-frameworks/nextjs/frontend-patterns/](../skills/03-frameworks/nextjs/frontend-patterns/) | 前端开发模式：React、Next.js、状态管理、性能优化、UI 最佳实践。 |
| **frontend-design** | [skills/07-media-content/frontend-design/](../skills/07-media-content/frontend-design/) | 生产级高质量前端界面设计，在视觉方向与代码质量之间做深度平衡。 |
| **frontend-slides** | [skills/07-media-content/frontend-slides/](../skills/07-media-content/frontend-slides/) | 从零或从 PPT 转出动画丰富的 HTML 幻灯片，引导非设计师发现美学方向。 |
| **vercel-react-best-practices** | [skills/03-frameworks/nextjs/vercel-react-best-practices/](../skills/03-frameworks/nextjs/vercel-react-best-practices/) | Vercel 工程出品的 React/Next.js 性能优化指引，含组件、数据获取、打包。 |
| **nextjs-turbopack** | [skills/03-frameworks/nextjs/nextjs-turbopack/](../skills/03-frameworks/nextjs/nextjs-turbopack/) | Next.js 16+ 与 Turbopack：增量打包、FS 缓存、开发速度、vs webpack。 |
| **nuxt4-patterns** | [skills/03-frameworks/nuxt/nuxt4-patterns/](../skills/03-frameworks/nuxt/nuxt4-patterns/) | Nuxt 4 模式：Hydration 安全、路由规则、懒加载、SSR 安全数据获取。 |
| **nestjs-patterns** | [skills/03-frameworks/nestjs/nestjs-patterns/](../skills/03-frameworks/nestjs/nestjs-patterns/) | NestJS 架构：模块、控制器、provider、DTO 校验、guard、拦截器、配置。 |
| **vercel-react-native-skills** | [skills/03-frameworks/react-native/vercel-react-native-skills/](../skills/03-frameworks/react-native/vercel-react-native-skills/) | React Native + Expo 构建高性能移动应用的最佳实践。 |
| **design-system** | [skills/07-media-content/design-system/](../skills/07-media-content/design-system/) | 生成或审计设计系统，检查视觉一致性并审查样式相关 PR。 |
| **bun-runtime** | [skills/02-coding-languages/general/bun-runtime/](../skills/02-coding-languages/general/bun-runtime/) | Bun 作为 runtime/包管理/打包/测试运行器，及 Node 迁移与 Vercel 支持。 |

## Flutter / Dart

Flutter/Dart 生产级模式与跨库代码审查。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **dart-flutter-patterns** | [skills/03-frameworks/flutter/dart-flutter-patterns/](../skills/03-frameworks/flutter/dart-flutter-patterns/) | 生产级 Dart/Flutter 模式：空安全、BLoC/Riverpod、GoRouter、Dio、Freezed、清晰架构。 |
| **flutter-dart-code-review** | [skills/03-frameworks/flutter/flutter-dart-code-review/](../skills/03-frameworks/flutter/flutter-dart-code-review/) | 跨库 Flutter/Dart 代码审查清单：widget、状态管理、性能、可访问性、清洁架构。 |

## 飞书（Lark）生态

飞书全家桶：IM、文档、多维表格、画板、日历、邮箱、妙记、审批、视频会议、任务、知识库、开放平台工作流。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **lark-shared** | [skills/09-ops-productivity/lark/lark-shared/](../skills/09-ops-productivity/lark/lark-shared/) | lark-cli 共享基础：配置、登录、身份切换、scope 与权限错误处理。 |
| **lark-skill-maker** | [skills/09-ops-productivity/lark/lark-skill-maker/](../skills/09-ops-productivity/lark/lark-skill-maker/) | 创建 lark-cli 自定义 Skill：包装原子 API 或编排多步 API 流程。 |
| **lark-openapi-explorer** | [skills/09-ops-productivity/lark/lark-openapi-explorer/](../skills/09-ops-productivity/lark/lark-openapi-explorer/) | 飞书原生 OpenAPI 探索：当 lark-* skill 未覆盖时查询原生接口。 |
| **lark-im** | [skills/09-ops-productivity/lark/lark-im/](../skills/09-ops-productivity/lark/lark-im/) | 飞书即时通讯：收发消息、搜聊天记录、管理群聊、上传下载图片文件。 |
| **lark-doc** | [skills/09-ops-productivity/lark/lark-doc/](../skills/09-ops-productivity/lark/lark-doc/) | 飞书云文档：创建与编辑文档，从 Markdown 生成，文档搜索与资源定位。 |
| **lark-sheets** | [skills/09-ops-productivity/lark/lark-sheets/](../skills/09-ops-productivity/lark/lark-sheets/) | 飞书电子表格：创建、读写、追加、查找、导出，与 docs 搜索分工。 |
| **lark-slides** | [skills/09-ops-productivity/lark/lark-slides/](../skills/09-ops-productivity/lark/lark-slides/) | 飞书幻灯片：用 XML 读取与管理 PPT 页面，创建演示优先用 +create。 |
| **lark-drive** | [skills/09-ops-productivity/lark/lark-drive/](../skills/09-ops-productivity/lark/lark-drive/) | 飞书云空间：文件与文件夹管理、评论、权限、本地文件导入为在线云文档。 |
| **lark-base** | [skills/09-ops-productivity/lark/lark-base/](../skills/09-ops-productivity/lark/lark-base/) | lark-cli 操作飞书多维表格（Base）：建表、字段、记录、视图、工作流、分析。 |
| **lark-wiki** | [skills/09-ops-productivity/lark/lark-wiki/](../skills/09-ops-productivity/lark/lark-wiki/) | 飞书知识库：管理知识空间与节点层级、组织文档与快捷方式。 |
| **lark-calendar** | [skills/09-ops-productivity/lark/lark-calendar/](../skills/09-ops-productivity/lark/lark-calendar/) | 飞书日历：日程与会议管理、忙闲查询、会议室预定等。 |
| **lark-task** | [skills/09-ops-productivity/lark/lark-task/](../skills/09-ops-productivity/lark/lark-task/) | 飞书任务：创建待办、管理任务状态与子任务、组织任务清单、分配协作。 |
| **lark-approval** | [skills/09-ops-productivity/lark/lark-approval/](../skills/09-ops-productivity/lark/lark-approval/) | 飞书审批 API：审批实例与审批任务的全量管理。 |
| **lark-mail** | [skills/09-ops-productivity/lark/lark-mail/](../skills/09-ops-productivity/lark/lark-mail/) | 飞书邮箱：草稿、编辑、发送、回复、转发、搜索、附件、文件夹、规则。 |
| **lark-contact** | [skills/09-ops-productivity/lark/lark-contact/](../skills/09-ops-productivity/lark/lark-contact/) | 飞书通讯录：查询组织架构、人员信息、按关键词搜索员工。 |
| **lark-event** | [skills/09-ops-productivity/lark/lark-event/](../skills/09-ops-productivity/lark/lark-event/) | 飞书事件订阅：通过 WebSocket 长连接实时监听事件并输出 NDJSON。 |
| **lark-minutes** | [skills/09-ops-productivity/lark/lark-minutes/](../skills/09-ops-productivity/lark/lark-minutes/) | 飞书妙记：查询与获取妙记信息、下载音视频、获取 AI 总结/待办/章节。 |
| **lark-vc** | [skills/09-ops-productivity/lark/lark-vc/](../skills/09-ops-productivity/lark/lark-vc/) | 飞书视频会议：查询会议记录与纪要（总结、待办、章节、逐字稿）。 |
| **lark-whiteboard** | [skills/09-ops-productivity/lark/lark-whiteboard/](../skills/09-ops-productivity/lark/lark-whiteboard/) | 飞书画板：导出预览、节点结构，用 PlantUML/Mermaid 或 OpenAPI 编辑画板。 |
| **lark-whiteboard-cli** | [skills/09-ops-productivity/lark/lark-whiteboard-cli/](../skills/09-ops-productivity/lark/lark-whiteboard-cli/) | 用 whiteboard-cli 在飞书画板绘制架构图、流程图、思维导图等的布局指南。 |
| **lark-workflow-meeting-summary** | [skills/09-ops-productivity/lark/lark-workflow-meeting-summary/](../skills/09-ops-productivity/lark/lark-workflow-meeting-summary/) | 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。 |
| **lark-workflow-standup-report** | [skills/09-ops-productivity/lark/lark-workflow-standup-report/](../skills/09-ops-productivity/lark/lark-workflow-standup-report/) | 日程待办摘要：编排 calendar 与 task，生成指定日期的日程与未完成任务摘要。 |
| **feishu-automation** | [projects/ai-seed-project/feishu-automation/](../projects/ai-seed-project/feishu-automation/) | 飞书自动化能力，优先用官方 OpenAPI MCP/CLI，不把后台配置动作误判为 MCP 能力。 |
| **feishu-card-ws** | [projects/ai-seed-project-phase-one-feishu/feishu-card-ws/](../projects/ai-seed-project-phase-one-feishu/feishu-card-ws/) | 飞书交互式卡片在 WebSocket 长连接模式下的配置指南与回调处理。 |

## Google Workspace

Google Drive/Docs/Sheets/Slides 统一运营面板。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **google-workspace-ops** | [skills/09-ops-productivity/google-workspace/google-workspace-ops/](../skills/09-ops-productivity/google-workspace/google-workspace-ops/) | 把 Google Drive/Docs/Sheets/Slides 作为一个工作流面板统一操作。 |

## 浏览器自动化

agent-browser、Playwright、Browser Use、AgentCore、远端浏览器、CDP/Electron 与 Vercel Sandbox。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **agent-browser** | [skills/01-agent-engineering/agent-browser/](../skills/01-agent-engineering/agent-browser/) | AI Agent 的浏览器自动化 CLI，用于网页导航、表单填写、截图、数据抓取。 |
| **browser-use** | [skills/01-agent-engineering/browser-use/](../skills/01-agent-engineering/browser-use/) | 浏览器交互自动化，用于网页测试、表单填写、截图、数据提取。 |
| **agentcore** | [skills/01-agent-engineering/agentcore/](../skills/01-agent-engineering/agentcore/) | 在 AWS Bedrock AgentCore 云端浏览器上运行 agent-browser。 |
| **remote-browser** | [skills/01-agent-engineering/remote-browser/](../skills/01-agent-engineering/remote-browser/) | 在沙箱远端机器上控制本地浏览器，用于无 GUI 沙箱场景。 |
| **vercel-sandbox** | [skills/01-agent-engineering/vercel-sandbox/](../skills/01-agent-engineering/vercel-sandbox/) | 在 Vercel Sandbox 微型 VM 中运行 agent-browser + Chrome 做浏览器自动化。 |
| **electron** | [skills/01-agent-engineering/electron/](../skills/01-agent-engineering/electron/) | 通过 CDP 用 agent-browser 自动化 Electron 桌面应用（VS Code、Slack 等）。 |
| **playwright** | [skills/04-testing-quality/playwright/](../skills/04-testing-quality/playwright/) | 用 playwright-cli 从终端自动化真实浏览器做导航、表单、截图、UI 调试。 |
| **browser-qa** | [skills/01-agent-engineering/browser-qa/](../skills/01-agent-engineering/browser-qa/) | 部署功能后自动化视觉测试与 UI 交互验证。 |
| **slack** | [skills/09-ops-productivity/general/slack/](../skills/09-ops-productivity/general/slack/) | 通过浏览器自动化在 Slack 中检查未读、导航、发消息、搜对话、抓取信息。 |
| **dogfood** | [skills/01-agent-engineering/dogfood/](../skills/01-agent-engineering/dogfood/) | 系统化测试 Web 应用以发现 Bug、UX 问题，输出带截图和复现步骤的报告。 |
| **ui-demo** | [skills/07-media-content/ui-demo/](../skills/07-media-content/ui-demo/) | 用 Playwright 录制精致的 UI demo/讲解/教学视频，生成带光标的 WebM。 |
| **cloud** | [skills/01-agent-engineering/cloud/](../skills/01-agent-engineering/cloud/) | Browser Use Cloud 托管 API 与 SDK 的文档参考。 |
| **open-source** | [skills/01-agent-engineering/open-source/](../skills/01-agent-engineering/open-source/) | browser-use 开源 Python 库的文档参考（Agent/Browser/Tools 配置）。 |

## 视频 / 影像生成

视频创作全链路：Manim、Remotion、剪映、VideoDB、fal.ai、create-promo-video 等。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **manim-video** | [skills/07-media-content/manim-video/](../skills/07-media-content/manim-video/) | 构建可复用的 Manim 技术讲解动画，覆盖概念图、系统图、产品走查。 |
| **remotion-video-creation** | [skills/07-media-content/remotion-video-creation/](../skills/07-media-content/remotion-video-creation/) | Remotion 在 React 中做视频创作的 29 条领域规则（3D、动画、字幕、过渡）。 |
| **video-editing** | [skills/07-media-content/video-editing/](../skills/07-media-content/video-editing/) | AI 辅助视频剪辑全流程：FFmpeg、Remotion、ElevenLabs、fal.ai 到 Descript。 |
| **videodb** | [skills/07-media-content/videodb/](../skills/07-media-content/videodb/) | 对视频/音频 See-Understand-Act：摄取、索引、时间线编辑、生成、实时报警。 |
| **jianying-editor** | [skills/07-media-content/jianying-editor/](../skills/07-media-content/jianying-editor/) | 剪映 AI 自动剪辑高级封装 API（JyWrapper）：录屏、素材、字幕、Web 动效。 |
| **ui-demo** | [skills/07-media-content/ui-demo/](../skills/07-media-content/ui-demo/) | 用 Playwright 录制精致的 UI demo/讲解/教学视频，生成带光标的 WebM。 |
| **fal-ai-media** | [skills/07-media-content/fal-ai-media/](../skills/07-media-content/fal-ai-media/) | 基于 fal.ai MCP 的统一媒体生成：文生图、图/文生视频、TTS、视频转音频。 |
| **ai-music-generation** | [projects/content-assets/ai-music-generation/](../projects/content-assets/ai-music-generation/) | 通过 inference.sh 生成 AI 音乐/歌曲，支持 ElevenLabs、Diffrythm、腾讯歌曲生成。 |
| **create-promo-video** | [projects/content-assets/create-promo-video/](../projects/content-assets/create-promo-video/) | 为项目生成 TikTok 风格短宣传片，分析代码库后用 Remotion 输出竖版/横版。 |
| **video-producer** | [projects/content-assets/video-producer/](../projects/content-assets/video-producer/) | 端到端 Remotion 视频制作：叙事、场景动画、视觉风格、渲染全链路编排。 |

## 文档处理

PDF/DOCX/PPTX/XLSX 读写、Nutrient 文档处理、前端切片、签证翻译与 NotebookLM 转换。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **pdf** | [skills/07-media-content/pdf/](../skills/07-media-content/pdf/) | 读写/审阅 PDF，倾向 Poppler 渲染做可视校验，用 reportlab/pdfplumber/pypdf。 |
| **docx** | [skills/07-media-content/docx/](../skills/07-media-content/docx/) | 全面处理 .docx：创建、编辑、修订跟踪、评论、格式保留与文本提取。 |
| **pptx** | [skills/07-media-content/pptx/](../skills/07-media-content/pptx/) | 演示文稿 .pptx 的创建、编辑、布局、评论与演讲者备注。 |
| **xlsx** | [skills/07-media-content/xlsx/](../skills/07-media-content/xlsx/) | 电子表格 .xlsx/.csv 等创建、编辑、公式、格式、数据分析与可视化。 |
| **frontend-slides** | [skills/07-media-content/frontend-slides/](../skills/07-media-content/frontend-slides/) | 从零或从 PPT 转出动画丰富的 HTML 幻灯片，引导非设计师发现美学方向。 |
| **nutrient-document-processing** | [skills/07-media-content/nutrient-document-processing/](../skills/07-media-content/nutrient-document-processing/) | 用 Nutrient DWS API 处理文档：转换、OCR、提取、脱敏、签章、表单填充。 |
| **visa-doc-translate** | [skills/07-media-content/visa-doc-translate/](../skills/07-media-content/visa-doc-translate/) | 签证申请文件图片翻译并生成中英双语 PDF。 |
| **anything-to-notebooklm** | [skills/07-media-content/anything-to-notebooklm/](../skills/07-media-content/anything-to-notebooklm/) | 多源内容处理器：公众号、网页、YouTube、PDF、MD 上传 NotebookLM 并转播客/PPT。 |

## 数据与研究

深度研究、神经搜索、PubMed、数据采集、线索情报、社交图谱与市场研究。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **deep-research** | [skills/06-data-search/deep-research/](../skills/06-data-search/deep-research/) | 基于 firecrawl/exa MCP 的多源深度研究，合成带引用的研究报告。 |
| **exa-search** | [skills/06-data-search/exa-search/](../skills/06-data-search/exa-search/) | 通过 Exa MCP 做 Web、代码与公司研究的神经搜索。 |
| **research-ops** | [skills/06-data-search/research-ops/](../skills/06-data-search/research-ops/) | 证据优先的现状研究工作流：基于当前公开证据与本地上下文给结论。 |
| **market-research** | [skills/06-data-search/market-research/](../skills/06-data-search/market-research/) | 市场研究、竞品分析、投资尽调、行业情报，带源引用与决策导向摘要。 |
| **market-research-reports** | [skills/08-writing-marketing/market-research-reports/](../skills/08-writing-marketing/market-research-reports/) | 生成 50+ 页顶级咨询公司风格市场研究报告，专业 LaTeX 格式，多框架分析。 |
| **pubmed-search** | [skills/06-data-search/pubmed-search/](../skills/06-data-search/pubmed-search/) | 通过 Valyu 语义搜索以自然语言检索 PubMed 生物医学文献，支持全文。 |
| **medical-research** | [skills/06-data-search/medical-research/](../skills/06-data-search/medical-research/) | 从 PubMed 获取论文并生成通俗易懂的研究摘要，覆盖医学/临床/科研主题。 |
| **data-scraper-agent** | [skills/06-data-search/data-scraper-agent/](../skills/06-data-search/data-scraper-agent/) | 构建全自动 AI 数据采集 Agent：按计划抓取公开源并用 LLM 富化入库。 |
| **knowledge-ops** | [skills/06-data-search/knowledge-ops/](../skills/06-data-search/knowledge-ops/) | 跨本地文件、MCP 记忆、向量库、Git 的知识库摄取、同步、去重与检索。 |
| **lead-intelligence** | [skills/06-data-search/lead-intelligence/](../skills/06-data-search/lead-intelligence/) | AI 线索情报与外联流水线：信号评分、路径发现、源派生声线、多渠道外联。 |
| **social-graph-ranker** | [skills/06-data-search/social-graph-ranker/](../skills/06-data-search/social-graph-ranker/) | 加权社交图排序引擎：暖介绍发现、桥接评分、X/LinkedIn 网络缺口分析。 |
| **database-migrations** | [skills/06-data-search/database-migrations/](../skills/06-data-search/database-migrations/) | 数据库迁移最佳实践：Schema 变更、数据迁移、回滚、零停机跨 DB/ORM。 |

## 数据库

PostgreSQL、ClickHouse、JPA/Hibernate、Kotlin Exposed 与迁移模式。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **postgres-patterns** | [skills/05-devops-infra/postgres-patterns/](../skills/05-devops-infra/postgres-patterns/) | PostgreSQL 查询优化、Schema 设计、索引与安全，基于 Supabase 最佳实践。 |
| **clickhouse-io** | [skills/05-devops-infra/clickhouse-io/](../skills/05-devops-infra/clickhouse-io/) | ClickHouse 数据库模式：查询优化、分析与高性能分析型负载的工程实践。 |
| **jpa-patterns** | [skills/03-frameworks/springboot/jpa-patterns/](../skills/03-frameworks/springboot/jpa-patterns/) | JPA/Hibernate 实体设计、关联、查询优化、事务、审计、索引、分页与连接池。 |
| **kotlin-exposed-patterns** | [skills/02-coding-languages/kotlin/kotlin-exposed-patterns/](../skills/02-coding-languages/kotlin/kotlin-exposed-patterns/) | JetBrains Exposed ORM 模式：DSL、DAO、事务、HikariCP、Flyway、仓储。 |
| **database-migrations** | [skills/06-data-search/database-migrations/](../skills/06-data-search/database-migrations/) | 数据库迁移最佳实践：Schema 变更、数据迁移、回滚、零停机跨 DB/ORM。 |

## DevOps / 基础设施

Docker、部署流水线、监控仪表板、API 连接器、云运维（阿里云 SWAS）。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **docker-patterns** | [skills/05-devops-infra/docker-patterns/](../skills/05-devops-infra/docker-patterns/) | Docker 与 Compose 模式：本地开发、容器安全、网络、卷策略、多服务编排。 |
| **deployment-patterns** | [skills/05-devops-infra/deployment-patterns/](../skills/05-devops-infra/deployment-patterns/) | 部署与 CI/CD 流水线、容器化、健康检查、回滚、上线检查单。 |
| **dashboard-builder** | [skills/09-ops-productivity/general/dashboard-builder/](../skills/09-ops-productivity/general/dashboard-builder/) | 为 Grafana/SigNoz 等构建回答真实运维问题的监控仪表板，而非面子工程。 |
| **api-connector-builder** | [skills/09-ops-productivity/general/api-connector-builder/](../skills/09-ops-productivity/general/api-connector-builder/) | 新增 API 连接器/provider 时，严格贴合目标仓库现有集成模式，不造二套架构。 |
| **aliyun-openapi-mcp-ops** | [projects/ai-seed-project/aliyun-openapi-mcp-ops/](../projects/ai-seed-project/aliyun-openapi-mcp-ops/) | 通过自建 OpenAPI MCP 运维阿里云，聚焦 SWAS 部署：OAuth、选择器更新、诊断、预发验证。 |
| **aliyun-swas-manage** | [projects/ai-seed-project-phase-one-feishu/aliyun-swas-manage/](../projects/ai-seed-project-phase-one-feishu/aliyun-swas-manage/) | 端到端管理阿里云 SWAS：实例、命令、磁盘快照、防火墙、监控与轻量数据库。 |

## 测试与质量

E2E、TDD、eval-harness、回归、canary、安全审查与代码走读。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **e2e-testing** | [skills/04-testing-quality/e2e-testing/](../skills/04-testing-quality/e2e-testing/) | Playwright E2E 模式：Page Object、配置、CI/CD、产物、flaky 策略。 |
| **tdd-workflow** | [skills/04-testing-quality/tdd-workflow/](../skills/04-testing-quality/tdd-workflow/) | 新功能/bug 修复/重构时强制 TDD，单元+集成+E2E 覆盖率 80%+。 |
| **playwright** | [skills/04-testing-quality/playwright/](../skills/04-testing-quality/playwright/) | 用 playwright-cli 从终端自动化真实浏览器做导航、表单、截图、UI 调试。 |
| **ai-regression-testing** | [skills/04-testing-quality/ai-regression-testing/](../skills/04-testing-quality/ai-regression-testing/) | AI 辅助开发的回归策略：sandbox API 测试、自动 Bug 检查、规避盲点。 |
| **eval-harness** | [skills/04-testing-quality/eval-harness/](../skills/04-testing-quality/eval-harness/) | Claude Code 会话的正式评测框架，实践 eval-driven development。 |
| **benchmark** | [skills/04-testing-quality/benchmark/](../skills/04-testing-quality/benchmark/) | 度量性能基线、PR 前后回归检测、技术栈方案对比。 |
| **canary-watch** | [skills/04-testing-quality/canary-watch/](../skills/04-testing-quality/canary-watch/) | 发布、合并、依赖升级后监控部署 URL 的回归情况。 |
| **click-path-audit** | [skills/04-testing-quality/click-path-audit/](../skills/04-testing-quality/click-path-audit/) | 追踪每个用户按钮的完整状态变更序列，发现功能各自正确但相互抵消的 bug。 |
| **security-review** | [skills/04-testing-quality/security-review/](../skills/04-testing-quality/security-review/) | 新增认证、输入处理、密钥、API、支付等场景的安全审查清单。 |
| **security-scan** | [skills/04-testing-quality/security-scan/](../skills/04-testing-quality/security-scan/) | 用 AgentShield 扫描 .claude 目录的安全漏洞、配置错误与注入风险。 |
| **security-bounty-hunter** | [skills/04-testing-quality/security-bounty-hunter/](../skills/04-testing-quality/security-bounty-hunter/) | 聚焦远程可达、能提交赏金报告的漏洞，过滤噪声式本地发现。 |
| **code-tour** | [skills/04-testing-quality/code-tour/](../skills/04-testing-quality/code-tour/) | 生成 CodeTour `.tour`：分角色、带文件行号锚点的分步导览。 |

## Web3 / 区块链

DeFi AMM 安全、EVM 跨链十进制、LLM 交易 Agent 安全、Keccak256 坑位、Agent 支付。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **defi-amm-security** | [skills/11-web3/defi-amm-security/](../skills/11-web3/defi-amm-security/) | Solidity AMM 合约、流动性池与换币流程的安全清单（重入、预言机操纵、滑点等）。 |
| **evm-token-decimals** | [skills/11-web3/evm-token-decimals/](../skills/11-web3/evm-token-decimals/) | 防范 EVM 跨链的十进制错配 bug：运行时查询、链感知缓存、桥接代币精度漂移。 |
| **llm-trading-agent-security** | [skills/11-web3/llm-trading-agent-security/](../skills/11-web3/llm-trading-agent-security/) | 自治交易 Agent 的安全：prompt 注入、消费上限、发送前模拟、熔断、MEV 防护。 |
| **nodejs-keccak256** | [skills/02-coding-languages/general/nodejs-keccak256/](../skills/02-coding-languages/general/nodejs-keccak256/) | 防范 JS/TS 的以太坊哈希坑：Node 的 sha3-256 不是 Keccak-256。 |
| **agent-payment-x402** | [skills/01-agent-engineering/agent-payment-x402/](../skills/01-agent-engineering/agent-payment-x402/) | 为 Agent 接入 x402 支付执行能力，含任务预算、支出控制、非托管钱包。 |

## ECC / Harness 工具链

ECC 插件生态的安装、配置、审计、盘点、规则蒸馏、团队编排、合规校验等治理工具。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **configure-ecc** | [skills/01-agent-engineering/configure-ecc/](../skills/01-agent-engineering/configure-ecc/) | ECC 的交互式安装器，选择并安装 skills/rules 到用户或项目目录。 |
| **ecc-tools-cost-audit** | [skills/09-ops-productivity/general/ecc-tools-cost-audit/](../skills/09-ops-productivity/general/ecc-tools-cost-audit/) | 证据优先的 ECC Tools 消耗与账单审计：PR 失控、配额绕过、溢价模型泄漏。 |
| **hookify-rules** | [skills/01-agent-engineering/hookify-rules/](../skills/01-agent-engineering/hookify-rules/) | 创建 hookify 规则的语法与模式指南。 |
| **rules-distill** | [skills/01-agent-engineering/rules-distill/](../skills/01-agent-engineering/rules-distill/) | 扫描 skills 抽取横切原则，蒸馏成 rules，可追加、修订或新建规则文件。 |
| **team-builder** | [skills/01-agent-engineering/team-builder/](../skills/01-agent-engineering/team-builder/) | 交互式 Agent 选择器，用于组合并派发并行团队。 |
| **skill-creator** | [skills/01-agent-engineering/skill-creator/](../skills/01-agent-engineering/skill-creator/) | 创建、修改和优化 skill，并可跑 eval 衡量触发准确率与性能。 |
| **skill-stocktake** | [skills/01-agent-engineering/skill-stocktake/](../skills/01-agent-engineering/skill-stocktake/) | 盘点和评估 Claude skill/command 质量，支持快速扫描和全量盘点模式。 |
| **skill-comply** | [skills/01-agent-engineering/skill-comply/](../skills/01-agent-engineering/skill-comply/) | 可视化 skill/rule/agent 是否真的被遵守，自动生成场景并报合规率。 |
| **agent-sort** | [skills/01-agent-engineering/agent-sort/](../skills/01-agent-engineering/agent-sort/) | 按 DAILY/LIBRARY 分类 ECC 的 skills/commands/rules，为特定仓库生成精简安装清单。 |
| **workspace-surface-audit** | [skills/01-agent-engineering/workspace-surface-audit/](../skills/01-agent-engineering/workspace-surface-audit/) | 审计当前仓库、MCP、插件、连接器，推荐最高价值的 ECC skills/hooks。 |
| **automation-audit-ops** | [skills/09-ops-productivity/general/automation-audit-ops/](../skills/09-ops-productivity/general/automation-audit-ops/) | ECC 自动化证据优先盘点：看哪些 jobs/hooks/连接器在跑、坏了、冗余或缺失。 |
| **context-budget** | [skills/01-agent-engineering/context-budget/](../skills/01-agent-engineering/context-budget/) | 审计 Claude Code 上下文窗口消耗，识别膨胀与冗余并给 Token 优化建议。 |
| **strategic-compact** | [skills/01-agent-engineering/strategic-compact/](../skills/01-agent-engineering/strategic-compact/) | 在任务阶段分界处建议手动压缩上下文，替代随意的自动压缩。 |
| **find-skill** | [skills/01-agent-engineering/find-skill/](../skills/01-agent-engineering/find-skill/) | 技能发现入口（文件体为空，疑似占位）。 |
| **find-skills** | [skills/01-agent-engineering/find-skills/](../skills/01-agent-engineering/find-skills/) | 自动发现与推荐可用 Agent 技能，回答"有没有能做 X 的技能"。 |
| **verification-loop** | [skills/01-agent-engineering/verification-loop/](../skills/01-agent-engineering/verification-loop/) | Claude Code 会话的综合验证系统。 |
| **prompt-optimizer** | [skills/01-agent-engineering/prompt-optimizer/](../skills/01-agent-engineering/prompt-optimizer/) | 分析原始 prompt，匹配 ECC 组件并输出可粘贴的优化版，仅作顾问不执行。 |

## AI API / LLM 平台

Claude API、端侧模型、Token 预算、成本路由、迭代检索、正则 vs LLM 决策。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **claude-api** | [skills/12-ai-api/claude-api/](../skills/12-ai-api/claude-api/) | Anthropic Claude API（Python/TS）：Messages、流式、工具、视觉、批处理、缓存、Agent SDK。 |
| **foundation-models-on-device** | [skills/02-coding-languages/swift/foundation-models-on-device/](../skills/02-coding-languages/swift/foundation-models-on-device/) | Apple FoundationModels 端侧 LLM：文本生成、@Generable、工具调用、快照流。 |
| **token-budget-advisor** | [skills/12-ai-api/token-budget-advisor/](../skills/12-ai-api/token-budget-advisor/) | 在回答前给用户选择响应深度与 Token 预算的顾问式工作流。 |
| **cost-aware-llm-pipeline** | [skills/02-coding-languages/general/cost-aware-llm-pipeline/](../skills/02-coding-languages/general/cost-aware-llm-pipeline/) | LLM API 成本优化：按复杂度做模型路由、预算追踪、重试、Prompt 缓存。 |
| **iterative-retrieval** | [skills/01-agent-engineering/iterative-retrieval/](../skills/01-agent-engineering/iterative-retrieval/) | 渐进式精炼检索上下文的模式，用于解决 subagent 上下文问题。 |
| **regex-vs-llm-structured-text** | [skills/02-coding-languages/general/regex-vs-llm-structured-text/](../skills/02-coding-languages/general/regex-vs-llm-structured-text/) | 结构化文本解析的正则 vs LLM 决策框架：先正则，低置信才用 LLM。 |
| **fal-ai-media** | [skills/07-media-content/fal-ai-media/](../skills/07-media-content/fal-ai-media/) | 基于 fal.ai MCP 的统一媒体生成：文生图、图/文生视频、TTS、视频转音频。 |
| **content-hash-cache-pattern** | [skills/02-coding-languages/general/content-hash-cache-pattern/](../skills/02-coding-languages/general/content-hash-cache-pattern/) | 用 SHA-256 内容哈希缓存昂贵文件处理：路径无关、自动失效、服务层分离。 |

## Agent 工程与自治编排

Agent harness 构造、自治循环、council、RFC 管线、DevFleet、dmux、NanoClaw、持续学习与记忆。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **agent-harness-construction** | [skills/01-agent-engineering/agent-harness-construction/](../skills/01-agent-engineering/agent-harness-construction/) | 设计和优化 Agent 动作空间、工具定义、观察格式以提升完成率。 |
| **agent-introspection-debugging** | [skills/01-agent-engineering/agent-introspection-debugging/](../skills/01-agent-engineering/agent-introspection-debugging/) | Agent 失败时的结构化自调试工作流：捕获、诊断、恢复、内省。 |
| **agentic-engineering** | [skills/01-agent-engineering/agentic-engineering/](../skills/01-agent-engineering/agentic-engineering/) | 以 eval-first、任务分解、模型成本路由的方式开展 Agent 工程实践。 |
| **ai-first-engineering** | [skills/01-agent-engineering/ai-first-engineering/](../skills/01-agent-engineering/ai-first-engineering/) | 以 AI Agent 为主要产出方的团队工程运营模型。 |
| **autonomous-agent-harness** | [skills/01-agent-engineering/autonomous-agent-harness/](../skills/01-agent-engineering/autonomous-agent-harness/) | 把 Claude Code 改造为全自治 Agent：持久记忆、定时任务、电脑使用、任务队列。 |
| **autonomous-loops** | [skills/01-agent-engineering/autonomous-loops/](../skills/01-agent-engineering/autonomous-loops/) | 自治 Claude Code 循环的设计模式，从顺序管线到 RFC 驱动的多 Agent DAG。 |
| **continuous-agent-loop** | [skills/01-agent-engineering/continuous-agent-loop/](../skills/01-agent-engineering/continuous-agent-loop/) | 持续自治 Agent 循环的模式，含质量门、eval 和恢复控制。 |
| **gan-style-harness** | [skills/01-agent-engineering/gan-style-harness/](../skills/01-agent-engineering/gan-style-harness/) | GAN 式 Generator-Evaluator Agent harness，用于自治构建高质量应用。 |
| **blueprint** | [skills/01-agent-engineering/blueprint/](../skills/01-agent-engineering/blueprint/) | 把一句话目标转为多会话多 Agent 的分步构建计划，每步自带冷启动上下文。 |
| **council** | [skills/01-agent-engineering/council/](../skills/01-agent-engineering/council/) | 对模糊决策召集四声议事会，在选择前先进行结构化异议辩论。 |
| **santa-method** | [skills/01-agent-engineering/santa-method/](../skills/01-agent-engineering/santa-method/) | 多 Agent 对抗验证收敛循环，两个独立审查都通过后才出交付。 |
| **ralphinho-rfc-pipeline** | [skills/01-agent-engineering/ralphinho-rfc-pipeline/](../skills/01-agent-engineering/ralphinho-rfc-pipeline/) | RFC 驱动的多 Agent DAG 执行模式，含质量门、合并队列、工作单元编排。 |
| **claude-devfleet** | [skills/01-agent-engineering/claude-devfleet/](../skills/01-agent-engineering/claude-devfleet/) | 通过 Claude DevFleet 编排多 Agent 编码任务，并行 worktree 派发与监控。 |
| **dmux-workflows** | [skills/01-agent-engineering/dmux-workflows/](../skills/01-agent-engineering/dmux-workflows/) | 使用 dmux 编排多 Agent 并行工作流，跨 Claude Code、Codex、OpenCode 等。 |
| **nanoclaw-repl** | [skills/01-agent-engineering/nanoclaw-repl/](../skills/01-agent-engineering/nanoclaw-repl/) | 运营与扩展 NanoClaw v2，ECC 基于 claude -p 的零依赖会话感知 REPL。 |
| **continuous-learning** | [skills/01-agent-engineering/continuous-learning/](../skills/01-agent-engineering/continuous-learning/) | 自动从会话中抽取可复用模式，保存为可供后续使用的 learned skills。 |
| **continuous-learning-v2** | [skills/01-agent-engineering/continuous-learning-v2/](../skills/01-agent-engineering/continuous-learning-v2/) | 基于 hooks 观察会话、生成 instinct 并进化为 skill/command/agent 的学习系统 v2。 |
| **proactive-agent** | [skills/01-agent-engineering/proactive-agent/](../skills/01-agent-engineering/proactive-agent/) | 把 Agent 从被动执行者转为主动伙伴，跨会话记忆、主动建议下一步。 |
| **architecture-decision-records** | [skills/01-agent-engineering/architecture-decision-records/](../skills/01-agent-engineering/architecture-decision-records/) | 把 Claude Code 会话中的架构决策自动记录为结构化 ADR 日志。 |
| **ck** | [skills/01-agent-engineering/ck/](../skills/01-agent-engineering/ck/) | 项目级持久记忆，自动加载项目上下文、追踪 git 会话、写入原生内存。 |
| **codebase-onboarding** | [skills/01-agent-engineering/codebase-onboarding/](../skills/01-agent-engineering/codebase-onboarding/) | 分析陌生代码库并生成结构化 onboarding 指南与起始 CLAUDE.md。 |
| **documentation-lookup** | [skills/01-agent-engineering/documentation-lookup/](../skills/01-agent-engineering/documentation-lookup/) | 通过 Context7 MCP 查最新官方文档，替代训练数据里的过时 API。 |
| **safety-guard** | [skills/01-agent-engineering/safety-guard/](../skills/01-agent-engineering/safety-guard/) | 在生产环境或自治运行时阻止破坏性操作。 |
| **enterprise-agent-ops** | [skills/01-agent-engineering/enterprise-agent-ops/](../skills/01-agent-engineering/enterprise-agent-ops/) | 长寿命 Agent 负载的可观测、安全边界、生命周期管理。 |
| **opensource-pipeline** | [skills/01-agent-engineering/opensource-pipeline/](../skills/01-agent-engineering/opensource-pipeline/) | 开源发布流水线：fork、脱敏、打包私有项目以安全公开（三 Agent 链）。 |
| **repo-scan** | [skills/01-agent-engineering/repo-scan/](../skills/01-agent-engineering/repo-scan/) | 跨栈源码资产审计，分类文件、识别嵌入第三方库，输出四级判定 HTML 报告。 |
| **plankton-code-quality** | [skills/01-agent-engineering/plankton-code-quality/](../skills/01-agent-engineering/plankton-code-quality/) | 基于 Plankton 的写入期代码质量把关——保存时自动格式化、lint、Claude 修复。 |
| **openclaw-persona-forge** | [skills/01-agent-engineering/openclaw-persona-forge/](../skills/01-agent-engineering/openclaw-persona-forge/) | 为 OpenClaw AI Agent 锻造龙虾灵魂方案：身份、角色底线、头像提示词。 |
| **search-first** | [skills/01-agent-engineering/search-first/](../skills/01-agent-engineering/search-first/) | 编码前先研究的工作流，调研现有工具、库、模式再写自定义代码。 |
| **agent-eval** | [skills/01-agent-engineering/agent-eval/](../skills/01-agent-engineering/agent-eval/) | 对多款编码 Agent（Claude Code、Aider、Codex 等）做成功率/成本/一致性对比。 |
| **product-lens** | [skills/01-agent-engineering/product-lens/](../skills/01-agent-engineering/product-lens/) | 在开工前验证"为什么要做"，压力测试产品方向避免仓促实现。 |

## 行业与业务

医疗、合同、采购、物流、供应链、生产、质量、合规等业务沉淀。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **healthcare-phi-compliance** | [skills/10-business-industry/healthcare-phi-compliance/](../skills/10-business-industry/healthcare-phi-compliance/) | 医疗应用 PHI/PII 合规：数据分级、访问控制、审计、加密、常见泄漏路径。 |
| **hipaa-compliance** | [skills/10-business-industry/hipaa-compliance/](../skills/10-business-industry/hipaa-compliance/) | HIPAA 专用入口：PHI 处置、covered entity、BAA、违规态势与美国医疗合规。 |
| **healthcare-cdss-patterns** | [skills/10-business-industry/healthcare-cdss-patterns/](../skills/10-business-industry/healthcare-cdss-patterns/) | 临床决策支持系统开发：药物互作、剂量校验、临床评分、告警分级与 EMR 集成。 |
| **healthcare-emr-patterns** | [skills/10-business-industry/healthcare-emr-patterns/](../skills/10-business-industry/healthcare-emr-patterns/) | 医疗 EMR/EHR 开发模式：临床安全、就诊流程、处方生成、CDSS 集成、无障碍 UI。 |
| **healthcare-eval-harness** | [skills/10-business-industry/healthcare-eval-harness/](../skills/10-business-industry/healthcare-eval-harness/) | 医疗发布的病人安全评测 harness：CDSS、PHI、临床流程与集成合规，失败阻断上线。 |
| **contract-review** | [skills/10-business-industry/contract-review/](../skills/10-business-industry/contract-review/) | 合同审核：三层审查（基础/业务/法律）、结构化注释、摘要与 Mermaid 流程图。 |
| **carrier-relationship-management** | [skills/10-business-industry/carrier-relationship-management/](../skills/10-business-industry/carrier-relationship-management/) | 承运商组合管理、费率谈判、绩效评分、运量分配与战略关系维护。 |
| **customs-trade-compliance** | [skills/10-business-industry/customs-trade-compliance/](../skills/10-business-industry/customs-trade-compliance/) | 海关文档、税则归类、关税优化、限制方筛查与跨司法域合规。 |
| **logistics-exception-management** | [skills/10-business-industry/logistics-exception-management/](../skills/10-business-industry/logistics-exception-management/) | 运输异常、延误、破损、丢失与承运商争议的处理范式与升级协议。 |
| **returns-reverse-logistics** | [skills/10-business-industry/returns-reverse-logistics/](../skills/10-business-industry/returns-reverse-logistics/) | 退货授权、收检、处置、退款、欺诈识别、保修索赔处理的经验沉淀。 |
| **energy-procurement** | [skills/10-business-industry/energy-procurement/](../skills/10-business-industry/energy-procurement/) | 电气/天然气采购、电价优化、需求费管理、PPA 评估与多厂能源成本管理。 |
| **inventory-demand-planning** | [skills/10-business-industry/inventory-demand-planning/](../skills/10-business-industry/inventory-demand-planning/) | 多门店零售的需求预测、安全库存、补货、促销拉动估算。 |
| **production-scheduling** | [skills/10-business-industry/production-scheduling/](../skills/10-business-industry/production-scheduling/) | 生产排程、作业排序、产线平衡、换线优化、瓶颈化解（离散与批量制造）。 |
| **quality-nonconformance** | [skills/10-business-industry/quality-nonconformance/](../skills/10-business-industry/quality-nonconformance/) | 质量管控、不合规调查、根因、CAPA、SPC 解读与供应商质量管理。 |

## 写作 / 营销 / 融资

文章写作、品牌声线、多平台分发、SEO、投资材料、财务建模、产品规划。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **article-writing** | [skills/08-writing-marketing/article-writing/](../skills/08-writing-marketing/article-writing/) | 按提供样本或品牌声线写文章、指南、博客、教程、Newsletter 等长文。 |
| **brand-voice** | [skills/08-writing-marketing/brand-voice/](../skills/08-writing-marketing/brand-voice/) | 从真实帖子/文章/文档提取可复用写作声线画像并跨内容/外联工作流复用。 |
| **content-engine** | [skills/08-writing-marketing/content-engine/](../skills/08-writing-marketing/content-engine/) | 构建多平台原生内容体系（X/LinkedIn/TikTok/YouTube），一源多适配。 |
| **crosspost** | [skills/08-writing-marketing/crosspost/](../skills/08-writing-marketing/crosspost/) | X/LinkedIn/Threads/Bluesky 多平台分发：按平台改写，不跨平台复制粘贴。 |
| **seo** | [skills/08-writing-marketing/seo/](../skills/08-writing-marketing/seo/) | 技术 SEO、页面优化、结构化数据、CWV、内容策略的审计、规划与实施。 |
| **connections-optimizer** | [skills/08-writing-marketing/connections-optimizer/](../skills/08-writing-marketing/connections-optimizer/) | 以"先审后剪"方式重组 X/LinkedIn 网络，并用真人声线起草定向外联。 |
| **investor-materials** | [skills/08-writing-marketing/investor-materials/](../skills/08-writing-marketing/investor-materials/) | 生成并更新 Pitch Deck、一页纸、Memo、孵化器申请、财务模型等融资材料。 |
| **investor-outreach** | [skills/08-writing-marketing/investor-outreach/](../skills/08-writing-marketing/investor-outreach/) | 为融资场景起草冷邮件、暖介绍、跟进与更新信，面向 VC/天使/战投。 |
| **market-research-reports** | [skills/08-writing-marketing/market-research-reports/](../skills/08-writing-marketing/market-research-reports/) | 生成 50+ 页顶级咨询公司风格市场研究报告，专业 LaTeX 格式，多框架分析。 |
| **creating-financial-models** | [skills/08-writing-marketing/creating-financial-models/](../skills/08-writing-marketing/creating-financial-models/) | 高级财务建模：DCF、敏感性、蒙特卡洛、场景规划、IRR/MOIC、WACC。 |
| **personal-architecture-designer** | [skills/08-writing-marketing/personal-architecture-designer/](../skills/08-writing-marketing/personal-architecture-designer/) | 把模糊想法和业务痛点深挖成清晰需求，再给出务实系统架构方案。 |
| **product-capability** | [skills/08-writing-marketing/product-capability/](../skills/08-writing-marketing/product-capability/) | 把 PRD/路线图讨论转为多服务可实现的能力计划，提前暴露约束与未决决策。 |

## 办公自动化 / 协作

邮件、即时消息、GitHub、Jira、X/Twitter、统一通知、财务账单与客户计费。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **email-ops** | [skills/09-ops-productivity/general/email-ops/](../skills/09-ops-productivity/general/email-ops/) | 证据优先的邮箱三件套：整理、起草、真实发送并用 Sent 箱验证跟进。 |
| **messages-ops** | [skills/09-ops-productivity/general/messages-ops/](../skills/09-ops-productivity/general/messages-ops/) | 证据优先的即时消息工作流：读 DM、找验证码、回复前检查、证明看了哪一源。 |
| **slack** | [skills/09-ops-productivity/general/slack/](../skills/09-ops-productivity/general/slack/) | 通过浏览器自动化在 Slack 中检查未读、导航、发消息、搜对话、抓取信息。 |
| **github-ops** | [skills/09-ops-productivity/general/github-ops/](../skills/09-ops-productivity/general/github-ops/) | 用 gh CLI 做仓库运营：Issue 分诊、PR 管理、CI、发布、贡献者、陈旧项。 |
| **jira-integration** | [skills/09-ops-productivity/general/jira-integration/](../skills/09-ops-productivity/general/jira-integration/) | 拉取 Jira 工单、分析需求、更新状态、评论、流转，MCP 或 REST。 |
| **terminal-ops** | [skills/09-ops-productivity/general/terminal-ops/](../skills/09-ops-productivity/general/terminal-ops/) | 证据优先的仓库执行工作流：跑命令、查仓库、诊断 CI、修窄范围并给执行证据。 |
| **x-api** | [skills/09-ops-productivity/general/x-api/](../skills/09-ops-productivity/general/x-api/) | X/Twitter API 集成：发推/发串、读时间线、搜索、分析、OAuth 与限流。 |
| **unified-notifications-ops** | [skills/09-ops-productivity/general/unified-notifications-ops/](../skills/09-ops-productivity/general/unified-notifications-ops/) | 把 GitHub/Linear/桌面/hooks/通讯面板的通知当作一个 ECC 工作流统一治理。 |
| **project-flow-ops** | [skills/09-ops-productivity/general/project-flow-ops/](../skills/09-ops-productivity/general/project-flow-ops/) | GitHub 对外、Linear 对内的执行流编排：Issue/PR 分诊、关联在办工作项。 |
| **finance-billing-ops** | [skills/09-ops-productivity/general/finance-billing-ops/](../skills/09-ops-productivity/general/finance-billing-ops/) | ECC 证据优先的营收、定价、退款、团队账单真相工作流。 |
| **customer-billing-ops** | [skills/09-ops-productivity/general/customer-billing-ops/](../skills/09-ops-productivity/general/customer-billing-ops/) | 基于 Stripe 等对接的客户账单运维：订阅、退款、流失分诊、门户恢复。 |

## 架构与编码规范

六边形/Clean Architecture、API 设计、后端模式、MCP server、通用编码规范与 Git 工作流。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **hexagonal-architecture** | [skills/02-coding-languages/general/hexagonal-architecture/](../skills/02-coding-languages/general/hexagonal-architecture/) | 设计与重构 Ports & Adapters 系统：清晰领域边界、依赖倒置、可测试用例编排。 |
| **api-design** | [skills/02-coding-languages/general/api-design/](../skills/02-coding-languages/general/api-design/) | REST API 设计：资源命名、状态码、分页、过滤、错误、版本、限流。 |
| **backend-patterns** | [skills/02-coding-languages/general/backend-patterns/](../skills/02-coding-languages/general/backend-patterns/) | 后端架构模式：API 设计、数据库优化、Node/Express/Next.js API 路由实践。 |
| **mcp-server-patterns** | [skills/02-coding-languages/general/mcp-server-patterns/](../skills/02-coding-languages/general/mcp-server-patterns/) | 用 Node/TS SDK 构建 MCP server：tools、resources、prompts、Zod、stdio/HTTP。 |
| **coding-standards** | [skills/02-coding-languages/general/coding-standards/](../skills/02-coding-languages/general/coding-standards/) | 跨项目的基础编码约定：命名、可读性、不可变、代码质量审查。 |
| **git-workflow** | [skills/02-coding-languages/general/git-workflow/](../skills/02-coding-languages/general/git-workflow/) | Git 分支策略、提交约定、merge vs rebase、冲突解决等团队协作模式。 |

## 项目：Codex Invoice（发票识别）

发票识别项目的真值集、回归门禁与受控前端自动修复。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **163-email-ground-truth** | [projects/codex-invoice/163-email-ground-truth/](../projects/codex-invoice/163-email-ground-truth/) | 163/网易邮箱真值集构建、审计与跑批，含 IMAP ID 命令等特殊处理。 |
| **qq-email-ground-truth** | [projects/codex-invoice/qq-email-ground-truth/](../projects/codex-invoice/qq-email-ground-truth/) | 构建/重建/审计/比对 QQ 邮箱发票真值集，验证跑批输出。 |
| **email-batch-test** | [projects/codex-invoice/email-batch-test/](../projects/codex-invoice/email-batch-test/) | 跑批测试标准与双邮箱回归门禁：P0/P1/P2 标准与保护区改动的双邮箱验证。 |
| **controlled-lockcheck-autofix** | [projects/codex-invoice/controlled-lockcheck-autofix/](../projects/codex-invoice/controlled-lockcheck-autofix/) | QQ 受控前端 lockcheck 自动化：失败分类、受限自动修复、打包门的证据留存。 |

## 项目：ALK Plus Tracker

重建或扩展 ALK+ Tracker UI 时的原始品牌视觉体系与版式约束。

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **hui-rui-lan** | [projects/alk-plus-tracker/hui-rui-lan/](../projects/alk-plus-tracker/hui-rui-lan/) | 重建或扩展 ALK+ Tracker UI 时保留原始品牌蓝视觉体系、区块顺序、玻璃卡片布局。 |

