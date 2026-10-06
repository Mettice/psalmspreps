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
