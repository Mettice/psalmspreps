# Psalms Preps: Form 1 Maths, English, Physics and Chemistry (offline)

An offline-first learning app for Cameroonian secondary students (English sub-system), starting with
Form 1 Mathematics, English, Physics and Chemistry. It is built for pupils who lose school days, so it **teaches** missed lessons
(idea cards, worked examples, practice with full working) instead of only quizzing on them.

## Try it

**https://psalmspreps.vercel.app/** (also https://mettice.github.io/psalmspreps/)

Open the link on a phone. The page is a single file: once it has loaded it works with no internet and sends
nothing. There is no name to enter. Progress is saved on that phone, in that browser only.

What it does today (prototype):

1. **Getting ready** (first visit only): 13 Primary 6 questions (place value, the four operations, times tables,
   word problems). No right/wrong is shown to the pupil.
2. **Maths Lessons 1–16, English Lessons 1–16, Physics Lessons 1–19 and Chemistry Lessons 1–21** (four tabs on the menu, a tick for each lesson done). Each lesson
   has 3–4 idea cards, a worked example, practice questions (levels 1 to 3) and a summary. A miss gets a fresh
   question; a second miss shows the full working. A lesson left part-way carries on where it stopped.
   English adds fill-the-blank, word-order and matching questions (all by tapping), and two writing lessons done on
   paper with a model answer and a self-check list. The three speech-work lessons (4, 8, 12) need audio and are left
   out for now. Physics measurement questions come with drawn rulers, measuring cylinders and thermometers.
3. **Results** for a grown-up: "Copy results" (end of a lesson) or "Copy all results" (menu → For a grown-up) gives
   the time per answer, "I don't know" use, the readiness areas, the questions to review and the writing self-check ticks, ready to paste into WhatsApp.

All lessons are drafts until a teacher has reviewed them (`docs/teacher-review.md`).

To use it with no internet at all, open the link once and save the page in the browser (menu → Download or Save
page); the saved file works on its own (some browsers do not keep progress for a saved file).

## For developers

Requirements: Node 22 or later, Python 3.10 or later.

```bash
npm test                              # engine, content (every question across 1000 variants), prototype
python -m unittest discover -s tests  # curriculum spine
npm run build:site                    # builds site/ (what Vercel and GitHub Pages publish)
npm run review                        # regenerates content/maths/REVIEW.md
npm run review:english                # regenerates content/english/REVIEW.md and AUTHORED.md
npm run review:physics                # regenerates content/physics/REVIEW.md, AUTHORED.md and figures/
npm run review:chemistry              # regenerates content/chemistry/REVIEW.md, AUTHORED.md and figures/
```

Every push to `main` runs all the tests and, only if they pass, publishes the site to GitHub Pages
(`.github/workflows/pages.yml`). Vercel also deploys every push to `main` (`vercel.json`).

| Folder | What it holds |
|---|---|
| `data/spine/` | Form 1 progression sheets parsed into JSON, approved overrides, `issues.md` |
| `data/calendar/` | The official school calendar (dates still to be filled in) |
| `content/maths/` | Lessons 0–16: notes, teach cards, worked examples, question templates (all drafts) |
| `content/english/` | English Lessons 1–16 (Batch E1, drafts): 11 with practice, 2 paper tasks (writing), 3 speech-work lessons deferred |
| `content/physics/` | Physics Lessons 1–19 (Batch P1, drafts): measurement questions come with drawn rulers, cylinders and thermometers |
| `content/chemistry/` | Chemistry Lessons 1–21 (Batch C1, drafts): atom counts from formulas are computed by code |
| `src/engine/` | The question engine: answers are always computed by code, never by a person or an AI |
| `tools/` | Sheet parser, review generators, prototype and site builders |
| `docs/` | `teacher-review.md` (everything a teacher should check, P1 first) and `phase3-spec.md` |

All lesson content is **draft** until a teacher has reviewed it: see `docs/teacher-review.md`.
