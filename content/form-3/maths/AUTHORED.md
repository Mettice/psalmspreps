# Maths Form 3, Form Three Maths: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f3-maths`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `m3-13-lin` | 13 | multiple choice, 1 | formulae |
| 2 | `m3-13-sq` | 13 | multiple choice, 2 | formulae |
| 3 | `m3-13-twice` | 13 | multiple choice, 3 | formulae |
| 4 | `m3-13-sq-card` (card c3m13-2) | 13 | multiple choice, 1 | formulae |
| 5 | `m3-14-form` | 14 | multiple choice, 1 | variation |
| 6 | `m3-15-form` | 15 | multiple choice, 1 | variation |
| 7 | `m3-15-graph` | 15 | multiple choice, 2 | variation |
| 8 | `m3-15-graph-card` (card c3m15-3) | 15 | multiple choice, 1 | variation |
| 9 | `m3-17-name` | 17 | multiple choice, 1 | trigonometry |
| 10 | `m3-18-exact` | 18 | multiple choice, 1 | trigonometry |
| 11 | `m3-18-value` | 18 | number, 2 | trigonometry |

### `m3-13-lin` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Make t the subject of v = u + at. | t = (v − u) ÷ a | t = v − u − a · t = (v + u) ÷ a · t = v ÷ a − u | a multiplies t: divide by a, do not subtract it. · u is added on the right: subtract it, do not add. · Subtract u first (it is added last), then divide by a. | Subtract u from both sides, then divide by a. |
| Make w the subject of P = 2l + 2w. | w = (P − 2l) ÷ 2 | w = P − 2l − 2 · w = (P + 2l) ÷ 2 · w = P ÷ 2 − 2l | 2 multiplies w: divide by 2, do not subtract it. · 2l is added: subtract it from both sides. · Divide the whole of P − 2l by 2. | Subtract 2l, then divide by 2. |
| Make x the subject of y = mx + c. | x = (y − c) ÷ m | x = y − c − m · x = (y + c) ÷ m · x = y ÷ m − c | m multiplies x: divide by m. · c is added: subtract it. · Subtract c first, then divide the whole of y − c by m. | Subtract c, then divide by m. |
| Make b the subject of A = ½(a + b)h. | b = 2A ÷ h − a | b = A ÷ 2h − a · b = 2A − h − a · b = 2Ah − a | Multiply by 2 to undo ½: 2A, then divide by h. · h multiplies the bracket: divide by h, do not subtract. · Divide by h, do not multiply. | Multiply by 2, divide by h, then subtract a. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Make w the subject of P = 2l + 2w.

- ◻️ w = P − 2l − 2  
  _↳ feedback if chosen: 2 multiplies w: divide by 2, do not subtract it._
- ◻️ w = P ÷ 2 − 2l  
  _↳ feedback if chosen: Divide the whole of P − 2l by 2._
- ◻️ w = (P + 2l) ÷ 2  
  _↳ feedback if chosen: 2l is added: subtract it from both sides._
- ✅ w = (P − 2l) ÷ 2

Full working after a second miss:

> Subtract 2l, then divide by 2.  
> So the answer is w = (P − 2l) ÷ 2.  

> Make t the subject of v = u + at.

- ✅ t = (v − u) ÷ a
- ◻️ t = v ÷ a − u  
  _↳ feedback if chosen: Subtract u first (it is added last), then divide by a._
- ◻️ t = v − u − a  
  _↳ feedback if chosen: a multiplies t: divide by a, do not subtract it._
- ◻️ t = (v + u) ÷ a  
  _↳ feedback if chosen: u is added on the right: subtract it, do not add._

Full working after a second miss:

> Subtract u from both sides, then divide by a.  
> So the answer is t = (v − u) ÷ a.  

> Make b the subject of A = ½(a + b)h.

- ✅ b = 2A ÷ h − a
- ◻️ b = A ÷ 2h − a  
  _↳ feedback if chosen: Multiply by 2 to undo ½: 2A, then divide by h._
- ◻️ b = 2A − h − a  
  _↳ feedback if chosen: h multiplies the bracket: divide by h, do not subtract._
