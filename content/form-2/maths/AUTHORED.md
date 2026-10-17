# Maths Form 2, Batch M2-1: authored answers for review

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

