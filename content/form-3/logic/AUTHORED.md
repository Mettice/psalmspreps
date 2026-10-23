# Logic Form 3, Form Three Logic: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f3-logic`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `l3-1-terms` | 1 | multiple choice, 1 | intro-logic |
| 2 | `l3-1-cases` | 1 | multiple choice, 1 | intro-logic |
| 3 | `l3-1-reason` | 1 | multiple choice, 2 | intro-logic |
| 4 | `l3-1-link` | 1 | matching, 2 | intro-logic |
| 5 | `l3-1-repair` | 1 | spot the error, 3 | intro-logic |
| 6 | `l3-1-repair-card` (card cl3-1-repair) | 1 | spot the error, 1 | intro-logic |
| 7 | `l3-2-terms` | 2 | multiple choice, 1 | intro-logic |
| 8 | `l3-2-cases` | 2 | multiple choice, 1 | intro-logic |
| 9 | `l3-2-reason` | 2 | multiple choice, 2 | intro-logic |
| 10 | `l3-2-link` | 2 | matching, 2 | intro-logic |
| 11 | `l3-2-repair` | 2 | spot the error, 3 | intro-logic |
| 12 | `l3-2-repair-card` (card cl3-2-repair) | 2 | spot the error, 1 | intro-logic |
| 13 | `l3-3-terms` | 3 | multiple choice, 1 | intro-logic |
| 14 | `l3-3-cases` | 3 | multiple choice, 1 | intro-logic |
| 15 | `l3-3-reason` | 3 | multiple choice, 2 | intro-logic |
| 16 | `l3-3-link` | 3 | matching, 2 | intro-logic |
| 17 | `l3-3-repair` | 3 | spot the error, 3 | intro-logic |
| 18 | `l3-3-repair-card` (card cl3-3-repair) | 3 | spot the error, 1 | intro-logic |
| 19 | `l3-4-terms` | 4 | multiple choice, 1 | intro-logic |
| 20 | `l3-4-cases` | 4 | multiple choice, 1 | intro-logic |
| 21 | `l3-4-reason` | 4 | multiple choice, 2 | intro-logic |
| 22 | `l3-4-link` | 4 | matching, 2 | intro-logic |
| 23 | `l3-4-repair` | 4 | spot the error, 3 | intro-logic |
| 24 | `l3-4-repair-card` (card cl3-4-repair) | 4 | spot the error, 1 | intro-logic |
| 25 | `l3-6-terms` | 6 | multiple choice, 1 | intro-logic |
| 26 | `l3-6-cases` | 6 | multiple choice, 1 | intro-logic |
| 27 | `l3-6-reason` | 6 | multiple choice, 2 | intro-logic |
| 28 | `l3-6-repair` | 6 | spot the error, 3 | intro-logic |
| 29 | `l3-6-repair-card` (card cl3-6-repair) | 6 | spot the error, 1 | intro-logic |
| 30 | `l3-7-terms` | 7 | multiple choice, 1 | intro-logic |
| 31 | `l3-7-cases` | 7 | multiple choice, 1 | intro-logic |
| 32 | `l3-7-reason` | 7 | multiple choice, 2 | intro-logic |
| 33 | `l3-7-link` | 7 | matching, 2 | intro-logic |
| 34 | `l3-7-repair` | 7 | spot the error, 3 | intro-logic |
| 35 | `l3-7-repair-card` (card cl3-7-repair) | 7 | spot the error, 1 | intro-logic |
| 36 | `l3-8-terms` | 8 | multiple choice, 1 | intro-logic |
| 37 | `l3-8-cases` | 8 | multiple choice, 1 | intro-logic |
| 38 | `l3-8-reason` | 8 | multiple choice, 2 | intro-logic |
| 39 | `l3-8-link` | 8 | matching, 2 | intro-logic |
| 40 | `l3-8-repair` | 8 | spot the error, 3 | intro-logic |
| 41 | `l3-8-repair-card` (card cl3-8-repair) | 8 | spot the error, 1 | intro-logic |
| 42 | `l3-9-terms` | 9 | multiple choice, 1 | intro-logic |
| 43 | `l3-9-cases` | 9 | multiple choice, 1 | intro-logic |
| 44 | `l3-9-reason` | 9 | multiple choice, 2 | intro-logic |
| 45 | `l3-9-link` | 9 | matching, 2 | intro-logic |
| 46 | `l3-9-repair` | 9 | spot the error, 3 | intro-logic |
| 47 | `l3-9-repair-card` (card cl3-9-repair) | 9 | spot the error, 1 | intro-logic |

### `l3-1-terms` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: claims offered as reasons for a conclusion ? | argument | premise · conclusion · inference | premise means a claim offered as support; the question instead describes claims offered as reasons for a conclusion. · conclusion means the claim the reasons are intended to establish; the question instead describes claims offered as reasons for a conclusion. · inference means the reasoning step from premises to a conclusion; the question instead describes claims offered as reasons for a conclusion. | Claims offered as reasons for a conclusion. |
| Which term means: a claim offered as support ? | premise | argument · conclusion · inference | argument means claims offered as reasons for a conclusion; the question instead describes a claim offered as support. · conclusion means the claim the reasons are intended to establish; the question instead describes a claim offered as support. · inference means the reasoning step from premises to a conclusion; the question instead describes a claim offered as support. | A claim offered as support. |
| Which term means: the claim the reasons are intended to establish ? | conclusion | argument · premise · inference | argument means claims offered as reasons for a conclusion; the question instead describes the claim the reasons are intended to establish. · premise means a claim offered as support; the question instead describes the claim the reasons are intended to establish. · inference means the reasoning step from premises to a conclusion; the question instead describes the claim the reasons are intended to establish. | The claim the reasons are intended to establish. |
| Which term means: the reasoning step from premises to a conclusion ? | inference | argument · premise · conclusion | argument means claims offered as reasons for a conclusion; the question instead describes the reasoning step from premises to a conclusion. · premise means a claim offered as support; the question instead describes the reasoning step from premises to a conclusion. · conclusion means the claim the reasons are intended to establish; the question instead describes the reasoning step from premises to a conclusion. | The reasoning step from premises to a conclusion. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: the claim the reasons are intended to establish ?

- ◻️ inference  
  _↳ feedback if chosen: inference means the reasoning step from premises to a conclusion; the question instead describes the claim the reasons are intended to establish._
- ◻️ argument  
  _↳ feedback if chosen: argument means claims offered as reasons for a conclusion; the question instead describes the claim the reasons are intended to establish._
- ✅ conclusion
- ◻️ premise  
  _↳ feedback if chosen: premise means a claim offered as support; the question instead describes the claim the reasons are intended to establish._

Full working after a second miss:

> The claim the reasons are intended to establish.  
> So the answer is “conclusion”.  

> Which term means: claims offered as reasons for a conclusion ?

- ◻️ inference  
  _↳ feedback if chosen: inference means the reasoning step from premises to a conclusion; the question instead describes claims offered as reasons for a conclusion._
- ◻️ premise  
  _↳ feedback if chosen: premise means a claim offered as support; the question instead describes claims offered as reasons for a conclusion._
- ✅ argument
- ◻️ conclusion  
  _↳ feedback if chosen: conclusion means the claim the reasons are intended to establish; the question instead describes claims offered as reasons for a conclusion._

Full working after a second miss:

> Claims offered as reasons for a conclusion.  
> So the answer is “argument”.  

> Which term means: a claim offered as support ?

- ◻️ conclusion  
  _↳ feedback if chosen: conclusion means the claim the reasons are intended to establish; the question instead describes a claim offered as support._
- ◻️ inference  
  _↳ feedback if chosen: inference means the reasoning step from premises to a conclusion; the question instead describes a claim offered as support._
- ◻️ argument  
  _↳ feedback if chosen: argument means claims offered as reasons for a conclusion; the question instead describes a claim offered as support._
- ✅ premise

Full working after a second miss:

> A claim offered as support.  
> So the answer is “premise”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-1-cases` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Ayuk says the path is muddy, so the class should use the paved route.
Which term best fits this example? | argument | premise · conclusion · inference | premise concerns a claim offered as support. This case instead illustrates claims offered as reasons for a conclusion. · conclusion concerns the claim the reasons are intended to establish. This case instead illustrates claims offered as reasons for a conclusion. · inference concerns the reasoning step from premises to a conclusion. This case instead illustrates claims offered as reasons for a conclusion. | Ayuk says the path is muddy, so the class should use the paved route. Claims offered as reasons for a conclusion. |
| Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.
Which term best fits this example? | premise | argument · conclusion · inference | argument concerns claims offered as reasons for a conclusion. This case instead illustrates a claim offered as support. · conclusion concerns the claim the reasons are intended to establish. This case instead illustrates a claim offered as support. · inference concerns the reasoning step from premises to a conclusion. This case instead illustrates a claim offered as support. | Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim. A claim offered as support. |
| Nji says the clinic is nearer, so we should go there. Consider we should go there.
Which term best fits this example? | conclusion | argument · premise · inference | argument concerns claims offered as reasons for a conclusion. This case instead illustrates the claim the reasons are intended to establish. · premise concerns a claim offered as support. This case instead illustrates the claim the reasons are intended to establish. · inference concerns the reasoning step from premises to a conclusion. This case instead illustrates the claim the reasons are intended to establish. | Nji says the clinic is nearer, so we should go there. Consider we should go there. The claim the reasons are intended to establish. |
| A learner moves from all club members have badges and Bih is a member to Bih has a badge.
Which term best fits this example? | inference | argument · premise · conclusion | argument concerns claims offered as reasons for a conclusion. This case instead illustrates the reasoning step from premises to a conclusion. · premise concerns a claim offered as support. This case instead illustrates the reasoning step from premises to a conclusion. · conclusion concerns the claim the reasons are intended to establish. This case instead illustrates the reasoning step from premises to a conclusion. | A learner moves from all club members have badges and Bih is a member to Bih has a badge. The reasoning step from premises to a conclusion. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Ayuk says the path is muddy, so the class should use the paved route.
> Which term best fits this example?

- ◻️ inference  
  _↳ feedback if chosen: inference concerns the reasoning step from premises to a conclusion. This case instead illustrates claims offered as reasons for a conclusion._
- ◻️ conclusion  
  _↳ feedback if chosen: conclusion concerns the claim the reasons are intended to establish. This case instead illustrates claims offered as reasons for a conclusion._
- ✅ argument
- ◻️ premise  
  _↳ feedback if chosen: premise concerns a claim offered as support. This case instead illustrates claims offered as reasons for a conclusion._

Full working after a second miss:

> Ayuk says the path is muddy, so the class should use the paved route. Claims offered as reasons for a conclusion.  
> So the answer is “argument”.  

> Ayuk says the path is muddy, so the class should use the paved route.
> Which term best fits this example?

- ◻️ premise  
  _↳ feedback if chosen: premise concerns a claim offered as support. This case instead illustrates claims offered as reasons for a conclusion._
- ◻️ inference  
  _↳ feedback if chosen: inference concerns the reasoning step from premises to a conclusion. This case instead illustrates claims offered as reasons for a conclusion._
- ◻️ conclusion  
  _↳ feedback if chosen: conclusion concerns the claim the reasons are intended to establish. This case instead illustrates claims offered as reasons for a conclusion._
- ✅ argument

Full working after a second miss:

> Ayuk says the path is muddy, so the class should use the paved route. Claims offered as reasons for a conclusion.  
> So the answer is “argument”.  

> Nji says the clinic is nearer, so we should go there. Consider we should go there.
> Which term best fits this example?

- ◻️ argument  
  _↳ feedback if chosen: argument concerns claims offered as reasons for a conclusion. This case instead illustrates the claim the reasons are intended to establish._
- ✅ conclusion
- ◻️ inference  
  _↳ feedback if chosen: inference concerns the reasoning step from premises to a conclusion. This case instead illustrates the claim the reasons are intended to establish._
- ◻️ premise  
  _↳ feedback if chosen: premise concerns a claim offered as support. This case instead illustrates the claim the reasons are intended to establish._

Full working after a second miss:

> Nji says the clinic is nearer, so we should go there. Consider we should go there. The claim the reasons are intended to establish.  
> So the answer is “conclusion”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-1-reason` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Ayuk says the path is muddy, so the class should use the paved route.
Which explanation justifies the classification? | Claims offered as reasons for a conclusion. | A claim offered as support. · The claim the reasons are intended to establish. · The reasoning step from premises to a conclusion. | That explanation describes premise, rather than the relationship illustrated in this example. · That explanation describes conclusion, rather than the relationship illustrated in this example. · That explanation describes inference, rather than the relationship illustrated in this example. | A calm proposal with supporting reasons is an argument; anger is irrelevant. |
| Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.
Which explanation justifies the classification? | A claim offered as support. | Claims offered as reasons for a conclusion. · The claim the reasons are intended to establish. · The reasoning step from premises to a conclusion. | That explanation describes argument, rather than the relationship illustrated in this example. · That explanation describes conclusion, rather than the relationship illustrated in this example. · That explanation describes inference, rather than the relationship illustrated in this example. | The leaking roof is a reason; moving the books is the conclusion. |
| Nji says the clinic is nearer, so we should go there. Consider we should go there.
Which explanation justifies the classification? | The claim the reasons are intended to establish. | Claims offered as reasons for a conclusion. · A claim offered as support. · The reasoning step from premises to a conclusion. | That explanation describes argument, rather than the relationship illustrated in this example. · That explanation describes premise, rather than the relationship illustrated in this example. · That explanation describes inference, rather than the relationship illustrated in this example. | Its role as the supported claim matters, not its position. |
| A learner moves from all club members have badges and Bih is a member to Bih has a badge.
Which explanation justifies the classification? | The reasoning step from premises to a conclusion. | Claims offered as reasons for a conclusion. · A claim offered as support. · The claim the reasons are intended to establish. | That explanation describes argument, rather than the relationship illustrated in this example. · That explanation describes premise, rather than the relationship illustrated in this example. · That explanation describes conclusion, rather than the relationship illustrated in this example. | An inference links support to a conclusion; it is not mere copying. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner moves from all club members have badges and Bih is a member to Bih has a badge.
> Which explanation justifies the classification?

- ◻️ A claim offered as support.  
  _↳ feedback if chosen: That explanation describes premise, rather than the relationship illustrated in this example._
- ◻️ The claim the reasons are intended to establish.  
  _↳ feedback if chosen: That explanation describes conclusion, rather than the relationship illustrated in this example._
- ✅ The reasoning step from premises to a conclusion.
- ◻️ Claims offered as reasons for a conclusion.  
  _↳ feedback if chosen: That explanation describes argument, rather than the relationship illustrated in this example._

Full working after a second miss:

> An inference links support to a conclusion; it is not mere copying.  
> So the answer is “The reasoning step from premises to a conclusion.”.  

> A learner moves from all club members have badges and Bih is a member to Bih has a badge.
> Which explanation justifies the classification?

- ◻️ Claims offered as reasons for a conclusion.  
  _↳ feedback if chosen: That explanation describes argument, rather than the relationship illustrated in this example._
- ◻️ A claim offered as support.  
  _↳ feedback if chosen: That explanation describes premise, rather than the relationship illustrated in this example._
- ◻️ The claim the reasons are intended to establish.  
  _↳ feedback if chosen: That explanation describes conclusion, rather than the relationship illustrated in this example._
- ✅ The reasoning step from premises to a conclusion.

Full working after a second miss:

> An inference links support to a conclusion; it is not mere copying.  
> So the answer is “The reasoning step from premises to a conclusion.”.  

> Nji says the clinic is nearer, so we should go there. Consider we should go there.
> Which explanation justifies the classification?

- ◻️ The reasoning step from premises to a conclusion.  
  _↳ feedback if chosen: That explanation describes inference, rather than the relationship illustrated in this example._
- ✅ The claim the reasons are intended to establish.
- ◻️ Claims offered as reasons for a conclusion.  
  _↳ feedback if chosen: That explanation describes argument, rather than the relationship illustrated in this example._
- ◻️ A claim offered as support.  
  _↳ feedback if chosen: That explanation describes premise, rather than the relationship illustrated in this example._

Full working after a second miss:

> Its role as the supported claim matters, not its position.  
> So the answer is “The claim the reasons are intended to establish.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-1-link` · Lesson 1 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- argument → **Ayuk says the path is muddy, so the class should use the paved route.**
- premise → **Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.**
- conclusion → **Nji says the clinic is nearer, so we should go there. Consider we should go there.**
- inference → **A learner moves from all club members have badges and Bih is a member to Bih has a badge.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): A learner moves from all club members have badges and Bih is a member to Bih has a badge. · Ayuk says the path is muddy, so the class should use the paved route. · Nji says the clinic is nearer, so we should go there. Consider we should go there.
- argument → **Ayuk says the path is muddy, so the class should use the paved route.**
- conclusion → **Nji says the clinic is nearer, so we should go there. Consider we should go there.**
- inference → **A learner moves from all club members have badges and Bih is a member to Bih has a badge.**

Full working after a second miss:

> The right pairs are:  
> argument → Ayuk says the path is muddy, so the class should use the paved route.  
> conclusion → Nji says the clinic is nearer, so we should go there. Consider we should go there.  
> inference → A learner moves from all club members have badges and Bih is a member to Bih has a badge.  

> Match each term to its example.

Right-hand side (shuffled): Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim. · A learner moves from all club members have badges and Bih is a member to Bih has a badge. · Nji says the clinic is nearer, so we should go there. Consider we should go there.
- conclusion → **Nji says the clinic is nearer, so we should go there. Consider we should go there.**
- premise → **Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.**
- inference → **A learner moves from all club members have badges and Bih is a member to Bih has a badge.**

Full working after a second miss:

> The right pairs are:  
> conclusion → Nji says the clinic is nearer, so we should go there. Consider we should go there.  
> premise → Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.  
> inference → A learner moves from all club members have badges and Bih is a member to Bih has a badge.  

> Match each term to its example.

Right-hand side (shuffled): Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim. · Ayuk says the path is muddy, so the class should use the paved route. · Nji says the clinic is nearer, so we should go there. Consider we should go there.
- argument → **Ayuk says the path is muddy, so the class should use the paved route.**
- conclusion → **Nji says the clinic is nearer, so we should go there. Consider we should go there.**
- premise → **Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.**

Full working after a second miss:

> The right pairs are:  
> argument → Ayuk says the path is muddy, so the class should use the paved route.  
> conclusion → Nji says the clinic is nearer, so we should go there. Consider we should go there.  
> premise → Bih says: the classroom roof leaks; therefore the books need moving. Consider the leaking roof claim.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-1-repair` · Lesson 1 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ argument: claims offered as reasons for a conclusion.
- ✅ premise: a claim offered as support.
- ✅ conclusion: the claim the reasons are intended to establish.
- ✅ inference: the reasoning step from premises to a conclusion.
- ❌ An argument must be an angry quarrel.  
  _↳ A calm proposal with supporting reasons is an argument; anger is irrelevant._
- ❌ A premise is always the final claim being defended.  
  _↳ The leaking roof is a reason; moving the books is the conclusion._
- ❌ A conclusion is necessarily the first sentence.  
  _↳ Its role as the supported claim matters, not its position._
- ❌ An inference is just copying an unrelated sentence.  
  _↳ An inference links support to a conclusion; it is not mere copying._


Three generated variants:

> Find the incorrect claim.

- ◻️ inference: the reasoning step from premises to a conclusion.  
  _↳ explanation: This statement is correct: inference means the reasoning step from premises to a conclusion. Look for a claim that conflicts with its definition._
- ✅ A conclusion is necessarily the first sentence.  
  _↳ explanation: Its role as the supported claim matters, not its position._
- ◻️ premise: a claim offered as support.  
  _↳ explanation: This statement is correct: premise means a claim offered as support. Look for a claim that conflicts with its definition._
- ◻️ argument: claims offered as reasons for a conclusion.  
  _↳ explanation: This statement is correct: argument means claims offered as reasons for a conclusion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A conclusion is necessarily the first sentence.”.  
> Its role as the supported claim matters, not its position.  

> Find the incorrect claim.

- ✅ An inference is just copying an unrelated sentence.  
  _↳ explanation: An inference links support to a conclusion; it is not mere copying._