- ◻️ b = 2Ah − a  
  _↳ feedback if chosen: Divide by h, do not multiply._

Full working after a second miss:

> Multiply by 2, divide by h, then subtract a.  
> So the answer is b = 2A ÷ h − a.  

Sources: formulae (Form 3 Mathematics syllabus, Term 1: transposition of formulae (change of subject))

### `m3-13-sq` · Lesson 13 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Make r the subject of A = πr². | r = √(A ÷ π) | r = A ÷ π² · r = √A ÷ π · r = (A ÷ π)² | Only r is squared: divide by π, then take the square root. · Take the square root of the whole of A ÷ π. · To undo a square, take the square root, do not square. | Divide by π, then take the square root. |
| Make v the subject of E = ½mv². | v = √(2E ÷ m) | v = 2E ÷ m² · v = √(E ÷ 2m) · v = (2E ÷ m)² | Only v is squared: undo it with a square root at the end. · Multiply by 2 to undo ½, do not divide. · To undo a square, take the square root. | Multiply by 2, divide by m, then take the square root. |
| Make x the subject of y = x² − k. | x = √(y + k) | x = √y − k · x = (y + k)² · x = √(y − k) | Add k first, then take the square root of the whole of y + k. · To undo a square, take the square root. · k is subtracted: add it to both sides. | Add k to both sides, then take the square root. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Make x the subject of y = x² − k.

- ◻️ x = (y + k)²  
  _↳ feedback if chosen: To undo a square, take the square root._
- ✅ x = √(y + k)
- ◻️ x = √(y − k)  
  _↳ feedback if chosen: k is subtracted: add it to both sides._
- ◻️ x = √y − k  
  _↳ feedback if chosen: Add k first, then take the square root of the whole of y + k._

Full working after a second miss:

> Add k to both sides, then take the square root.  
> So the answer is x = √(y + k).  

> Make v the subject of E = ½mv².

- ✅ v = √(2E ÷ m)
- ◻️ v = (2E ÷ m)²  
  _↳ feedback if chosen: To undo a square, take the square root._
- ◻️ v = 2E ÷ m²  
  _↳ feedback if chosen: Only v is squared: undo it with a square root at the end._
- ◻️ v = √(E ÷ 2m)  
  _↳ feedback if chosen: Multiply by 2 to undo ½, do not divide._

Full working after a second miss:

> Multiply by 2, divide by m, then take the square root.  
> So the answer is v = √(2E ÷ m).  

> Make v the subject of E = ½mv².

- ◻️ v = √(E ÷ 2m)  
  _↳ feedback if chosen: Multiply by 2 to undo ½, do not divide._
- ◻️ v = 2E ÷ m²  
  _↳ feedback if chosen: Only v is squared: undo it with a square root at the end._
- ✅ v = √(2E ÷ m)
- ◻️ v = (2E ÷ m)²  
  _↳ feedback if chosen: To undo a square, take the square root._

Full working after a second miss:

> Multiply by 2, divide by m, then take the square root.  
> So the answer is v = √(2E ÷ m).  

Sources: formulae (Form 3 Mathematics syllabus, Term 1: transposition of formulae (change of subject))

### `m3-13-twice` · Lesson 13 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Make x the subject of ax + b = cx + d. | x = (d − b) ÷ (a − c) | x = (d + b) ÷ (a + c) · x = (d − b) ÷ a − c · x = d − b − a + c | Move cx by subtracting it and b by subtracting it: signs change. · Factorise x(a − c), then divide by the whole bracket. · x is multiplied by (a − c): divide, do not subtract. | Collect x terms: ax − cx = d − b, factorise x(a − c) = d − b, then divide. |
| Make x the subject of y = (x + 1) ÷ (x − 1). | x = (y + 1) ÷ (y − 1) | x = (y − 1) ÷ (y + 1) · x = y + 1 − y + 1 · x = (1 − y) ÷ (y + 1) | Check with y = 3: x = 2 gives (2 + 1) ÷ (2 − 1) = 3, so x = (y + 1) ÷ (y − 1). · x is a factor: factorise x(y − 1), then divide. · From xy − x = y + 1, x(y − 1) = y + 1: the signs are as in the answer. | Multiply by (x − 1): xy − y = x + 1. Collect: xy − x = y + 1, so x(y − 1) = y + 1. |
| Make a the subject of p = (a + b) ÷ a. | a = b ÷ (p − 1) | a = b ÷ p − 1 · a = (b − 1) ÷ p · a = b ÷ (p + 1) | Divide b by the whole of (p − 1). · From pa = a + b: pa − a = b, so a(p − 1) = b. · Moving a to the left subtracts it: p − 1, not p + 1. | Multiply by a: pa = a + b. Collect: pa − a = b, a(p − 1) = b. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Make x the subject of y = (x + 1) ÷ (x − 1).

