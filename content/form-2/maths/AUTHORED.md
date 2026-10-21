# Maths Form 2, Batches M2-1, M2-2: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-maths`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: rules the computed answers use (src/engine/lib/maths2.js, tested in tests-js/maths2.test.js)

- **Integers**: negative numbers in brackets inside a calculation ((−3) × 4); same signs give a positive product or quotient, different signs a negative one. Answers that can be negative get the full keyboard (with a minus sign) on every variant.
- **Powers**: (−2)³ = (−2) × (−2) × (−2) = -8; laws of indices for the same base only.
- **Prime factorisation** by repeated division (60 ÷ 2 = 30; 30 ÷ 2 = 15; 15 ÷ 3 = 5; 5 ÷ 5 = 1), written 2 × 2 × 3 × 5 or 2² × 3 × 5; HCF and LCM computed (HCF(24, 36) = 12, LCM = 72).
- **Expressions**: 3x − y + 5; a coefficient 1 is not written; −2(x − 4) = −2x + 8.
- **Inequalities on the number line**: filled circle for ≤ and ≥, open circle for < and >, thick line and arrow towards the solutions.
- **Notation** as in Form 1: (AB) line, [AB) half line, [AB] segment, AB length; (Δ) for the perpendicular bisector.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `m2-4-spot` | 4 | spot the error, 3 | laws-of-indices |
| 2 | `m2-5-c2` (card c5-2) | 5 | multiple choice, 1 | primes |
| 3 | `m2-6-c4` (card c6-4) | 6 | matching, 1 | hcf-lcm |
| 4 | `m2-9-c1` (card c9-1) | 9 | multiple choice, 1 | triangle-inequality |
| 5 | `m2-10-c1` (card c10-1) | 10 | multiple choice, 1 | segment |
| 6 | `m2-11-def` | 11 | multiple choice, 1 | perpendicular-bisector |
| 7 | `m2-11-angle` | 11 | number, 1 | perpendicular-bisector |
| 8 | `m2-11-steps` | 11 | ordering, 2 | perpendicular-bisector |
| 9 | `m2-11-spot` | 11 | spot the error, 3 | perpendicular-bisector |
| 10 | `m2-12-c3` (card c12-3) | 12 | multiple choice, 1 | perpendicular-bisector |
| 11 | `m2-13-words` | 13 | matching, 2 | coordinates |
| 12 | `m2-13-c1` (card c13-1) | 13 | multiple choice, 1 | coordinates |
| 13 | `m2-17-c3` (card c17-3) | 17 | multiple choice, 1 | like-terms |
| 14 | `m2-29-def` | 29 | matching, 1 | triangles |
| 15 | `m2-29-point` | 29 | matching, 2 | triangles |
| 16 | `m2-29-spot` | 29 | spot the error, 3 | triangles |
| 17 | `m2-29-point-card` (card c29-3) | 29 | matching, 1 | triangles |
| 18 | `m2-30-spot` | 30 | spot the error, 3 | triangles |
| 19 | `m2-37-kind` | 37 | multiple choice, 1 | real-numbers |
| 20 | `m2-38-set` | 38 | multiple choice, 1 | real-numbers |
| 21 | `m2-38-order` | 38 | ordering, 1 | real-numbers |
| 22 | `m2-38-spot` | 38 | spot the error, 3 | real-numbers |
| 23 | `m2-41-which` | 41 | multiple choice, 3 | proportion |
| 24 | `m2-41-which-card` (card c41-3) | 41 | multiple choice, 1 | proportion |
| 25 | `m2-49-spot` | 49 | spot the error, 3 | polygons |
| 26 | `m2-52-what` | 52 | multiple choice, 2 | symmetry |
| 27 | `m2-52-spot` | 52 | spot the error, 3 | symmetry |
| 28 | `m2-52-what-card` (card c52-3) | 52 | multiple choice, 1 | symmetry |
| 29 | `m2-53-centre` | 53 | multiple choice, 1 | circles |
| 30 | `m2-53-spot` | 53 | spot the error, 3 | circles |

### `m2-4-spot` · Lesson 4 · spot the error, level 3

Prompt: Which statement is false?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ {pw('a', m)} × {pw('a', n)} = {pw('a', m + n)}
- ✅ {pw('a', m + n)} ÷ {pw('a', n)} = {pw('a', m)}
- ✅ ({pw('a', m)}){sup(n)} = {pw('a', m * n)}
- ✅ {pw(b, z)} = {one}
- ❌ {pw('a', m)} × {pw('a', n)} = {pw('a', m * n)}  
  _↳ When multiplying powers, add the indices: {pw('a', m)} × {pw('a', n)} = {pw('a', m + n)}._
- ❌ ({pw('a', m)}){sup(n)} = {pw('a', m + n)}  
  _↳ For a power of a power, multiply the indices: ({pw('a', m)}){sup(n)} = {pw('a', m * n)}._
- ❌ {pw(b, z)} = {z}  
  _↳ Any number except zero to the power zero is {one}._
- ❌ {pw(c, m)} × {pw(b, n)} = {pw(c * b, m + n)}  
  _↳ The laws only work when the bases are the same: {c} and {b} are different bases._


Three generated variants:

> Which statement is false?

- ◻️ (a³)⁵ = a¹⁵
- ✅ 7⁰ = 0  
  _↳ explanation: Any number except zero to the power zero is 1._
- ◻️ a⁸ ÷ a⁵ = a³
- ◻️ 7⁰ = 1

Full working after a second miss:

> The wrong statement is “7⁰ = 0”.  
> Any number except zero to the power zero is 1.  

> Which statement is false?

- ◻️ a⁹ ÷ a⁴ = a⁵
- ◻️ a⁵ × a⁴ = a⁹
- ◻️ 7⁰ = 1
- ✅ a⁵ × a⁴ = a²⁰  
  _↳ explanation: When multiplying powers, add the indices: a⁵ × a⁴ = a⁹._

Full working after a second miss:

> The wrong statement is “a⁵ × a⁴ = a²⁰”.  
> When multiplying powers, add the indices: a⁵ × a⁴ = a⁹.  

> Which statement is false?

- ✅ 2⁰ = 0  
  _↳ explanation: Any number except zero to the power zero is 1._
- ◻️ 2⁰ = 1
- ◻️ a⁴ × a⁵ = a⁹
- ◻️ (a⁴)⁵ = a²⁰

Full working after a second miss:

> The wrong statement is “2⁰ = 0”.  
> Any number except zero to the power zero is 1.  

Sources: laws-of-indices (Laws of indices for powers of the same base)

### `m2-5-c2` · Lesson 5 · multiple choice, level 1

Prompt: Which statement is true?

`p`: 11 · 13 · 17 · 19 · 23 · 29 · 31 · 37 · 41 · 43 · 47 · 53 · 59 · 61 · 67 · 71 · 73 · 79 · 83 · 89 · 97

`c`: 9 · 15 · 21 · 25 · 27 · 33 · 35 · 39 · 45 · 49 · 51 · 55 · 57 · 63

Shows 1 true and 2 false statement(s), drawn from:

- ✅ {two} is a prime number
- ✅ {p} is a prime number
- ✅ {e} is not a prime number
- ✅ {one} is not a prime number
- ❌ {one} is a prime number  
  _↳ {one} has only one factor; a prime has exactly two._
- ❌ {e} is a prime number  
  _↳ {e} is even, so {two} is a factor: {e} = {factorProduct(e)}._
- ❌ Every odd number is prime  
  _↳ Not every odd number: {c} = {factorProduct(c)}._
- ❌ {two} is not a prime number  
  _↳ {two} has exactly two factors, {one} and {two}, so it is prime._


Three generated variants:

> Which statement is true?

- ✅ 43 is a prime number
- ◻️ 2 is not a prime number  
  _↳ feedback if chosen: 2 has exactly two factors, 1 and 2, so it is prime._
- ◻️ 98 is a prime number  
  _↳ feedback if chosen: 98 is even, so 2 is a factor: 98 = 2 × 7 × 7._

Full working after a second miss:

> The true statement is “43 is a prime number”.  
> “2 is not a prime number” is false: 2 has exactly two factors, 1 and 2, so it is prime.  
> “98 is a prime number” is false: 98 is even, so 2 is a factor: 98 = 2 × 7 × 7.  

> Which statement is true?

- ◻️ 50 is a prime number  
  _↳ feedback if chosen: 50 is even, so 2 is a factor: 50 = 2 × 5 × 5._
- ◻️ 2 is not a prime number  
  _↳ feedback if chosen: 2 has exactly two factors, 1 and 2, so it is prime._
- ✅ 2 is a prime number

Full working after a second miss:

> The true statement is “2 is a prime number”.  
> “50 is a prime number” is false: 50 is even, so 2 is a factor: 50 = 2 × 5 × 5.  
> “2 is not a prime number” is false: 2 has exactly two factors, 1 and 2, so it is prime.  

> Which statement is true?

- ◻️ 1 is a prime number  
  _↳ feedback if chosen: 1 has only one factor; a prime has exactly two._
- ✅ 1 is not a prime number
- ◻️ 6 is a prime number  
  _↳ feedback if chosen: 6 is even, so 2 is a factor: 6 = 2 × 3._

Full working after a second miss:

> The true statement is “1 is not a prime number”.  
> “1 is a prime number” is false: 1 has only one factor; a prime has exactly two.  
> “6 is a prime number” is false: 6 is even, so 2 is a factor: 6 = 2 × 3.  

Sources: primes (Definition of prime and composite numbers; the fundamental theorem of arithmetic (unique prime factorisation))

