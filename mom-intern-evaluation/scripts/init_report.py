#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
MOM实习生绩效考核报告模板初始化脚本。

用法：
    python init_report.py input.json output.md
"""

import json
import sys
from pathlib import Path


INTERN_MEMBERS = [
    "朱俊聪",
    "陈浩",
    "方超",
    "成坚",
    "田康康",
    "田龙",
    "岑胜",
    "余婧怡",
    "岳丛",
    "徐晶京",
]


class ReportInitializer:
    def load_json(self, json_path: Path) -> dict:
        return json.loads(json_path.read_text(encoding="utf-8"))

    def generate_template(self, data: dict) -> str:
        summary = data.get("summary", {})
        month = summary.get("month") or "yyyy-mm"
        members = summary.get("intern_members") or INTERN_MEMBERS

        template = f"""# {month} MOM实习生绩效考核报告

## 一、实习生评分表

<!-- TODO: 按总分从高到低排序；评级只允许A/B/C；A最多1人且可为空；C固定2人。 -->

| 序号 | 姓名 | 工作量(25) | 工作深度(25) | 工作成果(30) | 学习态度与协作(20) | 总分 | 评级 |
|------|------|------------|--------------|--------------|---------------------|------|------|
"""

        for idx, member in enumerate(members, start=1):
            template += f"| {idx} | {member} | TODO | TODO | TODO | TODO | TODO | TODO |\n"

        template += """
**评分说明**：本评分为AI基于工作日志分析的建议，最终结果需负责人确认。

## 二、优秀实习生事迹

<!-- TODO: 只写A档实习生；如果无人达到A档，写“本月无A档实习生”。 -->

### 姓名（A，X分）

- **突出表现**：TODO
- **关键成果**：TODO
- **综合评价**：TODO

## 三、其他实习生综合评价

<!-- TODO: 写B档实习生，不写A档和C档。评价结构：事实表现 + 不足 + 建议。 -->

| 序号 | 姓名 | 评级 | 综合评价 |
|------|------|------|----------|
"""

        for idx, member in enumerate(members, start=1):
            template += f"| {idx} | {member} | TODO | TODO |\n"

        template += """
## 四、C档实习生改进建议

<!-- TODO: 固定写2名C档实习生。必须说明进入C档的具体原因和下月改进要求。 -->

| 序号 | 姓名 | 总分 | 主要问题 | 改进要求 |
|------|------|------|----------|----------|
| 1 | TODO | TODO | TODO | TODO |
| 2 | TODO | TODO | TODO | TODO |
"""

        return template

    def write_template(self, template: str, output_path: Path):
        output_path.write_text(template, encoding="utf-8")


def main():
    if len(sys.argv) < 3:
        print("使用方法: python init_report.py <input.json> <output.md>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_path}")
        sys.exit(1)

    initializer = ReportInitializer()
    try:
        data = initializer.load_json(input_path)
        template = initializer.generate_template(data)
        initializer.write_template(template, output_path)
        summary = data.get("summary", {})
        print("=" * 50)
        print("MOM实习生绩效考核模板生成完成")
        print("=" * 50)
        print(f"输入文件: {input_path}")
        print(f"输出文件: {output_path}")
        print(f"月份: {summary.get('month') or '未知'}")
        print(f"固定实习生人数: {summary.get('intern_count', len(INTERN_MEMBERS))}")
        print("下一步: 按SKILL.md流程填充TODO并删除HTML注释")
    except Exception as exc:
        print(f"错误: {exc}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