- ◻️ x = (y − 1) ÷ (y + 1)  
  _↳ feedback if chosen: Check with y = 3: x = 2 gives (2 + 1) ÷ (2 − 1) = 3, so x = (y + 1) ÷ (y − 1)._
- ✅ x = (y + 1) ÷ (y − 1)
- ◻️ x = y + 1 − y + 1  
  _↳ feedback if chosen: x is a factor: factorise x(y − 1), then divide._
- ◻️ x = (1 − y) ÷ (y + 1)  
  _↳ feedback if chosen: From xy − x = y + 1, x(y − 1) = y + 1: the signs are as in the answer._

Full working after a second miss:

> Multiply by (x − 1): xy − y = x + 1. Collect: xy − x = y + 1, so x(y − 1) = y + 1.  
> So the answer is x = (y + 1) ÷ (y − 1).  

> Make a the subject of p = (a + b) ÷ a.

- ◻️ a = (b − 1) ÷ p  
  _↳ feedback if chosen: From pa = a + b: pa − a = b, so a(p − 1) = b._
- ◻️ a = b ÷ (p + 1)  
  _↳ feedback if chosen: Moving a to the left subtracts it: p − 1, not p + 1._
- ◻️ a = b ÷ p − 1  
  _↳ feedback if chosen: Divide b by the whole of (p − 1)._
- ✅ a = b ÷ (p − 1)

Full working after a second miss:

> Multiply by a: pa = a + b. Collect: pa − a = b, a(p − 1) = b.  
> So the answer is a = b ÷ (p − 1).  

> Make x the subject of ax + b = cx + d.

- ◻️ x = (d − b) ÷ a − c  
  _↳ feedback if chosen: Factorise x(a − c), then divide by the whole bracket._
- ✅ x = (d − b) ÷ (a − c)
- ◻️ x = (d + b) ÷ (a + c)  
  _↳ feedback if chosen: Move cx by subtracting it and b by subtracting it: signs change._
- ◻️ x = d − b − a + c  
  _↳ feedback if chosen: x is multiplied by (a − c): divide, do not subtract._

Full working after a second miss:

> Collect x terms: ax − cx = d − b, factorise x(a − c) = d − b, then divide.  
> So the answer is x = (d − b) ÷ (a − c).  

Sources: formulae (Form 3 Mathematics syllabus, Term 1: transposition of formulae (change of subject))

### `m3-13-sq-card` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Make r the subject of A = πr². | r = √(A ÷ π) | r = A ÷ π² · r = √A ÷ π · r = (A ÷ π)² | Only r is squared: divide by π, then take the square root. · Take the square root of the whole of A ÷ π. · To undo a square, take the square root, do not square. | Divide by π, then take the square root. |
| Make v the subject of E = ½mv². | v = √(2E ÷ m) | v = 2E ÷ m² · v = √(E ÷ 2m) · v = (2E ÷ m)² | Only v is squared: undo it with a square root at the end. · Multiply by 2 to undo ½, do not divide. · To undo a square, take the square root. | Multiply by 2, divide by m, then take the square root. |
| Make x the subject of y = x² − k. | x = √(y + k) | x = √y − k · x = (y + k)² · x = √(y − k) | Add k first, then take the square root of the whole of y + k. · To undo a square, take the square root. · k is subtracted: add it to both sides. | Add k to both sides, then take the square root. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Make v the subject of E = ½mv².

