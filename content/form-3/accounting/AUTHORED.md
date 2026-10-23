# Accounting Form 3, Form Three Accounting: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f3-accounting`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `a3-1-ohada` | 1 | multiple choice, 1 | ohada |
| 2 | `a3-1-class` | 1 | multiple choice, 1 | ohada |
| 3 | `a3-1-double` | 1 | multiple choice, 2 | ohada |
| 4 | `a3-1-double-card` (card c3a1-3) | 1 | multiple choice, 1 | ohada |
| 5 | `a3-2-order` | 2 | ordering, 1 | ohada |
| 6 | `a3-2-post` | 2 | multiple choice, 2 | ohada |
| 7 | `a3-2-err` | 2 | multiple choice, 3 | ohada |
| 8 | `a3-3-entry` | 3 | multiple choice, 2 | vat |
| 9 | `a3-4-cap` | 4 | multiple choice, 1 | ohada-transactions |
| 10 | `a3-4-loan` | 4 | multiple choice, 1 | ohada-transactions |
| 11 | `a3-5-asset` | 5 | multiple choice, 1 | ohada-transactions |
| 12 | `a3-5-entry` | 5 | multiple choice, 1 | ohada-transactions |
| 13 | `a3-6-entry` | 6 | multiple choice, 1 | ohada-transactions |
| 14 | `a3-7-entry` | 7 | multiple choice, 1 | ohada-transactions |
| 15 | `a3-7-buyer` | 7 | multiple choice, 3 | ohada-transactions |
| 16 | `a3-8-entry` | 8 | multiple choice, 1 | ohada-transactions |
| 17 | `a3-8-why` | 8 | multiple choice, 3 | ohada-transactions |
| 18 | `a3-10-def` | 10 | multiple choice, 1 | ohada-transactions |
| 19 | `a3-10-entry` | 10 | multiple choice, 1 | ohada-transactions |
| 20 | `a3-10-days` | 10 | number, 3 | ohada-transactions |

### `a3-1-ohada` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is OHADA? | An organisation that harmonises business law, including accounting, in member African states | A bank in Douala · A tax paid on sales · A type of company | It is not a bank. · That is VAT. · Companies are SARL, SA and others. | Its uniform acts apply in all member states. |
| What is SYSCOHADA? | The OHADA accounting system and chart of accounts | A Cameroonian bank · A spreadsheet program · A customs form | It is not a bank. · It is a set of rules, not software. · It is not a customs document. | It sets out the accounts and how to keep them. |
| Where and when was the OHADA treaty signed? | Port Louis, 1993 | Yaoundé, 1960 · Paris, 2017 · Douala, 2000 | 1960 is Cameroon's independence. · 2017 is the revision of SYSCOHADA. · Not the treaty date. | Signed in Port Louis (Mauritius) in 1993. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is OHADA?

- ◻️ A bank in Douala  
  _↳ feedback if chosen: It is not a bank._
- ◻️ A tax paid on sales  
  _↳ feedback if chosen: That is VAT._
- ✅ An organisation that harmonises business law, including accounting, in member African states
- ◻️ A type of company  
  _↳ feedback if chosen: Companies are SARL, SA and others._

Full working after a second miss:

> Its uniform acts apply in all member states.  
> So the answer is An organisation that harmonises business law, including accounting, in member African states.  

> What is SYSCOHADA?

- ◻️ A Cameroonian bank  
  _↳ feedback if chosen: It is not a bank._
- ◻️ A spreadsheet program  
  _↳ feedback if chosen: It is a set of rules, not software._
- ◻️ A customs form  
  _↳ feedback if chosen: It is not a customs document._
- ✅ The OHADA accounting system and chart of accounts

Full working after a second miss:

> It sets out the accounts and how to keep them.  
> So the answer is The OHADA accounting system and chart of accounts.  

> What is SYSCOHADA?

- ◻️ A customs form  
  _↳ feedback if chosen: It is not a customs document._
- ◻️ A Cameroonian bank  
  _↳ feedback if chosen: It is not a bank._
- ◻️ A spreadsheet program  
  _↳ feedback if chosen: It is a set of rules, not software._
- ✅ The OHADA accounting system and chart of accounts

Full working after a second miss:

> It sets out the accounts and how to keep them.  
> So the answer is The OHADA accounting system and chart of accounts.  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-1-class` · Lesson 1 · multiple choice, level 1

Prompt: In which class is this account? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| 571 Cash | class 5 (treasury) | class 7 (income) · class 1 (equity) · class 6 (expenses) | Income accounts start with 7. · Equity starts with 1. · Expenses start with 6. | The first digit is 5. |
| 701 Sales of goods | class 7 (income) | class 6 (expenses) · class 4 (third parties) · class 2 (fixed assets) | Sales are income, not expenses. · Third parties start with 4. · Fixed assets start with 2. | The first digit is 7. |
| 245 Transport equipment | class 2 (fixed assets) | class 3 (stocks) · class 5 (treasury) · class 6 (expenses) | Stocks start with 3. · Treasury starts with 5. · Expenses start with 6. | A vehicle used for years is a fixed asset. |
| 401 Suppliers | class 4 (third parties) | class 1 (equity) · class 6 (expenses) · class 5 (treasury) | Equity starts with 1. · Expenses start with 6. · Treasury starts with 5. | Suppliers and customers are third parties. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In which class is this account? 701 Sales of goods

- ◻️ class 2 (fixed assets)  
  _↳ feedback if chosen: Fixed assets start with 2._
- ◻️ class 6 (expenses)  
  _↳ feedback if chosen: Sales are income, not expenses._
- ◻️ class 4 (third parties)  
  _↳ feedback if chosen: Third parties start with 4._
- ✅ class 7 (income)

Full working after a second miss:

> The first digit is 7.  
> So the answer is class 7 (income).  

> In which class is this account? 401 Suppliers

- ✅ class 4 (third parties)
- ◻️ class 5 (treasury)  
  _↳ feedback if chosen: Treasury starts with 5._
- ◻️ class 6 (expenses)  
  _↳ feedback if chosen: Expenses start with 6._
- ◻️ class 1 (equity)  
  _↳ feedback if chosen: Equity starts with 1._

Full working after a second miss:

> Suppliers and customers are third parties.  
> So the answer is class 4 (third parties).  

> In which class is this account? 701 Sales of goods

- ◻️ class 2 (fixed assets)  
  _↳ feedback if chosen: Fixed assets start with 2._
- ◻️ class 6 (expenses)  
  _↳ feedback if chosen: Sales are income, not expenses._
- ◻️ class 4 (third parties)  
  _↳ feedback if chosen: Third parties start with 4._
- ✅ class 7 (income)

Full working after a second miss:

> The first digit is 7.  
> So the answer is class 7 (income).  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-1-double` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does double entry mean? | Every transaction is recorded in at least two accounts, with equal debits and credits | Every transaction is written twice in the same account · Only cash transactions are recorded · Debits are always bigger than credits | It uses two (or more) different accounts. · All transactions are recorded. · Debits always equal credits. | Each transaction has a giving and a receiving side. |
| A trader sells goods for cash. Which accounts are affected? | 571 Cash (debit) and 701 Sales (credit) | 571 Cash only · 601 Purchases and 401 Suppliers · 101 Capital and 162 Loans | Double entry needs two accounts. · Those are for buying on credit. · Those are financing accounts. | Cash comes in; sales income is earned. |
| Which type of enterprise is owned by one person? | a sole trader | a public limited company (SA) · a partnership · a cooperative | An SA has many shareholders. · A partnership has two or more partners. · A cooperative has many members. | Many small shops are sole traders. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which type of enterprise is owned by one person?

