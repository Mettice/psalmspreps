"""Item banks turned into templates, for every subject taught in English: QA, CL, MT, WO, SP, TF."""
from lessonlib import *


def QA(id, level, prompt, items, sources, review="authored", **kw):
    """Multiple choice from a bank. items: dicts {q?, r, w: [3 wrong], e: [3 explanations], y: why r is right}.
    The prompt may use {X.q}."""
    for it in items:
        assert len(it["w"]) == 3 and len(it["e"]) == 3, it
    return mcq(id, level, prompt, "{X.r}", [("{X.w[0]}", "w0"), ("{X.w[1]}", "w1"), ("{X.w[2]}", "w2")],
               ["{X.y}", "So the answer is “{answer}”."], {"X": {"pick": items}},
               misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}"), ("w2", "{X.e[2]}")], sources=sources, review=review, **kw)


def CL(id, level, prompt, items, sources, review="authored", **kw):
    """Choose the word for the blank. items: dicts {s: sentence with ___, a, w: [2 wrong], e: [2 explanations]}."""
    for it in items:
        assert it["s"].count("___") == 1 and len(it["w"]) == 2 and len(it["e"]) == 2, it
    return cloze(id, level, prompt, "{X.s}", "X.a", {"X": {"pick": items}},
                 choices=[("{X.w[0]}", "w0"), ("{X.w[1]}", "w1")], misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}")],
                 sources=sources, review=review, **kw)


def MT(id, level, prompt, pairs, sources, pick=4, **kw):
    return match(id, level, prompt, pairs, pick=pick, sources=sources, **kw)


def WO(id, level, sentences, sources, prompt="Tap the words in the right order."):
    """sentences: a string, or (sentence, another correct order)."""
    items = [{"a": s, "b": s} if isinstance(s, str) else {"a": s[0], "b": s[1]} for s in sentences]
    return word_order(id, level, prompt, "{X.a}", accept=["{X.b}"], vars={"X": {"pick": items}}, sources=sources)


def SP(id, level, prompt, right, wrong, sources, pick=(3, 1), review="authored"):
    """Spot the wrong sentence. right: sentences; wrong: (sentence, explanation)."""
    return pool(id, level, prompt, [st(r, "true") for r in right], [st(w, "false", e) for w, e in wrong],
                pick=pick, spot=True, review=review, sources=sources)


def TF(id, level, prompt, right, wrong, sources, pick=(1, 2), review="authored"):
    """Choose the true / correct sentence. wrong: (sentence, explanation)."""
    return pool(id, level, prompt, [st(r, "true") for r in right], [st(w, "false", e) for w, e in wrong],
                pick=pick, review=review, sources=sources)


def subj(t, m, person, plural):
    return {"t": t, "m": m, "s": {"text": m, "person": person, "plural": plural}}


SUBJECTS = [subj("I", "I", 1, False), subj("You", "you", 2, False), subj("We", "we", 1, True), subj("They", "they", 3, True),
            subj("He", "he", 3, False), subj("She", "she", 3, False), subj("Bih", "Bih", 3, False), subj("Ayuk", "Ayuk", 3, False),
            subj("My mother", "my mother", 3, False), subj("Our teacher", "our teacher", 3, False),
            subj("Tabe and Ndi", "Tabe and Ndi", 3, True), subj("My cousins", "my cousins", 3, True)]
THIRD = [s for s in SUBJECTS if s["s"]["person"] == 3]
