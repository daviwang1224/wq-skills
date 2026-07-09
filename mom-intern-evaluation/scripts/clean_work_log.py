#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
MOM实习生工作日志清洗脚本。

用法：
    python clean_work_log.py input.txt output.json
    python clean_work_log.py input.txt output.json --verbose
"""

import json
import re
import sys
from enum import Enum
from pathlib import Path
from typing import Dict, List, Tuple


INTERN_MEMBERS = [
    "朱俊聪",
    "陈浩",
    "岑胜",
    "成坚",
    "田康康",
    "丁阳",
    "岑胜",
    "余婧怡",
    "岳丛",
    "徐晶京",
    "芦智文"

]


class State(Enum):
    READING_CONTENT = "reading"
    SKIPPING = "skipping"


class WorkLogCleaner:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.date_pattern = r"^\d{4}-\d{2}-\d{2}"
        self.lunar_weather_pattern = r"[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]年\s+\S+\s+周[一二三四五六日]\s+\S+"
        self.bracket_pattern = r"\[\]"
        self.skip_trigger_pattern = (
            r"^(?:每日金句|明日计划|本月计划|月计划|"
            r"\d+月计划|[一二三四五六七八九十]+月计划)(?:[：:（(\s]|$)"
        )
        self.name_pattern = r"[（(]([^）)]+)[）)]"
        self.intern_set = set(INTERN_MEMBERS)
        self.keywords_config = {
            "workload": {
                "high": {
                    "weight": 2,
                    "keywords": ["完成", "开发", "实现", "修复", "联调", "测试", "提交", "整理", "配置", "部署"],
                },
                "medium": {
                    "weight": 1,
                    "keywords": ["学习", "了解", "熟悉", "阅读", "调研", "参与", "讨论", "确认", "记录"],
                },
            },
            "depth": {
                "high": {
                    "weight": 2,
                    "keywords": ["设计", "优化", "重构", "接口", "组件", "模型", "流程", "规则", "排查", "定位"],
                },
                "medium": {
                    "weight": 1,
                    "keywords": ["页面", "功能", "字段", "配置", "脚本", "数据", "文档", "用例", "问题"],
                },
            },
            "result": {
                "high": {
                    "weight": 2,
                    "keywords": ["完成", "提交", "交付", "上线", "验收", "通过", "解决", "闭环", "合入"],
                },
                "medium": {
                    "weight": 1,
                    "keywords": ["开发", "实现", "修复", "测试", "联调", "整理", "输出", "更新"],
                },
            },
            "attitude": {
                "high": {
                    "weight": 2,
                    "keywords": ["主动", "协助", "支持", "沟通", "配合", "复盘", "总结", "反馈"],
                },
                "medium": {
                    "weight": 1,
                    "keywords": ["参与", "确认", "同步", "学习", "熟悉", "记录", "会议"],
                },
            },
        }

    def log(self, message: str):
        if self.verbose:
            print(f"[INFO] {message}")

    def is_date_line(self, line: str) -> bool:
        return bool(re.match(self.date_pattern, line.strip()))

    def extract_date(self, line: str) -> str:
        match = re.match(self.date_pattern, line.strip())
        return match.group(0) if match else ""

    def should_skip(self, line: str) -> bool:
        return bool(re.match(self.skip_trigger_pattern, line.strip()))

    def clean_line(self, line: str) -> str:
        line = re.sub(self.lunar_weather_pattern, "", line)
        line = re.sub(self.bracket_pattern, "", line)
        return line.strip()

    def extract_names(self, line: str) -> List[str]:
        matches = re.findall(self.name_pattern, line)
        if not matches:
            return []
        names_str = matches[-1].strip()
        names = [name.strip() for name in re.split(r"[、,，]", names_str) if name.strip()]
        return [name for name in names if name in self.intern_set]

    def process_line(self, line: str, current_date: str, details: Dict[str, Dict[str, List[str]]]):
        cleaned_line = self.clean_line(line)
        if not cleaned_line:
            return

        names = self.extract_names(cleaned_line)
        if len(names) != 1:
            self.log(f"跳过非单人实习生日志: {cleaned_line[:50]}")
            return

        name = names[0]
        content = re.sub(self.name_pattern, "", cleaned_line).strip().rstrip("；;")
        if not content:
            return

        details.setdefault(name, {}).setdefault(current_date, []).append(content)
        self.log(f"归入 [{name}][{current_date}]: {content[:50]}")

    def clean_log(self, input_path: Path) -> Tuple[dict, dict]:
        try:
            lines = input_path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = input_path.read_text(encoding="gbk").splitlines()

        details: Dict[str, Dict[str, List[str]]] = {name: {} for name in INTERN_MEMBERS}
        current_date = None
        state = State.SKIPPING
        valid_lines = 0
        skipped_lines = 0

        for line in lines:
            stripped = line.strip()
            if self.is_date_line(stripped):
                current_date = self.extract_date(stripped)
                state = State.READING_CONTENT
                continue

            if current_date is None:
                skipped_lines += 1
                continue

            if state == State.READING_CONTENT and self.should_skip(stripped):
                state = State.SKIPPING
                skipped_lines += 1
                continue

            if state == State.SKIPPING:
                skipped_lines += 1
                continue

            before = sum(len(logs) for dates in details.values() for logs in dates.values())
            self.process_line(stripped, current_date, details)
            after = sum(len(logs) for dates in details.values() for logs in dates.values())
            if after > before:
                valid_lines += 1
            else:
                skipped_lines += 1

        summary = self.calculate_summary(details)
        scoring_reference = self.calculate_scoring_reference(details, summary["work_days"])
        stats = {
            "total_lines": len(lines),
            "valid_lines": valid_lines,
            "skipped_lines": skipped_lines,
            "intern_count": len(INTERN_MEMBERS),
            "hit_intern_count": sum(1 for logs in details.values() if logs),
            "work_days": summary["work_days"],
            "total_entries": sum(ref["entries"] for ref in scoring_reference.values()),
        }
        return {"summary": summary, "details": details, "scoring_reference": scoring_reference}, stats

    def calculate_summary(self, details: Dict[str, Dict[str, List[str]]]) -> dict:
        all_dates = set()
        for dates in details.values():
            all_dates.update(dates.keys())

        month = sorted(all_dates)[0][:7] if all_dates else ""
        return {
            "month": month,
            "intern_count": len(INTERN_MEMBERS),
            "hit_intern_count": sum(1 for dates in details.values() if dates),
            "work_days": len(all_dates),
            "intern_members": INTERN_MEMBERS,
        }

    def count_keywords(self, text: str, keywords: List[str]) -> Dict[str, int]:
        return {keyword: text.count(keyword) for keyword in keywords if text.count(keyword) > 0}

    def count_by_config(self, text: str, dimension: str, level: str) -> Dict[str, int]:
        return self.count_keywords(text, self.keywords_config[dimension][level]["keywords"])

    def calculate_dimension_reference(self, text: str, dimension: str) -> Tuple[int, int, Dict[str, str]]:
        high = self.count_by_config(text, dimension, "high")
        medium = self.count_by_config(text, dimension, "medium")
        high_count = sum(high.values())
        medium_count = sum(medium.values())
        weighted = high_count * 2 + medium_count
        return high_count, medium_count, {
            f"{dimension}_high": self.keywords_to_string(high),
            f"{dimension}_medium": self.keywords_to_string(medium),
            f"{dimension}_weighted": weighted,
        }

    def calculate_scoring_reference(self, details: Dict[str, Dict[str, List[str]]], work_days: int) -> dict:
        scoring_ref = {}
        for name in INTERN_MEMBERS:
            dates = details.get(name, {})
            all_logs = [log for logs in dates.values() for log in logs]
            all_text = " ".join(all_logs)
            work_days_covered = len(dates)
            coverage = work_days_covered / work_days if work_days else 0
            ref = {
                "entries": len(all_logs),
                "work_days_covered": work_days_covered,
                "coverage": round(coverage, 2),
                "has_logs": bool(all_logs),
            }

            for dimension in ["workload", "depth", "result", "attitude"]:
                high_count, medium_count, extra = self.calculate_dimension_reference(all_text, dimension)
                ref[f"{dimension}_high_count"] = high_count
                ref[f"{dimension}_medium_count"] = medium_count
                ref.update(extra)

            ref["weighted_total"] = sum(ref[f"{dimension}_weighted"] for dimension in ["workload", "depth", "result", "attitude"])
            ref["workload_score_reference"] = self.calculate_workload_score(ref["weighted_total"], coverage, len(all_logs))
            scoring_ref[name] = ref

        return scoring_ref

    def calculate_workload_score(self, weighted_total: int, coverage: float, entries: int) -> int:
        if entries == 0:
            return 0
        if weighted_total >= 60 and coverage >= 0.70:
            return min(25, 22 + (weighted_total - 60) // 15)
        if weighted_total >= 40 and coverage >= 0.50:
            return min(21, 18 + (weighted_total - 40) // 10)
        if weighted_total >= 20 and coverage >= 0.30:
            return min(17, 12 + (weighted_total - 20) // 5)
        return min(11, max(1, weighted_total // 3))

    def keywords_to_string(self, keyword_dict: Dict[str, int]) -> str:
        if not keyword_dict:
            return ""
        return " | ".join(f"{key}:{value}" for key, value in keyword_dict.items())

    def convert_details_to_array(self, details: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
        array_details = {}
        for name in INTERN_MEMBERS:
            dates = details.get(name, {})
            entries = []
            for date in sorted(dates.keys(), reverse=True):
                entries.append(f"{date}: {'；'.join(dates[date])}")
            array_details[name] = entries
        return array_details

    def write_json(self, cleaned_data: dict, output_path: Path):
        output_data = {
            "summary": cleaned_data["summary"],
            "details": self.convert_details_to_array(cleaned_data["details"]),
            "scoring_reference": cleaned_data["scoring_reference"],
        }
        output_path.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    if len(sys.argv) < 3:
        print("使用方法: python clean_work_log.py <input.txt> <output.json> [--verbose]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_path}")
        sys.exit(1)

    cleaner = WorkLogCleaner(verbose=verbose)
    try:
        cleaned_data, stats = cleaner.clean_log(input_path)
        cleaner.write_json(cleaned_data, output_path)
        print("=" * 50)
        print("MOM实习生日志清洗完成")
        print("=" * 50)
        print(f"输入文件: {input_path}")
        print(f"输出文件: {output_path}")
        print(f"固定实习生人数: {stats['intern_count']}")
        print(f"命中日志人数: {stats['hit_intern_count']}")
        print(f"工作日志天数: {stats['work_days']}")
        print(f"有效内容条数: {stats['total_entries']}")
    except Exception as exc:
        print(f"错误: {exc}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