- ✅ a sole trader
- ◻️ a cooperative  
  _↳ feedback if chosen: A cooperative has many members._
- ◻️ a public limited company (SA)  
  _↳ feedback if chosen: An SA has many shareholders._
- ◻️ a partnership  
  _↳ feedback if chosen: A partnership has two or more partners._

Full working after a second miss:

> Many small shops are sole traders.  
> So the answer is a sole trader.  

> A trader sells goods for cash. Which accounts are affected?

- ◻️ 571 Cash only  
  _↳ feedback if chosen: Double entry needs two accounts._
- ✅ 571 Cash (debit) and 701 Sales (credit)
- ◻️ 601 Purchases and 401 Suppliers  
  _↳ feedback if chosen: Those are for buying on credit._
- ◻️ 101 Capital and 162 Loans  
  _↳ feedback if chosen: Those are financing accounts._

Full working after a second miss:

> Cash comes in; sales income is earned.  
> So the answer is 571 Cash (debit) and 701 Sales (credit).  

> Which type of enterprise is owned by one person?

- ◻️ a partnership  
  _↳ feedback if chosen: A partnership has two or more partners._
- ◻️ a cooperative  
  _↳ feedback if chosen: A cooperative has many members._
- ✅ a sole trader
- ◻️ a public limited company (SA)  
  _↳ feedback if chosen: An SA has many shareholders._

Full working after a second miss:

> Many small shops are sole traders.  
> So the answer is a sole trader.  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-1-double-card` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does double entry mean? | Every transaction is recorded in at least two accounts, with equal debits and credits | Every transaction is written twice in the same account · Only cash transactions are recorded · Debits are always bigger than credits | It uses two (or more) different accounts. · All transactions are recorded. · Debits always equal credits. | Each transaction has a giving and a receiving side. |
| A trader sells goods for cash. Which accounts are affected? | 571 Cash (debit) and 701 Sales (credit) | 571 Cash only · 601 Purchases and 401 Suppliers · 101 Capital and 162 Loans | Double entry needs two accounts. · Those are for buying on credit. · Those are financing accounts. | Cash comes in; sales income is earned. |
| Which type of enterprise is owned by one person? | a sole trader | a public limited company (SA) · a partnership · a cooperative | An SA has many shareholders. · A partnership has two or more partners. · A cooperative has many members. | Many small shops are sole traders. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which type of enterprise is owned by one person?

- ◻️ a cooperative  
  _↳ feedback if chosen: A cooperative has many members._
- ✅ a sole trader
- ◻️ a public limited company (SA)  
  _↳ feedback if chosen: An SA has many shareholders._
- ◻️ a partnership  
  _↳ feedback if chosen: A partnership has two or more partners._

Full working after a second miss:

> Many small shops are sole traders.  
> So the answer is a sole trader.  

> What does double entry mean?

- ◻️ Every transaction is written twice in the same account  
  _↳ feedback if chosen: It uses two (or more) different accounts._
- ◻️ Only cash transactions are recorded  
  _↳ feedback if chosen: All transactions are recorded._
- ✅ Every transaction is recorded in at least two accounts, with equal debits and credits
- ◻️ Debits are always bigger than credits  
  _↳ feedback if chosen: Debits always equal credits._

Full working after a second miss:

> Each transaction has a giving and a receiving side.  
> So the answer is Every transaction is recorded in at least two accounts, with equal debits and credits.  

> A trader sells goods for cash. Which accounts are affected?

- ◻️ 601 Purchases and 401 Suppliers  
  _↳ feedback if chosen: Those are for buying on credit._
- ◻️ 101 Capital and 162 Loans  
  _↳ feedback if chosen: Those are financing accounts._
- ✅ 571 Cash (debit) and 701 Sales (credit)
- ◻️ 571 Cash only  
  _↳ feedback if chosen: Double entry needs two accounts._

Full working after a second miss:

> Cash comes in; sales income is earned.  
> So the answer is 571 Cash (debit) and 701 Sales (credit).  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-2-order` · Lesson 2 · ordering, level 1

Prompt: Put the stages of the accounting cycle in order.

Items in the right order:

1. Source documents
2. Journal
3. Ledger
4. Trial balance
5. Financial statements


Three generated variants:

> Put the stages of the accounting cycle in order.

Shown as: Journal · Trial balance · Source documents · Ledger · Financial statements
Correct order: Source documents → Journal → Ledger → Trial balance → Financial statements

Hint (draft): Documents first, statements last.

Full working after a second miss:

> The correct order is: Source documents → Journal → Ledger → Trial balance → Financial statements.  

> Put the stages of the accounting cycle in order.

Shown as: Journal · Financial statements · Trial balance · Ledger · Source documents
Correct order: Source documents → Journal → Ledger → Trial balance → Financial statements

Hint (draft): Documents first, statements last.

Full working after a second miss:

> The correct order is: Source documents → Journal → Ledger → Trial balance → Financial statements.  

> Put the stages of the accounting cycle in order.

Shown as: Source documents · Trial balance · Financial statements · Ledger · Journal
Correct order: Source documents → Journal → Ledger → Trial balance → Financial statements

Hint (draft): Documents first, statements last.

Full working after a second miss:

