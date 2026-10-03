"""Validate a spine. Never modifies it; returns issue dicts for the report.

Severity policy (approved 2026-10-02):
- Lesson seq is the source of truth for order; dates are approximate windows, so
  overlapping or out-of-order windows are info, not issues.
- Chapter/title keyword heuristics are info only: the official sheet structure wins.
"""
import json
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from parse_sheets import split_module

RULES = Path(__file__).resolve().parent / "chapter_rules"

DANGLING = {"the", "of", "in", "and", "a", "an", "to", "for", "with", "by", "on", "or", "from",
            "et", "de", "du", "des", "la", "le", "les", "à", "au", "aux", "en"}
WEEKDAYS = "Mon Tue Wed Thu Fri Sat Sun".split()
REPEATING_KINDS = {"integration", "evaluation", "remediation", "catch_up"}
SPLIT_RE = re.compile(r"\(part\s*\d+\)|\bcontinue[sd]?\b|\bsuite\b", re.I)
KNOWN_SUBJECTS = {"mathematics", "english language", "french", "biology", "chemistry", "physics",
                  "computer science", "history", "geography", "citizenship", "literature in english",
                  "religious studies", "economics", "food science", "manual labour", "sports", "home economics"}
# Activity series numbered independently of lessons; PW and "Practical Work" are the same series.
SERIES_RE = re.compile(r"\b(further stud(?:y|ies)|guided work|practical work|pw|experiment|gw|fs)\s*(\d+)", re.I)
SERIES_NAME = {"further study": "Further study", "further studies": "Further study", "guided work": "Guided work",
               "practical work": "PW", "pw": "PW", "experiment": "Experiment", "gw": "GW", "fs": "FS"}
# Dropped ligatures ("ti", "fi", "tt") in the source text: questons, adjectves, idiomatc, writng,
# artcles, fnancial, defne, leter, tme. Heuristic, flagged for review only.
LIGATURE_RES = [re.compile(p) for p in (
    r"[^t]tons?$",          # -tion(s)  -> -ton(s)
    r"tves?$",              # -tive(s)  -> -tve(s)
    r"[a-z]{3}tcs?$",       # -tic(s)   -> -tc(s)
    r"[a-z]tngs?$",         # -ting(s)  -> -tng(s)
    r"tcle|tcul",           # article, particular
    r"^activies$",          # activities
    r"^(de)?fn|^defne|^modifer",  # fi
    r"^leters?$",           # tt
    r"^tme$|^tps$",         # time, tips
)]
NOT_LIGATURE = {"button", "buttons", "skeleton", "carton", "baton", "proton", "protons", "piston", "boston",
                "washington", "photon", "crouton", "mutton", "etc", "newton", "newtons"}


ASSESSMENT_KINDS = {"integration", "evaluation", "remediation"}
ASSESS_LABEL_RE = re.compile(r"^(.+?)\s*(?::|\.|\()\s*\(?\s*(integration|evaluation|correction|remed|remid)", re.I)


def assessment_label(title):
    """'Understanding soil: Integration' / 'Notion of Embroidery (Evaluation)' -> the chapter name it gives."""
    m = ASSESS_LABEL_RE.match(title)
    return m.group(1).strip(" .:") if m else None


def match_chapter(label, chapters):
    """Best chapter for a label by shared word stems; None if nothing is shared."""
    scored = sorted(((len(stems(label) & stems(c)), -len(stems(c) ^ stems(label)), c) for c in chapters), reverse=True)
    return scored[0][2] if scored and scored[0][0] else None


def year_bounds(year):
    """'2026-27' -> (2026-09-01, 2027-07-31). ASSUMPTION: confirm against the official calendar."""
    y1 = int(year[:4])
    return date(y1, 9, 1), date(y1 + 1, 7, 31)


def lessons_of(spine):
    return [l for t in spine["terms"] for l in t["lessons"]]


def d(s):
    return date.fromisoformat(s) if s else None


