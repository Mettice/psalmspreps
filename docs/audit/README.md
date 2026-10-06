# Subject audit: the 9 non-Maths subjects

Audit only: no lesson content was written. One file per subject, plus this summary. Regenerate with `python tools/audit/build_audit.py` (judgements in `tools/audit/audit_data.py`).

## Method

Every spine row is either **teachable** (lesson, practical, group work, further study, guided work) or **reuse** (integration, evaluation, remediation, catch-up: mixed review, no new items). Each teachable row gets one class, by the main kind of practice it allows:

- **C** computed: code verifies? yes: code computes the answer
- **F** fact table: code verifies? yes: against an authored table
- **A** authored: code verifies? yes: against an authored key
- **X** paper-only: code verifies? no: self-check against a model answer
- **D** deferred: code verifies? no: needs audio or equipment

**% templatable** below has two figures: *computed* (C, answers worked out by code, as in Maths) and *code-generated* (C + F: code also builds questions from an authored fact table, so one reviewed table gives many variants).

**P1 estimate** per teachable row: C = 2, F = 4, A = 7, X = 3, D = 0 (later), plus 1 per drawn diagram or map, plus the subject's open conventions. Calibration: Maths Lessons 0–16 were mostly C and produced 24 P1 items, about 1.5 per lesson, so C = 2 errs on the high side. These are estimates for planning, not counts.

## Summary

| Subject | Teachable rows | Computed (C) | Code-generated (C+F) | Authored (A) | Paper-only (X) | Deferred (D) | Est. P1 | P1 per row | Drawn SVG | Maps | Code-drawn | Drawn files (est.) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Chemistry](chemistry.md) | 53 | 9 (17%) | 39 (74%) | 13 | 1 | 0 | ~243 | 4.6 | 8 | 0 | 7 | ~64 KB |
| [Physics](physics.md) | 39 | 9 (23%) | 26 (67%) | 13 | 0 | 0 | ~193 | 4.9 | 13 | 0 | 7 | ~104 KB |
| [French](french.md) | 75 | 33 (44%) | 46 (61%) | 23 | 2 | 4 | ~295 | 3.9 | 5 | 0 | 1 | ~40 KB |
| [Geography](geography.md) | 25 | 6 (24%) | 15 (60%) | 8 | 2 | 0 | ~123 | 4.9 | 8 | 2 | 4 | ~144 KB |
| [Home Economics](home-economics.md) | 47 | 0 (0%) | 28 (60%) | 19 | 0 | 0 | ~260 | 5.5 | 13 | 0 | 1 | ~104 KB |
| [Computer Science](computer-science.md) | 42 | 6 (14%) | 22 (52%) | 18 | 1 | 1 | ~216 | 5.1 | 10 | 0 | 3 | ~80 KB |
| [English language](english-language.md) | 101 | 19 (19%) | 41 (41%) | 27 | 20 | 13 | ~380 | 3.8 | 2 | 0 | 4 | ~16 KB |
| [History](history.md) | 28 | 1 (4%) | 9 (32%) | 17 | 2 | 0 | ~165 | 5.9 | 1 | 3 | 0 | ~128 KB |
| [Biology](biology.md) | 44 | 1 (2%) | 12 (27%) | 27 | 5 | 0 | ~261 | 5.9 | 9 | 0 | 2 | ~72 KB |
| **Total** | 454 | 84 | 238 | 165 | 33 | 18 | ~2136 | | 69 | 5 | 29 | ~752 KB |

Sorted by code-generated %. Shared diagrams are counted once per subject, so the size total overstates a little (see Shared assets).

## Rankings

**By % templatable (code-generated, then computed)**

1. Chemistry: 74% code-generated, 17% computed
2. Physics: 67% code-generated, 23% computed
3. French: 61% code-generated, 44% computed
4. Geography: 60% code-generated, 24% computed
5. Home Economics: 60% code-generated, 0% computed
6. Computer Science: 52% code-generated, 14% computed
7. English language: 41% code-generated, 19% computed
8. History: 32% code-generated, 4% computed
9. Biology: 27% code-generated, 2% computed

**By P1 load per teachable row (lightest first)**

1. English language: 3.8 per row, ~380 in total
2. French: 3.9 per row, ~295 in total
3. Chemistry: 4.6 per row, ~243 in total
4. Geography: 4.9 per row, ~123 in total
5. Physics: 4.9 per row, ~193 in total
6. Computer Science: 5.1 per row, ~216 in total
7. Home Economics: 5.5 per row, ~260 in total
8. History: 5.9 per row, ~165 in total
9. Biology: 5.9 per row, ~261 in total

**By asset needs (lightest first: drawn files, then audio-deferred rows)**

