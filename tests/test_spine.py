"""Run: python -m unittest discover -s tests

Parser tests use real rows from tests/fixtures/sheet_rows.json (copied verbatim from the
PDFs by tests/fixtures/make_fixtures.py). Where no sheet contains a failure mode, the test
says so and builds the case from a real row.
"""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "spine"))
import build  # noqa: E402
import ligatures  # noqa: E402
import overrides as ovr  # noqa: E402
import parse_sheets as P  # noqa: E402
import validate_spine as v  # noqa: E402

FIX = json.loads((ROOT / "tests" / "fixtures" / "sheet_rows.json").read_text(encoding="utf-8"))
SHEETS = ROOT / "data" / "sheets"
RAW = ROOT / "data" / "spine" / "raw"


def parse_fixture(name, rows=None):
    f = FIX[name]
    return P.parse_rows(f["meta_rows"] + (rows if rows is not None else f["rows"]), f["header_line"], f["source"])


def by_row(spine):
    return {l["raw"]["seq"]: l for l in v.lessons_of(spine)}


def checks(spine, **kw):
    return {i["check"] for i in v.validate(spine, **kw)}


# --------------------------------------------------------------------------- new failure modes
class ChapterWrap(unittest.TestCase):
    """English sheet, rows 49-50: chapter 'RLS:Doing Sports to Maintain good' wraps; row 50's cell is 'Health'."""

    def test_fragment_is_merged_into_previous_chapter(self):
        rows = by_row(parse_fixture("english_chapter_wrap"))
        for r in (49, 50, 51, 52):
            self.assertEqual(rows[r]["chapter"], "Doing Sports to Maintain good Health")
        self.assertEqual(rows[50]["raw"]["chapter_wrap_merged"], "Health")
        self.assertEqual(rows[53]["chapter"], "Consulting and Meeting a Health Professional")
        self.assertNotIn("chapter_wrap_merged", rows[53]["raw"])

    def test_merge_is_flagged(self):
        issues = v.validate(parse_fixture("english_chapter_wrap"))
        self.assertIn(("chapter-wrap-merged", [50]), [(i["check"], i["rows"]) for i in issues])

    def test_new_chapter_in_new_term_is_not_a_wrap(self):
        # French row 65 'Communication et TIC' is unnumbered in a numbered sheet, but starts Term 3 with new dates.
        prev = "IV.Activités économiques et\nmonde du travail"
        self.assertFalse(P.looks_like_wrap(prev, "Communication et TIC", marked_sheet=True, same_window=False))
        rows = by_row(parse_fixture("french_new_term_not_a_wrap"))
        self.assertEqual(rows[65]["chapter"], "Communication et TIC")
        self.assertNotIn("chapter_wrap_merged", rows[65]["raw"])


class ReversedDates(unittest.TestCase):
    """No 2026-27 Form 1 sheet has end < start (checked in RealSheets). Built from real Maths row 6, dates swapped."""

    def test_end_before_start_is_an_error(self):
        row = list(FIX["maths_dates"]["rows"][2])
        self.assertEqual(row[0], "6")
        row[1] = "25/09/2026\nau 14/09/2026"
        spine = parse_fixture("maths_dates", [["FIRST TERM", "", "", "", "", ""], row])
        l = v.lessons_of(spine)[0]
        self.assertEqual((l["start"], l["end"]), ("2026-09-25", "2026-09-14"))
        found = [i for i in v.validate(spine) if i["check"] == "end-before-start"]
        self.assertEqual(found[0]["severity"], "error")

    def test_reversed_window_is_left_out_of_break_labelling(self):
        row = list(FIX["maths_dates"]["rows"][2])
        row[1] = "25/09/2026\nau 14/09/2026"
        spine = parse_fixture("maths_dates", [["FIRST TERM", "", "", "", "", ""], row])
        self.assertEqual(build.label_breaks(spine), [])


