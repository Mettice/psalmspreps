# Accounting Form 2, Batch A2-1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-accounting`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: rules

- Assets = Liabilities + Owner's equity (computed). Assets increase on the debit side; capital and liabilities on the credit side; expenses debited, revenues credited (authored).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `a2-1-own` | 1 | matching, 1 | financial-position |
| 2 | `a2-1-date` | 1 | multiple choice, 2 | financial-position |
| 3 | `a2-1-date-card` (card c1-3) | 1 | multiple choice, 1 | financial-position |
| 4 | `a2-2-side` | 2 | matching, 1 | financial-position |
| 5 | `a2-2-order` | 2 | matching, 1 | financial-position |
| 6 | `a2-2-head` | 2 | multiple choice, 3 | financial-position |
| 7 | `a2-3-kind` | 3 | matching, 1 | financial-position |
| 8 | `a2-3-debt` | 3 | multiple choice, 1 | financial-position |
| 9 | `a2-3-spot` | 3 | spot the error, 3 | financial-position |
| 10 | `a2-4-change` | 4 | multiple choice, 3 | financial-position |
| 11 | `a2-4-change-card` (card c4-3) | 4 | multiple choice, 1 | financial-position |
| 12 | `a2-5-kind` | 5 | matching, 1 | economic-flows |
| 13 | `a2-5-pair` | 5 | multiple choice, 1 | economic-flows |
| 14 | `a2-5-analyse` | 5 | multiple choice, 2 | economic-flows |
| 15 | `a2-5-spot` | 5 | spot the error, 3 | economic-flows |
| 16 | `a2-5-analyse-card` (card c5-3) | 5 | multiple choice, 1 | economic-flows |
| 17 | `a2-6-arrow` | 6 | multiple choice, 1 | economic-flows |
| 18 | `a2-6-rule` | 6 | multiple choice, 1 | economic-flows |
| 19 | `a2-6-which` | 6 | multiple choice, 2 | economic-flows |
| 20 | `a2-6-spot` | 6 | spot the error, 3 | economic-flows |
| 21 | `a2-6-which-card` (card c6-3) | 6 | multiple choice, 1 | economic-flows |
| 22 | `a2-7-what` | 7 | multiple choice, 1 | recording |
| 23 | `a2-7-side` | 7 | multiple choice, 1 | recording |
| 24 | `a2-7-entry` | 7 | multiple choice, 2 | recording |
| 25 | `a2-7-spot` | 7 | spot the error, 3 | recording |
| 26 | `a2-7-entry-card` (card c7-3) | 7 | multiple choice, 1 | recording |
| 27 | `a2-8-sort` | 8 | matching, 2 | recording |
| 28 | `a2-8-record` | 8 | multiple choice, 3 | recording |
| 29 | `a2-8-sort-card` (card c8-3) | 8 | matching, 1 | recording |
| 30 | `a2-10-kind` | 10 | matching, 1 | recording |
| 31 | `a2-11-kind` | 11 | multiple choice, 1 | recording |
| 32 | `a2-11-pair` | 11 | multiple choice, 1 | recording |
| 33 | `a2-11-total` | 11 | multiple choice, 2 | recording |
| 34 | `a2-11-spot` | 11 | spot the error, 3 | recording |
| 35 | `a2-11-total-card` (card c11-3) | 11 | multiple choice, 1 | recording |
| 36 | `a2-12-recip` | 12 | multiple choice, 1 | recording |
| 37 | `a2-12-limit` | 12 | spot the error, 3 | recording |
| 38 | `a2-12-limit-card` (card c12-3) | 12 | spot the error, 1 | recording |

### `a2-1-own` · Lesson 1 · matching, level 1

Prompt: Sort the items: does the business own it, or owe it?

Pairs (4 shown each time, sorted into groups):

- delivery van → **owns**
- stock of goods → **owns**
- cash in hand → **owns**
- money owed by customers → **owns**
- bank loan → **owes**
- money owed to suppliers → **owes**
- unpaid electricity bill → **owes**


Three generated variants:

> Sort the items: does the business own it, or owe it?

Groups: owns · owes
- money owed by customers → **owns**
- bank loan → **owes**
- cash in hand → **owns**
- delivery van → **owns**

Full working after a second miss:

> The right pairs are:  
> money owed by customers → owns  
> bank loan → owes  
> cash in hand → owns  
> delivery van → owns  

> Sort the items: does the business own it, or owe it?

Groups: owns · owes
- stock of goods → **owns**
- money owed by customers → **owns**
- bank loan → **owes**
- cash in hand → **owns**

Full working after a second miss:

> The right pairs are:  
> stock of goods → owns  
> money owed by customers → owns  
> bank loan → owes  
> cash in hand → owns  

> Sort the items: does the business own it, or owe it?

Groups: owns · owes
- unpaid electricity bill → **owes**
- delivery van → **owns**
- cash in hand → **owns**
- bank loan → **owes**

Full working after a second miss:

> The right pairs are:  
> unpaid electricity bill → owes  
> delivery van → owns  
> cash in hand → owns  
> bank loan → owes  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-1-date` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the financial position always given at a particular date? | It changes with every transaction. | It never changes. · The law forbids dates. · Only the year matters. | It changes all the time. · The date is required. · The exact date matters. | Each sale or purchase changes it. |
| What does evaluating the financial position mean? | listing what is owned and owed and giving each a money value | counting the customers · painting the shop · choosing a new name | That is not evaluation. · That is not evaluation. · That is not evaluation. | Each item gets a value in FCFA. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the financial position always given at a particular date?

- ✅ It changes with every transaction.
- ◻️ It never changes.  
  _↳ feedback if chosen: It changes all the time._
- ◻️ The law forbids dates.  
  _↳ feedback if chosen: The date is required._
- ◻️ Only the year matters.  
  _↳ feedback if chosen: The exact date matters._

Full working after a second miss:

> Each sale or purchase changes it.  
> So the answer is “It changes with every transaction.”.  

> What does evaluating the financial position mean?

- ◻️ choosing a new name  
  _↳ feedback if chosen: That is not evaluation._
- ◻️ painting the shop  
  _↳ feedback if chosen: That is not evaluation._
- ◻️ counting the customers  
  _↳ feedback if chosen: That is not evaluation._
- ✅ listing what is owned and owed and giving each a money value

Full working after a second miss:

> Each item gets a value in FCFA.  
> So the answer is “listing what is owned and owed and giving each a money value”.  

> What does evaluating the financial position mean?

- ◻️ counting the customers  
  _↳ feedback if chosen: That is not evaluation._
- ◻️ choosing a new name  
  _↳ feedback if chosen: That is not evaluation._
- ✅ listing what is owned and owed and giving each a money value
- ◻️ painting the shop  
  _↳ feedback if chosen: That is not evaluation._

Full working after a second miss:

> Each item gets a value in FCFA.  
> So the answer is “listing what is owned and owed and giving each a money value”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-1-date-card` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the financial position always given at a particular date? | It changes with every transaction. | It never changes. · The law forbids dates. · Only the year matters. | It changes all the time. · The date is required. · The exact date matters. | Each sale or purchase changes it. |
| What does evaluating the financial position mean? | listing what is owned and owed and giving each a money value | counting the customers · painting the shop · choosing a new name | That is not evaluation. · That is not evaluation. · That is not evaluation. | Each item gets a value in FCFA. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the financial position always given at a particular date?

- ◻️ It never changes.  
  _↳ feedback if chosen: It changes all the time._
- ✅ It changes with every transaction.
- ◻️ Only the year matters.  
  _↳ feedback if chosen: The exact date matters._
- ◻️ The law forbids dates.  
  _↳ feedback if chosen: The date is required._

Full working after a second miss:

> Each sale or purchase changes it.  
> So the answer is “It changes with every transaction.”.  

> What does evaluating the financial position mean?

- ◻️ painting the shop  
  _↳ feedback if chosen: That is not evaluation._
- ◻️ choosing a new name  
  _↳ feedback if chosen: That is not evaluation._
- ◻️ counting the customers  
  _↳ feedback if chosen: That is not evaluation._
- ✅ listing what is owned and owed and giving each a money value

Full working after a second miss:

> Each item gets a value in FCFA.  
> So the answer is “listing what is owned and owed and giving each a money value”.  

> Why is the financial position always given at a particular date?

- ◻️ Only the year matters.  
  _↳ feedback if chosen: The exact date matters._
- ✅ It changes with every transaction.
- ◻️ It never changes.  
  _↳ feedback if chosen: It changes all the time._
- ◻️ The law forbids dates.  
  _↳ feedback if chosen: The date is required._

Full working after a second miss:

