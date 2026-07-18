# wq-skills

面向 Agent Skills 规格组织的技能仓库，包含需求澄清、评审分析、文档生成、绩效评价和业务协作等场景。

本仓库的定位是“技能格式通用”，不是“技能内容通用”。技能可以包含具体业务领域、团队背景、流程规则和个人画像，但文件结构与元数据应尽量遵循通用 Agent Skills 约定，避免写成某一个 Agent 客户端的专属格式。

## 基本结构

每个技能是一个独立目录，至少包含 `SKILL.md`：

```text
skill-name/
├── SKILL.md          # 必需：技能元数据和执行说明
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：按需读取的参考资料
├── assets/           # 可选：模板、图片、样例等资源
└── agents/           # 可选：特定客户端的展示元数据
```

`SKILL.md` 的 YAML frontmatter 应优先保持为通用字段：

```yaml
---
name: skill-name
description: 简要说明技能做什么，以及什么场景下使用。
---
```

## 技能列表

当前仓库包含 **20 个技能**。

### 需求与产品协作

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [agent-md-advisor](agent-md-advisor/) | Agent 指令文件顾问 | 审查、诊断、重写或创建 AGENTS.md / CLAUDE.md 等 agent 指令文件 |
| [ask-clarify](ask-clarify/) | 需求澄清与结构化 | 将模糊需求转化为可执行任务定义 |
| [mind-partner](mind-partner/) | 私人 AI 协作伙伴 | 基于用户背景进行想法分析、方案设计和决策辅助 |
| [prd-writer](prd-writer/) | PRD 编写助手 | 引导产品发现对话并生成中文 PRD |
| [think2do](think2do/) | 谋定而后动，先想再做 | 简单任务中先澄清目标，再给出多方案对比和推荐结论 |

### 评审与分析

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [datamodel-checker](datamodel-checker/) | 数据模型检查 | 验证 MOM 数据模型规范符合性和业务设计合理性 |
| [interviewer-review-assistant](interviewer-review-assistant/) | 面试官复盘助手 | 复盘面试提问质量、追问闭环和能力覆盖 |
| [isa95-model-reviewer](isa95-model-reviewer/) | ISA-95 模型评审 | 评审制造业业务模型、领域模型和数据模型的合理性 |
| [oss-scanner](oss-scanner/) | 开源组件扫描与合规分析 | 扫描依赖并分析许可证合规风险 |
| [ubiquitous-language](ubiquitous-language/) | 统一语言 | 维护 CONTEXT.md / CONTEXT-MAP.md，统一项目领域术语 |

### 文档与汇报

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [humanizer](humanizer/) | 中文文本人性化 | 去除 AI 写作痕迹，使文本更自然、更像人写 |
| [mental-model](mental-model/) | 思维模型卡 | 从碎片、对话和复盘中提炼隐性决策规则 |
| [reading-marker](reading-marker/) | 阅读标记 | 将长文标记为可复述、可复用、可检查的认知导航 |
| [seed-sprout-report](seed-sprout-report/) | 发芽报告助手 | 将记录、笔记或想法拓展成跨领域联想文本 |
| [sop-creator](sop-creator/) | SOP 创建器 | 将业务流程整理为可执行的标准作业程序 |
| [work-thought-doc-writer](work-thought-doc-writer/) | 工作洞察文章写作 | 将工作素材、管理观察和产品判断写成中文洞察文章 |

### 绩效与评价

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [mom-intern-evaluation](mom-intern-evaluation/) | MOM 实习生绩效考核 | 基于实习生日志生成月度绩效考核报告 |
| [team-monthly-evaluation](team-monthly-evaluation/) | 团队月度评价 | 基于团队日志生成月度综合评价 |

### 同事画像

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [boss-ning](boss-ning/) | 宁总同事画像 | 以公司总经理视角提供战略经营、资源配置和组织管理判断参考 |
| [wangqing](wangqing/) | 王晴同事画像 | 以 MOM 与CDAP研发总监视角提供产品研发、流程建设和团队管理参考 |

同事画像技能采用复合结构：`SKILL.md` 为默认入口，`work_skill.md` 和 `persona_skill.md` 分别作为工作能力与人格特征入口，具体内容保存在 `work.md` 和 `persona.md`。

## 编写要求

- `SKILL.md` frontmatter 至少包含 `name` 和 `description`。
- `name` 使用小写字母、数字和连字符。
- `description` 说明技能功能和触发场景。
- 具体业务规则可以放在 `SKILL.md`，详细资料优先放入 `references/`。
- 可重复、确定性的处理逻辑优先放入 `scripts/`。
- 避免在通用技能说明中绑定某个 Agent 客户端、插件市场或本地安装方式。
- 特定客户端的展示配置可以放入独立目录，不应成为技能运行的唯一入口。

## 维护指南

维护和新增技能时，应遵循当前工作区生效的 `AGENTS.md` 指令及本 README 中的编写要求。

## 相关资源

- [Agent Skills 规范](https://agentskills.io/specification)
- [Agent Skills 网站](https://agentskills.io)

## 许可证

MIT License