### `m2-6-c4` · Lesson 6 · matching, level 1

Prompt: Sort each problem: do you need the HCF or the LCM?

Pairs (4 shown each time, sorted into groups):

- the largest number of equal bags you can make from 24 mangoes and 36 oranges → **HCF**
- the longest equal pieces you can cut from ropes of 12 m and 18 m → **HCF**
- the largest square tiles that exactly cover a floor 30 dm by 42 dm → **HCF**
- the biggest equal teams you can make from 20 girls and 25 boys, girls and boys kept apart → **HCF**
- when two buses that leave every 12 and 18 minutes next leave together → **LCM**
- when two lights that flash every 4 and 6 seconds next flash together → **LCM**
- the smallest number of sweets that can be shared equally among 4 children or among 6 children → **LCM**
- when two pupils who visit the library every 3 and every 5 days are next there on the same day → **LCM**


Three generated variants:

> Sort each problem: do you need the HCF or the LCM?

Groups: HCF · LCM
- the smallest number of sweets that can be shared equally among 4 children or among 6 children → **LCM**
- when two buses that leave every 12 and 18 minutes next leave together → **LCM**
- the longest equal pieces you can cut from ropes of 12 m and 18 m → **HCF**
- the biggest equal teams you can make from 20 girls and 25 boys, girls and boys kept apart → **HCF**

Full working after a second miss:

> The right pairs are:  
> the smallest number of sweets that can be shared equally among 4 children or among 6 children → LCM  
> when two buses that leave every 12 and 18 minutes next leave together → LCM  
> the longest equal pieces you can cut from ropes of 12 m and 18 m → HCF  
> the biggest equal teams you can make from 20 girls and 25 boys, girls and boys kept apart → HCF  

> Sort each problem: do you need the HCF or the LCM?

Groups: HCF · LCM
- when two pupils who visit the library every 3 and every 5 days are next there on the same day → **LCM**
- when two lights that flash every 4 and 6 seconds next flash together → **LCM**
- the largest square tiles that exactly cover a floor 30 dm by 42 dm → **HCF**
- the longest equal pieces you can cut from ropes of 12 m and 18 m → **HCF**

Full working after a second miss:

> The right pairs are:  
> when two pupils who visit the library every 3 and every 5 days are next there on the same day → LCM  
> when two lights that flash every 4 and 6 seconds next flash together → LCM  
> the largest square tiles that exactly cover a floor 30 dm by 42 dm → HCF  
> the longest equal pieces you can cut from ropes of 12 m and 18 m → HCF  

> Sort each problem: do you need the HCF or the LCM?

Groups: HCF · LCM
- the largest number of equal bags you can make from 24 mangoes and 36 oranges → **HCF**
- the largest square tiles that exactly cover a floor 30 dm by 42 dm → **HCF**
- the biggest equal teams you can make from 20 girls and 25 boys, girls and boys kept apart → **HCF**
- when two pupils who visit the library every 3 and every 5 days are next there on the same day → **LCM**

Full working after a second miss:

> The right pairs are:  
> the largest number of equal bags you can make from 24 mangoes and 36 oranges → HCF  
> the largest square tiles that exactly cover a floor 30 dm by 42 dm → HCF  
> the biggest equal teams you can make from 20 girls and 25 boys, girls and boys kept apart → HCF  
> when two pupils who visit the library every 3 and every 5 days are next there on the same day → LCM  

Sources: hcf-lcm (Definitions of the highest common factor (HCF, also highest common divisor) and lowest common multiple (LCM); the prime-factor method; HCF × LCM = a × b for two numbers)

### `m2-9-c1` · Lesson 9 · multiple choice, level 1

Prompt: Which statement is true for every triangle ABC?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ AB < AC + CB
- ✅ BC < BA + AC
- ✅ AC < AB + BC
- ❌ AB > AC + CB  
  _↳ The straight side AB is the shortest way from A to B, so it is less than AC + CB._
- ❌ AB = AC + CB  
  _↳ That only happens when C is on the segment [AB]: then there is no triangle._
- ❌ BC > BA + AC  
  _↳ The straight side BC is shorter than going through A: BC < BA + AC._
- ❌ AC = AB + BC  
  _↳ That only happens when B is on the segment [AC]: then there is no triangle._


Three generated variants:

> Which statement is true for every triangle ABC?

- ◻️ AB > AC + CB  
  _↳ feedback if chosen: The straight side AB is the shortest way from A to B, so it is less than AC + CB._
- ✅ BC < BA + AC
- ◻️ AB = AC + CB  
  _↳ feedback if chosen: That only happens when C is on the segment [AB]: then there is no triangle._

Full working after a second miss:

> The true statement is “BC < BA + AC”.  
> “AB > AC + CB” is false: The straight side AB is the shortest way from A to B, so it is less than AC + CB.  
> “AB = AC + CB” is false: That only happens when C is on the segment [AB]: then there is no triangle.  

> Which statement is true for every triangle ABC?

- ◻️ AC = AB + BC  
  _↳ feedback if chosen: That only happens when B is on the segment [AC]: then there is no triangle._
- ◻️ AB = AC + CB  
  _↳ feedback if chosen: That only happens when C is on the segment [AB]: then there is no triangle._
- ✅ AB < AC + CB

Full working after a second miss:

> The true statement is “AB < AC + CB”.  
> “AC = AB + BC” is false: That only happens when B is on the segment [AC]: then there is no triangle.  
> “AB = AC + CB” is false: That only happens when C is on the segment [AB]: then there is no triangle.  

> Which statement is true for every triangle ABC?

- ◻️ AC = AB + BC  
  _↳ feedback if chosen: That only happens when B is on the segment [AC]: then there is no triangle._
- ✅ AC < AB + BC
- ◻️ BC > BA + AC  
  _↳ feedback if chosen: The straight side BC is shorter than going through A: BC < BA + AC._

Full working after a second miss:

> The true statement is “AC < AB + BC”.  
> “AC = AB + BC” is false: That only happens when B is on the segment [AC]: then there is no triangle.  
> “BC > BA + AC” is false: The straight side BC is shorter than going through A: BC < BA + AC.  

Sources: triangle-inequality (The triangle inequality (Euclid, Elements I.20))

### `m2-10-c1` · Lesson 10 · multiple choice, level 1

Prompt: Which one names the segment with end points {L[0]} and {L[1]}?

Table `L` (one row is picked each time):

| 0 | 1 |
|---|---|
| A | B |
| P | Q |
| E | F |
| K | L |
| M | N |
| R | S |

Right answer: `[{L[0]}{L[1]}]`; wrong choices: `({L[0]}{L[1]})`, `[{L[0]}{L[1]})`, `{L[0]}{L[1]}`

- Feedback `line`: “({L[0]}{L[1]}) with round brackets is the whole line, which has no end points.”
- Feedback `half`: “[{L[0]}{L[1]}) is a half line: it starts at {L[0]} and never ends.”
- Feedback `length`: “{L[0]}{L[1]} with no brackets is the length of the segment, a number of centimetres.”

Three generated variants:

> Which one names the segment with end points E and F?

- ✅ [EF]
- ◻️ EF  
  _↳ feedback if chosen: EF with no brackets is the length of the segment, a number of centimetres._
- ◻️ [EF)  
  _↳ feedback if chosen: [EF) is a half line: it starts at E and never ends._
- ◻️ (EF)  
  _↳ feedback if chosen: (EF) with round brackets is the whole line, which has no end points._

Full working after a second miss:

> A segment is written with square brackets around both end points.  
> So the segment is [EF].  

> Which one names the segment with end points K and L?

- ✅ [KL]
- ◻️ KL  
  _↳ feedback if chosen: KL with no brackets is the length of the segment, a number of centimetres._
- ◻️ (KL)  
  _↳ feedback if chosen: (KL) with round brackets is the whole line, which has no end points._
- ◻️ [KL)  
  _↳ feedback if chosen: [KL) is a half line: it starts at K and never ends._

Full working after a second miss:

> A segment is written with square brackets around both end points.  
> So the segment is [KL].  

> Which one names the segment with end points E and F?

- ✅ [EF]
- ◻️ (EF)  
  _↳ feedback if chosen: (EF) with round brackets is the whole line, which has no end points._
- ◻️ [EF)  
  _↳ feedback if chosen: [EF) is a half line: it starts at E and never ends._
- ◻️ EF  
  _↳ feedback if chosen: EF with no brackets is the length of the segment, a number of centimetres._

Full working after a second miss:

> A segment is written with square brackets around both end points.  
> So the segment is [EF].  

Sources: segment (Notation used in Cameroonian mathematics (French-influenced), as in Form 1: (AB) line, [AB) half line, [AB] segment, AB length; midpoint; a point M is on [AB] exactly when AM + MB = AB)

### `m2-11-def` · Lesson 11 · multiple choice, level 1

Prompt: Which line is the perpendicular bisector of [AB]?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the line through the midpoint of [AB] that is perpendicular to (AB)
- ✅ the line that cuts [AB] at its midpoint, at a right angle
- ✅ the line (Δ) through M, the midpoint of [AB], with (Δ) ⊥ (AB)
- ❌ any line through the midpoint of [AB]  
  _↳ It must also be perpendicular to (AB)._
- ❌ any line perpendicular to (AB)  
  _↳ It must also pass through the midpoint of [AB]._
- ❌ the line (AB) itself  
  _↳ (AB) contains the segment; the perpendicular bisector crosses it at a right angle._
- ❌ the line through A that is perpendicular to (AB)  
  _↳ It must pass through the midpoint of [AB], not through A._