> The correct order is: Source documents → Journal → Ledger → Trial balance → Financial statements.  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-2-post` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is posting? | Transferring journal amounts to the ledger accounts | Sending letters to customers · Adding up the trial balance · Paying suppliers | That is correspondence. · That comes after posting. · That is a transaction, not posting. | Each journal line goes to its ledger account. |
| A journal entry debits 571 Cash and credits 701 Sales with 25 000 FCFA. How is it posted? | 25 000 on the debit side of Cash and on the credit side of Sales | 25 000 on the credit side of Cash · 50 000 in Cash only · 25 000 on the debit side of Sales | Cash is debited. · Each account gets the amount once, on its own side. · Sales is credited. | Post each amount to the same side as in the journal. |
| Which document is the starting point of the accounting cycle? | source documents such as invoices and receipts | the trial balance · the balance sheet · the ledger | That comes later. · That comes at the end. · The ledger comes after the journal. | Every entry must be supported by a document. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which document is the starting point of the accounting cycle?

- ◻️ the balance sheet  
  _↳ feedback if chosen: That comes at the end._
- ✅ source documents such as invoices and receipts
- ◻️ the ledger  
  _↳ feedback if chosen: The ledger comes after the journal._
- ◻️ the trial balance  
  _↳ feedback if chosen: That comes later._

Full working after a second miss:

> Every entry must be supported by a document.  
> So the answer is source documents such as invoices and receipts.  

> What is posting?

- ◻️ Adding up the trial balance  
  _↳ feedback if chosen: That comes after posting._
- ◻️ Sending letters to customers  
  _↳ feedback if chosen: That is correspondence._
- ◻️ Paying suppliers  
  _↳ feedback if chosen: That is a transaction, not posting._
- ✅ Transferring journal amounts to the ledger accounts

Full working after a second miss:

> Each journal line goes to its ledger account.  
> So the answer is Transferring journal amounts to the ledger accounts.  

> A journal entry debits 571 Cash and credits 701 Sales with 25 000 FCFA. How is it posted?

- ◻️ 50 000 in Cash only  
  _↳ feedback if chosen: Each account gets the amount once, on its own side._
- ◻️ 25 000 on the debit side of Sales  
  _↳ feedback if chosen: Sales is credited._
- ✅ 25 000 on the debit side of Cash and on the credit side of Sales
- ◻️ 25 000 on the credit side of Cash  
  _↳ feedback if chosen: Cash is debited._

Full working after a second miss:

> Post each amount to the same side as in the journal.  
> So the answer is 25 000 on the debit side of Cash and on the credit side of Sales.  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-2-err` · Lesson 2 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A trial balance agrees. Does that prove there are no errors? | No: some errors (such as a wrong account or a missing entry) do not affect the totals | Yes, always · Yes, if it is typed · No, a trial balance never agrees | Some errors are hidden. · Typing does not matter. · A correct trial balance agrees. | Errors of omission or of principle leave the totals equal. |
| Rent of 50 000 FCFA was paid in cash but posted only to the Rent account. What happens to the trial balance? | It does not agree: debits exceed credits by 50 000 | It agrees · Credits exceed debits by 50 000 · It doubles | One side is missing. · The debit was posted, the credit was not. · Nothing doubles. | Only one side was posted. |
| Why do debit and credit totals agree in a correct trial balance? | Every transaction was recorded with equal debits and credits | The accountant chooses the totals · Because Cash is always the largest account · Because there are always ten accounts | Totals come from the entries. · Not related. · Any number of accounts. | Double entry keeps the books in balance. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Rent of 50 000 FCFA was paid in cash but posted only to the Rent account. What happens to the trial balance?

- ◻️ It doubles  
  _↳ feedback if chosen: Nothing doubles._
- ◻️ Credits exceed debits by 50 000  
  _↳ feedback if chosen: The debit was posted, the credit was not._
- ◻️ It agrees  
  _↳ feedback if chosen: One side is missing._
- ✅ It does not agree: debits exceed credits by 50 000

Full working after a second miss:

> Only one side was posted.  
> So the answer is It does not agree: debits exceed credits by 50 000.  

> A trial balance agrees. Does that prove there are no errors?

- ◻️ Yes, if it is typed  
  _↳ feedback if chosen: Typing does not matter._
- ✅ No: some errors (such as a wrong account or a missing entry) do not affect the totals
- ◻️ Yes, always  
  _↳ feedback if chosen: Some errors are hidden._
- ◻️ No, a trial balance never agrees  
  _↳ feedback if chosen: A correct trial balance agrees._

Full working after a second miss:

> Errors of omission or of principle leave the totals equal.  
> So the answer is No: some errors (such as a wrong account or a missing entry) do not affect the totals.  

> Rent of 50 000 FCFA was paid in cash but posted only to the Rent account. What happens to the trial balance?

- ✅ It does not agree: debits exceed credits by 50 000
- ◻️ It doubles  
  _↳ feedback if chosen: Nothing doubles._
- ◻️ It agrees  
  _↳ feedback if chosen: One side is missing._
- ◻️ Credits exceed debits by 50 000  
  _↳ feedback if chosen: The debit was posted, the credit was not._

Full working after a second miss:

> Only one side was posted.  
> So the answer is It does not agree: debits exceed credits by 50 000.  

Sources: ohada (Form 3 Accounting syllabus, Term 1: brief OHADA history, chart of accounts, enterprises, double entry; journal, ledger and trial balance)

### `a3-3-entry` · Lesson 3 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In a credit sale, which account records the VAT charged to the customer? | 443 VAT invoiced (credit) | 445 VAT recoverable (debit) · 601 Purchases (debit) · 571 Cash (credit) | That is VAT on purchases. · Not a sale. · Cash is not involved in a credit sale. | VAT charged on sales is owed to the State. |
| In a credit purchase of goods, which account records the VAT paid to the supplier? | 445 VAT recoverable (debit) | 443 VAT invoiced (credit) · 701 Sales (credit) · 101 Capital (credit) | That is VAT on sales. · Not a sale. · Not a financing transaction. | The enterprise can deduct this VAT. |
| Which account is debited when goods are sold on credit for an amount including tax? | 411 Customers (with the TTC amount) | 701 Sales · 443 VAT invoiced · 401 Suppliers | Sales is credited with the HT amount. · VAT invoiced is credited. · Suppliers are for purchases. | The customer owes the full TTC amount. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In a credit purchase of goods, which account records the VAT paid to the supplier?

- ◻️ 701 Sales (credit)  
  _↳ feedback if chosen: Not a sale._
- ◻️ 101 Capital (credit)  
  _↳ feedback if chosen: Not a financing transaction._
- ✅ 445 VAT recoverable (debit)
- ◻️ 443 VAT invoiced (credit)  
  _↳ feedback if chosen: That is VAT on sales._

Full working after a second miss:

> The enterprise can deduct this VAT.  
> So the answer is 445 VAT recoverable (debit).  

> In a credit purchase of goods, which account records the VAT paid to the supplier?

- ◻️ 101 Capital (credit)  
  _↳ feedback if chosen: Not a financing transaction._
- ◻️ 443 VAT invoiced (credit)  
  _↳ feedback if chosen: That is VAT on sales._
- ✅ 445 VAT recoverable (debit)
- ◻️ 701 Sales (credit)  
  _↳ feedback if chosen: Not a sale._

Full working after a second miss:

> The enterprise can deduct this VAT.  
> So the answer is 445 VAT recoverable (debit).  

> In a credit purchase of goods, which account records the VAT paid to the supplier?

- ✅ 445 VAT recoverable (debit)
- ◻️ 443 VAT invoiced (credit)  
  _↳ feedback if chosen: That is VAT on sales._
- ◻️ 101 Capital (credit)  
  _↳ feedback if chosen: Not a financing transaction._
- ◻️ 701 Sales (credit)  
  _↳ feedback if chosen: Not a sale._

Full working after a second miss:

> The enterprise can deduct this VAT.  
> So the answer is 445 VAT recoverable (debit).  

Sources: vat (Form 3 Accounting syllabus, Term 1: calculation and accounting entries for VAT recoverable, VAT invoiced, VAT payable and VAT credit)

