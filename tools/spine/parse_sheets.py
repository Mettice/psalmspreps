"""Parse MINESEC progression-sheet PDFs into raw spine dicts.

Nothing is corrected here. The parser only normalises layout noise (the diagonal
watermark, line wraps, bullet glyphs, quotes around chapter names, chapter text
that wrapped into the next row) and keeps the original cell text in each lesson's
`raw` field so every later fix can be audited against the sheet.

Use tools/spine/build.py to run the whole pipeline.
"""
import re
import unicodedata
from datetime import datetime

WATERMARK_MIN_SIZE = 15  # the diagonal "OFFICIEL" watermark is >20pt; table text is <10pt

# English and French header variants (matched after accent folding).
TERM_WORDS = {"FIRST": 1, "SECOND": 2, "THIRD": 3,
              "PREMIER": 1, "PREMIERE": 1, "DEUXIEME": 2, "TROISIEME": 3}
META_KEYS = {"class": ("class", "classe"),
             "subject": ("subjects", "subject", "matiere", "matieres", "discipline", "disciplines")}
YEAR_RE = re.compile(r"(?:Academic calendar|Calendrier (?:acad[ée]mique|scolaire)|Ann[ée]e scolaire)"
                     r"\s*:\s*(\d{4})\s*[-/]\s*(\d{2,4})", re.I)
DECLARED_RE = re.compile(r"\((\d+)\s+(?:Lessons|Le[çc]ons)\)", re.I)
DATE_RE = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")
# "Lesson 1.", "Lesson 1:", "Lesson:44-", "Leçon15.", "Leçon 5 .", "Leeson 12:", "Lesson 33 Reactions"
LESSON_RE = re.compile(r"^\s*(Le+s+on|Le[çc]on)\s*:?\s*(\d+)\s*([.:\-–]*)\s*(.*)$", re.S | re.I)
TU_RE = re.compile(r"^\s*TU\s*(\d+)\s*[.:]?\s*(.*)$", re.S | re.I)
BULLETS = "◆•▪●■"
DANGLING = {"the", "of", "in", "and", "a", "an", "to", "for", "with", "by", "on", "or", "from",
            "et", "de", "du", "des", "la", "le", "les", "à", "au", "aux", "en"}
# Chapter-start markers ("Chap 3:", "Chapter 2:", "II.", "4.", "RLS:").
CHAPTER_MARKER_RE = re.compile(r'^\s*"?\s*(chap(ter)?\s*\d+|[IVX]+\s*\.|\d+\s*\.|\d+\s|RLS\s*:)', re.I)

KINDS = [  # first match wins; checked against the raw title cell
    ("catch_up", r"catch[- ]?up"),
    ("remediation", r"remed|remid|correction|revision and consolidation"),
    ("evaluation", r"[ée]valuation"),
    ("integration", r"int[ée]gration"),
    ("further_study", r"^\s*(TU\s*\d+\s*[.:]?\s*)?(further stud|FS\s*\d)"),
    ("practical", r"\bPW\s*\d|practical work|experiment\s*\d"),
    ("group_work", r"\bGW\s*\d"),
    ("further_study", r"further stud|\bFS\s*\d"),
    ("guided_work", r"guided work"),
]


def fold(s):
    """Lowercase ASCII fold for matching header words (é -> e)."""
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def squash(text):
    """Collapse whitespace; drop private-use glyphs (Symbol-font bullets) and bullet characters."""
    text = "".join(" " if unicodedata.category(ch) == "Co" or ch in BULLETS else ch for ch in (text or ""))
    return re.sub(r"\s+", " ", text).strip()


def iso(d, m, y):
    try:
        return datetime(int(y), int(m), int(d)).date().isoformat()
    except ValueError:
        return None


def clean_chapter(raw):
    """Layout cleanup only: quotes, leading chapter number, continuation marker, trailing full stop."""
    c = squash(raw).strip('"').strip()
    c = re.sub(r"^(chap(ter)?\s*\d+\s*[:.]?|[IVX]+\s*\.|\d+\s*\.?)\s*", "", c, flags=re.I)
    c = re.sub(r"\s*\((cont'?d?|continues|suite)\.?\)\s*$", "", c, flags=re.I)
    return c.strip(' ".')


def split_module(raw):
    """'Chap2: Family life - RLS: Describing family' -> ('Family life', 'Describing family').

    English-language sheets put a module (Chap N) and a real-life situation (RLS) in one cell.
    """
    parts = re.split(r"\bRLS\s*:\s*", squash(raw), maxsplit=1)
    if len(parts) == 1:
        return None, clean_chapter(raw)
    module = clean_chapter(re.sub(r"[\s.\-–]+$", "", parts[0]))
    return (module or None), clean_chapter(parts[1])


def kind_of(cell):
    for kind, pat in KINDS:
        if re.search(pat, squash(cell), re.I):
            return kind
    return "lesson"


