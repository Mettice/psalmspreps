"""Shared helpers for the Form 4 generators (Claude's subjects)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lessonlib import mcq


def goal(by_the_end, builds_on, leads_to):
    """The first Learn section from Form 4 on (AUTHORING section 3): one measurable goal, what it builds on, what it leads to."""
    return ("Your goal and connections",
            f"By the end, you should be able to {by_the_end}\nBuilds on: {builds_on}\nLeads to: {leads_to}")


def bank(id, level, prompt, items, sources, figure=None, review="authored"):
    """Multiple choice from a bank of {q, r, w: [3], e: [3], y}: authored items, each wrong option with its own feedback."""
    for it in items:
        assert len(it["w"]) == 3 and len(it["e"]) == 3, it
    kw = {"figure": figure} if figure else {}
    return mcq(id, level, prompt, "{X.r}", [("{X.w[0]}", "w0"), ("{X.w[1]}", "w1"), ("{X.w[2]}", "w2")],
               ["{X.y}", "So the answer is {answer}."], vars={"X": {"pick": items}},
               misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}"), ("w2", "{X.e[2]}")], sources=sources, review=review, **kw)


# a rounded answer is fair only when the pupil's own rounding cannot land on the other side: no exact 5 in the
# third decimal place (for answers to 2 d.p.)
def not_half(expr):
    return f"abs({expr} * 1000 - round({expr} * 1000)) > 0.01 || abs(round({expr} * 1000)) % 10 != 5"