### `a3-4-cap` · Lesson 4 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The owner pays 1 000 000 FCFA into the business bank account. | Dr 521 Bank / Cr 101 Capital | Dr 101 Capital / Cr 521 Bank · Dr 521 Bank / Cr 162 Loans · Dr 571 Cash / Cr 701 Sales | Reversed: money comes into the bank, so Bank is debited. · It is the owner's money, not a loan. · It is not a sale. | Bank increases (debit); Capital increases (credit). |
| The owner brings 300 000 FCFA in cash to start the business. | Dr 571 Cash / Cr 101 Capital | Dr 101 Capital / Cr 571 Cash · Dr 571 Cash / Cr 162 Loans · Dr 601 Purchases / Cr 571 Cash | Reversed. · Not a loan. · Not a purchase. | Cash comes in from the owner. |
| The owner contributes a car worth 2 500 000 FCFA to the business. | Dr 245 Transport equipment / Cr 101 Capital | Dr 101 Capital / Cr 245 Transport equipment · Dr 521 Bank / Cr 101 Capital · Dr 245 Transport equipment / Cr 162 Loans | Reversed. · No money moves through the bank. · It is the owner's contribution, not a loan. | The asset received is debited; capital is credited. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? The owner brings 300 000 FCFA in cash to start the business.

- ✅ Dr 571 Cash / Cr 101 Capital
- ◻️ Dr 571 Cash / Cr 162 Loans  
  _↳ feedback if chosen: Not a loan._
- ◻️ Dr 601 Purchases / Cr 571 Cash  
  _↳ feedback if chosen: Not a purchase._
- ◻️ Dr 101 Capital / Cr 571 Cash  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> Cash comes in from the owner.  
> So the answer is Dr 571 Cash / Cr 101 Capital.  

> Which entry records this? The owner pays 1 000 000 FCFA into the business bank account.

- ◻️ Dr 571 Cash / Cr 701 Sales  
  _↳ feedback if chosen: It is not a sale._
- ◻️ Dr 101 Capital / Cr 521 Bank  
  _↳ feedback if chosen: Reversed: money comes into the bank, so Bank is debited._
- ✅ Dr 521 Bank / Cr 101 Capital
- ◻️ Dr 521 Bank / Cr 162 Loans  
  _↳ feedback if chosen: It is the owner's money, not a loan._

Full working after a second miss:

> Bank increases (debit); Capital increases (credit).  
> So the answer is Dr 521 Bank / Cr 101 Capital.  

> Which entry records this? The owner brings 300 000 FCFA in cash to start the business.

- ◻️ Dr 101 Capital / Cr 571 Cash  
  _↳ feedback if chosen: Reversed._
- ◻️ Dr 571 Cash / Cr 162 Loans  
  _↳ feedback if chosen: Not a loan._
- ◻️ Dr 601 Purchases / Cr 571 Cash  
  _↳ feedback if chosen: Not a purchase._
- ✅ Dr 571 Cash / Cr 101 Capital

Full working after a second miss:

> Cash comes in from the owner.  
> So the answer is Dr 571 Cash / Cr 101 Capital.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-4-loan` · Lesson 4 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The business receives a bank loan of 5 000 000 FCFA into its account. | Dr 521 Bank / Cr 162 Loans | Dr 162 Loans / Cr 521 Bank · Dr 521 Bank / Cr 101 Capital · Dr 671 Interest / Cr 521 Bank | That is a repayment. · A loan is not the owner's capital. · Interest is an expense paid later. | Bank increases; the debt (Loans) increases. |
| The business repays 500 000 FCFA of its loan by bank transfer. | Dr 162 Loans / Cr 521 Bank | Dr 521 Bank / Cr 162 Loans · Dr 101 Capital / Cr 521 Bank · Dr 162 Loans / Cr 101 Capital | That is receiving a loan. · Capital is not repaid here. · The money leaves the bank. | The debt falls (debit Loans); Bank falls (credit). |
| The business pays 60 000 FCFA interest on its loan by bank. | Dr 671 Interest / Cr 521 Bank | Dr 162 Loans / Cr 521 Bank · Dr 521 Bank / Cr 671 Interest · Dr 671 Interest / Cr 101 Capital | Interest does not reduce the loan itself. · Reversed. · It is paid from the bank. | Interest is an expense (class 6). |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? The business repays 500 000 FCFA of its loan by bank transfer.

- ◻️ Dr 521 Bank / Cr 162 Loans  
  _↳ feedback if chosen: That is receiving a loan._
- ✅ Dr 162 Loans / Cr 521 Bank
- ◻️ Dr 162 Loans / Cr 101 Capital  
  _↳ feedback if chosen: The money leaves the bank._
- ◻️ Dr 101 Capital / Cr 521 Bank  
  _↳ feedback if chosen: Capital is not repaid here._

Full working after a second miss:

> The debt falls (debit Loans); Bank falls (credit).  
> So the answer is Dr 162 Loans / Cr 521 Bank.  

> Which entry records this? The business pays 60 000 FCFA interest on its loan by bank.

- ◻️ Dr 521 Bank / Cr 671 Interest  
  _↳ feedback if chosen: Reversed._
- ✅ Dr 671 Interest / Cr 521 Bank
- ◻️ Dr 162 Loans / Cr 521 Bank  
  _↳ feedback if chosen: Interest does not reduce the loan itself._
- ◻️ Dr 671 Interest / Cr 101 Capital  
  _↳ feedback if chosen: It is paid from the bank._

Full working after a second miss:

> Interest is an expense (class 6).  
> So the answer is Dr 671 Interest / Cr 521 Bank.  

> Which entry records this? The business repays 500 000 FCFA of its loan by bank transfer.

- ◻️ Dr 101 Capital / Cr 521 Bank  
  _↳ feedback if chosen: Capital is not repaid here._
- ✅ Dr 162 Loans / Cr 521 Bank
- ◻️ Dr 521 Bank / Cr 162 Loans  
  _↳ feedback if chosen: That is receiving a loan._
- ◻️ Dr 162 Loans / Cr 101 Capital  
  _↳ feedback if chosen: The money leaves the bank._

Full working after a second miss:

> The debt falls (debit Loans); Bank falls (credit).  
> So the answer is Dr 162 Loans / Cr 521 Bank.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-5-asset` · Lesson 5 · multiple choice, level 1

Prompt: Is this a fixed asset? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A photocopier bought for the office, to be used for five years | Yes: office equipment (class 2) | No: it is an expense of the month · No: it is stock for sale · No: it is treasury | Items used for years are capitalised. · It is not bought to resell. · Treasury is cash and bank. | Long-term use makes it a fixed asset. |
| Reams of paper used up in a month | No: it is an expense (class 6) | Yes: office equipment · Yes: a building · Yes: transport equipment | Paper is consumed quickly. · Not a building. · Not a vehicle. | Consumables are expenses. |
| A lorry bought by a transport company | Yes: transport equipment (245) | No: it is a purchase of goods (601) · No: it is capital · No: it is a loan | The company uses it, it does not resell it. · Capital is the owner's contribution. · A loan is borrowed money. | Used for many years: fixed asset. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this a fixed asset? A lorry bought by a transport company