- ◻️ premise: a claim offered as support.  
  _↳ explanation: This statement is correct: premise means a claim offered as support. Look for a claim that conflicts with its definition._
- ◻️ conclusion: the claim the reasons are intended to establish.  
  _↳ explanation: This statement is correct: conclusion means the claim the reasons are intended to establish. Look for a claim that conflicts with its definition._
- ◻️ argument: claims offered as reasons for a conclusion.  
  _↳ explanation: This statement is correct: argument means claims offered as reasons for a conclusion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “An inference is just copying an unrelated sentence.”.  
> An inference links support to a conclusion; it is not mere copying.  

> Find the incorrect claim.

- ✅ A premise is always the final claim being defended.  
  _↳ explanation: The leaking roof is a reason; moving the books is the conclusion._
- ◻️ argument: claims offered as reasons for a conclusion.  
  _↳ explanation: This statement is correct: argument means claims offered as reasons for a conclusion. Look for a claim that conflicts with its definition._
- ◻️ inference: the reasoning step from premises to a conclusion.  
  _↳ explanation: This statement is correct: inference means the reasoning step from premises to a conclusion. Look for a claim that conflicts with its definition._
- ◻️ conclusion: the claim the reasons are intended to establish.  
  _↳ explanation: This statement is correct: conclusion means the claim the reasons are intended to establish. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A premise is always the final claim being defended.”.  
> The leaking roof is a reason; moving the books is the conclusion.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-1-repair-card` · Lesson 1 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ argument: claims offered as reasons for a conclusion.
- ✅ premise: a claim offered as support.
- ✅ conclusion: the claim the reasons are intended to establish.
- ✅ inference: the reasoning step from premises to a conclusion.
- ❌ An argument must be an angry quarrel.  
  _↳ A calm proposal with supporting reasons is an argument; anger is irrelevant._
- ❌ A premise is always the final claim being defended.  
  _↳ The leaking roof is a reason; moving the books is the conclusion._
- ❌ A conclusion is necessarily the first sentence.  
  _↳ Its role as the supported claim matters, not its position._
- ❌ An inference is just copying an unrelated sentence.  
  _↳ An inference links support to a conclusion; it is not mere copying._


Three generated variants:

> Find the incorrect claim.

- ◻️ inference: the reasoning step from premises to a conclusion.  
  _↳ explanation: This statement is correct: inference means the reasoning step from premises to a conclusion. Look for a claim that conflicts with its definition._
- ◻️ conclusion: the claim the reasons are intended to establish.  
  _↳ explanation: This statement is correct: conclusion means the claim the reasons are intended to establish. Look for a claim that conflicts with its definition._
- ✅ A premise is always the final claim being defended.  
  _↳ explanation: The leaking roof is a reason; moving the books is the conclusion._
- ◻️ argument: claims offered as reasons for a conclusion.  
  _↳ explanation: This statement is correct: argument means claims offered as reasons for a conclusion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A premise is always the final claim being defended.”.  
> The leaking roof is a reason; moving the books is the conclusion.  

> Find the incorrect claim.

- ◻️ conclusion: the claim the reasons are intended to establish.  
  _↳ explanation: This statement is correct: conclusion means the claim the reasons are intended to establish. Look for a claim that conflicts with its definition._
- ✅ A premise is always the final claim being defended.  
  _↳ explanation: The leaking roof is a reason; moving the books is the conclusion._
- ◻️ inference: the reasoning step from premises to a conclusion.  
  _↳ explanation: This statement is correct: inference means the reasoning step from premises to a conclusion. Look for a claim that conflicts with its definition._
- ◻️ premise: a claim offered as support.  
  _↳ explanation: This statement is correct: premise means a claim offered as support. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A premise is always the final claim being defended.”.  
> The leaking roof is a reason; moving the books is the conclusion.  

> Find the incorrect claim.

- ◻️ conclusion: the claim the reasons are intended to establish.  
  _↳ explanation: This statement is correct: conclusion means the claim the reasons are intended to establish. Look for a claim that conflicts with its definition._
- ◻️ argument: claims offered as reasons for a conclusion.  
  _↳ explanation: This statement is correct: argument means claims offered as reasons for a conclusion. Look for a claim that conflicts with its definition._
- ✅ An argument must be an angry quarrel.  
  _↳ explanation: A calm proposal with supporting reasons is an argument; anger is irrelevant._
- ◻️ premise: a claim offered as support.  
  _↳ explanation: This statement is correct: premise means a claim offered as support. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “An argument must be an angry quarrel.”.  
> A calm proposal with supporting reasons is an argument; anger is irrelevant.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-terms` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: a reason's bearing on the claim under discussion ? | relevance | consistency · evidence · fallacy | consistency means claims being able to hold together without contradiction in the same respect; the question instead describes a reason's bearing on the claim under discussion. · evidence means information used to support or test a factual claim; the question instead describes a reason's bearing on the claim under discussion. · fallacy means a mistake in the reasoning offered; the question instead describes a reason's bearing on the claim under discussion. | A reason's bearing on the claim under discussion. |
| Which term means: claims being able to hold together without contradiction in the same respect ? | consistency | relevance · evidence · fallacy | relevance means a reason's bearing on the claim under discussion; the question instead describes claims being able to hold together without contradiction in the same respect. · evidence means information used to support or test a factual claim; the question instead describes claims being able to hold together without contradiction in the same respect. · fallacy means a mistake in the reasoning offered; the question instead describes claims being able to hold together without contradiction in the same respect. | Claims being able to hold together without contradiction in the same respect. |
| Which term means: information used to support or test a factual claim ? | evidence | relevance · consistency · fallacy | relevance means a reason's bearing on the claim under discussion; the question instead describes information used to support or test a factual claim. · consistency means claims being able to hold together without contradiction in the same respect; the question instead describes information used to support or test a factual claim. · fallacy means a mistake in the reasoning offered; the question instead describes information used to support or test a factual claim. | Information used to support or test a factual claim. |
| Which term means: a mistake in the reasoning offered ? | fallacy | relevance · consistency · evidence | relevance means a reason's bearing on the claim under discussion; the question instead describes a mistake in the reasoning offered. · consistency means claims being able to hold together without contradiction in the same respect; the question instead describes a mistake in the reasoning offered. · evidence means information used to support or test a factual claim; the question instead describes a mistake in the reasoning offered. | A mistake in the reasoning offered. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: a mistake in the reasoning offered ?

- ◻️ consistency  
  _↳ feedback if chosen: consistency means claims being able to hold together without contradiction in the same respect; the question instead describes a mistake in the reasoning offered._
- ✅ fallacy
- ◻️ relevance  
  _↳ feedback if chosen: relevance means a reason's bearing on the claim under discussion; the question instead describes a mistake in the reasoning offered._
- ◻️ evidence  
  _↳ feedback if chosen: evidence means information used to support or test a factual claim; the question instead describes a mistake in the reasoning offered._

Full working after a second miss:

> A mistake in the reasoning offered.  
> So the answer is “fallacy”.  

> Which term means: claims being able to hold together without contradiction in the same respect ?

- ◻️ evidence  
  _↳ feedback if chosen: evidence means information used to support or test a factual claim; the question instead describes claims being able to hold together without contradiction in the same respect._
- ◻️ relevance  
  _↳ feedback if chosen: relevance means a reason's bearing on the claim under discussion; the question instead describes claims being able to hold together without contradiction in the same respect._
- ✅ consistency
- ◻️ fallacy  
  _↳ feedback if chosen: fallacy means a mistake in the reasoning offered; the question instead describes claims being able to hold together without contradiction in the same respect._

Full working after a second miss:

> Claims being able to hold together without contradiction in the same respect.  
> So the answer is “consistency”.  

> Which term means: information used to support or test a factual claim ?

- ◻️ fallacy  
  _↳ feedback if chosen: fallacy means a mistake in the reasoning offered; the question instead describes information used to support or test a factual claim._
- ✅ evidence
- ◻️ consistency  
  _↳ feedback if chosen: consistency means claims being able to hold together without contradiction in the same respect; the question instead describes information used to support or test a factual claim._
- ◻️ relevance  
  _↳ feedback if chosen: relevance means a reason's bearing on the claim under discussion; the question instead describes information used to support or test a factual claim._

Full working after a second miss:

> Information used to support or test a factual claim.  
> So the answer is “evidence”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-cases` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A proposal to repair a roof cites water entering through holes.
Which term best fits this example? | relevance | consistency · evidence · fallacy | consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates a reason's bearing on the claim under discussion. · evidence concerns information used to support or test a factual claim. This case instead illustrates a reason's bearing on the claim under discussion. · fallacy concerns a mistake in the reasoning offered. This case instead illustrates a reason's bearing on the claim under discussion. | A proposal to repair a roof cites water entering through holes. A reason's bearing on the claim under discussion. |
| The club says its door is open this afternoon and not locked this afternoon.
Which term best fits this example? | consistency | relevance · evidence · fallacy | relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates claims being able to hold together without contradiction in the same respect. · evidence concerns information used to support or test a factual claim. This case instead illustrates claims being able to hold together without contradiction in the same respect. · fallacy concerns a mistake in the reasoning offered. This case instead illustrates claims being able to hold together without contradiction in the same respect. | The club says its door is open this afternoon and not locked this afternoon. Claims being able to hold together without contradiction in the same respect. |
| A learner checks a rain gauge before reporting rainfall.
Which term best fits this example? | evidence | relevance · consistency · fallacy | relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates information used to support or test a factual claim. · consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates information used to support or test a factual claim. · fallacy concerns a mistake in the reasoning offered. This case instead illustrates information used to support or test a factual claim. | A learner checks a rain gauge before reporting rainfall. Information used to support or test a factual claim. |
| A learner rejects a rainfall report solely because the reporter has old shoes.
Which term best fits this example? | fallacy | relevance · consistency · evidence | relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates a mistake in the reasoning offered. · consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates a mistake in the reasoning offered. · evidence concerns information used to support or test a factual claim. This case instead illustrates a mistake in the reasoning offered. | A learner rejects a rainfall report solely because the reporter has old shoes. A mistake in the reasoning offered. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner checks a rain gauge before reporting rainfall.
> Which term best fits this example?

- ◻️ consistency  
  _↳ feedback if chosen: consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates information used to support or test a factual claim._
- ✅ evidence
- ◻️ fallacy  
  _↳ feedback if chosen: fallacy concerns a mistake in the reasoning offered. This case instead illustrates information used to support or test a factual claim._
- ◻️ relevance  
  _↳ feedback if chosen: relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates information used to support or test a factual claim._

Full working after a second miss:

> A learner checks a rain gauge before reporting rainfall. Information used to support or test a factual claim.  
> So the answer is “evidence”.  

> A learner rejects a rainfall report solely because the reporter has old shoes.
> Which term best fits this example?

- ✅ fallacy
- ◻️ consistency  
  _↳ feedback if chosen: consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates a mistake in the reasoning offered._
- ◻️ evidence  
  _↳ feedback if chosen: evidence concerns information used to support or test a factual claim. This case instead illustrates a mistake in the reasoning offered._
- ◻️ relevance  
  _↳ feedback if chosen: relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates a mistake in the reasoning offered._

Full working after a second miss:

> A learner rejects a rainfall report solely because the reporter has old shoes. A mistake in the reasoning offered.  
> So the answer is “fallacy”.  

> A learner checks a rain gauge before reporting rainfall.
> Which term best fits this example?

- ◻️ relevance  
  _↳ feedback if chosen: relevance concerns a reason's bearing on the claim under discussion. This case instead illustrates information used to support or test a factual claim._
- ◻️ consistency  
  _↳ feedback if chosen: consistency concerns claims being able to hold together without contradiction in the same respect. This case instead illustrates information used to support or test a factual claim._
- ✅ evidence
- ◻️ fallacy  
  _↳ feedback if chosen: fallacy concerns a mistake in the reasoning offered. This case instead illustrates information used to support or test a factual claim._

Full working after a second miss:

> A learner checks a rain gauge before reporting rainfall. Information used to support or test a factual claim.  
> So the answer is “evidence”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-reason` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A proposal to repair a roof cites water entering through holes.
Which explanation justifies the classification? | A reason's bearing on the claim under discussion. | Claims being able to hold together without contradiction in the same respect. · Information used to support or test a factual claim. · A mistake in the reasoning offered. | That explanation describes consistency, rather than the relationship illustrated in this example. · That explanation describes evidence, rather than the relationship illustrated in this example. · That explanation describes fallacy, rather than the relationship illustrated in this example. | The evidence must bear on the particular conclusion; interest alone is insufficient. |
| The club says its door is open this afternoon and not locked this afternoon.
Which explanation justifies the classification? | Claims being able to hold together without contradiction in the same respect. | A reason's bearing on the claim under discussion. · Information used to support or test a factual claim. · A mistake in the reasoning offered. | That explanation describes relevance, rather than the relationship illustrated in this example. · That explanation describes evidence, rather than the relationship illustrated in this example. · That explanation describes fallacy, rather than the relationship illustrated in this example. | Consistency concerns compatibility of claims, not loudness or repetition. |
| A learner checks a rain gauge before reporting rainfall.
Which explanation justifies the classification? | Information used to support or test a factual claim. | A reason's bearing on the claim under discussion. · Claims being able to hold together without contradiction in the same respect. · A mistake in the reasoning offered. | That explanation describes relevance, rather than the relationship illustrated in this example. · That explanation describes consistency, rather than the relationship illustrated in this example. · That explanation describes fallacy, rather than the relationship illustrated in this example. | Repetition does not establish reliability; examine the underlying observations. |
| A learner rejects a rainfall report solely because the reporter has old shoes.
Which explanation justifies the classification? | A mistake in the reasoning offered. | A reason's bearing on the claim under discussion. · Claims being able to hold together without contradiction in the same respect. · Information used to support or test a factual claim. | That explanation describes relevance, rather than the relationship illustrated in this example. · That explanation describes consistency, rather than the relationship illustrated in this example. · That explanation describes evidence, rather than the relationship illustrated in this example. | The reporter's shoes do not establish whether the rainfall report is correct. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner checks a rain gauge before reporting rainfall.
> Which explanation justifies the classification?

- ◻️ A mistake in the reasoning offered.  
  _↳ feedback if chosen: That explanation describes fallacy, rather than the relationship illustrated in this example._
- ✅ Information used to support or test a factual claim.
- ◻️ Claims being able to hold together without contradiction in the same respect.  
  _↳ feedback if chosen: That explanation describes consistency, rather than the relationship illustrated in this example._
- ◻️ A reason's bearing on the claim under discussion.  
  _↳ feedback if chosen: That explanation describes relevance, rather than the relationship illustrated in this example._

Full working after a second miss:

> Repetition does not establish reliability; examine the underlying observations.  
> So the answer is “Information used to support or test a factual claim.”.  

> The club says its door is open this afternoon and not locked this afternoon.
> Which explanation justifies the classification?

- ✅ Claims being able to hold together without contradiction in the same respect.
- ◻️ A mistake in the reasoning offered.  
  _↳ feedback if chosen: That explanation describes fallacy, rather than the relationship illustrated in this example._
- ◻️ Information used to support or test a factual claim.  
  _↳ feedback if chosen: That explanation describes evidence, rather than the relationship illustrated in this example._
- ◻️ A reason's bearing on the claim under discussion.  
  _↳ feedback if chosen: That explanation describes relevance, rather than the relationship illustrated in this example._

Full working after a second miss:

> Consistency concerns compatibility of claims, not loudness or repetition.  
> So the answer is “Claims being able to hold together without contradiction in the same respect.”.  

> A learner checks a rain gauge before reporting rainfall.
> Which explanation justifies the classification?

- ◻️ A reason's bearing on the claim under discussion.  
  _↳ feedback if chosen: That explanation describes relevance, rather than the relationship illustrated in this example._
- ◻️ Claims being able to hold together without contradiction in the same respect.  
  _↳ feedback if chosen: That explanation describes consistency, rather than the relationship illustrated in this example._
- ✅ Information used to support or test a factual claim.
- ◻️ A mistake in the reasoning offered.  
  _↳ feedback if chosen: That explanation describes fallacy, rather than the relationship illustrated in this example._

Full working after a second miss:

> Repetition does not establish reliability; examine the underlying observations.  
> So the answer is “Information used to support or test a factual claim.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-link` · Lesson 2 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- relevance → **A proposal to repair a roof cites water entering through holes.**
- consistency → **The club says its door is open this afternoon and not locked this afternoon.**
- evidence → **A learner checks a rain gauge before reporting rainfall.**
- fallacy → **A learner rejects a rainfall report solely because the reporter has old shoes.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): A learner checks a rain gauge before reporting rainfall. · The club says its door is open this afternoon and not locked this afternoon. · A proposal to repair a roof cites water entering through holes.
- evidence → **A learner checks a rain gauge before reporting rainfall.**
- relevance → **A proposal to repair a roof cites water entering through holes.**
- consistency → **The club says its door is open this afternoon and not locked this afternoon.**

Full working after a second miss:

> The right pairs are:  
> evidence → A learner checks a rain gauge before reporting rainfall.  
> relevance → A proposal to repair a roof cites water entering through holes.  
> consistency → The club says its door is open this afternoon and not locked this afternoon.  

> Match each term to its example.

Right-hand side (shuffled): A proposal to repair a roof cites water entering through holes. · A learner checks a rain gauge before reporting rainfall. · The club says its door is open this afternoon and not locked this afternoon.
- relevance → **A proposal to repair a roof cites water entering through holes.**
- consistency → **The club says its door is open this afternoon and not locked this afternoon.**
- evidence → **A learner checks a rain gauge before reporting rainfall.**

Full working after a second miss:

> The right pairs are:  
> relevance → A proposal to repair a roof cites water entering through holes.  
> consistency → The club says its door is open this afternoon and not locked this afternoon.  
> evidence → A learner checks a rain gauge before reporting rainfall.  

> Match each term to its example.

Right-hand side (shuffled): The club says its door is open this afternoon and not locked this afternoon. · A learner checks a rain gauge before reporting rainfall. · A learner rejects a rainfall report solely because the reporter has old shoes.
- evidence → **A learner checks a rain gauge before reporting rainfall.**
- fallacy → **A learner rejects a rainfall report solely because the reporter has old shoes.**
- consistency → **The club says its door is open this afternoon and not locked this afternoon.**

Full working after a second miss:

> The right pairs are:  
> evidence → A learner checks a rain gauge before reporting rainfall.  
> fallacy → A learner rejects a rainfall report solely because the reporter has old shoes.  
> consistency → The club says its door is open this afternoon and not locked this afternoon.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-repair` · Lesson 2 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ relevance: a reason's bearing on the claim under discussion.
- ✅ consistency: claims being able to hold together without contradiction in the same respect.
- ✅ evidence: information used to support or test a factual claim.
- ✅ fallacy: a mistake in the reasoning offered.
- ❌ Any interesting fact supports any conclusion.  
  _↳ The evidence must bear on the particular conclusion; interest alone is insufficient._
- ❌ Consistency means repeating words loudly.  
  _↳ Consistency concerns compatibility of claims, not loudness or repetition._
- ❌ A rumour is conclusive evidence because many people repeat it.  
  _↳ Repetition does not establish reliability; examine the underlying observations._
- ❌ Disliking a reporter disproves the report.  
  _↳ The reporter's shoes do not establish whether the rainfall report is correct._


Three generated variants:

> Find the incorrect claim.

- ◻️ fallacy: a mistake in the reasoning offered.  
  _↳ explanation: This statement is correct: fallacy means a mistake in the reasoning offered. Look for a claim that conflicts with its definition._
- ◻️ relevance: a reason's bearing on the claim under discussion.  
  _↳ explanation: This statement is correct: relevance means a reason's bearing on the claim under discussion. Look for a claim that conflicts with its definition._
- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ✅ A rumour is conclusive evidence because many people repeat it.  
  _↳ explanation: Repetition does not establish reliability; examine the underlying observations._

Full working after a second miss:

> The wrong statement is “A rumour is conclusive evidence because many people repeat it.”.  
> Repetition does not establish reliability; examine the underlying observations.  

> Find the incorrect claim.

- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ◻️ relevance: a reason's bearing on the claim under discussion.  
  _↳ explanation: This statement is correct: relevance means a reason's bearing on the claim under discussion. Look for a claim that conflicts with its definition._
- ✅ Any interesting fact supports any conclusion.  
  _↳ explanation: The evidence must bear on the particular conclusion; interest alone is insufficient._
- ◻️ fallacy: a mistake in the reasoning offered.  
  _↳ explanation: This statement is correct: fallacy means a mistake in the reasoning offered. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Any interesting fact supports any conclusion.”.  
> The evidence must bear on the particular conclusion; interest alone is insufficient.  

> Find the incorrect claim.

- ✅ Disliking a reporter disproves the report.  
  _↳ explanation: The reporter's shoes do not establish whether the rainfall report is correct._
- ◻️ evidence: information used to support or test a factual claim.  
  _↳ explanation: This statement is correct: evidence means information used to support or test a factual claim. Look for a claim that conflicts with its definition._
- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ◻️ fallacy: a mistake in the reasoning offered.  
  _↳ explanation: This statement is correct: fallacy means a mistake in the reasoning offered. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Disliking a reporter disproves the report.”.  
> The reporter's shoes do not establish whether the rainfall report is correct.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-2-repair-card` · Lesson 2 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ relevance: a reason's bearing on the claim under discussion.
- ✅ consistency: claims being able to hold together without contradiction in the same respect.
- ✅ evidence: information used to support or test a factual claim.
- ✅ fallacy: a mistake in the reasoning offered.
- ❌ Any interesting fact supports any conclusion.  
  _↳ The evidence must bear on the particular conclusion; interest alone is insufficient._
- ❌ Consistency means repeating words loudly.  
  _↳ Consistency concerns compatibility of claims, not loudness or repetition._
- ❌ A rumour is conclusive evidence because many people repeat it.  
  _↳ Repetition does not establish reliability; examine the underlying observations._
- ❌ Disliking a reporter disproves the report.  
  _↳ The reporter's shoes do not establish whether the rainfall report is correct._


Three generated variants:

> Find the incorrect claim.

- ◻️ relevance: a reason's bearing on the claim under discussion.  
  _↳ explanation: This statement is correct: relevance means a reason's bearing on the claim under discussion. Look for a claim that conflicts with its definition._
- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ◻️ fallacy: a mistake in the reasoning offered.  
  _↳ explanation: This statement is correct: fallacy means a mistake in the reasoning offered. Look for a claim that conflicts with its definition._
- ✅ Any interesting fact supports any conclusion.  
  _↳ explanation: The evidence must bear on the particular conclusion; interest alone is insufficient._

Full working after a second miss:

> The wrong statement is “Any interesting fact supports any conclusion.”.  
> The evidence must bear on the particular conclusion; interest alone is insufficient.  

> Find the incorrect claim.

- ✅ Disliking a reporter disproves the report.  
  _↳ explanation: The reporter's shoes do not establish whether the rainfall report is correct._
- ◻️ evidence: information used to support or test a factual claim.  
  _↳ explanation: This statement is correct: evidence means information used to support or test a factual claim. Look for a claim that conflicts with its definition._
- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ◻️ relevance: a reason's bearing on the claim under discussion.  
  _↳ explanation: This statement is correct: relevance means a reason's bearing on the claim under discussion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Disliking a reporter disproves the report.”.  
> The reporter's shoes do not establish whether the rainfall report is correct.  

> Find the incorrect claim.

- ◻️ fallacy: a mistake in the reasoning offered.  
  _↳ explanation: This statement is correct: fallacy means a mistake in the reasoning offered. Look for a claim that conflicts with its definition._
- ◻️ consistency: claims being able to hold together without contradiction in the same respect.  
  _↳ explanation: This statement is correct: consistency means claims being able to hold together without contradiction in the same respect. Look for a claim that conflicts with its definition._
- ✅ A rumour is conclusive evidence because many people repeat it.  
  _↳ explanation: Repetition does not establish reliability; examine the underlying observations._
- ◻️ evidence: information used to support or test a factual claim.  
  _↳ explanation: This statement is correct: evidence means information used to support or test a factual claim. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A rumour is conclusive evidence because many people repeat it.”.  
> Repetition does not establish reliability; examine the underlying observations.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-terms` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: assessment of the structure of an inference ? | formal logic | material assessment · deductive assessment · inductive assessment | material assessment means examination of the content or factual truth of claims; the question instead describes assessment of the structure of an inference. · deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes assessment of the structure of an inference. · inductive assessment means judging how strongly evidence supports a probable conclusion; the question instead describes assessment of the structure of an inference. | Assessment of the structure of an inference. |
| Which term means: examination of the content or factual truth of claims ? | material assessment | formal logic · deductive assessment · inductive assessment | formal logic means assessment of the structure of an inference; the question instead describes examination of the content or factual truth of claims. · deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes examination of the content or factual truth of claims. · inductive assessment means judging how strongly evidence supports a probable conclusion; the question instead describes examination of the content or factual truth of claims. | Examination of the content or factual truth of claims. |
| Which term means: asking whether true premises would guarantee the conclusion ? | deductive assessment | formal logic · material assessment · inductive assessment | formal logic means assessment of the structure of an inference; the question instead describes asking whether true premises would guarantee the conclusion. · material assessment means examination of the content or factual truth of claims; the question instead describes asking whether true premises would guarantee the conclusion. · inductive assessment means judging how strongly evidence supports a probable conclusion; the question instead describes asking whether true premises would guarantee the conclusion. | Asking whether true premises would guarantee the conclusion. |
| Which term means: judging how strongly evidence supports a probable conclusion ? | inductive assessment | formal logic · material assessment · deductive assessment | formal logic means assessment of the structure of an inference; the question instead describes judging how strongly evidence supports a probable conclusion. · material assessment means examination of the content or factual truth of claims; the question instead describes judging how strongly evidence supports a probable conclusion. · deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes judging how strongly evidence supports a probable conclusion. | Judging how strongly evidence supports a probable conclusion. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: judging how strongly evidence supports a probable conclusion ?

- ✅ inductive assessment
- ◻️ deductive assessment  
  _↳ feedback if chosen: deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes judging how strongly evidence supports a probable conclusion._
- ◻️ material assessment  
  _↳ feedback if chosen: material assessment means examination of the content or factual truth of claims; the question instead describes judging how strongly evidence supports a probable conclusion._
- ◻️ formal logic  
  _↳ feedback if chosen: formal logic means assessment of the structure of an inference; the question instead describes judging how strongly evidence supports a probable conclusion._

Full working after a second miss:

> Judging how strongly evidence supports a probable conclusion.  
> So the answer is “inductive assessment”.  

> Which term means: assessment of the structure of an inference ?

- ◻️ material assessment  
  _↳ feedback if chosen: material assessment means examination of the content or factual truth of claims; the question instead describes assessment of the structure of an inference._
- ◻️ deductive assessment  
  _↳ feedback if chosen: deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes assessment of the structure of an inference._
- ✅ formal logic
- ◻️ inductive assessment  
  _↳ feedback if chosen: inductive assessment means judging how strongly evidence supports a probable conclusion; the question instead describes assessment of the structure of an inference._

Full working after a second miss:

> Assessment of the structure of an inference.  
> So the answer is “formal logic”.  

> Which term means: examination of the content or factual truth of claims ?

- ◻️ formal logic  
  _↳ feedback if chosen: formal logic means assessment of the structure of an inference; the question instead describes examination of the content or factual truth of claims._
- ✅ material assessment
- ◻️ inductive assessment  
  _↳ feedback if chosen: inductive assessment means judging how strongly evidence supports a probable conclusion; the question instead describes examination of the content or factual truth of claims._
- ◻️ deductive assessment  
  _↳ feedback if chosen: deductive assessment means asking whether true premises would guarantee the conclusion; the question instead describes examination of the content or factual truth of claims._

Full working after a second miss:

> Examination of the content or factual truth of claims.  
> So the answer is “material assessment”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-cases` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.
Which term best fits this example? | formal logic | material assessment · deductive assessment · inductive assessment | material assessment concerns examination of the content or factual truth of claims. This case instead illustrates assessment of the structure of an inference. · deductive assessment concerns asking whether true premises would guarantee the conclusion. This case instead illustrates assessment of the structure of an inference. · inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates assessment of the structure of an inference. | A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card. Assessment of the structure of an inference. |
| A learner checks the actual club register to see whether Bih belongs.
Which term best fits this example? | material assessment | formal logic · deductive assessment · inductive assessment | formal logic concerns assessment of the structure of an inference. This case instead illustrates examination of the content or factual truth of claims. · deductive assessment concerns asking whether true premises would guarantee the conclusion. This case instead illustrates examination of the content or factual truth of claims. · inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates examination of the content or factual truth of claims. | A learner checks the actual club register to see whether Bih belongs. Examination of the content or factual truth of claims. |
| A learner asks if a counterexample could leave the premises true but the conclusion false.
Which term best fits this example? | deductive assessment | formal logic · material assessment · inductive assessment | formal logic concerns assessment of the structure of an inference. This case instead illustrates asking whether true premises would guarantee the conclusion. · material assessment concerns examination of the content or factual truth of claims. This case instead illustrates asking whether true premises would guarantee the conclusion. · inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates asking whether true premises would guarantee the conclusion. | A learner asks if a counterexample could leave the premises true but the conclusion false. Asking whether true premises would guarantee the conclusion. |
| A learner evaluates how representative a market survey is before generalising.
Which term best fits this example? | inductive assessment | formal logic · material assessment · deductive assessment | formal logic concerns assessment of the structure of an inference. This case instead illustrates judging how strongly evidence supports a probable conclusion. · material assessment concerns examination of the content or factual truth of claims. This case instead illustrates judging how strongly evidence supports a probable conclusion. · deductive assessment concerns asking whether true premises would guarantee the conclusion. This case instead illustrates judging how strongly evidence supports a probable conclusion. | A learner evaluates how representative a market survey is before generalising. Judging how strongly evidence supports a probable conclusion. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.
> Which term best fits this example?

- ✅ formal logic
- ◻️ deductive assessment  
  _↳ feedback if chosen: deductive assessment concerns asking whether true premises would guarantee the conclusion. This case instead illustrates assessment of the structure of an inference._
- ◻️ material assessment  
  _↳ feedback if chosen: material assessment concerns examination of the content or factual truth of claims. This case instead illustrates assessment of the structure of an inference._
- ◻️ inductive assessment  
  _↳ feedback if chosen: inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates assessment of the structure of an inference._

Full working after a second miss:

> A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card. Assessment of the structure of an inference.  
> So the answer is “formal logic”.  

> A learner checks the actual club register to see whether Bih belongs.
> Which term best fits this example?

- ✅ material assessment
- ◻️ deductive assessment  
  _↳ feedback if chosen: deductive assessment concerns asking whether true premises would guarantee the conclusion. This case instead illustrates examination of the content or factual truth of claims._
- ◻️ formal logic  
  _↳ feedback if chosen: formal logic concerns assessment of the structure of an inference. This case instead illustrates examination of the content or factual truth of claims._
- ◻️ inductive assessment  
  _↳ feedback if chosen: inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates examination of the content or factual truth of claims._

Full working after a second miss:

> A learner checks the actual club register to see whether Bih belongs. Examination of the content or factual truth of claims.  
> So the answer is “material assessment”.  

> A learner asks if a counterexample could leave the premises true but the conclusion false.
> Which term best fits this example?

- ◻️ formal logic  
  _↳ feedback if chosen: formal logic concerns assessment of the structure of an inference. This case instead illustrates asking whether true premises would guarantee the conclusion._
- ✅ deductive assessment
- ◻️ inductive assessment  
  _↳ feedback if chosen: inductive assessment concerns judging how strongly evidence supports a probable conclusion. This case instead illustrates asking whether true premises would guarantee the conclusion._
- ◻️ material assessment  
  _↳ feedback if chosen: material assessment concerns examination of the content or factual truth of claims. This case instead illustrates asking whether true premises would guarantee the conclusion._

Full working after a second miss:

> A learner asks if a counterexample could leave the premises true but the conclusion false. Asking whether true premises would guarantee the conclusion.  
> So the answer is “deductive assessment”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-reason` · Lesson 3 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.
Which explanation justifies the classification? | Assessment of the structure of an inference. | Examination of the content or factual truth of claims. · Asking whether true premises would guarantee the conclusion. · Judging how strongly evidence supports a probable conclusion. | That explanation describes material assessment, rather than the relationship illustrated in this example. · That explanation describes deductive assessment, rather than the relationship illustrated in this example. · That explanation describes inductive assessment, rather than the relationship illustrated in this example. | A valid pattern preserves truth conditionally; premise truth needs separate checking. |
| A learner checks the actual club register to see whether Bih belongs.
Which explanation justifies the classification? | Examination of the content or factual truth of claims. | Assessment of the structure of an inference. · Asking whether true premises would guarantee the conclusion. · Judging how strongly evidence supports a probable conclusion. | That explanation describes formal logic, rather than the relationship illustrated in this example. · That explanation describes deductive assessment, rather than the relationship illustrated in this example. · That explanation describes inductive assessment, rather than the relationship illustrated in this example. | Consulting a register checks content, not just logical form. |
| A learner asks if a counterexample could leave the premises true but the conclusion false.
Which explanation justifies the classification? | Asking whether true premises would guarantee the conclusion. | Assessment of the structure of an inference. · Examination of the content or factual truth of claims. · Judging how strongly evidence supports a probable conclusion. | That explanation describes formal logic, rather than the relationship illustrated in this example. · That explanation describes material assessment, rather than the relationship illustrated in this example. · That explanation describes inductive assessment, rather than the relationship illustrated in this example. | Deductive validity excludes a true-premise, false-conclusion counterexample. |
| A learner evaluates how representative a market survey is before generalising.
Which explanation justifies the classification? | Judging how strongly evidence supports a probable conclusion. | Assessment of the structure of an inference. · Examination of the content or factual truth of claims. · Asking whether true premises would guarantee the conclusion. | That explanation describes formal logic, rather than the relationship illustrated in this example. · That explanation describes material assessment, rather than the relationship illustrated in this example. · That explanation describes deductive assessment, rather than the relationship illustrated in this example. | An induction can support a probability without guaranteeing all cases. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner checks the actual club register to see whether Bih belongs.
> Which explanation justifies the classification?

- ◻️ Assessment of the structure of an inference.  
  _↳ feedback if chosen: That explanation describes formal logic, rather than the relationship illustrated in this example._
- ◻️ Judging how strongly evidence supports a probable conclusion.  
  _↳ feedback if chosen: That explanation describes inductive assessment, rather than the relationship illustrated in this example._
- ◻️ Asking whether true premises would guarantee the conclusion.  
  _↳ feedback if chosen: That explanation describes deductive assessment, rather than the relationship illustrated in this example._
- ✅ Examination of the content or factual truth of claims.

Full working after a second miss:

> Consulting a register checks content, not just logical form.  
> So the answer is “Examination of the content or factual truth of claims.”.  

> A learner evaluates how representative a market survey is before generalising.
> Which explanation justifies the classification?

- ✅ Judging how strongly evidence supports a probable conclusion.
- ◻️ Examination of the content or factual truth of claims.  
  _↳ feedback if chosen: That explanation describes material assessment, rather than the relationship illustrated in this example._
- ◻️ Assessment of the structure of an inference.  
  _↳ feedback if chosen: That explanation describes formal logic, rather than the relationship illustrated in this example._
- ◻️ Asking whether true premises would guarantee the conclusion.  
  _↳ feedback if chosen: That explanation describes deductive assessment, rather than the relationship illustrated in this example._

Full working after a second miss:

> An induction can support a probability without guaranteeing all cases.  
> So the answer is “Judging how strongly evidence supports a probable conclusion.”.  

> A learner checks the actual club register to see whether Bih belongs.
> Which explanation justifies the classification?

- ✅ Examination of the content or factual truth of claims.
- ◻️ Assessment of the structure of an inference.  
  _↳ feedback if chosen: That explanation describes formal logic, rather than the relationship illustrated in this example._
- ◻️ Asking whether true premises would guarantee the conclusion.  
  _↳ feedback if chosen: That explanation describes deductive assessment, rather than the relationship illustrated in this example._
- ◻️ Judging how strongly evidence supports a probable conclusion.  
  _↳ feedback if chosen: That explanation describes inductive assessment, rather than the relationship illustrated in this example._

Full working after a second miss:

> Consulting a register checks content, not just logical form.  
> So the answer is “Examination of the content or factual truth of claims.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-link` · Lesson 3 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- formal logic → **A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.**
- material assessment → **A learner checks the actual club register to see whether Bih belongs.**
- deductive assessment → **A learner asks if a counterexample could leave the premises true but the conclusion false.**
- inductive assessment → **A learner evaluates how representative a market survey is before generalising.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): A learner asks if a counterexample could leave the premises true but the conclusion false. · A learner evaluates how representative a market survey is before generalising. · A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.
- formal logic → **A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.**
- deductive assessment → **A learner asks if a counterexample could leave the premises true but the conclusion false.**
- inductive assessment → **A learner evaluates how representative a market survey is before generalising.**

Full working after a second miss:

> The right pairs are:  
> formal logic → A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.  
> deductive assessment → A learner asks if a counterexample could leave the premises true but the conclusion false.  
> inductive assessment → A learner evaluates how representative a market survey is before generalising.  

> Match each term to its example.

Right-hand side (shuffled): A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card. · A learner evaluates how representative a market survey is before generalising. · A learner checks the actual club register to see whether Bih belongs.
- inductive assessment → **A learner evaluates how representative a market survey is before generalising.**
- material assessment → **A learner checks the actual club register to see whether Bih belongs.**
- formal logic → **A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.**

Full working after a second miss:

> The right pairs are:  
> inductive assessment → A learner evaluates how representative a market survey is before generalising.  
> material assessment → A learner checks the actual club register to see whether Bih belongs.  
> formal logic → A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.  

> Match each term to its example.

Right-hand side (shuffled): A learner evaluates how representative a market survey is before generalising. · A learner checks the actual club register to see whether Bih belongs. · A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.
- formal logic → **A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.**
- inductive assessment → **A learner evaluates how representative a market survey is before generalising.**
- material assessment → **A learner checks the actual club register to see whether Bih belongs.**

Full working after a second miss:

> The right pairs are:  
> formal logic → A learner checks the pattern all members have cards; Bih is a member; therefore Bih has a card.  
> inductive assessment → A learner evaluates how representative a market survey is before generalising.  
> material assessment → A learner checks the actual club register to see whether Bih belongs.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-repair` · Lesson 3 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ formal logic: assessment of the structure of an inference.
- ✅ material assessment: examination of the content or factual truth of claims.
- ✅ deductive assessment: asking whether true premises would guarantee the conclusion.
- ✅ inductive assessment: judging how strongly evidence supports a probable conclusion.
- ❌ Formal validity proves that every premise is factually true.  
  _↳ A valid pattern preserves truth conditionally; premise truth needs separate checking._
- ❌ Checking a register is only an examination of sentence shape.  
  _↳ Consulting a register checks content, not just logical form._
- ❌ Any plausible conclusion is deductively valid.  
  _↳ Deductive validity excludes a true-premise, false-conclusion counterexample._
- ❌ A sample guarantees every future case.  
  _↳ An induction can support a probability without guaranteeing all cases._


Three generated variants:

> Find the incorrect claim.

- ✅ Formal validity proves that every premise is factually true.  
  _↳ explanation: A valid pattern preserves truth conditionally; premise truth needs separate checking._
- ◻️ deductive assessment: asking whether true premises would guarantee the conclusion.  
  _↳ explanation: This statement is correct: deductive assessment means asking whether true premises would guarantee the conclusion. Look for a claim that conflicts with its definition._
- ◻️ formal logic: assessment of the structure of an inference.  
  _↳ explanation: This statement is correct: formal logic means assessment of the structure of an inference. Look for a claim that conflicts with its definition._
- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Formal validity proves that every premise is factually true.”.  
> A valid pattern preserves truth conditionally; premise truth needs separate checking.  

> Find the incorrect claim.

- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._
- ◻️ deductive assessment: asking whether true premises would guarantee the conclusion.  
  _↳ explanation: This statement is correct: deductive assessment means asking whether true premises would guarantee the conclusion. Look for a claim that conflicts with its definition._
- ✅ A sample guarantees every future case.  
  _↳ explanation: An induction can support a probability without guaranteeing all cases._
- ◻️ inductive assessment: judging how strongly evidence supports a probable conclusion.  
  _↳ explanation: This statement is correct: inductive assessment means judging how strongly evidence supports a probable conclusion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A sample guarantees every future case.”.  
> An induction can support a probability without guaranteeing all cases.  

> Find the incorrect claim.

- ◻️ formal logic: assessment of the structure of an inference.  
  _↳ explanation: This statement is correct: formal logic means assessment of the structure of an inference. Look for a claim that conflicts with its definition._
- ✅ Any plausible conclusion is deductively valid.  
  _↳ explanation: Deductive validity excludes a true-premise, false-conclusion counterexample._
- ◻️ inductive assessment: judging how strongly evidence supports a probable conclusion.  
  _↳ explanation: This statement is correct: inductive assessment means judging how strongly evidence supports a probable conclusion. Look for a claim that conflicts with its definition._
- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Any plausible conclusion is deductively valid.”.  
> Deductive validity excludes a true-premise, false-conclusion counterexample.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-3-repair-card` · Lesson 3 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ formal logic: assessment of the structure of an inference.
- ✅ material assessment: examination of the content or factual truth of claims.
- ✅ deductive assessment: asking whether true premises would guarantee the conclusion.
- ✅ inductive assessment: judging how strongly evidence supports a probable conclusion.
- ❌ Formal validity proves that every premise is factually true.  
  _↳ A valid pattern preserves truth conditionally; premise truth needs separate checking._
