"""Helpers that write lesson JSON (content/<class>/<subject>/<n>.json) for any class (2026-10-23, from the Form 2 helpers).

    import lessonlib as L
    L.use_class("form-3", "Form 3")
    L.lesson("maths", "mathematics", 2, ("m3-2", "Simplify algebraic expressions"), [], note, worked, cards, questions, learn=learn)

See docs/AUTHORING.md for the rules every lesson must pass (npm test).
"""
import json
from pathlib import Path

CONTENT = Path(__file__).resolve().parents[2] / "content"
CLASS = {"dir": "form-2", "label": "Form 2"}
ROOT = CONTENT / CLASS["dir"]


def use_class(folder, label):
    """folder: "form-3", "form-4", "lower-6" …; label: the lessons' `class` field ("Form 3")."""
    global ROOT
    CLASS.update(dir=folder, label=label)
    ROOT = CONTENT / folder


def tpl(id, type, level, prompt, review="rule", sources=(), vars=None, **kw):
    t = {"id": id, "type": type, "level": level, "review": review, "sources": list(sources)}
    if vars is not None:
        t["vars"] = vars
    t["prompt"] = prompt
    for k, v in kw.items():
        if v is not None:
            t[k] = v
    return t


def num(id, level, prompt, answer, solution, vars=None, misc=(), sources=(), review="rule", **kw):
    return tpl(id, "numeric", level, prompt, review, sources, vars, answer=answer,
               misconceptions=[{"id": m[0], "wrong": m[1], "explain": m[2], **({"when": m[3]} if len(m) > 3 else {})} for m in misc] or None,
               solution=list(solution), **kw)


def mcq(id, level, prompt, correct, distractors, solution, vars=None, misc=(), sources=(), review="rule", **kw):
    """distractors: list of (text, misconception_id); misc: (id, explain) or (id, explain, wrong)."""
    ds = []
    for d in distractors:
        if isinstance(d, tuple):
            ds.append({"text": d[0], "misconception": d[1]})
        else:
            ds.append(d)
    ms = []
    for m in misc:
        x = {"id": m[0], "explain": m[1]}
        if len(m) > 2:
            x["wrong"] = m[2]
        ms.append(x)
    return tpl(id, "mcq", level, prompt, review, sources, vars, correct=correct, distractors=ds,
               misconceptions=ms, solution=list(solution), **kw)


def st(text, truth, explain=None):
    s = {"text": text, "truth": truth}
    if explain:
        s["explain"] = explain
    return s


def pool(id, level, prompt, right, wrong, pick=(1, 3), vars=None, sources=(), review="authored", spot=False, **kw):
    return tpl(id, "spot_error" if spot else "mcq", level, prompt, review, sources, vars,
               pool={"right": right, "wrong": wrong}, pick={"right": pick[0], "wrong": pick[1]}, **kw)


def steps(id, level, prompt, steps_, vars=None, sources=(), review="rule", **kw):
    return tpl(id, "spot_error", level, prompt, review, sources, vars, steps=steps_, **kw)


def cloze(id, level, prompt, text, answer, vars=None, choices=None, misc=(), sources=(), review="rule", **kw):
    ch = None
    if choices is not None:
        ch = [{"text": c[0], "misconception": c[1]} if isinstance(c, tuple) else c for c in choices]
    ms = []
    for m in misc:  # (id, explain) for a choice; (id, wrong, explain[, when]) for a typed answer, as for numeric
        x = {"id": m[0], "explain": m[1]} if len(m) == 2 else {"id": m[0], "wrong": m[1], "explain": m[2], **({"when": m[3]} if len(m) > 3 else {})}
        ms.append(x)
    return tpl(id, "cloze", level, prompt, review, sources, vars, text=text, answer=answer, choices=ch,
               misconceptions=ms or None, **kw)


def order(id, level, prompt, items, order_="as_written", vars=None, sources=(), review="rule", **kw):
    its = [{"text": i[0], "key": i[1]} if isinstance(i, tuple) else {"text": i} for i in items]
    return tpl(id, "ordering", level, prompt, review, sources, vars, items=its, order=order_, **kw)


def match(id, level, prompt, pairs, pick=None, groups=False, group_order=None, vars=None, sources=(), review="authored", **kw):
    return tpl(id, "matching", level, prompt, review, sources, vars, pool=[{"left": a, "right": b} for a, b in pairs],
               pick=pick, groups=groups or None, group_order=group_order, **kw)


def word_order(id, level, prompt, answer, accept=None, vars=None, sources=(), review="authored", **kw):
    return tpl(id, "word_order", level, prompt, review, sources, vars, answer=answer, accept=accept, **kw)


def card(id, idea, example, check, vars=None, checks=(), figure=None):
    c = {"id": id, "status": "draft", "idea": idea, "vars": vars or {}, "example": list(example), "checks": list(checks)}
    if figure:
        c["figure"] = figure
    c["check"] = {"ref": check} if isinstance(check, str) else check
    return c


def worked(vars, problem, steps_, answer, checks=(), figure=None):
    w = {"status": "draft", "vars": vars, "problem": problem, "steps": list(steps_), "answer": answer, "checks": list(checks)}
    if figure:
        w["figure"] = figure
    return w


def level1_cards(cards, questions):
    """A card's check must be level 1: a card that points at a harder practice question gets its own level-1 copy."""
    q = {t["id"]: t for t in questions}
    for c in cards:
        ref = c["check"].get("ref")
        if ref and q[ref]["level"] != 1:
            c["check"] = {**q[ref], "id": f"{ref}-card", "level": 1}


def lesson(subject_dir, subject, n, skill, prereq, note, worked_, cards, questions, paper=None, lang="en", learn=None):
    level1_cards(cards, questions)
    l = {"subject": subject, "class": CLASS["label"], "lesson_no": n, "language": lang, "prerequisites": list(prereq),
         "skills": [{"id": skill[0], "name": skill[1]}],
         "note": {"status": "draft", "text": note, "checks": []},
         **({"learn": {"status": "draft", **learn}} if learn else {}),
         "worked_example": worked_, "teach": {"cards": cards}, "questions": questions}
    if paper:
        l["paper_task"] = {"status": "draft", **paper}
    write(subject_dir, n, l)


def deferred(subject_dir, subject, n, sheet_title, reason):
    write(subject_dir, n, {"subject": subject, "class": CLASS["label"], "lesson_no": n, "language": "en", "status": "deferred",
                           "sheet_title": sheet_title, "deferred_reason": reason})


def write(subject_dir, n, l):
    d = ROOT / subject_dir
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{n}.json").write_text(json.dumps(l, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", d / f"{n}.json")


def learn(sections, key_words=(), examples=(), mistake=None, vars=None, checks=()):
    """The Learn screens: sections [(heading, text) or (heading, text, figure)], key_words [(word, meaning)],
    examples [text], mistake (wrong, right, why). 1-4 sections, at most 120 words each and 450 in all; numbers as {expr}."""
    out = {"vars": vars or {}, "sections": [dict(zip(("heading", "text", "figure"), s)) for s in sections]}
    if key_words:
        out["key_words"] = [{"word": w, "meaning": m} for w, m in key_words]
    if examples:
        out["examples"] = list(examples)
    if mistake:
        out["mistake"] = dict(zip(("wrong", "right", "why"), mistake))
    if checks:
        out["checks"] = list(checks)
    return out
