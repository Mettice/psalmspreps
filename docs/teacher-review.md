# Teacher review log

Everything in the app that a teacher should confirm: conventions, authored facts (answers fixed by a
person, not computed by code), and judgment calls (decisions made while building that nobody has
approved yet). Each item has an ID to quote, a location, and a checkbox.

**Priorities:** every item is tagged [P1] wrong maths or facts would mislead the pupil, [P2] conventions and wording, [P3] cosmetic.

**How to use:** tick `[x]` to approve, or write a correction under the item. This file is append-only:
new items are added at the end of the right section with the date, and nothing is deleted. A changed
decision gets a new item that refers to the old ID.

Context (2026-10-02): the pupil has missed most of this term, so the app is his main
teacher, not revision. No exercise-book check is possible; teachers review later.

Related files: `content/maths/AUTHORED.md` (every authored question, all variants, with sources),
`content/maths/REVIEW.md` (every draft rendered), `content/maths/sources.json`.

## P1 summary: check these first

P1 = wrong maths or facts here would mislead the pupil. P2 = conventions and wording. P3 = cosmetic.
24 P1 items: 22 open, 2 closed.

| Item | What to check | Status |
|---|---|---|
| TR-A02 | Orthogonal = perpendicular in a plane | open |
| TR-A04 | ℕ contains 0; ℕ* does not | open |
| TR-A07 | Ordinal endings | open |
| TR-A08 | Roman numerals | open |
| TR-A13 | Length units ladder | open |
| TR-B01 | Lesson 1 note, history of numbers | open |
| TR-B02 | Egyptian numerals had no zero | open |
| TR-B03 | The 60-minute hour comes from Babylonian base 60 | open |
| TR-B04 | Lesson 2 note | open |
| TR-B05 | Through two different points there is exactly one straight line; any two points are collinear; three need not be | open |
| TR-B06 | Midpoint and its converse | open |
| TR-B07 | Perpendicular bisector | open |
| TR-B08 | Lines in a plane | open |
| TR-B09 | Cardinal / ordinal / nominal definitions and the example sentences | open |
| TR-B10 | All 19 authored questions | open |
| TR-C11 | Which mistakes count as "predictable" | open |
| TR-C12 | Teach cards | open |
| TR-C23 | Typed answers | open |
| TR-C26 | Full working for every question | open |
| TR-C29 | Lesson 3 hints (draft) | open |
| TR-C31 | Borrowing wording in base subtraction working | open |
| TR-C33 | Typed answers for whole numbers | open |
| TR-D01 | "Egyptian rewording (as previously instructed)" | closed |
| TR-D02 | "Base-60 source (as previously instructed)" | closed |

---

## A. Conventions (pending review)