- ❌ Checking a register is only an examination of sentence shape.  
  _↳ Consulting a register checks content, not just logical form._
- ❌ Any plausible conclusion is deductively valid.  
  _↳ Deductive validity excludes a true-premise, false-conclusion counterexample._
- ❌ A sample guarantees every future case.  
  _↳ An induction can support a probability without guaranteeing all cases._


Three generated variants:

> Find the incorrect claim.

- ◻️ formal logic: assessment of the structure of an inference.  
  _↳ explanation: This statement is correct: formal logic means assessment of the structure of an inference. Look for a claim that conflicts with its definition._
- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._
- ◻️ inductive assessment: judging how strongly evidence supports a probable conclusion.  
  _↳ explanation: This statement is correct: inductive assessment means judging how strongly evidence supports a probable conclusion. Look for a claim that conflicts with its definition._
- ✅ Any plausible conclusion is deductively valid.  
  _↳ explanation: Deductive validity excludes a true-premise, false-conclusion counterexample._

Full working after a second miss:

> The wrong statement is “Any plausible conclusion is deductively valid.”.  
> Deductive validity excludes a true-premise, false-conclusion counterexample.  

> Find the incorrect claim.

- ◻️ formal logic: assessment of the structure of an inference.  
  _↳ explanation: This statement is correct: formal logic means assessment of the structure of an inference. Look for a claim that conflicts with its definition._
- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._
- ✅ A sample guarantees every future case.  
  _↳ explanation: An induction can support a probability without guaranteeing all cases._
- ◻️ deductive assessment: asking whether true premises would guarantee the conclusion.  
  _↳ explanation: This statement is correct: deductive assessment means asking whether true premises would guarantee the conclusion. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A sample guarantees every future case.”.  
> An induction can support a probability without guaranteeing all cases.  

> Find the incorrect claim.

- ◻️ material assessment: examination of the content or factual truth of claims.  
  _↳ explanation: This statement is correct: material assessment means examination of the content or factual truth of claims. Look for a claim that conflicts with its definition._
- ✅ Checking a register is only an examination of sentence shape.  
  _↳ explanation: Consulting a register checks content, not just logical form._
- ◻️ inductive assessment: judging how strongly evidence supports a probable conclusion.  
  _↳ explanation: This statement is correct: inductive assessment means judging how strongly evidence supports a probable conclusion. Look for a claim that conflicts with its definition._
- ◻️ formal logic: assessment of the structure of an inference.  
  _↳ explanation: This statement is correct: formal logic means assessment of the structure of an inference. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Checking a register is only an examination of sentence shape.”.  
> Consulting a register checks content, not just logical form.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-terms` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: reasoning that aims to guarantee its conclusion from its premises ? | deduction | induction · symbolic representation · informal analysis | induction means reasoning that supports a conclusion as probable from evidence; the question instead describes reasoning that aims to guarantee its conclusion from its premises. · symbolic representation means use of symbols to express logical relationships; the question instead describes reasoning that aims to guarantee its conclusion from its premises. · informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes reasoning that aims to guarantee its conclusion from its premises. | Reasoning that aims to guarantee its conclusion from its premises. |
| Which term means: reasoning that supports a conclusion as probable from evidence ? | induction | deduction · symbolic representation · informal analysis | deduction means reasoning that aims to guarantee its conclusion from its premises; the question instead describes reasoning that supports a conclusion as probable from evidence. · symbolic representation means use of symbols to express logical relationships; the question instead describes reasoning that supports a conclusion as probable from evidence. · informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes reasoning that supports a conclusion as probable from evidence. | Reasoning that supports a conclusion as probable from evidence. |
| Which term means: use of symbols to express logical relationships ? | symbolic representation | deduction · induction · informal analysis | deduction means reasoning that aims to guarantee its conclusion from its premises; the question instead describes use of symbols to express logical relationships. · induction means reasoning that supports a conclusion as probable from evidence; the question instead describes use of symbols to express logical relationships. · informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes use of symbols to express logical relationships. | Use of symbols to express logical relationships. |
| Which term means: assessment of reasoning expressed in ordinary language ? | informal analysis | deduction · induction · symbolic representation | deduction means reasoning that aims to guarantee its conclusion from its premises; the question instead describes assessment of reasoning expressed in ordinary language. · induction means reasoning that supports a conclusion as probable from evidence; the question instead describes assessment of reasoning expressed in ordinary language. · symbolic representation means use of symbols to express logical relationships; the question instead describes assessment of reasoning expressed in ordinary language. | Assessment of reasoning expressed in ordinary language. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: reasoning that supports a conclusion as probable from evidence ?

- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation means use of symbols to express logical relationships; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ◻️ deduction  
  _↳ feedback if chosen: deduction means reasoning that aims to guarantee its conclusion from its premises; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ✅ induction

Full working after a second miss:

> Reasoning that supports a conclusion as probable from evidence.  
> So the answer is “induction”.  

> Which term means: reasoning that aims to guarantee its conclusion from its premises ?

- ◻️ induction  
  _↳ feedback if chosen: induction means reasoning that supports a conclusion as probable from evidence; the question instead describes reasoning that aims to guarantee its conclusion from its premises._
- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes reasoning that aims to guarantee its conclusion from its premises._
- ✅ deduction
- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation means use of symbols to express logical relationships; the question instead describes reasoning that aims to guarantee its conclusion from its premises._

Full working after a second miss:

> Reasoning that aims to guarantee its conclusion from its premises.  
> So the answer is “deduction”.  

> Which term means: reasoning that supports a conclusion as probable from evidence ?

- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation means use of symbols to express logical relationships; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis means assessment of reasoning expressed in ordinary language; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ◻️ deduction  
  _↳ feedback if chosen: deduction means reasoning that aims to guarantee its conclusion from its premises; the question instead describes reasoning that supports a conclusion as probable from evidence._
- ✅ induction

Full working after a second miss:

> Reasoning that supports a conclusion as probable from evidence.  
> So the answer is “induction”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-cases` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.
Which term best fits this example? | deduction | induction · symbolic representation · informal analysis | induction concerns reasoning that supports a conclusion as probable from evidence. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises. · symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises. · informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises. | All cards in a hypothetical box are blue; this card is from that box; therefore it is blue. Reasoning that aims to guarantee its conclusion from its premises. |
| Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
Which term best fits this example? | induction | deduction · symbolic representation · informal analysis | deduction concerns reasoning that aims to guarantee its conclusion from its premises. This case instead illustrates reasoning that supports a conclusion as probable from evidence. · symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates reasoning that supports a conclusion as probable from evidence. · informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates reasoning that supports a conclusion as probable from evidence. | Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do. Reasoning that supports a conclusion as probable from evidence. |
| A pupil writes P and not P to display a conflict in a claim.
Which term best fits this example? | symbolic representation | deduction · induction · informal analysis | deduction concerns reasoning that aims to guarantee its conclusion from its premises. This case instead illustrates use of symbols to express logical relationships. · induction concerns reasoning that supports a conclusion as probable from evidence. This case instead illustrates use of symbols to express logical relationships. · informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates use of symbols to express logical relationships. | A pupil writes P and not P to display a conflict in a claim. Use of symbols to express logical relationships. |
| A class checks whether a club proposal's stated reasons address the proposal.
Which term best fits this example? | informal analysis | deduction · induction · symbolic representation | deduction concerns reasoning that aims to guarantee its conclusion from its premises. This case instead illustrates assessment of reasoning expressed in ordinary language. · induction concerns reasoning that supports a conclusion as probable from evidence. This case instead illustrates assessment of reasoning expressed in ordinary language. · symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates assessment of reasoning expressed in ordinary language. | A class checks whether a club proposal's stated reasons address the proposal. Assessment of reasoning expressed in ordinary language. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.
> Which term best fits this example?

- ◻️ induction  
  _↳ feedback if chosen: induction concerns reasoning that supports a conclusion as probable from evidence. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises._
- ✅ deduction
- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises._
- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates reasoning that aims to guarantee its conclusion from its premises._

Full working after a second miss:

> All cards in a hypothetical box are blue; this card is from that box; therefore it is blue. Reasoning that aims to guarantee its conclusion from its premises.  
> So the answer is “deduction”.  

> Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
> Which term best fits this example?

- ✅ induction
- ◻️ deduction  
  _↳ feedback if chosen: deduction concerns reasoning that aims to guarantee its conclusion from its premises. This case instead illustrates reasoning that supports a conclusion as probable from evidence._
- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates reasoning that supports a conclusion as probable from evidence._
- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates reasoning that supports a conclusion as probable from evidence._

Full working after a second miss:

> Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do. Reasoning that supports a conclusion as probable from evidence.  
> So the answer is “induction”.  

> Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
> Which term best fits this example?

- ◻️ informal analysis  
  _↳ feedback if chosen: informal analysis concerns assessment of reasoning expressed in ordinary language. This case instead illustrates reasoning that supports a conclusion as probable from evidence._
- ◻️ deduction  
  _↳ feedback if chosen: deduction concerns reasoning that aims to guarantee its conclusion from its premises. This case instead illustrates reasoning that supports a conclusion as probable from evidence._
- ✅ induction
- ◻️ symbolic representation  
  _↳ feedback if chosen: symbolic representation concerns use of symbols to express logical relationships. This case instead illustrates reasoning that supports a conclusion as probable from evidence._

Full working after a second miss:

> Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do. Reasoning that supports a conclusion as probable from evidence.  
> So the answer is “induction”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-reason` · Lesson 4 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.
Which explanation justifies the classification? | Reasoning that aims to guarantee its conclusion from its premises. | Reasoning that supports a conclusion as probable from evidence. · Use of symbols to express logical relationships. · Assessment of reasoning expressed in ordinary language. | That explanation describes induction, rather than the relationship illustrated in this example. · That explanation describes symbolic representation, rather than the relationship illustrated in this example. · That explanation describes informal analysis, rather than the relationship illustrated in this example. | The defining aim is necessary support, not the number of cases mentioned. |
| Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
Which explanation justifies the classification? | Reasoning that supports a conclusion as probable from evidence. | Reasoning that aims to guarantee its conclusion from its premises. · Use of symbols to express logical relationships. · Assessment of reasoning expressed in ordinary language. | That explanation describes deduction, rather than the relationship illustrated in this example. · That explanation describes symbolic representation, rather than the relationship illustrated in this example. · That explanation describes informal analysis, rather than the relationship illustrated in this example. | Unexamined cases may differ, so the support is probable. |
| A pupil writes P and not P to display a conflict in a claim.
Which explanation justifies the classification? | Use of symbols to express logical relationships. | Reasoning that aims to guarantee its conclusion from its premises. · Reasoning that supports a conclusion as probable from evidence. · Assessment of reasoning expressed in ordinary language. | That explanation describes deduction, rather than the relationship illustrated in this example. · That explanation describes induction, rather than the relationship illustrated in this example. · That explanation describes informal analysis, rather than the relationship illustrated in this example. | Symbols display relationships; they do not verify facts. |
| A class checks whether a club proposal's stated reasons address the proposal.
Which explanation justifies the classification? | Assessment of reasoning expressed in ordinary language. | Reasoning that aims to guarantee its conclusion from its premises. · Reasoning that supports a conclusion as probable from evidence. · Use of symbols to express logical relationships. | That explanation describes deduction, rather than the relationship illustrated in this example. · That explanation describes induction, rather than the relationship illustrated in this example. · That explanation describes symbolic representation, rather than the relationship illustrated in this example. | Ordinary language can be assessed carefully and rigorously. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A class checks whether a club proposal's stated reasons address the proposal.
> Which explanation justifies the classification?

- ✅ Assessment of reasoning expressed in ordinary language.
- ◻️ Reasoning that supports a conclusion as probable from evidence.  
  _↳ feedback if chosen: That explanation describes induction, rather than the relationship illustrated in this example._
- ◻️ Reasoning that aims to guarantee its conclusion from its premises.  
  _↳ feedback if chosen: That explanation describes deduction, rather than the relationship illustrated in this example._
- ◻️ Use of symbols to express logical relationships.  
  _↳ feedback if chosen: That explanation describes symbolic representation, rather than the relationship illustrated in this example._

Full working after a second miss:

> Ordinary language can be assessed carefully and rigorously.  
> So the answer is “Assessment of reasoning expressed in ordinary language.”.  

> Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
> Which explanation justifies the classification?

- ◻️ Reasoning that aims to guarantee its conclusion from its premises.  
  _↳ feedback if chosen: That explanation describes deduction, rather than the relationship illustrated in this example._
- ✅ Reasoning that supports a conclusion as probable from evidence.
- ◻️ Use of symbols to express logical relationships.  
  _↳ feedback if chosen: That explanation describes symbolic representation, rather than the relationship illustrated in this example._
- ◻️ Assessment of reasoning expressed in ordinary language.  
  _↳ feedback if chosen: That explanation describes informal analysis, rather than the relationship illustrated in this example._

Full working after a second miss:

> Unexamined cases may differ, so the support is probable.  
> So the answer is “Reasoning that supports a conclusion as probable from evidence.”.  

> A class checks whether a club proposal's stated reasons address the proposal.
> Which explanation justifies the classification?

- ◻️ Use of symbols to express logical relationships.  
  _↳ feedback if chosen: That explanation describes symbolic representation, rather than the relationship illustrated in this example._
- ✅ Assessment of reasoning expressed in ordinary language.
- ◻️ Reasoning that supports a conclusion as probable from evidence.  
  _↳ feedback if chosen: That explanation describes induction, rather than the relationship illustrated in this example._
- ◻️ Reasoning that aims to guarantee its conclusion from its premises.  
  _↳ feedback if chosen: That explanation describes deduction, rather than the relationship illustrated in this example._

Full working after a second miss:

> Ordinary language can be assessed carefully and rigorously.  
> So the answer is “Assessment of reasoning expressed in ordinary language.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-link` · Lesson 4 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- deduction → **All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.**
- induction → **Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.**
- symbolic representation → **A pupil writes P and not P to display a conflict in a claim.**
- informal analysis → **A class checks whether a club proposal's stated reasons address the proposal.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do. · A class checks whether a club proposal's stated reasons address the proposal. · All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.
- deduction → **All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.**
- induction → **Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.**
- informal analysis → **A class checks whether a club proposal's stated reasons address the proposal.**

Full working after a second miss:

> The right pairs are:  
> deduction → All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.  
> induction → Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.  
> informal analysis → A class checks whether a club proposal's stated reasons address the proposal.  

> Match each term to its example.

Right-hand side (shuffled): All cards in a hypothetical box are blue; this card is from that box; therefore it is blue. · A class checks whether a club proposal's stated reasons address the proposal. · Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.
- deduction → **All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.**
- induction → **Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.**
- informal analysis → **A class checks whether a club proposal's stated reasons address the proposal.**

Full working after a second miss:

> The right pairs are:  
> deduction → All cards in a hypothetical box are blue; this card is from that box; therefore it is blue.  
> induction → Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.  
> informal analysis → A class checks whether a club proposal's stated reasons address the proposal.  

> Match each term to its example.

Right-hand side (shuffled): Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do. · A class checks whether a club proposal's stated reasons address the proposal. · A pupil writes P and not P to display a conflict in a claim.
- symbolic representation → **A pupil writes P and not P to display a conflict in a claim.**
- induction → **Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.**
- informal analysis → **A class checks whether a club proposal's stated reasons address the proposal.**

Full working after a second miss:

> The right pairs are:  
> symbolic representation → A pupil writes P and not P to display a conflict in a claim.  
> induction → Several sampled stalls sell plantains, so a learner predicts that many stalls in the market do.  
> informal analysis → A class checks whether a club proposal's stated reasons address the proposal.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-repair` · Lesson 4 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ deduction: reasoning that aims to guarantee its conclusion from its premises.
- ✅ induction: reasoning that supports a conclusion as probable from evidence.
- ✅ symbolic representation: use of symbols to express logical relationships.
- ✅ informal analysis: assessment of reasoning expressed in ordinary language.
- ❌ Deduction is defined simply as moving from many cases to a generalisation.  
  _↳ The defining aim is necessary support, not the number of cases mentioned._
- ❌ Induction guarantees the unexamined stalls.  
  _↳ Unexamined cases may differ, so the support is probable._
- ❌ A symbolic expression is true merely because it uses letters.  
  _↳ Symbols display relationships; they do not verify facts._
- ❌ Informal analysis means accepting careless reasoning.  
  _↳ Ordinary language can be assessed carefully and rigorously._


Three generated variants:

> Find the incorrect claim.

- ◻️ symbolic representation: use of symbols to express logical relationships.  
  _↳ explanation: This statement is correct: symbolic representation means use of symbols to express logical relationships. Look for a claim that conflicts with its definition._
- ✅ Deduction is defined simply as moving from many cases to a generalisation.  
  _↳ explanation: The defining aim is necessary support, not the number of cases mentioned._
- ◻️ induction: reasoning that supports a conclusion as probable from evidence.  
  _↳ explanation: This statement is correct: induction means reasoning that supports a conclusion as probable from evidence. Look for a claim that conflicts with its definition._
- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Deduction is defined simply as moving from many cases to a generalisation.”.  
> The defining aim is necessary support, not the number of cases mentioned.  

> Find the incorrect claim.

- ✅ Induction guarantees the unexamined stalls.  
  _↳ explanation: Unexamined cases may differ, so the support is probable._
- ◻️ informal analysis: assessment of reasoning expressed in ordinary language.  
  _↳ explanation: This statement is correct: informal analysis means assessment of reasoning expressed in ordinary language. Look for a claim that conflicts with its definition._
- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._
- ◻️ induction: reasoning that supports a conclusion as probable from evidence.  
  _↳ explanation: This statement is correct: induction means reasoning that supports a conclusion as probable from evidence. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Induction guarantees the unexamined stalls.”.  
> Unexamined cases may differ, so the support is probable.  

> Find the incorrect claim.

- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._
- ✅ A symbolic expression is true merely because it uses letters.  
  _↳ explanation: Symbols display relationships; they do not verify facts._
- ◻️ symbolic representation: use of symbols to express logical relationships.  
  _↳ explanation: This statement is correct: symbolic representation means use of symbols to express logical relationships. Look for a claim that conflicts with its definition._
- ◻️ induction: reasoning that supports a conclusion as probable from evidence.  
  _↳ explanation: This statement is correct: induction means reasoning that supports a conclusion as probable from evidence. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A symbolic expression is true merely because it uses letters.”.  