class AccentsAndIPA(unittest.TestCase):
    def test_fixture_rows_keep_ipa_and_accents(self):
        rows = by_row(parse_fixture("french_ipa"))
        self.assertEqual(rows[37]["title"], "Orthographe : Les sons /Ʒ/ et /ʃ/")
        self.assertIn("/ɥ/,/ɲ/", rows[71]["title"])
        self.assertIn("/ã/", rows[71]["title"])
        self.assertEqual(rows[16]["title"], "Activités d'intégration")

    @unittest.skipUnless((SHEETS / "progression_form-1_french_annuel.pdf").exists(), "needs the French PDF")
    def test_watermark_filter_keeps_ipa_from_the_pdf(self):
        rows = by_row(P.parse_pdf(SHEETS / "progression_form-1_french_annuel.pdf"))
        self.assertIn("/Ʒ/ et /ʃ/", rows[37]["title"])
        self.assertIn("/ɥ/,/ɲ/", rows[71]["title"])
        self.assertEqual(rows[1]["chapter"], "Vie familiale et intégration sociale")

    @unittest.skipUnless((SHEETS / "progression_form-1_english-language_annuel.pdf").exists(), "needs the English PDF")
    def test_watermark_filter_keeps_english_ipa(self):
        rows = by_row(P.parse_pdf(SHEETS / "progression_form-1_english-language_annuel.pdf"))
        self.assertIn("/ə/", rows[78]["title"])
        self.assertIn("/əʊ/ /aʊ/", rows[83]["title"])

    @unittest.skipUnless((SHEETS / "progression_form-1_mathematics_annuel.pdf").exists(), "needs the Maths PDF")
    def test_watermark_letters_do_not_leak(self):
        # Before filtering, this title extracted as 'Time zones in tPhe world'.
        rows = by_row(P.parse_pdf(SHEETS / "progression_form-1_mathematics_annuel.pdf"))
        self.assertEqual(rows[27]["title"], "Time zones in the world")
        self.assertEqual(rows[6]["title"], "Elements of ℕ and of ℕ*")


class Headers(unittest.TestCase):
    def test_english_headers(self):
        s = parse_fixture("maths_dates")
        self.assertEqual((s["subject"], s["class"], s["year"], s["declared_lessons"]), ("mathematics", "Form 1", "2026-27", 69))

    def test_french_headers(self):
        # No 2026-27 sheet uses French headers; header text is synthetic, the lesson row is real (French row 15).
        meta = [["Sous-système:", "Francophone", "Type d'enseignement:", "Général"],
                ["Classe:", "6e", "Matière:", "Mathématiques"],
                ["Trimestre:", "Tous les trimestres (32 Leçons)", "", ""]]
        rows = meta + [["PREMIER TRIMESTRE", "", "", "", "", ""], FIX["french_ipa"]["rows"][1]]
        s = P.parse_rows(rows, "FICHE DE PROGRESSION HARMONISÉE\nCalendrier académique : 2026-27", "x.pdf")
        self.assertEqual((s["subject"], s["class"], s["year"], s["declared_lessons"]), ("mathématiques", "6e", "2026-27", 32))
        self.assertEqual(s["terms"][0]["term"], 1)
        self.assertEqual(v.lessons_of(s)[0]["lesson_no"], 15)