- [ ] **TR-A01 [P2] Half-line notation.** (AB) is a line, [AB) a half line starting at A through B, [AB] a segment, AB its length. Instructed as pending review on 2026-10-02. *Location:* `content/maths/11.json` (note, cards c11-1 to c11-3, m11-*), `12.json`, `14.json`, `15.json`; source `line-notation` in `content/maths/sources.json`.
- [ ] **TR-A02 [P1] Orthogonal = perpendicular in a plane.** Instructed as pending review on 2026-10-02. *Location:* `content/maths/16.json` (note, with `review` flag; card c16-2 and its check `c16-2-check`).
- [ ] **TR-A03 [P2] Number style.** 4-digit numbers not grouped (7750, 1948); 5+ digits grouped with a space (12 500 FCFA); decimal point, not comma. Set by Dion 2026-10-02; enforced by tests. *Location:* `fmt()` in `src/engine/lib/maths.js`; tests in `tests-js/content.test.js`.
- [ ] **TR-A04 [P1] ℕ contains 0; ℕ* does not.** Symbols ∈ and ∉. *Location:* `content/maths/5.json` (note, cards c5-1 to c5-3).
- [ ] **TR-A05 [P3] Set notation with commas:** ℕ = {0, 1, 2, 3, …}. (French-medium books often use semicolons.) *Location:* `content/maths/5.json`.
- [ ] **TR-A06 [P2] Numbers in words, British style:** "and" after hundred (three hundred and five; three thousand and five), hyphens from twenty-one to ninety-nine, no commas between groups. *Location:* `words()` in `src/engine/lib/maths.js`; `content/maths/4.json`.
- [ ] **TR-A07 [P1] Ordinal endings:** 1st, 2nd, 3rd, 4th; numbers ending in 11, 12, 13 take th (111th). *Location:* `ordinal()` in `src/engine/lib/maths.js`; `content/maths/6.json`.
- [ ] **TR-A08 [P1] Roman numerals:** only the standard form is accepted (IV not IIII), largest 3999, six subtractive pairs IV IX XL XC CD CM. *Location:* `roman()`, `fromRoman()` in `src/engine/lib/maths.js`; `content/maths/2.json`.
- [ ] **TR-A09 [P2] Egyptian symbol names:** stroke (1), heel bone (10), coil of rope (100), lotus flower (1000). Pictures are described in words, not drawn. *Location:* `egyptianList()` in `src/engine/lib/maths.js`; `content/maths/2.json`.
- [ ] **TR-A10 [P2] Base notation:** subscript base (1101₂); "base ten" written in words; remainders written "r" in division lines. *Location:* `content/maths/8.json`, `9.json`, `10.json`.
- [ ] **TR-A11 [P2] Order of operations is called BODMAS** (Brackets, Orders, Division and Multiplication, Addition and Subtraction). *Location:* `content/maths/7.json`.
- [ ] **TR-A12 [P2] Power vocabulary:** base, exponent (index), squared, cubed. *Location:* `content/maths/7.json`.
- [ ] **TR-A13 [P1] Length units ladder:** km hm dam m dm cm mm, each ten times the next. *Location:* `content/maths/13.json`.
- [ ] **TR-A14 [P2] Line symbols:** // parallel, ⊥ perpendicular. *Location:* `content/maths/16.json`.
- [ ] **TR-A15 [P3] Currency written after the amount:** 12 500 FCFA. *Location:* lessons 0, 3, 7.
- [ ] **TR-A16 [P3] Cameroonian English and local context:** British spellings (metre, organising); names (Ngwa, Enow, Ayuk, Bih, Tabe, Ewane, Mih, Ndi, Ashu, Ebai, Fon, Mbah, Mami Nkeng); places (Bamenda Main Market, Limbe market, Mile Two taxi park). No real distances between real towns are used. *Location:* all lessons.

## B. Authored facts (answers fixed by a person)

- [ ] **TR-B01 [P1] Lesson 1 note, history of numbers:** counting with stones; tally marks grouped in fives; Egyptians wrote numbers with pictures (lotus = 1000); Babylonians counted in sixties, which is why an hour has 60 minutes; Romans used letters; our digits came from India and were carried by Arab traders and scholars; India gave us zero as a number. *Location:* `content/maths/1.json` note; sources `hindu-arabic`, `babylonian`, `egyptian`.
- [ ] **TR-B02 [P1] Egyptian numerals had no zero.** This is my inference from their additive system, not a quoted source. *Location:* `m1-zero-symbol` feedback in `content/maths/1.json`; source `egyptian`. See open item TR-D01.
  - Superseded 2026-10-03 by Dion's wording (TR-D01): no longer an inference to check.
- [ ] **TR-B03 [P1] The 60-minute hour comes from Babylonian base 60.** Seen only in Britannica search summaries; the exact article was not confirmed. *Location:* `content/maths/1.json` (note, `m1-sixty`); source `babylonian`. See open item TR-D02.
  - Source question settled 2026-10-03 (TR-D02); the fact itself still awaits teacher sign-off.
- [ ] **TR-B04 [P1] Lesson 2 note:** Egyptian symbol values; the Roman rules (add when equal or smaller follows, subtract the six pairs, never four of the same letter in a row). *Location:* `content/maths/2.json`, cards c2-1 to c2-4.
- [ ] **TR-B05 [P1] Through two different points there is exactly one straight line; any two points are collinear; three need not be.** *Location:* `content/maths/11.json`, `12.json` (m12-facts, cards c12-1, c12-2).
- [ ] **TR-B06 [P1] Midpoint and its converse:** M is the midpoint only if M is on [AB] AND AM = MB. *Location:* `content/maths/14.json` (note, m14-converse, card c14-3).
- [ ] **TR-B07 [P1] Perpendicular bisector:** passes through the midpoint at a right angle, not through A; every point on it is the same distance from A and B (and the converse); construction steps in order: opening more than half of AB, arcs from A, same opening arcs from B, join the crossing points. *Location:* `content/maths/15.json` (note, m15-steps, m15-spot, cards c15-1 to c15-3).
- [ ] **TR-B08 [P1] Lines in a plane:** exactly one parallel and one perpendicular through a point not on a line; two lines perpendicular to the same line are parallel; a line perpendicular to one of two parallel lines is perpendicular to the other; parallel is transitive. *Location:* `content/maths/16.json`; rule table `lineRule()` in `src/engine/lib/maths.js`.
- [ ] **TR-B09 [P1] Cardinal / ordinal / nominal definitions and the example sentences** (a taxi number and a shirt number are nominal; "Today is the 17th day" is ordinal). *Location:* `content/maths/6.json` (note, m6-classify, card c6-1 and its check).
- [ ] **TR-B10 [P1] All 19 authored questions** (14 practice templates and 5 card checks), each with every variant, answer, feedback and sources. *Location:* `content/maths/AUTHORED.md`. Tick here when that file has been reviewed item by item.

