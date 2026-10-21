# Subject activity pilots

These twelve draft activities appear after the worked example and before ordinary practice. Other lessons retain their existing sequence. Each stage uses the existing question engine, retry help, saved progress and targeted review.

| Subject | Pilot | Activity |
|---|---|---|
| Maths | Form 1, lesson 7 | Complete missing BODMAS working, then solve a new calculation independently |
| Accounting | Form 2, lesson 1 | Complete assets and capital working, then evaluate another business |
| Physics | Form 1, lesson 16 | Predict water displacement, read a cylinder diagram, explain the subtraction |
| Chemistry | Form 1, lesson 8 | Predict thermometer behaviour, inspect the reading, explain eye position |
| Biology | Form 1, lesson 13 | Compare cell diagrams and link structures to their functions |
| History | Form 1, lesson 2 | Examine an explicitly invented classroom source, select a supported claim, recognise limits |
| Geography | Form 1, lesson 5 | Read a grid map, select a nearer destination, justify with grid distances |
| English | Form 1, lesson 13 | Read a travel dialogue, practise the structure, write an original sentence |
| French | Form 1, lesson 3 | Read introductions, practise the structure, introduce an imaginary character |
| Français intensif | Form 2, lesson 1 | Compare adjectives in a dialogue, then write an original sentence |
| Computer Science | Form 1, lesson 11 | Complete a trace, predict output, repair a repetition error |
| Home Economics | Form 1, lesson 20 | Choose and sequence household tasks, then justify the plan |

## Content format

`activity` contains a draft status, title, and ordered `stages`. Each stage has a title and an inline `question` using the existing question template schema. Question IDs must be unique within the lesson, including cards and ordinary practice. Numeric missing working uses `blanks`.

An optional `reflection` uses the existing paper task schema: prompt, model answer, checklist, variables and checks. It supplements ordinary practice. The pupil writes in an exercise book before seeing the model, then ticks a self-check list. Original writing is not automatically marked. Its completion and ticks appear separately in copied results.

Teacher review mode includes every activity stage and reflection. Activities remain drafts pending subject-teacher review. Keep the next rollout limited until teachers have checked correctness, language, difficulty and whether the stages fit the lesson.

Validation: `node --test tests-js/activities.test.js`, followed by `npm test` and `npm run build:site`.