> Symbols display relationships; they do not verify facts.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-4-repair-card` · Lesson 4 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ deduction: reasoning that aims to guarantee its conclusion from its premises.
- ✅ induction: reasoning that supports a conclusion as probable from evidence.
- ✅ symbolic representation: use of symbols to express logical relationships.
- ✅ informal analysis: assessment of reasoning expressed in ordinary language.
- ❌ Deduction is defined simply as moving from many cases to a generalisation.  
  _↳ The defining aim is necessary support, not the number of cases mentioned._
- ❌ Induction guarantees the unexamined stalls.  
  _↳ Unexamined cases may differ, so the support is probable._
- ❌ A symbolic expression is true merely because it uses letters.  
  _↳ Symbols display relationships; they do not verify facts._
- ❌ Informal analysis means accepting careless reasoning.  
  _↳ Ordinary language can be assessed carefully and rigorously._


Three generated variants:

> Find the incorrect claim.

- ◻️ symbolic representation: use of symbols to express logical relationships.  
  _↳ explanation: This statement is correct: symbolic representation means use of symbols to express logical relationships. Look for a claim that conflicts with its definition._
- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._
- ◻️ informal analysis: assessment of reasoning expressed in ordinary language.  
  _↳ explanation: This statement is correct: informal analysis means assessment of reasoning expressed in ordinary language. Look for a claim that conflicts with its definition._
- ✅ Deduction is defined simply as moving from many cases to a generalisation.  
  _↳ explanation: The defining aim is necessary support, not the number of cases mentioned._

Full working after a second miss:

> The wrong statement is “Deduction is defined simply as moving from many cases to a generalisation.”.  
> The defining aim is necessary support, not the number of cases mentioned.  

> Find the incorrect claim.

- ◻️ informal analysis: assessment of reasoning expressed in ordinary language.  
  _↳ explanation: This statement is correct: informal analysis means assessment of reasoning expressed in ordinary language. Look for a claim that conflicts with its definition._
- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._
- ✅ Informal analysis means accepting careless reasoning.  
  _↳ explanation: Ordinary language can be assessed carefully and rigorously._
- ◻️ induction: reasoning that supports a conclusion as probable from evidence.  
  _↳ explanation: This statement is correct: induction means reasoning that supports a conclusion as probable from evidence. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Informal analysis means accepting careless reasoning.”.  
> Ordinary language can be assessed carefully and rigorously.  

> Find the incorrect claim.

- ✅ Informal analysis means accepting careless reasoning.  
  _↳ explanation: Ordinary language can be assessed carefully and rigorously._
- ◻️ induction: reasoning that supports a conclusion as probable from evidence.  
  _↳ explanation: This statement is correct: induction means reasoning that supports a conclusion as probable from evidence. Look for a claim that conflicts with its definition._
- ◻️ deduction: reasoning that aims to guarantee its conclusion from its premises.  
  _↳ explanation: This statement is correct: deduction means reasoning that aims to guarantee its conclusion from its premises. Look for a claim that conflicts with its definition._
- ◻️ informal analysis: assessment of reasoning expressed in ordinary language.  
  _↳ explanation: This statement is correct: informal analysis means assessment of reasoning expressed in ordinary language. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Informal analysis means accepting careless reasoning.”.  
> Ordinary language can be assessed carefully and rigorously.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-6-terms` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: keeping a thing or proposition identical with itself in an argument ? | identity | non-contradiction · excluded middle · qualification | non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes keeping a thing or proposition identical with itself in an argument. · excluded middle means the classical rule P or not P; the question instead describes keeping a thing or proposition identical with itself in an argument. · qualification means specifying the time and respect of a claim; the question instead describes keeping a thing or proposition identical with itself in an argument. | Keeping a thing or proposition identical with itself in an argument. |
| Which term means: excluding P and not P as both true in the same respect and time ? | non-contradiction | identity · excluded middle · qualification | identity means keeping a thing or proposition identical with itself in an argument; the question instead describes excluding P and not P as both true in the same respect and time. · excluded middle means the classical rule P or not P; the question instead describes excluding P and not P as both true in the same respect and time. · qualification means specifying the time and respect of a claim; the question instead describes excluding P and not P as both true in the same respect and time. | Excluding p and not p as both true in the same respect and time. |
| Which term means: the classical rule P or not P ? | excluded middle | identity · non-contradiction · qualification | identity means keeping a thing or proposition identical with itself in an argument; the question instead describes the classical rule P or not P. · non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes the classical rule P or not P. · qualification means specifying the time and respect of a claim; the question instead describes the classical rule P or not P. | The classical rule p or not p. |
| Which term means: specifying the time and respect of a claim ? | qualification | identity · non-contradiction · excluded middle | identity means keeping a thing or proposition identical with itself in an argument; the question instead describes specifying the time and respect of a claim. · non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes specifying the time and respect of a claim. · excluded middle means the classical rule P or not P; the question instead describes specifying the time and respect of a claim. | Specifying the time and respect of a claim. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: keeping a thing or proposition identical with itself in an argument ?

- ✅ identity
- ◻️ qualification  
  _↳ feedback if chosen: qualification means specifying the time and respect of a claim; the question instead describes keeping a thing or proposition identical with itself in an argument._
- ◻️ excluded middle  
  _↳ feedback if chosen: excluded middle means the classical rule P or not P; the question instead describes keeping a thing or proposition identical with itself in an argument._
- ◻️ non-contradiction  
  _↳ feedback if chosen: non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes keeping a thing or proposition identical with itself in an argument._

Full working after a second miss:

> Keeping a thing or proposition identical with itself in an argument.  
> So the answer is “identity”.  

> Which term means: keeping a thing or proposition identical with itself in an argument ?

- ◻️ excluded middle  
  _↳ feedback if chosen: excluded middle means the classical rule P or not P; the question instead describes keeping a thing or proposition identical with itself in an argument._
- ◻️ qualification  
  _↳ feedback if chosen: qualification means specifying the time and respect of a claim; the question instead describes keeping a thing or proposition identical with itself in an argument._
- ✅ identity
- ◻️ non-contradiction  
  _↳ feedback if chosen: non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes keeping a thing or proposition identical with itself in an argument._

Full working after a second miss:

> Keeping a thing or proposition identical with itself in an argument.  
> So the answer is “identity”.  

> Which term means: the classical rule P or not P ?

- ◻️ qualification  
  _↳ feedback if chosen: qualification means specifying the time and respect of a claim; the question instead describes the classical rule P or not P._
- ◻️ identity  
  _↳ feedback if chosen: identity means keeping a thing or proposition identical with itself in an argument; the question instead describes the classical rule P or not P._
- ◻️ non-contradiction  
  _↳ feedback if chosen: non-contradiction means excluding P and not P as both true in the same respect and time; the question instead describes the classical rule P or not P._
- ✅ excluded middle

Full working after a second miss:

> The classical rule p or not p.  
> So the answer is “excluded middle”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-6-cases` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A class uses library to mean the same reading room throughout its discussion.
Which term best fits this example? | identity | non-contradiction · excluded middle · qualification | non-contradiction concerns excluding P and not P as both true in the same respect and time. This case instead illustrates keeping a thing or proposition identical with itself in an argument. · excluded middle concerns the classical rule P or not P. This case instead illustrates keeping a thing or proposition identical with itself in an argument. · qualification concerns specifying the time and respect of a claim. This case instead illustrates keeping a thing or proposition identical with itself in an argument. | A class uses library to mean the same reading room throughout its discussion. Keeping a thing or proposition identical with itself in an argument. |
| A notice cannot truthfully say the same room is fully open and not open at the same instant.
Which term best fits this example? | non-contradiction | identity · excluded middle · qualification | identity concerns keeping a thing or proposition identical with itself in an argument. This case instead illustrates excluding P and not P as both true in the same respect and time. · excluded middle concerns the classical rule P or not P. This case instead illustrates excluding P and not P as both true in the same respect and time. · qualification concerns specifying the time and respect of a claim. This case instead illustrates excluding P and not P as both true in the same respect and time. | A notice cannot truthfully say the same room is fully open and not open at the same instant. Excluding p and not p as both true in the same respect and time. |
| Either the specified library light is on now or it is not on now.
Which term best fits this example? | excluded middle | identity · non-contradiction · qualification | identity concerns keeping a thing or proposition identical with itself in an argument. This case instead illustrates the classical rule P or not P. · non-contradiction concerns excluding P and not P as both true in the same respect and time. This case instead illustrates the classical rule P or not P. · qualification concerns specifying the time and respect of a claim. This case instead illustrates the classical rule P or not P. | Either the specified library light is on now or it is not on now. The classical rule p or not p. |
| A learner distinguishes a heavy bag from a heavy school workload before comparing claims.
Which term best fits this example? | qualification | identity · non-contradiction · excluded middle | identity concerns keeping a thing or proposition identical with itself in an argument. This case instead illustrates specifying the time and respect of a claim. · non-contradiction concerns excluding P and not P as both true in the same respect and time. This case instead illustrates specifying the time and respect of a claim. · excluded middle concerns the classical rule P or not P. This case instead illustrates specifying the time and respect of a claim. | A learner distinguishes a heavy bag from a heavy school workload before comparing claims. Specifying the time and respect of a claim. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A notice cannot truthfully say the same room is fully open and not open at the same instant.
> Which term best fits this example?

- ◻️ qualification  
  _↳ feedback if chosen: qualification concerns specifying the time and respect of a claim. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ◻️ excluded middle  
  _↳ feedback if chosen: excluded middle concerns the classical rule P or not P. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ◻️ identity  
  _↳ feedback if chosen: identity concerns keeping a thing or proposition identical with itself in an argument. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ✅ non-contradiction

Full working after a second miss:

> A notice cannot truthfully say the same room is fully open and not open at the same instant. Excluding p and not p as both true in the same respect and time.  
> So the answer is “non-contradiction”.  

> A class uses library to mean the same reading room throughout its discussion.
> Which term best fits this example?

- ◻️ excluded middle  
  _↳ feedback if chosen: excluded middle concerns the classical rule P or not P. This case instead illustrates keeping a thing or proposition identical with itself in an argument._
- ✅ identity
- ◻️ qualification  
  _↳ feedback if chosen: qualification concerns specifying the time and respect of a claim. This case instead illustrates keeping a thing or proposition identical with itself in an argument._
- ◻️ non-contradiction  
  _↳ feedback if chosen: non-contradiction concerns excluding P and not P as both true in the same respect and time. This case instead illustrates keeping a thing or proposition identical with itself in an argument._

Full working after a second miss:

> A class uses library to mean the same reading room throughout its discussion. Keeping a thing or proposition identical with itself in an argument.  
> So the answer is “identity”.  

> A notice cannot truthfully say the same room is fully open and not open at the same instant.
> Which term best fits this example?

- ◻️ qualification  
  _↳ feedback if chosen: qualification concerns specifying the time and respect of a claim. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ◻️ identity  
  _↳ feedback if chosen: identity concerns keeping a thing or proposition identical with itself in an argument. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ◻️ excluded middle  
  _↳ feedback if chosen: excluded middle concerns the classical rule P or not P. This case instead illustrates excluding P and not P as both true in the same respect and time._
- ✅ non-contradiction

Full working after a second miss:

> A notice cannot truthfully say the same room is fully open and not open at the same instant. Excluding p and not p as both true in the same respect and time.  
> So the answer is “non-contradiction”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-6-reason` · Lesson 6 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A class uses library to mean the same reading room throughout its discussion.
Which explanation justifies the classification? | Keeping a thing or proposition identical with itself in an argument. | Excluding p and not p as both true in the same respect and time. · The classical rule p or not p. · Specifying the time and respect of a claim. | That explanation describes non-contradiction, rather than the relationship illustrated in this example. · That explanation describes excluded middle, rather than the relationship illustrated in this example. · That explanation describes qualification, rather than the relationship illustrated in this example. | A valid comparison keeps the relevant meaning fixed. |
| A notice cannot truthfully say the same room is fully open and not open at the same instant.
Which explanation justifies the classification? | Excluding p and not p as both true in the same respect and time. | Keeping a thing or proposition identical with itself in an argument. · The classical rule p or not p. · Specifying the time and respect of a claim. | That explanation describes identity, rather than the relationship illustrated in this example. · That explanation describes excluded middle, rather than the relationship illustrated in this example. · That explanation describes qualification, rather than the relationship illustrated in this example. | The different times remove the conflict; fix time and respect before applying the law. |
| Either the specified library light is on now or it is not on now.
Which explanation justifies the classification? | The classical rule p or not p. | Keeping a thing or proposition identical with itself in an argument. · Excluding p and not p as both true in the same respect and time. · Specifying the time and respect of a claim. | That explanation describes identity, rather than the relationship illustrated in this example. · That explanation describes non-contradiction, rather than the relationship illustrated in this example. · That explanation describes qualification, rather than the relationship illustrated in this example. | The law concerns the alternatives, not our knowledge of which holds. |
| A learner distinguishes a heavy bag from a heavy school workload before comparing claims.
Which explanation justifies the classification? | Specifying the time and respect of a claim. | Keeping a thing or proposition identical with itself in an argument. · Excluding p and not p as both true in the same respect and time. · The classical rule p or not p. | That explanation describes identity, rather than the relationship illustrated in this example. · That explanation describes non-contradiction, rather than the relationship illustrated in this example. · That explanation describes excluded middle, rather than the relationship illustrated in this example. | Words can be used in different senses; specify the relevant sense. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A class uses library to mean the same reading room throughout its discussion.
> Which explanation justifies the classification?

- ✅ Keeping a thing or proposition identical with itself in an argument.
- ◻️ Specifying the time and respect of a claim.  
  _↳ feedback if chosen: That explanation describes qualification, rather than the relationship illustrated in this example._
- ◻️ The classical rule p or not p.  
  _↳ feedback if chosen: That explanation describes excluded middle, rather than the relationship illustrated in this example._
- ◻️ Excluding p and not p as both true in the same respect and time.  
  _↳ feedback if chosen: That explanation describes non-contradiction, rather than the relationship illustrated in this example._

Full working after a second miss:

> A valid comparison keeps the relevant meaning fixed.  
> So the answer is “Keeping a thing or proposition identical with itself in an argument.”.  

> A notice cannot truthfully say the same room is fully open and not open at the same instant.
> Which explanation justifies the classification?

- ◻️ Keeping a thing or proposition identical with itself in an argument.  
  _↳ feedback if chosen: That explanation describes identity, rather than the relationship illustrated in this example._
- ◻️ The classical rule p or not p.  
  _↳ feedback if chosen: That explanation describes excluded middle, rather than the relationship illustrated in this example._
- ✅ Excluding p and not p as both true in the same respect and time.
- ◻️ Specifying the time and respect of a claim.  
  _↳ feedback if chosen: That explanation describes qualification, rather than the relationship illustrated in this example._

Full working after a second miss:

> The different times remove the conflict; fix time and respect before applying the law.  
> So the answer is “Excluding p and not p as both true in the same respect and time.”.  

> Either the specified library light is on now or it is not on now.
> Which explanation justifies the classification?

- ◻️ Keeping a thing or proposition identical with itself in an argument.  
  _↳ feedback if chosen: That explanation describes identity, rather than the relationship illustrated in this example._
- ✅ The classical rule p or not p.
- ◻️ Excluding p and not p as both true in the same respect and time.  
  _↳ feedback if chosen: That explanation describes non-contradiction, rather than the relationship illustrated in this example._
- ◻️ Specifying the time and respect of a claim.  
  _↳ feedback if chosen: That explanation describes qualification, rather than the relationship illustrated in this example._

Full working after a second miss:

> The law concerns the alternatives, not our knowledge of which holds.  
> So the answer is “The classical rule p or not p.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-6-repair` · Lesson 6 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ identity: keeping a thing or proposition identical with itself in an argument.
- ✅ non-contradiction: excluding P and not P as both true in the same respect and time.
- ✅ excluded middle: the classical rule P or not P.
- ✅ qualification: specifying the time and respect of a claim.
- ❌ A term may change meaning unnoticed halfway through a proof.  
  _↳ A valid comparison keeps the relevant meaning fixed._
- ❌ Open in the morning and closed at night is a contradiction.  
  _↳ The different times remove the conflict; fix time and respect before applying the law._
- ❌ Not knowing whether a light is on defeats excluded middle.  
  _↳ The law concerns the alternatives, not our knowledge of which holds._
- ❌ Every use of the same word has exactly the same meaning.  
  _↳ Words can be used in different senses; specify the relevant sense._


Three generated variants:

> Find the incorrect claim.

- ◻️ identity: keeping a thing or proposition identical with itself in an argument.  
  _↳ explanation: This statement is correct: identity means keeping a thing or proposition identical with itself in an argument. Look for a claim that conflicts with its definition._
- ✅ Not knowing whether a light is on defeats excluded middle.  
  _↳ explanation: The law concerns the alternatives, not our knowledge of which holds._
- ◻️ non-contradiction: excluding P and not P as both true in the same respect and time.  
  _↳ explanation: This statement is correct: non-contradiction means excluding P and not P as both true in the same respect and time. Look for a claim that conflicts with its definition._
- ◻️ qualification: specifying the time and respect of a claim.  
  _↳ explanation: This statement is correct: qualification means specifying the time and respect of a claim. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Not knowing whether a light is on defeats excluded middle.”.  
> The law concerns the alternatives, not our knowledge of which holds.  

> Find the incorrect claim.

- ◻️ qualification: specifying the time and respect of a claim.  
  _↳ explanation: This statement is correct: qualification means specifying the time and respect of a claim. Look for a claim that conflicts with its definition._
- ◻️ excluded middle: the classical rule P or not P.  
  _↳ explanation: This statement is correct: excluded middle means the classical rule P or not P. Look for a claim that conflicts with its definition._
- ◻️ non-contradiction: excluding P and not P as both true in the same respect and time.  
  _↳ explanation: This statement is correct: non-contradiction means excluding P and not P as both true in the same respect and time. Look for a claim that conflicts with its definition._
- ✅ Every use of the same word has exactly the same meaning.  
  _↳ explanation: Words can be used in different senses; specify the relevant sense._

Full working after a second miss:

> The wrong statement is “Every use of the same word has exactly the same meaning.”.  
> Words can be used in different senses; specify the relevant sense.  

> Find the incorrect claim.

- ◻️ qualification: specifying the time and respect of a claim.  
  _↳ explanation: This statement is correct: qualification means specifying the time and respect of a claim. Look for a claim that conflicts with its definition._
- ✅ A term may change meaning unnoticed halfway through a proof.  
  _↳ explanation: A valid comparison keeps the relevant meaning fixed._
- ◻️ excluded middle: the classical rule P or not P.  
  _↳ explanation: This statement is correct: excluded middle means the classical rule P or not P. Look for a claim that conflicts with its definition._
- ◻️ non-contradiction: excluding P and not P as both true in the same respect and time.  
  _↳ explanation: This statement is correct: non-contradiction means excluding P and not P as both true in the same respect and time. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A term may change meaning unnoticed halfway through a proof.”.  
> A valid comparison keeps the relevant meaning fixed.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-6-repair-card` · Lesson 6 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ identity: keeping a thing or proposition identical with itself in an argument.
- ✅ non-contradiction: excluding P and not P as both true in the same respect and time.
- ✅ excluded middle: the classical rule P or not P.
- ✅ qualification: specifying the time and respect of a claim.
- ❌ A term may change meaning unnoticed halfway through a proof.  
  _↳ A valid comparison keeps the relevant meaning fixed._
- ❌ Open in the morning and closed at night is a contradiction.  
  _↳ The different times remove the conflict; fix time and respect before applying the law._
- ❌ Not knowing whether a light is on defeats excluded middle.  
  _↳ The law concerns the alternatives, not our knowledge of which holds._
- ❌ Every use of the same word has exactly the same meaning.  
  _↳ Words can be used in different senses; specify the relevant sense._


Three generated variants:

> Find the incorrect claim.

- ◻️ identity: keeping a thing or proposition identical with itself in an argument.  
  _↳ explanation: This statement is correct: identity means keeping a thing or proposition identical with itself in an argument. Look for a claim that conflicts with its definition._
- ◻️ non-contradiction: excluding P and not P as both true in the same respect and time.  
  _↳ explanation: This statement is correct: non-contradiction means excluding P and not P as both true in the same respect and time. Look for a claim that conflicts with its definition._