1. English language: ~16 KB drawn (diagrams: 2, maps: 0), deferred rows: 13
2. French: ~40 KB drawn (diagrams: 5, maps: 0), deferred rows: 4
3. Chemistry: ~64 KB drawn (diagrams: 8, maps: 0), deferred rows: 0
4. Biology: ~72 KB drawn (diagrams: 9, maps: 0), deferred rows: 0
5. Computer Science: ~80 KB drawn (diagrams: 10, maps: 0), deferred rows: 1
6. Physics: ~104 KB drawn (diagrams: 13, maps: 0), deferred rows: 0
7. Home Economics: ~104 KB drawn (diagrams: 13, maps: 0), deferred rows: 0
8. History: ~128 KB drawn (diagrams: 1, maps: 3), deferred rows: 0
9. Geography: ~144 KB drawn (diagrams: 8, maps: 2), deferred rows: 0

**Reading the P1 ranking.** English and French look light per row only because 33 English rows and 6 French rows are paper-only or deferred, and those count little or nothing for now. In absolute terms they are the two heaviest subjects. Across all 9 subjects the estimate is roughly 2,100 P1 items, against 24 for Maths Lessons 0–16: most of the new work is facts that a person must check, not answers code can compute.

## Engine gaps across subjects

| Gap | What it is | Needed by | Size of work |
|---|---|---|---|
| Matching, sort into groups | Pair items, or sort them into 2–4 groups; tap-tap at 360px, no drag | all 9 | small |
| Fact-table templates | Questions drawn from an authored table; distractors from other rows (extends `pool`) | all 9 | small–medium |
| Labelling | SVG with numbered pins; pick a name for each pin | all 9 | medium |
| Cloze | Typed word in a gap; accepted answers; case, apostrophe and accent policy | English, French, some sciences | small |
| Paper-only flow | Task, model answer, checklist; not counted toward mastery; listed for a grown-up | 8 | small (needs a Phase 3 spec decision) |
| Units library | Mass, volume, time, temperature, SI prefixes (today `convert` is length only) | Chemistry, Physics | small |
| Instrument renderers | Code-drawn ruler, balance, cylinder, thermometers, pH scale, pie chart, with computed readings | Chemistry, Physics, Biology | medium |
| Geography library | Local time, latitude/longitude, grid references, scale; code-drawn grid map and climograph | Geography | medium |
| Dates library + timeline | BC/AD without year 0, centuries, ordering from an authored date table | History | small |
| English morphology | -s, -ing, -ed, plurals, comparatives, contractions, question tags, a/an + exception tables | English | medium |
| French morphology | Conjugation, agreement, elision, numbers in words + exception tables; French UI strings | French | medium–large |
| Reading passage type | One passage, several questions | English, French | small (the passages are the big job) |
| Mini interpreter, spreadsheet, folder tree, URL parser | Reuse `expr.js` | Computer Science | medium |
| Picture options in MCQ | Choices that are images | Home Economics, Biology, Physics | small |
| Audio | Playback of recorded sounds | English (13 rows), French (3 rows + parts) | small code, large size: deferred |
| Block editor | Drag-free block programming | Computer Science (1 row) | large: deferred or paper |

## Shared assets and content (write once)

- Lab equipment set: Biology 6, Chemistry 3–4, Physics 5.
- Hazard symbols: Chemistry 5, Physics 19.
- Particle diagrams and change-of-state table: Chemistry 11, Physics 11–12.
- Water sources, pollution, water cycle: Biology 49–50, Chemistry 49–50 and 56, Geography 20.
- Food classes: Biology 42, Home Economics 3.
- Climate change: Physics 36, Geography 21, English 86.
- Waste sorting: Geography 16, Home Economics 42–43.
- Egyptian and Hindu-Arabic numerals: History 14 and 23, Maths Lessons 1 and 3.
- Computer parts: Computer Science 21, French 75.

## Decisions needed (for Dion)

1. **Audio:** an optional audio pack downloaded once, or speech and listening rows done with a grown-up from a printed list? (English 13 rows, French 3+.)
2. **Paper-only work** (writing, speaking, practicals, field work): shown in the app with a model answer and checklist and listed in the parent summary, but not counted toward mastery?
3. **Sensitive content** (Biology 37–41; History 6, 10, 24–28): parent preview before it unlocks?
4. **Block programming** (Computer Science 35): build a tiny block editor, or keep it on paper?
5. **Order of subjects:** the rankings suggest Physics and Chemistry next (computable measurement block, fact tables, low asset cost), then Geography (computable, but maps). English and French have the largest computed grammar share but also the heaviest authoring (original reading texts) and the audio question. This is a judgement, not a measured result.

Nothing here changes content: no lesson has been written for these subjects. Still in force: no new content until the Lesson 3 test results come back.
