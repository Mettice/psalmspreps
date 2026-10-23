# Maths Form 4, Form Four Maths: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f4-maths`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `m4-9-step` | 9 | multiple choice, 2 | quadratic-equations |
| 2 | `m4-9-step-card` (card c4m9-3) | 9 | multiple choice, 1 | quadratic-equations |

### `m4-9-step` · Lesson 9 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Deriving the formula from ax² + bx + c = {0}, what is the first step? | Divide every term by a | Take the square root of both sides · Subtract b from both sides · Multiply every term by c | There is no square yet to take the root of; first make the x² coefficient {1}. · bx is a term with x; subtracting b alone does not keep the equation balanced. · Multiplying by c does not help; the aim is x² with coefficient {1}. | Dividing by a gives x² + (b/a)x + c/a = {0}, ready for completing the square. |
| After dividing by a and moving c/a, we have x² + (b/a)x = −c/a. What is added to both sides? | (b/{2}a)² | (b/a)² · b/{2}a · c/a | Half of the coefficient b/a is b/{2}a; square that, not b/a. · b/{2}a must be squared to complete the square. · c/a is already used; the added term comes from the x coefficient. | Half of b/a is b/{2}a; adding (b/{2}a)² makes the left side (x + b/{2}a)². |
| The completed square is (x + b/{2}a)² = (b² − {4}ac)/{4}a². What is the next step? | Take the square root of both sides, with ± | Divide both sides by {4}a² · Square both sides · Take the square root with + only | {4}a² is inside the fraction; the next step removes the square on the left. · Squaring makes it more complicated; we need to undo the square. · Both signs give roots; the ± is the reason a quadratic can have two roots. | x + b/{2}a = ±√(b² − {4}ac)/{2}a, then subtract b/{2}a. |
| Which expression decides how many real roots ax² + bx + c = {0} has? | b² − {4}ac | b² + {4}ac · {2}a · −b | The formula has b² minus {4}ac under the root. · {2}a is the denominator; it never changes the number of roots. · −b only shifts both roots together. | b² − {4}ac is under the square root: positive gives two roots, zero one, negative none. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Deriving the formula from ax² + bx + c = 0, what is the first step?

- ✅ Divide every term by a
- ◻️ Subtract b from both sides  
  _↳ feedback if chosen: bx is a term with x; subtracting b alone does not keep the equation balanced._
- ◻️ Multiply every term by c  
  _↳ feedback if chosen: Multiplying by c does not help; the aim is x² with coefficient 1._
- ◻️ Take the square root of both sides  
  _↳ feedback if chosen: There is no square yet to take the root of; first make the x² coefficient 1._

Full working after a second miss:

> Dividing by a gives x² + (b/a)x + c/a = 0, ready for completing the square.  
> So the answer is Divide every term by a.  

> Deriving the formula from ax² + bx + c = 0, what is the first step?

- ◻️ Multiply every term by c  
  _↳ feedback if chosen: Multiplying by c does not help; the aim is x² with coefficient 1._
- ◻️ Take the square root of both sides  
  _↳ feedback if chosen: There is no square yet to take the root of; first make the x² coefficient 1._
- ◻️ Subtract b from both sides  
  _↳ feedback if chosen: bx is a term with x; subtracting b alone does not keep the equation balanced._
- ✅ Divide every term by a

Full working after a second miss:

> Dividing by a gives x² + (b/a)x + c/a = 0, ready for completing the square.  
> So the answer is Divide every term by a.  

> After dividing by a and moving c/a, we have x² + (b/a)x = −c/a. What is added to both sides?

- ◻️ b/2a  
  _↳ feedback if chosen: b/2a must be squared to complete the square._
- ◻️ c/a  
  _↳ feedback if chosen: c/a is already used; the added term comes from the x coefficient._
- ◻️ (b/a)²  
  _↳ feedback if chosen: Half of the coefficient b/a is b/2a; square that, not b/a._
- ✅ (b/2a)²

Full working after a second miss:

