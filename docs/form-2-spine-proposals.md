# Form 2 curriculum: fixes to the sheets

**Status: approved by Dion on 2026-10-17 (“approve all”) and applied** as overrides in `data/spine/form-2/overrides/`
(each with its reason and “approved by Dion”). After the fixes every Form 2 subject has 0 errors. Proposal G1 is applied
by `python tools/spine/build.py --class form-2`: slips in the sheets' own lesson numbers are reported as info only.

The 11 Form 2 progression sheets were read by `python tools/spine/build.py --class form-2` into
`data/spine/form-2/` (report: `data/spine/form-2/issues.md`). As for Form 1, nothing is changed until approved;
each approved fix becomes a logged override (reason + approved by Dion), and the sheets themselves stay untouched.

## Subjects found

| Subject | Rows | Notes |
|---|---|---|
| Accounting | 27 | new in Form 2; clean |
| Biology | 67 | 2 fixes below |
| Chemistry | 60 | 1 fix below |
| Computer Science | 55 | 1 fix below |
| English Language | 104 | Term 3 heading missing |
| Français intensif | 130 | new in Form 2; 2 fixes below |
| French | 85 | 2 fixes below |
| Geography | 27 | a block printed in the wrong term |
| History | 22 | 3 fixes below |
| Mathematics | 69 | 1 fix below |
| Physics | 36 | clean |

**Not in the folder:** Home Economics (Form 1 had it). Is it taught in Form 2?

## The main proposal: number Form 2 lessons by their place in the year

Many errors are only about the lesson **numbers** on the sheets: the same number twice, numbers going backwards,
numbers missing, or a lesson split over two rows with one number (Part 1 / Part 2). Geography, History and Biology in
Form 1 already use the row's place in the year instead. **Proposal G1:** do this for every Form 2 subject. That alone
clears 17 of the 26 errors, and the rest are the real slips below.

## Real slips on the sheets

| # | Subject | What the sheet has | Proposed fix |
|---|---|---|---|
| 1 | Biology | Row 38 “1ST BREAK” | Delete: it marks the holiday, it is not a lesson |
| 2 | Biology | Row 39 “Lesson 50: Management of solid wastes”, dated 14–18 Dec inside “Nutrition related diseases” | Keep it where the sheet dates it; flag for the Biology teacher (it may belong to a later chapter) |
| 3 | Chemistry | Row 53 “Techniques for separation: review” repeats row 41, in Term 3 | Keep it as a revision row (reuses earlier lessons, no new lesson) |
| 4 | Computer Science | Rows 21–24 (Lessons 32–35, dated 25 Jan–12 Feb) are printed inside Term 1 | Move them into Term 2 after Lesson 31, by their dates and numbers |
| 5 | English | No “Term 3” heading | Start Term 3 at row 77 (8 March, as on the other sheets) |
| 6 | Français intensif | Row 68 repeats row 62 (“Conjugaison : Le passé simple”) | Delete row 68 |
| 7 | Français intensif | Rows 105–107 titles begin “101.”, “102.”, “103.” | Remove the stray numbers from the titles |
| 8 | French | Row 38 repeats row 36 (adjective agreement, revision) | Delete row 38 |
| 9 | French | Rows 70–71 repeat rows 49–50 exactly | Delete rows 70 and 71 |
| 10 | Geography | Rows 11–18 (“Towns in Africa” chapter, dated 8 Mar–21 May) are printed inside Term 1, and there is no “Term 3” heading | Move them to the end and make them Term 3 |
| 11 | Geography | Header reads “Geography Ok” | Rename to “Geography” (as approved for Form 1) |
| 12 | History | Row 8 is the second part of row 6 (“… continues and ends”) but comes after the further study in row 7 | Put row 8 straight after row 6 |
| 13 | History | Row 18 (Lesson 11) comes before row 19 (Lesson 10) | Swap them |
| 14 | History | Row 22 title starts “;Lesson 14:” | Clean the title: “The Americas: The Rise, Peak and Decline of the Inca, Maya and Aztec” |
| 15 | Mathematics | Row 14 “ordinate, origin,” is a broken piece of row 13 | Delete row 14 (row 13 already has the full title) |

To approve, reply “approve all”, or name the numbers you want changed.