- ◻️ No: it is a purchase of goods (601)  
  _↳ feedback if chosen: The company uses it, it does not resell it._
- ◻️ No: it is capital  
  _↳ feedback if chosen: Capital is the owner's contribution._
- ◻️ No: it is a loan  
  _↳ feedback if chosen: A loan is borrowed money._
- ✅ Yes: transport equipment (245)

Full working after a second miss:

> Used for many years: fixed asset.  
> So the answer is Yes: transport equipment (245).  

> Is this a fixed asset? Reams of paper used up in a month

- ◻️ Yes: office equipment  
  _↳ feedback if chosen: Paper is consumed quickly._
- ◻️ Yes: a building  
  _↳ feedback if chosen: Not a building._
- ✅ No: it is an expense (class 6)
- ◻️ Yes: transport equipment  
  _↳ feedback if chosen: Not a vehicle._

Full working after a second miss:

> Consumables are expenses.  
> So the answer is No: it is an expense (class 6).  

> Is this a fixed asset? Reams of paper used up in a month

- ◻️ Yes: office equipment  
  _↳ feedback if chosen: Paper is consumed quickly._
- ✅ No: it is an expense (class 6)
- ◻️ Yes: a building  
  _↳ feedback if chosen: Not a building._
- ◻️ Yes: transport equipment  
  _↳ feedback if chosen: Not a vehicle._

Full working after a second miss:

> Consumables are expenses.  
> So the answer is No: it is an expense (class 6).  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-5-entry` · Lesson 5 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Office furniture is bought on credit for 500 000 FCFA HT (VAT 96 250). | Dr 244 Office furniture 500 000; Dr 4451 VAT 96 250 / Cr 481 Suppliers of fixed assets 596 250 | Dr 601 Purchases 596 250 / Cr 401 Suppliers 596 250 · Dr 481 Suppliers 596 250 / Cr 244 Office furniture 596 250 · Dr 244 Office furniture 596 250 / Cr 521 Bank 596 250 | Furniture used by the business is a fixed asset, not goods for resale. · Reversed. · It was bought on credit, and the VAT is recorded separately. | Asset HT and recoverable VAT debited; supplier of fixed assets credited TTC. |
| The supplier of fixed assets is paid 596 250 FCFA by cheque. | Dr 481 Suppliers of fixed assets / Cr 521 Bank | Dr 521 Bank / Cr 481 Suppliers of fixed assets · Dr 244 Office furniture / Cr 521 Bank · Dr 401 Suppliers / Cr 571 Cash | Reversed: money leaves the bank. · The asset was already recorded. · Paid by cheque from the bank, to the supplier of fixed assets. | The debt falls; the bank falls. |
| A computer is bought and paid at once by bank: 800 000 FCFA HT, VAT 154 000. | Dr 2183 Computer equipment 800 000; Dr 4451 VAT 154 000 / Cr 521 Bank 954 000 | Dr 601 Purchases 954 000 / Cr 521 Bank 954 000 · Dr 2183 Computer equipment 954 000 / Cr 481 Suppliers 954 000 · Dr 521 Bank 954 000 / Cr 2183 Computer equipment 954 000 | A computer for use is a fixed asset. · It was paid at once by bank, and VAT is separate. · Reversed. | Paid immediately: credit Bank. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? A computer is bought and paid at once by bank: 800 000 FCFA HT, VAT 154 000.

- ◻️ Dr 2183 Computer equipment 954 000 / Cr 481 Suppliers 954 000  
  _↳ feedback if chosen: It was paid at once by bank, and VAT is separate._
- ✅ Dr 2183 Computer equipment 800 000; Dr 4451 VAT 154 000 / Cr 521 Bank 954 000
- ◻️ Dr 601 Purchases 954 000 / Cr 521 Bank 954 000  
  _↳ feedback if chosen: A computer for use is a fixed asset._
- ◻️ Dr 521 Bank 954 000 / Cr 2183 Computer equipment 954 000  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> Paid immediately: credit Bank.  
> So the answer is Dr 2183 Computer equipment 800 000; Dr 4451 VAT 154 000 / Cr 521 Bank 954 000.  

> Which entry records this? Office furniture is bought on credit for 500 000 FCFA HT (VAT 96 250).

- ◻️ Dr 601 Purchases 596 250 / Cr 401 Suppliers 596 250  
  _↳ feedback if chosen: Furniture used by the business is a fixed asset, not goods for resale._
- ◻️ Dr 244 Office furniture 596 250 / Cr 521 Bank 596 250  
  _↳ feedback if chosen: It was bought on credit, and the VAT is recorded separately._
- ◻️ Dr 481 Suppliers 596 250 / Cr 244 Office furniture 596 250  
  _↳ feedback if chosen: Reversed._
- ✅ Dr 244 Office furniture 500 000; Dr 4451 VAT 96 250 / Cr 481 Suppliers of fixed assets 596 250

Full working after a second miss:

> Asset HT and recoverable VAT debited; supplier of fixed assets credited TTC.  
> So the answer is Dr 244 Office furniture 500 000; Dr 4451 VAT 96 250 / Cr 481 Suppliers of fixed assets 596 250.  

> Which entry records this? The supplier of fixed assets is paid 596 250 FCFA by cheque.

- ◻️ Dr 401 Suppliers / Cr 571 Cash  
  _↳ feedback if chosen: Paid by cheque from the bank, to the supplier of fixed assets._
- ◻️ Dr 244 Office furniture / Cr 521 Bank  
  _↳ feedback if chosen: The asset was already recorded._
- ◻️ Dr 521 Bank / Cr 481 Suppliers of fixed assets  
  _↳ feedback if chosen: Reversed: money leaves the bank._
- ✅ Dr 481 Suppliers of fixed assets / Cr 521 Bank

Full working after a second miss:

> The debt falls; the bank falls.  
> So the answer is Dr 481 Suppliers of fixed assets / Cr 521 Bank.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-6-entry` · Lesson 6 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Goods are bought on credit for 100 000 FCFA HT (VAT 19 250). | Dr 601 Purchases 100 000; Dr 445 VAT recoverable 19 250 / Cr 401 Suppliers 119 250 | Dr 401 Suppliers 119 250 / Cr 601 Purchases 119 250 · Dr 601 Purchases 119 250 / Cr 571 Cash 119 250 · Dr 411 Customers 119 250 / Cr 701 Sales 119 250 | Reversed. · It is on credit, and the VAT is recorded separately. · That is a sale. | Purchases and recoverable VAT debited; the supplier credited TTC. |
| Goods are sold on credit for 200 000 FCFA HT (VAT 38 500). | Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500 | Dr 701 Sales 238 500 / Cr 411 Customers 238 500 · Dr 571 Cash 238 500 / Cr 701 Sales 238 500 · Dr 411 Customers 200 000 / Cr 701 Sales 200 000 | Reversed. · It is a credit sale, and VAT must be shown separately. · The VAT is missing. | The customer owes the TTC amount. |
| Goods are sold for cash: 50 000 FCFA HT (VAT 9 625). | Dr 571 Cash 59 625 / Cr 701 Sales 50 000; Cr 443 VAT invoiced 9 625 | Dr 411 Customers 59 625 / Cr 701 Sales 59 625 · Dr 601 Purchases 59 625 / Cr 571 Cash 59 625 · Dr 571 Cash 50 000 / Cr 701 Sales 50 000 | It is a cash sale, not on credit. · That is a purchase. · The VAT collected must be recorded. | Cash comes in for the full TTC. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? Goods are sold on credit for 200 000 FCFA HT (VAT 38 500).

