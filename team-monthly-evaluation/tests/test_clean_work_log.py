import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "clean_work_log.py"
spec = importlib.util.spec_from_file_location("clean_work_log", SCRIPT_PATH)
clean_work_log = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clean_work_log)


class CleanWorkLogTest(unittest.TestCase):
    def clean_text(self, text: str) -> dict:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
            f.write(text)
            temp_path = Path(f.name)

        try:
            cleaner = clean_work_log.WorkLogCleaner()
            data, _ = cleaner.clean_log(temp_path)
            return data
        finally:
            temp_path.unlink(missing_ok=True)

    def test_month_plan_work_item_does_not_start_skip_block(self):
        data = self.clean_text(
            "\n".join(
                [
                    "2026-05-01",
                    "[] 【HX月计划需求】完成联调。（薛启宽）",
                    "[] 【页面设计JS脚本优化】修复模板语法问题。（施亚铭）",
                    "每日金句",
                    "[] 【页面设计模型功能覆盖】这条应该被跳过。（施亚铭）",
                    "2026-05-02",
                    "[] 【运行态独立登录】完成验证。（施亚铭）",
                ]
            )
        )

        self.assertEqual(data["scoring_reference"]["薛启宽"]["entries"], 1)
        self.assertEqual(data["scoring_reference"]["施亚铭"]["entries"], 2)

    def test_multi_name_suffix_is_skipped_before_whitelist_filter(self):
        data = self.clean_text(
            "\n".join(
                [
                    "2026-05-01",
                    "[] 【协作事项】完成方案对齐。（施亚铭、非白名单）",
                    "[] 【单人事项】完成方案验证。（施亚铭）",
                ]
            )
        )

        self.assertEqual(data["scoring_reference"]["施亚铭"]["entries"], 1)

    def test_202605_sample_counts_shiyaming_entries(self):
        sample = Path(r"D:\2_project\km-work-docs-system\02-inbox\202605-logs.md")
        if not sample.exists():
            self.skipTest(f"样例日志不存在: {sample}")

        cleaner = clean_work_log.WorkLogCleaner()
        data, _ = cleaner.clean_log(sample)

        self.assertEqual(data["scoring_reference"]["施亚铭"]["entries"], 17)


if __name__ == "__main__":
    unittest.main()