- ◻️ excluded middle: the classical rule P or not P.  
  _↳ explanation: This statement is correct: excluded middle means the classical rule P or not P. Look for a claim that conflicts with its definition._
- ✅ Not knowing whether a light is on defeats excluded middle.  
  _↳ explanation: The law concerns the alternatives, not our knowledge of which holds._

Full working after a second miss:

> The wrong statement is “Not knowing whether a light is on defeats excluded middle.”.  
> The law concerns the alternatives, not our knowledge of which holds.  

> Find the incorrect claim.

- ✅ A term may change meaning unnoticed halfway through a proof.  
  _↳ explanation: A valid comparison keeps the relevant meaning fixed._
- ◻️ non-contradiction: excluding P and not P as both true in the same respect and time.  
  _↳ explanation: This statement is correct: non-contradiction means excluding P and not P as both true in the same respect and time. Look for a claim that conflicts with its definition._
- ◻️ qualification: specifying the time and respect of a claim.  
  _↳ explanation: This statement is correct: qualification means specifying the time and respect of a claim. Look for a claim that conflicts with its definition._
- ◻️ excluded middle: the classical rule P or not P.  
  _↳ explanation: This statement is correct: excluded middle means the classical rule P or not P. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A term may change meaning unnoticed halfway through a proof.”.  
> A valid comparison keeps the relevant meaning fixed.  

> Find the incorrect claim.

- ◻️ excluded middle: the classical rule P or not P.  
  _↳ explanation: This statement is correct: excluded middle means the classical rule P or not P. Look for a claim that conflicts with its definition._
- ✅ Every use of the same word has exactly the same meaning.  
  _↳ explanation: Words can be used in different senses; specify the relevant sense._
- ◻️ identity: keeping a thing or proposition identical with itself in an argument.  
  _↳ explanation: This statement is correct: identity means keeping a thing or proposition identical with itself in an argument. Look for a claim that conflicts with its definition._
- ◻️ qualification: specifying the time and respect of a claim.  
  _↳ explanation: This statement is correct: qualification means specifying the time and respect of a claim. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Every use of the same word has exactly the same meaning.”.  
> Words can be used in different senses; specify the relevant sense.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-terms` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: switching a word's meaning within reasoning ? | equivocation | contradictory claims · exact negation · suspended judgment | contradictory claims means claims that negate one another under the same conditions; the question instead describes switching a word's meaning within reasoning. · exact negation means denial of the same proposition rather than a different claim; the question instead describes switching a word's meaning within reasoning. · suspended judgment means withholding a decision when evidence is insufficient; the question instead describes switching a word's meaning within reasoning. | Switching a word's meaning within reasoning. |
| Which term means: claims that negate one another under the same conditions ? | contradictory claims | equivocation · exact negation · suspended judgment | equivocation means switching a word's meaning within reasoning; the question instead describes claims that negate one another under the same conditions. · exact negation means denial of the same proposition rather than a different claim; the question instead describes claims that negate one another under the same conditions. · suspended judgment means withholding a decision when evidence is insufficient; the question instead describes claims that negate one another under the same conditions. | Claims that negate one another under the same conditions. |
| Which term means: denial of the same proposition rather than a different claim ? | exact negation | equivocation · contradictory claims · suspended judgment | equivocation means switching a word's meaning within reasoning; the question instead describes denial of the same proposition rather than a different claim. · contradictory claims means claims that negate one another under the same conditions; the question instead describes denial of the same proposition rather than a different claim. · suspended judgment means withholding a decision when evidence is insufficient; the question instead describes denial of the same proposition rather than a different claim. | Denial of the same proposition rather than a different claim. |
| Which term means: withholding a decision when evidence is insufficient ? | suspended judgment | equivocation · contradictory claims · exact negation | equivocation means switching a word's meaning within reasoning; the question instead describes withholding a decision when evidence is insufficient. · contradictory claims means claims that negate one another under the same conditions; the question instead describes withholding a decision when evidence is insufficient. · exact negation means denial of the same proposition rather than a different claim; the question instead describes withholding a decision when evidence is insufficient. | Withholding a decision when evidence is insufficient. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: claims that negate one another under the same conditions ?

- ◻️ equivocation  
  _↳ feedback if chosen: equivocation means switching a word's meaning within reasoning; the question instead describes claims that negate one another under the same conditions._
- ✅ contradictory claims
- ◻️ suspended judgment  
  _↳ feedback if chosen: suspended judgment means withholding a decision when evidence is insufficient; the question instead describes claims that negate one another under the same conditions._
- ◻️ exact negation  
  _↳ feedback if chosen: exact negation means denial of the same proposition rather than a different claim; the question instead describes claims that negate one another under the same conditions._

Full working after a second miss:

> Claims that negate one another under the same conditions.  
> So the answer is “contradictory claims”.  

> Which term means: denial of the same proposition rather than a different claim ?

- ◻️ equivocation  
  _↳ feedback if chosen: equivocation means switching a word's meaning within reasoning; the question instead describes denial of the same proposition rather than a different claim._
- ◻️ suspended judgment  
  _↳ feedback if chosen: suspended judgment means withholding a decision when evidence is insufficient; the question instead describes denial of the same proposition rather than a different claim._
- ◻️ contradictory claims  
  _↳ feedback if chosen: contradictory claims means claims that negate one another under the same conditions; the question instead describes denial of the same proposition rather than a different claim._
- ✅ exact negation

Full working after a second miss:

> Denial of the same proposition rather than a different claim.  
> So the answer is “exact negation”.  

> Which term means: withholding a decision when evidence is insufficient ?

- ◻️ contradictory claims  
  _↳ feedback if chosen: contradictory claims means claims that negate one another under the same conditions; the question instead describes withholding a decision when evidence is insufficient._
- ◻️ equivocation  
  _↳ feedback if chosen: equivocation means switching a word's meaning within reasoning; the question instead describes withholding a decision when evidence is insufficient._
- ✅ suspended judgment
- ◻️ exact negation  
  _↳ feedback if chosen: exact negation means denial of the same proposition rather than a different claim; the question instead describes withholding a decision when evidence is insufficient._

Full working after a second miss:

> Withholding a decision when evidence is insufficient.  
> So the answer is “suspended judgment”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-cases` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.
Which term best fits this example? | equivocation | contradictory claims · exact negation · suspended judgment | contradictory claims concerns claims that negate one another under the same conditions. This case instead illustrates switching a word's meaning within reasoning. · exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates switching a word's meaning within reasoning. · suspended judgment concerns withholding a decision when evidence is insufficient. This case instead illustrates switching a word's meaning within reasoning. | A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing. Switching a word's meaning within reasoning. |
| The same meeting is cancelled and the same meeting is not cancelled.
Which term best fits this example? | contradictory claims | equivocation · exact negation · suspended judgment | equivocation concerns switching a word's meaning within reasoning. This case instead illustrates claims that negate one another under the same conditions. · exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates claims that negate one another under the same conditions. · suspended judgment concerns withholding a decision when evidence is insufficient. This case instead illustrates claims that negate one another under the same conditions. | The same meeting is cancelled and the same meeting is not cancelled. Claims that negate one another under the same conditions. |
| The denial of the room is open now is the room is not open now.
Which term best fits this example? | exact negation | equivocation · contradictory claims · suspended judgment | equivocation concerns switching a word's meaning within reasoning. This case instead illustrates denial of the same proposition rather than a different claim. · contradictory claims concerns claims that negate one another under the same conditions. This case instead illustrates denial of the same proposition rather than a different claim. · suspended judgment concerns withholding a decision when evidence is insufficient. This case instead illustrates denial of the same proposition rather than a different claim. | The denial of the room is open now is the room is not open now. Denial of the same proposition rather than a different claim. |
| Bih has not checked the notice and says she does not yet know if the meeting is cancelled.
Which term best fits this example? | suspended judgment | equivocation · contradictory claims · exact negation | equivocation concerns switching a word's meaning within reasoning. This case instead illustrates withholding a decision when evidence is insufficient. · contradictory claims concerns claims that negate one another under the same conditions. This case instead illustrates withholding a decision when evidence is insufficient. · exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates withholding a decision when evidence is insufficient. | Bih has not checked the notice and says she does not yet know if the meeting is cancelled. Withholding a decision when evidence is insufficient. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The same meeting is cancelled and the same meeting is not cancelled.
> Which term best fits this example?

- ◻️ suspended judgment  
  _↳ feedback if chosen: suspended judgment concerns withholding a decision when evidence is insufficient. This case instead illustrates claims that negate one another under the same conditions._
- ✅ contradictory claims
- ◻️ equivocation  
  _↳ feedback if chosen: equivocation concerns switching a word's meaning within reasoning. This case instead illustrates claims that negate one another under the same conditions._
- ◻️ exact negation  
  _↳ feedback if chosen: exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates claims that negate one another under the same conditions._

Full working after a second miss:

> The same meeting is cancelled and the same meeting is not cancelled. Claims that negate one another under the same conditions.  
> So the answer is “contradictory claims”.  

> A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.
> Which term best fits this example?

- ✅ equivocation
- ◻️ contradictory claims  
  _↳ feedback if chosen: contradictory claims concerns claims that negate one another under the same conditions. This case instead illustrates switching a word's meaning within reasoning._
- ◻️ exact negation  
  _↳ feedback if chosen: exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates switching a word's meaning within reasoning._
- ◻️ suspended judgment  
  _↳ feedback if chosen: suspended judgment concerns withholding a decision when evidence is insufficient. This case instead illustrates switching a word's meaning within reasoning._

Full working after a second miss:

> A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing. Switching a word's meaning within reasoning.  
> So the answer is “equivocation”.  

> Bih has not checked the notice and says she does not yet know if the meeting is cancelled.
> Which term best fits this example?

- ✅ suspended judgment
- ◻️ exact negation  
  _↳ feedback if chosen: exact negation concerns denial of the same proposition rather than a different claim. This case instead illustrates withholding a decision when evidence is insufficient._
- ◻️ contradictory claims  
  _↳ feedback if chosen: contradictory claims concerns claims that negate one another under the same conditions. This case instead illustrates withholding a decision when evidence is insufficient._
- ◻️ equivocation  
  _↳ feedback if chosen: equivocation concerns switching a word's meaning within reasoning. This case instead illustrates withholding a decision when evidence is insufficient._

Full working after a second miss:

> Bih has not checked the notice and says she does not yet know if the meeting is cancelled. Withholding a decision when evidence is insufficient.  
> So the answer is “suspended judgment”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-reason` · Lesson 7 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.
Which explanation justifies the classification? | Switching a word's meaning within reasoning. | Claims that negate one another under the same conditions. · Denial of the same proposition rather than a different claim. · Withholding a decision when evidence is insufficient. | That explanation describes contradictory claims, rather than the relationship illustrated in this example. · That explanation describes exact negation, rather than the relationship illustrated in this example. · That explanation describes suspended judgment, rather than the relationship illustrated in this example. | One spelling can have different meanings; this switch breaks the reasoning. |
| The same meeting is cancelled and the same meeting is not cancelled.
Which explanation justifies the classification? | Claims that negate one another under the same conditions. | Switching a word's meaning within reasoning. · Denial of the same proposition rather than a different claim. · Withholding a decision when evidence is insufficient. | That explanation describes equivocation, rather than the relationship illustrated in this example. · That explanation describes exact negation, rather than the relationship illustrated in this example. · That explanation describes suspended judgment, rather than the relationship illustrated in this example. | A genuine contradiction needs the same meeting and conditions. |
| The denial of the room is open now is the room is not open now.
Which explanation justifies the classification? | Denial of the same proposition rather than a different claim. | Switching a word's meaning within reasoning. · Claims that negate one another under the same conditions. · Withholding a decision when evidence is insufficient. | That explanation describes equivocation, rather than the relationship illustrated in this example. · That explanation describes contradictory claims, rather than the relationship illustrated in this example. · That explanation describes suspended judgment, rather than the relationship illustrated in this example. | Large concerns size, not whether the room is open. |
| Bih has not checked the notice and says she does not yet know if the meeting is cancelled.
Which explanation justifies the classification? | Withholding a decision when evidence is insufficient. | Switching a word's meaning within reasoning. · Claims that negate one another under the same conditions. · Denial of the same proposition rather than a different claim. | That explanation describes equivocation, rather than the relationship illustrated in this example. · That explanation describes contradictory claims, rather than the relationship illustrated in this example. · That explanation describes exact negation, rather than the relationship illustrated in this example. | Lack of knowledge establishes neither alternative; investigate. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The denial of the room is open now is the room is not open now.
> Which explanation justifies the classification?

- ◻️ Switching a word's meaning within reasoning.  
  _↳ feedback if chosen: That explanation describes equivocation, rather than the relationship illustrated in this example._
- ◻️ Withholding a decision when evidence is insufficient.  
  _↳ feedback if chosen: That explanation describes suspended judgment, rather than the relationship illustrated in this example._
- ✅ Denial of the same proposition rather than a different claim.
- ◻️ Claims that negate one another under the same conditions.  
  _↳ feedback if chosen: That explanation describes contradictory claims, rather than the relationship illustrated in this example._

Full working after a second miss:

> Large concerns size, not whether the room is open.  
> So the answer is “Denial of the same proposition rather than a different claim.”.  

> The denial of the room is open now is the room is not open now.
> Which explanation justifies the classification?

- ◻️ Claims that negate one another under the same conditions.  
  _↳ feedback if chosen: That explanation describes contradictory claims, rather than the relationship illustrated in this example._
- ◻️ Withholding a decision when evidence is insufficient.  
  _↳ feedback if chosen: That explanation describes suspended judgment, rather than the relationship illustrated in this example._
- ◻️ Switching a word's meaning within reasoning.  
  _↳ feedback if chosen: That explanation describes equivocation, rather than the relationship illustrated in this example._
- ✅ Denial of the same proposition rather than a different claim.

Full working after a second miss:

> Large concerns size, not whether the room is open.  
> So the answer is “Denial of the same proposition rather than a different claim.”.  

> The same meeting is cancelled and the same meeting is not cancelled.
> Which explanation justifies the classification?

- ◻️ Switching a word's meaning within reasoning.  
  _↳ feedback if chosen: That explanation describes equivocation, rather than the relationship illustrated in this example._
- ✅ Claims that negate one another under the same conditions.
- ◻️ Denial of the same proposition rather than a different claim.  
  _↳ feedback if chosen: That explanation describes exact negation, rather than the relationship illustrated in this example._
- ◻️ Withholding a decision when evidence is insufficient.  
  _↳ feedback if chosen: That explanation describes suspended judgment, rather than the relationship illustrated in this example._

Full working after a second miss:

> A genuine contradiction needs the same meeting and conditions.  
> So the answer is “Claims that negate one another under the same conditions.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-link` · Lesson 7 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- equivocation → **A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.**
- contradictory claims → **The same meeting is cancelled and the same meeting is not cancelled.**
- exact negation → **The denial of the room is open now is the room is not open now.**
- suspended judgment → **Bih has not checked the notice and says she does not yet know if the meeting is cancelled.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): Bih has not checked the notice and says she does not yet know if the meeting is cancelled. · A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing. · The denial of the room is open now is the room is not open now.
- exact negation → **The denial of the room is open now is the room is not open now.**
- equivocation → **A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.**
- suspended judgment → **Bih has not checked the notice and says she does not yet know if the meeting is cancelled.**

Full working after a second miss:

> The right pairs are:  
> exact negation → The denial of the room is open now is the room is not open now.  
> equivocation → A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.  
> suspended judgment → Bih has not checked the notice and says she does not yet know if the meeting is cancelled.  

> Match each term to its example.

Right-hand side (shuffled): The same meeting is cancelled and the same meeting is not cancelled. · The denial of the room is open now is the room is not open now. · A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.
- equivocation → **A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.**
- exact negation → **The denial of the room is open now is the room is not open now.**
- contradictory claims → **The same meeting is cancelled and the same meeting is not cancelled.**

Full working after a second miss:

> The right pairs are:  
> equivocation → A learner moves from saving at a bank to sitting on a river bank as though bank meant the same thing.  
> exact negation → The denial of the room is open now is the room is not open now.  
> contradictory claims → The same meeting is cancelled and the same meeting is not cancelled.  

> Match each term to its example.

Right-hand side (shuffled): The same meeting is cancelled and the same meeting is not cancelled. · The denial of the room is open now is the room is not open now. · Bih has not checked the notice and says she does not yet know if the meeting is cancelled.
- exact negation → **The denial of the room is open now is the room is not open now.**
- contradictory claims → **The same meeting is cancelled and the same meeting is not cancelled.**
- suspended judgment → **Bih has not checked the notice and says she does not yet know if the meeting is cancelled.**

Full working after a second miss:

> The right pairs are:  
> exact negation → The denial of the room is open now is the room is not open now.  
> contradictory claims → The same meeting is cancelled and the same meeting is not cancelled.  
> suspended judgment → Bih has not checked the notice and says she does not yet know if the meeting is cancelled.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-repair` · Lesson 7 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ equivocation: switching a word's meaning within reasoning.
- ✅ contradictory claims: claims that negate one another under the same conditions.
- ✅ exact negation: denial of the same proposition rather than a different claim.
- ✅ suspended judgment: withholding a decision when evidence is insufficient.
- ❌ Repeating the same spelling guarantees the same meaning.  
  _↳ One spelling can have different meanings; this switch breaks the reasoning._
- ❌ Any disagreement about different meetings is a contradiction.  
  _↳ A genuine contradiction needs the same meeting and conditions._
- ❌ The denial of the room is open is the room is large.  
  _↳ Large concerns size, not whether the room is open._
- ❌ Uncertainty proves the meeting is not cancelled.  
  _↳ Lack of knowledge establishes neither alternative; investigate._


Three generated variants:

> Find the incorrect claim.

- ◻️ contradictory claims: claims that negate one another under the same conditions.  
  _↳ explanation: This statement is correct: contradictory claims means claims that negate one another under the same conditions. Look for a claim that conflicts with its definition._
- ◻️ suspended judgment: withholding a decision when evidence is insufficient.  
  _↳ explanation: This statement is correct: suspended judgment means withholding a decision when evidence is insufficient. Look for a claim that conflicts with its definition._
- ◻️ exact negation: denial of the same proposition rather than a different claim.  
  _↳ explanation: This statement is correct: exact negation means denial of the same proposition rather than a different claim. Look for a claim that conflicts with its definition._
- ✅ The denial of the room is open is the room is large.  
  _↳ explanation: Large concerns size, not whether the room is open._

Full working after a second miss:

> The wrong statement is “The denial of the room is open is the room is large.”.  
> Large concerns size, not whether the room is open.  

> Find the incorrect claim.

- ◻️ suspended judgment: withholding a decision when evidence is insufficient.  
  _↳ explanation: This statement is correct: suspended judgment means withholding a decision when evidence is insufficient. Look for a claim that conflicts with its definition._
- ◻️ equivocation: switching a word's meaning within reasoning.  
  _↳ explanation: This statement is correct: equivocation means switching a word's meaning within reasoning. Look for a claim that conflicts with its definition._
- ✅ Any disagreement about different meetings is a contradiction.  
  _↳ explanation: A genuine contradiction needs the same meeting and conditions._
- ◻️ exact negation: denial of the same proposition rather than a different claim.  
  _↳ explanation: This statement is correct: exact negation means denial of the same proposition rather than a different claim. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Any disagreement about different meetings is a contradiction.”.  
> A genuine contradiction needs the same meeting and conditions.  

> Find the incorrect claim.

- ◻️ contradictory claims: claims that negate one another under the same conditions.  
  _↳ explanation: This statement is correct: contradictory claims means claims that negate one another under the same conditions. Look for a claim that conflicts with its definition._
- ◻️ suspended judgment: withholding a decision when evidence is insufficient.  
  _↳ explanation: This statement is correct: suspended judgment means withholding a decision when evidence is insufficient. Look for a claim that conflicts with its definition._
- ✅ The denial of the room is open is the room is large.  
  _↳ explanation: Large concerns size, not whether the room is open._
- ◻️ equivocation: switching a word's meaning within reasoning.  
  _↳ explanation: This statement is correct: equivocation means switching a word's meaning within reasoning. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “The denial of the room is open is the room is large.”.  
> Large concerns size, not whether the room is open.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-7-repair-card` · Lesson 7 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ equivocation: switching a word's meaning within reasoning.
- ✅ contradictory claims: claims that negate one another under the same conditions.
- ✅ exact negation: denial of the same proposition rather than a different claim.
- ✅ suspended judgment: withholding a decision when evidence is insufficient.
- ❌ Repeating the same spelling guarantees the same meaning.  
  _↳ One spelling can have different meanings; this switch breaks the reasoning._
