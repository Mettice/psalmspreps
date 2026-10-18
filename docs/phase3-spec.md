# Phase 3 (PWA): decisions recorded so far

Decisions made during Phases 1 and 2 that the app must follow. Each one says who decided and when.
The original Phase 3 brief (offline-first Vite + React PWA, IndexedDB only, under 2 MB, 360 px screens,
screens Setup / Today / Catch-up map / Lesson / Parent summary) still applies; this file adds to it.

**Context change (Dion, 2026-10-02):** the pupil has missed most of this term. The app is his
**primary instruction**, not revision. Lessons must teach from zero; coverage cannot be assumed.

Every convention and judgment call is also logged for teachers in `docs/teacher-review.md` (append-only).

## 1. Lesson state: coverage and mastery are separate (Dion, 2026-10-02)

| Field | Values | Starts at | Set by | Never set by |
|---|---|---|---|---|
| `coverage[lesson_no]` | `not_taught`, `taught` | `not_taught` for every lesson | The weekly teacher checklist ("Which of these lessons did your teacher actually cover?") | Answers, Lesson 0, dates |
| `mastery[skill_id]` | `unknown`, `shaky`, `solid` | `unknown` | Answers in Form 1 lessons only | The checklist, Lesson 0, dates |
| `readiness` | score, per-area results, weak areas | none | Lesson 0 only | Everything else |

