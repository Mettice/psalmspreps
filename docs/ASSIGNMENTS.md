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

- **Codex: Form 4 Term 1 Logic, Economics and English**, authorised by Dion on 2026-10-23 after the available Form 3 rows and the request to continue to the next subject.
  Continue in `C:\Users\efuet\preps-codex` on `f3-codex`; generators belong in `tools/authoring/form4/`.
  Keep the established lesson sequence and add a visible measurable end goal, earlier knowledge and next-topic
  connection to each opening Learn screen. See `content/form-4/logic/LEARNING-PATH.md`.

- Remaining Form 4 subjects and Forms 5, Lower and Upper Sixth Term 1: listed in `content/classes.json`
  (cinema subjects excepted); subject ownership is still to be split. Sheet errors in each class's `issues.md`
  need Dion's decisions first.
- Codex: bring Form 2 Term 3 French (70–81) and Français intensif (104–128) up to the quality bar (4+ questions,
  specific feedback, 3+ variants, Learn screens) when Form 3 is done.
