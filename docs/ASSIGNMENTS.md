# Who writes what (decided by Dion, 2026-10-23)

Order: **Term 1 of every class first.** Split by class and subject so no two authors touch the same files.
Rules: `docs/AUTHORING.md`. Each author logs in `docs/log/<author>.md`.

## Size of the job (Term 1 lesson rows, from the spines)

| Class | Term 1 rows | Listed in content/classes.json |
|---|---|---|
| Form 3 | 294 | yes |
| Form 4 | 469 | yes |
| Form 5 | 449 | yes |
| Lower Sixth | 801 | yes |
| Upper Sixth | 897 | yes |

About 2,900 Term 1 rows in all (some sixth-form sheets look inflated by the parser; see each `issues.md`).
At the pace so far (30–50 good lessons per author per long session), Form 3 Term 1 is a few sessions per author;
everything to Upper Sixth Term 1 is many weeks of steady work. Quality first: a thin lesson does not teach.

## Now: Form 3, Term 1

| Author | Subjects (Term 1 rows) | Branch / folder |
|---|---|---|
| **Claude** | Maths (34), Physics (17), Chemistry (24), Biology (16), Computer Science (26), Accounting (9) | `f3-claude`, `C:\Users\efuet\preps` |
| **Codex** | English (39), French (30), Français intensif (49), History (18), Geography (13), Economics (11), Logic (8) | `f3-codex`, `C:\Users\efuet\preps-codex` |
| **ChatGPT** | Learn screens for the **Form 1** lessons in the live app, every subject except Maths and Physics (numbers must be computed, so Claude writes those) | text only; pasted in by Claude or Codex |

Every new lesson has Learn screens. Subject ids: `f3-<folder>` (`content/classes.json`); lesson files
`content/form-3/<folder>/<seq>.json`; template ids start with the subject's `ids` prefix (m3-, e3-, fr3-, fi3-, y3-, g3-, n3-, l3-, …).

## ChatGPT: Learn screens for Form 1 (the live app)

Pupils said the lessons go too fast from a short definition to questions. Every Form 1 lesson gets Learn screens.
Use the prompt in `docs/prompts/chatgpt-learn.md`: paste one lesson's JSON, get back a `learn` JSON. Save the reply as
`.handoff/learn/<subject>-<n>.json`, then whoever has the repository runs:

```bash
python tools/content/add_learn.py content/<subject>/<n>.json .handoff/learn/<subject>-<n>.json
```

and `npm test`. Form 1 changes stay on `form-2` until Dion approves them for the live app (`main`).

## Form 4 continuation and next classes

- **Codex: Form 4 Term 1 Logic, Economics, English, History, Geography, French and Français intensif**, authorised by Dion on 2026-10-23 after the available Form 3 rows and the requests to continue to the next subject.
  Continue in `C:\Users\efuet\preps-codex` on `f3-codex`; generators belong in `tools/authoring/form4/`.
  Keep the established lesson sequence and add a visible measurable end goal, earlier knowledge and next-topic
  connection to each opening Learn screen. See `content/form-4/logic/LEARNING-PATH.md`.

- **Claude: Form 4 Term 1 Maths (35), Additional Maths (57), Physics (15), Chemistry (27), Biology (31),
  Human Biology (30), Geology (28), Computer Science (27), Accounting (9), Food and Nutrition (9)**: the same split
  as Form 3 (numbers and sciences), set 2026-10-23 once Form 3 Term 1 was merged into `form-2`. Branch `f3-claude`
  in `C:\Users\efuet\preps`; generators in `tools/authoring/form4/`; the same opening goal screen as Codex's.
- **Codex: the other Form 4 subjects** (English, French, Français intensif, History, Geography; Literature waits
  for the set books, AUTHORING section 6). Dion can move any subject between authors.
- **Codex, authorised by Dion on 2026-10-24:** Form Five Term One English, French, Français intensif, History, Geography, Economics and Logic; then Lower Sixth Term One English, French, Français intensif, African History, Cameroon History, World History, Geography, Economics and Philosophy; then Upper Sixth Term One English, French, Français intensif, Cameroon History, World History, Geography, Economics and Philosophy. Literature in English may be handled with prescribed-text rows held for teacher feedback until books/editions are confirmed.
  Work through Form Five first, then Lower Sixth, then Upper Sixth, completing and pushing each subject after tests and browser checks. Keep the existing ownership split for Maths/sciences/technical subjects. Generators stay in the relevant `tools/authoring/<class>/` folder. Unclear sheet titles and prescribed books remain teacher-feedback items; do not invent corrections or replacements.
- Codex: bring Form 2 Term 3 French (70–81) and Français intensif (104–128) up to the quality bar (4+ questions,
  specific feedback, 3+ variants, Learn screens) when Form 3 is done.
  French 70–81 and Français intensif 104–128 upgraded on 2026-10-24; both assigned Term Three quality batches are complete as drafts pending teacher review.

## Codex coverage and teacher feedback (2026-10-24)

- The earlier completed batches contain 348 written drafts, including guided practicals, and 74 explicitly deferred teaching rows. No assigned teaching row is unaccounted for; diagnostic rows remain excluded under AUTHORING.md.
- Form Four Literature foundations 2/19 are drafted using original examples. Text-specific rows await teacher feedback on books/editions. Form Three/Four Français intensif prescribed-text rows and the three ambiguous Form Three French titles also remain deferred.
- Dion requested that unresolved book choices and titles be kept for teacher feedback. Collect decisions in the subject TEACHER-REVIEW.md files; do not guess replacements or mark them approved.
- The earlier-batch coverage and row-by-row feedback list is [CODEX-CONTENT-STATUS.md](CODEX-CONTENT-STATUS.md). Run `python tools/authoring/audit_codex_scope.py` to refresh that baseline. The new Form Five/Sixth assignment above is additional work and is not counted as complete in the 348-draft baseline.

- Form Five English Term One: 31 teaching drafts (rows 2–32) completed on 2026-10-24 with goals/connections, writing models and teacher notes; diagnostic row 1 excluded. This adds to the earlier baseline.
- Form Five Logic Term One: nine teaching rows plus screen-based guided work 6 (ten drafts, rows 1–10) completed on 2026-10-24. Explicit existence conventions and local eduction terminology require teacher review.
- Form Five Economics Term One: fourteen lesson rows plus practicals 5/15 and guided work 17 (seventeen drafts) completed on 2026-10-24. Further-study 11/18 excluded by row policy; current parameters and teacher approval are not claimed. Form Five now has 58 new drafts across English, Logic and Economics; French, Français intensif, History and Geography remain.
- Form Five French Term One: 29 parsed teaching drafts completed on 2026-10-24. Row 3 has a vocabulary title but integration classification; TR-french-1 records the discrepancy for teacher/integrator review. Integrations remain excluded. Form Five now has 87 new drafts across four subjects; Français intensif, History and Geography remain.
- Form Five Français intensif Term One: thirty active language drafts and twenty explicit prescribed-text deferrals completed on 2026-10-24. Integrations excluded. Form Five now has 117 drafts across five subjects, with History and Geography still to author; books remain teacher-feedback items.