Three generated variants:

> Which line is the perpendicular bisector of [AB]?

- ✅ the line (Δ) through M, the midpoint of [AB], with (Δ) ⊥ (AB)
- ◻️ the line (AB) itself  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it at a right angle._
- ◻️ the line through A that is perpendicular to (AB)  
  _↳ feedback if chosen: It must pass through the midpoint of [AB], not through A._
- ◻️ any line through the midpoint of [AB]  
  _↳ feedback if chosen: It must also be perpendicular to (AB)._

Full working after a second miss:

> The true statement is “the line (Δ) through M, the midpoint of [AB], with (Δ) ⊥ (AB)”.  
> “the line (AB) itself” is false: (AB) contains the segment; the perpendicular bisector crosses it at a right angle.  
> “the line through A that is perpendicular to (AB)” is false: It must pass through the midpoint of [AB], not through A.  
> “any line through the midpoint of [AB]” is false: It must also be perpendicular to (AB).  

> Which line is the perpendicular bisector of [AB]?

- ◻️ any line perpendicular to (AB)  
  _↳ feedback if chosen: It must also pass through the midpoint of [AB]._
- ◻️ the line (AB) itself  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it at a right angle._
- ✅ the line through the midpoint of [AB] that is perpendicular to (AB)
- ◻️ any line through the midpoint of [AB]  
  _↳ feedback if chosen: It must also be perpendicular to (AB)._

Full working after a second miss:

> The true statement is “the line through the midpoint of [AB] that is perpendicular to (AB)”.  
> “any line perpendicular to (AB)” is false: It must also pass through the midpoint of [AB].  
> “the line (AB) itself” is false: (AB) contains the segment; the perpendicular bisector crosses it at a right angle.  
> “any line through the midpoint of [AB]” is false: It must also be perpendicular to (AB).  

> Which line is the perpendicular bisector of [AB]?

- ◻️ any line perpendicular to (AB)  
  _↳ feedback if chosen: It must also pass through the midpoint of [AB]._
- ✅ the line through the midpoint of [AB] that is perpendicular to (AB)
- ◻️ the line (AB) itself  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it at a right angle._
- ◻️ any line through the midpoint of [AB]  
  _↳ feedback if chosen: It must also be perpendicular to (AB)._

Full working after a second miss:

> The true statement is “the line through the midpoint of [AB] that is perpendicular to (AB)”.  
> “any line perpendicular to (AB)” is false: It must also pass through the midpoint of [AB].  
> “the line (AB) itself” is false: (AB) contains the segment; the perpendicular bisector crosses it at a right angle.  
> “any line through the midpoint of [AB]” is false: It must also be perpendicular to (AB).  

Sources: perpendicular-bisector (Definition and ruler-and-compasses construction of the perpendicular bisector (mediator) of a segment; its characteristic property: the points equidistant from the end points)

### `m2-11-angle` · Lesson 11 · number, level 1

Prompt: (Δ) is the perpendicular bisector of [{L[0]}{L[1]}]. What is the size of the angle between (Δ) and ({L[0]}{L[1]}), in degrees?
Right answer: `90`

Table `L` (one row is picked each time):

| 0 | 1 |
|---|---|
| A | B |
| P | Q |
| E | F |
| K | L |
| M | N |
| R | S |

- Feedback `straight` (typed `180`): “{180}° is a straight angle. Perpendicular lines make a right angle.”
- Feedback `half` (typed `45`): “Perpendicular means a right angle, not half of one.”

Three generated variants:

> (Δ) is the perpendicular bisector of [EF]. What is the size of the angle between (Δ) and (EF), in degrees?

Answer: **90 °**
- Typed **180** (straight) → “180° is a straight angle. Perpendicular lines make a right angle.”
- Typed **45** (half) → “Perpendicular means a right angle, not half of one.”

Full working after a second miss:

> The perpendicular bisector is perpendicular to the line (EF).  
> Perpendicular lines meet at a right angle: 90°.  

> (Δ) is the perpendicular bisector of [AB]. What is the size of the angle between (Δ) and (AB), in degrees?

Answer: **90 °**
- Typed **180** (straight) → “180° is a straight angle. Perpendicular lines make a right angle.”
- Typed **45** (half) → “Perpendicular means a right angle, not half of one.”

Full working after a second miss:

> The perpendicular bisector is perpendicular to the line (AB).  
> Perpendicular lines meet at a right angle: 90°.  

> (Δ) is the perpendicular bisector of [MN]. What is the size of the angle between (Δ) and (MN), in degrees?

Answer: **90 °**
- Typed **180** (straight) → “180° is a straight angle. Perpendicular lines make a right angle.”
- Typed **45** (half) → “Perpendicular means a right angle, not half of one.”

Full working after a second miss:

> The perpendicular bisector is perpendicular to the line (MN).  
> Perpendicular lines meet at a right angle: 90°.  

Sources: perpendicular-bisector (Definition and ruler-and-compasses construction of the perpendicular bisector (mediator) of a segment; its characteristic property: the points equidistant from the end points)

### `m2-11-steps` · Lesson 11 · ordering, level 2

Prompt: Put the steps for constructing the perpendicular bisector of [AB] in order.

Items in the right order:

1. Open the compasses to more than half of AB
2. With the point on A, draw an arc above [AB] and an arc below it
3. With the same opening and the point on B, draw arcs that cross the first two
4. Join the two crossing points with a ruler


Three generated variants:

> Put the steps for constructing the perpendicular bisector of [AB] in order.

Shown as: Join the two crossing points with a ruler · With the point on A, draw an arc above [AB] and an arc below it · With the same opening and the point on B, draw arcs that cross the first two · Open the compasses to more than half of AB
Correct order: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler

Full working after a second miss:

> The correct order is: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler.  

> Put the steps for constructing the perpendicular bisector of [AB] in order.

Shown as: Join the two crossing points with a ruler · With the point on A, draw an arc above [AB] and an arc below it · With the same opening and the point on B, draw arcs that cross the first two · Open the compasses to more than half of AB
Correct order: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler

Full working after a second miss:

> The correct order is: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler.  

> Put the steps for constructing the perpendicular bisector of [AB] in order.

Shown as: With the same opening and the point on B, draw arcs that cross the first two · Open the compasses to more than half of AB · With the point on A, draw an arc above [AB] and an arc below it · Join the two crossing points with a ruler
Correct order: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler

Full working after a second miss:

> The correct order is: Open the compasses to more than half of AB → With the point on A, draw an arc above [AB] and an arc below it → With the same opening and the point on B, draw arcs that cross the first two → Join the two crossing points with a ruler.  

Sources: perpendicular-bisector (Definition and ruler-and-compasses construction of the perpendicular bisector (mediator) of a segment; its characteristic property: the points equidistant from the end points)

### `m2-11-spot` · Lesson 11 · spot the error, level 3

Prompt: Ngwa wrote these sentences about constructing the perpendicular bisector of [AB], with AB = {ab} cm. Which sentence is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ I open the compasses to {h + 2} cm
- ✅ The line I draw passes through the midpoint of [AB]
- ✅ The line I draw is perpendicular to (AB)
- ✅ I keep the same opening for the arcs from A and from B
- ❌ I open the compasses to {h - 1} cm  
  _↳ {h - 1} cm is less than half of AB ({h} cm): the arcs would not cross._
- ❌ I change the opening before drawing the arcs from B  
  _↳ The opening must stay the same for the arcs from A and from B._
- ❌ The line I draw passes through A  
  _↳ The perpendicular bisector passes through the midpoint of [AB], not through A._


Three generated variants:

> Ngwa wrote these sentences about constructing the perpendicular bisector of [AB], with AB = 16 cm. Which sentence is wrong?

- ◻️ The line I draw is perpendicular to (AB)
- ◻️ The line I draw passes through the midpoint of [AB]
- ✅ I open the compasses to 7 cm  
  _↳ explanation: 7 cm is less than half of AB (8 cm): the arcs would not cross._
- ◻️ I keep the same opening for the arcs from A and from B

Full working after a second miss:

> The wrong statement is “I open the compasses to 7 cm”.  
> 7 cm is less than half of AB (8 cm): the arcs would not cross.  

> Ngwa wrote these sentences about constructing the perpendicular bisector of [AB], with AB = 16 cm. Which sentence is wrong?

- ◻️ I keep the same opening for the arcs from A and from B
- ✅ The line I draw passes through A  
  _↳ explanation: The perpendicular bisector passes through the midpoint of [AB], not through A._
- ◻️ The line I draw is perpendicular to (AB)
- ◻️ I open the compasses to 10 cm

Full working after a second miss:

> The wrong statement is “The line I draw passes through A”.  
> The perpendicular bisector passes through the midpoint of [AB], not through A.  

> Ngwa wrote these sentences about constructing the perpendicular bisector of [AB], with AB = 8 cm. Which sentence is wrong?

- ◻️ I keep the same opening for the arcs from A and from B
- ◻️ The line I draw is perpendicular to (AB)
- ✅ The line I draw passes through A  
  _↳ explanation: The perpendicular bisector passes through the midpoint of [AB], not through A._
- ◻️ The line I draw passes through the midpoint of [AB]

Full working after a second miss:

> The wrong statement is “The line I draw passes through A”.  
> The perpendicular bisector passes through the midpoint of [AB], not through A.  

Sources: perpendicular-bisector (Definition and ruler-and-compasses construction of the perpendicular bisector (mediator) of a segment; its characteristic property: the points equidistant from the end points)

### `m2-12-c3` · Lesson 12 · multiple choice, level 1

