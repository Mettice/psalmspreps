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
`content/maths/REVIEW.md` (every draft rendered), `content/maths/sources.json`. English: `content/english/AUTHORED.md`,
`content/english/REVIEW.md`, `content/english/sources.json`. Physics: `content/physics/AUTHORED.md`,
`content/physics/REVIEW.md` (with drawings in `content/physics/figures/`), `content/physics/sources.json`. Chemistry: `content/chemistry/AUTHORED.md`,
`content/chemistry/REVIEW.md`, `content/chemistry/sources.json`.

## P1 summary: check these first

P1 = wrong maths or facts here would mislead the pupil. P2 = conventions and wording. P3 = cosmetic.
74 P1 items: 72 open, 2 closed (Maths 25, English 18, Physics 18, Chemistry 13). A printable Maths list for teachers: `docs/teacher-review-maths-P1.md`.

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
| TR-C41 | Lessons 1, 2 and 4–16 are in front of the pupil with P1 items still open | open |
| TR-E01 | Irregular verb table (63 verbs): simple past and past participle | open |
| TR-E02 | Spelling of the he/she/it form (-s, -es, -ies, has) | open |
| TR-E03 | Spelling of -ing and -ed, including when to double the last letter (British: travelled) | open |
| TR-E04 | a / an by sound, and its exception lists | open |
| TR-E05 | Plurals and the irregular plural list | open |
| TR-E06 | Countable and uncountable nouns; units (a loaf of bread, a bar of soap) | open |
| TR-E07 | How each compound word is written (one word or two) | open |
| TR-E08 | Conversion sentences: is the word a noun or a verb? | open |
| TR-E09 | Reading texts and their keys (account, notices, timetables) | open |
| TR-E10 | Every statement in the spot-the-error and true-sentence questions | open |
| TR-E11 | English notes (13) and teach cards (45) | open |
| TR-E12 | Number words, ordinal words and the misspelling lists | open |
| TR-E13 | Greetings and introductions: which reply fits | open |
| TR-E14 | Means of transport: road/water/rail/air; by bus, on foot | open |
| TR-E15 | Present Perfect: not with a finished time; ever, never, already, yet | open |
| TR-E16 | Simple Present vs Present continuous: the time words | open |
| TR-E17 | Forms and invitations: dd/mm/yyyy, BLOCK LETTERS, the model answers | open |
| TR-E18 | Typed English answers: what the app accepts as right | open |
| TR-P02 | Scientists, discoveries and dates | open |
| TR-P03 | g = 10 N/kg on Earth; about 1.6 N/kg on the Moon | open |
| TR-P04 | T(K) = T(°C) + 273; fixed points | open |
| TR-P05 | Unit ladders and conversions | open |
| TR-P06 | Density facts and values | open |
| TR-P07 | Names of the changes of state; examples | open |
| TR-P08 | How the drawn ruler, cylinder and thermometer are read | open |
| TR-P09 | Branches of science and of physics | open |
| TR-P10 | The scientific method; fair test | open |
| TR-P11 | Equipment and what it measures | open |
| TR-P12 | Laboratory safety | open |
| TR-P13 | SI units, symbols, prefixes | open |
| TR-P14 | States of matter | open |
| TR-P15 | Mass and weight | open |
| TR-P16 | Hazard symbols and product labels | open |
| TR-P17 | Physics statement pools | open |
| TR-P18 | Physics notes (19) and teach cards (58) | open |
| TR-P19 | Typed Physics answers | open |
| TR-K02 | Element table, symbols, spellings, Latin names | open |
| TR-K03 | Formulas and atom counts | open |
| TR-K04 | Branches of chemistry | open |
| TR-K05 | Laboratory equipment and uses | open |
| TR-K06 | Hazard symbols and reagents | open |
| TR-K07 | Chemistry laboratory safety | open |
| TR-K08 | Physical and chemical changes | open |
| TR-K09 | States of matter and kinetic theory | open |
| TR-K10 | Pure substances, mixtures, solutions | open |
| TR-K11 | Separation methods and steps | open |
| TR-K12 | Gases in liquids; composition of air | open |
| TR-K13 | Mixtures and compounds compared | open |
| TR-K14 | Chemistry statement pools, notes (21) and cards (63) | open |
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