- There is no date-based coverage estimate any more (superseded 2026-10-02): every lesson starts `not_taught`.
- Skills: a lesson has one implicit skill `m{lesson_no}` unless it declares `skills` (Lesson 7: `m7-operations`, `m7-powers`). Templates and cards in a multi-skill lesson carry `skill`.
- The catch-up map shows both, e.g. "not taught · unknown", "taught · shaky".
- Implemented in `src/engine/state.js` (pure functions, tested in `tests-js/state.test.js`).
- Still to specify: how answers in daily sessions move mastery (the brief's "level up after 2 correct in a row" and "2 wrong → worked example again").

## 2. Lesson 0: Primary 6 readiness (Dion, 2026-10-02; supersedes the Form 1 placement diagnostic)

- At most 15 questions; currently 13, about 10 minutes. Areas: place value up to millions, the four operations, multiplication tables, simple word problems.
- Produces a readiness score and per-area results; an area is **weak** when fewer than two thirds of its questions are right.
- Sets **no Form 1 mastery and no coverage**. Form 1 mastery starts `unknown`.
- Weak areas should trigger short Primary 6 practice (to be specified; the templates in `content/maths/0.json` can serve as that practice).
- **No feedback during the check, and no score for the pupil (approved 2026-10-03):** it ends on a neutral "Let's start" screen. The score and weak-area flags appear only in the adult-facing results ("Copy results" in the prototype; the parent summary in the app).
- Implemented in `src/engine/readiness.js` (`buildReadiness`, `scoreReadiness`).

## 3. Teach mode for every lesson (Dion, 2026-10-02)

1. **Cards** (3–4): one idea + a tiny example + 1 level-1 check question each.
2. **Worked example.**
3. **Practice**, levels 1 → 3.
4. **The note** (at most 150 words) as a summary.

Two tries on every card check **and** every practice question (Dion, 2026-10-03):

| | Wrong answer | "I don't know" |
|---|---|---|
| **1st miss** | "Not quite" + the explanation for that mistake (no answer). Cards also re-show their example. Then a **fresh variant**. | Hint (if any) + worked example (cards: the card's example). Then a fresh variant. |
| **2nd miss** | The correct answer with **full working**, then move on; the item is marked **"needs review"**. | Same. |

- The fresh variant is guaranteed to differ from the question just answered (new numbers, or a new option order for fixed questions).
- Full working: numeric and multiple-choice templates carry a `solution` (templates, no typed numbers, tested to show the computed answer); true/false, spot-the-error and ordering questions build theirs from their own data. Exposed as `q.solution`.
- Cards, hints and solutions follow the same rules as worked examples: status draft, no typed numbers.
- Implemented in `src/engine/teach.js` (`startTeach`, `nextPhase`, `answerItem`, `itemQuestion`, `needsReview`, `practicePlan`; practice is one step per template, easiest first).

## 4. "I don't know" (Dion, 2026-10-02)

- Every question shows an "I don't know" button.
- Counts as **incorrect** (for mastery, readiness and card retries).
- Shows **no answer and no misconception feedback**: only the template's hint (if it has one) and the worked example (in cards: the card's example again). A second miss (wrong or "I don't know") shows the answer with full working (§3).
- Engine: `check(q, DONT_KNOW)` returns `{correct: false, dontKnow: true, misconception: null, show: ["hint", "worked_example"]}` (or `["worked_example"]` without a hint).
- Hints (draft) exist for Lessons 3 and 8 so far; other lessons show the worked example alone.

## 5. Number style (Dion, 2026-10-02)

- 4-digit numbers are not grouped: 7750, 1948. 5 or more digits are grouped with a space: 12 500 FCFA. Non-breaking space, so numbers never split across lines.
- Decimal point, not comma. Input accepts "12 500", "12500", "12,500" (thousands) and "2,5" (decimal).
- Applied in `fmt()`; enforced by tests on all written content and generated questions.

## 6. Calendar (Dion, Phase 1 round 2)

- Terms, holidays and evaluation weeks come only from `data/calendar/2026-27.json`, never from the progression sheets. Most dates are still TODO.

## 7. Assessment rows (Dion, Phase 1 round 2)

- Spine rows of kind integration / evaluation / remediation carry `assesses: <chapter>`; results link to that chapter.

## 8. Prototype constraints (Dion, 2026-10-02)

`tools/prototype/lesson3.html` (built by `node tools/prototype/build.mjs` from the real engine and content):
offline single file, under 500 KB (currently about 78 KB), works at 360 px, no personal data (no name, no storage,
no network), and a "Copy results" button with time per answer and "I don't know" use. Flow: Lesson 0 readiness →
Lesson 3 teach mode → practice → note → results. A test (`tests-js/prototype.test.js`) rebuilds it and checks size,
no network or storage calls, and that the inlined engine runs.

**Changed 2026-10-05 (Dion: the pupil tested Lesson 3 and liked it, "add all"):** the prototype is now
`tools/prototype/maths.html` with Lesson 0 and Lessons 1–16, a lesson menu, and progress saved in the browser
(`localStorage`, one key, every access in try/catch; it still sends nothing). Size limit 256 KB (about 204 KB now).
The readiness check runs once. Published as the site's `index.html`; `/lesson3/` serves the same app so old links work.

## 9. Content still in draft

- All notes, teach cards and worked examples are `status: draft`.
- Conventions pending review: [AB) notation, orthogonal = perpendicular in a plane, number style (teacher-review A01–A03).
- 19 authored questions await review in `content/maths/AUTHORED.md`.

## 10. English and the new question types (Dion, 2026-10-06)

- **Engine first, tests before content.** New template types in `src/engine/template.js`, all answers checked against
  exact accepted lists:
  - `cloze`: one `___` blank. With `choices` it is shown like multiple choice; without, the pupil types. Typed answers
    are case-insensitive, outer and repeated spaces are ignored, curly apostrophes count as straight ones; spaces inside
    the answer still matter. The keyboard is the text keyboard.
  - `word_order`: the pupil taps word tiles into a sentence. The final . ? or ! is not a tile. Any listed correct order is
    accepted; capital letters are ignored when checking.
  - `matching`: pairs (left → right), all must be right; wrong pairs are reported. With `groups: true` it becomes
    "sort into groups". UI at 360 px: tap a left item, then a right item (no dragging).
- **Writing lessons are paper tasks** (`paper_task`): prompt → the pupil writes in the exercise book → "I have written
  it" → model answer + self-check list. No auto-marking; mastery for the lesson stays `unknown` (`isAutoMarked()`).
  Steps: cards → worked example → paper task → note.
- **Speech-work lessons are deferred** (`status: "deferred"`): hidden from the pupil, no teach steps, and never shown
  or recorded in the weekly coverage checklist (`checklistLessons()`, `applyChecklist(state, answers, deferred)`).
- **Libraries per subject:** English templates use `{...maths, ...english}` (`src/engine/lib/english.js` adds word
  forms, subject agreement, a/an, plurals, ordinal words, dates and timetable helpers).
- **Skills are named per subject** (`e3`, not `m3`): every English lesson declares `skills`.
- **Prompts may have line breaks** (timetables, notices, invitations): the UI must show them (`white-space: pre-line`).
- Not yet in the app: the prototype renders mcq, numeric, spot-the-error and ordering only. The three new types and
  the paper flow need UI before English can go in front of the pupil.

**Changed 2026-10-06 (Dion: "build the screens for English, then release Batch E1"):** the app is now
`tools/prototype/form1.html` with Maths and English (subject tabs on the lesson menu). Every interaction is a tap, never a drag:
- Word order: tap a word to add it to the sentence; tap a word in the sentence to send it back. Tiles wrap at 360 px
  (tested with 15 words); the final . ? or ! sits after the last tile; "Check" works only when every word is placed.
- Matching: tap a left item, then a right item; the pair gets the same number badge; tap either item of a pair to undo it.
  Sorting: tap a word, then tap its group; tap a word inside a group to take it out.
- Cloze: the blank sits inside the sentence. Typed answers use the same answer box as numbers (Enter or "Check"), with
  the text keyboard and with autocorrect, auto-capitals and spellcheck off so the phone cannot correct the pupil.
- Paper task: the task → "I've written it" → model answer + self-check list. Ticks are saved with the lesson and appear
  only in "Copy results"; nothing is scored and mastery stays unknown.
- Deferred lessons (English 4, 8, 12) are not shipped at all: no content, no title, not in the menu.
- "Copy results" and "Copy all results" list Maths and English with the same fields, plus the paper-task ticks.
- Same motion, 48 px tap targets (tiles also 48 px wide) and reduced-motion rules as Maths. Size limit 448 KB (about
  368 KB now; the Phase 3 budget for the whole app stays 2 MB).
- Saved progress moved to version 2 (lessons keyed "maths:3", "english:3"; one lesson in progress per subject). A
  version-1 save (Maths only) is upgraded in place under the same key, so the pupil keeps his ticks; a damaged
  lesson-in-progress is dropped rather than breaking the page.

## 11. Physics and drawn instruments (2026-10-07)

- Subject order agreed with Dion: Physics, Chemistry, Geography, then the rest; French last.
- `src/engine/lib/physics.js`: unit conversions (length, mass, capacity, time), weight (g = 10 N/kg), density, °C ↔ K,
  changes of state, label dates, and **drawn instruments**: `ruler()` (0–8 cm), `cylinder()`, `displacement()`,
  `thermometer()`, `clinical()`. Each returns an SVG string drawn from the question's own numbers, so the reading is
  computed, never typed; tests check that every drawing shows exactly that reading.
- Any template, teach card or worked example may have `figure: expr`. The app shows it under the prompt (at most 300 px
  tall, full width, light and dark colours from the page). REVIEW.md links the drawings as files in `content/{subject}/figures/`.
- Content for new subjects is tested by one shared suite (`tests-js/subject-suite.js`) with the same rules as Maths
  and English; Physics templates start with `p`, skills `p1` … `p19`.
- Physics Batch P1 (Lessons 1–19) was written and tested, then **released on 2026-10-07** at Dion's request (TR-P26):
  a third tab, `lib/physics.js` in the bundle, size limit 640 KB. Releasing it
  means adding `physics` to `SUBJECTS` and `lib/physics.js` to the bundle in `tools/prototype/build.mjs`.

## 12. Chemistry (2026-10-07)

- `src/engine/lib/chemistry.js`: an authored element table (first 20 + common metals, British spellings, Latin
  origins) and a formula parser (`parseFormula()`, brackets supported) so atom counts and element lists are computed.
  Chemistry templates use `{...maths, ...english, ...physics, ...chemistry}` and reuse the Physics units and drawings.
- Content is tested by the shared suite; template ids start with `ch`, skills `ch1` … `ch21`. In multiple choice the
  suite compares options exactly, because some questions (element symbols) offer the same letters in different capitals.
- Batch C1 (Lessons 1–21) was written and tested, then **released on 2026-10-07** at Dion's request (TR-K19): a fourth
  tab (the subject tabs now sit two by two), `lib/chemistry.js` in the bundle, size limit 800 KB.

## 13. Geography (2026-10-06)

- `src/engine/lib/geography.js`: local time from longitude (`localTime()`, `clock()`, `duration()`), time zones
  (`zone()`), positions (`lat()`, `lon()`, `latlon()`), map scale (`realKm()`, `mapCm()`, `ratio()`), grid references
  (`grid4()`, `grid6()`), leap years, authored tables (planets, continents, oceans, parallels), and **code-drawn maps**:
  `gridMap()`, `graticule()`, `marginMap()`, `dayNight()`, `parallels()`. The places on a drawn map come from the
  question's own numbers, so the answer is computed. The expression language reads only variables and calls library
  functions, so tables are exposed as functions (`planetName(i)`, `parallelLat(i)`, `gridPlaces()`).
- Geography is numbered by **place in the year** (spine `seq`): the sheet's practicals PW1–PW5 have no lesson number,
  and two-part lessons share one. The shared suite takes `numbering: "seq"`; so does the review renderer (TR-G14).
- Template ids start with `g`, skills `g1` … `g10`. Library order: `{...maths, ...english, ...physics, ...chemistry, ...geography}`.
- Batch G1 (Lessons 1–10, Term 1) was written and tested, then **released on 2026-10-07** at Dion's request (TR-G19): a fifth
  tab, `lib/geography.js` in the bundle, lessons numbered by place in the year (`BY_SEQ` in the build), size limit 900 KB.

## 14. Home Economics (2026-10-07)

- `src/engine/lib/homeeconomics.js`: the kitchen work triangle (`triangleTotal()`, `goodTriangle()`, `triangleVerdict()`;
  sides 1.2–2.7 m, total 4–7.9 m, TR-H01) and drawings made by code with **lettered parts**: `traditionalKitchen(k)`,
  `fireplaces(k)`, `kitchenUnits(k)` (the letters follow arrangement `k`, so `letterOf()` / `fireLetter()` give the answer)
  and `kitchenPlan(type)` for the five kitchen shapes.
- Subject id `home-economics`; template ids start with `he`, skills `he1` … `he21`; lesson numbers are the sheet's (equal
  to the row), so Batch H1 is Lessons 1–7, 10–17 and 20–21 (rows 8–9 and 18–19 are integration and remediation).
