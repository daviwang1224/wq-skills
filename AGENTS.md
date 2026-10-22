# Repository Guidelines

## 项目结构

每个技能使用独立目录，必须包含 `SKILL.md`。可选 `scripts/`、`references/`、`assets/`、`agents/`。新增、删除或重命名技能时，同步更新根目录 `README.md`。

## 编码与命名

- 技能目录和 `name` 使用小写字母、数字及连字符，例如 `monthly-summary-assistant`。
- `SKILL.md` frontmatter 至少包含 `name` 和 `description`，说明能力及触发场景。
- 核心规则写入 `SKILL.md`，详细资料放入 `references/`，确定性逻辑放入 `scripts/`。
- 文本文件使用 UTF-8，内容保持简洁、明确、可执行。

## 提交与 Pull Request

提交信息使用 `feat:`、`fix:`、`docs:` 等前缀加简短说明，例如 `feat: 新增月度总结技能`。每个提交只处理一个主题。PR 应说明技能用途、主要变更和验证方式。

## 安全与配置

禁止提交密钥、令牌、客户数据或未经脱敏的内部信息。Windows 使用 PowerShell；Git SSH 使用 `C:/Program Files/Git/usr/bin/ssh.exe`。不得擅自还原他人的未提交变更。