> Each sale or purchase changes it.  
> So the answer is “It changes with every transaction.”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-2-side` · Lesson 2 · matching, level 1

Prompt: On which side of the balance sheet does each item go?

Pairs (5 shown each time, sorted into groups):

- land and buildings → **assets side**
- equipment → **assets side**
- delivery van → **assets side**
- stock of goods → **assets side**
- debtors (customers who owe) → **assets side**
- cash in hand → **assets side**
- money in the bank → **assets side**
- bank loan → **capital and liabilities side**
- creditors (suppliers to be paid) → **capital and liabilities side**
- capital → **capital and liabilities side**


Three generated variants:

> On which side of the balance sheet does each item go?

Groups: assets side · capital and liabilities side
- land and buildings → **assets side**
- creditors (suppliers to be paid) → **capital and liabilities side**
- debtors (customers who owe) → **assets side**
- delivery van → **assets side**
- bank loan → **capital and liabilities side**

Full working after a second miss:

> The right pairs are:  
> land and buildings → assets side  
> creditors (suppliers to be paid) → capital and liabilities side  
> debtors (customers who owe) → assets side  
> delivery van → assets side  
> bank loan → capital and liabilities side  

> On which side of the balance sheet does each item go?

Groups: assets side · capital and liabilities side
- stock of goods → **assets side**
- money in the bank → **assets side**
- debtors (customers who owe) → **assets side**
- bank loan → **capital and liabilities side**
- capital → **capital and liabilities side**

Full working after a second miss:

> The right pairs are:  
> stock of goods → assets side  
> money in the bank → assets side  
> debtors (customers who owe) → assets side  
> bank loan → capital and liabilities side  
> capital → capital and liabilities side  

> On which side of the balance sheet does each item go?

Groups: assets side · capital and liabilities side
- creditors (suppliers to be paid) → **capital and liabilities side**
- stock of goods → **assets side**
- land and buildings → **assets side**
- debtors (customers who owe) → **assets side**
- capital → **capital and liabilities side**

Full working after a second miss:

> The right pairs are:  
> creditors (suppliers to be paid) → capital and liabilities side  
> stock of goods → assets side  
> land and buildings → assets side  
> debtors (customers who owe) → assets side  
> capital → capital and liabilities side  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-2-order` · Lesson 2 · matching, level 1

Prompt: Sort the assets: fixed or current?

Pairs (4 shown each time, sorted into groups):

- land → **fixed**
- buildings → **fixed**
- equipment → **fixed**
- vehicles → **fixed**
- stock → **current**
- debtors → **current**
- bank → **current**
- cash → **current**


Three generated variants:

> Sort the assets: fixed or current?

Groups: fixed · current
- cash → **current**
- buildings → **fixed**
- stock → **current**
- bank → **current**

Full working after a second miss:

> The right pairs are:  
> cash → current  
> buildings → fixed  
> stock → current  
> bank → current  

> Sort the assets: fixed or current?

Groups: fixed · current
- buildings → **fixed**
- vehicles → **fixed**
- cash → **current**
- stock → **current**

Full working after a second miss:

> The right pairs are:  
> buildings → fixed  
> vehicles → fixed  
> cash → current  
> stock → current  

> Sort the assets: fixed or current?

Groups: fixed · current
- buildings → **fixed**
- land → **fixed**
- equipment → **fixed**
- cash → **current**

Full working after a second miss:

> The right pairs are:  
> buildings → fixed  
> land → fixed  
> equipment → fixed  
> cash → current  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-2-head` · Lesson 2 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What must the heading of a balance sheet contain? | the name of the business and the date | only the owner's age · the weather · the customers' names | That is not needed. · That is not needed. · That is not needed. | “X Ltd, balance sheet as at 31 December 2026”. |
| Why must the two sides of a balance sheet be equal? | Everything owned was financed by the owner or by debts. | It is a coincidence. · To look nice. · Because the owner chooses it. | It is always true. · It follows from the equation. · It is a rule of accounting. | Assets = capital + liabilities. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What must the heading of a balance sheet contain?

- ✅ the name of the business and the date
- ◻️ the customers' names  
  _↳ feedback if chosen: That is not needed._
- ◻️ only the owner's age  
  _↳ feedback if chosen: That is not needed._
- ◻️ the weather  
  _↳ feedback if chosen: That is not needed._

Full working after a second miss:

> “X Ltd, balance sheet as at 31 December 2026”.  
> So the answer is “the name of the business and the date”.  

> What must the heading of a balance sheet contain?

- ✅ the name of the business and the date
- ◻️ the customers' names  
  _↳ feedback if chosen: That is not needed._
- ◻️ the weather  
  _↳ feedback if chosen: That is not needed._
- ◻️ only the owner's age  
  _↳ feedback if chosen: That is not needed._

Full working after a second miss:

> “X Ltd, balance sheet as at 31 December 2026”.  
> So the answer is “the name of the business and the date”.  

> Why must the two sides of a balance sheet be equal?

- ◻️ Because the owner chooses it.  
  _↳ feedback if chosen: It is a rule of accounting._
- ◻️ To look nice.  
  _↳ feedback if chosen: It follows from the equation._
- ◻️ It is a coincidence.  
  _↳ feedback if chosen: It is always true._
- ✅ Everything owned was financed by the owner or by debts.

Full working after a second miss:

> Assets = capital + liabilities.  
> So the answer is “Everything owned was financed by the owner or by debts.”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-3-kind` · Lesson 3 · matching, level 1

Prompt: Classify each item.

Pairs (5 shown each time, sorted into groups):

- land and buildings → **asset**
- equipment → **asset**
- delivery van → **asset**
- stock of goods → **asset**
- debtors (customers who owe) → **asset**
- cash in hand → **asset**
- money in the bank → **asset**
- bank loan → **liability**
- creditors (suppliers to be paid) → **liability**
- capital → **owner's equity**


Three generated variants:

> Classify each item.

Groups: asset · liability · owner's equity
- stock of goods → **asset**
- cash in hand → **asset**
- capital → **owner's equity**
- land and buildings → **asset**
- creditors (suppliers to be paid) → **liability**

Full working after a second miss:

> The right pairs are:  
> stock of goods → asset  
> cash in hand → asset  
> capital → owner's equity  
> land and buildings → asset  
> creditors (suppliers to be paid) → liability  

> Classify each item.

Groups: asset · liability · owner's equity
- bank loan → **liability**
- capital → **owner's equity**
- stock of goods → **asset**
- delivery van → **asset**
- debtors (customers who owe) → **asset**

Full working after a second miss:

> The right pairs are:  
> bank loan → liability  
> capital → owner's equity  
> stock of goods → asset  
> delivery van → asset  
> debtors (customers who owe) → asset  

> Classify each item.

Groups: asset · liability · owner's equity
- creditors (suppliers to be paid) → **liability**
- bank loan → **liability**
- delivery van → **asset**
- capital → **owner's equity**
- money in the bank → **asset**

Full working after a second miss:

> The right pairs are:  
> creditors (suppliers to be paid) → liability  
> bank loan → liability  
> delivery van → asset  
> capital → owner's equity  
> money in the bank → asset  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-3-debt` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Are debtors an asset or a liability? | an asset | a liability · owner's equity · neither | Debtors owe the business money. · Capital is the owner's share. · They are an asset. | Debtors will pay the business. |
| Are creditors an asset or a liability? | a liability | an asset · owner's equity · neither | The business owes them. · Capital is the owner's share. · They are a liability. | The business must pay creditors. |
| Which of these is a liability? | a bank loan | cash in hand · equipment · stock | Cash is an asset. · Equipment is an asset. · Stock is an asset. | A loan must be repaid. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Are creditors an asset or a liability?

- ◻️ owner's equity  
  _↳ feedback if chosen: Capital is the owner's share._
- ◻️ an asset  
  _↳ feedback if chosen: The business owes them._
- ◻️ neither  
  _↳ feedback if chosen: They are a liability._
- ✅ a liability

Full working after a second miss:

> The business must pay creditors.  
> So the answer is “a liability”.  

> Are debtors an asset or a liability?

- ✅ an asset
- ◻️ a liability  
  _↳ feedback if chosen: Debtors owe the business money._
- ◻️ owner's equity  
  _↳ feedback if chosen: Capital is the owner's share._
- ◻️ neither  
  _↳ feedback if chosen: They are an asset._

Full working after a second miss:

> Debtors will pay the business.  
> So the answer is “an asset”.  

> Are debtors an asset or a liability?

- ◻️ a liability  
  _↳ feedback if chosen: Debtors owe the business money._
- ✅ an asset
- ◻️ owner's equity  
  _↳ feedback if chosen: Capital is the owner's share._
- ◻️ neither  
  _↳ feedback if chosen: They are an asset._

Full working after a second miss:

> Debtors will pay the business.  
> So the answer is “an asset”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-3-spot` · Lesson 3 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Equipment is an asset.
- ✅ A bank loan is a liability.
- ✅ Capital is the owner's equity.
- ✅ Debtors are assets.
- ❌ Creditors are assets.  
  _↳ Creditors are liabilities: the business owes them._
- ❌ Debtors are liabilities.  
  _↳ Debtors owe the business: they are assets._
- ❌ Drawings increase capital.  
  _↳ Drawings reduce capital._


Three generated variants:

> Which statement is wrong?

- ◻️ A bank loan is a liability.
- ◻️ Capital is the owner's equity.
- ✅ Creditors are assets.  
  _↳ explanation: Creditors are liabilities: the business owes them._
- ◻️ Debtors are assets.

Full working after a second miss:

> The wrong statement is “Creditors are assets.”.  
> Creditors are liabilities: the business owes them.  

> Which statement is wrong?

- ◻️ Debtors are assets.
- ◻️ Capital is the owner's equity.
- ✅ Creditors are assets.  
  _↳ explanation: Creditors are liabilities: the business owes them._
- ◻️ Equipment is an asset.

Full working after a second miss:

> The wrong statement is “Creditors are assets.”.  
> Creditors are liabilities: the business owes them.  

> Which statement is wrong?