def fmt(l):
    no = f"Lesson {l['lesson_no']}" if l["lesson_no"] is not None else l["kind"].replace("_", " ")
    return f"seq {l['seq']} ({no}: {l['title'][:70]})"


def norm_title(t):
    words = re.sub(r"[^\w\s]", " ", t.lower()).split()
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("s") else w for w in words)


def stems(text):
    return {w[:5] for w in re.findall(r"[a-zà-ÿ]{4,}", text.lower())} - {"and", "the", "with", "from"}


def dropped_ligature(word):
    w = word.lower()
    return len(w) >= 3 and w.isalpha() and w not in NOT_LIGATURE and any(r.search(w) for r in LIGATURE_RES)


def validate(spine, chapter_rules=None, resolved=frozenset()):
    """Returns a list of issue dicts: severity, check, seqs, rows, problem, fix."""
    issues = []

    def add(sev, check, ls, problem, fix):
        rows = [l["raw"]["seq"] for l in ls]
        if ls and all((check, r) in resolved for r in rows):
            return
        issues.append({"severity": sev, "check": check, "seqs": [l["seq"] for l in ls], "rows": rows,
                       "problem": problem, "fix": fix})

    lessons = lessons_of(spine)
    lo, hi = year_bounds(spine["year"])
    y1 = lo.year

    # --- sheet-level ---------------------------------------------------------------------------
    if spine["subject"] not in KNOWN_SUBJECTS:
        guess = re.sub(r"(?i)\s+(ok|final|v\d+|draft)$", "", spine["subject_label"]).lower()
        add("warn", "subject-name", [], f"Subject on the sheet header is '{spine['subject_label']}', not a known subject name.",
            f"Probably '{guess}'. Confirm, then add a subject override (it also renames the output file).")
    deleted = spine.get("deleted_rows", [])
    if spine.get("declared_lessons") is not None and spine["declared_lessons"] - len(deleted) != len(lessons):
        add("error", "lesson-count-mismatch", [], f"Header declares {spine['declared_lessons']} lessons; {len(lessons)} rows parsed"
            + (f" after deleting rows {deleted}" if deleted else "") + ".", "Check for dropped or duplicated rows.")
    term_nos = [t["term"] for t in spine["terms"]]
    if term_nos != [1, 2, 3]:
        later = [l for l in lessons if l["start"] and l["start"] >= f"{y1 + 1}-03-08"]
        hint = (f" The other sheets mostly start Term 3 on {y1 + 1}-03-08; here that is {fmt(later[0])}." if later else "")
        add("error", "term-headers", [], f"Terms found: {term_nos} (expected [1, 2, 3]).{hint}",
            "Add the missing term header at the right row (an override); the app needs term boundaries.")

    # --- dates ---------------------------------------------------------------------------------
    weekend = {}
    for l in lessons:
        s, e = d(l["start"]), d(l["end"])
        if s is None or e is None:
            add("error", "unparseable-date", [l], f"{fmt(l)}: date(s) missing or invalid in '{l['raw']['period']}'.",
                "Read the real dates from the original sheet.")
            continue
        if e < s:
            add("error", "end-before-start", [l], f"{fmt(l)}: ends {e}, before it starts {s}.",
                "The two dates are probably swapped: swap them (override).")
        for label, x in (("start", s), ("end", e)):
            if x.weekday() >= 5:
                weekend.setdefault((label, x), []).append(l)
            expected = y1 if x.month >= 9 else y1 + 1
            if x.year != expected:
                add("error", "wrong-year", [l], f"{fmt(l)}: {label} {x} has year {x.year}; that month of {spine['year']} is in {expected}.",
                    f"Likely typo: change the year to {expected}, keeping day and month.")
            elif not lo <= x <= hi:
                add("error", "outside-academic-year", [l], f"{fmt(l)}: {label} {x} is outside {lo}..{hi}.",
                    "Confirm the date with the school.")
    for (label, x), ls in weekend.items():
        near = x - timedelta(days=x.weekday() - 4) if label == "end" else x + timedelta(days=7 - x.weekday())
        add("info", "weekend-date", ls, f"{len(ls)} row(s) {label} on {x}, a {WEEKDAYS[x.weekday()]}: seq "
            + ", ".join(str(l["seq"]) for l in ls) + ".",
            f"None: dates are approximate windows (decision 2026-10-02). Nearest school day: {near}.")
    for a, b in zip(lessons, lessons[1:]):
        if a["start"] and b["start"] and b["start"] < a["start"]:
            add("info", "dates-go-backwards", [a, b], f"{fmt(b)} starts {b['start']}, before the previous row ({a['start']}).",
                "None needed: seq order wins; dates are approximate windows.")
    blocks = []
    for l in lessons:
        key = (l["chapter"], l["start"], l["end"])
        if not blocks or blocks[-1][0] != key:
            blocks.append((key, []))
        blocks[-1][1].append(l)
    for (ka, la), (kb, lb) in zip(blocks, blocks[1:]):
        if ka[2] and kb[1] and kb[1] <= ka[2] and ka[0] != kb[0] and ka[1:] != kb[1:]:
            add("info", "overlapping-windows", [la[0], lb[0]],
                f"'{ka[0]}' runs {ka[1]}..{ka[2]}; '{kb[0]}' starts {kb[1]}, inside that window.",
                "None needed: seq order wins; dates are approximate windows.")

    # --- numbering -----------------------------------------------------------------------------
    numbered = [l for l in lessons if l["lesson_no"] is not None]
    for a, b in zip(numbered, numbered[1:]):
        if b["lesson_no"] < a["lesson_no"]:
            same = a["start"] == b["start"] and a["end"] == b["end"]
            add("error", "non-monotonic-lesson-no", [a, b], f"{fmt(a)} is followed by {fmt(b)}: lesson numbers go backwards.",
                f"Swap the rows so Lesson {b['lesson_no']} comes first." + (" Dates are identical." if same else "")
                if b["lesson_no"] == a["lesson_no"] - 1 else "Check whether the number or the position is wrong.")
    for l in lessons:
        if l["kind"] == "lesson" and l["lesson_no"] is None and numbered:
            add("warn", "missing-lesson-no", [l], f"{fmt(l)}: no lesson number in '{l['raw']['title'][:60]}'.",
                "Assign the number from the syllabus, or mark it as a non-lesson activity.")
    nums = sorted({l["lesson_no"] for l in numbered})
    gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in nums] if nums else []
    if gaps:
        add("warn", "lesson-no-gap", [], f"Lesson numbers missing from the sequence: {gaps}.", "Check for dropped lessons.")
    by_no = {}
    for l in numbered:
        by_no.setdefault(l["lesson_no"], []).append(l)
    for n, ls in by_no.items():
        if len(ls) > 1:
            if all(SPLIT_RE.search(l["title"]) for l in ls[1:]):
                continue  # "Lesson 2 (Part 2)" / "Lesson 2 continues" are planned splits
            add("error", "duplicate-lesson-no", ls, f"Lesson {n} appears {len(ls)} times: " + "; ".join(fmt(l) for l in ls) + ".",
                "Renumber or delete the repeated row; see also duplicate-title.")
    seqs = [l["raw"]["seq"] for l in lessons]
    if sorted(seqs + deleted) != list(range(1, len(seqs) + len(deleted) + 1)):
        add("error", "seq-gap", [], f"Sheet row numbers are not 1..{len(seqs)}.", "Check for dropped or duplicated rows.")

    tu_rows = [l for l in lessons if "tu" in l]
    if tu_rows:
        for l in lessons:
            if "tu" not in l:
                add("info", "missing-tu", [l], f"{fmt(l)}: no teaching-unit (TU) number, unlike the rest of the sheet.",
                    "None: left null (decision 2026-10-02).")
        for a, b in zip(tu_rows, tu_rows[1:]):
            if b["tu"] < a["tu"]:
                add("error", "non-monotonic-tu", [a, b], f"TU {a['tu']} is followed by TU {b['tu']}.", "Check the TU numbers.")
            elif b["tu"] == a["tu"] and not SPLIT_RE.search(b["title"]):
                add("warn", "repeated-tu", [a, b], f"TU {a['tu']} is used for two different rows: {fmt(a)} and {fmt(b)}.",
                    "Either a planned two-period unit (mark it 'Part 2') or a numbering slip.")
        tus = sorted({l["tu"] for l in tu_rows})
        tgap = [n for n in range(tus[0], tus[-1] + 1) if n not in tus]
        if tgap:
            add("info", "tu-gap", [], f"TU numbers missing: {tgap}.",
                "None if caused by an approved deletion or a TU left null (decision 2026-10-02).")

    series = {}
    for l in lessons:
        m = SERIES_RE.search(l["title"])
        if m:
            series.setdefault(SERIES_NAME[m.group(1).lower()], []).append((int(m.group(2)), l))
    for name, items in series.items():
        for (na, la), (nb, lb) in zip(items, items[1:]):
            if nb < na or (nb == na and norm_title(la["title"]) != norm_title(lb["title"]) and not SPLIT_RE.search(lb["title"])):
                add("warn", "activity-numbering", [la, lb], f"'{name} {na}' is followed by '{name} {nb}'.",
                    f"Probably '{name} {na + 1}'. Confirm the number.")

    # --- duplicates ----------------------------------------------------------------------------
    groups, loose = {}, {}
    for l in lessons:
        if l["kind"] in REPEATING_KINDS:
            continue
        groups.setdefault((l["chapter"], norm_title(l["title"])), []).append(l)
        loose.setdefault((l["chapter"], norm_title(re.sub(r"\(.*?\)", "", l["title"]))), []).append(l)
    exact = set()
    for ls in groups.values():
        if len(ls) > 1:
            exact.update(id(l) for l in ls)
            add("error", "duplicate-title", ls, "Same lesson listed twice in one chapter: " + "; ".join(fmt(l) for l in ls) + ".",
                "Delete the repeated row, or retitle it if it is a different lesson.")
    for ls in loose.values():
        if len(ls) > 1 and not all(id(l) in exact for l in ls) and not all(SPLIT_RE.search(l["title"]) for l in ls):
            add("warn", "near-duplicate-title", ls, "Titles differ only in bracketed detail: " + "; ".join(fmt(l) for l in ls) + ".",
                "Probably one lesson listed twice; merge, or confirm they are two periods.")

    # --- chapters ------------------------------------------------------------------------------
    for l in lessons:
        if l["raw"].get("chapter_wrap_merged"):
            add("warn", "chapter-wrap-merged", [l],
                f"{fmt(l)}: chapter cell '{l['raw']['chapter_wrap_merged']}' was the end of the previous chapter's text, "
                f"merged into '{l['chapter']}'.", "None if the merged name is right; otherwise override the chapter.")
    order = []
    for l in lessons:
        if not order or order[-1] != l["chapter"]:
            order.append(l["chapter"])
    for ch in sorted({c for c in order if order.count(c) > 1}):
        add("warn", "chapter-not-contiguous", [l for l in lessons if l["chapter"] == ch][:1],
            f"Chapter '{ch}' appears in separate blocks.", "Check whether lessons were misplaced.")
    # A chapter's printed cell, found by name: an approved move can carry the cell row elsewhere.
    # Key by the row's current chapter first (survives renames), then by the printed name (survives moves).
    cell_of = {}
    cells = [(l, l["raw"]["chapter_cell"]) for l in lessons
             if l["raw"]["chapter_cell"] and not l["raw"].get("chapter_wrap_merged")]
    for l, c in cells:
        cell_of.setdefault(l["chapter"], c)
    for l, c in cells:
        cell_of.setdefault(split_module(c)[1], c)
    numbers, unnumbered, prev_ch = [], [], None
    for l in lessons:
        cell = cell_of.get(l["chapter"])
        if not cell or l["chapter"] == prev_ch:
            continue
        prev_ch = l["chapter"]
        if re.match(r"\s*RLS", cell, re.I):
            continue  # English: RLS sub-chapters are unnumbered by design; modules carry the numbers
        m = re.match(r'\s*"?\s*(?:chap(?:ter)?\s*(\d+)|([IVX]+)\s*\.|(\d+)\s*[.\s])', cell, re.I)
        if m:
            roman = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}
            n = int(m.group(1) or m.group(3)) if (m.group(1) or m.group(3)) else roman.get(m.group(2).upper())
            numbers.append((n, l))
        else:
            unnumbered.append(l)
    if numbers:
        for (na, la), (nb, lb) in zip(numbers, numbers[1:]):
            if nb != na + 1:
                add("warn", "chapter-numbering", [lb], f"Chapter number {na} ('{la['chapter']}') is followed by {nb} ('{lb['chapter']}').",
                    "Check the chapter numbers.")
        if unnumbered:
            add("info", "chapter-unnumbered", unnumbered,
                f"{len(unnumbered)} chapter(s) have no number while others do: " + "; ".join(f"'{l['chapter']}'" for l in unnumbered[:8])
                + ("..." if len(unnumbered) > 8 else "") + ".", "Cosmetic, unless a number is needed for ordering.")
    cross = {}
    for l in lessons:
        if l["kind"] not in ASSESSMENT_KINDS:
            continue
        label = assessment_label(l["title"])
        if label and not l.get("assesses"):
            add("warn", "assessment-target-unknown", [l], f"{fmt(l)} names '{label}', which matches no chapter of this sheet.",
                "Set `assesses` with an override.")
        elif l.get("assesses") and l["assesses"] != l["chapter"]:
            cross.setdefault((l["assesses"], l["chapter"]), []).append(l)
    for (target, ch), ls in cross.items():
        add("info", "assesses-other-chapter", ls,
            f"seq {', '.join(str(l['seq']) for l in ls)} sit in '{ch}' but assess '{target}' (field `assesses`).",
            "None: labels kept; the app links these results to the assessed chapter (decision 2026-10-02).")
    if chapter_rules:
        for l in lessons:
            own = chapter_rules.get(l["chapter"])
            t = l["title"].lower()
            if own is None or any(k in t for k in own):
                continue
            hits = [c for c, ks in chapter_rules.items() if c != l["chapter"] and any(k in t for k in ks)]
            if hits:
                add("info", "chapter-mismatch", [l], f"{fmt(l)} is filed under '{l['chapter']}' but its title points to {hits}.",
                    "None: the official sheet structure wins (decision 2026-10-02). Shown for awareness.")

    # --- title typos ---------------------------------------------------------------------------
    for l in lessons:
        t, raw = l["title"], l["raw"]
        sep = raw.get("separator")
        if sep and re.fullmatch(r"\.{2,}", sep):
            add("info", "typo-double-dot", [l], f"{fmt(l)}: '{sep}' after the lesson number.", "Cosmetic.")
        if re.match(r"\s*Le{2,}s|\s*Less{2,}", raw["title"]):
            add("info", "typo-lesson-prefix", [l], f"{fmt(l)}: lesson prefix misspelt in '{raw['title'][:20]}'.", "Cosmetic.")
        if t.count("(") != t.count(")"):
            add("info", "typo-unbalanced-bracket", [l], f"{fmt(l)}: unbalanced parenthesis.", "Cosmetic: close the bracket.")
        words = re.sub(r"[^\w\s]", "", t.lower()).split()
        last = t.split()[-1] if t.split() else ""
        if words and l["kind"] == "lesson" and re.fullmatch(r"[\w’']+[,;]?", last) and                 (words[-1] in DANGLING or t.lower().endswith(("in the set", "the set"))):
            add("warn", "truncated-title", [l], f"{fmt(l)}: title looks cut off ('...{' '.join(words[-3:])}').",
                "Get the full title from the syllabus.")
    if not spine["subject"].startswith("french"):
        hits = {}
        for l in lessons:
            for w in re.findall(r"[A-Za-z]+", f"{l['title']} {l['chapter']} {l.get('module') or ''}"):
                if dropped_ligature(w):
                    hits.setdefault(w, []).append(l)
        if hits:
            ls = sorted({id(x): x for v in hits.values() for x in v}.values(), key=lambda x: x["seq"])
            add("warn", "dropped-ligatures", ls,
                f"{len(hits)} words look like the source lost 'ti'/'fi'/'tt' letters (e.g. " +
                ", ".join(sorted(hits)[:12]) + ("..." if len(hits) > 12 else "") + f"), across {len(ls)} rows.",
                "Restore the letters (questons -> questions, fnancial -> financial, leter -> letter). "
                "One bulk override per word, after review. Learners see these titles.")

    add("info", "summary", [], f"{len(lessons)} rows parsed; per term {[len(t['lessons']) for t in spine['terms']]}; "
        f"kinds {dict(Counter(l['kind'] for l in lessons))}.", "None.")
    return issues