class TitleVariants(unittest.TestCase):
    def test_lesson_prefixes(self):
        en = by_row(parse_fixture("english_title_variants"))
        self.assertEqual((en[44]["lesson_no"], en[44]["title"]), (44, "Reading- read a text about a balanced diet"))
        self.assertEqual((en[70]["lesson_no"], en[70]["title"]), (70, "Vocabulary- homonyms"))
        fr = by_row(parse_fixture("french_ipa"))
        self.assertEqual((fr[15]["lesson_no"], fr[15]["title"]), (15, "Grammaire : Les adjectifs possessifs"))
        ch = by_row(parse_fixture("chemistry_title_variants"))
        self.assertEqual((ch[37]["lesson_no"], ch[37]["title"]), (33, "Reactions of acids and bases"))
        self.assertEqual((ch[9]["lesson_no"], ch[9]["kind"]), (None, "integration"))
        ph = parse_fixture("physics_title_variants")
        self.assertEqual(v.lessons_of(ph)[0]["lesson_no"], 12)
        self.assertIn("typo-lesson-prefix", checks(ph))

    def test_teaching_units_and_activities(self):
        geo = by_row(parse_fixture("geography_tu"))
        self.assertEqual((geo[2]["tu"], geo[2]["lesson_no"]), (2, 2))
        self.assertEqual((geo[13]["kind"], geo[14]["kind"], geo[14]["tu"]), ("practical", "practical", 9))
        self.assertNotIn("tu", geo[13])
        hist = by_row(parse_fixture("history_tu"))
        self.assertEqual((hist[2]["kind"], hist[2]["tu"]), ("further_study", 2))
        self.assertEqual(hist[3]["kind"], "guided_work")
        self.assertEqual(hist[28]["tu"], 26)

    def test_geography_findings(self):
        issues = {(i["check"], tuple(i["rows"])) for i in v.validate(parse_fixture("geography_tu"))}
        self.assertIn(("missing-tu", (13,)), issues)
        self.assertIn(("duplicate-title", (13, 14)), issues)
        self.assertIn(("weekend-date", (12, 13, 14)), issues)  # 06/02/2027 is a Saturday
        # Lesson 2 (Part 1)/(Part 2) is a planned split, not a duplicate
        self.assertFalse([i for i in issues if i[0] in ("duplicate-lesson-no", "near-duplicate-title") and 2 in i[1]])

    def test_chemistry_duplicates(self):
        found = {(i["check"], tuple(i["rows"])) for i in v.validate(parse_fixture("chemistry_title_variants"))}
        self.assertIn(("non-monotonic-lesson-no", (59, 60)), found)
        self.assertIn(("duplicate-lesson-no", (59, 61)), found)


class ModulesAndChapters(unittest.TestCase):
    def test_english_module_split(self):
        rows = by_row(parse_fixture("english_modules"))
        self.assertEqual(rows[21]["module"], "Family life and relationships")
        self.assertEqual(rows[21]["chapter"], "Describing Family Relations, Roles and Behaviours of Family Members")
        self.assertEqual(rows[22]["chapter"], rows[21]["chapter"])
        self.assertEqual((rows[81]["module"], rows[81]["chapter"]), ("People and things around us", "People and things around us"))

    def test_numbered_chapter_without_space(self):
        rows = by_row(parse_fixture("maths_dates"))
        self.assertEqual(rows[49]["chapter"], "Symmetry")
        self.assertEqual(rows[6]["chapter"], "The set of natural numbers and Number bases")


class Ligatures(unittest.TestCase):
    def test_real_english_rows(self):
        words = {"imperatves", "tps", "idiomatc", "writng", "relatonship", "questons", "leter", "requestng", "fnancial"}
        for w in words - {"relatonship"}:
            self.assertTrue(v.dropped_ligature(w), w)
        issue = next(i for i in v.validate(parse_fixture("english_chapter_wrap")) if i["check"] == "dropped-ligatures")
        self.assertEqual(issue["rows"], [45, 47, 48, 50])

    def test_no_false_positives_on_clean_words(self):
        for w in ("understanding", "natural", "properties", "button", "skeleton", "etc", "physics", "movies", "listening"):
            self.assertFalse(v.dropped_ligature(w), w)


# --------------------------------------------------------------------------- validator (synthetic)
def L(seq, no, chapter="Ch A", title="Fractions basics", start="2026-09-07", end="2026-09-11", kind="lesson"):
    return {"seq": seq, "lesson_no": no, "chapter": chapter, "title": title, "start": start, "end": end, "kind": kind,
            "raw": {"seq": seq, "period": f"{start} au {end}", "chapter_cell": chapter, "title": f"Lesson {no}. {title}",
                    "separator": "."}}


def spine(*lessons, terms=None):
    terms = terms or [{"term": 1, "lessons": list(lessons)}, {"term": 2, "lessons": []}, {"term": 3, "lessons": []}]
    return {"subject": "mathematics", "subject_label": "Mathematics", "class": "Form 1", "year": "2026-27",
            "declared_lessons": None, "terms": terms}