- ◻️ Debtors are assets.
- ◻️ A bank loan is a liability.
- ◻️ Capital is the owner's equity.
- ✅ Creditors are assets.  
  _↳ explanation: Creditors are liabilities: the business owes them._

Full working after a second miss:

> The wrong statement is “Creditors are assets.”.  
> Creditors are liabilities: the business owes them.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-4-change` · Lesson 4 · multiple choice, level 3

Prompt: {X.q} How does the equation change?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Equipment is bought for cash. | Equipment goes up and cash goes down by the same amount. | Assets and liabilities both go up. · Capital goes down. · Nothing changes at all. | No debt is created. · The owner's share is unchanged. · Two assets change. | One asset replaces another. |
| Goods are bought on credit. | Stock and creditors both go up by the same amount. | Stock goes up and cash goes down. · Capital goes up. · Creditors go down. | No cash was paid. · The owner put nothing in. · A new debt is created. | An asset and a liability rise together. |
| The owner puts more cash into the business. | Cash and capital both go up by the same amount. | Cash goes up and creditors go up. · Cash goes down. · Equipment goes up. | It is not a debt to outsiders. · Cash comes in. · No equipment is bought. | An asset and owner's equity rise together. |
| A creditor is paid by cheque. | Bank goes down and creditors go down by the same amount. | Bank goes up. · Capital goes up. · Creditors go up. | Money leaves the bank. · The owner's share is unchanged. · The debt is reduced. | An asset and a liability fall together. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Goods are bought on credit. How does the equation change?

- ✅ Stock and creditors both go up by the same amount.
- ◻️ Stock goes up and cash goes down.  
  _↳ feedback if chosen: No cash was paid._
- ◻️ Capital goes up.  
  _↳ feedback if chosen: The owner put nothing in._
- ◻️ Creditors go down.  
  _↳ feedback if chosen: A new debt is created._

Full working after a second miss:

> An asset and a liability rise together.  
> So the answer is “Stock and creditors both go up by the same amount.”.  

> The owner puts more cash into the business. How does the equation change?

- ✅ Cash and capital both go up by the same amount.
- ◻️ Cash goes down.  
  _↳ feedback if chosen: Cash comes in._
- ◻️ Equipment goes up.  
  _↳ feedback if chosen: No equipment is bought._
- ◻️ Cash goes up and creditors go up.  
  _↳ feedback if chosen: It is not a debt to outsiders._

Full working after a second miss:

> An asset and owner's equity rise together.  
> So the answer is “Cash and capital both go up by the same amount.”.  

> The owner puts more cash into the business. How does the equation change?

- ◻️ Cash goes up and creditors go up.  
  _↳ feedback if chosen: It is not a debt to outsiders._
- ◻️ Equipment goes up.  
  _↳ feedback if chosen: No equipment is bought._
- ◻️ Cash goes down.  
  _↳ feedback if chosen: Cash comes in._
- ✅ Cash and capital both go up by the same amount.

Full working after a second miss:

> An asset and owner's equity rise together.  
> So the answer is “Cash and capital both go up by the same amount.”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-4-change-card` · Lesson 4 · multiple choice, level 1

Prompt: {X.q} How does the equation change?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Equipment is bought for cash. | Equipment goes up and cash goes down by the same amount. | Assets and liabilities both go up. · Capital goes down. · Nothing changes at all. | No debt is created. · The owner's share is unchanged. · Two assets change. | One asset replaces another. |
| Goods are bought on credit. | Stock and creditors both go up by the same amount. | Stock goes up and cash goes down. · Capital goes up. · Creditors go down. | No cash was paid. · The owner put nothing in. · A new debt is created. | An asset and a liability rise together. |
| The owner puts more cash into the business. | Cash and capital both go up by the same amount. | Cash goes up and creditors go up. · Cash goes down. · Equipment goes up. | It is not a debt to outsiders. · Cash comes in. · No equipment is bought. | An asset and owner's equity rise together. |
| A creditor is paid by cheque. | Bank goes down and creditors go down by the same amount. | Bank goes up. · Capital goes up. · Creditors go up. | Money leaves the bank. · The owner's share is unchanged. · The debt is reduced. | An asset and a liability fall together. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Goods are bought on credit. How does the equation change?

- ◻️ Stock goes up and cash goes down.  
  _↳ feedback if chosen: No cash was paid._
- ◻️ Creditors go down.  
  _↳ feedback if chosen: A new debt is created._
- ✅ Stock and creditors both go up by the same amount.
- ◻️ Capital goes up.  
  _↳ feedback if chosen: The owner put nothing in._

Full working after a second miss:

> An asset and a liability rise together.  
> So the answer is “Stock and creditors both go up by the same amount.”.  

> Goods are bought on credit. How does the equation change?

- ◻️ Creditors go down.  
  _↳ feedback if chosen: A new debt is created._
- ◻️ Capital goes up.  
  _↳ feedback if chosen: The owner put nothing in._
- ✅ Stock and creditors both go up by the same amount.
- ◻️ Stock goes up and cash goes down.  
  _↳ feedback if chosen: No cash was paid._

Full working after a second miss:

> An asset and a liability rise together.  
> So the answer is “Stock and creditors both go up by the same amount.”.  

> Equipment is bought for cash. How does the equation change?

- ◻️ Assets and liabilities both go up.  
  _↳ feedback if chosen: No debt is created._
- ◻️ Nothing changes at all.  
  _↳ feedback if chosen: Two assets change._
- ✅ Equipment goes up and cash goes down by the same amount.
- ◻️ Capital goes down.  
  _↳ feedback if chosen: The owner's share is unchanged._

Full working after a second miss:

> One asset replaces another.  
> So the answer is “Equipment goes up and cash goes down by the same amount.”.  

Sources: financial-position (The financial position of an enterprise and the balance sheet (OHADA / SYSCOHADA vocabulary simplified for Form 2))

### `a2-5-kind` · Lesson 5 · matching, level 1

Prompt: Sort the flows: real or financial?

Pairs (4 shown each time, sorted into groups):

- goods delivered by a supplier → **real flow**
- a service received (repairs) → **real flow**
- goods sold to a customer → **real flow**
- work done by an employee → **real flow**
- cash paid to a supplier → **financial flow**
- a cheque received from a customer → **financial flow**
- salary paid to an employee → **financial flow**
- a bank loan received → **financial flow**


Three generated variants:

> Sort the flows: real or financial?

Groups: real flow · financial flow
- salary paid to an employee → **financial flow**
- goods delivered by a supplier → **real flow**
- a bank loan received → **financial flow**
- goods sold to a customer → **real flow**

Full working after a second miss:

> The right pairs are:  
> salary paid to an employee → financial flow  
> goods delivered by a supplier → real flow  
> a bank loan received → financial flow  
> goods sold to a customer → real flow  

> Sort the flows: real or financial?

Groups: real flow · financial flow
- goods delivered by a supplier → **real flow**
- work done by an employee → **real flow**
- goods sold to a customer → **real flow**
- cash paid to a supplier → **financial flow**

Full working after a second miss:

> The right pairs are:  
> goods delivered by a supplier → real flow  
> work done by an employee → real flow  
> goods sold to a customer → real flow  
> cash paid to a supplier → financial flow  

> Sort the flows: real or financial?

Groups: real flow · financial flow
- a cheque received from a customer → **financial flow**
- goods delivered by a supplier → **real flow**
- cash paid to a supplier → **financial flow**
- a bank loan received → **financial flow**

Full working after a second miss:

> The right pairs are:  
> a cheque received from a customer → financial flow  
> goods delivered by a supplier → real flow  
> cash paid to a supplier → financial flow  
> a bank loan received → financial flow  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-5-pair` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A customer buys goods and pays cash. Which flows are there? | goods out to the customer and cash in to the business | only goods out · only cash out · goods in and cash in | Money also moves. · Cash comes in. · Goods go out. | A real flow out, a financial flow in. |
| An employee is paid her salary. Which flow is the payment? | a financial flow | a real flow · no flow · a flow of goods | Money is financial. · Money moves. · No goods move. | Salary is money. |
| Who are the partners of a business? | suppliers, customers, employees, the bank and the State | only the owner · only customers · only the bank | There are others. · There are others. · There are others. | Many partners exchange with the business. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Who are the partners of a business?

- ✅ suppliers, customers, employees, the bank and the State
- ◻️ only the owner  
  _↳ feedback if chosen: There are others._
- ◻️ only customers  
  _↳ feedback if chosen: There are others._
- ◻️ only the bank  
  _↳ feedback if chosen: There are others._

Full working after a second miss:

> Many partners exchange with the business.  
> So the answer is “suppliers, customers, employees, the bank and the State”.  

> A customer buys goods and pays cash. Which flows are there?

- ◻️ only cash out  
  _↳ feedback if chosen: Cash comes in._
- ◻️ goods in and cash in  
  _↳ feedback if chosen: Goods go out._
- ◻️ only goods out  
  _↳ feedback if chosen: Money also moves._
- ✅ goods out to the customer and cash in to the business

Full working after a second miss:

> A real flow out, a financial flow in.  
> So the answer is “goods out to the customer and cash in to the business”.  

> A customer buys goods and pays cash. Which flows are there?

- ◻️ only goods out  
  _↳ feedback if chosen: Money also moves._
- ✅ goods out to the customer and cash in to the business
- ◻️ goods in and cash in  
  _↳ feedback if chosen: Goods go out._
- ◻️ only cash out  
  _↳ feedback if chosen: Cash comes in._

Full working after a second miss:

> A real flow out, a financial flow in.  
> So the answer is “goods out to the customer and cash in to the business”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-5-analyse` · Lesson 5 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Goods are bought on credit. What is special about this transaction? | The goods come in now, but the payment comes later: a debt is created. | Money comes in now. · No goods move. · It is not a transaction. | No money moves now. · Goods come in. · It is a transaction. | The financial flow is delayed. |
| What does accounting analysis of a transaction find? | its flows, the partners and the accounts affected | the owner's age · the colour of the goods · the weather that day | Not relevant. · Not relevant. · Not relevant. | Analysis prepares the recording. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does accounting analysis of a transaction find?