### Added 2026-10-05 (all 16 lessons in the app, after the Lesson 3 test went well)
- [ ] **TR-C38 [P2] Saved progress (this phone and browser only):** the readiness check runs once; after that the app opens on the lesson menu. A lesson left part-way carries on where it stopped: a question left after a first miss comes back as a fresh variant; after a second miss, at the next step. Finishing a lesson again replaces its earlier results. "Clear all progress on this phone" (behind "For a grown-up", with a confirmation) starts again. Nothing is sent anywhere. *Location:* `load()`, `save()`, `openLesson()`, `resumable()` in `tools/prototype/app.js`.
- [ ] **TR-C39 [P2] Lesson menu:** Lessons 1–16 in sheet order, a tick when done, "Started · tap to carry on" for the one in progress; the big button suggests the first lesson not yet done. No lesson is locked behind its prerequisites. One line says the lessons are drafts that a teacher has not checked. *Location:* `menu()` in `tools/prototype/app.js`.
- [ ] **TR-C40 [P3] Lesson titles tidied for display only,** e.g. "Number bases :Convert" → "Number bases: Convert", "Line segment.- Midpoint" → "Line segment: Midpoint". The spine keeps the sheet's text. *Location:* `tidy()` in `tools/prototype/build.mjs`.
- [ ] **TR-C41 [P1] Lessons 1, 2 and 4–16 are now in front of the pupil** while their P1 items (see the summary above) are still open. *Location:* `content/maths/*.json`.

## D. Open items (need an answer before approval)

- [x] **TR-D01 [P1] "Egyptian rewording (as previously instructed)".** I have no earlier instruction about rewording the Egyptian content in this project's history. Current wording is unchanged: "Egyptian numerals had no zero: an empty place was simply left out." Please restate the rewording you want. *Location:* `m1-zero-symbol` in `content/maths/1.json`; source `egyptian`.
  - **Closed 2026-10-03 (Dion):** wording is now "Egyptian numerals had no place value, so they did not need a zero digit to hold empty places." Applied in `m1-zero-symbol` (feedback and full working), `m2-egyptian` feedback, the Lesson 2 note, source `egyptian`, and `content/maths/AUTHORED.md`.
- [x] **TR-D02 [P1] "Base-60 source (as previously instructed)".** Same: no earlier instruction found. Current source is Britannica "Cuneiform numeral", checked only through search summaries. Please restate which source to use. *Location:* `babylonian` in `content/maths/sources.json`.
  - **Closed 2026-10-03 (Dion):** the 60-minute hour comes from the Babylonian base-60 (sexagesimal) system; any reliable history-of-mathematics source is acceptable. Source `babylonian` updated accordingly.
- [ ] **TR-D03 [P2] School calendar dates.** 22 dates are still TODO. *Location:* `data/calendar/2026-27.json`.

## E. English Form 1, Batch E1 (Lessons 1–16), added 2026-10-06

Lessons 1–3, 5–7, 10, 11 and 13–15 are taught with auto-marked practice; Lessons 9 and 16 (Writing) are paper tasks;
Lessons 4, 8 and 12 (Speech Work) are deferred. 13 notes, 45 teach cards, 61 practice templates and 19 card-check
templates: 41 have an **authored key** (a person fixed the answer) and 39 are **computed by rule** (code applies a
spelling or grammar rule to an authored word table). Everything is draft. Every authored key, word table and statement
is printed in `content/english/AUTHORED.md`; every question as the pupil sees it is in `content/english/REVIEW.md`.