Prompt: {P[0]}A = {P[0]}B and {P[1]}A = {P[1]}B. Which line is the perpendicular bisector of [AB]?

Table `P` (one row is picked each time):

| 0 | 1 |
|---|---|
| C | D |
| E | F |
| K | L |
| M | N |
| P | Q |
| R | S |

Right answer: `({P[0]}{P[1]})`; wrong choices: `(AB)`, `({P[0]}A)`, `({P[1]}B)`

- Feedback `ab`: “(AB) contains the segment; the perpendicular bisector crosses it.”
- Feedback `pa`: “The perpendicular bisector does not pass through A: A is not at the same distance from A and B.”
- Feedback `pb`: “The perpendicular bisector does not pass through B: B is not at the same distance from A and B.”

Three generated variants:

> PA = PB and QA = QB. Which line is the perpendicular bisector of [AB]?

- ◻️ (PA)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through A: A is not at the same distance from A and B._
- ◻️ (QB)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through B: B is not at the same distance from A and B._
- ✅ (PQ)
- ◻️ (AB)  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it._

Full working after a second miss:

> P and Q are both equidistant from A and B, so both are on the perpendicular bisector.  
> The line through them is (PQ).  

> EA = EB and FA = FB. Which line is the perpendicular bisector of [AB]?

- ◻️ (FB)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through B: B is not at the same distance from A and B._
- ◻️ (EA)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through A: A is not at the same distance from A and B._
- ✅ (EF)
- ◻️ (AB)  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it._

Full working after a second miss:

> E and F are both equidistant from A and B, so both are on the perpendicular bisector.  
> The line through them is (EF).  

> EA = EB and FA = FB. Which line is the perpendicular bisector of [AB]?

- ◻️ (EA)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through A: A is not at the same distance from A and B._
- ◻️ (AB)  
  _↳ feedback if chosen: (AB) contains the segment; the perpendicular bisector crosses it._
- ✅ (EF)
- ◻️ (FB)  
  _↳ feedback if chosen: The perpendicular bisector does not pass through B: B is not at the same distance from A and B._

Full working after a second miss:

> E and F are both equidistant from A and B, so both are on the perpendicular bisector.  
> The line through them is (EF).  

Sources: perpendicular-bisector (Definition and ruler-and-compasses construction of the perpendicular bisector (mediator) of a segment; its characteristic property: the points equidistant from the end points)

### `m2-13-words` · Lesson 13 · matching, level 2

Prompt: Match each word to its meaning.

Pairs (4 shown each time):

- abscissa → **the first number of an ordered pair**
- ordinate → **the second number of an ordered pair**
- origin → **the point (0, 0), where the axes cross**
- x-axis → **the horizontal axis**
- y-axis → **the vertical axis**
- ordered pair → **two numbers in brackets, in a fixed order**


Three generated variants:

> Match each word to its meaning.

Right-hand side (shuffled): the point (0, 0), where the axes cross · the vertical axis · the first number of an ordered pair · the second number of an ordered pair
- abscissa → **the first number of an ordered pair**
- ordinate → **the second number of an ordered pair**
- origin → **the point (0, 0), where the axes cross**
- y-axis → **the vertical axis**

Full working after a second miss:

> The right pairs are:  
> abscissa → the first number of an ordered pair  
> ordinate → the second number of an ordered pair  
> origin → the point (0, 0), where the axes cross  
> y-axis → the vertical axis  

> Match each word to its meaning.

Right-hand side (shuffled): the second number of an ordered pair · the point (0, 0), where the axes cross · the first number of an ordered pair · the vertical axis
- y-axis → **the vertical axis**
- origin → **the point (0, 0), where the axes cross**
- ordinate → **the second number of an ordered pair**
- abscissa → **the first number of an ordered pair**

Full working after a second miss:

> The right pairs are:  
> y-axis → the vertical axis  
> origin → the point (0, 0), where the axes cross  
> ordinate → the second number of an ordered pair  
> abscissa → the first number of an ordered pair  

> Match each word to its meaning.

Right-hand side (shuffled): the second number of an ordered pair · the horizontal axis · the first number of an ordered pair · two numbers in brackets, in a fixed order
- ordered pair → **two numbers in brackets, in a fixed order**
- ordinate → **the second number of an ordered pair**
- x-axis → **the horizontal axis**
- abscissa → **the first number of an ordered pair**

Full working after a second miss:

> The right pairs are:  
> ordered pair → two numbers in brackets, in a fixed order  
> ordinate → the second number of an ordered pair  
> x-axis → the horizontal axis  
> abscissa → the first number of an ordered pair  

Sources: coordinates (Cartesian coordinates in the plane: x-axis and y-axis, origin O(0, 0), ordered pair (abscissa, ordinate))

### `m2-13-c1` · Lesson 13 · multiple choice, level 1

Prompt: Which statement is true?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ The origin O has coordinates (0, 0)
- ✅ The x-axis is horizontal
- ✅ The y-axis is vertical
- ✅ The x-axis and the y-axis are perpendicular
- ❌ The origin O has coordinates (1, 1)  
  _↳ The origin is where the axes cross: both coordinates are 0._
- ❌ The x-axis is vertical  
  _↳ The x-axis is the horizontal one._
- ❌ The y-axis is horizontal  
  _↳ The y-axis is the vertical one._
- ❌ The x-axis and the y-axis are parallel  
  _↳ The axes cross at the origin, at a right angle: they are perpendicular._


Three generated variants:

> Which statement is true?

- ◻️ The y-axis is horizontal  
  _↳ feedback if chosen: The y-axis is the vertical one._
- ◻️ The x-axis and the y-axis are parallel  
  _↳ feedback if chosen: The axes cross at the origin, at a right angle: they are perpendicular._
- ✅ The y-axis is vertical

Full working after a second miss:

> The true statement is “The y-axis is vertical”.  
> “The y-axis is horizontal” is false: The y-axis is the vertical one.  
> “The x-axis and the y-axis are parallel” is false: The axes cross at the origin, at a right angle: they are perpendicular.  

> Which statement is true?

- ◻️ The x-axis is vertical  
  _↳ feedback if chosen: The x-axis is the horizontal one._
- ✅ The y-axis is vertical
- ◻️ The origin O has coordinates (1, 1)  
  _↳ feedback if chosen: The origin is where the axes cross: both coordinates are 0._

Full working after a second miss:

> The true statement is “The y-axis is vertical”.  
> “The x-axis is vertical” is false: The x-axis is the horizontal one.  
> “The origin O has coordinates (1, 1)” is false: The origin is where the axes cross: both coordinates are 0.  

> Which statement is true?

- ◻️ The origin O has coordinates (1, 1)  
  _↳ feedback if chosen: The origin is where the axes cross: both coordinates are 0._
- ◻️ The y-axis is horizontal  
  _↳ feedback if chosen: The y-axis is the vertical one._
- ✅ The origin O has coordinates (0, 0)

Full working after a second miss:

> The true statement is “The origin O has coordinates (0, 0)”.  
> “The origin O has coordinates (1, 1)” is false: The origin is where the axes cross: both coordinates are 0.  
> “The y-axis is horizontal” is false: The y-axis is the vertical one.  

Sources: coordinates (Cartesian coordinates in the plane: x-axis and y-axis, origin O(0, 0), ordered pair (abscissa, ordinate))

### `m2-17-c3` · Lesson 17 · multiple choice, level 1

Prompt: Which pair are like terms?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ {mono(a, 'ab')} and {mono(b, 'ba')}
- ✅ {mono(a, 'xy')} and {mono(b, 'yx')}
- ✅ {mono(a, 'pq')} and {mono(b, 'qp')}
- ❌ {mono(a, 'ab')} and {mono(b, 'a')}  
  _↳ {mono(b, 'a')} has only the letter a; {mono(a, 'ab')} has a and b._
- ❌ {mono(a, 'xy')} and {mono(b, 'x²y')}  
  _↳ x²y has x squared; xy has x on its own._
- ❌ {mono(a, 'pq')} and {mono(a, 'p')}  
  _↳ {mono(a, 'p')} has only the letter p._
- ❌ {mono(a, 'x')} and {mono(a, 'y')}  
  _↳ The letters are different._


Three generated variants:

> Which pair are like terms?

- ✅ 6xy and 5yx
- ◻️ 6xy and 5x²y  
  _↳ feedback if chosen: x²y has x squared; xy has x on its own._
- ◻️ 6pq and 6p  
  _↳ feedback if chosen: 6p has only the letter p._

Full working after a second miss:

> The true statement is “6xy and 5yx”.  
> “6xy and 5x²y” is false: x²y has x squared; xy has x on its own.  
> “6pq and 6p” is false: 6p has only the letter p.  

> Which pair are like terms?

- ✅ 8xy and 4yx
- ◻️ 8pq and 8p  
  _↳ feedback if chosen: 8p has only the letter p._
- ◻️ 8x and 8y  
  _↳ feedback if chosen: The letters are different._

Full working after a second miss:

> The true statement is “8xy and 4yx”.  
> “8pq and 8p” is false: 8p has only the letter p.  
> “8x and 8y” is false: The letters are different.  

> Which pair are like terms?

- ◻️ 4xy and 5x²y  
  _↳ feedback if chosen: x²y has x squared; xy has x on its own._
- ◻️ 4x and 4y  
  _↳ feedback if chosen: The letters are different._
- ✅ 4ab and 5ba

Full working after a second miss:

> The true statement is “4ab and 5ba”.  
> “4xy and 5x²y” is false: x²y has x squared; xy has x on its own.  
> “4x and 4y” is false: The letters are different.  