- ◻️ the weather that day  
  _↳ feedback if chosen: Not relevant._
- ◻️ the owner's age  
  _↳ feedback if chosen: Not relevant._
- ✅ its flows, the partners and the accounts affected
- ◻️ the colour of the goods  
  _↳ feedback if chosen: Not relevant._

Full working after a second miss:

> Analysis prepares the recording.  
> So the answer is “its flows, the partners and the accounts affected”.  

> Goods are bought on credit. What is special about this transaction?

- ◻️ Money comes in now.  
  _↳ feedback if chosen: No money moves now._
- ◻️ No goods move.  
  _↳ feedback if chosen: Goods come in._
- ✅ The goods come in now, but the payment comes later: a debt is created.
- ◻️ It is not a transaction.  
  _↳ feedback if chosen: It is a transaction._

Full working after a second miss:

> The financial flow is delayed.  
> So the answer is “The goods come in now, but the payment comes later: a debt is created.”.  

> What does accounting analysis of a transaction find?

- ✅ its flows, the partners and the accounts affected
- ◻️ the weather that day  
  _↳ feedback if chosen: Not relevant._
- ◻️ the owner's age  
  _↳ feedback if chosen: Not relevant._
- ◻️ the colour of the goods  
  _↳ feedback if chosen: Not relevant._

Full working after a second miss:

> Analysis prepares the recording.  
> So the answer is “its flows, the partners and the accounts affected”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-5-spot` · Lesson 5 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Goods delivered are a real flow.
- ✅ Cash paid is a financial flow.
- ✅ The bank is a partner.
- ✅ A credit purchase creates a debt.
- ❌ A cheque is a real flow.  
  _↳ A cheque is money: a financial flow._
- ❌ Work done by an employee is a financial flow.  
  _↳ Work is a service: a real flow._
- ❌ Every transaction has only one flow.  
  _↳ Most have two opposite flows._


Three generated variants:

> Which statement is wrong?

- ◻️ Goods delivered are a real flow.
- ◻️ A credit purchase creates a debt.
- ◻️ The bank is a partner.
- ✅ Work done by an employee is a financial flow.  
  _↳ explanation: Work is a service: a real flow._

Full working after a second miss:

> The wrong statement is “Work done by an employee is a financial flow.”.  
> Work is a service: a real flow.  

> Which statement is wrong?

- ✅ Every transaction has only one flow.  
  _↳ explanation: Most have two opposite flows._
- ◻️ The bank is a partner.
- ◻️ Goods delivered are a real flow.
- ◻️ Cash paid is a financial flow.

Full working after a second miss:

> The wrong statement is “Every transaction has only one flow.”.  
> Most have two opposite flows.  

> Which statement is wrong?

- ◻️ The bank is a partner.
- ✅ Every transaction has only one flow.  
  _↳ explanation: Most have two opposite flows._
- ◻️ Goods delivered are a real flow.
- ◻️ Cash paid is a financial flow.

Full working after a second miss:

> The wrong statement is “Every transaction has only one flow.”.  
> Most have two opposite flows.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-5-analyse-card` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Goods are bought on credit. What is special about this transaction? | The goods come in now, but the payment comes later: a debt is created. | Money comes in now. · No goods move. · It is not a transaction. | No money moves now. · Goods come in. · It is a transaction. | The financial flow is delayed. |
| What does accounting analysis of a transaction find? | its flows, the partners and the accounts affected | the owner's age · the colour of the goods · the weather that day | Not relevant. · Not relevant. · Not relevant. | Analysis prepares the recording. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Goods are bought on credit. What is special about this transaction?

- ✅ The goods come in now, but the payment comes later: a debt is created.
- ◻️ It is not a transaction.  
  _↳ feedback if chosen: It is a transaction._
- ◻️ No goods move.  
  _↳ feedback if chosen: Goods come in._
- ◻️ Money comes in now.  
  _↳ feedback if chosen: No money moves now._

Full working after a second miss:

> The financial flow is delayed.  
> So the answer is “The goods come in now, but the payment comes later: a debt is created.”.  

> What does accounting analysis of a transaction find?

- ◻️ the owner's age  
  _↳ feedback if chosen: Not relevant._
- ◻️ the colour of the goods  
  _↳ feedback if chosen: Not relevant._
- ✅ its flows, the partners and the accounts affected
- ◻️ the weather that day  
  _↳ feedback if chosen: Not relevant._

Full working after a second miss:

> Analysis prepares the recording.  
> So the answer is “its flows, the partners and the accounts affected”.  

> Goods are bought on credit. What is special about this transaction?

- ◻️ It is not a transaction.  
  _↳ feedback if chosen: It is a transaction._
- ◻️ Money comes in now.  
  _↳ feedback if chosen: No money moves now._
- ◻️ No goods move.  
  _↳ feedback if chosen: Goods come in._
- ✅ The goods come in now, but the payment comes later: a debt is created.

Full working after a second miss:

> The financial flow is delayed.  
> So the answer is “The goods come in now, but the payment comes later: a debt is created.”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-6-arrow` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In a flow diagram, what does an arrow show? | the direction a flow moves, from one partner to another | the owner's name · the date of the balance sheet · a profit | Not shown by arrows. · Not shown by arrows. · Not shown by arrows. | Arrows show who gives and who receives. |
| Goods are sold for cash. In which direction does the cash arrow point? | from the customer to the business | from the business to the customer · from the bank to the State · there is no cash arrow | The goods go that way. · They are not involved. · Cash moves. | The customer pays the business. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Goods are sold for cash. In which direction does the cash arrow point?

- ◻️ from the business to the customer  
  _↳ feedback if chosen: The goods go that way._
- ◻️ from the bank to the State  
  _↳ feedback if chosen: They are not involved._
- ◻️ there is no cash arrow  
  _↳ feedback if chosen: Cash moves._
- ✅ from the customer to the business

Full working after a second miss:

> The customer pays the business.  
> So the answer is “from the customer to the business”.  

> Goods are sold for cash. In which direction does the cash arrow point?

- ◻️ from the bank to the State  
  _↳ feedback if chosen: They are not involved._
- ◻️ from the business to the customer  
  _↳ feedback if chosen: The goods go that way._
- ✅ from the customer to the business
- ◻️ there is no cash arrow  
  _↳ feedback if chosen: Cash moves._

Full working after a second miss:

> The customer pays the business.  
> So the answer is “from the customer to the business”.  

> Goods are sold for cash. In which direction does the cash arrow point?

- ◻️ from the bank to the State  
  _↳ feedback if chosen: They are not involved._
- ◻️ from the business to the customer  
  _↳ feedback if chosen: The goods go that way._
- ✅ from the customer to the business
- ◻️ there is no cash arrow  
  _↳ feedback if chosen: Cash moves._

Full working after a second miss:

> The customer pays the business.  
> So the answer is “from the customer to the business”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-6-rule` · Lesson 6 · multiple choice, level 1

Prompt: Equipment is bought for cash. Which analysis is correct?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ Debit Equipment, credit Cash
- ✅ Equipment increases and cash decreases
- ❌ Debit Cash, credit Equipment  
  _↳ Equipment receives (debit); cash gives (credit)._
- ❌ Credit both accounts  
  _↳ One account is debited and one credited._
- ❌ Only the Cash account changes  
  _↳ Two accounts change._


Three generated variants:

> Equipment is bought for cash. Which analysis is correct?

- ✅ Equipment increases and cash decreases
- ◻️ Credit both accounts  
  _↳ feedback if chosen: One account is debited and one credited._
- ◻️ Only the Cash account changes  
  _↳ feedback if chosen: Two accounts change._

Full working after a second miss:

> The true statement is “Equipment increases and cash decreases”.  
> “Credit both accounts” is false: One account is debited and one credited.  
> “Only the Cash account changes” is false: Two accounts change.  

> Equipment is bought for cash. Which analysis is correct?

- ◻️ Debit Cash, credit Equipment  
  _↳ feedback if chosen: Equipment receives (debit); cash gives (credit)._
- ◻️ Credit both accounts  
  _↳ feedback if chosen: One account is debited and one credited._
- ✅ Debit Equipment, credit Cash

Full working after a second miss:

> The true statement is “Debit Equipment, credit Cash”.  
> “Debit Cash, credit Equipment” is false: Equipment receives (debit); cash gives (credit).  
> “Credit both accounts” is false: One account is debited and one credited.  

> Equipment is bought for cash. Which analysis is correct?

- ✅ Equipment increases and cash decreases
- ◻️ Debit Cash, credit Equipment  
  _↳ feedback if chosen: Equipment receives (debit); cash gives (credit)._