- ◻️ Dr 701 Sales 238 500 / Cr 411 Customers 238 500  
  _↳ feedback if chosen: Reversed._
- ◻️ Dr 411 Customers 200 000 / Cr 701 Sales 200 000  
  _↳ feedback if chosen: The VAT is missing._
- ✅ Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500
- ◻️ Dr 571 Cash 238 500 / Cr 701 Sales 238 500  
  _↳ feedback if chosen: It is a credit sale, and VAT must be shown separately._

Full working after a second miss:

> The customer owes the TTC amount.  
> So the answer is Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500.  

> Which entry records this? Goods are sold on credit for 200 000 FCFA HT (VAT 38 500).

- ✅ Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500
- ◻️ Dr 411 Customers 200 000 / Cr 701 Sales 200 000  
  _↳ feedback if chosen: The VAT is missing._
- ◻️ Dr 571 Cash 238 500 / Cr 701 Sales 238 500  
  _↳ feedback if chosen: It is a credit sale, and VAT must be shown separately._
- ◻️ Dr 701 Sales 238 500 / Cr 411 Customers 238 500  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> The customer owes the TTC amount.  
> So the answer is Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500.  

> Which entry records this? Goods are bought on credit for 100 000 FCFA HT (VAT 19 250).

- ◻️ Dr 411 Customers 119 250 / Cr 701 Sales 119 250  
  _↳ feedback if chosen: That is a sale._
- ◻️ Dr 401 Suppliers 119 250 / Cr 601 Purchases 119 250  
  _↳ feedback if chosen: Reversed._
- ◻️ Dr 601 Purchases 119 250 / Cr 571 Cash 119 250  
  _↳ feedback if chosen: It is on credit, and the VAT is recorded separately._
- ✅ Dr 601 Purchases 100 000; Dr 445 VAT recoverable 19 250 / Cr 401 Suppliers 119 250

Full working after a second miss:

> Purchases and recoverable VAT debited; the supplier credited TTC.  
> So the answer is Dr 601 Purchases 100 000; Dr 445 VAT recoverable 19 250 / Cr 401 Suppliers 119 250.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-7-entry` · Lesson 7 · multiple choice, level 1

Prompt: Which entry does the SELLER make? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Deposits of 10 000 FCFA are charged to a customer for crates delivered. | Dr 411 Customers / Cr 4194 Customers, consigned containers | Dr 4194 / Cr 411 · Dr 411 / Cr 701 Sales · Dr 4094 / Cr 401 | Reversed: that is the refund. · Deposits are not sales income. · Those are the buyer's accounts. | The deposit is a debt to the customer until the crates come back. |
| The customer returns the crates and the 10 000 FCFA deposit is credited back to his account. | Dr 4194 Customers, consigned containers / Cr 411 Customers | Dr 411 / Cr 4194 · Dr 701 Sales / Cr 411 · Dr 4194 / Cr 701 Sales | That charges the deposit. · Sales were not involved. · The deposit is refunded, not sold. | The debt to the customer is cancelled. |
| Cash is refunded to a customer who brings back crates worth 6 000 FCFA in deposits. | Dr 4194 Customers, consigned containers / Cr 571 Cash | Dr 571 Cash / Cr 4194 · Dr 601 Purchases / Cr 571 Cash · Dr 4194 / Cr 701 Sales | Cash goes out, so Cash is credited. · No purchase of goods. · The deposit is refunded, not sold. | Refund in cash cancels the deposit debt. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry does the SELLER make? Cash is refunded to a customer who brings back crates worth 6 000 FCFA in deposits.

- ◻️ Dr 601 Purchases / Cr 571 Cash  
  _↳ feedback if chosen: No purchase of goods._
- ✅ Dr 4194 Customers, consigned containers / Cr 571 Cash
- ◻️ Dr 571 Cash / Cr 4194  
  _↳ feedback if chosen: Cash goes out, so Cash is credited._
- ◻️ Dr 4194 / Cr 701 Sales  
  _↳ feedback if chosen: The deposit is refunded, not sold._

Full working after a second miss:

> Refund in cash cancels the deposit debt.  
> So the answer is Dr 4194 Customers, consigned containers / Cr 571 Cash.  

> Which entry does the SELLER make? Deposits of 10 000 FCFA are charged to a customer for crates delivered.

- ✅ Dr 411 Customers / Cr 4194 Customers, consigned containers
- ◻️ Dr 411 / Cr 701 Sales  
  _↳ feedback if chosen: Deposits are not sales income._
- ◻️ Dr 4194 / Cr 411  
  _↳ feedback if chosen: Reversed: that is the refund._
- ◻️ Dr 4094 / Cr 401  
  _↳ feedback if chosen: Those are the buyer's accounts._

Full working after a second miss:

> The deposit is a debt to the customer until the crates come back.  
> So the answer is Dr 411 Customers / Cr 4194 Customers, consigned containers.  

> Which entry does the SELLER make? The customer returns the crates and the 10 000 FCFA deposit is credited back to his account.

- ◻️ Dr 4194 / Cr 701 Sales  
  _↳ feedback if chosen: The deposit is refunded, not sold._
- ✅ Dr 4194 Customers, consigned containers / Cr 411 Customers
- ◻️ Dr 701 Sales / Cr 411  
  _↳ feedback if chosen: Sales were not involved._
- ◻️ Dr 411 / Cr 4194  
  _↳ feedback if chosen: That charges the deposit._

Full working after a second miss:

> The debt to the customer is cancelled.  
> So the answer is Dr 4194 Customers, consigned containers / Cr 411 Customers.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-7-buyer` · Lesson 7 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which account does the BUYER debit when paying a deposit on containers to be returned? | 4094 Suppliers, containers to be returned | 4194 Customers, consigned containers · 601 Purchases of goods · 701 Sales | That is the seller's account. · The deposit is not a purchase of goods. · The buyer is not selling. | The supplier owes the buyer the deposit back. |
| Why is no VAT charged on the deposit for returnable crates? | The deposit is refundable, not a sale of the crates | Crates are always free · VAT is only on services · Deposits are illegal | The customer pays a deposit. · VAT applies to goods too. · Deposits are normal. | Only if the crates are kept do they become a sale. |
| A customer keeps 5 crates instead of returning them. How are they treated? | As a sale of containers to the customer | As a loan · As capital · They are ignored | Not a loan. · Not capital. · They must be accounted for. | Unreturned containers are treated as sold (or bought). |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is no VAT charged on the deposit for returnable crates?