- Batch H1 (Term 1) was written and tested, then **released on 2026-10-07** at Dion's request (TR-H17): a sixth tab,
  `lib/homeeconomics.js` in the bundle; the page is about 875 KB of the 900 KB limit.

## 15. History, Biology and Computer Science (2026-10-07)

Dion asked for "History, Biology, Computer Science" together; each Term 1 batch was written and tested, then all three
were **released on 2026-10-07** (TR-S12): nine tabs, build limit raised to 1.3 MB (page about 1157 KB of the 2 MB budget).
- **History** (`src/engine/lib/history.js`): years BC/AD with no year 0 (`year()`, `yearsBetween()`), centuries,
  a timeline drawn by code, an authored table of early humans. Numbered by place in the year (most rows are further
  study or guided work). Ids `hi`, skills `hi1` … `hi10`. Review items TR-Y.
- **Biology** (`src/engine/lib/biology.js`): magnification = eyepiece × objective; drawings with lettered parts
  (`microscope()`, `plantCell()`, `animalCell()`, `soilProfile()`; `bioLetter()` gives the letter). Lessons 1–9 and
  13–21, matched to the spine by place in the year because practicals have kind "practical". Ids `b`, skills `b1` …
  `b21`. Review items TR-L (TR-B is taken).
- **Computer Science** (`src/engine/lib/computerscience.js`): number and shape patterns, tracing short algorithms,
  authored history and generations, drawings (`shapeSequence()`, `labLayout()`). Lessons 1–6, 8–11, 13–14, 16–18.
  Ids `cs`, skills `cs1` … `cs18`. Review items TR-S.