## C. Judgment calls (made while building, not yet approved)

### Curriculum spine (Phase 1)
- [ ] **TR-C01 [P2] Watermark removal:** characters of 15 pt or more are dropped as the diagonal watermark. *Location:* `WATERMARK_MIN_SIZE` in `tools/spine/parse_sheets.py`.
- [ ] **TR-C02 [P2] Wrapped chapter text:** a chapter cell is merged into the previous chapter only if it is in the same date window and term and either the previous text ends in a joining word or the sheet marks every chapter (Chap / RLS / I.) and the fragment is short. *Location:* `looks_like_wrap()` in `tools/spine/parse_sheets.py`.
- [ ] **TR-C03 [P2] Lesson kinds** (lesson, integration, evaluation, remediation, catch-up, practical, further study, guided work, group work) are recognised from title words. *Location:* `KINDS` in `tools/spine/parse_sheets.py`.
- [ ] **TR-C04 [P2] English modules:** "Chap N" cells are modules and "RLS:" cells are the chapters inside them. *Location:* `split_module()` in `tools/spine/parse_sheets.py`.
- [ ] **TR-C05 [P2] `assesses` matching:** an assessment row is linked to the chapter that shares the most word stems with its label; with no label, to its own chapter. *Location:* `assign_assesses()` in `tools/spine/build.py`.
- [ ] **TR-C06 [P2] Break labels:** a gap with 4 or more missing school days counts as a week; 2+ weeks = holiday, 1 week = evaluation. *Location:* `label_breaks()` in `tools/spine/build.py`.
- [ ] **TR-C07 [P2] Ligature repairs** use a US-English dictionary (pyspellchecker); British spellings it does not know are left alone. *Location:* `tools/spine/ligatures.py`; override `english-language-ligatures`.
- [ ] **TR-C08 [P3] Extra typo fixes** beyond those named by Dion (e.g. Gramar, Aquaintainces, gklobal, liesure, etiquetes, atouristic, aninvitaton, waarming, warmig, questioon, progrss, mordern, shadaw, activitities). *Location:* `*-typos` overrides in `data/spine/overrides/`.

### Teaching content (Phases 2 and 3)
- [ ] **TR-C09 [P2] Prerequisites between lessons.** *Location:* `prerequisites` in each `content/maths/{n}.json`.
- [ ] **TR-C10 [P2] Question levels:** 1 = recall, 2 = apply, 3 = problem or spot the error; which question gets which level. *Location:* `level` on every template.
- [ ] **TR-C11 [P1] Which mistakes count as "predictable"** and get their own explanation (misconceptions), and the wording of each explanation. *Location:* `misconceptions` on every template; listed per question in `content/maths/REVIEW.md`.
- [ ] **TR-C12 [P1] Teach cards:** the choice of 3–4 ideas per lesson, their order, and their examples. 50 cards in total. *Location:* `teach.cards` in `content/maths/1.json` to `16.json`.
- [ ] **TR-C13 [P3] Card checks reuse practice questions.** 26 of the 50 cards use a level-1 practice template as their check, so the pupil meets that question type again in practice. *Location:* cards with `"check": {"ref": …}`.
- [ ] **TR-C14 [P2] A wrong card answer gets one retry, then the lesson moves on** (the card is marked "needs review" in the results). Instructed: re-show the example and give a fresh variant; the "only once" limit is my choice. *Location:* `answerCard()` in `src/engine/teach.js`.
  - Replaced 2026-10-03 by Dion's rule (TR-C28): after a second miss the app shows the answer with full working before moving on.