def todo(v):
    return not v or v == "TODO"


def validate_calendar(spine, cal):
    """Drift between a spine and the official calendar file. Info only: the app uses the calendar."""
    issues = []

    def add(check, ls, problem):
        issues.append({"severity": "info", "check": check, "seqs": [l["seq"] for l in ls],
                       "rows": [l["raw"]["seq"] for l in ls], "problem": problem,
                       "fix": "None: the app follows data/calendar, not the sheet."})

    lessons = lessons_of(spine)
    if cal.get("year") != spine["year"]:
        add("calendar-year", [], f"Calendar is for {cal.get('year')}, sheet is for {spine['year']}.")
        return issues
    term1 = next((t for t in cal.get("terms", []) if t["term"] == 1), {})
    if todo(term1.get("start")) and not todo(cal.get("start")) and lessons and lessons[0]["start"]             and lessons[0]["start"] != cal["start"]:  # otherwise the Term 1 check below reports it
        add("calendar-drift", lessons[:1], f"Sheet starts {lessons[0]['start']}; calendar year starts {cal['start']}.")
    if not todo(cal.get("end")):
        late = [l for l in lessons if l["end"] and l["end"] > cal["end"]]
        if late:
            add("calendar-drift", late[:1], f"{len(late)} row(s) end after the calendar year ends ({cal['end']}).")
    for ct in cal.get("terms", []):
        st = next((t for t in spine["terms"] if t["term"] == ct["term"] and t["lessons"]), None)
        if not st:
            continue
        first, last = st["lessons"][0], st["lessons"][-1]
        if not todo(ct.get("start")) and first["start"] and first["start"] != ct["start"]:
            add("calendar-drift", [first], f"Term {ct['term']} starts {first['start']} on the sheet, {ct['start']} in the calendar.")
        if not todo(ct.get("end")) and last["end"] and last["end"] > ct["end"]:
            add("calendar-drift", [last], f"Term {ct['term']} runs to {last['end']} on the sheet; the calendar ends it {ct['end']}.")
    for h in cal.get("holidays", []) + cal.get("evaluation_weeks", []):
        if todo(h.get("start")) or todo(h.get("end")):
            continue
        inside = [l for l in lessons if l["start"] and l["start"] >= h["start"] and l["end"] <= h["end"]]
        if inside:
            add("calendar-drift", inside, f"{len(inside)} row(s) are scheduled entirely inside '{h['name']}' "
                f"({h['start']} to {h['end']}).")
    return issues


def calendar_todos(cal):
    n = sum(todo(cal.get(k)) for k in ("start", "end"))
    for group in ("terms", "holidays", "evaluation_weeks"):
        n += sum(todo(x.get("start")) + todo(x.get("end")) for x in cal.get(group, []))
    return n


def load_rules(stem):
    rp = RULES / f"{stem}.json"
    if not rp.exists():
        return None
    return {k: v for k, v in json.loads(rp.read_text(encoding="utf-8")).items() if not k.startswith("_")}
