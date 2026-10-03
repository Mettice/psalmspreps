# Authored answers for review (Maths Form 1, Lessons 1–16: practice and teach-card checks)

These 19 templates have answers fixed by the author (facts, definitions, notation), not computed by code.
Each one lists every variant a pupil can see, the answer the app accepts, the feedback for each wrong choice, and the sources.
Letters such as P and Q are drawn at random in the app; one sample is shown here.

Regenerate with `node tools/content/render_authored.mjs`.

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `m1-zero-symbol` | 1 | mcq, 1 | hindu-arabic, roman-no-zero, egyptian, tally |
| 2 | `m1-digits-origin` | 1 | mcq, 1 | hindu-arabic |
| 3 | `m1-sixty` | 1 | mcq, 1 | babylonian |
| 4 | `m6-classify` | 6 | mcq, 1 | number-roles |
| 5 | `c6-1-check` (card c6-1) | 6 | mcq, 1 | number-roles |
| 6 | `m11-notation` | 11 | mcq, 1 | line-notation |
| 7 | `m11-end-points` | 11 | numeric, 1 | line-notation |
| 8 | `m11-true` | 11 | mcq, 2 | line-notation, one-line-two-points |
| 9 | `m11-spot` | 11 | spot_error, 3 | line-notation |
| 10 | `c11-3-check` (card c11-3) | 11 | mcq, 1 | line-notation |
| 11 | `m12-facts` | 12 | mcq, 1 | one-line-two-points |
| 12 | `m14-converse` | 14 | mcq, 3 | midpoint |
| 13 | `c14-3-check` (card c14-3) | 14 | mcq, 1 | midpoint |
| 14 | `m15-steps` | 15 | ordering, 2 | perpendicular-bisector |
| 15 | `m15-spot` | 15 | spot_error, 3 | perpendicular-bisector |
| 16 | `c15-1-check` (card c15-1) | 15 | mcq, 1 | perpendicular-bisector |
| 17 | `m16-symbol` | 16 | mcq, 1 | line-symbols |
| 18 | `m16-through-point` | 16 | numeric, 1 | parallel-postulate, one-perpendicular |
| 19 | `c16-2-check` (card c16-2) | 16 | mcq, 1 | line-symbols |

## 1. `m1-zero-symbol` (Lesson 1: The history and evolution of numbers)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| Which number system gave us a symbol for zero? | **Hindu-Arabic numerals** | Roman numerals: _The Romans had no symbol for zero. Zero as a number came from India._<br>Egyptian numerals: _Egyptian numerals had no place value, so they did not need a zero digit to hold empty places._<br>Tally marks: _Tally marks only count things that are there; they have no mark for zero._ |

**Full working shown after a second miss** (sample):

> Zero as a number came from India, with the Hindu-Arabic digits. Roman numerals and tally marks have no zero, and Egyptian numerals had no place value, so they did not need a zero digit to hold empty places.  
> Answer: Hindu-Arabic numerals.  

**Sources**

