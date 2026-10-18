# Form 3 curriculum (and Form 2 Home Economics): fixes to the sheets

**Status: approved by Dion on 2026-10-18 (“approve all”) and applied.** Every Form 3 subject now has 0 errors. Each fix is a logged override
(reason + approved by Dion) in `data/spine/form-3/overrides/`; the sheets themselves stay untouched.

The 13 Form 3 progression sheets were read by `python tools/spine/build.py --class form-3` into `data/spine/form-3/`
(full report: `data/spine/form-3/issues.md`). The Form 2 Home Economics sheet, added after the first Form 2 reading,
was read with `--class form-2` (report: `data/spine/form-2/issues.md`).

## Form 2 Home Economics

66 rows, **0 errors**. Only the chapter numbers printed on the sheet jump (2 → 4, 12 → 14 → 13 → 15); with lessons
numbered by place in the year (G1) this does not matter. One thing to note, no change proposed:

| # | What the sheet has | Proposal |
|---|---|---|
| H1 | Row 49 (“Lesson 50: Obesity”) comes before row 50 (“Lesson 49: Rickets and osteomalacia”) | Keep the order printed on the sheet (rows follow each other in the app); the teacher can say if rickets should come first |

## Form 3: subjects found

| Subject | Rows | Notes |
|---|---|---|
| Accounting | 27 | clean (subject name only) |
| Biology | 66 | 1 typo |
| Chemistry | 69 | 1 title to check |
| Computer Science | 83 | clean |
| Economics | 41 | **new in Form 3**; 1 repeated row |
| English Language | 108 | clean |
| Français intensif | 131 | repeated reading slots (not mistakes), 1 cut title |
| French | 79 | repeated activity types (not mistakes) |
| Geography | 47 | practical numbered twice; header “Geography Ok” |
| History | 41 | clean |
| Logic | 26 | **new in Form 3**; clean (subject name only) |
| Mathematics | 76 | 1 cut title |
| Physics | 37 | clean |

**G1 for Form 3:** number Form 3 lessons by their place in the year, as approved for Form 2.

## What the 11 “errors” really are

Most are the same activity on purpose, week after week, not slips:

| # | Subject | What the sheet has | Proposal |
|---|---|---|---|
| 1 | Français intensif | “Initiation à la littérature : lecture d’une œuvre au programme” on about 35 rows across the year | Keep them all: it is the weekly reading of the set book. In the app they become “reading the set book” sessions (the book itself is not in the app) |
| 2 | Français intensif | “Expression orale : saynètes” twice (rows 88 and 101) | Keep both: two drama sessions |
| 3 | French | “Expression orale : interprétation d’images” twice and “Lecture : texte adossé au module” twice in one module (rows 38/47, 39/44) | Keep all: the same kind of activity with different material |
| 4 | Economics | Row 4 repeats row 3 (“Lesson 2: Introduction to the tools of economic analysis”), same dates | Keep both as Part 1 and Part 2 of the lesson (two periods) |

## Real slips

| # | Subject | What the sheet has | Proposed fix |
|---|---|---|---|
| 5 | Français intensif | Row 24 is cut off: “Lecture suivie d’une œuvre au” | Complete it: “… d’une œuvre au programme” (as on row 23) |
| 6 | Mathematics | Row 50 is cut off: “Cartesian product A×B and” | Write “Cartesian product A×B” (or send the full title if the syllabus has more) |
| 7 | Geography | Row 6 is “PW1: Locate a place on a map” again (row 4 is PW 1 with the same title) | Call it “PW 1 (continued)”; header “Geography Ok” → “Geography” |
| 8 | Biology | Row 22 “Claasification: Integration” | Spell it “Classification: Integration” |
| 9 | Chemistry | Row 13 “Alkaline metals and Halogens” after row 12 “Alkali metals and halogens” | Keep two lessons; write row 13 as “Alkaline earth metals and halogens” (the usual name) |
| 10 | Accounting, Logic, Français intensif | Subject names not yet known to the reader | Add them as subjects: accounting, logic, français intensif |

(The reader also flagged “singleton” in Mathematics row 43 as a word with missing letters: it is a real word, no change.)

To approve, reply “approve all”, or name the numbers you want changed.