- ◻️ v = (2E ÷ m)²  
  _↳ feedback if chosen: To undo a square, take the square root._
- ✅ v = √(2E ÷ m)
- ◻️ v = 2E ÷ m²  
  _↳ feedback if chosen: Only v is squared: undo it with a square root at the end._
- ◻️ v = √(E ÷ 2m)  
  _↳ feedback if chosen: Multiply by 2 to undo ½, do not divide._

Full working after a second miss:

> Multiply by 2, divide by m, then take the square root.  
> So the answer is v = √(2E ÷ m).  

> Make v the subject of E = ½mv².

- ✅ v = √(2E ÷ m)
- ◻️ v = (2E ÷ m)²  
  _↳ feedback if chosen: To undo a square, take the square root._
- ◻️ v = 2E ÷ m²  
  _↳ feedback if chosen: Only v is squared: undo it with a square root at the end._
- ◻️ v = √(E ÷ 2m)  
  _↳ feedback if chosen: Multiply by 2 to undo ½, do not divide._

Full working after a second miss:

> Multiply by 2, divide by m, then take the square root.  
> So the answer is v = √(2E ÷ m).  

> Make x the subject of y = x² − k.

- ✅ x = √(y + k)
- ◻️ x = √y − k  
  _↳ feedback if chosen: Add k first, then take the square root of the whole of y + k._
- ◻️ x = √(y − k)  
  _↳ feedback if chosen: k is subtracted: add it to both sides._
- ◻️ x = (y + k)²  
  _↳ feedback if chosen: To undo a square, take the square root._

Full working after a second miss:

> Add k to both sides, then take the square root.  
> So the answer is x = √(y + k).  

Sources: formulae (Form 3 Mathematics syllabus, Term 1: transposition of formulae (change of subject))

### `m3-14-form` · Lesson 14 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| y varies inversely as x. Which formula is right? | y = k ÷ x | y = kx · y = k + x · y = kx² | y = kx is direct variation. · Variation uses multiplying or dividing by k, not adding. · y = kx² is direct variation with the square of x. | Inverse variation: y = k ÷ x. |
| y varies directly as the square of x. Which formula is right? | y = kx² | y = k ÷ x² · y = (kx)² · y = kx | Dividing by x² is inverse variation. · Only x is squared; k is not. · That is direct variation with x, not x². | Directly as the square: y = kx². |
| y varies inversely as the square root of x. Which formula is right? | y = k ÷ √x | y = k√x · y = √(k ÷ x) · y = k ÷ x² | k√x is direct variation with √x. · k is not under the root. · That is the square, not the square root. | Inversely as √x: y = k ÷ √x. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> y varies directly as the square of x. Which formula is right?

- ◻️ y = kx  
  _↳ feedback if chosen: That is direct variation with x, not x²._
- ◻️ y = k ÷ x²  
  _↳ feedback if chosen: Dividing by x² is inverse variation._
- ◻️ y = (kx)²  
  _↳ feedback if chosen: Only x is squared; k is not._
- ✅ y = kx²

Full working after a second miss:

> Directly as the square: y = kx².  
> So the answer is y = kx².  

> y varies inversely as x. Which formula is right?

- ✅ y = k ÷ x
- ◻️ y = kx  
  _↳ feedback if chosen: y = kx is direct variation._
- ◻️ y = kx²  
  _↳ feedback if chosen: y = kx² is direct variation with the square of x._
- ◻️ y = k + x  
  _↳ feedback if chosen: Variation uses multiplying or dividing by k, not adding._

Full working after a second miss:

> Inverse variation: y = k ÷ x.  
> So the answer is y = k ÷ x.  

> y varies inversely as the square root of x. Which formula is right?

- ◻️ y = k ÷ x²  
  _↳ feedback if chosen: That is the square, not the square root._
- ◻️ y = √(k ÷ x)  
  _↳ feedback if chosen: k is not under the root._
- ◻️ y = k√x  
  _↳ feedback if chosen: k√x is direct variation with √x._
- ✅ y = k ÷ √x