def split_title(cell):
    """Returns (tu, lesson_no, title, separator) from a raw title cell."""
    text = squash(cell)
    tu = None
    m = TU_RE.match(text)
    if m:
        tu, text = int(m.group(1)), m.group(2)
    m = LESSON_RE.match(text)
    if m:  # "Lesson 2 (Part 1): Our Planet" keeps "(Part 1)" in the title
        return tu, int(m.group(2)), re.sub(r"^[-–]\s*", "", m.group(4)).rstrip(".").strip(), m.group(3)
    return tu, None, re.sub(r"^[-–]\s*", "", text).rstrip(".").strip(), None


def looks_like_wrap(prev_chapter_raw, fragment, marked_sheet, same_window):
    """A chapter cell that continues the previous row's chapter text instead of starting a new one.

    Only possible when the row shares the previous row's dates and term: a wrapped
    fragment is printed in the very next row of the same block.
    """
    frag, prev = squash(fragment), squash(prev_chapter_raw)
    if not frag or not prev or not same_window:
        return False
    if re.sub(r"\W", "", prev.split()[-1].lower()) in DANGLING or frag[0].islower():
        return True
    # In sheets that mark every chapter ("Chap 3", "RLS:", "II."), a short unmarked fragment is a wrap.
    return marked_sheet and not CHAPTER_MARKER_RE.match(frag) and len(frag.split()) <= 3


def parse_rows(rows, header_text="", source=""):
    """rows: table rows as lists of cell strings, watermark already removed."""
    meta = {}
    m = YEAR_RE.search(header_text)
    if m:
        meta["year"] = f"{m.group(1)}-{m.group(2)[-2:]}"
    lesson_rows, terms, current = [], [], None
    for row in rows:
        row = [squash(c) for c in row] + [""] * 4
        for i in (0, 2):  # header rows are "Key: | value | Key: | value"
            k = fold(row[i]).rstrip(":").strip()
            for field, names in META_KEYS.items():
                if k in names and row[i + 1]:
                    meta[field] = row[i + 1]
        d = DECLARED_RE.search(row[1])
        if d and fold(row[0]).startswith(("term", "trimestre", "periode")):
            meta["declared_lessons"] = int(d.group(1))
        words = fold(row[0]).upper().replace("-", " ").split()
        if any(w in ("TERM", "TRIMESTRE") for w in words) and not any(row[1:4]):
            num = next((TERM_WORDS[w] for w in words if w in TERM_WORDS), None)
            num = num or next((int(w) for w in words if w.isdigit()), None)
            current = {"term": num, "lessons": []}
            terms.append(current)
        elif row[0].isdigit():
            if current is None:
                current = {"term": None, "lessons": []}
                terms.append(current)
            lesson_rows.append((current, row))

    chapter_cells = [r[2] for _, r in lesson_rows if r[2]]
    marked = len(chapter_cells) >= 3 and \
        sum(bool(CHAPTER_MARKER_RE.match(c)) for c in chapter_cells) / len(chapter_cells) >= 0.8
    uses_modules = any(re.search(r"\bRLS\s*:", c) for c in chapter_cells)

    chapter_raw, module, prev_key, done = "", None, None, []
    for term, row in lesson_rows:
        period, ch, cell = row[1], row[2], row[3]
        raw = {"seq": int(row[0]), "period": period, "chapter_cell": ch, "title": cell}
        key = (id(term), period)
        same_window, prev_key = key == prev_key, key
        if ch and chapter_raw and looks_like_wrap(chapter_raw, ch, marked, same_window):
            old = split_module(chapter_raw)[1]
            chapter_raw = f"{chapter_raw} {ch}"
            new = split_module(chapter_raw)[1]
            for prev in reversed(done):  # earlier rows of the chapter get the completed name too
                if prev["chapter"] != old:
                    break
                prev["chapter"] = new
            raw["chapter_wrap_merged"] = ch
        elif ch:
            chapter_raw = ch
            if uses_modules and re.match(r"\s*chap", ch, re.I):
                module = split_module(ch)[0] or clean_chapter(ch)
        dates = DATE_RE.findall(period)
        tu, no, title, sep = split_title(cell)
        raw["separator"] = sep
        lesson = {
            "seq": int(row[0]),
            "lesson_no": no,
            "chapter": split_module(chapter_raw)[1],
            "title": title,
            "start": iso(*dates[0]) if len(dates) > 0 else None,
            "end": iso(*dates[1]) if len(dates) > 1 else None,
            "kind": kind_of(cell),
            "raw": raw,
        }
        if tu is not None:
            lesson["tu"] = tu
        if module:
            lesson["module"] = module
        term["lessons"].append(lesson)
        done.append(lesson)

    subject = meta.get("subject", "")
    return {
        "subject": subject.lower(),
        "subject_label": subject,
        "class": meta.get("class"),
        "year": meta.get("year"),
        "source": source,
        "declared_lessons": meta.get("declared_lessons"),
        "terms": terms,
    }


def extract(path):
    """Returns (header_text, rows) from a PDF with the watermark removed."""
    import pdfplumber

    rows, header = [], ""
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            clean = page.filter(lambda o: o.get("object_type") != "char" or o["size"] < WATERMARK_MIN_SIZE)
            if i == 0:
                header = clean.extract_text() or ""
            for table in clean.extract_tables():
                rows.extend([c or "" for c in r] for r in table)
    return header, rows


def parse_pdf(path):
    header, rows = extract(path)
    return parse_rows(rows, header, path.name)