class Validator(unittest.TestCase):
    def test_clean_spine_has_no_errors_or_warnings(self):
        sp = spine(L(1, 1), L(2, 2, title="Decimals basics", start="2026-09-14", end="2026-09-18"))
        self.assertEqual([i for i in v.validate(sp) if i["severity"] != "info"], [])

    def test_wrong_year_and_outside_year(self):
        self.assertIn("wrong-year", checks(spine(L(1, 1, start="2025-09-07", end="2025-09-11"))))
        self.assertIn("outside-academic-year", checks(spine(L(1, 1, start="2027-08-02", end="2027-08-06"))))

    def test_overlap_and_backwards_dates_are_info_only(self):
        sp = spine(L(1, 1, chapter="A", start="2026-09-07", end="2026-09-18"),
                   L(2, 2, chapter="B", title="Other thing", start="2026-09-09", end="2026-09-25"),
                   L(3, 3, chapter="B", title="Third thing", start="2026-09-08", end="2026-09-25"))
        sev = {i["check"]: i["severity"] for i in v.validate(sp)}
        self.assertEqual(sev["overlapping-windows"], "info")
        self.assertEqual(sev["dates-go-backwards"], "info")

    def test_chapter_mismatch_is_info_only(self):
        sp = spine(L(1, 1, chapter="Circles", title="Types of angles"))
        found = [i for i in v.validate(sp, {"Circles": ["circle"], "Angles": ["angle"]}) if i["check"] == "chapter-mismatch"]
        self.assertEqual(found[0]["severity"], "info")

    def test_missing_term_header_is_an_error(self):
        sp = spine(terms=[{"term": 1, "lessons": [L(1, 1)]}, {"term": 2, "lessons": []}])
        self.assertIn("term-headers", checks(sp))

    def test_declared_count(self):
        sp = spine(L(1, 1))
        sp["declared_lessons"] = 2
        self.assertIn("lesson-count-mismatch", checks(sp))

    def test_resolved_issues_are_suppressed(self):
        sp = spine(L(1, 1, title="Addition in the set"))
        self.assertIn("truncated-title", checks(sp))
        self.assertNotIn("truncated-title", checks(sp, resolved={("truncated-title", 1)}))

    def test_validator_does_not_mutate(self):
        sp = parse_fixture("english_chapter_wrap")
        before = copy.deepcopy(sp)
        v.validate(sp)
        self.assertEqual(before, sp)


class Breaks(unittest.TestCase):
    def test_labels(self):
        sp = spine(L(1, 1, start="2026-09-07", end="2026-09-11"),
                   L(2, 2, title="b", start="2026-09-17", end="2026-09-18"),   # 3 school days gap: not a break
                   L(3, 3, title="c", start="2026-09-28", end="2026-10-02"),   # 1 week: evaluation
                   L(4, 4, title="d", start="2026-10-19", end="2026-10-23"))   # 2 weeks: holiday
        self.assertEqual([(b["type"], b["start"], b["end"]) for b in build.label_breaks(sp)],
                         [("evaluation", "2026-09-19", "2026-09-27"), ("holiday", "2026-10-03", "2026-10-18")])


# --------------------------------------------------------------------------- overrides
@unittest.skipUnless((RAW / "mathematics.json").exists(), "run tools/spine/build.py first")
class Overrides(unittest.TestCase):
    def setUp(self):
        self.raw = json.loads((RAW / "mathematics.json").read_text(encoding="utf-8"))
        self.ovs = json.loads((ROOT / "data/spine/overrides/mathematics.json").read_text(encoding="utf-8"))["overrides"]

    def test_approved_overrides(self):
        out, resolved = ovr.apply(self.raw, self.ovs)
        ls = v.lessons_of(out)
        self.assertEqual([l["seq"] for l in ls], list(range(1, 70)))
        self.assertEqual((ls[22]["lesson_no"], ls[22]["raw"]["seq"]), (22, 24))
        self.assertEqual(ls[23]["title"], "Multiplication and division in the set ℤ of integers")
        self.assertTrue(ls[36]["title"].endswith("square numbers)"))
        self.assertEqual({o["approved_by"] for o in out["overrides_applied"]}, {"Dion"})
        errors = [i for i in v.validate(out, v.load_rules("mathematics"), resolved) if i["severity"] != "info"]
        self.assertEqual(errors, [])
        self.assertEqual(v.lessons_of(self.raw)[22]["lesson_no"], 23, "raw spine must stay untouched")

    def test_stale_override_fails_loudly(self):
        bad = copy.deepcopy(self.ovs)
        bad[1]["expect"]["title"] = "something else"
        with self.assertRaises(ovr.OverrideError):
            ovr.apply(self.raw, bad)

    def test_override_needs_approval(self):
        bad = copy.deepcopy(self.ovs)
        del bad[0]["approved_by"]
        with self.assertRaises(ovr.OverrideError):
            ovr.apply(self.raw, bad)