- [Encyclopaedia Britannica, 'Hindu-Arabic numerals'](https://www.britannica.com/topic/Hindu-Arabic-numerals). Supports: The digits originated in India (6th or 7th century) and reached Europe through Middle Eastern mathematicians such as al-Khwarizmi. The Hindus were the first to use zero in the modern way. _Checked: Search-result summary of the page (the page itself could not be opened)._
- [Encyclopaedia Britannica, 'Is It Still Important to Learn Roman Numerals?'](https://www.britannica.com/story/is-it-still-important-to-learn-roman-numerals). Supports: Zero cannot be written with Roman numerals. _Checked: Search-result summary of the page (the page itself could not be opened)._
- [Encyclopaedia Britannica, 'Mathematics in ancient Egypt'](https://www.britannica.com/science/mathematics/Mathematics-in-ancient-Egypt). Supports: Separate symbols for 1, 10, 100, 1000 and so on, each repeated as often as needed (an additive system with no place value); 1000 is a lotus flower. Wording approved by Dion 2026-10-03: 'Egyptian numerals had no place value, so they did not need a zero digit to hold empty places.' _Checked: Search-result summary of the page (the page itself could not be opened)._
- Definition of tally marks. Supports: One mark is made for each object counted, so there is no mark for zero. _Checked: Not externally sourced._

Decision: ☐ approve ☐ change: ____________

## 2. `m1-digits-origin` (Lesson 1: The history and evolution of numbers)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| The digits 0 to 9 that we use today first came from: | **India** | Rome: _Our digits are called Hindu-Arabic numerals: they came from India, and Arab traders and scholars spread them._<br>Egypt: _Our digits are called Hindu-Arabic numerals: they came from India, and Arab traders and scholars spread them._<br>Babylon: _Our digits are called Hindu-Arabic numerals: they came from India, and Arab traders and scholars spread them._ |

**Full working shown after a second miss** (sample):

> Our digits are called Hindu-Arabic numerals: they first came from India, and Arab traders and scholars carried them to other lands.  
> Answer: India.  

**Sources**

- [Encyclopaedia Britannica, 'Hindu-Arabic numerals'](https://www.britannica.com/topic/Hindu-Arabic-numerals). Supports: The digits originated in India (6th or 7th century) and reached Europe through Middle Eastern mathematicians such as al-Khwarizmi. The Hindus were the first to use zero in the modern way. _Checked: Search-result summary of the page (the page itself could not be opened)._

Decision: ☐ approve ☐ change: ____________

## 3. `m1-sixty` (Lesson 1: The history and evolution of numbers)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| The Babylonians counted in groups of sixty. Where do we still use groups of sixty today? | **There are sixty minutes in one hour.** | There are sixty days in one month.: _Time still uses the Babylonian sixty: sixty seconds in a minute and sixty minutes in an hour._<br>There are sixty centimetres in one metre.: _Time still uses the Babylonian sixty: sixty seconds in a minute and sixty minutes in an hour._<br>There are sixty months in one year.: _Time still uses the Babylonian sixty: sixty seconds in a minute and sixty minutes in an hour._ |

**Full working shown after a second miss** (sample):

> The Babylonian base-sixty (sexagesimal) system is why we still count sixty seconds in a minute and sixty minutes in an hour.  
> Answer: There are sixty minutes in one hour.  

**Sources**

- [Any reliable history-of-mathematics source on the Babylonian sexagesimal (base-60) system, e.g. Encyclopaedia Britannica, 'Cuneiform numeral'](https://www.britannica.com/topic/cuneiform-numeral). Supports: The Babylonians used a base-60 (sexagesimal) system, which is the origin of 60 minutes in an hour and 60 seconds in a minute. _Checked: Fact approved by Dion 2026-10-03 (TR-D02): any reliable history-of-mathematics source is acceptable; no specific article is required._

Decision: ☐ approve ☐ change: ____________

## 4. `m6-classify` (Lesson 6: Cardinal, Ordinal and Nominal numbers)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| In the sentence “There are 38 pupils in Form One B.”, the number is: | **cardinal** | ordinal: _An ordinal number gives a position: 1st, 2nd, 3rd… Here the number is cardinal._<br>nominal: _A nominal number is only a label, like a phone or taxi number. Here the number is cardinal._ |
| In the sentence “Ngwa bought 38 oranges at the market.”, the number is: | **cardinal** | ordinal: _An ordinal number gives a position: 1st, 2nd, 3rd… Here the number is cardinal._<br>nominal: _A nominal number is only a label, like a phone or taxi number. Here the number is cardinal._ |
| In the sentence “Ewane finished 1st in the inter-class race.”, the number is: | **ordinal** | cardinal: _A cardinal number answers 'how many?'. Here the number is ordinal._<br>nominal: _A nominal number is only a label, like a phone or taxi number. Here the number is ordinal._ |
| In the sentence “Today is the 1st day of the month.”, the number is: | **ordinal** | cardinal: _A cardinal number answers 'how many?'. Here the number is ordinal._<br>nominal: _A nominal number is only a label, like a phone or taxi number. Here the number is ordinal._ |
| In the sentence “The number painted on the taxi is 574.”, the number is: | **nominal** | cardinal: _A cardinal number answers 'how many?'. Here the number is nominal._<br>ordinal: _An ordinal number gives a position: 1st, 2nd, 3rd… Here the number is nominal._ |
| In the sentence “Bih wears shirt number 1 in the school football team.”, the number is: | **nominal** | cardinal: _A cardinal number answers 'how many?'. Here the number is nominal._<br>ordinal: _An ordinal number gives a position: 1st, 2nd, 3rd… Here the number is nominal._ |

**Full working shown after a second miss** (sample):

> Does the number count something? Cardinal. Does it give a position? Ordinal. Is it only a label? Nominal.  
> Here the number is ordinal.  

**Sources**

- Standard school definitions of cardinal, ordinal and nominal numbers. Supports: Cardinal: how many. Ordinal: position or order. Nominal: a label that does not count anything (phone, taxi or shirt number). _Checked: Not externally sourced: compare with the pupil's textbook._

Decision: ☐ approve ☐ change: ____________

## 5. `c6-1-check` (Lesson 6: Cardinal, Ordinal and Nominal numbers)

Type: mcq, level 1.

**Which sentence uses a cardinal number (a number that tells how many)?** (choose the TRUE statement; the app shows 1 true and 3 false, picked at random)

| Statement | True or false (as authored) | Feedback |
|---|---|---|
| There are 40 pupils in the class. | true | |
| Ngwa has 40 goats. | true | |
| Enow came 1st in the race. | **false** | 1st gives a position: it is an ordinal number. |
| The number painted on the taxi is 574. | **false** | A taxi number is only a label: it is a nominal number. |
| Bih wears shirt number 1. | **false** | A shirt number is only a label: it is a nominal number. |

**Full working shown after a second miss** (sample):

> The true statement is “There are 29 pupils in the class.”.  
> “Enow came 4th in the race.” is false: 4th gives a position: it is an ordinal number.  
> “Bih wears shirt number 4.” is false: A shirt number is only a label: it is a nominal number.  
> “The number painted on the taxi is 584.” is false: A taxi number is only a label: it is a nominal number.  

**Sources**

- Standard school definitions of cardinal, ordinal and nominal numbers. Supports: Cardinal: how many. Ordinal: position or order. Nominal: a label that does not count anything (phone, taxi or shirt number). _Checked: Not externally sourced: compare with the pupil's textbook._

Decision: ☐ approve ☐ change: ____________

## 6. `m11-notation` (Lesson 11: Points and notation of lines, half lines and line segments)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| Which notation names the half line that starts at E and passes through R? | **[ER)** | (ER): _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>[ER]: _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>[RE): _A half line is named starting with its end point. [RE) starts at R, not at E._ |
| Which notation names the line through E and R? | **(ER)** | [ER): _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>[ER]: _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>[RE): _A half line is named starting with its end point. [RE) starts at R, not at E._ |
| Which notation names the segment with end points E and R? | **[ER]** | [ER): _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>(ER): _Look at the brackets: ( ) means no end point, [ ) one end point, [ ] two end points._<br>[RE): _A half line is named starting with its end point. [RE) starts at R, not at E._ |

**Full working shown after a second miss** (sample):

> ( ) means no end point: a line. [ ) means one end point: a half line, named from its end point. [ ] means two end points: a segment.  
> So the line through C and P is written (CP).  

**Sources**

- Notation used in Cameroonian Form 1 mathematics (French-influenced): (AB) line, [AB) half line, [AB] segment, AB length. Supports: Which brackets name which figure; a half line is named from its end point; a line has no end point and no length. _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________

## 7. `m11-end-points` (Lesson 11: Points and notation of lines, half lines and line segments)

Type: numeric, level 1.

| Question | Answer accepted | Recognised wrong answers and feedback |
|---|---|---|
| How many end points does (ER) have? | **0** | 2: _E and R only give the figure its name. Count the square brackets: each [ or ] marks an end point._ |
| How many end points does [ER) have? | **1** | 2: _E and R only give the figure its name. Count the square brackets: each [ or ] marks an end point._ |
| How many end points does [ER] have? | **2** |  |

**Full working shown after a second miss** (sample):

> Each square bracket [ or ] marks an end point; a round bracket means the figure goes on forever.  
> [CS) has 1 end point.  

**Sources**

- Notation used in Cameroonian Form 1 mathematics (French-influenced): (AB) line, [AB) half line, [AB] segment, AB length. Supports: Which brackets name which figure; a half line is named from its end point; a line has no end point and no length. _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________

## 8. `m11-true` (Lesson 11: Points and notation of lines, half lines and line segments)

Type: mcq, level 2.

**Which statement is true?** (choose the TRUE statement; the app shows 1 true and 3 false, picked at random)

| Statement | True or false (as authored) | Feedback |
|---|---|---|
| (ER) and (RE) are the same line. | true | |
| [ER] and [RE] are the same segment. | true | |
| [ER) has one end point: E. | true | |
| [ER) and [RE) are the same half line. | **false** | [ER) starts at E; [RE) starts at R and goes the other way. |
| The line (ER) has two end points. | **false** | A line goes on forever in both directions: it has no end point. |
| The segment [ER] goes on forever. | **false** | A segment stops at its two end points, E and R. |
| Through E and R we can draw two different straight lines. | **false** | Through two points there is exactly one straight line. |

**Full working shown after a second miss** (sample):

> The true statement is “(SP) and (PS) are the same line.”.  
> “The line (SP) has two end points.” is false: A line goes on forever in both directions: it has no end point.  
> “[SP) and [PS) are the same half line.” is false: [SP) starts at S; [PS) starts at P and goes the other way.  
> “Through S and P we can draw two different straight lines.” is false: Through two points there is exactly one straight line.  

**Sources**

- Notation used in Cameroonian Form 1 mathematics (French-influenced): (AB) line, [AB) half line, [AB] segment, AB length. Supports: Which brackets name which figure; a half line is named from its end point; a line has no end point and no length. _Checked: Not externally sourced: compare with the pupil's exercise book._
- Euclid, Elements, Book I, Postulate 1 (a straight line can be drawn between any two points). Supports: Exactly one straight line passes through two different points, so any two points are collinear; three points need not be. _Checked: Not externally sourced (standard axiom)._

Decision: ☐ approve ☐ change: ____________

## 9. `m11-spot` (Lesson 11: Points and notation of lines, half lines and line segments)

Type: spot_error, level 3.

**One of these statements is false. Which one?** (choose the FALSE statement; the app shows 3 true and 1 false, picked at random)

| Statement | True or false (as authored) | Feedback |
|---|---|---|
| (ER) and (RE) are the same line. | true | |
| [ER] and [RE] are the same segment. | true | |
| [ER) has one end point: E. | true | |
| We can measure the length ER of the segment [ER]. | true | |
| [ER) and [RE) are the same half line. | **false** | [ER) starts at E; [RE) starts at R and goes the other way. |
| We can measure the length of the line (ER). | **false** | A line goes on forever, so it has no length. Only a segment has a length. |

**Full working shown after a second miss** (sample):

> The wrong statement is “[FL) and [LF) are the same half line.”.  
> [FL) starts at F; [LF) starts at L and goes the other way.  

**Sources**

- Notation used in Cameroonian Form 1 mathematics (French-influenced): (AB) line, [AB) half line, [AB] segment, AB length. Supports: Which brackets name which figure; a half line is named from its end point; a line has no end point and no length. _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________

## 10. `c11-3-check` (Lesson 11: Points and notation of lines, half lines and line segments)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| Which of these has a length you can measure? | **[ER]** | (ER): _Lines and half lines go on forever, so they have no length. Only a segment has one._<br>[ER): _Lines and half lines go on forever, so they have no length. Only a segment has one._ |

**Full working shown after a second miss** (sample):

> Lines and half lines go on forever, so they have no length.  
> Only the segment [SD] has a length you can measure.  

**Sources**

- Notation used in Cameroonian Form 1 mathematics (French-influenced): (AB) line, [AB) half line, [AB] segment, AB length. Supports: Which brackets name which figure; a half line is named from its end point; a line has no end point and no length. _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________

## 11. `m12-facts` (Lesson 12: Collinear points)

Type: mcq, level 1.

**Which statement is true?** (choose the TRUE statement; the app shows 1 true and 3 false, picked at random)

| Statement | True or false (as authored) | Feedback |
|---|---|---|
| Any two points are always collinear. | true | |
| Through two different points there is exactly one straight line. | true | |
| Through two points we can draw many straight lines. | **false** | Through two different points there is exactly one straight line. |
| Any three points are always collinear. | **false** | Three points are collinear only if the third one is on the line through the other two. |
| Two points are collinear only if they are close together. | **false** | Distance does not matter: one line always passes through any two points. |
| Points on a curved path are always collinear. | **false** | Collinear means on one straight line, not on a curve. |

**Full working shown after a second miss** (sample):

> The true statement is “Through two different points there is exactly one straight line.”.  
> “Two points are collinear only if they are close together.” is false: Distance does not matter: one line always passes through any two points.  
> “Any three points are always collinear.” is false: Three points are collinear only if the third one is on the line through the other two.  
> “Through two points we can draw many straight lines.” is false: Through two different points there is exactly one straight line.  

**Sources**

- Euclid, Elements, Book I, Postulate 1 (a straight line can be drawn between any two points). Supports: Exactly one straight line passes through two different points, so any two points are collinear; three points need not be. _Checked: Not externally sourced (standard axiom)._

Decision: ☐ approve ☐ change: ____________

## 12. `m14-converse` (Lesson 14: Line segment.- Midpoint property of a line segment and its converse)

Type: mcq, level 3.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| MA = MB = 10 cm. Can you be sure that M is the midpoint of [AB]? | **No: M must also be on [AB].** | Yes, because MA = MB.: _Many points are at the same distance from A and B (all the points of the perpendicular bisector). Only the one on [AB] is the midpoint._<br>Yes, because 10 is a whole number.: _The size of the number does not matter. Check whether M is on [AB]._<br>No: the midpoint is never at the same distance from A and B.: _The midpoint is always at the same distance from A and B. But being at the same distance is not enough on its own._ |

**Full working shown after a second miss** (sample):

> Every point of the perpendicular bisector of [AB] has MA = MB, but only one of them is on [AB].  
> Answer: No: M must also be on [AB].  

**Sources**

- Definition of the midpoint of a segment; the perpendicular bisector as the set of points equidistant from A and B. Supports: MA = MB alone does not make M the midpoint: every point of the perpendicular bisector has MA = MB, and only the one on [AB] is the midpoint. _Checked: Not externally sourced (standard definitions)._

Decision: ☐ approve ☐ change: ____________

## 13. `c14-3-check` (Lesson 14: Line segment.- Midpoint property of a line segment and its converse)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| M is on [AB] and AM = MB. Is M the midpoint of [AB]? | **Yes** | No: _M is the midpoint only when it is on [AB] AND AM = MB._ |
| MA = MB, but M is not on [AB]. Is M the midpoint of [AB]? | **No** | Yes: _M is the midpoint only when it is on [AB] AND AM = MB._ |

**Full working shown after a second miss** (sample):

> The midpoint needs both: M on [AB] AND AM = MB.  
> Answer: No  

**Sources**

- Definition of the midpoint of a segment; the perpendicular bisector as the set of points equidistant from A and B. Supports: MA = MB alone does not make M the midpoint: every point of the perpendicular bisector has MA = MB, and only the one on [AB] is the midpoint. _Checked: Not externally sourced (standard definitions)._

Decision: ☐ approve ☐ change: ____________

## 14. `m15-steps` (Lesson 15: Constructing the perpendicular bisector of a line segment)

Type: ordering, level 2.

**Put the steps for constructing the perpendicular bisector of [AB] in order.**

Correct order (as authored):

1. Open the compasses to more than half of AB.
2. Put the point on A and draw an arc above and below [AB].
3. With the same opening, put the point on B and draw arcs that cut the first two.
4. Join the two crossing points with a ruler.

**Full working shown after a second miss** (sample):

> The correct order is: Open the compasses to more than half of AB. → Put the point on A and draw an arc above and below [AB]. → With the same opening, put the point on B and draw arcs that cut the first two. → Join the two crossing points with a ruler..  

**Sources**

- Euclid, Elements, Book I, Proposition 10 (bisecting a segment); the standard ruler-and-compasses construction of the perpendicular bisector. Supports: The construction steps and their order; the bisector passes through the midpoint at a right angle and not through A; its points are equidistant from A and B. _Checked: Not externally sourced (standard construction)._

Decision: ☐ approve ☐ change: ____________

## 15. `m15-spot` (Lesson 15: Constructing the perpendicular bisector of a line segment)

Type: spot_error, level 3.

**One of these statements is false. Which one?** (choose the FALSE statement; the app shows 3 true and 1 false, picked at random)

| Statement | True or false (as authored) | Feedback |
|---|---|---|
| If P is on the perpendicular bisector of [AB] and PA = 13 cm, then PB = 13 cm. | true | |
| The perpendicular bisector of [AB] passes through the midpoint of [AB]. | true | |
| The perpendicular bisector of [AB] makes a right angle with [AB]. | true | |
| If PA = 13 cm and PB = 14 cm, then P is on the perpendicular bisector of [AB]. | **false** | P is on the perpendicular bisector only if PA = PB. Here 13 ≠ 14. |
| The perpendicular bisector of [AB] passes through A. | **false** | It passes through the midpoint of [AB], not through A. |

**Full working shown after a second miss** (sample):

> The wrong statement is “The perpendicular bisector of [AB] passes through A.”.  
> It passes through the midpoint of [AB], not through A.  

**Sources**

- Euclid, Elements, Book I, Proposition 10 (bisecting a segment); the standard ruler-and-compasses construction of the perpendicular bisector. Supports: The construction steps and their order; the bisector passes through the midpoint at a right angle and not through A; its points are equidistant from A and B. _Checked: Not externally sourced (standard construction)._

Decision: ☐ approve ☐ change: ____________

## 16. `c15-1-check` (Lesson 15: Constructing the perpendicular bisector of a line segment)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| The perpendicular bisector of [AB] passes through: | **the midpoint of [AB]** | the point A: _It cuts [AB] in the middle, so it passes through the midpoint, not through A or B._<br>the point B: _It cuts [AB] in the middle, so it passes through the midpoint, not through A or B._<br>no point of [AB]: _It cuts [AB]: it passes through the midpoint._ |

**Full working shown after a second miss** (sample):

> It cuts [AB] into two equal parts, at a right angle.  
> So it passes through the midpoint of [AB].  

**Sources**

- Euclid, Elements, Book I, Proposition 10 (bisecting a segment); the standard ruler-and-compasses construction of the perpendicular bisector. Supports: The construction steps and their order; the bisector passes through the midpoint at a right angle and not through A; its points are equidistant from A and B. _Checked: Not externally sourced (standard construction)._

Decision: ☐ approve ☐ change: ____________

## 17. `m16-symbol` (Lesson 16: Parallel, perpendicular and orthogonal lines. - Notation and properties)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| What does (d) // (d′) mean? | **(d) and (d′) are parallel.** | (d) and (d′) are perpendicular.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._<br>(d) and (d′) are the same line.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._<br>(d) and (d′) meet, but not at a right angle.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._ |
| What does (d) ⊥ (d′) mean? | **(d) and (d′) are perpendicular.** | (d) and (d′) are parallel.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._<br>(d) and (d′) are the same line.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._<br>(d) and (d′) meet, but not at a right angle.: _// means parallel (never meet). ⊥ means perpendicular (meet at a right angle)._ |

**Full working shown after a second miss** (sample):

> // means parallel: the lines never meet. ⊥ means perpendicular: they meet at a right angle.  
> So (d) ⊥ (d′) means: (d) and (d′) are perpendicular.  

**Sources**

- Symbols // (parallel) and ⊥ (perpendicular) as used in Form 1. Supports: // means parallel (never meet); ⊥ means perpendicular (meet at a right angle). _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________

## 18. `m16-through-point` (Lesson 16: Parallel, perpendicular and orthogonal lines. - Notation and properties)

Type: numeric, level 1.

| Question | Answer accepted | Recognised wrong answers and feedback |
|---|---|---|
| Through a point P that is not on the line (d), how many lines can you draw parallel to (d)? | **1** | 2: _Through a point not on (d) there is exactly one parallel line to (d)._<br>0: _There is always exactly one: you can draw it with a set square and a ruler._ |
| Through a point P that is not on the line (d), how many lines can you draw perpendicular to (d)? | **1** | 2: _Through a point not on (d) there is exactly one perpendicular line to (d)._<br>0: _There is always exactly one: you can draw it with a set square and a ruler._ |

**Full working shown after a second miss** (sample):

> Through a point not on (d) there is exactly one parallel line to (d).  
> Answer: 1  

**Sources**

- [Playfair's axiom (equivalent to Euclid's parallel postulate); Encyclopaedia Britannica, 'Euclidean geometry'](https://www.britannica.com/science/Euclidean-geometry). Supports: Through a point not on a line there is exactly one parallel line. _Checked: Search-result summary of the page (the page itself could not be opened)._
- Euclid, Elements, Book I, Proposition 12, and the standard uniqueness theorem for perpendiculars in a plane. Supports: Through a point not on a line there is exactly one line perpendicular to it. _Checked: Not externally sourced (standard theorem)._

Decision: ☐ approve ☐ change: ____________

## 19. `c16-2-check` (Lesson 16: Parallel, perpendicular and orthogonal lines. - Notation and properties)

Type: mcq, level 1.

| Question | Answer accepted | Wrong choices and the feedback each one gets |
|---|---|---|
| Two lines in a plane meet at a right angle. They are: | **perpendicular** | parallel: _Parallel lines never meet. Perpendicular (orthogonal) lines meet at a right angle._<br>the same line: _Parallel lines never meet. Perpendicular (orthogonal) lines meet at a right angle._ |
| Two lines in a plane never meet. They are: | **parallel** | perpendicular: _Parallel lines never meet. Perpendicular (orthogonal) lines meet at a right angle._<br>the same line: _Parallel lines never meet. Perpendicular (orthogonal) lines meet at a right angle._ |

**Full working shown after a second miss** (sample):

> Parallel lines never meet; perpendicular (orthogonal) lines meet at a right angle.  
> Lines that meet at a right angle are perpendicular.  

**Sources**

- Symbols // (parallel) and ⊥ (perpendicular) as used in Form 1. Supports: // means parallel (never meet); ⊥ means perpendicular (meet at a right angle). _Checked: Not externally sourced: compare with the pupil's exercise book._

Decision: ☐ approve ☐ change: ____________