### P1: wrong facts here would mislead the pupil
- [ ] **TR-E01 [P1] Irregular verb table:** 63 verbs with their simple past and past participle, British forms (got, not gotten). "be" has "was/were". *Location:* `IRREGULAR` in `src/engine/lib/english.js`; listed in `content/english/AUTHORED.md` Part 1.
- [ ] **TR-E02 [P1] The he/she/it form:** -es after s, sh, ch, x, z and o (washes, goes); consonant + y → -ies (carries; but plays); have → has. Tested on known answers. *Location:* `thirdPerson()` in `src/engine/lib/english.js`; `tests-js/english.test.js`.
- [ ] **TR-E03 [P1] -ing and -ed spelling:** drop a final e (making; but seeing, being); ie → y (lying); double the last consonant after one short vowel in one-syllable verbs (running, stopped); the two-syllable list (begin, forget, prefer, …); British doubling of a final l (travelled, cancelled); never doubled: visit, open, listen, happen, enter, answer, offer, order, wonder, remember, cover, suffer. *Location:* `ing()`, `regularPast()`, `doublesFinal()` in `src/engine/lib/english.js`.
- [ ] **TR-E04 [P1] a / an by sound:** an hour, an honest man; a uniform, a university, a European, a one-way street. *Location:* `article()` in `src/engine/lib/english.js`; Lesson 10 card c10-2.
- [ ] **TR-E05 [P1] Plurals:** -es after s, sh, ch, x, z and for tomato, potato, mango, hero, echo; -ies; the irregular list (children, men, women, feet, teeth, mice, people, knives, wives, leaves, loaves, lives, shelves, halves, sheep, fish). *Location:* `plural()`, `IRREGULAR_PLURAL` in `src/engine/lib/english.js`.
- [ ] **TR-E06 [P1] Countable and uncountable nouns:** countable: orange, egg, bucket, mango, plantain, pencil, chair, goat, bag, tomato, banana, bottle; uncountable: rice, water, salt, oil, sugar, sand, money, bread, milk, flour, garri, advice. Units: a loaf of bread, a bar of soap, a bottle of oil, a bucket of water, a packet of salt, a bag of rice. *Location:* `content/english/10.json`.
- [ ] **TR-E07 [P1] Written form of compounds:** one word: football, airport, railway, motorbike, classroom, toothbrush, blackboard, roundabout, footpath; two words: bus stop, car park, road sign, taxi driver, traffic light. The matching question uses only halves that cannot be joined another way (air–port, class–room, black–board, round–about, motor–bike). "Seat belt" appears only in a correct sentence, never as a question (dictionaries also show "seatbelt"). *Location:* `content/english/14.json`.
- [ ] **TR-E08 [P1] Conversion (noun or verb):** the 14 sentences in `e14-class` and the 6 pairs in `e14-convert`. *Location:* `content/english/14.json`.
- [ ] **TR-E09 [P1] Reading texts and keys:** the account of the compound clean-up and its true/false statements; the notice generator (event, day, time, place, what to bring) and its four questions; the timetable questions (which lesson at a time, which lesson comes next). All texts are original. *Location:* `content/english/5.json`.
- [ ] **TR-E10 [P1] Statement pools:** every correct and wrong sentence in the spot-the-error and "which is true" questions (Lessons 1, 2, 3, 5, 7, 10, 11, 13, 14, 15), with the explanation shown for each wrong one. *Location:* `content/english/AUTHORED.md` Part 2.
- [ ] **TR-E11 [P1] Notes and teach cards:** 13 notes (each at most 150 words) and 45 cards: the choice of ideas, their order and their examples. Grammar terms are the sheet's: Simple Present tense (affirmative, negative and interrogative), Present continuous tense, Simple Past tense, Present Perfect tense, countable and uncountable nouns, conversion and compounding, irregular verbs. *Location:* `note` and `teach.cards` in `content/english/*.json`; rendered in `content/english/REVIEW.md`.
- [ ] **TR-E12 [P1] Number words:** British style as in Maths TR-A06 (and after hundred, hyphens 21–99); typed answers must have the hyphen; "a hundred" is accepted for "one hundred". Ordinal words (first, second, third, fifth, eighth, ninth, twelfth, twentieth, twenty-first). The misspelling lists in `e2-spelling`, `e2-correct`, `c6-1-check` and `e6-spelling`. *Location:* `content/english/2.json`, `6.json`; `ordinalWords()` in `src/engine/lib/english.js`.
- [ ] **TR-E13 [P1] Greetings and introductions:** Good morning before midday; Good afternoon after midday until about five or six o'clock; Good evening; "Good night" is for leaving, not greeting; the six question-and-reply pairs in `e1-reply`; with an older person or a teacher, greet first, add sir or madam, and prefer "Good morning" to "Hi". *Location:* `content/english/1.json`.
- [ ] **TR-E14 [P1] Means of transport:** road (taxi, bus, motorbike, lorry, bicycle, car), water (canoe, boat, ship, ferry), rail (train), air (plane, helicopter); by + transport with no article (by train, not by the train); on foot (not by foot); the four journey questions (How, How long, How much, Where). *Location:* `content/english/13.json`.
- [ ] **TR-E15 [P1] Present Perfect:** have/has + past participle; not with a finished time (yesterday, last week, two days ago, last Saturday); "already" may end the sentence (British); the four ever/never/already/yet sentences in `c15-3-check` and the two wrong choices given for each. *Location:* `content/english/15.json`.
- [ ] **TR-E16 [P1] Simple Present or Present continuous:** "every day", "every evening" and "on Saturdays" → Simple Present; "now" and "at the moment" → Present continuous. *Location:* `e7-which`, `c7-4-check` in `content/english/7.json`.
- [ ] **TR-E17 [P1] Forms and invitations:** dates as dd/mm/yyyy (British order); "BLOCK LETTERS" means capitals; an invitation tells who, what, when, where and how to reply; the model answers of both paper tasks (Lesson 9 shopping list, Lesson 16 form and invitation). *Location:* `content/english/9.json`, `16.json`.
- [ ] **TR-E18 [P1] What counts as a right typed answer:** case and extra spaces are ignored ("GOES" and " goes " are right); curly and straight apostrophes are the same; spaces inside an answer still matter ("busstop" is wrong for "bus stop"); "do not / does not / did not" are accepted for "don't / doesn't / didn't"; prices may be typed 1500, 1 500 or 1,500. Contractions such as "Bih's eaten" are not offered. *Location:* `normaliseText()` and cloze checking in `src/engine/template.js`; `accept` lists in `content/english/*.json`.