Sources: like-terms (Definition of like terms (same letters with the same powers))

### `m2-29-def` · Lesson 29 · matching, level 1

Prompt: Match each line of a triangle to what it is.

Pairs (4 shown each time):

- a height → **from a vertex, perpendicular to the opposite side**
- a median → **from a vertex to the midpoint of the opposite side**
- a perpendicular bisector → **perpendicular to a side at its midpoint**
- an angle bisector → **cuts an angle into two equal angles**


Three generated variants:

> Match each line of a triangle to what it is.

Right-hand side (shuffled): perpendicular to a side at its midpoint · from a vertex to the midpoint of the opposite side · from a vertex, perpendicular to the opposite side · cuts an angle into two equal angles
- a perpendicular bisector → **perpendicular to a side at its midpoint**
- a median → **from a vertex to the midpoint of the opposite side**
- an angle bisector → **cuts an angle into two equal angles**
- a height → **from a vertex, perpendicular to the opposite side**

Full working after a second miss:

> The right pairs are:  
> a perpendicular bisector → perpendicular to a side at its midpoint  
> a median → from a vertex to the midpoint of the opposite side  
> an angle bisector → cuts an angle into two equal angles  
> a height → from a vertex, perpendicular to the opposite side  

> Match each line of a triangle to what it is.

Right-hand side (shuffled): from a vertex, perpendicular to the opposite side · cuts an angle into two equal angles · perpendicular to a side at its midpoint · from a vertex to the midpoint of the opposite side
- a height → **from a vertex, perpendicular to the opposite side**
- a median → **from a vertex to the midpoint of the opposite side**
- an angle bisector → **cuts an angle into two equal angles**
- a perpendicular bisector → **perpendicular to a side at its midpoint**

Full working after a second miss:

> The right pairs are:  
> a height → from a vertex, perpendicular to the opposite side  
> a median → from a vertex to the midpoint of the opposite side  
> an angle bisector → cuts an angle into two equal angles  
> a perpendicular bisector → perpendicular to a side at its midpoint  

> Match each line of a triangle to what it is.

Right-hand side (shuffled): perpendicular to a side at its midpoint · from a vertex, perpendicular to the opposite side · cuts an angle into two equal angles · from a vertex to the midpoint of the opposite side
- a perpendicular bisector → **perpendicular to a side at its midpoint**
- a median → **from a vertex to the midpoint of the opposite side**
- a height → **from a vertex, perpendicular to the opposite side**
- an angle bisector → **cuts an angle into two equal angles**

Full working after a second miss:

> The right pairs are:  
> a perpendicular bisector → perpendicular to a side at its midpoint  
> a median → from a vertex to the midpoint of the opposite side  
> a height → from a vertex, perpendicular to the opposite side  
> an angle bisector → cuts an angle into two equal angles  

Sources: triangles (Angle sum of a triangle, exterior angle, special lines and their meeting points, isosceles/equilateral/right-angled triangles, Pythagoras’ theorem and its converse (integral triples), area ½bh)

### `m2-29-point` · Lesson 29 · matching, level 2

Prompt: Match each set of three lines to the point where they meet.

Pairs (4 shown each time):

- the three heights → **the orthocentre**
- the three medians → **the centroid**
- the three perpendicular bisectors → **the circumcentre**
- the three angle bisectors → **the incentre**


Three generated variants:

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the centroid · the orthocentre · the circumcentre · the incentre
- the three perpendicular bisectors → **the circumcentre**
- the three heights → **the orthocentre**
- the three angle bisectors → **the incentre**
- the three medians → **the centroid**

Full working after a second miss:

> The right pairs are:  
> the three perpendicular bisectors → the circumcentre  
> the three heights → the orthocentre  
> the three angle bisectors → the incentre  
> the three medians → the centroid  

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the incentre · the centroid · the circumcentre · the orthocentre
- the three medians → **the centroid**
- the three heights → **the orthocentre**
- the three perpendicular bisectors → **the circumcentre**
- the three angle bisectors → **the incentre**

Full working after a second miss:

> The right pairs are:  
> the three medians → the centroid  
> the three heights → the orthocentre  
> the three perpendicular bisectors → the circumcentre  
> the three angle bisectors → the incentre  

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the incentre · the orthocentre · the circumcentre · the centroid
- the three perpendicular bisectors → **the circumcentre**
- the three medians → **the centroid**
- the three angle bisectors → **the incentre**
- the three heights → **the orthocentre**

Full working after a second miss:

> The right pairs are:  
> the three perpendicular bisectors → the circumcentre  
> the three medians → the centroid  
> the three angle bisectors → the incentre  
> the three heights → the orthocentre  

Sources: triangles (Angle sum of a triangle, exterior angle, special lines and their meeting points, isosceles/equilateral/right-angled triangles, Pythagoras’ theorem and its converse (integral triples), area ½bh)

### `m2-29-spot` · Lesson 29 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A median joins a vertex to the midpoint of the opposite side.
- ✅ The circumcentre is where the perpendicular bisectors meet.
- ✅ A height is perpendicular to a side.
- ✅ An angle bisector cuts an angle into two equal angles.
- ❌ A median is always perpendicular to the opposite side.  
  _↳ That is a height; a median goes to the midpoint._
- ❌ The centroid is where the heights meet.  
  _↳ The heights meet at the orthocentre; the medians meet at the centroid._
- ❌ The incentre is the centre of the circle through the three vertices.  
  _↳ That is the circumcentre; the incentre is the centre of the circle inside the triangle._


Three generated variants:

> Which statement is wrong?

- ◻️ The circumcentre is where the perpendicular bisectors meet.
- ◻️ A median joins a vertex to the midpoint of the opposite side.
- ✅ A median is always perpendicular to the opposite side.  
  _↳ explanation: That is a height; a median goes to the midpoint._
- ◻️ An angle bisector cuts an angle into two equal angles.

Full working after a second miss:

> The wrong statement is “A median is always perpendicular to the opposite side.”.  
> That is a height; a median goes to the midpoint.  

> Which statement is wrong?

- ✅ A median is always perpendicular to the opposite side.  
  _↳ explanation: That is a height; a median goes to the midpoint._
- ◻️ The circumcentre is where the perpendicular bisectors meet.
- ◻️ A height is perpendicular to a side.
- ◻️ An angle bisector cuts an angle into two equal angles.

Full working after a second miss:

> The wrong statement is “A median is always perpendicular to the opposite side.”.  
> That is a height; a median goes to the midpoint.  

> Which statement is wrong?

- ◻️ The circumcentre is where the perpendicular bisectors meet.
- ✅ A median is always perpendicular to the opposite side.  
  _↳ explanation: That is a height; a median goes to the midpoint._
- ◻️ A median joins a vertex to the midpoint of the opposite side.
- ◻️ A height is perpendicular to a side.

Full working after a second miss:

> The wrong statement is “A median is always perpendicular to the opposite side.”.  
> That is a height; a median goes to the midpoint.  

Sources: triangles (Angle sum of a triangle, exterior angle, special lines and their meeting points, isosceles/equilateral/right-angled triangles, Pythagoras’ theorem and its converse (integral triples), area ½bh)

### `m2-29-point-card` · Lesson 29 · matching, level 1

Prompt: Match each set of three lines to the point where they meet.

Pairs (4 shown each time):

- the three heights → **the orthocentre**
- the three medians → **the centroid**
- the three perpendicular bisectors → **the circumcentre**
- the three angle bisectors → **the incentre**


Three generated variants:

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the centroid · the incentre · the orthocentre · the circumcentre
- the three heights → **the orthocentre**
- the three perpendicular bisectors → **the circumcentre**
- the three angle bisectors → **the incentre**
- the three medians → **the centroid**

Full working after a second miss:

> The right pairs are:  
> the three heights → the orthocentre  
> the three perpendicular bisectors → the circumcentre  
> the three angle bisectors → the incentre  
> the three medians → the centroid  

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the incentre · the circumcentre · the centroid · the orthocentre
- the three angle bisectors → **the incentre**
- the three perpendicular bisectors → **the circumcentre**
- the three heights → **the orthocentre**
- the three medians → **the centroid**

Full working after a second miss:

> The right pairs are:  
> the three angle bisectors → the incentre  
> the three perpendicular bisectors → the circumcentre  
> the three heights → the orthocentre  
> the three medians → the centroid  

> Match each set of three lines to the point where they meet.

Right-hand side (shuffled): the centroid · the incentre · the orthocentre · the circumcentre
- the three heights → **the orthocentre**
- the three perpendicular bisectors → **the circumcentre**
- the three medians → **the centroid**
- the three angle bisectors → **the incentre**

Full working after a second miss:

> The right pairs are:  
> the three heights → the orthocentre  
> the three perpendicular bisectors → the circumcentre  
> the three medians → the centroid  
> the three angle bisectors → the incentre  

Sources: triangles (Angle sum of a triangle, exterior angle, special lines and their meeting points, isosceles/equilateral/right-angled triangles, Pythagoras’ theorem and its converse (integral triples), area ½bh)

### `m2-30-spot` · Lesson 30 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ An equilateral triangle has three angles of 60°.
- ✅ The hypotenuse is the longest side of a right-angled triangle.
- ✅ An isosceles triangle has two equal angles.
- ✅ A triangle can be both right-angled and isosceles.
- ❌ A scalene triangle has two equal sides.  
  _↳ A scalene triangle has no equal sides._
- ❌ An equilateral triangle can have a right angle.  
  _↳ Its angles are all 60°._
