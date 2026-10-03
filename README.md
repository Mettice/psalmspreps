# Psalms Preps: Form 1 Maths (offline)

An offline-first learning app for Cameroonian secondary students (English sub-system), starting with
Form 1 Mathematics. It is built for pupils who lose school days, so it **teaches** missed lessons
(idea cards, worked examples, practice with full working) instead of only quizzing on them.

## Try it

**https://mettice.github.io/psalmspreps/**

Direct link to the lesson: https://mettice.github.io/psalmspreps/lesson3/

Open the link on a phone. The page is a single file: once it has loaded it works with no internet,
stores nothing and sends nothing. There is no name to enter.

What it does today (prototype):

1. **Getting ready**: 13 Primary 6 questions (place value, the four operations, times tables, word problems).
   No right/wrong is shown to the pupil.
2. **Lesson 3, Hindu-Arabic numerals and place value**: 3 idea cards, a worked example, 6 practice
   questions (levels 1 to 3) and a summary. A miss gets a fresh question; a second miss shows the full working.
3. **Results** for a grown-up: "Copy results" gives the time per answer, "I don't know" use, the
   readiness areas and the questions to review, ready to paste into WhatsApp.

To use it with no internet at all, open the link once and save the page in the browser (menu → Download or Save page); the saved file works on its own.

## For developers

Requirements: Node 22 or later, Python 3.10 or later.

```bash
npm test                              # engine, content (every question across 1000 variants), prototype
python -m unittest discover -s tests  # curriculum spine
npm run build:site                    # builds site/ (what GitHub Pages publishes)
npm run review                        # regenerates content/maths/REVIEW.md
```

Every push to `main` runs all the tests and, only if they pass, publishes the site
(`.github/workflows/pages.yml`).

| Folder | What it holds |
|---|---|
| `data/spine/` | Form 1 progression sheets parsed into JSON, approved overrides, `issues.md` |
| `data/calendar/` | The official school calendar (dates still to be filled in) |
| `content/maths/` | Lessons 0–16: notes, teach cards, worked examples, question templates (all drafts) |
| `src/engine/` | The question engine: answers are always computed by code, never by a person or an AI |
| `tools/` | Sheet parser, review generators, prototype and site builders |
| `docs/` | `teacher-review.md` (everything a teacher should check, P1 first) and `phase3-spec.md` |

All lesson content is **draft** until a teacher has reviewed it: see `docs/teacher-review.md`.