- ◻️ Only the Cash account changes  
  _↳ feedback if chosen: Two accounts change._

Full working after a second miss:

> The true statement is “Equipment increases and cash decreases”.  
> “Debit Cash, credit Equipment” is false: Equipment receives (debit); cash gives (credit).  
> “Only the Cash account changes” is false: Two accounts change.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-6-which` · Lesson 6 · multiple choice, level 2

Prompt: {X.q} Which account is debited?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Goods are bought on credit from Tabe Supplies. | Purchases (goods) | Tabe Supplies (creditor) · Cash · Capital | The supplier gives: credit. · No cash moves. · The owner is not involved. | Goods are received: debit Purchases. |
| A customer pays 50 000 FCFA cash for goods. | Cash | Sales · Capital · Equipment | Sales is credited. · Not involved. · Not involved. | Cash is received: debit Cash. |
| The owner brings 1 000 000 FCFA into the business bank account. | Bank | Capital · Creditors · Sales | Capital gives: credit. · Not involved. · Not involved. | The bank receives: debit Bank. |
| Electricity bill paid in cash. | Electricity (expense) | Cash · Sales · Capital | Cash gives: credit. · Not involved. · Not involved. | The expense receives the service: debit it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Electricity bill paid in cash. Which account is debited?

- ✅ Electricity (expense)
- ◻️ Cash  
  _↳ feedback if chosen: Cash gives: credit._
- ◻️ Capital  
  _↳ feedback if chosen: Not involved._
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._

Full working after a second miss:

> The expense receives the service: debit it.  
> So the answer is “Electricity (expense)”.  

> The owner brings 1 000 000 FCFA into the business bank account. Which account is debited?

- ◻️ Creditors  
  _↳ feedback if chosen: Not involved._
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ✅ Bank
- ◻️ Capital  
  _↳ feedback if chosen: Capital gives: credit._

Full working after a second miss:

> The bank receives: debit Bank.  
> So the answer is “Bank”.  

> Electricity bill paid in cash. Which account is debited?

- ✅ Electricity (expense)
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ◻️ Cash  
  _↳ feedback if chosen: Cash gives: credit._
- ◻️ Capital  
  _↳ feedback if chosen: Not involved._

Full working after a second miss:

> The expense receives the service: debit it.  
> So the answer is “Electricity (expense)”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-6-spot` · Lesson 6 · spot the error, level 3

Prompt: Which analysis is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Cash sale: debit Cash, credit Sales.
- ✅ Rent paid in cash: debit Rent, credit Cash.
- ✅ Owner brings cash: debit Cash, credit Capital.
- ✅ Credit purchase: debit Purchases, credit Creditors.
- ❌ Cash sale: debit Sales, credit Cash.  
  _↳ Cash receives (debit); Sales gives (credit)._
- ❌ Equipment bought for cash: debit Cash, credit Equipment.  
  _↳ Debit Equipment, credit Cash._
- ❌ Paying a creditor by cheque: debit Bank, credit Creditors.  
  _↳ Debit Creditors (debt reduced), credit Bank (money leaves)._


Three generated variants:

> Which analysis is wrong?

- ◻️ Cash sale: debit Cash, credit Sales.
- ◻️ Rent paid in cash: debit Rent, credit Cash.
- ✅ Paying a creditor by cheque: debit Bank, credit Creditors.  
  _↳ explanation: Debit Creditors (debt reduced), credit Bank (money leaves)._
- ◻️ Credit purchase: debit Purchases, credit Creditors.

Full working after a second miss:

> The wrong statement is “Paying a creditor by cheque: debit Bank, credit Creditors.”.  
> Debit Creditors (debt reduced), credit Bank (money leaves).  

> Which analysis is wrong?

- ◻️ Owner brings cash: debit Cash, credit Capital.
- ✅ Equipment bought for cash: debit Cash, credit Equipment.  
  _↳ explanation: Debit Equipment, credit Cash._
- ◻️ Credit purchase: debit Purchases, credit Creditors.
- ◻️ Cash sale: debit Cash, credit Sales.

Full working after a second miss:

> The wrong statement is “Equipment bought for cash: debit Cash, credit Equipment.”.  
> Debit Equipment, credit Cash.  

> Which analysis is wrong?

- ◻️ Cash sale: debit Cash, credit Sales.
- ◻️ Owner brings cash: debit Cash, credit Capital.
- ✅ Equipment bought for cash: debit Cash, credit Equipment.  
  _↳ explanation: Debit Equipment, credit Cash._
- ◻️ Credit purchase: debit Purchases, credit Creditors.

Full working after a second miss:

> The wrong statement is “Equipment bought for cash: debit Cash, credit Equipment.”.  
> Debit Equipment, credit Cash.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-6-which-card` · Lesson 6 · multiple choice, level 1

Prompt: {X.q} Which account is debited?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Goods are bought on credit from Tabe Supplies. | Purchases (goods) | Tabe Supplies (creditor) · Cash · Capital | The supplier gives: credit. · No cash moves. · The owner is not involved. | Goods are received: debit Purchases. |
| A customer pays 50 000 FCFA cash for goods. | Cash | Sales · Capital · Equipment | Sales is credited. · Not involved. · Not involved. | Cash is received: debit Cash. |
| The owner brings 1 000 000 FCFA into the business bank account. | Bank | Capital · Creditors · Sales | Capital gives: credit. · Not involved. · Not involved. | The bank receives: debit Bank. |
| Electricity bill paid in cash. | Electricity (expense) | Cash · Sales · Capital | Cash gives: credit. · Not involved. · Not involved. | The expense receives the service: debit it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Electricity bill paid in cash. Which account is debited?

- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ◻️ Cash  
  _↳ feedback if chosen: Cash gives: credit._
- ✅ Electricity (expense)
- ◻️ Capital  
  _↳ feedback if chosen: Not involved._

Full working after a second miss:

> The expense receives the service: debit it.  
> So the answer is “Electricity (expense)”.  

> Goods are bought on credit from Tabe Supplies. Which account is debited?

- ◻️ Tabe Supplies (creditor)  
  _↳ feedback if chosen: The supplier gives: credit._
- ◻️ Cash  
  _↳ feedback if chosen: No cash moves._
- ✅ Purchases (goods)
- ◻️ Capital  
  _↳ feedback if chosen: The owner is not involved._

Full working after a second miss:

> Goods are received: debit Purchases.  
> So the answer is “Purchases (goods)”.  

> Goods are bought on credit from Tabe Supplies. Which account is debited?

- ✅ Purchases (goods)
- ◻️ Cash  
  _↳ feedback if chosen: No cash moves._
- ◻️ Tabe Supplies (creditor)  
  _↳ feedback if chosen: The supplier gives: credit._
- ◻️ Capital  
  _↳ feedback if chosen: The owner is not involved._

Full working after a second miss:

> Goods are received: debit Purchases.  
> So the answer is “Purchases (goods)”.  

Sources: economic-flows (Economic flows (real and financial) between the enterprise and its partners; accounting analysis (the receiving account is debited, the giving account credited))

### `a2-7-what` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the ledger? | the book (or file) containing all the accounts | the owner's diary · a list of customers' phone numbers · the shop's sign | Not that. · Not that. · Not that. | All the accounts together. |
| What is an account? | a record of all the changes in one item | a type of bank · the owner's money only · a receipt | Not that. · It can be any item. · A receipt is a document. | One account for each item. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the ledger?

- ◻️ the owner's diary  
  _↳ feedback if chosen: Not that._
- ✅ the book (or file) containing all the accounts
- ◻️ a list of customers' phone numbers  
  _↳ feedback if chosen: Not that._
- ◻️ the shop's sign  
  _↳ feedback if chosen: Not that._

Full working after a second miss:

> All the accounts together.  
> So the answer is “the book (or file) containing all the accounts”.  

> What is the ledger?

- ◻️ the owner's diary  
  _↳ feedback if chosen: Not that._
- ◻️ the shop's sign  
  _↳ feedback if chosen: Not that._
- ✅ the book (or file) containing all the accounts
- ◻️ a list of customers' phone numbers  
  _↳ feedback if chosen: Not that._

Full working after a second miss:

> All the accounts together.  
> So the answer is “the book (or file) containing all the accounts”.  

> What is the ledger?

- ◻️ the owner's diary  
  _↳ feedback if chosen: Not that._
- ◻️ a list of customers' phone numbers  
  _↳ feedback if chosen: Not that._
- ✅ the book (or file) containing all the accounts
- ◻️ the shop's sign  
  _↳ feedback if chosen: Not that._

Full working after a second miss:

> All the accounts together.  
> So the answer is “the book (or file) containing all the accounts”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-7-side` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which side of a T-account is the debit side? | the left side | the right side · the top · the bottom | That is credit. · The name is at the top. · No. | Debit = left. |
| What does “Cr” mean? | credit, the right side | cash received · creditor only · the left side | It is an abbreviation of credit. · Not only. · That is debit. | Cr = credit = right. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does “Cr” mean?

- ◻️ cash received  
  _↳ feedback if chosen: It is an abbreviation of credit._
- ✅ credit, the right side
- ◻️ creditor only  
  _↳ feedback if chosen: Not only._
- ◻️ the left side  
  _↳ feedback if chosen: That is debit._

Full working after a second miss:

> Cr = credit = right.  
> So the answer is “credit, the right side”.  