- ◻️ Deposits are illegal  
  _↳ feedback if chosen: Deposits are normal._
- ◻️ VAT is only on services  
  _↳ feedback if chosen: VAT applies to goods too._
- ✅ The deposit is refundable, not a sale of the crates
- ◻️ Crates are always free  
  _↳ feedback if chosen: The customer pays a deposit._

Full working after a second miss:

> Only if the crates are kept do they become a sale.  
> So the answer is The deposit is refundable, not a sale of the crates.  

> A customer keeps 5 crates instead of returning them. How are they treated?

- ◻️ They are ignored  
  _↳ feedback if chosen: They must be accounted for._
- ◻️ As a loan  
  _↳ feedback if chosen: Not a loan._
- ◻️ As capital  
  _↳ feedback if chosen: Not capital._
- ✅ As a sale of containers to the customer

Full working after a second miss:

> Unreturned containers are treated as sold (or bought).  
> So the answer is As a sale of containers to the customer.  

> A customer keeps 5 crates instead of returning them. How are they treated?

- ✅ As a sale of containers to the customer
- ◻️ They are ignored  
  _↳ feedback if chosen: They must be accounted for._
- ◻️ As a loan  
  _↳ feedback if chosen: Not a loan._
- ◻️ As capital  
  _↳ feedback if chosen: Not capital._

Full working after a second miss:

> Unreturned containers are treated as sold (or bought).  
> So the answer is As a sale of containers to the customer.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-8-entry` · Lesson 8 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A customer pays 150 000 FCFA by cheque, paid into the bank. | Dr 521 Bank / Cr 411 Customers | Dr 411 Customers / Cr 521 Bank · Dr 521 Bank / Cr 701 Sales · Dr 571 Cash / Cr 401 Suppliers | Reversed. · The sale was already recorded; now the debt is settled. · Not cash and not a supplier. | Bank increases; the customer owes less. |
| The business pays a supplier 90 000 FCFA by bank transfer. | Dr 401 Suppliers / Cr 521 Bank | Dr 521 Bank / Cr 401 Suppliers · Dr 601 Purchases / Cr 521 Bank · Dr 401 Suppliers / Cr 701 Sales | Reversed. · The purchase was already recorded; now the debt is paid. · No sale. | The debt falls; the bank falls. |
| 200 000 FCFA cash is paid into the bank. | Dr 521 Bank / Cr 571 Cash | Dr 571 Cash / Cr 521 Bank · Dr 521 Bank / Cr 101 Capital · Dr 521 Bank / Cr 701 Sales | That is withdrawing cash from the bank. · It is not new capital. · It is not a sale. | Money moves from the till to the bank. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? 200 000 FCFA cash is paid into the bank.

- ◻️ Dr 571 Cash / Cr 521 Bank  
  _↳ feedback if chosen: That is withdrawing cash from the bank._
- ◻️ Dr 521 Bank / Cr 101 Capital  
  _↳ feedback if chosen: It is not new capital._
- ◻️ Dr 521 Bank / Cr 701 Sales  
  _↳ feedback if chosen: It is not a sale._
- ✅ Dr 521 Bank / Cr 571 Cash

Full working after a second miss:

> Money moves from the till to the bank.  
> So the answer is Dr 521 Bank / Cr 571 Cash.  

> Which entry records this? The business pays a supplier 90 000 FCFA by bank transfer.

- ✅ Dr 401 Suppliers / Cr 521 Bank
- ◻️ Dr 401 Suppliers / Cr 701 Sales  
  _↳ feedback if chosen: No sale._
- ◻️ Dr 601 Purchases / Cr 521 Bank  
  _↳ feedback if chosen: The purchase was already recorded; now the debt is paid._
- ◻️ Dr 521 Bank / Cr 401 Suppliers  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> The debt falls; the bank falls.  
> So the answer is Dr 401 Suppliers / Cr 521 Bank.  

> Which entry records this? 200 000 FCFA cash is paid into the bank.

- ◻️ Dr 521 Bank / Cr 101 Capital  
  _↳ feedback if chosen: It is not new capital._
- ◻️ Dr 521 Bank / Cr 701 Sales  
  _↳ feedback if chosen: It is not a sale._
- ◻️ Dr 571 Cash / Cr 521 Bank  
  _↳ feedback if chosen: That is withdrawing cash from the bank._
- ✅ Dr 521 Bank / Cr 571 Cash

Full working after a second miss:

> Money moves from the till to the bank.  
> So the answer is Dr 521 Bank / Cr 571 Cash.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-8-why` · Lesson 8 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why can the cash account never have a credit balance? | You cannot pay out more cash than is in the till | Cash is always a liability · Cash is in class 7 · Credits are not allowed in accounting | Cash is an asset. · Cash is in class 5. · Credits are normal. | A credit balance on Cash means an error. |
| Why do sellers offer cash discounts? | To encourage customers to pay early | To increase VAT · To reduce their bank balance · Because the law requires it | Discounts reduce the amount. · They receive money sooner. · It is a business choice. | Early payment improves the seller's cash flow. |
| A cheque from a customer bounces (is unpaid). What should happen in the accounts? | The entry is reversed: Dr 411 Customers / Cr 521 Bank | Nothing changes · Dr 521 Bank / Cr 411 Customers again · Dr 701 Sales / Cr 411 | The bank did not receive the money. · That records it as received again. · Sales are not changed. | The customer still owes the money. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A cheque from a customer bounces (is unpaid). What should happen in the accounts?

- ◻️ Dr 701 Sales / Cr 411  
  _↳ feedback if chosen: Sales are not changed._
- ✅ The entry is reversed: Dr 411 Customers / Cr 521 Bank
- ◻️ Nothing changes  
  _↳ feedback if chosen: The bank did not receive the money._
- ◻️ Dr 521 Bank / Cr 411 Customers again  
  _↳ feedback if chosen: That records it as received again._

Full working after a second miss:

> The customer still owes the money.  
> So the answer is The entry is reversed: Dr 411 Customers / Cr 521 Bank.  

> Why can the cash account never have a credit balance?

- ◻️ Credits are not allowed in accounting  
  _↳ feedback if chosen: Credits are normal._
- ◻️ Cash is in class 7  
  _↳ feedback if chosen: Cash is in class 5._
- ✅ You cannot pay out more cash than is in the till
- ◻️ Cash is always a liability  
  _↳ feedback if chosen: Cash is an asset._

Full working after a second miss:

> A credit balance on Cash means an error.  
> So the answer is You cannot pay out more cash than is in the till.  

> Why can the cash account never have a credit balance?

- ✅ You cannot pay out more cash than is in the till
- ◻️ Cash is always a liability  
  _↳ feedback if chosen: Cash is an asset._
- ◻️ Cash is in class 7  
  _↳ feedback if chosen: Cash is in class 5._
- ◻️ Credits are not allowed in accounting  
  _↳ feedback if chosen: Credits are normal._