### P2: conventions and decisions
- [ ] **TR-E19 [P2] Prices** in Lesson 9 (rice 700 FCFA a kilo, soap 300 FCFA a bar, salt 150 FCFA a packet, palm oil 1200 FCFA a litre, beans 900 FCFA a kilo, sugar 850 FCFA a kilo) are invented illustrations for a town market, not data. *Location:* `content/english/9.json`.
- [ ] **TR-E20 [P2] Lesson 16 is a paper task.** The sheet calls it "Writing- Fill out simple forms, e.g. an invitation letter"; the audit had planned fill-in-the-form questions. Following the rule "Writing lessons → paper task", it is now paper, with three auto-marked card checks (form labels, date order, invitation parts). *Location:* `content/english/16.json`; `docs/audit/english-language.md` row 16.
- [ ] **TR-E21 [P2] Speaking lessons (1 and 13)** are taught with auto-marked questions about the language (the right reply, the right preposition, word order, a conversation in order). The pupil does not speak to the app. *Location:* `content/english/1.json`, `13.json`.
- [ ] **TR-E22 [P2] Speech Work deferred:** Lessons 4, 8 and 12 need recorded sounds. They are hidden from the pupil and left out of the coverage checklist until an audio decision is made. *Location:* `content/english/4.json`, `8.json`, `12.json`; `isDeferred()` in `src/engine/teach.js`; `checklistLessons()` and `applyChecklist()` in `src/engine/state.js`.
- [ ] **TR-E23 [P2] Word order:** the final . ? or ! stays at the end and is not a tile; capital letters do not matter when checking; a comma stays on its word ("Mummy,"). Another correct order is accepted only if listed (e.g. "My name is Bih and I am from Kumbo." and "I am from Kumbo and my name is Bih."). *Location:* `word_order` in `src/engine/template.js`.
- [ ] **TR-E24 [P2] Matching:** all pairs must be right; the wrong pairs are listed. "Sort into groups" uses the same type, with several items per group. *Location:* `matching` in `src/engine/template.js`.
- [ ] **TR-E25 [P2] Paper tasks:** the pupil reads the task, writes in the exercise book, then sees the model answer and a self-check list. The app does not mark it and mastery stays "unknown"; the parent summary should list paper tasks done. *Location:* `paper_task`, `renderPaper()` and `isAutoMarked()` in `src/engine/teach.js`.
- [ ] **TR-E26 [P2] Sources not opened online:** the English sources (Cambridge English Grammar Today, Oxford Learner's Dictionaries) are cited as standard references and were not checked online for this batch; each says so in `content/english/sources.json`.
- [ ] **TR-E27 [P2] Question levels:** 1 = recognise or recall; 2 = produce (type a form, build a sentence, read a text); 3 = spot the error. *Location:* `level` on every English template.

### P3: cosmetic
- [ ] **TR-E28 [P3] Names, places and food:** Ayuk, Bih, Tabe, Ndi, Ewane, Mih, Ashu, Ebai, Enow, Manyi, Ndip, Akwen; Bamenda, Buea, Limbe, Kumba, Mamfe, Kumbo, Wum, Douala, Yaoundé, Small Mankon, Molyko, the Limbe Botanic Garden, Mount Cameroon; achu, eru, fufu and njama njama, koki, puff-puff, garri, plantains. *Location:* all English lessons.
- [ ] **TR-E29 [P3] Timetable times** are written 7:30, 8:30 … with a colon. *Location:* `content/english/5.json`.

**Authored templates (41), each printed with all its data in `content/english/AUTHORED.md`:** `e1-reply` (L1), `e1-greet` (L1), `e1-build` (L1), `e1-dialogue` (L1), `e1-spot` (L1), `c1-1-check` (L1), `c1-2-check` (L1), `e2-sort` (L2), `e2-capital` (L2), `e2-spelling` (L2), `e2-correct` (L2), `e2-spot` (L2), `e3-spot` (L3), `e5-account` (L5), `e5-irregular` (L5), `e6-spelling` (L6), `c6-1-check` (L6), `e7-spot` (L7), `c9-1-check` (L9), `c9-3-check` (L9), `e10-sort` (L10), `e10-unit` (L10), `e10-spot` (L10), `c10-3-check` (L10), `e11-irregular` (L11), `e11-spot` (L11), `e13-sort` (L13), `e13-by` (L13), `e13-reply` (L13), `e13-build` (L13), `e13-spot` (L13), `e14-match` (L14), `e14-written` (L14), `e14-class` (L14), `e14-join` (L14), `e14-convert` (L14), `e14-spot` (L14), `e15-participle` (L15), `e15-spot` (L15), `c15-3-check` (L15), `c16-1-check` (L16). Spot-the-error and true-sentence pools are TR-E10; matching and choice keys fall under the topic items above (TR-E06 to TR-E17).

### Added 2026-10-06 (English screens, Batch E1 released in the app)
- [ ] **TR-E30 [P2] Tap-only screens:** word order (tap to place, tap to remove), matching (tap left then right, tap a pair to undo), sorting (tap a word then its group), the inline blank, and the paper task ("I've written it", then the model answer and self-check ticks). *Location:* `wordOrder()`, `matching()`, `sorting()`, `clozeSentence()`, `paperTask()` in `tools/prototype/app.js`; `docs/phase3-spec.md` §10.
- [ ] **TR-E31 [P2] First-miss feedback in Lesson 3 no longer shows the answer:** "so the verb takes -s." replaces "so the verb takes -s: Our teacher goes …" (and the same for the no -s case), following the rule that a first miss explains without giving the answer. *Location:* `e3-form` misconceptions in `content/english/3.json`.
- [ ] **TR-E32 [P3] Feedback after a wrong matching or sorting attempt** names the items that are not right yet ("These are not right yet: sell, eat, give, sing."), without showing their partners. *Location:* `retry()` in `tools/prototype/app.js`.
- [ ] **TR-C42 [P2] Fixed a display bug in the live Maths app:** after tapping an item in an ordering question, the word "null" appeared among the remaining items (e.g. Lesson 15, construction steps). Fixed 2026-10-06 and guarded by a test. *Location:* `fill()` in `tools/prototype/app.js`; `tests-js/prototype.test.js`.
- [ ] **TR-C43 [P2] The readiness check no longer blocks the app:** the app always opens on the lesson menu; the check is offered as the first button on the Maths tab until it is done, and the English tab never shows it. Maths lessons can still be opened before the check (as before, nothing is locked). Changed 2026-10-07 at Dion's request. *Location:* `menu()` in `tools/prototype/app.js`.

## P. Physics Form 1, Batch P1 (Lessons 1–19, Term 1), added 2026-10-07

All 19 lessons are taught with auto-marked practice. 19 notes, 58 teach cards, 93 practice templates and 16 card-check
templates: 68 have an **authored key** and 41 are **computed by rule** (conversions, weight, density, temperature,
readings of drawn instruments). 7 templates come with a drawing made by code from the question's own numbers (ruler,
measuring cylinder, two cylinders for displacement, thermometer); tests check that each drawing shows exactly the
reading. Everything is draft and **not yet in the app**: it goes in after review. Every authored key and statement is in
`content/physics/AUTHORED.md`; every question and drawing as the pupil sees it is in `content/physics/REVIEW.md`.

