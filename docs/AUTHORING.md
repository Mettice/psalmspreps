# Writing lessons: the guide for every author (Claude, Codex, ChatGPT, people)

Psalms Preps is an offline app that **teaches** the Cameroon anglophone secondary curriculum. For many pupils
the app is the main teacher, so a lesson must explain before it asks. This guide is the contract: a lesson that
follows it passes `npm test`, builds into the app, and reads like the others.

Owner: Dion (decides anything marked **ask**). Integrator: Claude merges every branch into `form-2` and rebuilds.

---

## 1. Ground rules

1. **Never touch `main`.** `main` is the live app a Form 1 pupil uses every day. Work happens on your own branch
   (section 9); Claude merges into `form-2`; only Dion decides when anything reaches `main`.
2. **Stage explicit paths only.** Never `git add -A`, `git add .` or `git commit -a`. Never commit PDFs
   (`data/**/*.pdf`), `.handoff/`, or the built pages `tools/prototype/*.html` (the integrator rebuilds them).
3. **Do not edit shared files** unless your assignment says so: `src/engine/teach.js`, `template.js`, `expr.js`,
   `tools/prototype/*.js|mjs`, `tests-js/subject-suite.js`, `tests-js/prototype.test.js`, `content/classes.json`,
   `package.json`. If you need a change there, write it in your log and ask.
4. Every number a pupil sees in cards, worked examples, Learn screens, working and hints is **computed**
   (`{expr}`), never typed. A wrong typed number is the worst bug this app can have.
5. **Honest reports.** End every session with a log entry (section 10): what you wrote, what you checked
   (tests, browser), what you did not check, and anything a teacher must verify.

## 2. Which rows to write

The yearly sheets are parsed into **spines**: `data/spine/<class>/<subject>.json` (`terms[].lessons[]`, each with
`seq`, `title`, `kind`, dates). A lesson file is named by the row's **`seq`** (its place in the year):
`content/form-3/maths/2.json` is row seq 2.

- Write rows of kind **`lesson`**. Practicals: write them as guided preparation (what to do, what to observe,
  how to record) when the pupil can learn it from the screen; otherwise skip.
- Skip integration, evaluation, remediation, revision, "contact with students" and "diagnostic" rows (seq 1 of many
  sheets): they are not lessons.
- Order of work (decision 2026-10-23): **Term 1 of every class first**, then Term 2, then Term 3.
- Speech-only rows (pronunciation, listening that needs audio): mark `deferred` with a reason, or teach the
  written part (spelling, stress marks) and say so in the review notes.

## 3. What a lesson looks like (pupil's order)

1. **Learn screens** (`learn`) — **required for every new lesson.** The fuller explanation pupils asked for.
2. **Cards** (`teach.cards`, 3–4) — one key idea each, a tiny example, then a level-1 check question.
3. **Worked example** (`worked_example`) — one problem solved step by step.
4. **Practice** (`questions`) — levels 1, 2 and 3; each wrong answer gets feedback, a second try on a fresh
   variant, then the full working.
5. **Summary** (`note`) — at most 150 words, the lesson in brief.

Writing lessons (essays, letters, compositions) replace practice with a `paper_task`: prompt, model answer, self-check list.

### The JSON (made for you by `tools/authoring/lessonlib.py`)

```text
{ subject, class, lesson_no, language, prerequisites: [seq…], skills: [{id, name}],
  note: {status: "draft", text},
  learn: {status: "draft", vars?, checks?, sections: [{heading, text, figure?}], key_words?: [{word, meaning}],
          examples?: [text], mistake?: {wrong, right, why}},
  worked_example: {status, vars, problem, steps: [...], answer, checks, figure?},
  teach: {cards: [{id, status, idea, vars, example: [...], checks, figure?, check: {ref: <question id>} | <inline template>}]},
  questions: [template…],
  paper_task?: {status, prompt, model: [...], checklist: [...], vars, checks} }
```