- ❌ Any disagreement about different meetings is a contradiction.  
  _↳ A genuine contradiction needs the same meeting and conditions._
- ❌ The denial of the room is open is the room is large.  
  _↳ Large concerns size, not whether the room is open._
- ❌ Uncertainty proves the meeting is not cancelled.  
  _↳ Lack of knowledge establishes neither alternative; investigate._


Three generated variants:

> Find the incorrect claim.

- ✅ Uncertainty proves the meeting is not cancelled.  
  _↳ explanation: Lack of knowledge establishes neither alternative; investigate._
- ◻️ suspended judgment: withholding a decision when evidence is insufficient.  
  _↳ explanation: This statement is correct: suspended judgment means withholding a decision when evidence is insufficient. Look for a claim that conflicts with its definition._
- ◻️ exact negation: denial of the same proposition rather than a different claim.  
  _↳ explanation: This statement is correct: exact negation means denial of the same proposition rather than a different claim. Look for a claim that conflicts with its definition._
- ◻️ equivocation: switching a word's meaning within reasoning.  
  _↳ explanation: This statement is correct: equivocation means switching a word's meaning within reasoning. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Uncertainty proves the meeting is not cancelled.”.  
> Lack of knowledge establishes neither alternative; investigate.  

> Find the incorrect claim.

- ◻️ exact negation: denial of the same proposition rather than a different claim.  
  _↳ explanation: This statement is correct: exact negation means denial of the same proposition rather than a different claim. Look for a claim that conflicts with its definition._
- ◻️ equivocation: switching a word's meaning within reasoning.  
  _↳ explanation: This statement is correct: equivocation means switching a word's meaning within reasoning. Look for a claim that conflicts with its definition._
- ✅ Uncertainty proves the meeting is not cancelled.  
  _↳ explanation: Lack of knowledge establishes neither alternative; investigate._
- ◻️ contradictory claims: claims that negate one another under the same conditions.  
  _↳ explanation: This statement is correct: contradictory claims means claims that negate one another under the same conditions. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Uncertainty proves the meeting is not cancelled.”.  
> Lack of knowledge establishes neither alternative; investigate.  

> Find the incorrect claim.

- ✅ The denial of the room is open is the room is large.  
  _↳ explanation: Large concerns size, not whether the room is open._
- ◻️ suspended judgment: withholding a decision when evidence is insufficient.  
  _↳ explanation: This statement is correct: suspended judgment means withholding a decision when evidence is insufficient. Look for a claim that conflicts with its definition._
- ◻️ exact negation: denial of the same proposition rather than a different claim.  
  _↳ explanation: This statement is correct: exact negation means denial of the same proposition rather than a different claim. Look for a claim that conflicts with its definition._
- ◻️ contradictory claims: claims that negate one another under the same conditions.  
  _↳ explanation: This statement is correct: contradictory claims means claims that negate one another under the same conditions. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “The denial of the room is open is the room is large.”.  
> Large concerns size, not whether the room is open.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-terms` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: grasping a concept without affirming or denying ? | simple apprehension | judgment · reasoning · term | judgment means affirming or denying a relation; the question instead describes grasping a concept without affirming or denying. · reasoning means drawing a supported judgment from other judgments; the question instead describes grasping a concept without affirming or denying. · term means a linguistic expression of a concept; the question instead describes grasping a concept without affirming or denying. | Grasping a concept without affirming or denying. |
| Which term means: affirming or denying a relation ? | judgment | simple apprehension · reasoning · term | simple apprehension means grasping a concept without affirming or denying; the question instead describes affirming or denying a relation. · reasoning means drawing a supported judgment from other judgments; the question instead describes affirming or denying a relation. · term means a linguistic expression of a concept; the question instead describes affirming or denying a relation. | Affirming or denying a relation. |
| Which term means: drawing a supported judgment from other judgments ? | reasoning | simple apprehension · judgment · term | simple apprehension means grasping a concept without affirming or denying; the question instead describes drawing a supported judgment from other judgments. · judgment means affirming or denying a relation; the question instead describes drawing a supported judgment from other judgments. · term means a linguistic expression of a concept; the question instead describes drawing a supported judgment from other judgments. | Drawing a supported judgment from other judgments. |
| Which term means: a linguistic expression of a concept ? | term | simple apprehension · judgment · reasoning | simple apprehension means grasping a concept without affirming or denying; the question instead describes a linguistic expression of a concept. · judgment means affirming or denying a relation; the question instead describes a linguistic expression of a concept. · reasoning means drawing a supported judgment from other judgments; the question instead describes a linguistic expression of a concept. | A linguistic expression of a concept. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: drawing a supported judgment from other judgments ?

- ◻️ simple apprehension  
  _↳ feedback if chosen: simple apprehension means grasping a concept without affirming or denying; the question instead describes drawing a supported judgment from other judgments._
- ◻️ term  
  _↳ feedback if chosen: term means a linguistic expression of a concept; the question instead describes drawing a supported judgment from other judgments._
- ✅ reasoning
- ◻️ judgment  
  _↳ feedback if chosen: judgment means affirming or denying a relation; the question instead describes drawing a supported judgment from other judgments._

Full working after a second miss:

> Drawing a supported judgment from other judgments.  
> So the answer is “reasoning”.  

> Which term means: drawing a supported judgment from other judgments ?

- ✅ reasoning
- ◻️ judgment  
  _↳ feedback if chosen: judgment means affirming or denying a relation; the question instead describes drawing a supported judgment from other judgments._
- ◻️ simple apprehension  
  _↳ feedback if chosen: simple apprehension means grasping a concept without affirming or denying; the question instead describes drawing a supported judgment from other judgments._
- ◻️ term  
  _↳ feedback if chosen: term means a linguistic expression of a concept; the question instead describes drawing a supported judgment from other judgments._

Full working after a second miss:

> Drawing a supported judgment from other judgments.  
> So the answer is “reasoning”.  

> Which term means: grasping a concept without affirming or denying ?

- ◻️ reasoning  
  _↳ feedback if chosen: reasoning means drawing a supported judgment from other judgments; the question instead describes grasping a concept without affirming or denying._
- ◻️ term  
  _↳ feedback if chosen: term means a linguistic expression of a concept; the question instead describes grasping a concept without affirming or denying._
- ✅ simple apprehension
- ◻️ judgment  
  _↳ feedback if chosen: judgment means affirming or denying a relation; the question instead describes grasping a concept without affirming or denying._

Full working after a second miss:

> Grasping a concept without affirming or denying.  
> So the answer is “simple apprehension”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-cases` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner thinks of a library without claiming that it is open.
Which term best fits this example? | simple apprehension | judgment · reasoning · term | judgment concerns affirming or denying a relation. This case instead illustrates grasping a concept without affirming or denying. · reasoning concerns drawing a supported judgment from other judgments. This case instead illustrates grasping a concept without affirming or denying. · term concerns a linguistic expression of a concept. This case instead illustrates grasping a concept without affirming or denying. | A learner thinks of a library without claiming that it is open. Grasping a concept without affirming or denying. |
| A learner asserts that the library is open today.
Which term best fits this example? | judgment | simple apprehension · reasoning · term | simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates affirming or denying a relation. · reasoning concerns drawing a supported judgment from other judgments. This case instead illustrates affirming or denying a relation. · term concerns a linguistic expression of a concept. This case instead illustrates affirming or denying a relation. | A learner asserts that the library is open today. Affirming or denying a relation. |
| The rules allow entry when the library opens; it is open; so entry is allowed.
Which term best fits this example? | reasoning | simple apprehension · judgment · term | simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates drawing a supported judgment from other judgments. · judgment concerns affirming or denying a relation. This case instead illustrates drawing a supported judgment from other judgments. · term concerns a linguistic expression of a concept. This case instead illustrates drawing a supported judgment from other judgments. | The rules allow entry when the library opens; it is open; so entry is allowed. Drawing a supported judgment from other judgments. |
| The word library expresses an idea in a discussion.
Which term best fits this example? | term | simple apprehension · judgment · reasoning | simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates a linguistic expression of a concept. · judgment concerns affirming or denying a relation. This case instead illustrates a linguistic expression of a concept. · reasoning concerns drawing a supported judgment from other judgments. This case instead illustrates a linguistic expression of a concept. | The word library expresses an idea in a discussion. A linguistic expression of a concept. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The rules allow entry when the library opens; it is open; so entry is allowed.
> Which term best fits this example?

- ◻️ simple apprehension  
  _↳ feedback if chosen: simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ judgment  
  _↳ feedback if chosen: judgment concerns affirming or denying a relation. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ term  
  _↳ feedback if chosen: term concerns a linguistic expression of a concept. This case instead illustrates drawing a supported judgment from other judgments._
- ✅ reasoning

Full working after a second miss:

> The rules allow entry when the library opens; it is open; so entry is allowed. Drawing a supported judgment from other judgments.  
> So the answer is “reasoning”.  

> The rules allow entry when the library opens; it is open; so entry is allowed.
> Which term best fits this example?

- ◻️ judgment  
  _↳ feedback if chosen: judgment concerns affirming or denying a relation. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ term  
  _↳ feedback if chosen: term concerns a linguistic expression of a concept. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ simple apprehension  
  _↳ feedback if chosen: simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates drawing a supported judgment from other judgments._
- ✅ reasoning

Full working after a second miss:

> The rules allow entry when the library opens; it is open; so entry is allowed. Drawing a supported judgment from other judgments.  
> So the answer is “reasoning”.  

> The rules allow entry when the library opens; it is open; so entry is allowed.
> Which term best fits this example?

- ✅ reasoning
- ◻️ simple apprehension  
  _↳ feedback if chosen: simple apprehension concerns grasping a concept without affirming or denying. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ judgment  
  _↳ feedback if chosen: judgment concerns affirming or denying a relation. This case instead illustrates drawing a supported judgment from other judgments._
- ◻️ term  
  _↳ feedback if chosen: term concerns a linguistic expression of a concept. This case instead illustrates drawing a supported judgment from other judgments._

Full working after a second miss:

> The rules allow entry when the library opens; it is open; so entry is allowed. Drawing a supported judgment from other judgments.  
> So the answer is “reasoning”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-reason` · Lesson 8 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner thinks of a library without claiming that it is open.
Which explanation justifies the classification? | Grasping a concept without affirming or denying. | Affirming or denying a relation. · Drawing a supported judgment from other judgments. · A linguistic expression of a concept. | That explanation describes judgment, rather than the relationship illustrated in this example. · That explanation describes reasoning, rather than the relationship illustrated in this example. · That explanation describes term, rather than the relationship illustrated in this example. | The concept alone makes no affirmation about opening. |
| A learner asserts that the library is open today.
Which explanation justifies the classification? | Affirming or denying a relation. | Grasping a concept without affirming or denying. · Drawing a supported judgment from other judgments. · A linguistic expression of a concept. | That explanation describes simple apprehension, rather than the relationship illustrated in this example. · That explanation describes reasoning, rather than the relationship illustrated in this example. · That explanation describes term, rather than the relationship illustrated in this example. | A judgment can be asserted without giving its reasons. |
| The rules allow entry when the library opens; it is open; so entry is allowed.
Which explanation justifies the classification? | Drawing a supported judgment from other judgments. | Grasping a concept without affirming or denying. · Affirming or denying a relation. · A linguistic expression of a concept. | That explanation describes simple apprehension, rather than the relationship illustrated in this example. · That explanation describes judgment, rather than the relationship illustrated in this example. · That explanation describes term, rather than the relationship illustrated in this example. | Reasoning requires a movement from supporting claims to a conclusion. |
| The word library expresses an idea in a discussion.
Which explanation justifies the classification? | A linguistic expression of a concept. | Grasping a concept without affirming or denying. · Affirming or denying a relation. · Drawing a supported judgment from other judgments. | That explanation describes simple apprehension, rather than the relationship illustrated in this example. · That explanation describes judgment, rather than the relationship illustrated in this example. · That explanation describes reasoning, rather than the relationship illustrated in this example. | Truth and falsity apply to assertions, not an isolated term in this use. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The rules allow entry when the library opens; it is open; so entry is allowed.
> Which explanation justifies the classification?

- ◻️ Affirming or denying a relation.  
  _↳ feedback if chosen: That explanation describes judgment, rather than the relationship illustrated in this example._
- ◻️ A linguistic expression of a concept.  
  _↳ feedback if chosen: That explanation describes term, rather than the relationship illustrated in this example._
- ◻️ Grasping a concept without affirming or denying.  
  _↳ feedback if chosen: That explanation describes simple apprehension, rather than the relationship illustrated in this example._
- ✅ Drawing a supported judgment from other judgments.

Full working after a second miss:

> Reasoning requires a movement from supporting claims to a conclusion.  
> So the answer is “Drawing a supported judgment from other judgments.”.  

> A learner thinks of a library without claiming that it is open.
> Which explanation justifies the classification?

- ◻️ Affirming or denying a relation.  
  _↳ feedback if chosen: That explanation describes judgment, rather than the relationship illustrated in this example._
- ◻️ Drawing a supported judgment from other judgments.  
  _↳ feedback if chosen: That explanation describes reasoning, rather than the relationship illustrated in this example._
- ◻️ A linguistic expression of a concept.  
  _↳ feedback if chosen: That explanation describes term, rather than the relationship illustrated in this example._
- ✅ Grasping a concept without affirming or denying.

Full working after a second miss:

> The concept alone makes no affirmation about opening.  
> So the answer is “Grasping a concept without affirming or denying.”.  

> The word library expresses an idea in a discussion.
> Which explanation justifies the classification?

- ◻️ Grasping a concept without affirming or denying.  
  _↳ feedback if chosen: That explanation describes simple apprehension, rather than the relationship illustrated in this example._
- ✅ A linguistic expression of a concept.
- ◻️ Drawing a supported judgment from other judgments.  
  _↳ feedback if chosen: That explanation describes reasoning, rather than the relationship illustrated in this example._
- ◻️ Affirming or denying a relation.  
  _↳ feedback if chosen: That explanation describes judgment, rather than the relationship illustrated in this example._

Full working after a second miss:

> Truth and falsity apply to assertions, not an isolated term in this use.  
> So the answer is “A linguistic expression of a concept.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-link` · Lesson 8 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- simple apprehension → **A learner thinks of a library without claiming that it is open.**
- judgment → **A learner asserts that the library is open today.**
- reasoning → **The rules allow entry when the library opens; it is open; so entry is allowed.**
- term → **The word library expresses an idea in a discussion.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): A learner asserts that the library is open today. · The rules allow entry when the library opens; it is open; so entry is allowed. · The word library expresses an idea in a discussion.
- judgment → **A learner asserts that the library is open today.**
- term → **The word library expresses an idea in a discussion.**
- reasoning → **The rules allow entry when the library opens; it is open; so entry is allowed.**

Full working after a second miss:

> The right pairs are:  
> judgment → A learner asserts that the library is open today.  
> term → The word library expresses an idea in a discussion.  
> reasoning → The rules allow entry when the library opens; it is open; so entry is allowed.  

> Match each term to its example.

Right-hand side (shuffled): A learner thinks of a library without claiming that it is open. · The word library expresses an idea in a discussion. · The rules allow entry when the library opens; it is open; so entry is allowed.
- reasoning → **The rules allow entry when the library opens; it is open; so entry is allowed.**
- term → **The word library expresses an idea in a discussion.**
- simple apprehension → **A learner thinks of a library without claiming that it is open.**

Full working after a second miss:

> The right pairs are:  
> reasoning → The rules allow entry when the library opens; it is open; so entry is allowed.  
> term → The word library expresses an idea in a discussion.  
> simple apprehension → A learner thinks of a library without claiming that it is open.  

> Match each term to its example.

Right-hand side (shuffled): A learner thinks of a library without claiming that it is open. · The word library expresses an idea in a discussion. · A learner asserts that the library is open today.
- judgment → **A learner asserts that the library is open today.**
- simple apprehension → **A learner thinks of a library without claiming that it is open.**
- term → **The word library expresses an idea in a discussion.**

Full working after a second miss:

> The right pairs are:  
> judgment → A learner asserts that the library is open today.  
> simple apprehension → A learner thinks of a library without claiming that it is open.  
> term → The word library expresses an idea in a discussion.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-repair` · Lesson 8 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ simple apprehension: grasping a concept without affirming or denying.
- ✅ judgment: affirming or denying a relation.
- ✅ reasoning: drawing a supported judgment from other judgments.
- ✅ term: a linguistic expression of a concept.
- ❌ Merely thinking library asserts that every library is open.  
  _↳ The concept alone makes no affirmation about opening._
- ❌ Every judgment already includes a supporting argument.  
  _↳ A judgment can be asserted without giving its reasons._
- ❌ A single unsupported assertion is automatically an inference.  
  _↳ Reasoning requires a movement from supporting claims to a conclusion._
- ❌ An isolated term must be true or false.  
  _↳ Truth and falsity apply to assertions, not an isolated term in this use._


Three generated variants:

> Find the incorrect claim.

- ◻️ judgment: affirming or denying a relation.  
  _↳ explanation: This statement is correct: judgment means affirming or denying a relation. Look for a claim that conflicts with its definition._
- ◻️ term: a linguistic expression of a concept.  
  _↳ explanation: This statement is correct: term means a linguistic expression of a concept. Look for a claim that conflicts with its definition._
- ◻️ reasoning: drawing a supported judgment from other judgments.  
  _↳ explanation: This statement is correct: reasoning means drawing a supported judgment from other judgments. Look for a claim that conflicts with its definition._
- ✅ A single unsupported assertion is automatically an inference.  
  _↳ explanation: Reasoning requires a movement from supporting claims to a conclusion._

Full working after a second miss:

> The wrong statement is “A single unsupported assertion is automatically an inference.”.  
> Reasoning requires a movement from supporting claims to a conclusion.  

> Find the incorrect claim.

- ◻️ term: a linguistic expression of a concept.  
  _↳ explanation: This statement is correct: term means a linguistic expression of a concept. Look for a claim that conflicts with its definition._
- ✅ Every judgment already includes a supporting argument.  
  _↳ explanation: A judgment can be asserted without giving its reasons._
- ◻️ judgment: affirming or denying a relation.  
  _↳ explanation: This statement is correct: judgment means affirming or denying a relation. Look for a claim that conflicts with its definition._
- ◻️ reasoning: drawing a supported judgment from other judgments.  
  _↳ explanation: This statement is correct: reasoning means drawing a supported judgment from other judgments. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Every judgment already includes a supporting argument.”.  
> A judgment can be asserted without giving its reasons.  

> Find the incorrect claim.

- ✅ A single unsupported assertion is automatically an inference.  
  _↳ explanation: Reasoning requires a movement from supporting claims to a conclusion._
- ◻️ term: a linguistic expression of a concept.  
  _↳ explanation: This statement is correct: term means a linguistic expression of a concept. Look for a claim that conflicts with its definition._
- ◻️ reasoning: drawing a supported judgment from other judgments.  
  _↳ explanation: This statement is correct: reasoning means drawing a supported judgment from other judgments. Look for a claim that conflicts with its definition._
- ◻️ judgment: affirming or denying a relation.  
  _↳ explanation: This statement is correct: judgment means affirming or denying a relation. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A single unsupported assertion is automatically an inference.”.  
> Reasoning requires a movement from supporting claims to a conclusion.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-8-repair-card` · Lesson 8 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ simple apprehension: grasping a concept without affirming or denying.
- ✅ judgment: affirming or denying a relation.
- ✅ reasoning: drawing a supported judgment from other judgments.
- ✅ term: a linguistic expression of a concept.
- ❌ Merely thinking library asserts that every library is open.  
  _↳ The concept alone makes no affirmation about opening._
- ❌ Every judgment already includes a supporting argument.  
  _↳ A judgment can be asserted without giving its reasons._
