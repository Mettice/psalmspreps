# Psalms Preps: Form 1 Maths (offline)

An offline-first learning app for Cameroonian secondary students (English sub-system), starting with
Form 1 Mathematics. It is built for pupils who lose school days, so it **teaches** missed lessons
(idea cards, worked examples, practice with full working) instead of only quizzing on them.

## Try it

**https://psalmspreps.vercel.app/** (also https://mettice.github.io/psalmspreps/)

Open the link on a phone. The page is a single file: once it has loaded it works with no internet and sends
nothing. There is no name to enter. Progress is saved on that phone, in that browser only.

What it does today (prototype):

1. **Getting ready** (first visit only): 13 Primary 6 questions (place value, the four operations, times tables,
   word problems). No right/wrong is shown to the pupil.
2. **Lessons 1–16** of Form 1 Maths, from a menu with a tick for each lesson done. Each lesson has 3–4 idea cards,
   a worked example, practice questions (levels 1 to 3) and a summary. A miss gets a fresh question; a second miss
   shows the full working. A lesson left part-way carries on where it stopped.
3. **Results** for a grown-up: "Copy results" (end of a lesson) or "Copy all results" (menu → For a grown-up) gives
   the time per answer, "I don't know" use, the readiness areas and the questions to review, ready to paste into WhatsApp.

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
```

Every push to `main` runs all the tests and, only if they pass, publishes the site to GitHub Pages
(`.github/workflows/pages.yml`). Vercel also deploys every push to `main` (`vercel.json`).

| Folder | What it holds |
|---|---|
| `data/spine/` | Form 1 progression sheets parsed into JSON, approved overrides, `issues.md` |
| `data/calendar/` | The official school calendar (dates still to be filled in) |
| `content/maths/` | Lessons 0–16: notes, teach cards, worked examples, question templates (all drafts) |
| `src/engine/` | The question engine: answers are always computed by code, never by a person or an AI |
| `tools/` | Sheet parser, review generators, prototype and site builders |
| `docs/` | `teacher-review.md` (everything a teacher should check, P1 first) and `phase3-spec.md` |

All lesson content is **draft** until a teacher has reviewed it: see `docs/teacher-review.md`.
