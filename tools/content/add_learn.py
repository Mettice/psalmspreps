"""Adds or replaces the Learn screens of one lesson (2026-10-23).

    python tools/content/add_learn.py content/form-2/maths/55.json learn.json

learn.json holds the `learn` object: {status, vars?, checks?, sections, key_words?, examples?, mistake?}.
It is placed right after `note`, and the lesson is written in the house format (indent 1, LF, final newline).
"""
import json
import sys
from pathlib import Path


def add_learn(lesson_path, learn):
    p = Path(lesson_path)
    lesson = json.loads(p.read_text(encoding="utf-8"))
    lesson.pop("learn", None)
    out = {}
    for k, v in lesson.items():
        out[k] = v
        if k == "note":
            out["learn"] = learn
    p.write_bytes((json.dumps(out, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))


if __name__ == "__main__":
    add_learn(sys.argv[1], json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")))