### P1: wrong facts here would mislead the pupil
- [ ] **TR-P02 [P1] Scientists, discoveries and dates:** Newton (laws of motion and gravity, 1687), Faraday (electricity from magnets, 1831), Bell (telephone, 1876), Marie Curie (radioactivity, 1898), the Wright brothers (first powered aeroplane flight, 1903), Fleming (penicillin, 1928), Arthur Zang (Cardiopad, about 2011); and how each helps people today. The ordering question uses these dates. *Location:* `content/physics/2.json`.
- [ ] **TR-P03 [P1] g = 10 N/kg on Earth** (not 9.8) and **about 1.6 N/kg on the Moon**. *Location:* `weight()` in `src/engine/lib/physics.js`; `content/physics/15.json`.
- [ ] **TR-P04 [P1] Temperature:** T(K) = T(°C) + 273 (not 273.15); pure ice melts at 0 °C and pure water boils at 100 °C at normal air pressure; a change of 1 °C equals a change of 1 K; thermometers use mercury or coloured alcohol. *Location:* `toKelvin()`, `toCelsius()` in `src/engine/lib/physics.js`; `content/physics/18.json`.
- [ ] **TR-P05 [P1] Unit ladders:** length km … mm; mass t (1000 kg), kg … mg; capacity L, mL (also cL, dL); 1 L = 1 dm³ = 1000 cm³; 1 mL = 1 cm³; 1 m³ = 1000 L; 1 h = 60 min = 3600 s. *Location:* `convertUnit()` in `src/engine/lib/physics.js`.
- [ ] **TR-P06 [P1] Density:** density = mass ÷ volume (answers to 2 decimals); water 1 g/cm³; 1 g/cm³ = 1000 kg/m³; less than 1 g/cm³ floats; ice about 0.92, kerosene about 0.8, iron about 7.9 g/cm³; wood about 0.6 g/cm³ in a card example. *Location:* `content/physics/17.json`.
- [ ] **TR-P07 [P1] Changes of state:** melting, freezing (solidification), evaporation (boiling = fast evaporation at the boiling point), condensation, sublimation (solid → gas) and deposition (gas → solid; some books call this sublimation too); heat taken in going solid → liquid → gas; the eight everyday examples (dew, palm oil hardening on a cold Bamenda morning, mothballs, drying clothes …). *Location:* `processName()`, `heatFlow()` in `src/engine/lib/physics.js`; `content/physics/12.json`.
- [ ] **TR-P08 [P1] Drawings and how to read them:** ruler 0–8 cm with millimetre marks (an object need not start at zero: length = end − start); measuring cylinder with a mark every 2 mL and a number every 10 mL, read at the bottom of the meniscus; displacement = reading after − reading before; thermometer 0–50 °C with a mark every degree. *Location:* `ruler()`, `cylinder()`, `displacement()`, `thermometer()` in `src/engine/lib/physics.js`; drawings in `content/physics/figures/`.
- [ ] **TR-P09 [P1] Branches:** science (Physics, Chemistry, Biology, Geology, Meteorology, Astronomy) and physics (mechanics, heat, optics, sound/acoustics, electricity and magnetism), and the example questions sorted into each. *Location:* `content/physics/1.json`, `3.json`.
- [ ] **TR-P10 [P1] The scientific method:** six steps in this order: observe, ask a question, suggest a testable answer (hypothesis), test with an experiment, record and study the results, draw a conclusion; a fair test changes one thing only. *Location:* `content/physics/4.json`.
- [ ] **TR-P11 [P1] Equipment and what it measures:** metre rule/ruler and measuring tape (length), beam and top-pan balance (mass), measuring cylinder (volume of a liquid), stopwatch (time), thermometer (temperature), spring balance (weight, a force); retort stand, Bunsen burner, beaker and tripod hold or heat. Which instrument is "best" for a desk (metre rule) or a field (measuring tape). *Location:* `content/physics/5.json`, `8.json`, `13.json`.
- [ ] **TR-P12 [P1] Laboratory safety:** the safe and not-safe actions, and what to do after a breakage, a burn, a gas smell. *Location:* `content/physics/6.json`.
- [ ] **TR-P13 [P1] SI units:** metre, kilogram, second, kelvin, ampere and their symbols; the SI unit of mass is the kilogram (not the gram) and of temperature the kelvin (not °C); prefixes kilo, centi, milli. Only five of the seven base units are taught. *Location:* `content/physics/10.json`.
- [ ] **TR-P14 [P1] States of matter:** properties and the particle model; examples (stone, ice, wood, nail, chalk / water, palm oil, kerosene, milk, honey / air, water vapour, oxygen, carbon dioxide). *Location:* `content/physics/11.json`.
- [ ] **TR-P15 [P1] Mass and weight:** the eight statements sorted into mass or weight; mass is the same everywhere, weight changes. *Location:* `content/physics/14.json`, `15.json`.
- [ ] **TR-P16 [P1] Hazard symbols and labels:** the seven symbols described in words (flame, skull and crossbones, corrosion, exclamation mark, gas bottle, dead tree and fish, exploding bomb) and their meanings; kerosene/petrol flammable, rat poison toxic, battery acid corrosive, cooking gas under pressure; label parts (warning, expiry, storage, use, maker); never store kerosene in a drink bottle. *Location:* `content/physics/19.json`.
- [ ] **TR-P17 [P1] Statement pools:** every right and wrong sentence in the spot-the-error and "which is true" questions, with the explanation for each wrong one. *Location:* `content/physics/AUTHORED.md` Part 2.
- [ ] **TR-P18 [P1] Notes and teach cards:** 19 notes and 58 cards: the ideas, their order and their examples. *Location:* `content/physics/REVIEW.md`.
- [ ] **TR-P19 [P1] Typed answers:** decimals may be typed 2.5 or 2,5; negative temperatures with a minus sign (−18 or -18); a misconception list catches common slips (forgetting to convert grams to kilograms, reading only the end of an object, adding 273 to a temperature difference). *Location:* `misconceptions` on every numeric template in `content/physics/*.json`.