- [ ] **TR-C15 [P3] Fresh variants of fixed questions.** For questions with no random part (e.g. `m1-digits-origin`, `c15-1-check`), the retry is the same question with the options in a new order. *Location:* `cardQuestion()` in `src/engine/teach.js`.
- [ ] **TR-C16 [P2] Practice order:** in teach mode, practice is one question from each template, easiest first. The full session rules (2 correct in a row to level up, etc.) are Phase 3. *Location:* `practicePlan()` in `src/engine/teach.js`.
- [ ] **TR-C17 [P2] Readiness check design:** 13 questions (limit 15) in four areas; question ranges (4-digit addition and subtraction, 3-digit × 2-digit, 3-digit quotients, tables to 12 × 12, three word problems). *Location:* `content/maths/0.json`.
- [ ] **TR-C18 [P2] Weak foundation rule:** an area is weak when fewer than two thirds of its questions are right. *Location:* `weak_if_below` in `content/maths/0.json`; `scoreReadiness()` in `src/engine/readiness.js`.
- [x] **TR-C19 [P2] No right/wrong shown during the readiness check;** results appear at the end. *Location:* `readinessQ()` in `tools/prototype/app.js`.
  - **Approved by Dion 2026-10-03.** Extended: the readiness check now ends on a neutral "Let's start" screen; scores and weak areas appear only in "Copy results" (TR-C30).
- [ ] **TR-C20 [P2] Hints exist only for Lesson 8 and two card checks (c8-2, c8-3).** Elsewhere "I don't know" shows the worked example alone. *Location:* `hint` fields.
  - Updated 2026-10-03: Lesson 3 now has hints too (TR-C29).
- [ ] **TR-C21 [P2] After a wrong practice answer the app shows the right answer** plus the explanation for the mistake. After "I don't know" it shows no answer, only the hint and the worked example. *Location:* `feedback()` in `tools/prototype/app.js`.
  - Superseded 2026-10-03 by TR-C27: the answer is now shown only after a second miss.
- [ ] **TR-C22 [P2] Lesson 7 skills:** "operations" (four operations, BODMAS, properties) and "powers". The spot-the-error question `m7-spot` mixes both and is filed under powers. *Location:* `content/maths/7.json`.
- [ ] **TR-C23 [P1] Typed answers:** "12 500", "12500" and "12,500" all mean twelve thousand five hundred; "2,5" means two and a half. *Location:* `parseNumber()` in `src/engine/template.js`.
- [ ] **TR-C24 [P3] Feedback tone,** e.g. "That's fine. Let's look at it together." after "I don't know". *Location:* `tools/prototype/app.js`.
- [ ] **TR-C25 [P3] Prototype draws new numbers each time the page opens** (no fixed seed), so two runs are never identical. *Location:* `SEED` in `tools/prototype/app.js`.

