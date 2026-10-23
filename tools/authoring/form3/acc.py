"""Form 3 Accounting, Term 1 (OHADA/SYSCOHADA), rows 1-8 and 10. Run: python tools/authoring/form3/acc.py
VAT in Cameroon: 19.25 % (as in Form 2). Amounts excluding tax are multiples of 4000 FCFA, so VAT is a whole number of francs."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "accounting", "accounting"
SRC = ["ohada"]
HT = {"k": {"int": [2, 50]}, "ht": {"expr": "k * 4000"}, "vat": {"expr": "k * 770"}}


def E(entry):
    """A journal entry or account written as fixed text in cards, Learn screens and worked examples."""
    return "{'" + entry + "'}"


# ---------------------------------------------------------------- 1. OHADA, chart of accounts, enterprises, double entry
L.lesson(D, S, 1, ("a3-1", "OHADA, the chart of accounts, enterprises and double entry"), [],
  "OHADA (Organisation for the Harmonisation of Business Law in Africa) was created by a treaty signed in Port Louis in 1993; Cameroon is a member. Its accounting law, SYSCOHADA (revised in 2017), gives member states the same accounting rules.\n"
  "The chart of accounts groups accounts in classes by their first digit:\n"
  "1 equity and long-term liabilities (101 Capital, 162 Loans) · 2 fixed assets (231 Buildings, 245 Transport equipment) · 3 stocks (311 Goods) · 4 third parties (401 Suppliers, 411 Customers, 443 VAT invoiced) · 5 treasury (521 Bank, 571 Cash) · 6 expenses (601 Purchases of goods, 661 Salaries) · 7 income (701 Sales of goods) · 8 other income and expenses.\n"
  "Enterprises: sole traders, partnerships and companies (SARL, SA) in trade, industry or services.\n"
  "Double entry: every transaction affects at least two accounts; total debits = total credits.",
  worked({},
         "In which class are these accounts: {'571 Cash'}, {'601 Purchases of goods'}, {'101 Capital'}?",
         ["The first digit gives the class.", "{'571'} → class {5} (treasury); {'601'} → class {6} (expenses); {'101'} → class {1} (equity)."],
         "Class {5}, class {6} and class {1}"),
  [card("c3a1-1", "OHADA gives member states one set of business and accounting rules (SYSCOHADA).",
        ["Cameroon, Senegal, Côte d'Ivoire and others"], "a3-1-ohada"),
   card("c3a1-2", "The first digit of an account number gives its class.",
        [E("521 Bank") + " is in class {5}: treasury."], "a3-1-class"),
   card("c3a1-3", "Double entry: every debit has an equal credit.",
        ["Cash sale: debit Cash, credit Sales."], "a3-1-double")],
  [bank("a3-1-ohada", 1, "{X.q}", [
     {"q": "What is OHADA?", "r": "An organisation that harmonises business law, including accounting, in member African states", "w": ["A bank in Douala", "A tax paid on sales", "A type of company"],
      "e": ["It is not a bank.", "That is VAT.", "Companies are SARL, SA and others."], "y": "Its uniform acts apply in all member states."},
     {"q": "What is SYSCOHADA?", "r": "The OHADA accounting system and chart of accounts", "w": ["A Cameroonian bank", "A spreadsheet program", "A customs form"],
      "e": ["It is not a bank.", "It is a set of rules, not software.", "It is not a customs document."], "y": "It sets out the accounts and how to keep them."},
     {"q": "Where and when was the OHADA treaty signed?", "r": "Port Louis, 1993", "w": ["Yaoundé, 1960", "Paris, 2017", "Douala, 2000"],
      "e": ["1960 is Cameroon's independence.", "2017 is the revision of SYSCOHADA.", "Not the treaty date."], "y": "Signed in Port Louis (Mauritius) in 1993."}], SRC),
   bank("a3-1-class", 1, "In which class is this account? {X.q}", [
     {"q": "571 Cash", "r": "class 5 (treasury)", "w": ["class 7 (income)", "class 1 (equity)", "class 6 (expenses)"],
      "e": ["Income accounts start with 7.", "Equity starts with 1.", "Expenses start with 6."], "y": "The first digit is 5."},
     {"q": "701 Sales of goods", "r": "class 7 (income)", "w": ["class 6 (expenses)", "class 4 (third parties)", "class 2 (fixed assets)"],
      "e": ["Sales are income, not expenses.", "Third parties start with 4.", "Fixed assets start with 2."], "y": "The first digit is 7."},
     {"q": "245 Transport equipment", "r": "class 2 (fixed assets)", "w": ["class 3 (stocks)", "class 5 (treasury)", "class 6 (expenses)"],
      "e": ["Stocks start with 3.", "Treasury starts with 5.", "Expenses start with 6."], "y": "A vehicle used for years is a fixed asset."},
     {"q": "401 Suppliers", "r": "class 4 (third parties)", "w": ["class 1 (equity)", "class 6 (expenses)", "class 5 (treasury)"],
      "e": ["Equity starts with 1.", "Expenses start with 6.", "Treasury starts with 5."], "y": "Suppliers and customers are third parties."}], SRC),
   bank("a3-1-double", 2, "{X.q}", [
     {"q": "What does double entry mean?", "r": "Every transaction is recorded in at least two accounts, with equal debits and credits", "w": ["Every transaction is written twice in the same account", "Only cash transactions are recorded", "Debits are always bigger than credits"],
      "e": ["It uses two (or more) different accounts.", "All transactions are recorded.", "Debits always equal credits."], "y": "Each transaction has a giving and a receiving side."},
     {"q": "A trader sells goods for cash. Which accounts are affected?", "r": "571 Cash (debit) and 701 Sales (credit)", "w": ["571 Cash only", "601 Purchases and 401 Suppliers", "101 Capital and 162 Loans"],
      "e": ["Double entry needs two accounts.", "Those are for buying on credit.", "Those are financing accounts."], "y": "Cash comes in; sales income is earned."},
     {"q": "Which type of enterprise is owned by one person?", "r": "a sole trader", "w": ["a public limited company (SA)", "a partnership", "a cooperative"],
      "e": ["An SA has many shareholders.", "A partnership has two or more partners.", "A cooperative has many members."], "y": "Many small shops are sole traders."}], SRC),
   num("a3-1-num", 3, "Total debits in a journal are {d} FCFA. Every entry is balanced. What are the total credits (FCFA)?", "d",
       ["In double entry, total debits always equal total credits.", "Total credits = {answer} FCFA."],
       vars={"d": {"int": [50000, 900000], "step": 5000}},
       misc=[("half", "d / 2", "Debits and credits are equal in total; nothing is halved."), ("double", "2 * d", "They are equal, not double.")],
       unit="FCFA", sources=SRC)],
  learn=learn(
    [("OHADA and SYSCOHADA",
      "OHADA is the Organisation for the Harmonisation of Business Law in Africa. Its treaty was signed in Port Louis in {1993}, and Cameroon is one of its member states.\n"
      "OHADA makes 'uniform acts' that apply in all member states. The accounting one is SYSCOHADA (revised in {2017}): the same accounts and rules from Douala to Dakar, so accounts can be understood across borders."),
     ("The chart of accounts",
      "Each account has a number; its first digit gives its class:\n"
      "• {1} equity and long-term liabilities (Capital, Loans)\n• {2} fixed assets (Buildings, Equipment, Vehicles)\n• {3} stocks (Goods, Raw materials)\n"
      "• {4} third parties (Suppliers, Customers, Staff, State/VAT)\n• {5} treasury (Bank, Cash)\n• {6} expenses (Purchases, Salaries, Electricity)\n• {7} income (Sales, Services)\n• {8} other income and expenses."),
     ("Enterprises and double entry",
      "Enterprises may be sole traders, partnerships or companies (SARL, SA), working in trade, industry or services.\n"
      "Every transaction has two sides. In double entry each transaction is recorded in at least two accounts: one debited and one credited for the same amount. So total debits always equal total credits.\n"
      "A cash sale: debit Cash (money comes in), credit Sales (income earned).")],
    key_words=[("OHADA", "organisation harmonising business law in member African states"), ("SYSCOHADA", "the OHADA accounting system"),
               ("chart of accounts", "the numbered list of accounts grouped in classes"), ("double entry", "recording each transaction as an equal debit and credit")],
    examples=[E("101 Capital") + ": class {1}", E("601 Purchases of goods") + ": class {6}", E("411 Customers") + ": class {4}"],
    mistake=("Sales ({'701'}) is an expense account", "Sales is an income account in class {7}",
             "Class {6} holds expenses; class {7} holds income.")))

# ---------------------------------------------------------------- 2. Journal, ledger, trial balance
L.lesson(D, S, 2, ("a3-2", "The accounting cycle: journal, ledger and trial balance"), [1],
  "Accounting cycle: source documents (invoices, receipts) → journal → ledger → trial balance → financial statements.\n"
  "• Journal: transactions recorded in date order, each with the accounts debited and credited, amounts and a short explanation.\n"
  "• Ledger: each account on its own page (T-account); journal amounts are posted to the debit or credit side.\n"
  "• Balance of an account = difference between its debit total and credit total (debit balance if debits are bigger).\n"
  "• Trial balance: a list of all account balances; total debit balances must equal total credit balances. If not, there is an error.",
  worked({"a": 500000, "b": 120000, "c": 80000},
         "The Bank account has debits of {a} FCFA and {b} FCFA and a credit of {c} FCFA. Find its balance.",
         ["Total debits = {a} + {b} = {a + b} FCFA.", "Total credits = {c} FCFA.", "Balance = {a + b} − {c} = {a + b - c} FCFA (a debit balance)."],
         "{a + b - c} FCFA debit balance", checks=["a + b - c == 540000"]),
  [card("c3a2-1", "Journal → ledger → trial balance.",
        ["Record, post, check."], "a3-2-order"),
   card("c3a2-2", "The balance is the difference between the two sides of an account.",
        ["Debits {300000}, credits {100000}: debit balance {200000}"], "a3-2-bal"),
   card("c3a2-3", "In a trial balance, debit and credit totals must agree.",
        ["If they differ, look for an error."], "a3-2-tb")],
  [order("a3-2-order", 1, "Put the stages of the accounting cycle in order.",
         ["Source documents", "Journal", "Ledger", "Trial balance", "Financial statements"], hint="Documents first, statements last.", sources=SRC, review="authored"),
   num("a3-2-bal", 1, "An account has debits totalling {d} FCFA and credits totalling {c} FCFA. What is the size of its balance (FCFA)?", "abs(d - c)",
       ["Balance = larger side − smaller side.", "|{d} − {c}| = {answer} FCFA ({d > c ? 'debit' : 'credit'} balance)."],
       vars={"d": {"int": [100000, 900000], "step": 10000}, "c": {"int": [50000, 800000], "step": 10000}},
       misc=[("sum", "d + c", "The balance is the difference between the sides, not their sum.")],
       unit="FCFA", sources=SRC, where=["d != c"]),
   num("a3-2-tb", 2, "A trial balance shows debit balances of {x}, {y} and {z} FCFA and credit balances of {u} and {v} FCFA. By how much do the totals differ (FCFA)? (0 if they agree)", "abs(x + y + z - u - v)",
       ["Debit total = {x} + {y} + {z} = {x + y + z}.", "Credit total = {u} + {v} = {u + v}.", "Difference = {answer} FCFA."],
       vars={"x": {"int": [100000, 500000], "step": 10000}, "y": {"int": [50000, 300000], "step": 10000}, "z": {"int": [20000, 200000], "step": 10000},
             "u": {"int": [100000, 600000], "step": 10000}, "e": {"pick": [0, 0, 10000, 20000, 50000]}, "v": {"expr": "x + y + z - u + e"}},
       misc=[("total", "x + y + z", "That is the debit total. Compare it with the credit total.")],
       unit="FCFA", sources=SRC, where=["v > 0"]),
   bank("a3-2-post", 2, "{X.q}", [
     {"q": "What is posting?", "r": "Transferring journal amounts to the ledger accounts", "w": ["Sending letters to customers", "Adding up the trial balance", "Paying suppliers"],
      "e": ["That is correspondence.", "That comes after posting.", "That is a transaction, not posting."], "y": "Each journal line goes to its ledger account."},
     {"q": "A journal entry debits 571 Cash and credits 701 Sales with 25 000 FCFA. How is it posted?", "r": "25 000 on the debit side of Cash and on the credit side of Sales", "w": ["25 000 on the credit side of Cash", "50 000 in Cash only", "25 000 on the debit side of Sales"],
      "e": ["Cash is debited.", "Each account gets the amount once, on its own side.", "Sales is credited."], "y": "Post each amount to the same side as in the journal."},
     {"q": "Which document is the starting point of the accounting cycle?", "r": "source documents such as invoices and receipts", "w": ["the trial balance", "the balance sheet", "the ledger"],
      "e": ["That comes later.", "That comes at the end.", "The ledger comes after the journal."], "y": "Every entry must be supported by a document."}], SRC),
   bank("a3-2-err", 3, "{X.q}", [
     {"q": "A trial balance agrees. Does that prove there are no errors?", "r": "No: some errors (such as a wrong account or a missing entry) do not affect the totals", "w": ["Yes, always", "Yes, if it is typed", "No, a trial balance never agrees"],
      "e": ["Some errors are hidden.", "Typing does not matter.", "A correct trial balance agrees."], "y": "Errors of omission or of principle leave the totals equal."},
     {"q": "Rent of 50 000 FCFA was paid in cash but posted only to the Rent account. What happens to the trial balance?", "r": "It does not agree: debits exceed credits by 50 000", "w": ["It agrees", "Credits exceed debits by 50 000", "It doubles"],
      "e": ["One side is missing.", "The debit was posted, the credit was not.", "Nothing doubles."], "y": "Only one side was posted."},
     {"q": "Why do debit and credit totals agree in a correct trial balance?", "r": "Every transaction was recorded with equal debits and credits", "w": ["The accountant chooses the totals", "Because Cash is always the largest account", "Because there are always ten accounts"],
      "e": ["Totals come from the entries.", "Not related.", "Any number of accounts."], "y": "Double entry keeps the books in balance."}], SRC)],
  learn=learn(
    [("From documents to statements",
      "Every transaction starts with a source document: an invoice, a receipt, a bank statement. The accounting cycle then follows:\n"
      "source documents → journal → ledger → trial balance → financial statements (balance sheet and income statement)."),
     ("Journal and ledger",
      "The journal records transactions in date order. Each entry gives the date, the account(s) debited and credited, the amounts and a short description; the debits equal the credits.\n"
      "The ledger has one page (a T-account) for each account. Posting means copying each journal amount to the same side of the right ledger account.\n"
      "The balance of an account is the difference between its two sides: a debit balance if the debits are bigger, a credit balance if the credits are bigger."),
     ("Trial balance",
      "A trial balance lists every account with its balance, debit balances in one column and credit balances in the other. The two totals must be equal.\n"
      "If they differ, there is an error (a one-sided posting, a wrong addition). But equal totals do not prove everything is right: an entry left out completely, or posted to the wrong account on the correct side, does not show up.")],
    key_words=[("journal", "book of first entry, in date order"), ("ledger", "book of accounts, one page per account"), ("posting", "copying journal amounts to the ledger"),
               ("trial balance", "list of balances to check that debits equal credits")],
    examples=["Debits {500000}, credits {120000}: debit balance {380000}", "Trial balance totals {950000} = {950000}: agrees"],
    mistake=("Balance = debits + credits", "Balance = the larger side − the smaller side",
             "A balance is the difference between the two sides.")))

# ---------------------------------------------------------------- 3. VAT
SRC = ["vat"]
L.lesson(D, S, 3, ("a3-3", "Value added tax (VAT): calculation and accounting entries"), [2],
  "VAT in Cameroon is 19.25% of the price excluding tax (HT): 17.5% VAT plus 10% of that as council tax (17.5% × 1.1 = 19.25%).\n"
  "• Amount including tax (TTC) = HT + VAT = HT × 1.1925.\n"
  "• On sales, the enterprise charges VAT: credit 443 VAT invoiced (collected).\n"
  "• On purchases, it pays VAT it can recover: debit 445 VAT recoverable.\n"
  "• VAT payable to the State = VAT invoiced − VAT recoverable (account 4441). If recoverable is bigger, the difference is a VAT credit (4449), carried forward.",
  worked({"ht": 200000},
         "Goods are sold for {ht} FCFA HT. Find the VAT and the amount including tax.",
         ["VAT = {19.25}% × {ht} = {ht * 0.1925} FCFA.", "TTC = {ht} + {ht * 0.1925} = {ht * 1.1925} FCFA."],
         "VAT {ht * 0.1925} FCFA; TTC {ht * 1.1925} FCFA", checks=["ht * 0.1925 == 38500"]),
  [card("c3a3-1", "VAT = {19.25}% of the price excluding tax.",
        ["{100000} HT: VAT {19250}"], "a3-3-vat"),
   card("c3a3-2", "TTC = HT + VAT.",
        ["{100000} + {19250} = {119250}"], "a3-3-ttc"),
   card("c3a3-3", "VAT payable = VAT invoiced − VAT recoverable.",
        ["{60000} − {45000} = {15000} to pay"], "a3-3-pay")],
  [num("a3-3-vat", 1, "Goods worth {ht} FCFA HT are sold. Find the VAT at {19.25}% (FCFA).", "vat",
       ["VAT = {19.25} ÷ {100} × {ht}.", "= {answer} FCFA."],
       vars=HT, misc=[("ttc", "ht + vat", "That is the amount including tax. VAT is only the tax part."), ("rate", "ht * 0.175", "The rate in Cameroon is {19.25}% ({17.5}% plus council tax).")],
       unit="FCFA", sources=SRC),
   num("a3-3-ttc", 1, "Find the amount including tax (TTC) for a sale of {ht} FCFA HT (VAT {19.25}%).", "ht + vat",
       ["VAT = {vat} FCFA.", "TTC = {ht} + {vat} = {answer} FCFA."],
       vars=HT, misc=[("vat", "vat", "That is the VAT only; add it to the HT amount.")],
       unit="FCFA", sources=SRC),
   num("a3-3-pay", 2, "In a month, VAT invoiced on sales is {inv} FCFA and VAT recoverable on purchases is {rec} FCFA. What VAT must be paid to the State (FCFA)? (0 if there is a credit)", "max(inv - rec, 0)",
       ["VAT payable = invoiced − recoverable = {inv} − {rec}.", "{inv > rec ? 'Payable: ' + fmt(inv - rec) + ' FCFA.' : 'Recoverable is bigger: no VAT to pay; credit of ' + fmt(rec - inv) + ' FCFA.'}"],
       vars={"a": {"int": [10, 80]}, "b": {"int": [5, 70]}, "inv": {"expr": "a * 770"}, "rec": {"expr": "b * 770"}},
       misc=[("add", "inv + rec", "Subtract the recoverable VAT from the invoiced VAT.")],
       unit="FCFA", sources=SRC, where=["a != b", "inv + rec != max(inv - rec, 0)"]),
   bank("a3-3-entry", 2, "{X.q}", [
     {"q": "In a credit sale, which account records the VAT charged to the customer?", "r": "443 VAT invoiced (credit)", "w": ["445 VAT recoverable (debit)", "601 Purchases (debit)", "571 Cash (credit)"],
      "e": ["That is VAT on purchases.", "Not a sale.", "Cash is not involved in a credit sale."], "y": "VAT charged on sales is owed to the State."},
     {"q": "In a credit purchase of goods, which account records the VAT paid to the supplier?", "r": "445 VAT recoverable (debit)", "w": ["443 VAT invoiced (credit)", "701 Sales (credit)", "101 Capital (credit)"],
      "e": ["That is VAT on sales.", "Not a sale.", "Not a financing transaction."], "y": "The enterprise can deduct this VAT."},
     {"q": "Which account is debited when goods are sold on credit for an amount including tax?", "r": "411 Customers (with the TTC amount)", "w": ["701 Sales", "443 VAT invoiced", "401 Suppliers"],
      "e": ["Sales is credited with the HT amount.", "VAT invoiced is credited.", "Suppliers are for purchases."], "y": "The customer owes the full TTC amount."}], SRC),
   num("a3-3-ht", 3, "An invoice shows a total including tax of {ttc} FCFA (VAT {19.25}%). Find the amount excluding tax (FCFA).", "ht",
       ["TTC = HT × {1.1925}.", "HT = {ttc} ÷ {1.1925} = {answer} FCFA."],
       vars={**HT, "ttc": {"expr": "ht + vat"}},
       misc=[("sub", "ttc - roundTo(ttc * 0.1925, 1)", "Taking {19.25}% of the TTC is wrong: VAT is {19.25}% of the HT. Divide by {1.1925}.")],
       unit="FCFA", sources=SRC)],
  learn=learn(
    [("A tax on added value",
      "Value added tax (VAT) is a tax on consumption. Each enterprise charges VAT on its sales and deducts the VAT it paid on its purchases, so in the end the final consumer bears the tax.\n"
      "In Cameroon the rate is {19.25}%: {17.5}% VAT plus council tax of {10}% of it ({17.5}% × {1.1} = {19.25}%)."),
     ("Calculating",
      "• HT (hors taxes): price excluding tax.\n• VAT = {19.25}% × HT.\n• TTC (toutes taxes comprises): HT + VAT = HT × {1.1925}.\n"
      "For {200000} FCFA HT: VAT = {38500} FCFA and TTC = {238500} FCFA.\n"
      "To go back from TTC to HT, divide by {1.1925}."),
     ("Recording and paying",
      "• Sales: debit {'411'} Customers with TTC; credit {'701'} Sales with HT and {'443'} VAT invoiced with the VAT.\n"
      "• Purchases: debit {'601'} Purchases with HT and {'445'} VAT recoverable with the VAT; credit {'401'} Suppliers with TTC.\n"
      "• At the end of the month, VAT payable ({'4441'}) = VAT invoiced − VAT recoverable, paid to the State. If recoverable is bigger, the difference is a VAT credit ({'4449'}) carried to the next month.")],
    key_words=[("VAT", "value added tax, {19.25}% in Cameroon"), ("HT", "amount excluding tax"), ("TTC", "amount including all taxes"),
               ("VAT credit", "recoverable VAT larger than invoiced VAT, carried forward")],
    examples=["HT {80000}: VAT {15400}, TTC {95400}", "Invoiced {50000} − recoverable {30000} = {20000} to pay"],
    mistake=("VAT = {19.25}% of the TTC amount", "VAT = {19.25}% of the HT amount",
             "VAT is calculated on the price before tax.")))
