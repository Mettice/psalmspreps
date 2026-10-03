"""Apply human-approved overrides (data/spine/overrides/{sheet}.json) to a raw spine.

Overrides address lessons by the row number printed on the sheet (`raw.seq`), which
never changes. After all ops, `seq` is renumbered 1..N so it stays the order of truth.
The `raw` block of every lesson is never modified.

Ops
  set            {seq, field, value}                 change one display field of one row
  swap           {seqs: [a, b]}                      swap two rows' positions
  move           {seq, before}                       move a row to just before another row
  delete         {seqs: [...]}                       remove rows (e.g. duplicates)
  split_term     {seq, term}                         start a new term at this row
  set_meta       {values: {subject, subject_label}}  sheet-level fields
  rename_chapter {from, to}                          display name of a chapter
  replace_words  {words: {wrong: right}, fields?}    whole-word display fixes, case kept
  resolve        {seqs, check}                       acknowledge a cosmetic issue
Every op needs id, reason, approved_by. `expect` (optional) guards against a changed sheet.
"""
import copy
import re

SETTABLE = {"title", "chapter", "lesson_no", "start", "end", "kind", "module", "assesses"}
META = {"subject", "subject_label"}
WORD_FIELDS = ("title", "chapter", "module")


class OverrideError(Exception):
    pass


def _rows(spine):
    return {l["raw"]["seq"]: l for t in spine["terms"] for l in t["lessons"]}


def _check_expect(rows, ov):
    exp = ov.get("expect") or {}
    # single-row ops use a flat {"field": value}; multi-row ops use {"row": {...}}
    if exp and all(isinstance(v, dict) for v in exp.values()):
        pairs = [(int(k), v) for k, v in exp.items()]
    else:
        pairs = [(ov["seq"], exp)] if exp else []
    for row, fields in pairs:
        if row not in rows:
            raise OverrideError(f"{ov['id']}: sheet row {row} does not exist")
        for f, v in fields.items():
            if rows[row].get(f) != v:
                raise OverrideError(f"{ov['id']}: row {row} {f} is {rows[row].get(f)!r}, expected {v!r}. "
                                    "The sheet changed; review this override.")


def _match_case(src, dst):
    return dst[:1].upper() + dst[1:] if src[:1].isupper() else dst


def replace_words(text, words):
    """Whole-word, case-insensitive replacement keeping the first letter's case. Returns (text, hits)."""
    hits = {}
    for wrong, right in words.items():
        pat = re.compile(rf"(?<![\w]){re.escape(wrong)}(?![\w])", re.I)
        text, n = pat.subn(lambda m: _match_case(m.group(0), right), text)
        if n:
            hits[wrong] = n
    return text, hits


def apply(spine, overrides):
    """Returns (new_spine, resolved) where resolved is a set of (check, sheet_row)."""
    out = copy.deepcopy(spine)
    resolved, log = set(), []
    for ov in overrides:
        for key in ("id", "op", "reason", "approved_by"):
            if not ov.get(key):
                raise OverrideError(f"override {ov.get('id', '?')} is missing '{key}'")
        rows = _rows(out)
        _check_expect(rows, ov)
        op, targets = ov["op"], []
        if op == "set":
            if ov["field"] not in SETTABLE:
                raise OverrideError(f"{ov['id']}: field {ov['field']!r} cannot be overridden")
            rows[ov["seq"]][ov["field"]] = ov["value"]
            targets = [ov["seq"]]
        elif op == "swap":
            a, b = ov["seqs"]
            la, lb = rows[a], rows[b]
            for t in out["terms"]:
                idx = {id(l): i for i, l in enumerate(t["lessons"])}
                if (id(la) in idx) != (id(lb) in idx):
                    raise OverrideError(f"{ov['id']}: rows {a} and {b} are in different terms")
                if id(la) in idx:
                    t["lessons"][idx[id(la)]], t["lessons"][idx[id(lb)]] = lb, la
            targets = [a, b]
        elif op == "move":
            row, anchor = rows.get(ov["seq"]), rows.get(ov["before"])
            if row is None or anchor is None:
                raise OverrideError(f"{ov['id']}: rows {ov['seq']} / {ov['before']} must both exist")
            for t in out["terms"]:
                t["lessons"] = [l for l in t["lessons"] if l is not row]
            for t in out["terms"]:
                if any(l is anchor for l in t["lessons"]):
                    t["lessons"].insert(next(i for i, l in enumerate(t["lessons"]) if l is anchor), row)
            targets = [ov["seq"]]
        elif op == "delete":
            missing = [r for r in ov["seqs"] if r not in rows]
            if missing:
                raise OverrideError(f"{ov['id']}: rows {missing} do not exist")
            for t in out["terms"]:
                t["lessons"] = [l for l in t["lessons"] if l["raw"]["seq"] not in ov["seqs"]]
            out.setdefault("deleted_rows", []).extend(ov["seqs"])
        elif op == "split_term":
            row = rows.get(ov["seq"])
            for i, t in enumerate(out["terms"]):
                pos = next((j for j, l in enumerate(t["lessons"]) if l is row), None)
                if pos is not None:
                    if pos == 0:
                        raise OverrideError(f"{ov['id']}: row {ov['seq']} already starts a term")
                    new = {"term": ov["term"], "lessons": t["lessons"][pos:]}
                    t["lessons"] = t["lessons"][:pos]
                    out["terms"].insert(i + 1, new)
                    break
            else:
                raise OverrideError(f"{ov['id']}: row {ov['seq']} does not exist")
            targets = [ov["seq"]]
        elif op == "set_meta":
            bad = set(ov["values"]) - META
            if bad:
                raise OverrideError(f"{ov['id']}: cannot set {sorted(bad)}")
            out.update(ov["values"])
        elif op == "rename_chapter":
            hit = [l for l in rows.values() if l["chapter"] == ov["from"]]
            if not hit:
                raise OverrideError(f"{ov['id']}: no chapter named {ov['from']!r}")
            for l in hit:
                l["chapter"] = ov["to"]
            targets = [l["raw"]["seq"] for l in hit]
        elif op == "replace_words":
            seen = {}
            for r, l in rows.items():
                changed = False
                for f in ov.get("fields", WORD_FIELDS):
                    if l.get(f):
                        l[f], hits = replace_words(l[f], ov["words"])
                        changed |= bool(hits)
                        for w, n in hits.items():
                            seen[w] = seen.get(w, 0) + n
                if changed:
                    targets.append(r)
            unused = sorted(set(ov["words"]) - set(seen))
            if unused:
                raise OverrideError(f"{ov['id']}: words not found (sheet changed?): {unused}")
        elif op == "resolve":
            resolved.update((ov["check"], r) for r in ov["seqs"])
            targets = ov["seqs"]
        else:
            raise OverrideError(f"{ov['id']}: unknown op {op!r}")
        for check in ov.get("resolves", []):
            resolved.update((check, r) for r in targets)
        rows = _rows(out)
        for r in targets:
            if r in rows:
                rows[r].setdefault("overrides", []).append(ov["id"])
        log.append({k: ov[k] for k in ("id", "op", "reason", "approved_by", "approved_on") if k in ov})
    seq = 0
    for t in out["terms"]:
        for l in t["lessons"]:
            seq += 1
            l["seq"] = seq
    out["overrides_applied"] = log
    return out, resolved