- Library order for each subject is every earlier library, then its own. A test now fails if a later library reuses a
  function name (TR-S10).

## 16. French (2026-10-08)

- `src/engine/lib/french.js` (all names start with `fr`, so nothing clashes with the English library): an authored noun
  table (gender, plural, vowel start), articles and possessives with élision and h aspiré, subject pronouns, the present
  of avoir, s’appeler and -er verbs, numbers 0–100 in words (traditional, and the 1990 spelling accepted when typed),
  alphabetical order ignoring accents, and helpers that build typical mistakes for wrong options.
- **French lessons are in French throughout.** A template with `lang: "fr"` makes the engine write its own working in
  French (« … », “La bonne réponse est …”, “Le bon ordre est : …”); English templates are unchanged (tested).
- Batch F1 = Lessons 1–15 (to the first integration row); ids `f`, skills `f1` … `f15`. Most answers are tapped, not
  typed, because typing accents on a phone is slow (TR-F10). **Released on 2026-10-13** (TR-F14): a tenth tab; inside
  French lessons the app’s own labels come from a small French table (`T()` in `app.js`), and `<html lang>` is set to
  `fr`. The page is about 1263 KB of the 1.3 MB limit.

## 17. Teacher review mode (2026-10-17)

- `tools/prototype/review.js`, bundled after `app.js`. The page's last line chooses: `?review` → the review list;
  otherwise the pupil's lesson menu. Review marks are kept under their own key (`psalmspreps-review-v1`); the test allows
  exactly that key and the pupil's key.
