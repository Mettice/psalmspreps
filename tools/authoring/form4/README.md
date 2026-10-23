# Form Four authoring

Follow docs/AUTHORING.md and the reference maths generator. Work only in the authorised worktree/branch and stage explicit paths. Keep generators here.

Dion requested the established lesson format plus visible purpose and connections (2026-10-23). Every new lesson's opening Learn section therefore states:

- **By the end:** an observable action, such as classify, translate, calculate or justify.
- **Builds on:** the specific earlier idea needed; connect to numbered prerequisites where available.
- **Leads to:** how the skill will be used in a later topic or a meaningful task.

Follow with actual explanations, worked reasoning and practice that assesses the stated action. Avoid an empty goal such as understand the topic. Keep within the existing four-section/word limits; no engine or interface changes are needed.

Logic example:

```text
python tools/authoring/form4/logic.py
node --test tools/authoring/form4/logic.test.mjs
node tools/authoring/form3/check_quality.mjs f4-logic
npm test
npm run review -- f4-logic
node tools/prototype/build.mjs
node tools/authoring/form4/walk_subject.cjs f4-logic
```

Do not commit the generated prototype HTML. LEARNING-PATH.md and TEACHER-REVIEW.md live with the subject content. The phone browser check verifies visible goals/connections, every lesson flow and the rendered Venn example.