Full working after a second miss:

> A credit balance on Cash means an error.  
> So the answer is You cannot pay out more cash than is in the till.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-10-def` · Lesson 10 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is a trade bill? | A written promise or order to pay a sum on a fixed date | A receipt for cash already paid · A list of prices · A bank statement | It is about a future payment. · Not a price list. · Not a bank statement. | Bills of exchange and promissory notes are trade bills. |
| What is the maturity date of a bill? | the date on which it must be paid | the date it was printed · the date the goods were made · the owner's birthday | Printing date is not relevant. · Not related. · Not related. | The bill is payable on its due date. |
| Which is an advantage of a trade bill for the seller? | It is legal proof of the debt and can be discounted at a bank for cash | The customer never has to pay · It removes VAT · It is a sale of the business | The customer must pay at maturity. · VAT is not affected. · Not related. | It gives security and access to cash. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the maturity date of a bill?

- ◻️ the date it was printed  
  _↳ feedback if chosen: Printing date is not relevant._
- ◻️ the owner's birthday  
  _↳ feedback if chosen: Not related._
- ✅ the date on which it must be paid
- ◻️ the date the goods were made  
  _↳ feedback if chosen: Not related._

Full working after a second miss:

> The bill is payable on its due date.  
> So the answer is the date on which it must be paid.  

> Which is an advantage of a trade bill for the seller?

- ◻️ The customer never has to pay  
  _↳ feedback if chosen: The customer must pay at maturity._
- ✅ It is legal proof of the debt and can be discounted at a bank for cash
- ◻️ It is a sale of the business  
  _↳ feedback if chosen: Not related._
- ◻️ It removes VAT  
  _↳ feedback if chosen: VAT is not affected._

Full working after a second miss:

> It gives security and access to cash.  
> So the answer is It is legal proof of the debt and can be discounted at a bank for cash.  

> What is the maturity date of a bill?

- ✅ the date on which it must be paid
- ◻️ the date it was printed  
  _↳ feedback if chosen: Printing date is not relevant._
- ◻️ the owner's birthday  
  _↳ feedback if chosen: Not related._
- ◻️ the date the goods were made  
  _↳ feedback if chosen: Not related._

Full working after a second miss:

> The bill is payable on its due date.  
> So the answer is the date on which it must be paid.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-10-entry` · Lesson 10 · multiple choice, level 1

Prompt: Which entry records this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| SELLER: a customer accepts a bill of 300 000 FCFA for what he owes. | Dr 412 Customers, bills receivable / Cr 411 Customers | Dr 411 / Cr 412 · Dr 521 Bank / Cr 411 · Dr 401 / Cr 402 | Reversed. · No money has been received yet. · Those are the buyer's accounts. | The debt becomes a bill receivable. |
| SELLER: the bill of 300 000 FCFA is paid at maturity into the bank. | Dr 521 Bank / Cr 412 Customers, bills receivable | Dr 412 / Cr 521 · Dr 521 / Cr 411 · Dr 521 / Cr 701 Sales | Reversed. · The debt was already moved to 412. · Not a new sale. | The bill receivable is settled. |
| BUYER: the business accepts a bill of 250 000 FCFA drawn by its supplier. | Dr 401 Suppliers / Cr 402 Suppliers, bills payable | Dr 402 / Cr 401 · Dr 401 / Cr 521 Bank · Dr 412 / Cr 411 | Reversed. · Nothing is paid yet. · Those are the seller's accounts. | The debt becomes a bill payable. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which entry records this? SELLER: the bill of 300 000 FCFA is paid at maturity into the bank.

- ✅ Dr 521 Bank / Cr 412 Customers, bills receivable
- ◻️ Dr 521 / Cr 411  
  _↳ feedback if chosen: The debt was already moved to 412._
- ◻️ Dr 521 / Cr 701 Sales  
  _↳ feedback if chosen: Not a new sale._
- ◻️ Dr 412 / Cr 521  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> The bill receivable is settled.  
> So the answer is Dr 521 Bank / Cr 412 Customers, bills receivable.  

> Which entry records this? SELLER: the bill of 300 000 FCFA is paid at maturity into the bank.

- ◻️ Dr 521 / Cr 411  
  _↳ feedback if chosen: The debt was already moved to 412._
- ◻️ Dr 521 / Cr 701 Sales  
  _↳ feedback if chosen: Not a new sale._
- ✅ Dr 521 Bank / Cr 412 Customers, bills receivable
- ◻️ Dr 412 / Cr 521  
  _↳ feedback if chosen: Reversed._

Full working after a second miss:

> The bill receivable is settled.  
> So the answer is Dr 521 Bank / Cr 412 Customers, bills receivable.  

> Which entry records this? BUYER: the business accepts a bill of 250 000 FCFA drawn by its supplier.

- ◻️ Dr 412 / Cr 411  
  _↳ feedback if chosen: Those are the seller's accounts._
- ◻️ Dr 402 / Cr 401  
  _↳ feedback if chosen: Reversed._
- ◻️ Dr 401 / Cr 521 Bank  
  _↳ feedback if chosen: Nothing is paid yet._
- ✅ Dr 401 Suppliers / Cr 402 Suppliers, bills payable

Full working after a second miss:

> The debt becomes a bill payable.  
> So the answer is Dr 401 Suppliers / Cr 402 Suppliers, bills payable.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

### `a3-10-days` · Lesson 10 · number, level 3

Prompt: A bill dated 1 March (non-leap year) is payable {n} days later. Counting 1 January as day 1, what is the day number of its due date?
Right answer: `60 + n`

`n`: 30 · 45 · 60 · 90

- Feedback `nojan` (typed `n`): “Count the days in January and February too: {1} March is day {60}.”

Three generated variants:

> A bill dated 1 March (non-leap year) is payable 30 days later. Counting 1 January as day 1, what is the day number of its due date?

Answer: **90**
- Typed **30** (nojan) → “Count the days in January and February too: 1 March is day 60.”

Full working after a second miss:

> 1 March is day 60 of a non-leap year (31 + 28 + 1).  
> Due date = day 60 + 30 = day 90.  

> A bill dated 1 March (non-leap year) is payable 45 days later. Counting 1 January as day 1, what is the day number of its due date?

Answer: **105**
- Typed **45** (nojan) → “Count the days in January and February too: 1 March is day 60.”

Full working after a second miss:

> 1 March is day 60 of a non-leap year (31 + 28 + 1).  
> Due date = day 60 + 45 = day 105.  

> A bill dated 1 March (non-leap year) is payable 90 days later. Counting 1 January as day 1, what is the day number of its due date?

Answer: **150**
- Typed **90** (nojan) → “Count the days in January and February too: 1 March is day 60.”

Full working after a second miss:

> 1 March is day 60 of a non-leap year (31 + 28 + 1).  
> Due date = day 60 + 90 = day 150.  

Sources: ohada-transactions (Form 3 Accounting syllabus, Term 1: financing, investment, trading, commercial containers, cash settlement and trade bills transactions)