Full working after a second miss:

> Inversely as √x: y = k ÷ √x.  
> So the answer is y = k ÷ √x.  

Sources: variation (Form 3 Mathematics syllabus, Term 1: direct, inverse, joint and partial variation; graphs)

### `m3-15-form` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| z varies jointly as x and y. Which formula is right? | z = kxy | z = k(x + y) · z = kx ÷ y · z = xy | Jointly means multiply, not add. · kx ÷ y means inversely as y. · There must be a constant k. | Jointly: z = kxy. |
| z varies directly as x and inversely as y. Which formula is right? | z = kx ÷ y | z = kxy · z = ky ÷ x · z = k(x − y) | That is jointly as x and y. · x and y are the wrong way round. · Variation uses multiplying or dividing. | Directly as x (top), inversely as y (bottom). |
| P varies directly as the square of v and inversely as r. Which formula is right? | P = kv² ÷ r | P = kvr² · P = kr ÷ v² · P = k(v² − r) | r should divide, not multiply. · v² goes on top, r at the bottom. · Variation uses multiplying and dividing. | P = kv² ÷ r. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> z varies directly as x and inversely as y. Which formula is right?

- ◻️ z = k(x − y)  
  _↳ feedback if chosen: Variation uses multiplying or dividing._
- ◻️ z = kxy  
  _↳ feedback if chosen: That is jointly as x and y._
- ◻️ z = ky ÷ x  
  _↳ feedback if chosen: x and y are the wrong way round._
- ✅ z = kx ÷ y

Full working after a second miss:

> Directly as x (top), inversely as y (bottom).  
> So the answer is z = kx ÷ y.  

> P varies directly as the square of v and inversely as r. Which formula is right?

- ✅ P = kv² ÷ r
- ◻️ P = kvr²  
  _↳ feedback if chosen: r should divide, not multiply._
- ◻️ P = kr ÷ v²  
  _↳ feedback if chosen: v² goes on top, r at the bottom._
- ◻️ P = k(v² − r)  
  _↳ feedback if chosen: Variation uses multiplying and dividing._

Full working after a second miss:

> P = kv² ÷ r.  
> So the answer is P = kv² ÷ r.  

> z varies directly as x and inversely as y. Which formula is right?

- ◻️ z = kxy  
  _↳ feedback if chosen: That is jointly as x and y._
- ✅ z = kx ÷ y
- ◻️ z = ky ÷ x  
  _↳ feedback if chosen: x and y are the wrong way round._
- ◻️ z = k(x − y)  
  _↳ feedback if chosen: Variation uses multiplying or dividing._

Full working after a second miss:

> Directly as x (top), inversely as y (bottom).  
> So the answer is z = kx ÷ y.  

Sources: variation (Form 3 Mathematics syllabus, Term 1: direct, inverse, joint and partial variation; graphs)

### `m3-15-graph` · Lesson 15 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does the graph of y = kx (k > 0) look like? | A straight line through the origin | A curve that never meets the axes · A straight line that does not pass through the origin · A U-shaped curve | That is y = k ÷ x. · When x = 0, y = k × 0 = 0: the line passes through the origin. · That is y = kx². | y = kx is a straight line; x = 0 gives y = 0. |
| What does the graph of y = k ÷ x (k > 0, x > 0) look like? | A curve that gets closer to both axes but never meets them | A straight line through the origin · A U-shaped curve through the origin · A straight line sloping down to the x-axis | That is direct variation, y = kx. · That is y = kx². · y = k ÷ x is never zero, so it never reaches the x-axis. | y = k ÷ x: as x grows, y shrinks towards zero but never reaches it. |
| What does the graph of y = kx² (k > 0) look like? | A U-shaped curve (parabola) through the origin | A straight line through the origin · A curve that never meets the axes · A straight line that does not pass through the origin | y doubles when x doubles only for y = kx; here y is four times as big. · That is y = k ÷ x. · x = 0 gives y = 0: it passes through the origin. | y = kx² is a parabola with its lowest point at the origin. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does the graph of y = kx² (k > 0) look like?