### P2: conventions and decisions
- [ ] **TR-P01 [P2] Typed numbers rule for Physics:** as in Maths, cards and working contain no typed numbers, with one exception: a bare 1 in a definition ("1 km = 1000 m", where 1000 is computed). Constants such as 273 and 1000 are written as computed values (e.g. `{toKelvin(0)}`). *Location:* `literalDigits()` in `tests-js/subject-suite.js`.
- [ ] **TR-P20 [P2] Careers:** the nine jobs and what each person does; the five "which job suits this pupil" cases. *Location:* `content/physics/7.json`.
- [ ] **TR-P21 [P2] Physical and non-physical quantities:** the two lists (length … weight; love … courage). *Location:* `content/physics/9.json`.
- [ ] **TR-P22 [P2] Pictures not drawn yet:** lab equipment, particle diagrams, hazard symbols and a beam balance are described in words for now (the audit planned drawn pictures). *Location:* `docs/audit/physics.md`.
- [ ] **TR-P23 [P2] The ruler shows 0–8 cm** so the millimetre marks stay readable on a 360 px phone (about 3.5 px apart). Objects are 1.5 to 7.8 cm long. *Location:* `ruler()` in `src/engine/lib/physics.js`.
- [ ] **TR-P24 [P2] Physics is not in the app yet.** It joins the Maths and English tabs only after this review. *Location:* `SUBJECTS` in `tools/prototype/build.mjs`.