### Added 2026-10-03 (Round 5)
- [ ] **TR-C26 [P1] Full working for every question,** shown after a second miss: 79 written solutions (every numeric and multiple-choice template, practice and card checks) plus working built automatically for true/false, spot-the-error and ordering questions. Long working (base conversion, column arithmetic, Roman numerals) comes from helper functions. Tests check that the working contains no typed numbers and always shows the computed answer, across 1000 variants per question. *Location:* `solution` on each template; `solutionOf()` in `src/engine/template.js`; `divSteps`, `placeSum`, `columnAdd`, `columnSub`, `columnMul`, `romanWorking`, `expanded` in `src/engine/lib/maths.js`; every working rendered in `content/maths/REVIEW.md`.
- [ ] **TR-C27 [P2] First miss on a practice question:** "Not quite" plus the explanation for that mistake, without the answer, then a new question. (Cards: the same, plus the card's example again.) *Location:* `retry()` in `tools/prototype/app.js`.
- [ ] **TR-C28 [P2] Second miss (wrong or "I don't know") on any card or practice question:** show the correct answer with full working, then move on and mark the item "needs review". Instructed by Dion 2026-10-03. *Location:* `answerItem()` in `src/engine/teach.js`; `reveal()` in `tools/prototype/app.js`; `docs/phase3-spec.md` §3.
- [ ] **TR-C29 [P1] Lesson 3 hints (draft),** 7 of them, and Lesson 8 hints reworded so they contain no typed numbers. *Location:* `hint` on m3-* templates and `c3-3-check` in `content/maths/3.json`; `m8-to-base`, `m8-valid-digits`, `m8-to-ten`, `c8-2-check` in `8.json`.
- [ ] **TR-C30 [P2] Readiness ending:** the pupil sees "Thank you · Let's start" and no score; the score and weak areas go only into "Copy results", labelled "not shown to the pupil". *Location:* `readinessDone()` and `resultsText()` in `tools/prototype/app.js`.
- [ ] **TR-C31 [P1] Borrowing wording in base subtraction working,** including borrowing across a zero: "0 − 1 (lent) is less than 0, so borrow 4: 0 + 4 − 1 − 0 = 3". *Location:* `columnSub()` in `src/engine/lib/maths.js`.
  - **Reworded 2026-10-03 (Dion):** every borrowing case is now written as plain steps with no negative intermediates. Across a zero: "This 0 already lent 1 to the right and has nothing left, so it borrows from the next column. In base 4, borrowing gives 4. 4 − 1 (what it lent) = 3. Then 3 − 0 = 3." Other cases: "2 is less than 3, so it borrows from the next column. In base 5, borrowing gives 5 more: 2 + 5 = 7. Then 7 − 3 = 4." and "This 4 lent 1 to the right: 4 − 1 = 3. Then 3 − 1 = 2." Tested on 20 000 random subtractions in bases 2–9: no negative number appears, every step's arithmetic is right, every column result is a digit of the base. Still P1 and open, pending teacher review. Note for the reviewer: intermediate values such as "2 + 5 = 7" are counts in base ten, as in the Lesson 9 note.
- [ ] **TR-C32 [P3] Results wording:** "needs review" items are listed by card or template id in "Copy results". *Location:* `resultsText()` in `tools/prototype/app.js`.

### Added 2026-10-03 (UI polish before the pupil test)
- [ ] **TR-C33 [P1] Typed answers for whole numbers:** spaces, thin spaces, non-breaking spaces and commas are stripped before checking, so "9038766", "9 038 766" and "9,038,766" are all accepted (tested). For decimal answers commas are kept, so "2,5" still means two and a half (TR-C23). *Location:* `normaliseInput()` in `src/engine/template.js`; test in `tests-js/engine.test.js`.
- [ ] **TR-C34 [P3] Keyboard:** the number pad (inputmode "numeric") for whole-number and base answers; the decimal pad for decimal answers. *Location:* `inputModeFor()` in `src/engine/template.js`.
- [ ] **TR-C35 [P3] Feedback motion and wording (teach mode only):** green flash and a drawn check icon with "Correct!"; a small shake on a wrong answer; no shake after "I don't know" (it is not a wrong answer); the readiness check shows no right/wrong cues at all (tested). All motion is switched off under the phone's "reduce motion" setting. *Location:* `tools/prototype/app.js`; CSS in `tools/prototype/build.mjs`.
- [ ] **TR-C36 [P2] End screen:** confetti, "Lesson 3 done" and "You completed 9 questions" (cards plus practice items, not the score). The results text, which holds the readiness score and weak areas, is folded under "Show the text (for a grown-up)". It opens by itself only if the phone refuses the normal copy and the fallback needs it. *Location:* `results()` in `tools/prototype/app.js`.
- [ ] **TR-C37 [P3] Progress bar:** counts every screen of the lesson (cards, worked example, practice questions, summary), e.g. "5 / 13"; during readiness it counts the 13 questions. *Location:* `progress()` in `tools/prototype/app.js`.

## D. Open items (need an answer before approval)

- [x] **TR-D01 [P1] "Egyptian rewording (as previously instructed)".** I have no earlier instruction about rewording the Egyptian content in this project's history. Current wording is unchanged: "Egyptian numerals had no zero: an empty place was simply left out." Please restate the rewording you want. *Location:* `m1-zero-symbol` in `content/maths/1.json`; source `egyptian`.
  - **Closed 2026-10-03 (Dion):** wording is now "Egyptian numerals had no place value, so they did not need a zero digit to hold empty places." Applied in `m1-zero-symbol` (feedback and full working), `m2-egyptian` feedback, the Lesson 2 note, source `egyptian`, and `content/maths/AUTHORED.md`.
- [x] **TR-D02 [P1] "Base-60 source (as previously instructed)".** Same: no earlier instruction found. Current source is Britannica "Cuneiform numeral", checked only through search summaries. Please restate which source to use. *Location:* `babylonian` in `content/maths/sources.json`.
  - **Closed 2026-10-03 (Dion):** the 60-minute hour comes from the Babylonian base-60 (sexagesimal) system; any reliable history-of-mathematics source is acceptable. Source `babylonian` updated accordingly.
- [ ] **TR-D03 [P2] School calendar dates.** 22 dates are still TODO. *Location:* `data/calendar/2026-27.json`.
