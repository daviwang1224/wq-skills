#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
低代码平台双周日报初始化脚本

功能：
1. 读取清洗后的JSON文件
2. 生成包含完整结构的双周日报Markdown模板（匹配PPT结构）
3. 使用TODO标记指示需要填充的部分

使用方法：
    python init_report.py <input.json> <output.md>
    python init_report.py 2025-01_工作日志.json 低代码平台双周日报_2025-01.md
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class ReportInitializer:
    """双周日报初始化器"""

    def __init__(self):
        pass

    def load_json(self, json_path: Path) -> dict:
        """
        加载JSON文件

        Args:
            json_path: JSON文件路径

        Returns:
            JSON数据
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_template(self, data: dict) -> str:
        """
        生成双周日报模板（匹配PPT结构）

        Args:
            data: 清洗后的JSON数据

        Returns:
            Markdown模板内容
        """
        summary = data.get('summary', {})
        period = summary.get('period', 'yyyy-mm-dd - yyyy-mm-dd')
        person_count = summary.get('person_count', 0)

        # 获取当前日期
        current_date = datetime.now().strftime('%Y-%m-%d')

        details = data.get('details', {})

        # 收集所有工作内容（不再按IPD阶段分类）
        all_work = []
        for member, work_list in details.items():
            for work_entry in work_list:
                # work_entry 格式: "date: content"
                if ': ' in work_entry:
                    date, content = work_entry.split(': ', 1)
                    all_work.append({
                        'member': member,
                        'date': date,
                        'content': content
                    })

        # 按日期排序
        all_work.sort(key=lambda x: x['date'])

        template = f"""# KMArtizen.AI 低代码平台双周汇报

**汇报周期**：{period}
**主讲人**：王晴
**日期**：{current_date}
**公司信息**：武汉开目信息技术股份有限公司

---

## 一、版本进度总览

<!-- TODO: 填充版本进度总览 -->
<!-- 通过交互式问答收集以下信息：
1. 版本号、阶段、目标发布时间
2. 版本定位
3. 里程碑达成度
4. 团队成员信息（确认人数和角色分工）
-->

**版本号**：TODO | **阶段**：TODO | **目标发布时间**：TODO

**版本定位**：TODO（如：首个正式版本，完成"设计态→运行态"完整闭环）

### 里程碑达成度

| 指标 | 内容 | 说明 |
|------|------|------|
| 里程碑达成度 | TODO（✓核心功能模块完成 ✓培训体系建立等） | TODO |

### 团队成员

**共计{person_count}人**，TODO人全职，TODO人兼职

- **产品**：王晴（PM）、喻洁（UI/UE）
- **开发**：袁登（项目经理）、尹进雄（架构）、施亚铭/李正（前端）、魏宪亮/方清/廖迪金（后端）
- **测试**：TODO
- **跨团队成员**：TODO

---

## 二、当前工作进展

<!-- TODO: 基于JSON数据填充工作进展 -->
<!-- 从所有工作内容中筛选重点事项，按序号列出，每项工作需要添加说明 -->

| 序号 | 完成事项 | 负责人 | 说明 |
|------|----------|--------|------|
"""

        # 添加所有工作内容（最多显示15条）
        for idx, work in enumerate(all_work[:15], start=1):
            # 将内容截断到合适长度
            content = work['content'][:80]
            if len(work['content']) > 80:
                content += "..."
            template += f"| {idx} | {content} | {work['member']} | TODO |\n"

        if not all_work:
            template += "| 1 | TODO | TODO | TODO |\n"

        template += """
---

## 三、关键成果

<!-- TODO: 通过交互式问答收集关键成果 -->
<!-- 询问用户：从工作进展中，哪1-2项是最关键的成果？这些成果的价值和影响是什么？ -->

### 成果1：TODO标题

**价值**：TODO（标志着低代码平台从"功能开发"进入"推广应用"阶段...）

**详情**：
- TODO（具体完成的内容）
- TODO
- TODO

**负责人**：TODO

### 成果2：TODO标题

**价值**：TODO（补齐低代码平台五大核心模块的最后一块拼图...）

**详情**：
- TODO（具体完成的内容）
- TODO
- TODO

**负责人**：TODO

---

## 四、下2周工作计划

<!-- TODO: 通过交互式问答收集工作计划 -->
<!-- 询问用户：下2周的重点工作有哪些？请按优先级排序（P0/P1/P2），每项工作的负责人和预期产出是什么？ -->

**重点目标**：TODO（如：完成v1.0版本收尾工作，启动v1.1版本开发）

| 优先级 | 任务 | 负责人 | 预期产出 |
|--------|------|--------|----------|
| P0 | TODO | TODO | TODO |
| P0 | TODO | TODO | TODO |
| P0 | TODO | TODO | TODO |
| P1 | TODO | TODO | TODO |

---

## 五、风险与问题

<!-- TODO: 通过交互式问答收集风险与问题 -->
<!-- 询问用户：当前遇到的主要风险和问题有哪些？影响范围是什么？计划采取什么应对措施？谁负责跟进？ -->

| 问题描述 | 影响 | 应对措施 | 责任人 |
|----------|------|----------|--------|
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

---

"""

        return template

    def write_template(self, template: str, output_path: Path):
        """
        将模板写入文件

        Args:
            template: 模板内容
            output_path: 输出文件路径
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template)


def main():
    """主函数"""
    # 解析命令行参数
    if len(sys.argv) < 3:
        print("使用方法: python init_report.py <input.json> <output.md>")
        print("\n示例:")
        print("  python init_report.py 2025-01_工作日志.json 低代码平台双周日报_2025-01.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    # 检查输入文件是否存在
    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_path}")
        sys.exit(1)

    # 创建初始化器
    initializer = ReportInitializer()

    try:
        # 加载JSON数据
        print(f"正在读取: {input_path}")
        data = initializer.load_json(input_path)

        # 生成模板
        print("正在生成模板...")
        template = initializer.generate_template(data)

        # 写入文件
        print(f"正在写入: {output_path}")
        initializer.write_template(template, output_path)

        print("\n" + "="*50)
        print("模板生成完成！")
        print("="*50)
        print(f"输入文件: {input_path}")
        print(f"输出文件: {output_path}")
        print(f"\n汇报周期: {data['summary']['period']}")
        print(f"团队人数: {data['summary']['person_count']}")
        print(f"工作日数: {data['summary']['work_days']}")
        print("="*50)
        print("\n下一步: 通过交互式问答填充模板中的TODO标记部分")

    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