- ◻️ A straight line through the origin  
  _↳ feedback if chosen: y doubles when x doubles only for y = kx; here y is four times as big._
- ◻️ A curve that never meets the axes  
  _↳ feedback if chosen: That is y = k ÷ x._
- ◻️ A straight line that does not pass through the origin  
  _↳ feedback if chosen: x = 0 gives y = 0: it passes through the origin._
- ✅ A U-shaped curve (parabola) through the origin

Full working after a second miss:

> y = kx² is a parabola with its lowest point at the origin.  
> So the answer is A U-shaped curve (parabola) through the origin.  

> What does the graph of y = k ÷ x (k > 0, x > 0) look like?

- ◻️ A straight line through the origin  
  _↳ feedback if chosen: That is direct variation, y = kx._
- ◻️ A U-shaped curve through the origin  
  _↳ feedback if chosen: That is y = kx²._
- ◻️ A straight line sloping down to the x-axis  
  _↳ feedback if chosen: y = k ÷ x is never zero, so it never reaches the x-axis._
- ✅ A curve that gets closer to both axes but never meets them

Full working after a second miss:

> y = k ÷ x: as x grows, y shrinks towards zero but never reaches it.  
> So the answer is A curve that gets closer to both axes but never meets them.  

> What does the graph of y = kx² (k > 0) look like?

- ✅ A U-shaped curve (parabola) through the origin
- ◻️ A straight line that does not pass through the origin  
  _↳ feedback if chosen: x = 0 gives y = 0: it passes through the origin._
- ◻️ A straight line through the origin  
  _↳ feedback if chosen: y doubles when x doubles only for y = kx; here y is four times as big._
- ◻️ A curve that never meets the axes  
  _↳ feedback if chosen: That is y = k ÷ x._

Full working after a second miss:

> y = kx² is a parabola with its lowest point at the origin.  
> So the answer is A U-shaped curve (parabola) through the origin.  

Sources: variation (Form 3 Mathematics syllabus, Term 1: direct, inverse, joint and partial variation; graphs)

### `m3-15-graph-card` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does the graph of y = kx (k > 0) look like? | A straight line through the origin | A curve that never meets the axes · A straight line that does not pass through the origin · A U-shaped curve | That is y = k ÷ x. · When x = 0, y = k × 0 = 0: the line passes through the origin. · That is y = kx². | y = kx is a straight line; x = 0 gives y = 0. |
| What does the graph of y = k ÷ x (k > 0, x > 0) look like? | A curve that gets closer to both axes but never meets them | A straight line through the origin · A U-shaped curve through the origin · A straight line sloping down to the x-axis | That is direct variation, y = kx. · That is y = kx². · y = k ÷ x is never zero, so it never reaches the x-axis. | y = k ÷ x: as x grows, y shrinks towards zero but never reaches it. |
| What does the graph of y = kx² (k > 0) look like? | A U-shaped curve (parabola) through the origin | A straight line through the origin · A curve that never meets the axes · A straight line that does not pass through the origin | y doubles when x doubles only for y = kx; here y is four times as big. · That is y = k ÷ x. · x = 0 gives y = 0: it passes through the origin. | y = kx² is a parabola with its lowest point at the origin. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does the graph of y = k ÷ x (k > 0, x > 0) look like?

- ◻️ A U-shaped curve through the origin  
  _↳ feedback if chosen: That is y = kx²._
- ◻️ A straight line sloping down to the x-axis  
  _↳ feedback if chosen: y = k ÷ x is never zero, so it never reaches the x-axis._
- ✅ A curve that gets closer to both axes but never meets them
- ◻️ A straight line through the origin  
  _↳ feedback if chosen: That is direct variation, y = kx._

Full working after a second miss:

> y = k ÷ x: as x grows, y shrinks towards zero but never reaches it.  
> So the answer is A curve that gets closer to both axes but never meets them.  

> What does the graph of y = k ÷ x (k > 0, x > 0) look like?

- ◻️ A straight line through the origin  
  _↳ feedback if chosen: That is direct variation, y = kx._
- ◻️ A straight line sloping down to the x-axis  
  _↳ feedback if chosen: y = k ÷ x is never zero, so it never reaches the x-axis._