- ❌ The hypotenuse is next to the right angle.  
  _↳ The hypotenuse is opposite the right angle._


Three generated variants:

> Which statement is wrong?

- ✅ An equilateral triangle can have a right angle.  
  _↳ explanation: Its angles are all 60°._
- ◻️ An equilateral triangle has three angles of 60°.
- ◻️ A triangle can be both right-angled and isosceles.
- ◻️ The hypotenuse is the longest side of a right-angled triangle.

Full working after a second miss:

> The wrong statement is “An equilateral triangle can have a right angle.”.  
> Its angles are all 60°.  

> Which statement is wrong?

- ◻️ An isosceles triangle has two equal angles.
- ✅ The hypotenuse is next to the right angle.  
  _↳ explanation: The hypotenuse is opposite the right angle._
- ◻️ An equilateral triangle has three angles of 60°.
- ◻️ The hypotenuse is the longest side of a right-angled triangle.

Full working after a second miss:

> The wrong statement is “The hypotenuse is next to the right angle.”.  
> The hypotenuse is opposite the right angle.  

> Which statement is wrong?

- ◻️ The hypotenuse is the longest side of a right-angled triangle.
- ◻️ An equilateral triangle has three angles of 60°.
- ◻️ An isosceles triangle has two equal angles.
- ✅ The hypotenuse is next to the right angle.  
  _↳ explanation: The hypotenuse is opposite the right angle._

Full working after a second miss:

> The wrong statement is “The hypotenuse is next to the right angle.”.  
> The hypotenuse is opposite the right angle.  

Sources: triangles (Angle sum of a triangle, exterior angle, special lines and their meeting points, isosceles/equilateral/right-angled triangles, Pythagoras’ theorem and its converse (integral triples), area ½bh)

### `m2-37-kind` · Lesson 37 · multiple choice, level 1

Prompt: Is {X.x} rational or irrational?

Table `X` (one row is picked each time):

| r | w | e | y | x |
|---|---|---|---|---|
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | √49 = 7, a whole number. | √49 |
| irrational | rational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | 2 is not a perfect square: √2 = 1.414… never ends or repeats. | √2 |
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | It repeats: it is 1/3. | 0.333… |
| irrational | rational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | π = 3.14159… never ends or repeats. | π |
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | It is a fraction of two whole numbers. | 3/7 |
| irrational | rational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | 50 is not a perfect square. | √50 |
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | 1.25 = 5/4. | 1.25 |
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | √(16/25) = 4/5. | √(16/25) |
| rational | irrational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | −6 = −6/1. | −6 |
| irrational | rational · a natural number only · neither | Look at its decimal: does it end or repeat? · Ask whether it is a fraction of whole numbers. · Every real number is either rational or irrational. | 10 is not a perfect square. | √10 |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is √50 rational or irrational?

- ✅ irrational
- ◻️ rational  
  _↳ feedback if chosen: Look at its decimal: does it end or repeat?_
- ◻️ neither  
  _↳ feedback if chosen: Every real number is either rational or irrational._
- ◻️ a natural number only  
  _↳ feedback if chosen: Ask whether it is a fraction of whole numbers._

Full working after a second miss:

> 50 is not a perfect square.  
> So the answer is “irrational”.  

> Is 3/7 rational or irrational?

- ◻️ irrational  
  _↳ feedback if chosen: Look at its decimal: does it end or repeat?_
- ✅ rational
- ◻️ a natural number only  
  _↳ feedback if chosen: Ask whether it is a fraction of whole numbers._
- ◻️ neither  
  _↳ feedback if chosen: Every real number is either rational or irrational._

Full working after a second miss:

> It is a fraction of two whole numbers.  
> So the answer is “rational”.  

> Is √10 rational or irrational?

- ◻️ rational  
  _↳ feedback if chosen: Look at its decimal: does it end or repeat?_
- ◻️ a natural number only  
  _↳ feedback if chosen: Ask whether it is a fraction of whole numbers._
- ✅ irrational
- ◻️ neither  
  _↳ feedback if chosen: Every real number is either rational or irrational._

Full working after a second miss:

> 10 is not a perfect square.  
> So the answer is “irrational”.  

Sources: real-numbers (Square roots, rational and irrational numbers, ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, simplifying √(a²b))

### `m2-38-set` · Lesson 38 · multiple choice, level 1

Prompt: What is the smallest of the sets ℕ, ℤ, ℚ, ℝ that contains {X.x}?

Table `X` (one row is picked each time):

| r | w | e | y | x |
|---|---|---|---|---|
| ℕ | ℤ · ℚ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | 7 is a natural number. | 7 |
| ℤ | ℕ · ℚ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | −4 is an integer but not natural. | −4 |
| ℚ | ℕ · ℤ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | 2/3 is a fraction, not an integer. | 2/3 |
| ℝ | ℕ · ℤ · ℚ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | √5 is irrational: it is only in ℝ. | √5 |
| ℚ | ℕ · ℤ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | 0.75 = 3/4. | 0.75 |
| ℝ | ℕ · ℤ · ℚ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | π is irrational. | π |
| ℕ | ℤ · ℚ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | √36 = 6. | √36 |
| ℚ | ℕ · ℤ · ℝ | Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? · Check: is it a whole number, an integer, a fraction? | −1/2 is a fraction. | −1/2 |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the smallest of the sets ℕ, ℤ, ℚ, ℝ that contains 7?

- ✅ ℕ
- ◻️ ℚ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℤ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℝ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_

Full working after a second miss:

> 7 is a natural number.  
> So the answer is “ℕ”.  

> What is the smallest of the sets ℕ, ℤ, ℚ, ℝ that contains −1/2?

- ✅ ℚ
- ◻️ ℝ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℤ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℕ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_

Full working after a second miss:

> −1/2 is a fraction.  
> So the answer is “ℚ”.  

> What is the smallest of the sets ℕ, ℤ, ℚ, ℝ that contains −1/2?

- ◻️ ℕ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℤ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ◻️ ℝ  
  _↳ feedback if chosen: Check: is it a whole number, an integer, a fraction?_
- ✅ ℚ

Full working after a second miss:

> −1/2 is a fraction.  
> So the answer is “ℚ”.  

Sources: real-numbers (Square roots, rational and irrational numbers, ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, simplifying √(a²b))

### `m2-38-order` · Lesson 38 · ordering, level 1

Prompt: Put these numbers in order, from the smallest.

Table `X` (one row is picked each time):

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| −2 | −0.5 | √2 | 1.5 | π |
| −3/2 | 0 | 0.9 | √3 | 2 |
| −√4 | −1.5 | 1/3 | √2 | 1.5 |
| −π | −3 | −√5 | −1 | 0.5 |

Items in the right order:

1. {X[0]}
2. {X[1]}
3. {X[2]}
4. {X[3]}
5. {X[4]}


Three generated variants:

> Put these numbers in order, from the smallest.

Shown as: √3 · 0.9 · 2 · 0 · −3/2
Correct order: −3/2 → 0 → 0.9 → √3 → 2

Full working after a second miss:

> The correct order is: −3/2 → 0 → 0.9 → √3 → 2.  

> Put these numbers in order, from the smallest.

Shown as: √3 · −3/2 · 0 · 2 · 0.9
Correct order: −3/2 → 0 → 0.9 → √3 → 2

Full working after a second miss:

> The correct order is: −3/2 → 0 → 0.9 → √3 → 2.  

> Put these numbers in order, from the smallest.

Shown as: √2 · −0.5 · −2 · 1.5 · π
Correct order: −2 → −0.5 → √2 → 1.5 → π

Full working after a second miss:

> The correct order is: −2 → −0.5 → √2 → 1.5 → π.  

Sources: real-numbers (Square roots, rational and irrational numbers, ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, simplifying √(a²b))

### `m2-38-spot` · Lesson 38 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Every integer is a rational number.
- ✅ √2 is a real number.
- ✅ Every natural number is an integer.
- ✅ π is irrational.
- ❌ Every real number is rational.  
  _↳ Irrational numbers like √2 and π are real but not rational._
- ❌ −5 is a natural number.  
  _↳ Natural numbers are 0, 1, 2 …; −5 is an integer._
- ❌ 1/2 is not a real number.  
  _↳ Every fraction is a real number._


Three generated variants:

> Which statement is wrong?

- ◻️ Every integer is a rational number.
- ◻️ π is irrational.
- ◻️ √2 is a real number.
- ✅ −5 is a natural number.  
  _↳ explanation: Natural numbers are 0, 1, 2 …; −5 is an integer._

Full working after a second miss:

> The wrong statement is “−5 is a natural number.”.  
> Natural numbers are 0, 1, 2 …; −5 is an integer.  

> Which statement is wrong?

- ◻️ π is irrational.
- ✅ −5 is a natural number.  
  _↳ explanation: Natural numbers are 0, 1, 2 …; −5 is an integer._
- ◻️ Every integer is a rational number.
- ◻️ Every natural number is an integer.

Full working after a second miss:

> The wrong statement is “−5 is a natural number.”.  
> Natural numbers are 0, 1, 2 …; −5 is an integer.  

> Which statement is wrong?

- ◻️ π is irrational.
- ◻️ Every natural number is an integer.
- ✅ Every real number is rational.  
  _↳ explanation: Irrational numbers like √2 and π are real but not rational._
- ◻️ Every integer is a rational number.

Full working after a second miss:

> The wrong statement is “Every real number is rational.”.  
> Irrational numbers like √2 and π are real but not rational.  

Sources: real-numbers (Square roots, rational and irrational numbers, ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, simplifying √(a²b))

