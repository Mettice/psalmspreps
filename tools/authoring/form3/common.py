"""Shared helpers for the Form 3 generators."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lessonlib import mcq


def bank(id, level, prompt, items, sources, figure=None, review="authored"):
    """Multiple choice from a bank of {q, r, w: [3], e: [3], y}: authored items, each wrong option with its own feedback."""
    for it in items:
        assert len(it["w"]) == 3 and len(it["e"]) == 3, it
    kw = {"figure": figure} if figure else {}
    return mcq(id, level, prompt, "{X.r}", [("{X.w[0]}", "w0"), ("{X.w[1]}", "w1"), ("{X.w[2]}", "w2")],
               ["{X.y}", "So the answer is {answer}."], vars={"X": {"pick": items}},
               misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}"), ("w2", "{X.e[2]}")], sources=sources, review=review, **kw)