- ◻️ A U-shaped curve through the origin  
  _↳ feedback if chosen: That is y = kx²._
- ✅ A curve that gets closer to both axes but never meets them

Full working after a second miss:

> y = k ÷ x: as x grows, y shrinks towards zero but never reaches it.  
> So the answer is A curve that gets closer to both axes but never meets them.  

> What does the graph of y = kx (k > 0) look like?

- ◻️ A U-shaped curve  
  _↳ feedback if chosen: That is y = kx²._
- ◻️ A curve that never meets the axes  
  _↳ feedback if chosen: That is y = k ÷ x._
- ✅ A straight line through the origin
- ◻️ A straight line that does not pass through the origin  
  _↳ feedback if chosen: When x = 0, y = k × 0 = 0: the line passes through the origin._

Full working after a second miss:

> y = kx is a straight line; x = 0 gives y = 0.  
> So the answer is A straight line through the origin.  

Sources: variation (Form 3 Mathematics syllabus, Term 1: direct, inverse, joint and partial variation; graphs)

### `m3-17-name` · Lesson 17 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which ratio is opposite ÷ hypotenuse? | sin θ | cos θ · tan θ · hyp θ | cos θ is adjacent ÷ hypotenuse. · tan θ is opposite ÷ adjacent. · There is no ratio called hyp θ. | SOH: sine is opposite over hypotenuse. |
| Which ratio is opposite ÷ adjacent? | tan θ | sin θ · cos θ · sec θ | sin θ is opposite ÷ hypotenuse. · cos θ is adjacent ÷ hypotenuse. · Not used in Form 3: TOA gives tan. | TOA: tangent is opposite over adjacent. |
| Which side is the adjacent side for the angle θ? | The side next to θ that is not the hypotenuse | The side facing θ · The longest side · Any side touching the right angle | The side facing θ is the opposite side. · The longest side is the hypotenuse. · One of the sides at the right angle is opposite θ. | Adjacent means next to: it touches θ but is not the hypotenuse. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which ratio is opposite ÷ hypotenuse?

- ◻️ tan θ  
  _↳ feedback if chosen: tan θ is opposite ÷ adjacent._
- ✅ sin θ
- ◻️ hyp θ  
  _↳ feedback if chosen: There is no ratio called hyp θ._
- ◻️ cos θ  
  _↳ feedback if chosen: cos θ is adjacent ÷ hypotenuse._

Full working after a second miss:

> SOH: sine is opposite over hypotenuse.  
> So the answer is sin θ.  

> Which ratio is opposite ÷ adjacent?

- ◻️ sec θ  
  _↳ feedback if chosen: Not used in Form 3: TOA gives tan._
- ✅ tan θ
- ◻️ sin θ  
  _↳ feedback if chosen: sin θ is opposite ÷ hypotenuse._
- ◻️ cos θ  
  _↳ feedback if chosen: cos θ is adjacent ÷ hypotenuse._

Full working after a second miss:

> TOA: tangent is opposite over adjacent.  
> So the answer is tan θ.  

> Which ratio is opposite ÷ hypotenuse?

- ◻️ hyp θ  
  _↳ feedback if chosen: There is no ratio called hyp θ._
- ◻️ cos θ  
  _↳ feedback if chosen: cos θ is adjacent ÷ hypotenuse._
- ◻️ tan θ  
  _↳ feedback if chosen: tan θ is opposite ÷ adjacent._
- ✅ sin θ

Full working after a second miss:

> SOH: sine is opposite over hypotenuse.  
> So the answer is sin θ.  

Sources: trigonometry (Form 3 Mathematics syllabus, Term 1: trigonometric ratios of acute angles, complementary angles, special angles (30°, 45°, 60°), calculators, solving right-angled triangles, elevation and depression)

### `m3-18-exact` · Lesson 18 · multiple choice, level 1