### `m2-41-which` · Lesson 41 · multiple choice, level 3

Prompt: Is this direct or inverse proportion? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The number of tins bought and the total cost. | direct | inverse · neither · both | More tins cost more: both go up together. · The cost per tin is fixed. · It is only one kind. | Twice the tins → twice the cost. |
| The number of taps filling a tank and the time it takes. | inverse | direct · neither · both | More taps → less time. · The volume of the tank is fixed. · It is only one kind. | Twice the taps → half the time. |
| The speed of a car and the time for a fixed journey. | inverse | direct · neither · both | Faster → less time. · speed × time = distance is fixed. · It is only one kind. | Speed × time stays the same. |
| The distance a car travels at a fixed speed and the time taken. | direct | inverse · neither · both | More time → more distance. · distance ÷ time is fixed. · It is only one kind. | Distance ÷ time stays the same. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this direct or inverse proportion? The speed of a car and the time for a fixed journey.

- ✅ inverse
- ◻️ both  
  _↳ feedback if chosen: It is only one kind._
- ◻️ neither  
  _↳ feedback if chosen: speed × time = distance is fixed._
- ◻️ direct  
  _↳ feedback if chosen: Faster → less time._

Full working after a second miss:

> Speed × time stays the same.  
> So the answer is “inverse”.  

> Is this direct or inverse proportion? The speed of a car and the time for a fixed journey.

- ◻️ direct  
  _↳ feedback if chosen: Faster → less time._
- ◻️ neither  
  _↳ feedback if chosen: speed × time = distance is fixed._
- ✅ inverse
- ◻️ both  
  _↳ feedback if chosen: It is only one kind._

Full working after a second miss:

> Speed × time stays the same.  
> So the answer is “inverse”.  

> Is this direct or inverse proportion? The speed of a car and the time for a fixed journey.

- ◻️ neither  
  _↳ feedback if chosen: speed × time = distance is fixed._
- ◻️ both  
  _↳ feedback if chosen: It is only one kind._
- ✅ inverse
- ◻️ direct  
  _↳ feedback if chosen: Faster → less time._

Full working after a second miss:

> Speed × time stays the same.  
> So the answer is “inverse”.  

Sources: proportion (Direct and inverse proportion, unitary method)

### `m2-41-which-card` · Lesson 41 · multiple choice, level 1

Prompt: Is this direct or inverse proportion? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The number of tins bought and the total cost. | direct | inverse · neither · both | More tins cost more: both go up together. · The cost per tin is fixed. · It is only one kind. | Twice the tins → twice the cost. |
| The number of taps filling a tank and the time it takes. | inverse | direct · neither · both | More taps → less time. · The volume of the tank is fixed. · It is only one kind. | Twice the taps → half the time. |
| The speed of a car and the time for a fixed journey. | inverse | direct · neither · both | Faster → less time. · speed × time = distance is fixed. · It is only one kind. | Speed × time stays the same. |
| The distance a car travels at a fixed speed and the time taken. | direct | inverse · neither · both | More time → more distance. · distance ÷ time is fixed. · It is only one kind. | Distance ÷ time stays the same. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this direct or inverse proportion? The number of tins bought and the total cost.

- ◻️ both  
  _↳ feedback if chosen: It is only one kind._
- ◻️ inverse  
  _↳ feedback if chosen: More tins cost more: both go up together._
- ✅ direct
- ◻️ neither  
  _↳ feedback if chosen: The cost per tin is fixed._

Full working after a second miss:

> Twice the tins → twice the cost.  
> So the answer is “direct”.  

> Is this direct or inverse proportion? The distance a car travels at a fixed speed and the time taken.

- ◻️ inverse  
  _↳ feedback if chosen: More time → more distance._
- ✅ direct
- ◻️ both  
  _↳ feedback if chosen: It is only one kind._
- ◻️ neither  
  _↳ feedback if chosen: distance ÷ time is fixed._

Full working after a second miss:

> Distance ÷ time stays the same.  
> So the answer is “direct”.  

> Is this direct or inverse proportion? The distance a car travels at a fixed speed and the time taken.

- ◻️ both  
  _↳ feedback if chosen: It is only one kind._
- ◻️ neither  
  _↳ feedback if chosen: distance ÷ time is fixed._
- ✅ direct
- ◻️ inverse  
  _↳ feedback if chosen: More time → more distance._

Full working after a second miss:

> Distance ÷ time stays the same.  
> So the answer is “direct”.  

Sources: proportion (Direct and inverse proportion, unitary method)

### `m2-49-spot` · Lesson 49 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The opposite sides of a parallelogram are equal.
- ✅ A rectangle has equal diagonals.
- ✅ The diagonals of a rhombus are perpendicular.
- ✅ A regular hexagon has six lines of symmetry.
- ❌ All the angles of a parallelogram are equal.  
  _↳ Only opposite angles are equal; angles next to each other add up to 180°._
- ❌ The diagonals of every parallelogram are equal.  
  _↳ Only a rectangle (or a square) has equal diagonals._
- ❌ A regular pentagon has ten lines of symmetry.  
  _↳ A regular polygon with n sides has n lines of symmetry: five._


Three generated variants:

> Which statement is wrong?

- ✅ A regular pentagon has ten lines of symmetry.  
  _↳ explanation: A regular polygon with n sides has n lines of symmetry: five._
- ◻️ The opposite sides of a parallelogram are equal.
- ◻️ The diagonals of a rhombus are perpendicular.
- ◻️ A rectangle has equal diagonals.

Full working after a second miss:

> The wrong statement is “A regular pentagon has ten lines of symmetry.”.  
> A regular polygon with n sides has n lines of symmetry: five.  

> Which statement is wrong?

- ◻️ A rectangle has equal diagonals.
- ✅ A regular pentagon has ten lines of symmetry.  
  _↳ explanation: A regular polygon with n sides has n lines of symmetry: five._
- ◻️ The diagonals of a rhombus are perpendicular.
- ◻️ The opposite sides of a parallelogram are equal.

Full working after a second miss:

> The wrong statement is “A regular pentagon has ten lines of symmetry.”.  
> A regular polygon with n sides has n lines of symmetry: five.  

> Which statement is wrong?

- ◻️ A rectangle has equal diagonals.
- ◻️ A regular hexagon has six lines of symmetry.
- ✅ All the angles of a parallelogram are equal.  
  _↳ explanation: Only opposite angles are equal; angles next to each other add up to 180°._
- ◻️ The diagonals of a rhombus are perpendicular.

Full working after a second miss:

> The wrong statement is “All the angles of a parallelogram are equal.”.  
> Only opposite angles are equal; angles next to each other add up to 180°.  

Sources: polygons (Names of polygons, angle sum (n − 2) × 180°, regular polygons, properties of parallelograms, areas of parallelogram and trapezium)

### `m2-52-what` · Lesson 52 · multiple choice, level 2

Prompt: Which statement is true?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ The image of two perpendicular lines by a reflection is two perpendicular lines.
- ✅ The image of three points on a line by a half turn is three points on a line.
- ✅ The image of two parallel lines by a reflection is two parallel lines.
- ❌ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ Symmetry keeps lengths, so all four sides stay equal._
- ❌ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ Symmetry keeps angles: it is still 30°._
- ❌ The image of a segment of 4 cm by a reflection is a segment of 8 cm.  
  _↳ Symmetry keeps lengths: still 4 cm._


Three generated variants:

> Which statement is true?

- ✅ The image of three points on a line by a half turn is three points on a line.
- ◻️ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ feedback if chosen: Symmetry keeps lengths, so all four sides stay equal._
- ◻️ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ feedback if chosen: Symmetry keeps angles: it is still 30°._

Full working after a second miss:

> The true statement is “The image of three points on a line by a half turn is three points on a line.”.  
> “The image of a square by a reflection can be a rectangle that is not a square.” is false: Symmetry keeps lengths, so all four sides stay equal.  
> “The image of an angle of 30° by a half turn is an angle of 150°.” is false: Symmetry keeps angles: it is still 30°.  

> Which statement is true?

- ◻️ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ feedback if chosen: Symmetry keeps angles: it is still 30°._
- ✅ The image of two parallel lines by a reflection is two parallel lines.
- ◻️ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ feedback if chosen: Symmetry keeps lengths, so all four sides stay equal._

Full working after a second miss:

> The true statement is “The image of two parallel lines by a reflection is two parallel lines.”.  
> “The image of an angle of 30° by a half turn is an angle of 150°.” is false: Symmetry keeps angles: it is still 30°.  
> “The image of a square by a reflection can be a rectangle that is not a square.” is false: Symmetry keeps lengths, so all four sides stay equal.  

> Which statement is true?

- ◻️ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ feedback if chosen: Symmetry keeps angles: it is still 30°._
- ◻️ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ feedback if chosen: Symmetry keeps lengths, so all four sides stay equal._
- ✅ The image of two parallel lines by a reflection is two parallel lines.

Full working after a second miss:

> The true statement is “The image of two parallel lines by a reflection is two parallel lines.”.  
> “The image of an angle of 30° by a half turn is an angle of 150°.” is false: Symmetry keeps angles: it is still 30°.  
> “The image of a square by a reflection can be a rectangle that is not a square.” is false: Symmetry keeps lengths, so all four sides stay equal.  

Sources: symmetry (Line and point symmetry; reflections and half turns on a grid; what symmetry conserves)

### `m2-52-spot` · Lesson 52 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A reflection keeps lengths.
- ✅ A half turn keeps angles.
- ✅ The image of a square by a reflection is a square.
- ✅ Images of parallel lines are parallel.
- ❌ A reflection doubles lengths.  
  _↳ A reflection keeps lengths._