### P3: cosmetic
- [ ] **TR-P25 [P3] Context:** Cameroonian names, places (Buea, Bamenda, Kumba, Mamfe, Limbe, Yaoundé, Mount Cameroon) and goods (palm oil, maize, groundnuts, rice, kerosene). *Location:* all Physics lessons.
- [ ] **TR-P26 [P2] Physics released in the app on 2026-10-07 at Dion's request ("release physics and push it"),** before the TR-P items above were checked by a teacher; the lessons show the usual "drafts" line. The app now has three tabs (Maths, English, Physics) and is about 506 KB (limit raised to 640 KB; the 2 MB Phase 3 budget stands). Supersedes TR-P24. *Location:* `SUBJECTS`, `BATCH` in `tools/prototype/build.mjs`.

## K. Chemistry Form 1, Batch C1 (Lessons 1–21, Term 1), added 2026-10-07

All 21 lessons are taught with auto-marked practice. 21 notes, 63 teach cards, 94 practice templates and 15 card-check
templates: 91 have an **authored key** and 18 are **computed by rule** (unit conversions, weighing by difference, time,
temperature, atom counts from formulas, boiling-point order). Two questions show a drawn measuring cylinder or
thermometer (the Physics drawings). Chemistry is mostly facts and classification, so far more of it rests on teacher
review than Maths or Physics. Everything is draft and **not yet in the app**. Every authored key and statement is in
`content/chemistry/AUTHORED.md`; every question as the pupil sees it is in `content/chemistry/REVIEW.md`.

