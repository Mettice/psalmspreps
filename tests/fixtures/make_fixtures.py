"""Regenerate tests/fixtures/sheet_rows.json: real table rows copied verbatim from the PDFs.

    python tests/fixtures/make_fixtures.py

Rows are what pdfplumber returns after the watermark filter, so parser tests run on
real sheet data without needing the PDFs.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "spine"))
import parse_sheets  # noqa: E402

PICK = {  # fixture name -> (sheet, row numbers to keep)
    "english_chapter_wrap": ("english-language", [41, 45, 47, 48, 49, 50, 51, 52, 53]),
    "english_modules": ("english-language", [19, 20, 21, 22, 81, 82, 83]),
    "english_title_variants": ("english-language", [44, 70]),
    "french_new_term_not_a_wrap": ("french", [63, 64, 65, 66]),
    "french_ipa": ("french", [37, 71, 15, 16]),
    "maths_dates": ("mathematics", [5, 6, 49]),
    "chemistry_title_variants": ("chemistry", [9, 37, 59, 60, 61]),
    "physics_title_variants": ("physics", [12]),
    "geography_tu": ("geography-ok", [2, 3, 12, 13, 14]),
    "history_tu": ("history", [1, 2, 3, 5, 28]),
    "biology_assessments": ("biology", [15, 19, 20, 21, 22, 23, 24, 32, 33, 34]),
    "home_economics_order": ("home-economics", [1, 6, 7, 8, 9, 10, 11, 12, 13]),
}


def main():
    out = {}
    cache = {}
    for name, (sheet, wanted) in PICK.items():
        if sheet not in cache:
            pdf = ROOT / "data" / "sheets" / f"progression_form-1_{sheet}_annuel.pdf"
            cache[sheet] = (pdf.name, *parse_sheets.extract(pdf))
        source, header, rows = cache[sheet]
        meta = [r for r in rows if r and str(r[0]).rstrip(":") in ("Sub system", "Class", "Term")]
        keep, term = [], None
        for r in rows:
            first = (r[0] or "").strip()
            if "TERM" in first.upper() and not any(r[1:]):
                term = r
            elif first.isdigit() and int(first) in wanted:
                if term is not None:
                    keep.append(term)
                    term = None
                keep.append(r)
        out[name] = {"source": source, "header_line": next(l for l in header.splitlines() if "Academic calendar" in l),
                     "meta_rows": meta, "rows": keep}
    path = Path(__file__).with_name("sheet_rows.json")
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {path} ({len(out)} fixtures)")


if __name__ == "__main__":
    main()