- ❌ The image of a right angle by a half turn can be 120°.  
  _↳ Symmetry keeps angles: a right angle stays a right angle._
- ❌ Points on a line can have images that are not on a line.  
  _↳ Symmetry keeps alignment._


Three generated variants:

> Which statement is wrong?

- ✅ A reflection doubles lengths.  
  _↳ explanation: A reflection keeps lengths._
- ◻️ A half turn keeps angles.
- ◻️ A reflection keeps lengths.
- ◻️ The image of a square by a reflection is a square.

Full working after a second miss:

> The wrong statement is “A reflection doubles lengths.”.  
> A reflection keeps lengths.  

> Which statement is wrong?

- ✅ Points on a line can have images that are not on a line.  
  _↳ explanation: Symmetry keeps alignment._
- ◻️ The image of a square by a reflection is a square.
- ◻️ A reflection keeps lengths.
- ◻️ A half turn keeps angles.

Full working after a second miss:

> The wrong statement is “Points on a line can have images that are not on a line.”.  
> Symmetry keeps alignment.  

> Which statement is wrong?

- ◻️ A reflection keeps lengths.
- ◻️ Images of parallel lines are parallel.
- ✅ A reflection doubles lengths.  
  _↳ explanation: A reflection keeps lengths._
- ◻️ A half turn keeps angles.

Full working after a second miss:

> The wrong statement is “A reflection doubles lengths.”.  
> A reflection keeps lengths.  

Sources: symmetry (Line and point symmetry; reflections and half turns on a grid; what symmetry conserves)

### `m2-52-what-card` · Lesson 52 · multiple choice, level 1

Prompt: Which statement is true?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ The image of two perpendicular lines by a reflection is two perpendicular lines.
- ✅ The image of three points on a line by a half turn is three points on a line.
- ✅ The image of two parallel lines by a reflection is two parallel lines.
- ❌ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ Symmetry keeps lengths, so all four sides stay equal._
- ❌ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ Symmetry keeps angles: it is still 30°._
- ❌ The image of a segment of 4 cm by a reflection is a segment of 8 cm.  
  _↳ Symmetry keeps lengths: still 4 cm._


Three generated variants:

> Which statement is true?

- ✅ The image of two parallel lines by a reflection is two parallel lines.
- ◻️ The image of a segment of 4 cm by a reflection is a segment of 8 cm.  
  _↳ feedback if chosen: Symmetry keeps lengths: still 4 cm._
- ◻️ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ feedback if chosen: Symmetry keeps lengths, so all four sides stay equal._

Full working after a second miss:

> The true statement is “The image of two parallel lines by a reflection is two parallel lines.”.  
> “The image of a segment of 4 cm by a reflection is a segment of 8 cm.” is false: Symmetry keeps lengths: still 4 cm.  
> “The image of a square by a reflection can be a rectangle that is not a square.” is false: Symmetry keeps lengths, so all four sides stay equal.  

> Which statement is true?

- ◻️ The image of an angle of 30° by a half turn is an angle of 150°.  
  _↳ feedback if chosen: Symmetry keeps angles: it is still 30°._
- ◻️ The image of a segment of 4 cm by a reflection is a segment of 8 cm.  
  _↳ feedback if chosen: Symmetry keeps lengths: still 4 cm._
- ✅ The image of two perpendicular lines by a reflection is two perpendicular lines.

Full working after a second miss:

> The true statement is “The image of two perpendicular lines by a reflection is two perpendicular lines.”.  
> “The image of an angle of 30° by a half turn is an angle of 150°.” is false: Symmetry keeps angles: it is still 30°.  
> “The image of a segment of 4 cm by a reflection is a segment of 8 cm.” is false: Symmetry keeps lengths: still 4 cm.  

> Which statement is true?

- ◻️ The image of a square by a reflection can be a rectangle that is not a square.  
  _↳ feedback if chosen: Symmetry keeps lengths, so all four sides stay equal._
- ✅ The image of two perpendicular lines by a reflection is two perpendicular lines.
- ◻️ The image of a segment of 4 cm by a reflection is a segment of 8 cm.  
  _↳ feedback if chosen: Symmetry keeps lengths: still 4 cm._

Full working after a second miss:

> The true statement is “The image of two perpendicular lines by a reflection is two perpendicular lines.”.  
> “The image of a square by a reflection can be a rectangle that is not a square.” is false: Symmetry keeps lengths, so all four sides stay equal.  
> “The image of a segment of 4 cm by a reflection is a segment of 8 cm.” is false: Symmetry keeps lengths: still 4 cm.  

Sources: symmetry (Line and point symmetry; reflections and half turns on a grid; what symmetry conserves)

### `m2-53-centre` · Lesson 53 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where is the centre of the circumscribed circle of a triangle? | where the perpendicular bisectors of the sides meet | where the medians meet · where the heights meet · where the angle bisectors meet | That is the centroid. · That is the orthocentre. · That is the centre of the inscribed circle. | Every point of a perpendicular bisector is the same distance from both ends of the side. |
| Where is the centre of the circumscribed circle of a right-angled triangle? | at the midpoint of the hypotenuse | at the right-angle vertex · outside the triangle · at the midpoint of the shortest side | The right-angle vertex is on the circle. · For a right-angled triangle it is on the hypotenuse. · It is the midpoint of the longest side. | The hypotenuse is a diameter of the circle. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Where is the centre of the circumscribed circle of a triangle?

- ◻️ where the medians meet  
  _↳ feedback if chosen: That is the centroid._
- ◻️ where the heights meet  
  _↳ feedback if chosen: That is the orthocentre._
- ✅ where the perpendicular bisectors of the sides meet
- ◻️ where the angle bisectors meet  
  _↳ feedback if chosen: That is the centre of the inscribed circle._

Full working after a second miss:

> Every point of a perpendicular bisector is the same distance from both ends of the side.  
> So the answer is “where the perpendicular bisectors of the sides meet”.  

> Where is the centre of the circumscribed circle of a triangle?

- ◻️ where the angle bisectors meet  
  _↳ feedback if chosen: That is the centre of the inscribed circle._
- ◻️ where the medians meet  
  _↳ feedback if chosen: That is the centroid._
- ✅ where the perpendicular bisectors of the sides meet
- ◻️ where the heights meet  
  _↳ feedback if chosen: That is the orthocentre._

Full working after a second miss:

> Every point of a perpendicular bisector is the same distance from both ends of the side.  
> So the answer is “where the perpendicular bisectors of the sides meet”.  

> Where is the centre of the circumscribed circle of a right-angled triangle?

- ✅ at the midpoint of the hypotenuse
- ◻️ outside the triangle  
  _↳ feedback if chosen: For a right-angled triangle it is on the hypotenuse._
- ◻️ at the midpoint of the shortest side  
  _↳ feedback if chosen: It is the midpoint of the longest side._
- ◻️ at the right-angle vertex  
  _↳ feedback if chosen: The right-angle vertex is on the circle._

Full working after a second miss:

> The hypotenuse is a diameter of the circle.  
> So the answer is “at the midpoint of the hypotenuse”.  

Sources: circles (Circumscribed circle (circumcentre; midpoint of the hypotenuse) and the relative positions of two circles)

### `m2-53-spot` · Lesson 53 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The circumscribed circle passes through the three vertices.
- ✅ The circumcentre is the same distance from A, B and C.
- ✅ In a right-angled triangle the hypotenuse is a diameter of the circumscribed circle.
- ✅ Two perpendicular bisectors are enough to find the circumcentre.
- ❌ The circumcentre is always inside the triangle.  
  _↳ For an obtuse triangle it is outside; for a right-angled one it is on the hypotenuse._
- ❌ The circumcentre is where the medians meet.  
  _↳ The medians meet at the centroid._


Three generated variants:

> Which statement is wrong?

- ◻️ Two perpendicular bisectors are enough to find the circumcentre.
- ◻️ The circumcentre is the same distance from A, B and C.
- ◻️ In a right-angled triangle the hypotenuse is a diameter of the circumscribed circle.
- ✅ The circumcentre is where the medians meet.  
  _↳ explanation: The medians meet at the centroid._

Full working after a second miss:

> The wrong statement is “The circumcentre is where the medians meet.”.  
> The medians meet at the centroid.  

> Which statement is wrong?

- ◻️ In a right-angled triangle the hypotenuse is a diameter of the circumscribed circle.
- ✅ The circumcentre is where the medians meet.  
  _↳ explanation: The medians meet at the centroid._
- ◻️ Two perpendicular bisectors are enough to find the circumcentre.
- ◻️ The circumcentre is the same distance from A, B and C.

Full working after a second miss:

> The wrong statement is “The circumcentre is where the medians meet.”.  
> The medians meet at the centroid.  

> Which statement is wrong?

- ◻️ Two perpendicular bisectors are enough to find the circumcentre.
- ✅ The circumcentre is always inside the triangle.  
  _↳ explanation: For an obtuse triangle it is outside; for a right-angled one it is on the hypotenuse._
- ◻️ In a right-angled triangle the hypotenuse is a diameter of the circumscribed circle.
- ◻️ The circumcentre is the same distance from A, B and C.

Full working after a second miss:

> The wrong statement is “The circumcentre is always inside the triangle.”.  
> For an obtuse triangle it is outside; for a right-angled one it is on the hypotenuse.  

Sources: circles (Circumscribed circle (circumcentre; midpoint of the hypotenuse) and the relative positions of two circles)