> What does “Cr” mean?

- ◻️ cash received  
  _↳ feedback if chosen: It is an abbreviation of credit._
- ◻️ the left side  
  _↳ feedback if chosen: That is debit._
- ◻️ creditor only  
  _↳ feedback if chosen: Not only._
- ✅ credit, the right side

Full working after a second miss:

> Cr = credit = right.  
> So the answer is “credit, the right side”.  

> What does “Cr” mean?

- ◻️ creditor only  
  _↳ feedback if chosen: Not only._
- ✅ credit, the right side
- ◻️ cash received  
  _↳ feedback if chosen: It is an abbreviation of credit._
- ◻️ the left side  
  _↳ feedback if chosen: That is debit._

Full working after a second miss:

> Cr = credit = right.  
> So the answer is “credit, the right side”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-7-entry` · Lesson 7 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does each entry in an account show? | the date, the details and the amount | only the amount · the owner's signature · the weather | More is needed. · Not needed. · Not needed. | Date, details, amount. |
| In the Cash account, what is written in the details column when cash comes from the owner? | Capital | Cash · Rent · Sales | That is the account itself. · Rent is an expense. · Sales is not involved. | Write the other account. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does each entry in an account show?

- ✅ the date, the details and the amount
- ◻️ only the amount  
  _↳ feedback if chosen: More is needed._
- ◻️ the weather  
  _↳ feedback if chosen: Not needed._
- ◻️ the owner's signature  
  _↳ feedback if chosen: Not needed._

Full working after a second miss:

> Date, details, amount.  
> So the answer is “the date, the details and the amount”.  

> What does each entry in an account show?

- ◻️ the weather  
  _↳ feedback if chosen: Not needed._
- ◻️ the owner's signature  
  _↳ feedback if chosen: Not needed._
- ◻️ only the amount  
  _↳ feedback if chosen: More is needed._
- ✅ the date, the details and the amount

Full working after a second miss:

> Date, details, amount.  
> So the answer is “the date, the details and the amount”.  

> What does each entry in an account show?

- ◻️ the owner's signature  
  _↳ feedback if chosen: Not needed._
- ◻️ the weather  
  _↳ feedback if chosen: Not needed._
- ◻️ only the amount  
  _↳ feedback if chosen: More is needed._
- ✅ the date, the details and the amount

Full working after a second miss:

> Date, details, amount.  
> So the answer is “the date, the details and the amount”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-7-spot` · Lesson 7 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The debit side is on the left.
- ✅ The credit side is on the right.
- ✅ All accounts form the ledger.
- ✅ Each entry has a date.
- ❌ Debit means a bad entry.  
  _↳ Debit just means the left side._
- ❌ The credit side is on the left.  
  _↳ Credit is the right side._
- ❌ An entry needs no amount.  
  _↳ Every entry has an amount._


Three generated variants:

> Which statement is wrong?

- ◻️ The debit side is on the left.
- ◻️ All accounts form the ledger.
- ✅ An entry needs no amount.  
  _↳ explanation: Every entry has an amount._
- ◻️ Each entry has a date.

Full working after a second miss:

> The wrong statement is “An entry needs no amount.”.  
> Every entry has an amount.  

> Which statement is wrong?

- ◻️ All accounts form the ledger.
- ✅ Debit means a bad entry.  
  _↳ explanation: Debit just means the left side._
- ◻️ The debit side is on the left.
- ◻️ Each entry has a date.

Full working after a second miss:

> The wrong statement is “Debit means a bad entry.”.  
> Debit just means the left side.  

> Which statement is wrong?

- ◻️ The credit side is on the right.
- ◻️ All accounts form the ledger.
- ✅ The credit side is on the left.  
  _↳ explanation: Credit is the right side._
- ◻️ The debit side is on the left.

Full working after a second miss:

> The wrong statement is “The credit side is on the left.”.  
> Credit is the right side.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-7-entry-card` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does each entry in an account show? | the date, the details and the amount | only the amount · the owner's signature · the weather | More is needed. · Not needed. · Not needed. | Date, details, amount. |
| In the Cash account, what is written in the details column when cash comes from the owner? | Capital | Cash · Rent · Sales | That is the account itself. · Rent is an expense. · Sales is not involved. | Write the other account. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In the Cash account, what is written in the details column when cash comes from the owner?

- ◻️ Rent  
  _↳ feedback if chosen: Rent is an expense._
- ◻️ Cash  
  _↳ feedback if chosen: That is the account itself._
- ◻️ Sales  
  _↳ feedback if chosen: Sales is not involved._
- ✅ Capital

Full working after a second miss:

> Write the other account.  
> So the answer is “Capital”.  

> What does each entry in an account show?

- ◻️ only the amount  
  _↳ feedback if chosen: More is needed._
- ✅ the date, the details and the amount
- ◻️ the weather  
  _↳ feedback if chosen: Not needed._
- ◻️ the owner's signature  
  _↳ feedback if chosen: Not needed._

Full working after a second miss:

> Date, details, amount.  
> So the answer is “the date, the details and the amount”.  

> What does each entry in an account show?

- ◻️ only the amount  
  _↳ feedback if chosen: More is needed._
- ✅ the date, the details and the amount
- ◻️ the owner's signature  
  _↳ feedback if chosen: Not needed._
- ◻️ the weather  
  _↳ feedback if chosen: Not needed._

Full working after a second miss:

> Date, details, amount.  
> So the answer is “the date, the details and the amount”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-8-sort` · Lesson 8 · matching, level 2

Prompt: Sort the accounts: asset, or capital/liability?

Pairs (5 shown each time, sorted into groups):

- Cash → **asset**
- Bank → **asset**
- Equipment → **asset**
- Stock → **asset**
- Debtors → **asset**
- Capital → **capital or liability**
- Bank loan → **capital or liability**
- Creditors → **capital or liability**


Three generated variants:

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Creditors → **capital or liability**
- Bank → **asset**
- Bank loan → **capital or liability**
- Stock → **asset**
- Cash → **asset**

Full working after a second miss:

> The right pairs are:  
> Creditors → capital or liability  
> Bank → asset  
> Bank loan → capital or liability  
> Stock → asset  
> Cash → asset  

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Stock → **asset**
- Debtors → **asset**
- Bank → **asset**
- Bank loan → **capital or liability**
- Creditors → **capital or liability**

Full working after a second miss:

> The right pairs are:  
> Stock → asset  
> Debtors → asset  
> Bank → asset  
> Bank loan → capital or liability  
> Creditors → capital or liability  

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Debtors → **asset**
- Stock → **asset**
- Bank loan → **capital or liability**
- Equipment → **asset**
- Bank → **asset**

Full working after a second miss:

> The right pairs are:  
> Debtors → asset  
> Stock → asset  
> Bank loan → capital or liability  
> Equipment → asset  
> Bank → asset  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-8-record` · Lesson 8 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A creditor is paid 80 000 FCFA in cash. Which entries are made? | debit Creditors, credit Cash | debit Cash, credit Creditors · credit both · debit both | Cash decreases (credit); the debt decreases (debit). · One debit, one credit. · One debit, one credit. | The debt falls (debit) and cash falls (credit). |
| The owner brings 500 000 FCFA in cash. Which entries are made? | debit Cash, credit Capital | debit Capital, credit Cash · debit Cash, credit Creditors · credit Cash, credit Capital | Cash increases (debit), capital increases (credit). · It is the owner, not a supplier. · One debit, one credit. | An asset and capital both increase. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A creditor is paid 80 000 FCFA in cash. Which entries are made?

- ◻️ debit both  
  _↳ feedback if chosen: One debit, one credit._
- ◻️ debit Cash, credit Creditors  
  _↳ feedback if chosen: Cash decreases (credit); the debt decreases (debit)._
- ◻️ credit both  
  _↳ feedback if chosen: One debit, one credit._
- ✅ debit Creditors, credit Cash

Full working after a second miss:

> The debt falls (debit) and cash falls (credit).  
> So the answer is “debit Creditors, credit Cash”.  

> A creditor is paid 80 000 FCFA in cash. Which entries are made?

- ◻️ debit both  
  _↳ feedback if chosen: One debit, one credit._
- ◻️ credit both  
  _↳ feedback if chosen: One debit, one credit._
- ✅ debit Creditors, credit Cash
- ◻️ debit Cash, credit Creditors  
  _↳ feedback if chosen: Cash decreases (credit); the debt decreases (debit)._

Full working after a second miss:

> The debt falls (debit) and cash falls (credit).  
> So the answer is “debit Creditors, credit Cash”.  

> The owner brings 500 000 FCFA in cash. Which entries are made?

- ◻️ credit Cash, credit Capital  
  _↳ feedback if chosen: One debit, one credit._
- ◻️ debit Cash, credit Creditors  
  _↳ feedback if chosen: It is the owner, not a supplier._
- ◻️ debit Capital, credit Cash  
  _↳ feedback if chosen: Cash increases (debit), capital increases (credit)._
- ✅ debit Cash, credit Capital

Full working after a second miss:

> An asset and capital both increase.  
> So the answer is “debit Cash, credit Capital”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-8-sort-card` · Lesson 8 · matching, level 1

Prompt: Sort the accounts: asset, or capital/liability?

Pairs (5 shown each time, sorted into groups):