class RoundTwoOverrides(unittest.TestCase):
    """New override ops, exercised on real fixture rows."""

    def ov(self, **kw):
        return {"id": "t", "reason": "test", "approved_by": "Dion", **kw}

    def test_delete_keeps_counts_consistent(self):
        sp = parse_fixture("chemistry_title_variants")
        out, _ = ovr.apply(sp, [self.ov(op="delete", seqs=[60, 61])])
        self.assertEqual([l["raw"]["seq"] for l in v.lessons_of(out)], [9, 37, 59])
        self.assertEqual(out["deleted_rows"], [60, 61])
        self.assertFalse({"duplicate-lesson-no", "non-monotonic-lesson-no"} & checks(out))

    def test_split_term(self):
        out, _ = ovr.apply(parse_fixture("english_chapter_wrap"), [self.ov(op="split_term", seq=49, term=3)])
        self.assertEqual([(t["term"], [l["raw"]["seq"] for l in t["lessons"]]) for t in out["terms"]][-2:],
                         [(2, [41, 45, 47, 48]), (3, [49, 50, 51, 52, 53])])

    def test_set_meta_and_rename_chapter(self):
        sp = parse_fixture("geography_tu")
        out, _ = ovr.apply(sp, [
            self.ov(op="set_meta", values={"subject": "geography", "subject_label": "Geography"}),
            self.ov(op="rename_chapter", **{"from": "The Earth: A Planet of the Solar System", "to": "The Earth"})])
        self.assertEqual(out["subject"], "geography")
        self.assertEqual(by_row(out)[3]["chapter"], "The Earth")
        with self.assertRaises(ovr.OverrideError):
            ovr.apply(sp, [self.ov(op="set_meta", values={"class": "Form 2"})])

    def test_replace_words_keeps_case_and_raw(self):
        sp = parse_fixture("english_chapter_wrap")
        out, _ = ovr.apply(sp, [self.ov(op="replace_words", words={"imperatves": "imperatives", "writng": "writing"})])
        rows = by_row(out)
        self.assertEqual(rows[47]["title"], "Grammar- Use imperatives")
        self.assertIn("writing", rows[50]["title"])
        self.assertIn("imperatves", rows[47]["raw"]["title"])
        self.assertEqual(ovr.replace_words("Celebratng Special Days", {"celebratng": "celebrating"})[0],
                         "Celebrating Special Days")
        with self.assertRaises(ovr.OverrideError):  # a word that no longer occurs means the sheet changed
            ovr.apply(sp, [self.ov(op="replace_words", words={"nonexistentword": "x"})])

    def test_ligature_candidates(self):
        known = {"questions", "financial", "letter", "activities", "time", "tips", "define"}
        self.assertEqual(ligatures.candidates("questons", known), ["questions"])  # lost the 'i' after 't'
        self.assertEqual(ligatures.candidates("Activies", known), ["activities"])  # lost the whole 'ti'
        self.assertEqual(ligatures.candidates("fnancial", known), ["financial"])
        self.assertEqual(ligatures.candidates("leter", known), ["letter"])
        self.assertEqual(ligatures.candidates("Defne", known), ["define"])
        self.assertEqual(ligatures.candidates("Behaviours", known), [])


class Assessments(unittest.TestCase):
    def test_biology_rows_assess_the_chapter_they_name(self):
        sp = parse_fixture("biology_assessments")
        build.assign_assesses(sp)
        rows = by_row(sp)
        for r in (22, 23, 24):
            self.assertEqual((rows[r]["chapter"], rows[r]["assesses"]), ("Understanding soil", "Environment and Habitats"))
        self.assertNotIn("assesses", rows[19])  # an ordinary lesson
        found = [i for i in v.validate(sp) if i["check"] == "assesses-other-chapter"]
        self.assertEqual((found[0]["severity"], found[0]["rows"]), ("info", [22, 23, 24]))

    def test_bracket_labels_and_lesson_order(self):
        sp = parse_fixture("home_economics_order")
        build.assign_assesses(sp)
        rows = by_row(sp)
        self.assertEqual(rows[8]["assesses"], "Notion of Health and Nutrition")
        self.assertEqual(rows[9]["assesses"], "Notion of Health and Nutrition")
        self.assertIn(("non-monotonic-lesson-no", (11, 12)), {(i["check"], tuple(i["rows"])) for i in v.validate(sp)})


