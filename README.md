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

当前仓库包含 **17 个技能**。

### 需求与产品协作

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [agent-md-advisor](skills/agent-md-advisor/) | Agent 指令文件顾问 | 审查、诊断、重写或创建 AGENTS.md / CLAUDE.md 等 agent 指令文件 |
| [ask-clarify](skills/ask-clarify/) | 需求澄清与结构化 | 将模糊需求转化为可执行任务定义 |
| [mind-partner](skills/mind-partner/) | 私人 AI 协作伙伴 | 基于用户背景进行想法分析、方案设计和决策辅助 |
| [prd-writer](skills/prd-writer/) | PRD 编写助手 | 引导产品发现对话并生成中文 PRD |

### 评审与分析

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [datamodel-checker](skills/datamodel-checker/) | 数据模型检查 | 验证 KMMOM 数据模型规范符合性和业务设计合理性 |
| [interviewer-review-assistant](skills/interviewer-review-assistant/) | 面试官复盘助手 | 复盘面试提问质量、追问闭环和能力覆盖 |
| [isa95-model-reviewer](skills/isa95-model-reviewer/) | ISA-95 模型评审 | 评审制造业业务模型、领域模型和数据模型的合理性 |
| [oss-scanner](skills/oss-scanner/) | 开源组件扫描与合规分析 | 扫描依赖并分析许可证合规风险 |
| [ubiquitous-language](skills/ubiquitous-language/) | 统一语言 | 维护 CONTEXT.md / CONTEXT-MAP.md，统一项目领域术语 |

### 文档与汇报

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [lowcode-biweekly-report](skills/lowcode-biweekly-report/) | 低代码平台双周汇报助手 | 基于工作日志生成低代码平台双周汇报 |
| [meeting-summarizer](skills/meeting-summarizer/) | 会议纪要总结器 | 将会议内容整理为规范会议纪要 |
| [seed-sprout-report](skills/seed-sprout-report/) | 发芽报告助手 | 将记录、笔记或想法拓展成跨领域联想文本 |
| [sop-creator](skills/sop-creator/) | SOP 创建器 | 将业务流程整理为可执行的标准作业程序 |
| [week-report-assistant](skills/week-report-assistant/) | 双周汇报助手 | 从团队工作日志生成双周进展汇报 |

### 绩效与评价

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [mom-intern-evaluation](skills/mom-intern-evaluation/) | MOM 实习生绩效考核 | 基于实习生日志生成月度绩效考核报告 |
| [team-monthly-evaluation](skills/team-monthly-evaluation/) | 团队月度评价 | 基于团队日志生成月度综合评价 |

### 同事画像

| 技能 | 描述 | 主要功能 |
|------|------|---------|
| [wangqing](skills/wangqing/) | 同事画像技能 | 基于个人工作画像提供协作、判断和表达风格参考 |

## 编写要求

- `SKILL.md` frontmatter 至少包含 `name` 和 `description`。
- `name` 使用小写字母、数字和连字符。
- `description` 说明技能功能和触发场景。
- 具体业务规则可以放在 `SKILL.md`，详细资料优先放入 `references/`。
- 可重复、确定性的处理逻辑优先放入 `scripts/`。
- 避免在通用技能说明中绑定某个 Agent 客户端、插件市场或本地安装方式。
- 特定客户端的展示配置可以放入独立目录，不应成为技能运行的唯一入口。

## 维护指南

维护和新增技能时参考 [AGENTS.md](AGENTS.md)。

## 相关资源

- [Agent Skills 规范](https://agentskills.io/specification)
- [Agent Skills 网站](https://agentskills.io)

## 许可证

MIT License