- Cash → **asset**
- Bank → **asset**
- Equipment → **asset**
- Stock → **asset**
- Debtors → **asset**
- Capital → **capital or liability**
- Bank loan → **capital or liability**
- Creditors → **capital or liability**


Three generated variants:

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Bank loan → **capital or liability**
- Cash → **asset**
- Equipment → **asset**
- Capital → **capital or liability**
- Bank → **asset**

Full working after a second miss:

> The right pairs are:  
> Bank loan → capital or liability  
> Cash → asset  
> Equipment → asset  
> Capital → capital or liability  
> Bank → asset  

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Creditors → **capital or liability**
- Debtors → **asset**
- Bank → **asset**
- Capital → **capital or liability**
- Bank loan → **capital or liability**

Full working after a second miss:

> The right pairs are:  
> Creditors → capital or liability  
> Debtors → asset  
> Bank → asset  
> Capital → capital or liability  
> Bank loan → capital or liability  

> Sort the accounts: asset, or capital/liability?

Groups: asset · capital or liability
- Equipment → **asset**
- Cash → **asset**
- Bank loan → **capital or liability**
- Stock → **asset**
- Bank → **asset**

Full working after a second miss:

> The right pairs are:  
> Equipment → asset  
> Cash → asset  
> Bank loan → capital or liability  
> Stock → asset  
> Bank → asset  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-10-kind` · Lesson 10 · matching, level 1

Prompt: Sort the accounts: expense or revenue?

Pairs (4 shown each time, sorted into groups):

- rent paid → **expense**
- salaries → **expense**
- electricity → **expense**
- purchases of goods → **expense**
- sales → **revenue**
- commission received → **revenue**
- rent received → **revenue**
- interest received → **revenue**


Three generated variants:

> Sort the accounts: expense or revenue?

Groups: expense · revenue
- purchases of goods → **expense**
- sales → **revenue**
- electricity → **expense**
- salaries → **expense**

Full working after a second miss:

> The right pairs are:  
> purchases of goods → expense  
> sales → revenue  
> electricity → expense  
> salaries → expense  

> Sort the accounts: expense or revenue?

Groups: expense · revenue
- salaries → **expense**
- sales → **revenue**
- commission received → **revenue**
- rent paid → **expense**

Full working after a second miss:

> The right pairs are:  
> salaries → expense  
> sales → revenue  
> commission received → revenue  
> rent paid → expense  

> Sort the accounts: expense or revenue?

Groups: expense · revenue
- sales → **revenue**
- rent paid → **expense**
- commission received → **revenue**
- purchases of goods → **expense**

Full working after a second miss:

> The right pairs are:  
> sales → revenue  
> rent paid → expense  
> commission received → revenue  
> purchases of goods → expense  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-11-kind` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is double entry? | recording each transaction as a debit in one account and an equal credit in another | recording each transaction twice in the same account · recording only cash · writing in two colours | Two different accounts. · All transactions. · Colour does not matter. | Every debit has a matching credit. |
| What is a weakness of single entry? | It is incomplete and errors are hard to find. | It is too complicated. · It records everything twice. · It needs a computer. | It is simple. · That is double entry. · It does not. | Single entry gives an incomplete picture. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is double entry?

- ◻️ writing in two colours  
  _↳ feedback if chosen: Colour does not matter._
- ◻️ recording each transaction twice in the same account  
  _↳ feedback if chosen: Two different accounts._
- ✅ recording each transaction as a debit in one account and an equal credit in another
- ◻️ recording only cash  
  _↳ feedback if chosen: All transactions._

Full working after a second miss:

> Every debit has a matching credit.  
> So the answer is “recording each transaction as a debit in one account and an equal credit in another”.  

> What is a weakness of single entry?

- ◻️ It is too complicated.  
  _↳ feedback if chosen: It is simple._
- ◻️ It records everything twice.  
  _↳ feedback if chosen: That is double entry._
- ◻️ It needs a computer.  
  _↳ feedback if chosen: It does not._
- ✅ It is incomplete and errors are hard to find.

Full working after a second miss:

> Single entry gives an incomplete picture.  
> So the answer is “It is incomplete and errors are hard to find.”.  

> What is double entry?

- ✅ recording each transaction as a debit in one account and an equal credit in another
- ◻️ writing in two colours  
  _↳ feedback if chosen: Colour does not matter._
- ◻️ recording each transaction twice in the same account  
  _↳ feedback if chosen: Two different accounts._
- ◻️ recording only cash  
  _↳ feedback if chosen: All transactions._

Full working after a second miss:

> Every debit has a matching credit.  
> So the answer is “recording each transaction as a debit in one account and an equal credit in another”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-11-pair` · Lesson 11 · multiple choice, level 1

Prompt: A cash sale of 60 000 FCFA. Which double entry is correct?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ debit Cash 60 000, credit Sales 60 000
- ❌ debit Sales 60 000, credit Cash 60 000  
  _↳ Cash receives (debit); Sales is the revenue (credit)._
- ❌ debit Cash 60 000 only  
  _↳ Double entry needs a credit too._
- ❌ credit Cash 60 000, credit Sales 60 000  
  _↳ One debit and one credit._


Three generated variants:

> A cash sale of 60 000 FCFA. Which double entry is correct?

- ◻️ debit Cash 60 000 only  
  _↳ feedback if chosen: Double entry needs a credit too._
- ◻️ debit Sales 60 000, credit Cash 60 000  
  _↳ feedback if chosen: Cash receives (debit); Sales is the revenue (credit)._
- ✅ debit Cash 60 000, credit Sales 60 000

Full working after a second miss:

> The true statement is “debit Cash 60 000, credit Sales 60 000”.  
> “debit Cash 60 000 only” is false: Double entry needs a credit too.  
> “debit Sales 60 000, credit Cash 60 000” is false: Cash receives (debit); Sales is the revenue (credit).  

> A cash sale of 60 000 FCFA. Which double entry is correct?

- ◻️ debit Sales 60 000, credit Cash 60 000  
  _↳ feedback if chosen: Cash receives (debit); Sales is the revenue (credit)._
- ◻️ credit Cash 60 000, credit Sales 60 000  
  _↳ feedback if chosen: One debit and one credit._
- ✅ debit Cash 60 000, credit Sales 60 000

Full working after a second miss:

> The true statement is “debit Cash 60 000, credit Sales 60 000”.  
> “debit Sales 60 000, credit Cash 60 000” is false: Cash receives (debit); Sales is the revenue (credit).  
> “credit Cash 60 000, credit Sales 60 000” is false: One debit and one credit.  

> A cash sale of 60 000 FCFA. Which double entry is correct?

- ◻️ debit Sales 60 000, credit Cash 60 000  
  _↳ feedback if chosen: Cash receives (debit); Sales is the revenue (credit)._
- ◻️ debit Cash 60 000 only  
  _↳ feedback if chosen: Double entry needs a credit too._
- ✅ debit Cash 60 000, credit Sales 60 000

Full working after a second miss:

> The true statement is “debit Cash 60 000, credit Sales 60 000”.  
> “debit Sales 60 000, credit Cash 60 000” is false: Cash receives (debit); Sales is the revenue (credit).  
> “debit Cash 60 000 only” is false: Double entry needs a credit too.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-11-total` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In double entry, what is always true for the whole ledger? | total debits = total credits | debits are always bigger · credits are always bigger · there are no credits | They are equal. · They are equal. · Credits are needed. | Each debit has an equal credit. |
| Equipment is bought by cheque for 400 000 FCFA. Which account is credited? | Bank | Equipment · Capital · Sales | Equipment is debited. · Not involved. · Not involved. | Money leaves the bank: credit Bank. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In double entry, what is always true for the whole ledger?

- ◻️ there are no credits  
  _↳ feedback if chosen: Credits are needed._
- ✅ total debits = total credits
- ◻️ credits are always bigger  
  _↳ feedback if chosen: They are equal._
- ◻️ debits are always bigger  
  _↳ feedback if chosen: They are equal._

Full working after a second miss:

> Each debit has an equal credit.  
> So the answer is “total debits = total credits”.  

> Equipment is bought by cheque for 400 000 FCFA. Which account is credited?

- ◻️ Equipment  
  _↳ feedback if chosen: Equipment is debited._
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ◻️ Capital  
  _↳ feedback if chosen: Not involved._
- ✅ Bank

Full working after a second miss:

> Money leaves the bank: credit Bank.  
> So the answer is “Bank”.  

> Equipment is bought by cheque for 400 000 FCFA. Which account is credited?

- ◻️ Capital  
  _↳ feedback if chosen: Not involved._
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ✅ Bank
- ◻️ Equipment  
  _↳ feedback if chosen: Equipment is debited._

Full working after a second miss:

> Money leaves the bank: credit Bank.  
> So the answer is “Bank”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-11-spot` · Lesson 11 · spot the error, level 3

Prompt: Which double entry is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Owner brings cash: debit Cash, credit Capital.
- ✅ Rent paid in cash: debit Rent, credit Cash.
- ✅ Goods bought on credit: debit Purchases, credit Creditors.
- ✅ Cash sale: debit Cash, credit Sales.
- ❌ Salaries paid in cash: debit Cash, credit Salaries.  
  _↳ Debit Salaries (expense), credit Cash._
- ❌ Loan received in the bank: debit Bank loan, credit Bank.  
  _↳ Debit Bank, credit Bank loan._
- ❌ Customer pays a debt by cheque: debit Debtors, credit Bank.  
  _↳ Debit Bank, credit Debtors._


Three generated variants:

> Which double entry is wrong?

- ◻️ Rent paid in cash: debit Rent, credit Cash.
- ◻️ Owner brings cash: debit Cash, credit Capital.
- ◻️ Goods bought on credit: debit Purchases, credit Creditors.
- ✅ Loan received in the bank: debit Bank loan, credit Bank.  
  _↳ explanation: Debit Bank, credit Bank loan._

Full working after a second miss:

> The wrong statement is “Loan received in the bank: debit Bank loan, credit Bank.”.  
> Debit Bank, credit Bank loan.  

> Which double entry is wrong?

- ◻️ Goods bought on credit: debit Purchases, credit Creditors.
- ◻️ Cash sale: debit Cash, credit Sales.
- ✅ Customer pays a debt by cheque: debit Debtors, credit Bank.  
  _↳ explanation: Debit Bank, credit Debtors._
- ◻️ Rent paid in cash: debit Rent, credit Cash.

Full working after a second miss:

> The wrong statement is “Customer pays a debt by cheque: debit Debtors, credit Bank.”.  
> Debit Bank, credit Debtors.  

> Which double entry is wrong?

- ✅ Salaries paid in cash: debit Cash, credit Salaries.  
  _↳ explanation: Debit Salaries (expense), credit Cash._
- ◻️ Owner brings cash: debit Cash, credit Capital.
- ◻️ Rent paid in cash: debit Rent, credit Cash.
- ◻️ Cash sale: debit Cash, credit Sales.

Full working after a second miss:

> The wrong statement is “Salaries paid in cash: debit Cash, credit Salaries.”.  
> Debit Salaries (expense), credit Cash.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-11-total-card` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In double entry, what is always true for the whole ledger? | total debits = total credits | debits are always bigger · credits are always bigger · there are no credits | They are equal. · They are equal. · Credits are needed. | Each debit has an equal credit. |
| Equipment is bought by cheque for 400 000 FCFA. Which account is credited? | Bank | Equipment · Capital · Sales | Equipment is debited. · Not involved. · Not involved. | Money leaves the bank: credit Bank. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In double entry, what is always true for the whole ledger?

- ✅ total debits = total credits
- ◻️ there are no credits  
  _↳ feedback if chosen: Credits are needed._
- ◻️ debits are always bigger  
  _↳ feedback if chosen: They are equal._
- ◻️ credits are always bigger  
  _↳ feedback if chosen: They are equal._

Full working after a second miss:

> Each debit has an equal credit.  
> So the answer is “total debits = total credits”.  

> In double entry, what is always true for the whole ledger?

- ◻️ debits are always bigger  
  _↳ feedback if chosen: They are equal._
- ◻️ credits are always bigger  
  _↳ feedback if chosen: They are equal._
- ✅ total debits = total credits
- ◻️ there are no credits  
  _↳ feedback if chosen: Credits are needed._

Full working after a second miss:

> Each debit has an equal credit.  
> So the answer is “total debits = total credits”.  

> Equipment is bought by cheque for 400 000 FCFA. Which account is credited?

- ◻️ Capital  
  _↳ feedback if chosen: Not involved._
- ◻️ Equipment  
  _↳ feedback if chosen: Equipment is debited._
- ◻️ Sales  
  _↳ feedback if chosen: Not involved._
- ✅ Bank

Full working after a second miss:

> Money leaves the bank: credit Bank.  
> So the answer is “Bank”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-12-recip` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Cash of 50 000 is received from Sales. What appears in the Sales account? | “Cash 50 000” on the credit side | “Sales 50 000” on the debit side · nothing · “Capital” on the debit side | Each entry names the other account. · Every transaction appears twice. · Capital is not involved. | The Sales account is credited, naming Cash. |
| What is the reciprocity of accounts? | each transaction appears as a debit in one account and a credit in another | each account has a twin with the same name · accounts are opened in pairs · debit and credit are the same | Not that. · Not that. · They are opposite sides. | Double entry makes accounts mirror each other. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Cash of 50 000 is received from Sales. What appears in the Sales account?

- ◻️ “Capital” on the debit side  
  _↳ feedback if chosen: Capital is not involved._
- ✅ “Cash 50 000” on the credit side
- ◻️ “Sales 50 000” on the debit side  
  _↳ feedback if chosen: Each entry names the other account._
- ◻️ nothing  
  _↳ feedback if chosen: Every transaction appears twice._

Full working after a second miss:

> The Sales account is credited, naming Cash.  
> So the answer is ““Cash 50 000” on the credit side”.  

> What is the reciprocity of accounts?

- ◻️ debit and credit are the same  
  _↳ feedback if chosen: They are opposite sides._
- ◻️ accounts are opened in pairs  
  _↳ feedback if chosen: Not that._
- ◻️ each account has a twin with the same name  
  _↳ feedback if chosen: Not that._
- ✅ each transaction appears as a debit in one account and a credit in another

Full working after a second miss:

> Double entry makes accounts mirror each other.  
> So the answer is “each transaction appears as a debit in one account and a credit in another”.  

> Cash of 50 000 is received from Sales. What appears in the Sales account?

- ✅ “Cash 50 000” on the credit side
- ◻️ nothing  
  _↳ feedback if chosen: Every transaction appears twice._
- ◻️ “Capital” on the debit side  
  _↳ feedback if chosen: Capital is not involved._
- ◻️ “Sales 50 000” on the debit side  
  _↳ feedback if chosen: Each entry names the other account._

Full working after a second miss:

> The Sales account is credited, naming Cash.  
> So the answer is ““Cash 50 000” on the credit side”.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-12-limit` · Lesson 12 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A trial balance lists all account balances.
- ✅ Its two totals should be equal.
- ✅ It helps prepare the balance sheet.
- ✅ Reciprocity comes from double entry.
- ❌ If a trial balance agrees, there can be no errors at all.  
  _↳ Some errors, such as an entry left out completely, are not shown._
- ❌ A trial balance lists only cash.  
  _↳ It lists all balances._
- ❌ Debit and credit columns are never equal.  
  _↳ They are equal when double entry is correct._


Three generated variants:

> Which statement is wrong?

- ◻️ It helps prepare the balance sheet.
- ✅ If a trial balance agrees, there can be no errors at all.  
  _↳ explanation: Some errors, such as an entry left out completely, are not shown._
- ◻️ A trial balance lists all account balances.
- ◻️ Its two totals should be equal.

Full working after a second miss:

> The wrong statement is “If a trial balance agrees, there can be no errors at all.”.  
> Some errors, such as an entry left out completely, are not shown.  

> Which statement is wrong?

- ◻️ Its two totals should be equal.
- ✅ Debit and credit columns are never equal.  
  _↳ explanation: They are equal when double entry is correct._
- ◻️ A trial balance lists all account balances.
- ◻️ It helps prepare the balance sheet.

Full working after a second miss:

> The wrong statement is “Debit and credit columns are never equal.”.  
> They are equal when double entry is correct.  

> Which statement is wrong?

- ✅ Debit and credit columns are never equal.  
  _↳ explanation: They are equal when double entry is correct._
- ◻️ A trial balance lists all account balances.
- ◻️ It helps prepare the balance sheet.
- ◻️ Reciprocity comes from double entry.

Full working after a second miss:

> The wrong statement is “Debit and credit columns are never equal.”.  
> They are equal when double entry is correct.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

### `a2-12-limit-card` · Lesson 12 · spot the error, level 1

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A trial balance lists all account balances.
- ✅ Its two totals should be equal.
- ✅ It helps prepare the balance sheet.
- ✅ Reciprocity comes from double entry.
- ❌ If a trial balance agrees, there can be no errors at all.  
  _↳ Some errors, such as an entry left out completely, are not shown._
- ❌ A trial balance lists only cash.  
  _↳ It lists all balances._
- ❌ Debit and credit columns are never equal.  
  _↳ They are equal when double entry is correct._


Three generated variants:

> Which statement is wrong?

- ✅ If a trial balance agrees, there can be no errors at all.  
  _↳ explanation: Some errors, such as an entry left out completely, are not shown._
- ◻️ It helps prepare the balance sheet.
- ◻️ A trial balance lists all account balances.
- ◻️ Reciprocity comes from double entry.

Full working after a second miss:

> The wrong statement is “If a trial balance agrees, there can be no errors at all.”.  
> Some errors, such as an entry left out completely, are not shown.  

> Which statement is wrong?

- ✅ A trial balance lists only cash.  
  _↳ explanation: It lists all balances._
- ◻️ Reciprocity comes from double entry.
- ◻️ Its two totals should be equal.
- ◻️ A trial balance lists all account balances.

Full working after a second miss:

> The wrong statement is “A trial balance lists only cash.”.  
> It lists all balances.  

> Which statement is wrong?

- ◻️ A trial balance lists all account balances.
- ◻️ It helps prepare the balance sheet.
- ✅ A trial balance lists only cash.  
  _↳ explanation: It lists all balances._
- ◻️ Reciprocity comes from double entry.

Full working after a second miss:

> The wrong statement is “A trial balance lists only cash.”.  
> It lists all balances.  

Sources: recording (Ledger (T) accounts; the functioning of balance sheet, expense and revenue accounts; balancing; single and double entry; the trial balance and the reciprocity of accounts)