- ❌ A single unsupported assertion is automatically an inference.  
  _↳ Reasoning requires a movement from supporting claims to a conclusion._
- ❌ An isolated term must be true or false.  
  _↳ Truth and falsity apply to assertions, not an isolated term in this use._


Three generated variants:

> Find the incorrect claim.

- ✅ Every judgment already includes a supporting argument.  
  _↳ explanation: A judgment can be asserted without giving its reasons._
- ◻️ simple apprehension: grasping a concept without affirming or denying.  
  _↳ explanation: This statement is correct: simple apprehension means grasping a concept without affirming or denying. Look for a claim that conflicts with its definition._
- ◻️ term: a linguistic expression of a concept.  
  _↳ explanation: This statement is correct: term means a linguistic expression of a concept. Look for a claim that conflicts with its definition._
- ◻️ reasoning: drawing a supported judgment from other judgments.  
  _↳ explanation: This statement is correct: reasoning means drawing a supported judgment from other judgments. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Every judgment already includes a supporting argument.”.  
> A judgment can be asserted without giving its reasons.  

> Find the incorrect claim.

- ◻️ term: a linguistic expression of a concept.  
  _↳ explanation: This statement is correct: term means a linguistic expression of a concept. Look for a claim that conflicts with its definition._
- ✅ Every judgment already includes a supporting argument.  
  _↳ explanation: A judgment can be asserted without giving its reasons._
- ◻️ judgment: affirming or denying a relation.  
  _↳ explanation: This statement is correct: judgment means affirming or denying a relation. Look for a claim that conflicts with its definition._
- ◻️ simple apprehension: grasping a concept without affirming or denying.  
  _↳ explanation: This statement is correct: simple apprehension means grasping a concept without affirming or denying. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Every judgment already includes a supporting argument.”.  
> A judgment can be asserted without giving its reasons.  

> Find the incorrect claim.

- ◻️ reasoning: drawing a supported judgment from other judgments.  
  _↳ explanation: This statement is correct: reasoning means drawing a supported judgment from other judgments. Look for a claim that conflicts with its definition._
- ✅ Merely thinking library asserts that every library is open.  
  _↳ explanation: The concept alone makes no affirmation about opening._
- ◻️ judgment: affirming or denying a relation.  
  _↳ explanation: This statement is correct: judgment means affirming or denying a relation. Look for a claim that conflicts with its definition._
- ◻️ simple apprehension: grasping a concept without affirming or denying.  
  _↳ explanation: This statement is correct: simple apprehension means grasping a concept without affirming or denying. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “Merely thinking library asserts that every library is open.”.  
> The concept alone makes no affirmation about opening.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-terms` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which term means: an idea grasped by the mind ? | concept | term · intension · extension | term means a word or group of words expressing a concept; the question instead describes an idea grasped by the mind. · intension means the attributes included in a concept; the question instead describes an idea grasped by the mind. · extension means the things to which a concept applies; the question instead describes an idea grasped by the mind. | An idea grasped by the mind. |
| Which term means: a word or group of words expressing a concept ? | term | concept · intension · extension | concept means an idea grasped by the mind; the question instead describes a word or group of words expressing a concept. · intension means the attributes included in a concept; the question instead describes a word or group of words expressing a concept. · extension means the things to which a concept applies; the question instead describes a word or group of words expressing a concept. | A word or group of words expressing a concept. |
| Which term means: the attributes included in a concept ? | intension | concept · term · extension | concept means an idea grasped by the mind; the question instead describes the attributes included in a concept. · term means a word or group of words expressing a concept; the question instead describes the attributes included in a concept. · extension means the things to which a concept applies; the question instead describes the attributes included in a concept. | The attributes included in a concept. |
| Which term means: the things to which a concept applies ? | extension | concept · term · intension | concept means an idea grasped by the mind; the question instead describes the things to which a concept applies. · term means a word or group of words expressing a concept; the question instead describes the things to which a concept applies. · intension means the attributes included in a concept; the question instead describes the things to which a concept applies. | The things to which a concept applies. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which term means: an idea grasped by the mind ?

- ◻️ extension  
  _↳ feedback if chosen: extension means the things to which a concept applies; the question instead describes an idea grasped by the mind._
- ✅ concept
- ◻️ intension  
  _↳ feedback if chosen: intension means the attributes included in a concept; the question instead describes an idea grasped by the mind._
- ◻️ term  
  _↳ feedback if chosen: term means a word or group of words expressing a concept; the question instead describes an idea grasped by the mind._

Full working after a second miss:

> An idea grasped by the mind.  
> So the answer is “concept”.  

> Which term means: an idea grasped by the mind ?

- ◻️ term  
  _↳ feedback if chosen: term means a word or group of words expressing a concept; the question instead describes an idea grasped by the mind._
- ◻️ intension  
  _↳ feedback if chosen: intension means the attributes included in a concept; the question instead describes an idea grasped by the mind._
- ◻️ extension  
  _↳ feedback if chosen: extension means the things to which a concept applies; the question instead describes an idea grasped by the mind._
- ✅ concept

Full working after a second miss:

> An idea grasped by the mind.  
> So the answer is “concept”.  

> Which term means: the attributes included in a concept ?

- ◻️ extension  
  _↳ feedback if chosen: extension means the things to which a concept applies; the question instead describes the attributes included in a concept._
- ✅ intension
- ◻️ term  
  _↳ feedback if chosen: term means a word or group of words expressing a concept; the question instead describes the attributes included in a concept._
- ◻️ concept  
  _↳ feedback if chosen: concept means an idea grasped by the mind; the question instead describes the attributes included in a concept._

Full working after a second miss:

> The attributes included in a concept.  
> So the answer is “intension”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-cases` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner understands what a library is before choosing a word for it.
Which term best fits this example? | concept | term · intension · extension | term concerns a word or group of words expressing a concept. This case instead illustrates an idea grasped by the mind. · intension concerns the attributes included in a concept. This case instead illustrates an idea grasped by the mind. · extension concerns the things to which a concept applies. This case instead illustrates an idea grasped by the mind. | A learner understands what a library is before choosing a word for it. An idea grasped by the mind. |
| School library functions as one expression in a classification.
Which term best fits this example? | term | concept · intension · extension | concept concerns an idea grasped by the mind. This case instead illustrates a word or group of words expressing a concept. · intension concerns the attributes included in a concept. This case instead illustrates a word or group of words expressing a concept. · extension concerns the things to which a concept applies. This case instead illustrates a word or group of words expressing a concept. | School library functions as one expression in a classification. A word or group of words expressing a concept. |
| A school library adds belonging to a school to the general idea of a library.
Which term best fits this example? | intension | concept · term · extension | concept concerns an idea grasped by the mind. This case instead illustrates the attributes included in a concept. · term concerns a word or group of words expressing a concept. This case instead illustrates the attributes included in a concept. · extension concerns the things to which a concept applies. This case instead illustrates the attributes included in a concept. | A school library adds belonging to a school to the general idea of a library. The attributes included in a concept. |
| A learner lists actual examples that qualify as school libraries.
Which term best fits this example? | extension | concept · term · intension | concept concerns an idea grasped by the mind. This case instead illustrates the things to which a concept applies. · term concerns a word or group of words expressing a concept. This case instead illustrates the things to which a concept applies. · intension concerns the attributes included in a concept. This case instead illustrates the things to which a concept applies. | A learner lists actual examples that qualify as school libraries. The things to which a concept applies. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A learner understands what a library is before choosing a word for it.
> Which term best fits this example?

- ◻️ intension  
  _↳ feedback if chosen: intension concerns the attributes included in a concept. This case instead illustrates an idea grasped by the mind._
- ◻️ extension  
  _↳ feedback if chosen: extension concerns the things to which a concept applies. This case instead illustrates an idea grasped by the mind._
- ◻️ term  
  _↳ feedback if chosen: term concerns a word or group of words expressing a concept. This case instead illustrates an idea grasped by the mind._
- ✅ concept

Full working after a second miss:

> A learner understands what a library is before choosing a word for it. An idea grasped by the mind.  
> So the answer is “concept”.  

> A learner understands what a library is before choosing a word for it.
> Which term best fits this example?

- ✅ concept
- ◻️ extension  
  _↳ feedback if chosen: extension concerns the things to which a concept applies. This case instead illustrates an idea grasped by the mind._
- ◻️ term  
  _↳ feedback if chosen: term concerns a word or group of words expressing a concept. This case instead illustrates an idea grasped by the mind._
- ◻️ intension  
  _↳ feedback if chosen: intension concerns the attributes included in a concept. This case instead illustrates an idea grasped by the mind._

Full working after a second miss:

> A learner understands what a library is before choosing a word for it. An idea grasped by the mind.  
> So the answer is “concept”.  

> A learner understands what a library is before choosing a word for it.
> Which term best fits this example?

- ◻️ extension  
  _↳ feedback if chosen: extension concerns the things to which a concept applies. This case instead illustrates an idea grasped by the mind._
- ✅ concept
- ◻️ term  
  _↳ feedback if chosen: term concerns a word or group of words expressing a concept. This case instead illustrates an idea grasped by the mind._
- ◻️ intension  
  _↳ feedback if chosen: intension concerns the attributes included in a concept. This case instead illustrates an idea grasped by the mind._

Full working after a second miss:

> A learner understands what a library is before choosing a word for it. An idea grasped by the mind.  
> So the answer is “concept”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-reason` · Lesson 9 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A learner understands what a library is before choosing a word for it.
Which explanation justifies the classification? | An idea grasped by the mind. | A word or group of words expressing a concept. · The attributes included in a concept. · The things to which a concept applies. | That explanation describes term, rather than the relationship illustrated in this example. · That explanation describes intension, rather than the relationship illustrated in this example. · That explanation describes extension, rather than the relationship illustrated in this example. | The idea is its meaning, not the physical ink or sound. |
| School library functions as one expression in a classification.
Which explanation justifies the classification? | A word or group of words expressing a concept. | An idea grasped by the mind. · The attributes included in a concept. · The things to which a concept applies. | That explanation describes concept, rather than the relationship illustrated in this example. · That explanation describes intension, rather than the relationship illustrated in this example. · That explanation describes extension, rather than the relationship illustrated in this example. | Several words can express one concept and function as a term. |
| A school library adds belonging to a school to the general idea of a library.
Which explanation justifies the classification? | The attributes included in a concept. | An idea grasped by the mind. · A word or group of words expressing a concept. · The things to which a concept applies. | That explanation describes concept, rather than the relationship illustrated in this example. · That explanation describes term, rather than the relationship illustrated in this example. · That explanation describes extension, rather than the relationship illustrated in this example. | Intension concerns attributes, not spelling length. |
| A learner lists actual examples that qualify as school libraries.
Which explanation justifies the classification? | The things to which a concept applies. | An idea grasped by the mind. · A word or group of words expressing a concept. · The attributes included in a concept. | That explanation describes concept, rather than the relationship illustrated in this example. · That explanation describes term, rather than the relationship illustrated in this example. · That explanation describes intension, rather than the relationship illustrated in this example. | Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> School library functions as one expression in a classification.
> Which explanation justifies the classification?

- ◻️ An idea grasped by the mind.  
  _↳ feedback if chosen: That explanation describes concept, rather than the relationship illustrated in this example._
- ◻️ The attributes included in a concept.  
  _↳ feedback if chosen: That explanation describes intension, rather than the relationship illustrated in this example._
- ✅ A word or group of words expressing a concept.
- ◻️ The things to which a concept applies.  
  _↳ feedback if chosen: That explanation describes extension, rather than the relationship illustrated in this example._

Full working after a second miss:

> Several words can express one concept and function as a term.  
> So the answer is “A word or group of words expressing a concept.”.  

> A learner lists actual examples that qualify as school libraries.
> Which explanation justifies the classification?

- ◻️ A word or group of words expressing a concept.  
  _↳ feedback if chosen: That explanation describes term, rather than the relationship illustrated in this example._
- ◻️ An idea grasped by the mind.  
  _↳ feedback if chosen: That explanation describes concept, rather than the relationship illustrated in this example._
- ✅ The things to which a concept applies.
- ◻️ The attributes included in a concept.  
  _↳ feedback if chosen: That explanation describes intension, rather than the relationship illustrated in this example._

Full working after a second miss:

> Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison.  
> So the answer is “The things to which a concept applies.”.  

> A learner lists actual examples that qualify as school libraries.
> Which explanation justifies the classification?

- ✅ The things to which a concept applies.
- ◻️ A word or group of words expressing a concept.  
  _↳ feedback if chosen: That explanation describes term, rather than the relationship illustrated in this example._
- ◻️ The attributes included in a concept.  
  _↳ feedback if chosen: That explanation describes intension, rather than the relationship illustrated in this example._
- ◻️ An idea grasped by the mind.  
  _↳ feedback if chosen: That explanation describes concept, rather than the relationship illustrated in this example._

Full working after a second miss:

> Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison.  
> So the answer is “The things to which a concept applies.”.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-link` · Lesson 9 · matching, level 2

Prompt: Match each term to its example.

Pairs (3 shown each time):

- concept → **A learner understands what a library is before choosing a word for it.**
- term → **School library functions as one expression in a classification.**
- intension → **A school library adds belonging to a school to the general idea of a library.**
- extension → **A learner lists actual examples that qualify as school libraries.**


Three generated variants:

> Match each term to its example.

Right-hand side (shuffled): School library functions as one expression in a classification. · A learner lists actual examples that qualify as school libraries. · A school library adds belonging to a school to the general idea of a library.
- intension → **A school library adds belonging to a school to the general idea of a library.**
- extension → **A learner lists actual examples that qualify as school libraries.**
- term → **School library functions as one expression in a classification.**

Full working after a second miss:

> The right pairs are:  
> intension → A school library adds belonging to a school to the general idea of a library.  
> extension → A learner lists actual examples that qualify as school libraries.  
> term → School library functions as one expression in a classification.  

> Match each term to its example.

Right-hand side (shuffled): A school library adds belonging to a school to the general idea of a library. · School library functions as one expression in a classification. · A learner lists actual examples that qualify as school libraries.
- extension → **A learner lists actual examples that qualify as school libraries.**
- intension → **A school library adds belonging to a school to the general idea of a library.**
- term → **School library functions as one expression in a classification.**

Full working after a second miss:

> The right pairs are:  
> extension → A learner lists actual examples that qualify as school libraries.  
> intension → A school library adds belonging to a school to the general idea of a library.  
> term → School library functions as one expression in a classification.  

> Match each term to its example.

Right-hand side (shuffled): A learner lists actual examples that qualify as school libraries. · A learner understands what a library is before choosing a word for it. · School library functions as one expression in a classification.
- extension → **A learner lists actual examples that qualify as school libraries.**
- term → **School library functions as one expression in a classification.**
- concept → **A learner understands what a library is before choosing a word for it.**

Full working after a second miss:

> The right pairs are:  
> extension → A learner lists actual examples that qualify as school libraries.  
> term → School library functions as one expression in a classification.  
> concept → A learner understands what a library is before choosing a word for it.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-repair` · Lesson 9 · spot the error, level 3

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ concept: an idea grasped by the mind.
- ✅ term: a word or group of words expressing a concept.
- ✅ intension: the attributes included in a concept.
- ✅ extension: the things to which a concept applies.
- ❌ An idea and the ink used to write a word are identical objects.  
  _↳ The idea is its meaning, not the physical ink or sound._
- ❌ A term must contain only a single word.  
  _↳ Several words can express one concept and function as a term._
- ❌ Intension is the number of letters in the term.  
  _↳ Intension concerns attributes, not spelling length._
- ❌ A narrower concept always applies to more things than its broader parent.  
  _↳ Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison._


Three generated variants:

> Find the incorrect claim.

- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._
- ✅ A narrower concept always applies to more things than its broader parent.  
  _↳ explanation: Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison._
- ◻️ extension: the things to which a concept applies.  
  _↳ explanation: This statement is correct: extension means the things to which a concept applies. Look for a claim that conflicts with its definition._
- ◻️ concept: an idea grasped by the mind.  
  _↳ explanation: This statement is correct: concept means an idea grasped by the mind. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A narrower concept always applies to more things than its broader parent.”.  
> Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison.  

> Find the incorrect claim.

- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._
- ✅ A narrower concept always applies to more things than its broader parent.  
  _↳ explanation: Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison._
- ◻️ concept: an idea grasped by the mind.  
  _↳ explanation: This statement is correct: concept means an idea grasped by the mind. Look for a claim that conflicts with its definition._
- ◻️ intension: the attributes included in a concept.  
  _↳ explanation: This statement is correct: intension means the attributes included in a concept. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A narrower concept always applies to more things than its broader parent.”.  
> Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison.  

> Find the incorrect claim.

- ✅ An idea and the ink used to write a word are identical objects.  
  _↳ explanation: The idea is its meaning, not the physical ink or sound._
- ◻️ intension: the attributes included in a concept.  
  _↳ explanation: This statement is correct: intension means the attributes included in a concept. Look for a claim that conflicts with its definition._
- ◻️ concept: an idea grasped by the mind.  
  _↳ explanation: This statement is correct: concept means an idea grasped by the mind. Look for a claim that conflicts with its definition._
- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “An idea and the ink used to write a word are identical objects.”.  
> The idea is its meaning, not the physical ink or sound.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

### `l3-9-repair-card` · Lesson 9 · spot the error, level 1

Prompt: Find the incorrect claim.

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ concept: an idea grasped by the mind.
- ✅ term: a word or group of words expressing a concept.
- ✅ intension: the attributes included in a concept.
- ✅ extension: the things to which a concept applies.
- ❌ An idea and the ink used to write a word are identical objects.  
  _↳ The idea is its meaning, not the physical ink or sound._
- ❌ A term must contain only a single word.  
  _↳ Several words can express one concept and function as a term._
- ❌ Intension is the number of letters in the term.  
  _↳ Intension concerns attributes, not spelling length._
- ❌ A narrower concept always applies to more things than its broader parent.  
  _↳ Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison._


Three generated variants:

> Find the incorrect claim.

- ✅ An idea and the ink used to write a word are identical objects.  
  _↳ explanation: The idea is its meaning, not the physical ink or sound._
- ◻️ intension: the attributes included in a concept.  
  _↳ explanation: This statement is correct: intension means the attributes included in a concept. Look for a claim that conflicts with its definition._
- ◻️ extension: the things to which a concept applies.  
  _↳ explanation: This statement is correct: extension means the things to which a concept applies. Look for a claim that conflicts with its definition._
- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “An idea and the ink used to write a word are identical objects.”.  
> The idea is its meaning, not the physical ink or sound.  

> Find the incorrect claim.

- ◻️ extension: the things to which a concept applies.  
  _↳ explanation: This statement is correct: extension means the things to which a concept applies. Look for a claim that conflicts with its definition._
- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._
- ◻️ intension: the attributes included in a concept.  
  _↳ explanation: This statement is correct: intension means the attributes included in a concept. Look for a claim that conflicts with its definition._
- ✅ A narrower concept always applies to more things than its broader parent.  
  _↳ explanation: Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison._

Full working after a second miss:

> The wrong statement is “A narrower concept always applies to more things than its broader parent.”.  
> Adding a qualifying attribute restricts, rather than enlarges, the class in this comparison.  

> Find the incorrect claim.

- ✅ A term must contain only a single word.  
  _↳ explanation: Several words can express one concept and function as a term._
- ◻️ concept: an idea grasped by the mind.  
  _↳ explanation: This statement is correct: concept means an idea grasped by the mind. Look for a claim that conflicts with its definition._
- ◻️ term: a word or group of words expressing a concept.  
  _↳ explanation: This statement is correct: term means a word or group of words expressing a concept. Look for a claim that conflicts with its definition._
- ◻️ intension: the attributes included in a concept.  
  _↳ explanation: This statement is correct: intension means the attributes included in a concept. Look for a claim that conflicts with its definition._

Full working after a second miss:

> The wrong statement is “A term must contain only a single word.”.  
> Several words can express one concept and function as a term.  

Sources: intro-logic (OpenStax Introduction to Philosophy, chapter on logic; Stanford Encyclopedia of Philosophy, Contradiction; traditional school terminology for divisions and operations of mind)