Prompt: What is the exact value of {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| sin 30° | 1/2 | √3/2 · 1/√2 · √3 | √3/2 is sin 60° (or cos 30°). · 1/√2 is sin 45°. · √3 is tan 60°. | sin 30° = 1/2 (half an equilateral triangle). |
| cos 30° | √3/2 | 1/2 · 1/√3 · 1 | 1/2 is cos 60°. · 1/√3 is tan 30°. · cos 30° is less than 1. | cos 30° = √3/2. |
| tan 45° | 1 | 1/√2 · √3 · 1/2 | 1/√2 is sin 45° and cos 45°. · √3 is tan 60°. · 1/2 is sin 30°. | In half a square, opposite = adjacent, so tan 45° = 1. |
| tan 60° | √3 | 1/√3 · √3/2 · 1 | 1/√3 is tan 30°. · √3/2 is sin 60°. · 1 is tan 45°. | tan 60° = √3. |
| sin 45° | 1/√2 | 1 · 1/2 · √3/2 | 1 is tan 45°. · 1/2 is sin 30°. · √3/2 is sin 60°. | sin 45° = 1/√2 = √2/2. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the exact value of tan 60°?

- ✅ √3
- ◻️ 1/√3  
  _↳ feedback if chosen: 1/√3 is tan 30°._
- ◻️ √3/2  
  _↳ feedback if chosen: √3/2 is sin 60°._
- ◻️ 1  
  _↳ feedback if chosen: 1 is tan 45°._

Full working after a second miss:

> tan 60° = √3.  
> So the answer is √3.  

> What is the exact value of sin 30°?

- ◻️ 1/√2  
  _↳ feedback if chosen: 1/√2 is sin 45°._
- ◻️ √3/2  
  _↳ feedback if chosen: √3/2 is sin 60° (or cos 30°)._
- ✅ 1/2
- ◻️ √3  
  _↳ feedback if chosen: √3 is tan 60°._

Full working after a second miss:

> sin 30° = 1/2 (half an equilateral triangle).  
> So the answer is 1/2.  

> What is the exact value of sin 30°?

- ◻️ 1/√2  
  _↳ feedback if chosen: 1/√2 is sin 45°._
- ◻️ √3/2  
  _↳ feedback if chosen: √3/2 is sin 60° (or cos 30°)._
- ✅ 1/2
- ◻️ √3  
  _↳ feedback if chosen: √3 is tan 60°._

Full working after a second miss:

> sin 30° = 1/2 (half an equilateral triangle).  
> So the answer is 1/2.  

Sources: trigonometry (Form 3 Mathematics syllabus, Term 1: trigonometric ratios of acute angles, complementary angles, special angles (30°, 45°, 60°), calculators, solving right-angled triangles, elevation and depression)

### `m3-18-value` · Lesson 18 · number, level 2

Prompt: Without a calculator, find the value of {X.e}.
Right answer: `X.v`

Table `X` (one row is picked each time):

| e | s | v |
|---|---|---|
| sin 30° + cos 60° | 1/2 + 1/2 | 1 |
| 4 sin 30° × tan 45° | 4 × 1/2 × 1 | 2 |
| tan 45° − cos 60° | 1 − 1/2 | 0.5 |
| 2 cos 60° + 3 tan 45° | 2 × 1/2 + 3 × 1 | 4 |
| sin² 45° + cos² 45° | (1/√2)² + (1/√2)² = 1/2 + 1/2 | 1 |
| tan 60° × tan 30° | √3 × 1/√3 | 1 |


Three generated variants:

> Without a calculator, find the value of 4 sin 30° × tan 45°.

Answer: **2**

Full working after a second miss:

> 4 × 1/2 × 1  
> = 2.  

> Without a calculator, find the value of sin² 45° + cos² 45°.

Answer: **1**

Full working after a second miss:

> (1/√2)² + (1/√2)² = 1/2 + 1/2  
> = 1.  

> Without a calculator, find the value of sin 30° + cos 60°.

Answer: **1**

Full working after a second miss:

> 1/2 + 1/2  
> = 1.  

Sources: trigonometry (Form 3 Mathematics syllabus, Term 1: trigonometric ratios of acute angles, complementary angles, special angles (30°, 45°, 60°), calculators, solving right-angled triangles, elevation and depression)