class CalendarDrift(unittest.TestCase):
    CAL = {"year": "2026-27", "start": "2026-09-07", "end": "TODO",
           "terms": [{"term": 1, "start": "2026-09-07", "end": "TODO"}, {"term": 2, "start": "TODO", "end": "TODO"}],
           "holidays": [{"name": "Christmas", "start": "TODO", "end": "TODO"}], "evaluation_weeks": []}

    def test_drift_is_info_and_todo_is_skipped(self):
        issues = v.validate_calendar(parse_fixture("history_tu"), self.CAL)  # History starts 14/09
        self.assertEqual([(i["check"], i["severity"]) for i in issues], [("calendar-drift", "info")])
        self.assertIn("2026-09-14", issues[0]["problem"])
        self.assertEqual(v.calendar_todos(self.CAL), 6)

    def test_lessons_inside_a_known_holiday(self):
        cal = copy.deepcopy(self.CAL)
        cal["holidays"][0].update(start="2027-04-01", end="2027-05-31")
        found = [i for i in v.validate_calendar(parse_fixture("history_tu"), cal) if "Christmas" in i["problem"]]
        self.assertEqual(found[0]["rows"], [28])

    def test_real_calendar_file(self):
        cal = json.loads((ROOT / "data" / "calendar" / "2026-27.json").read_text(encoding="utf-8"))
        self.assertEqual((cal["start"], cal["terms"][0]["start"]), ("2026-09-07", "2026-09-07"))
        self.assertEqual([t["term"] for t in cal["terms"]], [1, 2, 3])


# --------------------------------------------------------------------------- all real sheets
@unittest.skipUnless(RAW.exists() and any(RAW.glob("*.json")), "run tools/spine/build.py first")
class RealSheets(unittest.TestCase):
    def setUp(self):
        self.spines = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in RAW.glob("*.json")}

    def test_every_sheet_matches_its_declared_count(self):
        pdfs = list(SHEETS.glob("*.pdf"))  # the PDFs stay local; GitHub has the parsed spines only
        self.assertEqual(len(self.spines), len(pdfs) if pdfs else 10)
        for name, sp in self.spines.items():
            self.assertEqual(len(v.lessons_of(sp)), sp["declared_lessons"], name)
            for l in v.lessons_of(sp):
                self.assertTrue(l["chapter"] and l["title"] and l["start"] and l["end"], (name, l["seq"]))

    def test_no_sheet_has_reversed_dates(self):
        # Recorded so a future sheet with reversed dates is noticed: the validator flags it (ReversedDates).
        for name, sp in self.spines.items():
            self.assertFalse([l["seq"] for l in v.lessons_of(sp) if l["end"] < l["start"]], name)

    def test_english_missing_third_term_is_reported(self):
        self.assertIn("term-headers", checks(self.spines["english-language"]))

    def test_round2_overrides_on_real_sheets(self):
        final = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "data" / "spine").glob("*.json")}
        self.assertNotIn("geography-ok", final)
        self.assertEqual((final["geography"]["subject"], final["geography"]["subject_label"]), ("geography", "Geography"))
        self.assertEqual([len(t["lessons"]) for t in final["english-language"]["terms"]], [32, 44, 28])
        self.assertEqual(final["english-language"]["terms"][2]["lessons"][0]["raw"]["seq"], 77)
        self.assertEqual(len(v.lessons_of(final["chemistry"])), 60)
        shown = json.dumps({k: [(l["title"], l["chapter"]) for l in v.lessons_of(sp)] for k, sp in final.items()})
        for typo in ("questons", "fnancial", "garderning", "Eygpt", "Arica", "Compenents", "Commnicating", "mordern"):
            self.assertNotIn(typo, shown)
        self.assertIn("questons", json.dumps(self.spines["english-language"]), "raw spine must stay untouched")


if __name__ == "__main__":
    unittest.main()
