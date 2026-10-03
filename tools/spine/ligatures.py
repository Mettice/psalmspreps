"""Repair words that lost a 'ti', 'fi' or 'tt' pair, or its second letter, in the source PDFs (questons -> questions).

    python tools/spine/ligatures.py

Build-time only (needs `pyspellchecker`; the app never ships it). For every word in a raw
spine's display text that the dictionary does not know, try inserting each pair at every
position. Exactly one dictionary word -> unambiguous repair. Several -> ambiguous, listed
for a human. None -> not a ligature problem (left to the typo overrides).

Writes or replaces one `replace_words` override per sheet, id "<sheet>-ligatures",
in data/spine/overrides/<sheet>.json. Policy approved by Dion on 2026-10-02.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "spine" / "raw"
OVERRIDES = ROOT / "data" / "spine" / "overrides"
PAIRS = ("ti", "fi", "tt")
FIELDS = ("title", "chapter", "module")


def candidates(word, known):
    """Dictionary words reachable by restoring a dropped pair, or only its second letter
    (the PDFs show both: 'Activies' lost 'ti', 'questons' lost the 'i' after 't')."""
    w = word.lower()
    found = set()
    for i in range(len(w) + 1):
        for p in PAIRS:
            found.add(w[:i] + p + w[i:])
            if i and w[i - 1] == p[0]:
                found.add(w[:i] + p[1] + w[i:])
    return sorted(c for c in found if c in known)


def propose(spine, checker):
    """Returns (repairs {word: fix}, ambiguous {word: [fixes]})."""
    words = set()
    for t in spine["terms"]:
        for l in t["lessons"]:
            for f in FIELDS:
                words.update(re.findall(r"[A-Za-z]{3,}", l.get(f) or ""))
    repairs, ambiguous = {}, {}
    for w in sorted(words, key=str.lower):
        lw = w.lower()
        if lw in repairs or lw in ambiguous or checker.known([lw]):
            continue
        c = candidates(lw, checker)
        if len(c) == 1:
            repairs[lw] = c[0]
        elif len(c) > 1:
            ambiguous[lw] = c
    return repairs, ambiguous


def main():
    from spellchecker import SpellChecker

    checker = SpellChecker(language="en")
    for path in sorted(RAW.glob("*.json")):
        spine = json.loads(path.read_text(encoding="utf-8"))
        if spine["subject"].startswith("french"):
            continue  # French content: no English dictionary repairs
        repairs, ambiguous = propose(spine, checker)
        ov_path = OVERRIDES / path.name
        doc = json.loads(ov_path.read_text(encoding="utf-8")) if ov_path.exists() else \
            {"subject": spine["subject"], "overrides": []}
        oid = f"{path.stem}-ligatures"
        before = len(doc["overrides"])
        doc["overrides"] = [o for o in doc["overrides"] if o["id"] != oid]
        changed = repairs or ambiguous or len(doc["overrides"]) != before
        if repairs or ambiguous:
            doc["overrides"].insert(0, {
                "id": oid, "op": "replace_words", "words": repairs, "ambiguous": ambiguous,
                "reason": "The source PDF lost 'ti'/'fi'/'tt' pairs. Each word here has exactly one dictionary "
                          "repair; ambiguous ones are listed, not applied.",
                "generated_by": "tools/spine/ligatures.py (pyspellchecker, en)",
                "approved_by": "Dion", "approved_on": "2026-10-02"})
        if changed:
            ov_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{path.stem}: {len(repairs)} repairs, {len(ambiguous)} ambiguous {ambiguous or ''}")


if __name__ == "__main__":
    main()
