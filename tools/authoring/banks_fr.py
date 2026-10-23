"""Helpers for Form 2 French and Français intensif: every template is marked lang "fr", the working is in French."""
import lessonlib as f2lib
from lessonlib import st, card, worked, deferred, learn, use_class


def fr(t):
    t["lang"] = "fr"
    return t


def num(*a, **k): return fr(f2lib.num(*a, **k))
def mcq(*a, **k): return fr(f2lib.mcq(*a, **k))
def pool(*a, **k): return fr(f2lib.pool(*a, **k))
def cloze(*a, **k): return fr(f2lib.cloze(*a, **k))
def order(*a, **k): return fr(f2lib.order(*a, **k))
def match(*a, **k): return fr(f2lib.match(*a, **k))
def word_order(*a, **k): return fr(f2lib.word_order(*a, **k))


def lesson_for(D, S):
    return lambda *a, **k: f2lib.lesson(D, S, *a, lang="fr", **k)


def QA(id, level, prompt, items, sources, review="authored", **kw):
    """Choix multiple dans une banque. items: {q?, r, w: [3 fausses], e: [3 explications], y: pourquoi r est juste}."""
    for it in items:
        assert len(it["w"]) == 3 and len(it["e"]) == 3, it
    return mcq(id, level, prompt, "{X.r}", [("{X.w[0]}", "w0"), ("{X.w[1]}", "w1"), ("{X.w[2]}", "w2")],
               ["{X.y}", "Donc la réponse est « {answer} »."], {"X": {"pick": items}},
               misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}"), ("w2", "{X.e[2]}")], sources=sources, review=review, **kw)


def CL(id, level, prompt, items, sources, review="authored", **kw):
    """Le mot qui manque. items: {s: phrase avec ___, a, w: [2 faux], e: [2 explications]}."""
    for it in items:
        assert it["s"].count("___") == 1 and len(it["w"]) == 2 and len(it["e"]) == 2, it
    return cloze(id, level, prompt, "{X.s}", "X.a", {"X": {"pick": items}},
                 choices=[("{X.w[0]}", "w0"), ("{X.w[1]}", "w1")], misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}")],
                 sources=sources, review=review, **kw)


def MT(id, level, prompt, pairs, sources, pick=4, **kw):
    return match(id, level, prompt, pairs, pick=pick, sources=sources, **kw)


def WO(id, level, sentences, sources, prompt="Touche les mots dans le bon ordre."):
    items = [{"a": s, "b": s} if isinstance(s, str) else {"a": s[0], "b": s[1]} for s in sentences]
    return word_order(id, level, prompt, "{X.a}", accept=["{X.b}"], vars={"X": {"pick": items}}, sources=sources)


def SP(id, level, prompt, right, wrong, sources, pick=(3, 1), review="authored"):
    """Trouve la phrase fausse. wrong: (phrase, explication)."""
    return pool(id, level, prompt, [st(r, "true") for r in right], [st(w, "false", e) for w, e in wrong],
                pick=pick, spot=True, review=review, sources=sources)


def TF(id, level, prompt, right, wrong, sources, pick=(1, 2), review="authored"):
    return pool(id, level, prompt, [st(r, "true") for r in right], [st(w, "false", e) for w, e in wrong],
                pick=pick, review=review, sources=sources)


def ORD(id, level, prompt, lists, sources, review="authored"):
    """Remettre dans l'ordre : lists = listes déjà dans le bon ordre (même longueur)."""
    n = len(lists[0])
    assert all(len(x) == n for x in lists)
    return order(id, level, prompt, [f"{{X[{i}]}}" for i in range(n)], vars={"X": {"pick": lists}}, sources=sources, review=review)
