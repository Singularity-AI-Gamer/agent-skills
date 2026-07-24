# 按能力域索引

共 29 个技能，按 6 个能力域 + projects（项目私有）分组。

## 目录

- [01 Agent 工程](#01-agent-工程)（6）
- [03 框架与技术栈](#03-框架与技术栈)（2）
- [06 数据与检索](#06-数据与检索)（8）
- [07 媒体与内容制作](#07-媒体与内容制作)（9）
- [08 写作与营销](#08-写作与营销)（1）
- [10 行业与业务](#10-行业与业务)（3）
- [Projects 项目私有](#projects-项目私有)（0）

## 01 Agent 工程（6）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **adaptive-quality-gate** | [skills/01-agent-engineering/adaptive-quality-gate/](../skills/01-agent-engineering/adaptive-quality-gate/) | 为任意重要任务自动判断并设置风险自适应质量门：从目标反推阈值、验证方法、证据和失败动作，证据不足时阻止无依据交付。 |
| **find-skills** | [skills/01-agent-engineering/find-skills/](../skills/01-agent-engineering/find-skills/) | 自动发现与推荐可用 Agent 技能，回答"有没有能做 X 的技能"。 |
| **santa-method** | [skills/01-agent-engineering/santa-method/](../skills/01-agent-engineering/santa-method/) | 多 Agent 对抗验证收敛循环，两个独立审查都通过后才出交付。 |
| **skill-creator** | [skills/01-agent-engineering/skill-creator/](../skills/01-agent-engineering/skill-creator/) | 创建、修改和优化 skill，并可跑 eval 衡量触发准确率与性能。 |
| **skill-lifecycle-manager** | [skills/01-agent-engineering/skill-lifecycle-manager/](../skills/01-agent-engineering/skill-lifecycle-manager/) | 管理本地/全局/项目级 skill 与 Skill-hub 生命周期：搜索、推荐、安装、升级、同步、合并、清理、来源校验、质量审计和发布。 |
| **yq-windows-trash-cleaner** | [skills/01-agent-engineering/yq-windows-trash-cleaner/](../skills/01-agent-engineering/yq-windows-trash-cleaner/) | Windows C盘、项目垃圾、Docker/WSL、Git worktree、CodeGraph、Agent 会话或内存异常需要安全审计、清理和验证时使用。 |

## 03 框架与技术栈（2）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **frontend-design** | [skills/03-frameworks/frontend-design/](../skills/03-frameworks/frontend-design/) | 创建具有高设计质量的生产级前端界面。 |
| **netlify-cli** | [skills/03-frameworks/netlify-cli/](../skills/03-frameworks/netlify-cli/) | 使用 Netlify CLI 完成安装、认证、站点关联、本地开发、环境变量管理与部署。 |

## 06 数据与检索（8）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **bioc-fulltext-fetch** | [skills/06-data-search/bioc-fulltext-fetch/](../skills/06-data-search/bioc-fulltext-fetch/) | 从 PubMed/PMC 获取结构化全文并按章节切分为 RAG 友好的 chunk。 |
| **clinical-trials-v2** | [skills/06-data-search/clinical-trials-v2/](../skills/06-data-search/clinical-trials-v2/) | 实时查询 ClinicalTrials.gov 试验协议、结果和招募状态。 |
| **cn-clinical-guidelines-fetch** | [skills/06-data-search/cn-clinical-guidelines-fetch/](../skills/06-data-search/cn-clinical-guidelines-fetch/) | 抓取中国权威医学指南（CSCO/NCCN 中文版/NMPA/CDE/NHC）。 |
| **europepmc-search** | [skills/06-data-search/europepmc-search/](../skills/06-data-search/europepmc-search/) | 多源文献聚合检索：PubMed + PMC + 预印本 + NCBI Bookshelf + 专利。 |
| **market-research-reports** | [skills/06-data-search/market-research-reports/](../skills/06-data-search/market-research-reports/) | 生成 50+ 页专业市场研究报告，McKinsey/BCG/Gartner 质量。 |
| **nmpa-drug-registry-lookup** | [skills/06-data-search/nmpa-drug-registry-lookup/](../skills/06-data-search/nmpa-drug-registry-lookup/) | 中国药品权威数据库：NMPA + CDE + DrugBank + PubChem 融合查询。 |
| **pubmed-eutils** | [skills/06-data-search/pubmed-eutils/](../skills/06-data-search/pubmed-eutils/) | 通过 NCBI E-utilities 搜索 PubMed 并获取结构化生物医学文献。 |
| **pubmed-search** | [skills/06-data-search/pubmed-search/](../skills/06-data-search/pubmed-search/) | 通过 Valyu 语义搜索以自然语言检索 PubMed 生物医学文献，支持全文。 |

## 07 媒体与内容制作（9）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **github-readme-visuals** | [skills/07-media-content/github-readme-visuals/](../skills/07-media-content/github-readme-visuals/) | 为 GitHub 仓库创建或更新产品主视觉、完整软件界面截图及中英文 README 图片区，并支持按参考图进行可验证的几何复刻。 |
| **html-design-polish** | [skills/07-media-content/html-design-polish/](../skills/07-media-content/html-design-polish/) | 网页需要产品清晰度、信息层级、响应式或视觉系统美化、重设计或设计审计时使用。 |
| **imagegen** | [skills/07-media-content/imagegen/](../skills/07-media-content/imagegen/) | 生成或编辑光栅图像（照片、插画、纹理、UI 模型等）。 |
| **impeccable** | [skills/07-media-content/impeccable/](../skills/07-media-content/impeccable/) | 设计、重设计、审计或精修生产级前端界面，涵盖信息架构、视觉层级、响应式、无障碍、动效与设计系统时使用。 |
| **make-interfaces-feel-better** | [skills/07-media-content/make-interfaces-feel-better/](../skills/07-media-content/make-interfaces-feel-better/) | 构建或审查 UI 细节、动画、排版、阴影、圆角、光学对齐和微交互，让界面更精致自然时使用。 |
| **ppt-nano** | [skills/07-media-content/ppt-nano/](../skills/07-media-content/ppt-nano/) | 白板板书风格 PPT 生成，适合教学、汇报、头脑风暴。 |
| **ui-ux-pro-max** | [skills/07-media-content/ui-ux-pro-max/](../skills/07-media-content/ui-ux-pro-max/) | 设计、构建或审查 Web/移动端 UI 时，检索风格、配色、字体、布局、UX、动效、图表及多技术栈实现建议。 |
| **xlsx** | [skills/07-media-content/xlsx/](../skills/07-media-content/xlsx/) | 电子表格 .xlsx/.csv 等创建、编辑、公式、格式、数据分析与可视化。 |
| **yq-editorial-presentation-html** | [skills/07-media-content/yq-editorial-presentation-html/](../skills/07-media-content/yq-editorial-presentation-html/) | Anthropic 暖色编辑设计语言，用于演示/case sharing/战略汇报。 |

## 08 写作与营销（1）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **yq-article-style-imitation** | [skills/08-writing-marketing/yq-article-style-imitation/](../skills/08-writing-marketing/yq-article-style-imitation/) | 任意作家文章风格仿写：验证作者原文、拆解表达 DNA、生成并修复公众号/小红书稿。 |

## 10 行业与业务（3）

| 技能名 | 路径 | 中文简介 |
|---|---|---|
| **contract-review** | [skills/10-business-industry/contract-review/](../skills/10-business-industry/contract-review/) | 合同审核：三层审查（基础/业务/法律）、结构化注释、摘要与 Mermaid 流程图。 |
| **creating-financial-models** | [skills/10-business-industry/creating-financial-models/](../skills/10-business-industry/creating-financial-models/) | 高级财务建模套件，含 DCF 估值、敏感性分析、蒙特卡洛模拟。 |
| **xhs-pharma-social-listening** | [skills/10-business-industry/xhs-pharma-social-listening/](../skills/10-business-industry/xhs-pharma-social-listening/) | 面向外资药企员工痛点的小红书证据化舆情研究：采集并分析药企、岗位、合规、医学事务与 AI 相关笔记和评论，按去重笔记加去重评论计算独立证据，并处理 MediaCrawler CAPTCHA/461 与 OpenCLI 回退。 |

## Projects 项目私有（0）

_暂无项目私有技能。_
