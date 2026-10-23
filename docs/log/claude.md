# Claude log

## 2026-10-23

- Checked Codex's work (commits 39335f6, e21ef66, 25b0290): tests 4465/4465; 37 new French/FI lessons walk clean (31 at once, 6 paper-task lessons after adding French button labels to the walker). Correct but thinner than the bar: 3 questions per lesson, about 2 variants each, half the wrong options share one feedback line, notes ~75 words. Codex did not write its handoff log.
- Learn screens (engine, app, teacher review, tests); samples Form 2 Maths 55, French 72.
- Installed app: subject libraries moved out of the core page (379 KB to 189 KB).
- content/classes.json + tools/classes.mjs: Form 3 subjects; lessons found from files; generic tests and review.
- Form 3 Maths row 2 (reference lesson). Spines for Forms 4, 5, Lower and Upper Sixth.
- Not checked: the new spines against the sheets by eye (see each issues.md).

## 2026-10-23 (afternoon), branch f3-claude

- Form 3 Maths Term 1 complete: rows 2–34 (33 lessons; row 1 is "contact and diagnostic", not a lesson). Every lesson has
  Learn screens, 3 cards, a worked example and 5 practice questions with levels 1–3. 209 content tests pass (1000 seeds per
  question); the browser walk is 33/33 clean, with width checked at 360 px on every screen.
- maths2.js additions (tested): sinD/cosD/tanD and their inverses, log10, logb, 2 × 2 matrix operations, matStr, matFig,
  trigFig, thalesFig.
- Found and fixed my own bug before committing: roundTo(x, 2) rounds to the nearest 2, not to 2 decimal places. The unit form
  roundTo(x, 0.01) is correct, and no earlier content had the mistake.
- Not checked: none of this has had a subject teacher's review (see content/form-3/maths/TEACHER-REVIEW.md, TR-M3-1 to TR-M3-13).

## 2026-10-23 (evening), branch f3-claude

- Form 3 Term 1 is complete for my subjects. Each was walked clean at 360 px:
  - Physics: 17 lessons;
  - Chemistry: 24;
  - Biology: 18;
  - Computer Science: 26;
  - Accounting: 9 (rows 1–8 and 10).
  Integration-activity rows are not written as lessons. 753 content tests pass.
- Accounting: account numbers in cards and Learn screens are fixed text. Bank-item data stays plain.
  Caught and fixed before committing:
  - a floating-point answer (× 1.1925, now × 11925 / 10000);
  - a confusing due-date prompt.
- Not checked: no subject teacher has reviewed any of this yet. The SYSCOHADA account numbers and the VAT simplifications are listed in
  content/form-3/accounting/TEACHER-REVIEW.md (TR-A3-1 to TR-A3-6).