### P1: wrong facts here would mislead the pupil
- [ ] **TR-K02 [P1] Element table:** the first 20 elements in order plus Fe, Cu, Zn, Ag, Sn, I, Au, Hg, Pb; names in British school spelling (aluminium, sulfur; "sulphur" is not accepted as typed); metal / non-metal / metalloid (B, Si are metalloids and are left out of the sorting question); Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb. *Location:* `ELEMENTS`, `LATIN` in `src/engine/lib/chemistry.js`; `content/chemistry/19.json`.
- [ ] **TR-K03 [P1] Formulas and atom counts:** the ten compounds (water H₂O, carbon dioxide CO₂, sodium chloride NaCl, calcium carbonate CaCO₃, sulfuric acid H₂SO₄, ammonia NH₃, methane CH₄, glucose C₆H₁₂O₆, magnesium oxide MgO, copper(II) sulfate CuSO₄) and how a formula is read (no number means one; brackets multiply). *Location:* `parseFormula()` in `src/engine/lib/chemistry.js`; `content/chemistry/20.json`.
- [ ] **TR-K04 [P1] Branches of chemistry:** organic, inorganic, physical, analytical chemistry and biochemistry, and what each studies. *Location:* `content/chemistry/1.json`.
- [ ] **TR-K05 [P1] Laboratory equipment and uses:** the 20 items in Lessons 3–4 and their jobs (e.g. a burette lets out an exact volume drop by drop; a pipette transfers one exact volume; never heat a measuring cylinder; a blue Bunsen flame is hotter than a yellow one). *Location:* `content/chemistry/3.json`, `4.json`.
- [ ] **TR-K06 [P1] Hazard symbols and reagents:** seven symbols in words (incl. flame over a circle = oxidising) and the typical hazard of six reagents (concentrated sulfuric acid and sodium hydroxide corrosive; ethanol and kerosene flammable; mercury toxic; potassium manganate(VII) oxidising); what to do for each symbol. *Location:* `content/chemistry/5.json`.
- [ ] **TR-K07 [P1] Chemistry safety:** waft smells; add acid to water; point heated test tubes away; never return chemicals to the stock bottle; first actions after a splash on skin or in the eye, a gas smell, a spitting test tube. *Location:* `content/chemistry/6.json`.
- [ ] **TR-K08 [P1] Physical and chemical changes:** the seven examples of each (palm wine and milk turning sour, bread dough rising, rusting… are chemical; dissolving sugar, grinding maize, palm oil hardening… are physical) and the signs of a chemical change. *Location:* `content/chemistry/9.json`.
- [ ] **TR-K09 [P1] States and kinetic theory:** changes of state as physical changes; iodine and ammonium chloride sublime; a pure substance has fixed melting and boiling points (salt water boils above 100 °C); particle movement in each state; diffusion (faster in gases and when warm). *Location:* `content/chemistry/10.json`, `11.json`.
- [ ] **TR-K10 [P1] Pure substances and mixtures:** the lists (distilled water, salt, sugar, oxygen, iron, gold, carbon dioxide are pure; air, sea water, soil, tap water, palm wine, concrete, milk, a soft drink are mixtures); types of mixtures; miscible and immiscible pairs (milk and water treated as miscible); solutions and suspensions. *Location:* `content/chemistry/12.json`, `13.json`.
- [ ] **TR-K11 [P1] Separation methods:** which method for which mixture, and the steps in order (salt from sand; simple distillation; using a separating funnel); residue and filtrate; fractional distillation by boiling point (ethanol about 78 °C, water 100 °C, acetic acid about 118 °C). *Location:* `content/chemistry/14.json` to `16.json`.
- [ ] **TR-K12 [P1] Gases in liquids and in air:** warm water holds less dissolved gas; opening a soft drink lowers the pressure; air is about 78 % nitrogen, 21 % oxygen, almost 1 % argon; fractional distillation of liquid air; sodium hydroxide solution absorbs carbon dioxide. *Location:* `content/chemistry/17.json`, `18.json`.
- [ ] **TR-K13 [P1] Mixtures and compounds compared:** the eight statements, and the iron and sulfur experiment (iron sulfide is not attracted by a magnet). *Location:* `content/chemistry/21.json`.
- [ ] **TR-K14 [P1] Statement pools, notes and cards:** every right and wrong sentence with its explanation, 21 notes and 63 cards. *Location:* `content/chemistry/AUTHORED.md`, `REVIEW.md`.

### P2: conventions and decisions
- [ ] **TR-K15 [P2] Uses of chemistry and "helps or harms":** the eight product → area pairs and the eight help/harm examples. *Location:* `content/chemistry/2.json`.
- [ ] **TR-K16 [P2] Depth for Form 1:** gas–gas separation (liquid air) and liquid–gas separation are taught at a simple, descriptive level; please say if the school goes further or less far. *Location:* `content/chemistry/17.json`, `18.json`.
- [ ] **TR-K17 [P2] Element-symbol questions offer wrong capitalisations** (Cu, CU, cu) as choices on purpose; the test compares tapped options exactly. *Location:* `ch19-symbol` in `content/chemistry/19.json`; `tests-js/subject-suite.js`.
- [ ] **TR-K18 [P2] Not in the app yet:** Chemistry joins as a fourth tab after this review. *Location:* `SUBJECTS` in `tools/prototype/build.mjs`.
- [ ] **TR-K19 [P2] Chemistry released in the app on 2026-10-07 at Dion's request ("release chemistry and push it"),** before the TR-K items above were checked by a teacher; the lessons show the usual "drafts" line. Four tabs now (Maths, English, Physics, Chemistry), shown two by two at 360 px; the page is about 640 KB (limit 800 KB; the 2 MB Phase 3 budget stands). Supersedes TR-K18. *Location:* `SUBJECTS`, `BATCH` in `tools/prototype/build.mjs`.