Question types: `numeric` (typed number, `misconceptions` with `wrong` + `explain`), `mcq` (`correct` +
`distractors`, each with a `misconception` explained), `cloze` (fill the gap: typed or chosen), `ordering`,
`word_order`, `matching` (pool of pairs), `spot_error` (find the wrong statement or step), `blanks` (step-by-step).
Variables: `{"int": [lo, hi]}`, `{"pick": [...]}`, computed expressions; `where` filters bad combinations.
Copy the patterns from the reference lesson (section 5) and existing Form 2 lessons of the same subject.

## 4. The quality bar (the tests check the first part; reviewers check the rest)

Checked by `npm test` (`tests-js/subject-suite.js`), for every template over 1000 random seeds:
- Notes ≤ 150 words. Learn: 1–4 sections, each ≤ 120 words, ≤ 450 words in all.
- 3–4 cards, each with a level-1 check whose variants differ across seeds.
- Practice covers levels 1, 2 and 3. Every answer verified; options distinct; every wrong option has feedback.
- No literal digits in cards, worked examples, Learn, working or hints. No `{`, `}`, `undefined`, `NaN`, `Infinity`.
- Every template has `sources` that exist in the subject's `sources.json`.

Expected by reviewers (Codex's Term 3 French met the tests but fell short here; aim higher):
- **Learn screens that teach**: a real explanation in plain words, Cameroonian examples (names like Bih, Ayuk,
  Ngozi; places like Buea, Bamenda, Douala; CFA francs), key words with meanings, and the most common mistake.
- **4–6 practice questions** per lesson, not 3. Levels rise: recall → apply → think (multi-step, explain, spot the error).
- **At least 3 variants per question** (random numbers or a bank of 3+ items), so a retry is a new question.
- **4 options** where possible, and **each wrong option has its own feedback** that names the mistake.
  "The answer is X" is not feedback.
- Card checks test the idea on that card, not another one.
- Content correct for the Cameroon syllabus and the GCE exams; anything uncertain goes in the review notes.

## 5. Reference lesson and tools

- Reference: `tools/authoring/form3/maths.py` → `content/form-3/maths/2.json` (Learn, cards, worked example,
  5 practice questions, specific feedback, everything computed). Learn samples in English and French:
  `content/form-2/maths/55.json`, `content/form-2/french/72.json`.
- `tools/authoring/lessonlib.py`: `use_class("form-3", "Form 3")`, `lesson(...)`, `learn(...)`, `card`, `worked`,
  `num`, `mcq`, `cloze`, `order`, `match`, `word_order`, `pool`, `deferred`.
- `tools/authoring/banks_en.py` / `banks_fr.py`: question banks for language and content subjects —
  `QA` (multiple choice from a bank of {q, r, w[3], e[3], y}), `CL` (cloze bank), `MT` (matching), `WO` (word
  order), `SP` (spot the error), `TF` (true/false pool); French versions mark `lang: "fr"`.
- `python tools/content/add_learn.py <lesson.json> <learn.json>` adds Learn screens to an existing lesson.
- Keep your generator scripts in `tools/authoring/<class>/<subject>.py` and commit them: lessons are rebuilt from them.

## 6. Per-subject conventions

**Maths, Additional/Further/Pure Maths** — everything computed with `src/engine/lib/maths.js` and `maths2.js`
(`poly`, `mono`, `bracket`, `br`, `fmt`, fractions, statistics, figures). Numeric answers wherever possible;
misconceptions as typed wrong values (sign errors, wrong order of operations). Figures as SVG functions.

**Physics, Chemistry, Biology, Human Biology, Geology** — SI units always shown; formulas and constants from
`physics.js`, `chemistry.js` (formulae, masses), `science2.js` (balanced equations, energy); diagrams as SVG.
Practicals become guided preparation. Biology/Human Biology: sensitive topics (reproduction, FGM, abortion,
drugs) — factual, age-appropriate, Cameroonian law marked **teacher to verify**.

**English Language, Literature in English** — banks (`banks_en.py`): grammar by `QA`/`CL`/`SP`, vocabulary by
`MT`, sentence building by `WO`. Writing lessons use `paper_task` with a model answer and checklist.
Literature: set texts change by year — **ask** which texts before writing; never reproduce copyrighted text,
summarise and quote at most a line.

**French, Français intensif** — entirely in French, `lang: "fr"` (`banks_fr.py`), French typography (space before
: ; ? !). Verb forms computed by `french.js` / `french2.js` (only verbs in their tables; add verbs with tests).
Oral rows: preparation (phrases, model dialogue), not listening.

**History, Cameroon/African/World History** — dates and names are authored facts with sources; dates in text go
through vars (no typed digits). Sources an author invents for a source-analysis exercise must say they are
invented. Contested points: give the syllabus view and flag for review.

**Geography** — Cameroon-first examples; map/grid reading with SVG; rates and densities computed
(`geography.js`).

**Economics, Accounting** — definitions with Cameroonian examples (CFA francs, local markets); every amount,
ratio and balance computed; accounting entries shown as ledgers or tables.

**Computer Science, ICT** — code traces and outputs computed where possible; pseudocode in the syllabus style;
no instructions that need a computer the pupil may not have — describe and show.

**Logic, Philosophy** — banks of statements; truth tables computed; arguments as `spot_error`.

**Food and Nutrition, Home Economics** — nutrient energy computed (`homeeconomics.js`); safety rules authored with sources.

**Cinema subjects (Sixth Form)** — **ask** before starting: these need decisions on scope.

## 7. Adding a class or a subject

Classes from Form 3 on are listed in `content/classes.json` (id prefix, spine, libraries, language). The build,
`tests-js/classes-content.test.js` and `npm run review -- <id>` read it, and a subject's lessons are the files
in its folder — no batch list to edit. Adding a class or subject to `classes.json` is the integrator's job:
ask if yours is missing. Form 3 is listed; Forms 4, 5, Lower and Upper Sixth have spines but are not listed yet.

## 8. Checking your work

```bash
python tools/authoring/form3/<subject>.py          # writes the lesson files
npm test                                           # every rule above, 1000 seeds per question
npm run review -- f3-<subject>                     # writes content/form-3/<subject>/REVIEW.md and AUTHORED.md
node tools/prototype/build.mjs                     # builds tools/prototype/form3-term-1.html (do not commit it)
```

Then open `tools/prototype/form3-term-1.html` at phone width (360 px) and go through every new lesson: no
`undefined`, nothing wider than the screen, every button leads somewhere. An automated walker is in
`tools/authoring/walk.js` (paste into the browser console, set `window.__only = ["f3-<subject>"]` first).

Teacher review notes go in **`content/<class>/<subject>/TEACHER-REVIEW.md`** (one file per subject, so authors
never edit the same file): numbered items `TR-<subject>-<n>` for every fact, convention or choice a teacher must check.

## 9. Working side by side

Each author works in **their own folder and branch**, so nobody overwrites anyone:

| Author | Folder | Branch |
|---|---|---|
| Claude | `C:\Users\efuet\preps` | `form-2` (integration) and `f3-claude` |
| Codex | `C:\Users\efuet\preps-codex` (git worktree) | `f3-codex` |
| ChatGPT (web) | no repository access | sends text; Claude or Codex pastes it in and runs the tests |

Push your branch when a batch passes: `git push -u origin <branch>`. Claude merges into `form-2`.
Before starting a session: `git fetch origin && git merge origin/form-2` (pick up the latest engine and rules).

## 10. Log

Each author appends to their own file, `docs/log/<author>.md` (`claude.md`, `codex.md`, `chatgpt.md`), so logs
never clash. Each entry: date, rows written, tests result, browser check, what was not checked, open questions.