- Every part of a lesson is shown with its answer (cards, check questions, worked example, practice, writing task,
  note). Marks are ✓/✗ plus a comment, keyed `subject:lesson:id`. “Send my review” uses the phone's share sheet, or
  copies the text; the message lists every problem with its comment, and counts the OKs per lesson.
- Verified at 360 px: all 154 lessons (1501 parts) render in review mode with no errors and no sideways scroll.
- Decided with Dion (2026-10-17): Term 1 stays free; money comes later. Next: an installable offline app with
  per-subject loading, together with a more colourful design and forgiving streaks.

## 18. Installable app and new design (2026-10-17)

**Installable, offline, one subject at a time.** The main link is now an installable web app (`site/` from
`tools/prototype/pwa/`):
- `index.html`: the core page (engine, screens, lesson titles; about 221 KB, limit 400 KB). `CONTENT` starts empty.
- `subjects/<id>.js`: one file per subject (66–131 KB), loaded the first time the subject is opened (`withSubject()`).
- `sw.js`: a service worker. The core page is checked online first (so updates arrive) and falls back to the saved copy;
  subject files are versioned by build and served from the phone once saved. On an update, subjects already saved are
  fetched again in their new version. Tested: with the server stopped, the app opened and a saved subject loaded.
- `manifest.webmanifest` and icons (an open book under a star, in the app's green; maskable versions for Android).
- “For a grown-up” offers “Save every subject for offline use” and “Download one file to share” (`offline.html`, the
  single-file app, kept for Bluetooth or a flash drive; size limit 1.5 MB). `/lesson3/` now redirects to the app.
- Progress is under the same browser key as before, so pupils keep their progress.

**Design (Dion: colourful, interactive, streaks):**
- Home: a greeting, three counters (🔥 streak days, ⭐ stars, ✓ lessons), “Carry on” for the latest unfinished lesson,
  one coloured tile per subject with its icon and progress bar, “My badges”, and the grown-up section.
- Each subject has a colour (dark enough for white text) and an icon. Its lessons appear as a path: done lessons
  filled with the subject colour, the next lesson highlighted and gently pulsing (off under reduced motion).
- **Streaks are forgiving** (ghost towns, power cuts, no data): a day counts when the pupil answers a question in a
  lesson, and up to two days off in a row never break a streak. Checked: two days off keep it, three end it.
- **Stars** for each finished lesson: 3 if at least 80% of first tries were right, 2 if at least half, otherwise 1;
  they pop in on the results screen.
- **Badges** (21): lesson counts (1, 5, 10, 25, 50), streaks (3, 7, 14 days), stars (30, 100), a lesson in every
  subject, and finishing each subject. Once earned, kept. New badges are announced at the end of a lesson.
- Verified at 360 px in the installable app: all 154 lessons run with no errors, no "null" and no sideways scroll; every
  lesson ends with its stars; badges and the streak update; light and dark themes.

## 19. Form 2, Term 1: Maths and English (2026-10-17, form-2 branch)

Built on the `form-2` branch only, so the live app (from `main`) is unchanged until Dion merges it.
- **Content:** `content/form-2/maths/` (rows 1–24; row 1, the diagnostic, deferred) and `content/form-2/english/`
  (rows 1–32; speech work deferred, writing lessons as paper tasks). Numbered by place in the year (proposal G1).
  New library `src/engine/lib/maths2.js` (integers, powers, primes, HCF and LCM, sequences, algebraic expressions,
  inequalities, and drawings: coordinate plane, number line, inequality line, perpendicular bisector, segment).
  Engine: a numeric template may be `signed`, which gives the full keyboard (with a minus sign) on every variant.
- **Tests:** `tests-js/form2-maths-content.test.js`, `form2-english-content.test.js` (the shared subject suite, with
  `dir` and `cls` options), `maths2.test.js`; the app tests check both classes.
- **App:** subject ids `f2-maths` and `f2-english`; a class switch on the home screen (only when a copy has more than
  one class); class names in headings, results and review mode; one shareable file per class (`form1.html` and
  `offline.html`; `form2.html` and `offline-form-2.html`). The service worker's re-save on update now accepts ids with
  digits (it would have missed `f2-maths`).
- **Verified at 360 px:** every lesson of both classes runs from the first card to the stars with no errors, no
  “null” and no sideways scroll.
- Review files: `npm run review:f2-maths`, `npm run review:f2-english`; teacher items TR-N, TR-W and TR-R04.

## 20. Form 2, Term 1: Physics, Chemistry and Biology (2026-10-18, form-2 branch)

- **Content:** `content/form-2/physics/` (rows 1–15), `chemistry/` (rows 1–4, 6–11, 13–17) and `biology/` (rows 1–9,
  13–21, practicals included). Integration, evaluation, remediation and review rows are not lessons, as in Form One.
- **New library** `src/engine/lib/science2.js`: mean and graphs (line graph, bar chart), speed conversions; electron
  shells, group and period, mass numbers, the valency table, formulae and names from valencies, the Bohr drawing; the
  flower and bean-seed drawings with shuffled letters. All three Form 2 sciences use the same library chain.
- A card whose check points at a harder practice question now gets its own level-1 copy (`id-card`), so card checks are
  always level 1.
- **App:** subjects `f2-physics`, `f2-chemistry`, `f2-biology` under Form Two. The Form Two shareable file is about 956 KB
  (limit 1.5 MB); the Form One file is unchanged in content.
- Review files: `npm run review:f2-physics`, `review:f2-chemistry`, `review:f2-biology`; teacher items TR-Q, TR-J, TR-V.

## 21. Form 2, Term 1: Home Economics, Geography, History, Computer Science, Accounting (2026-10-18, form-2 branch)

- 64 lessons: `content/form-2/{home-economics,geography,history,computer-science,accounting}/`. Integration, evaluation and
  remediation rows are not lessons; practicals, guided work and further study are taught.
- `science2.js` gains hexadecimal, 8-bit binary, ASCII codes and storage units (1 KB = 1024 bytes, TR-T05).
- Accounting is new: colour #556b2f and the 🧾 icon. Form Two now has ten subjects.
- The Form Two shareable file is about 1.34 MB (limit 1.5 MB). French and Français intensif will not fit: before they
  are added, the Form Two file must be split (for example sciences and languages) or the limit raised within the 2 MB budget.

