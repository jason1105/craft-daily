# -*- coding: utf-8 -*-
"""_parse_tip_json 的单元测试。

覆盖线上真实的失败模式：steps 字段内含 markdown 代码块，
旧的非贪婪围栏正则会抓到内层 ``` 把外层 JSON 撕碎（PR 修复点）。
"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_tip import _parse_tip_json


def _noop_diag(msg):
    return ValueError(msg)


class ParseTipJsonTest(unittest.TestCase):
    def test_plain_json(self):
        obj = {"name": "a", "steps": "1. 打开终端\n2. 输入命令"}
        self.assertEqual(_parse_tip_json(json.dumps(obj), _noop_diag), obj)

    def test_fenced_code_block_with_json_lang(self):
        obj = {"name": "a", "steps": "先看原文"}
        raw = "```json\n" + json.dumps(obj, ensure_ascii=False) + "\n```"
        self.assertEqual(_parse_tip_json(raw, _noop_diag), obj)

    def test_fenced_code_block_no_lang(self):
        obj = {"name": "b"}
        raw = "```\n" + json.dumps(obj) + "\n```"
        self.assertEqual(_parse_tip_json(raw, _noop_diag), obj)

    def test_nested_markdown_code_block_in_steps(self):
        """线上真实失败模式：steps 内含 ``` 围栏（防御性转义写法）。

        旧逻辑用非贪婪正则 ```(?:json)?\\s*(.+?)``` 时，会匹配到内层
        围栏并把外层 JSON 撕碎；新逻辑先整体解析，直接命中。
        """
        obj = {
            "name": "grep",
            "steps": (
                "1. 打开终端\n"
                "2. 执行：\n"
                "```\n"
                "grep -n 'pattern' file.txt\n"
                "```\n"
                "3. 查看输出"
            ),
        }
        raw = json.dumps(obj, ensure_ascii=False)
        # 先整体解析成功 —— 历史代码里这一步之前就被非贪婪正则拦住了
        self.assertEqual(_parse_tip_json(raw, _noop_diag), obj)

    def test_prose_before_and_after_json(self):
        obj = {"name": "c", "steps": "简易步骤"}
        raw = "好的，以下是整理后的内容：\n" + json.dumps(obj, ensure_ascii=False) + "\n希望对你有帮助。"
        self.assertEqual(_parse_tip_json(raw, _noop_diag), obj)

    def test_non_json_content_raises_diag_error(self):
        with self.assertRaises(ValueError) as ctx:
            _parse_tip_json("抱歉，我无法生成。", _noop_diag)
        self.assertIn("找不到 JSON", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()