> Half of b/a is b/2a; adding (b/2a)² makes the left side (x + b/2a)².  
> So the answer is (b/2a)².  

Sources: quadratic-equations (Form 4 Mathematics syllabus, Term 1, Algebraic processes: solving quadratic equations by factorisation, completing the square and the quadratic formula; forming equations from roots)

### `m4-9-step-card` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Deriving the formula from ax² + bx + c = {0}, what is the first step? | Divide every term by a | Take the square root of both sides · Subtract b from both sides · Multiply every term by c | There is no square yet to take the root of; first make the x² coefficient {1}. · bx is a term with x; subtracting b alone does not keep the equation balanced. · Multiplying by c does not help; the aim is x² with coefficient {1}. | Dividing by a gives x² + (b/a)x + c/a = {0}, ready for completing the square. |
| After dividing by a and moving c/a, we have x² + (b/a)x = −c/a. What is added to both sides? | (b/{2}a)² | (b/a)² · b/{2}a · c/a | Half of the coefficient b/a is b/{2}a; square that, not b/a. · b/{2}a must be squared to complete the square. · c/a is already used; the added term comes from the x coefficient. | Half of b/a is b/{2}a; adding (b/{2}a)² makes the left side (x + b/{2}a)². |
| The completed square is (x + b/{2}a)² = (b² − {4}ac)/{4}a². What is the next step? | Take the square root of both sides, with ± | Divide both sides by {4}a² · Square both sides · Take the square root with + only | {4}a² is inside the fraction; the next step removes the square on the left. · Squaring makes it more complicated; we need to undo the square. · Both signs give roots; the ± is the reason a quadratic can have two roots. | x + b/{2}a = ±√(b² − {4}ac)/{2}a, then subtract b/{2}a. |
| Which expression decides how many real roots ax² + bx + c = {0} has? | b² − {4}ac | b² + {4}ac · {2}a · −b | The formula has b² minus {4}ac under the root. · {2}a is the denominator; it never changes the number of roots. · −b only shifts both roots together. | b² − {4}ac is under the square root: positive gives two roots, zero one, negative none. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which expression decides how many real roots ax² + bx + c = 0 has?

- ◻️ 2a  
  _↳ feedback if chosen: 2a is the denominator; it never changes the number of roots._
- ◻️ b² + 4ac  
  _↳ feedback if chosen: The formula has b² minus 4ac under the root._
- ◻️ −b  
  _↳ feedback if chosen: −b only shifts both roots together._
- ✅ b² − 4ac

Full working after a second miss:

> b² − 4ac is under the square root: positive gives two roots, zero one, negative none.  
> So the answer is b² − 4ac.  

> Deriving the formula from ax² + bx + c = 0, what is the first step?

- ◻️ Subtract b from both sides  
  _↳ feedback if chosen: bx is a term with x; subtracting b alone does not keep the equation balanced._
- ◻️ Multiply every term by c  
  _↳ feedback if chosen: Multiplying by c does not help; the aim is x² with coefficient 1._
- ◻️ Take the square root of both sides  
  _↳ feedback if chosen: There is no square yet to take the root of; first make the x² coefficient 1._
- ✅ Divide every term by a

Full working after a second miss:

> Dividing by a gives x² + (b/a)x + c/a = 0, ready for completing the square.  
> So the answer is Divide every term by a.  

> Which expression decides how many real roots ax² + bx + c = 0 has?

- ◻️ −b  
  _↳ feedback if chosen: −b only shifts both roots together._
- ✅ b² − 4ac
- ◻️ 2a  
  _↳ feedback if chosen: 2a is the denominator; it never changes the number of roots._
- ◻️ b² + 4ac  
  _↳ feedback if chosen: The formula has b² minus 4ac under the root._

Full working after a second miss:

> b² − 4ac is under the square root: positive gives two roots, zero one, negative none.  
> So the answer is b² − 4ac.  

Sources: quadratic-equations (Form 4 Mathematics syllabus, Term 1, Algebraic processes: solving quadratic equations by factorisation, completing the square and the quadratic formula; forming equations from roots)

