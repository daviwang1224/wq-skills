---
name: mom-intern-evaluation
description: "生成MOM实习生月度绩效考核报告。用于用户提供txt格式实习生日志、要求考核MOM实习生表现、生成实习生A/B/C评级、分析实习生工作产出或准备实习生绩效材料时。工作流程：清洗日志生成JSON，生成考核模板，按实习生评分规则完成个人考核报告。"
---

# MOM实习生绩效考核

基于工作日志生成MOM实习生月度绩效考核报告，只评价个人，不做团队整体评价。

## 固定考核对象

只识别以下10名MOM实习生：

朱俊聪、陈浩、方超、成坚、田康康、田龙星、岑胜、余婧怡、岳丛、徐晶京。

如果日志中出现其他人员，不纳入本技能报告。固定考核对象即使没有日志，也必须出现在评分表中，并按缺失数据处理。

## 工作流程

### 步骤1：日志清洗

必须先运行清洗脚本，不要直接基于原始txt写报告：

```bash
python scripts/clean_work_log.py <input.txt> <output.json>
```

脚本输出JSON，包含：

- `summary`：月份、固定考核人数、日志覆盖天数、日志命中人数。
- `details`：每名实习生的日志明细。
- `scoring_reference`：每名实习生的评分参考数据。

### 步骤2：生成报告模板

运行模板脚本：

```bash
python scripts/init_report.py <input.json> <output.md>
```

报告正文只包含四部分：

1. 实习生评分表
2. 优秀实习生事迹
3. 其他实习生综合评价
4. C档实习生改进建议

不要在报告正文增加质量检查章节。

### 步骤3：读取评分规则

读取 [references/scoring-guide.md](references/scoring-guide.md)，按实习生版评分规则评分。

强制规则：

- 评级只允许A、B、C。
- A为优秀，最多1人；如果无人达到优秀标准，不要硬凑A。
- C为固定比例，10人必须2人；按总分从低到高确定末2名为C。
- B为及格，除A和C外均为B。
- 评分表必须按总分从高到低排序。
- 总分相同时，优先比较工作成果，其次比较工作深度，再次比较工作量。

### 步骤4：读取输出规范

读取 [references/output-patterns.md](references/output-patterns.md)，按指定结构填充模板。

输出要求：

- 只输出最终报告，不输出推理过程。
- 评价必须引用工作日志中的具体事实。
- 对日志为空或明显不足的人员，直接指出数据缺失或产出不足，不美化。
- 删除模板中的所有TODO和HTML注释。

### 步骤5：内部质量检查

交付前必须内部检查：

- 报告正文没有团队整体评价。
- 报告正文没有质量检查章节。
- 评分表包含固定10名实习生。
- 评级只有A、B、C。
- A不超过1人，且未达优秀标准时为0人。
- C正好2人。
- 总分等于四维度分数之和。
- 表格按总分从高到低排序。
- 所有TODO和HTML注释已删除。

质量检查只作为内部步骤，不写入报告正文。

## 参考资源

- 评分标准和评级分布：[references/scoring-guide.md](references/scoring-guide.md)
- 报告结构和输出规范：[references/output-patterns.md](references/output-patterns.md)
