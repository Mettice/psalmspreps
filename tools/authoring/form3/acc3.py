"""Form 3 Accounting, Term 1 (OHADA), rows 6-8 and 10 (trading, commercial containers, cash settlement, trade bills).
Run: python tools/authoring/form3/acc3.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "accounting", "accounting"
SRC = ["ohada-transactions"]
HT = {"k": {"int": [2, 50]}, "ht": {"expr": "k * 4000"}, "vat": {"expr": "k * 770"}}


def E(entry):
    """An account or journal entry written as fixed text."""
    return "{'" + entry + "'}"


def entries(id, level, prompt, items):
    return bank(id, level, prompt, items, SRC)


# ---------------------------------------------------------------- 6. Trading transactions
L.lesson(D, S, 6, ("a3-6", "Accounting for trading transactions: purchases and sales"), [3],
  "Trading transactions are the buying and selling of goods.\n"
  "• Purchase on credit: debit 601 Purchases of goods (HT), debit 445 VAT recoverable, credit 401 Suppliers (TTC).\n"
  "• Sale on credit: debit 411 Customers (TTC), credit 701 Sales of goods (HT), credit 443 VAT invoiced.\n"
  "• Cash sale or purchase: use 571 Cash (or 521 Bank) instead of 411 or 401.\n"
  "• Trade discount (rabais, remise): a reduction on the invoice; VAT is calculated on the net amount after discount.",
  worked({"g": 200000, "d": 10},
         "Goods listed at {g} FCFA are sold on credit with a {d}% trade discount (VAT {19.25}%). Find the net, the VAT and the total the customer owes.",
         ["Discount = {d}% × {g} = {g * d / 100}; net HT = {g} − {g * d / 100} = {g * (100 - d) / 100} FCFA.",
          "VAT = {19.25}% × {g * (100 - d) / 100} = {g * (100 - d) / 100 * 0.1925} FCFA.", "TTC = {g * (100 - d) / 100 * 1.1925} FCFA, debited to {'411 Customers'}."],
         "Net {g * (100 - d) / 100}; VAT {g * (100 - d) / 100 * 0.1925}; TTC {g * (100 - d) / 100 * 1.1925} FCFA", checks=["g * (100 - d) / 100 * 0.1925 == 34650"]),
  [card("c3a6-1", "Purchases: debit Purchases and VAT recoverable; credit Suppliers.",
        [E("Dr 601, Dr 445 / Cr 401")], "a3-6-entry"),
   card("c3a6-2", "Sales: debit Customers; credit Sales and VAT invoiced.",
        [E("Dr 411 / Cr 701, Cr 443")], "a3-6-ttc"),
   card("c3a6-3", "VAT is calculated after any trade discount.",
        ["Net HT first, then VAT."], "a3-6-disc")],
  [entries("a3-6-entry", 1, "Which entry records this? {X.q}", [
     {"q": "Goods are bought on credit for 100 000 FCFA HT (VAT 19 250).", "r": "Dr 601 Purchases 100 000; Dr 445 VAT recoverable 19 250 / Cr 401 Suppliers 119 250", "w": ["Dr 401 Suppliers 119 250 / Cr 601 Purchases 119 250", "Dr 601 Purchases 119 250 / Cr 571 Cash 119 250", "Dr 411 Customers 119 250 / Cr 701 Sales 119 250"],
      "e": ["Reversed.", "It is on credit, and the VAT is recorded separately.", "That is a sale."], "y": "Purchases and recoverable VAT debited; the supplier credited TTC."},
     {"q": "Goods are sold on credit for 200 000 FCFA HT (VAT 38 500).", "r": "Dr 411 Customers 238 500 / Cr 701 Sales 200 000; Cr 443 VAT invoiced 38 500", "w": ["Dr 701 Sales 238 500 / Cr 411 Customers 238 500", "Dr 571 Cash 238 500 / Cr 701 Sales 238 500", "Dr 411 Customers 200 000 / Cr 701 Sales 200 000"],
      "e": ["Reversed.", "It is a credit sale, and VAT must be shown separately.", "The VAT is missing."], "y": "The customer owes the TTC amount."},
     {"q": "Goods are sold for cash: 50 000 FCFA HT (VAT 9 625).", "r": "Dr 571 Cash 59 625 / Cr 701 Sales 50 000; Cr 443 VAT invoiced 9 625", "w": ["Dr 411 Customers 59 625 / Cr 701 Sales 59 625", "Dr 601 Purchases 59 625 / Cr 571 Cash 59 625", "Dr 571 Cash 50 000 / Cr 701 Sales 50 000"],
      "e": ["It is a cash sale, not on credit.", "That is a purchase.", "The VAT collected must be recorded."], "y": "Cash comes in for the full TTC."}]),
   num("a3-6-ttc", 1, "Goods are bought on credit for {ht} FCFA HT (VAT {19.25}%). What amount is credited to {'401'} Suppliers (FCFA)?", "ht + vat",
       ["VAT = {vat} FCFA.", "TTC = {ht} + {vat} = {answer} FCFA."],
       vars=HT, misc=[("ht", "ht", "The supplier is owed the amount including VAT.")],
       unit="FCFA", sources=SRC),
   num("a3-6-disc", 2, "Goods listed at {g} FCFA are sold with a {d}% trade discount. What is the net amount excluding tax (FCFA)?", "g * (100 - d) / 100",
       ["Discount = {d}% × {g} = {g * d / 100} FCFA.", "Net = {g} − {g * d / 100} = {answer} FCFA."],
       vars={"g": {"int": [20000, 500000], "step": 20000}, "d": {"pick": [5, 10, 15, 20]}},
       misc=[("disc", "g * d / 100", "That is the discount; subtract it from the list price.")],
       unit="FCFA", sources=SRC),
   num("a3-6-total", 3, "Goods listed at {g} FCFA are sold on credit with a {d}% trade discount (VAT {19.25}%). What amount is debited to {'411'} Customers (FCFA)?", "g * (100 - d) / 100 * 1.1925",
       ["Net HT = {g} × {(100 - d) / 100} = {g * (100 - d) / 100} FCFA.", "VAT = {g * (100 - d) / 100 * 0.1925}; TTC = {answer} FCFA."],
       vars={"q": {"int": [1, 25]}, "d": {"pick": [10, 20]}, "g": {"expr": "q * 40000"}},
       misc=[("vatfirst", "g * 1.1925", "Apply the discount first, then add VAT on the net amount."), ("novat", "g * (100 - d) / 100", "Add the VAT: the customer pays TTC.")],
       unit="FCFA", sources=SRC, where=["(g * (100 - d) / 100 * 0.1925) % 1 == 0"])],
  learn=learn(
    [("Buying goods",
      "Goods bought for resale go to {'601 Purchases of goods'} (amount excluding tax). The VAT paid goes to {'445 VAT recoverable'}.\n"
      "If bought on credit, the supplier is owed the total: credit {'401 Suppliers'} with the amount including tax. If paid at once, credit {'571 Cash'} or {'521 Bank'}."),
     ("Selling goods",
      "Sales of goods are income: credit {'701 Sales of goods'} with the amount excluding tax and {'443 VAT invoiced'} with the VAT.\n"
      "On credit, debit {'411 Customers'} with the total including tax; for cash, debit {'571 Cash'}.\n"
      "A sale of {200000} FCFA HT: {'Dr 411'} {238500}, {'Cr 701'} {200000}, {'Cr 443'} {38500}."),
     ("Trade discounts",
      "A trade discount (rabais, remise) reduces the price on the invoice, for example for a regular customer or a large order.\n"
      "Work out the net amount first: list price − discount. Then calculate VAT on the net amount.\n"
      "{200000} FCFA less {10}%: net {180000}, VAT {34650}, total {214650} FCFA.")],
    key_words=[("purchases of goods", "account {'601'}: goods bought to resell"), ("sales of goods", "account {'701'}: income from selling goods"),
               ("trade discount", "a price reduction shown on the invoice"), ("credit transaction", "paid later, not at once")],
    examples=[E("Dr 601 / Cr 401") + " (credit purchase)", E("Dr 411 / Cr 701, 443") + " (credit sale)", E("Dr 571 / Cr 701, 443") + " (cash sale)"],
    mistake=("VAT is calculated on the list price before the discount", "VAT is calculated on the net price after the discount",
             "Tax is charged only on what the customer actually pays for the goods.")))

# ---------------------------------------------------------------- 7. Commercial containers
L.lesson(D, S, 7, ("a3-7", "Accounting for transactions with commercial containers"), [6],
  "Commercial containers (emballages) such as crates, bottles and gas cylinders may be returnable. The customer pays a deposit (consignation) when goods are delivered in them and gets it back when they are returned.\n"
  "Seller:\n• Goods delivered with consigned containers: debit 411 Customers (goods TTC + deposit), credit 701 Sales and 443 VAT, and credit 4194 Customers, consigned containers (deposit). No VAT is charged on the deposit.\n"
  "• Containers returned: debit 4194, credit 411 (or 571 if refunded in cash) with the deposit refunded.\n"
  "Buyer: debit 4094 Suppliers, containers to be returned with the deposit paid; on return, credit 4094.\n"
  "Containers not returned are treated as sold (or bought).",
  worked({"n": 20, "dep": 500},
         "A drinks depot delivers drinks with {n} crates; the deposit is {dep} FCFA per crate. Find the deposit and the entry for it.",
         ["Deposit = {n} × {dep} = {n * dep} FCFA (no VAT on the deposit).", "Debit {'411 Customers'} {n * dep}; credit {'4194 Customers, consigned containers'} {n * dep}."],
         "Deposit {n * dep} FCFA: Dr {'411'} / Cr {'4194'}", checks=["n * dep == 10000"]),
  [card("c3a7-1", "Deposit = number of containers × deposit per container.",
        ["{12} crates × {500} = {6000} FCFA"], "a3-7-dep"),
   card("c3a7-2", "The seller credits {'4194'} with deposits received; no VAT on deposits.",
        [E("Cr 4194 Customers, consigned containers")], "a3-7-entry"),
   card("c3a7-3", "Returned containers are refunded; unreturned ones are treated as sold.",
        ["{15} of {20} crates returned: refund {15} deposits."], "a3-7-ret")],
  [num("a3-7-dep", 1, "A brewery depot delivers {n} crates with a deposit of {d} FCFA each. What is the total deposit (FCFA)?", "n * d",
       ["Deposit = {n} × {d}.", "= {answer} FCFA."],
       vars={"n": {"int": [5, 60]}, "d": {"pick": [300, 500, 1000, 1500]}},
       misc=[("vat", "n * d * 1.1925", "No VAT is charged on container deposits.")],
       unit="FCFA", sources=SRC),
   entries("a3-7-entry", 1, "Which entry does the SELLER make? {X.q}", [
     {"q": "Deposits of 10 000 FCFA are charged to a customer for crates delivered.", "r": "Dr 411 Customers / Cr 4194 Customers, consigned containers", "w": ["Dr 4194 / Cr 411", "Dr 411 / Cr 701 Sales", "Dr 4094 / Cr 401"],
      "e": ["Reversed: that is the refund.", "Deposits are not sales income.", "Those are the buyer's accounts."], "y": "The deposit is a debt to the customer until the crates come back."},
     {"q": "The customer returns the crates and the 10 000 FCFA deposit is credited back to his account.", "r": "Dr 4194 Customers, consigned containers / Cr 411 Customers", "w": ["Dr 411 / Cr 4194", "Dr 701 Sales / Cr 411", "Dr 4194 / Cr 701 Sales"],
      "e": ["That charges the deposit.", "Sales were not involved.", "The deposit is refunded, not sold."], "y": "The debt to the customer is cancelled."},
     {"q": "Cash is refunded to a customer who brings back crates worth 6 000 FCFA in deposits.", "r": "Dr 4194 Customers, consigned containers / Cr 571 Cash", "w": ["Dr 571 Cash / Cr 4194", "Dr 601 Purchases / Cr 571 Cash", "Dr 4194 / Cr 701 Sales"],
      "e": ["Cash goes out, so Cash is credited.", "No purchase of goods.", "The deposit is refunded, not sold."], "y": "Refund in cash cancels the deposit debt."}]),
   num("a3-7-ret", 2, "A customer received {n} crates (deposit {d} FCFA each) and returns {r} of them. How much deposit is refunded (FCFA)?", "r * d",
       ["Refund = returned crates × deposit = {r} × {d}.", "= {answer} FCFA."],
       vars={"n": {"int": [10, 50]}, "d": {"pick": [500, 1000]}, "r": {"int": [3, 40]}},
       misc=[("all", "n * d", "Only the {r} returned crates are refunded."), ("kept", "(n - r) * d", "That is the value of the crates not returned.")],
       unit="FCFA", sources=SRC, where=["r < n"]),
   bank("a3-7-buyer", 3, "{X.q}", [
     {"q": "Which account does the BUYER debit when paying a deposit on containers to be returned?", "r": "4094 Suppliers, containers to be returned", "w": ["4194 Customers, consigned containers", "601 Purchases of goods", "701 Sales"],
      "e": ["That is the seller's account.", "The deposit is not a purchase of goods.", "The buyer is not selling."], "y": "The supplier owes the buyer the deposit back."},
     {"q": "Why is no VAT charged on the deposit for returnable crates?", "r": "The deposit is refundable, not a sale of the crates", "w": ["Crates are always free", "VAT is only on services", "Deposits are illegal"],
      "e": ["The customer pays a deposit.", "VAT applies to goods too.", "Deposits are normal."], "y": "Only if the crates are kept do they become a sale."},
     {"q": "A customer keeps 5 crates instead of returning them. How are they treated?", "r": "As a sale of containers to the customer", "w": ["As a loan", "As capital", "They are ignored"],
      "e": ["Not a loan.", "Not capital.", "They must be accounted for."], "y": "Unreturned containers are treated as sold (or bought)."}], SRC)],
  learn=learn(
    [("Returnable containers",
      "Many goods come in returnable containers: crates of soft drinks and beer, gas cylinders, drums. The seller charges a deposit (consignation) to make sure the containers come back. When they are returned, the deposit is refunded.\n"
      "The deposit is not income and no VAT is charged on it: it is money the seller must give back."),
     ("The seller's entries",
      "• Containers delivered: debit {'411 Customers'}, credit {'4194 Customers, consigned containers'} with the deposits.\n"
      "• Containers returned: debit {'4194'}, credit {'411 Customers'} (or {'571 Cash'} if refunded in cash).\n"
      "Example: {20} crates at {500} FCFA = {10000} FCFA in deposits; {15} returned → refund {7500} FCFA."),
     ("The buyer's entries and unreturned containers",
      "The buyer records deposits paid in {'4094 Suppliers, containers to be returned'}: debit when paid, credit when the containers go back.\n"
      "Containers that are not returned are treated as sold by the seller and bought by the buyer.\n"
      "Keeping track of deposits avoids losing money on missing crates.")],
    key_words=[("commercial containers", "packaging such as crates, bottles and cylinders"), ("deposit (consignation)", "money paid for returnable containers, refunded on return"),
               ("{'4194'}", "seller's account for deposits on consigned containers"), ("{'4094'}", "buyer's account for deposits paid on containers")],
    examples=["{30} crates × {500} = {15000} FCFA deposit", "Return of {10} crates: refund {5000} FCFA"],
    mistake=("Container deposits are credited to {'701'} Sales", "They are credited to {'4194'} Customers, consigned containers",
             "A deposit is refundable, so it is a debt, not income.")))

# ---------------------------------------------------------------- 8. Cash settlement transactions
L.lesson(D, S, 8, ("a3-8", "Accounting for cash settlement transactions"), [6],
  "Settlement transactions pay or receive money owed:\n"
  "• Customer pays by cheque or transfer: debit 521 Bank, credit 411 Customers. In cash: debit 571 Cash.\n"
  "• Business pays a supplier: debit 401 Suppliers, credit 521 Bank (or 571 Cash).\n"
  "• Moving money between cash and bank: cash paid into the bank: debit 521 Bank, credit 571 Cash (often through 585 Transfers of funds).\n"
  "• Cash discount (escompte) for early payment: the seller records it as an expense (673 Discounts granted); the customer pays less.\n"
  "The cash and bank accounts must never show impossible balances; cash in hand cannot be negative.",
  worked({"open": 150000, "rec": 80000, "pay": 60000},
         "Cash in hand is {open} FCFA. A customer pays {rec} FCFA in cash and a supplier is paid {pay} FCFA in cash. Find the new cash balance.",
         ["Receipts increase cash: {open} + {rec} = {open + rec}.", "Payments decrease it: {open + rec} − {pay} = {open + rec - pay} FCFA."],
         "{open + rec - pay} FCFA", checks=["open + rec - pay == 170000"]),
  [card("c3a8-1", "Money received from a customer: debit Bank or Cash, credit Customers.",
        [E("Dr 521 / Cr 411")], "a3-8-entry"),
   card("c3a8-2", "Paying a supplier: debit Suppliers, credit Bank or Cash.",
        [E("Dr 401 / Cr 521")], "a3-8-bal"),
   card("c3a8-3", "A cash discount for early payment is an expense for the seller.",
        ["{2}% off for paying within {10} days"], "a3-8-disc")],
  [entries("a3-8-entry", 1, "Which entry records this? {X.q}", [
     {"q": "A customer pays 150 000 FCFA by cheque, paid into the bank.", "r": "Dr 521 Bank / Cr 411 Customers", "w": ["Dr 411 Customers / Cr 521 Bank", "Dr 521 Bank / Cr 701 Sales", "Dr 571 Cash / Cr 401 Suppliers"],
      "e": ["Reversed.", "The sale was already recorded; now the debt is settled.", "Not cash and not a supplier."], "y": "Bank increases; the customer owes less."},
     {"q": "The business pays a supplier 90 000 FCFA by bank transfer.", "r": "Dr 401 Suppliers / Cr 521 Bank", "w": ["Dr 521 Bank / Cr 401 Suppliers", "Dr 601 Purchases / Cr 521 Bank", "Dr 401 Suppliers / Cr 701 Sales"],
      "e": ["Reversed.", "The purchase was already recorded; now the debt is paid.", "No sale."], "y": "The debt falls; the bank falls."},
     {"q": "200 000 FCFA cash is paid into the bank.", "r": "Dr 521 Bank / Cr 571 Cash", "w": ["Dr 571 Cash / Cr 521 Bank", "Dr 521 Bank / Cr 101 Capital", "Dr 521 Bank / Cr 701 Sales"],
      "e": ["That is withdrawing cash from the bank.", "It is not new capital.", "It is not a sale."], "y": "Money moves from the till to the bank."}]),
   num("a3-8-bal", 2, "Cash in hand is {o} FCFA. During the day: cash sales {a} FCFA, a supplier paid {b} FCFA, {c} FCFA paid into the bank. What is the cash balance (FCFA)?", "o + a - b - c",
       ["Receipts: {o} + {a} = {o + a}.", "Payments: {b} + {c} = {b + c}.", "Balance = {o + a} − {b + c} = {answer} FCFA."],
       vars={"o": {"int": [100000, 300000], "step": 10000}, "a": {"int": [50000, 200000], "step": 5000}, "b": {"int": [20000, 100000], "step": 5000}, "c": {"int": [50000, 150000], "step": 10000}},
       misc=[("bank", "o + a - b + c", "Money paid into the bank leaves the cash box: subtract it.")],
       unit="FCFA", sources=SRC, where=["o + a - b - c > 0"]),
   num("a3-8-disc", 2, "A customer owes {t} FCFA and pays early with a {d}% cash discount. How much does he pay (FCFA)?", "t * (100 - d) / 100",
       ["Discount = {d}% × {t} = {t * d / 100} FCFA.", "Payment = {t} − {t * d / 100} = {answer} FCFA."],
       vars={"t": {"int": [50000, 500000], "step": 50000}, "d": {"pick": [1, 2, 3, 5]}},
       misc=[("disc", "t * d / 100", "That is the discount, not the payment.")],
       unit="FCFA", sources=SRC),
   bank("a3-8-why", 3, "{X.q}", [
     {"q": "Why can the cash account never have a credit balance?", "r": "You cannot pay out more cash than is in the till", "w": ["Cash is always a liability", "Cash is in class 7", "Credits are not allowed in accounting"],
      "e": ["Cash is an asset.", "Cash is in class 5.", "Credits are normal."], "y": "A credit balance on Cash means an error."},
     {"q": "Why do sellers offer cash discounts?", "r": "To encourage customers to pay early", "w": ["To increase VAT", "To reduce their bank balance", "Because the law requires it"],
      "e": ["Discounts reduce the amount.", "They receive money sooner.", "It is a business choice."], "y": "Early payment improves the seller's cash flow."},
     {"q": "A cheque from a customer bounces (is unpaid). What should happen in the accounts?", "r": "The entry is reversed: Dr 411 Customers / Cr 521 Bank", "w": ["Nothing changes", "Dr 521 Bank / Cr 411 Customers again", "Dr 701 Sales / Cr 411"],
      "e": ["The bank did not receive the money.", "That records it as received again.", "Sales are not changed."], "y": "The customer still owes the money."}], SRC)],
  learn=learn(
    [("Settling debts",
      "After a credit sale or purchase, someone still owes money. Settlement transactions pay these debts:\n"
      "• A customer pays: debit {'521 Bank'} (cheque, transfer, mobile money to the business account) or {'571 Cash'}; credit {'411 Customers'}.\n"
      "• The business pays a supplier: debit {'401 Suppliers'}; credit {'521 Bank'} or {'571 Cash'}."),
     ("Moving money and keeping it safe",
      "Cash paid into the bank: debit {'521 Bank'}, credit {'571 Cash'}. Cash withdrawn from the bank: the reverse. Many businesses use a transfer account ({'585'}) between the two.\n"
      "Keep track of the cash balance: opening cash + receipts − payments. It can never be negative: a credit balance on Cash shows an error."),
     ("Cash discounts",
      "To be paid sooner, a seller may offer a cash discount (escompte): for example {2}% off if the customer pays within {10} days.\n"
      "The customer pays less; the seller records the discount as an expense ({'673 Discounts granted'}), and the customer as income.\n"
      "{100000} FCFA with a {2}% discount: the customer pays {98000} FCFA.")],
    key_words=[("settlement", "paying or receiving money owed"), ("cash discount", "reduction for paying early"), ("cash balance", "opening cash + receipts − payments")],
    examples=[E("Dr 521 / Cr 411") + " (customer pays by cheque)", E("Dr 401 / Cr 571") + " (supplier paid in cash)", E("Dr 521 / Cr 571") + " (cash banked)"],
    mistake=("When a customer pays, credit Sales again", "Credit {'411'} Customers: the sale was already recorded",
             "Payment settles the debt; it is not a new sale.")))

# ---------------------------------------------------------------- 10. Trade bills
L.lesson(D, S, 10, ("a3-10", "Accounting for transactions with trade bills"), [8],
  "A trade bill (effet de commerce), such as a bill of exchange or a promissory note, is a written promise or order to pay a sum on a fixed date (maturity).\n"
  "Seller (drawer) who draws a bill on a customer:\n• Bill accepted: debit 412 Customers, bills receivable; credit 411 Customers.\n• Bill paid at maturity: debit 521 Bank; credit 412.\n"
  "Buyer who accepts a bill: debit 401 Suppliers; credit 402 Suppliers, bills payable. Paying it at maturity: debit 402; credit 521 Bank.\n"
  "Advantages: a clear date and legal proof of the debt; the seller can get cash earlier by discounting the bill at a bank.",
  worked({"t": 400000},
         "A customer owes {t} FCFA and accepts a bill of exchange for this amount, due in {60} days. Give the seller's entries now and at maturity.",
         ["Bill accepted: debit {'412 Customers, bills receivable'} {t}; credit {'411 Customers'} {t}.", "At maturity, when paid: debit {'521 Bank'} {t}; credit {'412'} {t}."],
         "Dr {'412'} / Cr {'411'}, then Dr {'521'} / Cr {'412'}", checks=["t == 400000"]),
  [card("c3a10-1", "A trade bill is a written promise or order to pay on a fixed date.",
        ["A bill of exchange due in {90} days"], "a3-10-def"),
   card("c3a10-2", "The seller moves the debt from {'411'} to {'412'} Bills receivable.",
        [E("Dr 412 / Cr 411")], "a3-10-entry"),
   card("c3a10-3", "The buyer moves the debt from {'401'} to {'402'} Bills payable.",
        [E("Dr 401 / Cr 402")], "a3-10-bal")],
  [bank("a3-10-def", 1, "{X.q}", [
     {"q": "What is a trade bill?", "r": "A written promise or order to pay a sum on a fixed date", "w": ["A receipt for cash already paid", "A list of prices", "A bank statement"],
      "e": ["It is about a future payment.", "Not a price list.", "Not a bank statement."], "y": "Bills of exchange and promissory notes are trade bills."},
     {"q": "What is the maturity date of a bill?", "r": "the date on which it must be paid", "w": ["the date it was printed", "the date the goods were made", "the owner's birthday"],
      "e": ["Printing date is not relevant.", "Not related.", "Not related."], "y": "The bill is payable on its due date."},
     {"q": "Which is an advantage of a trade bill for the seller?", "r": "It is legal proof of the debt and can be discounted at a bank for cash", "w": ["The customer never has to pay", "It removes VAT", "It is a sale of the business"],
      "e": ["The customer must pay at maturity.", "VAT is not affected.", "Not related."], "y": "It gives security and access to cash."}], SRC),
   entries("a3-10-entry", 1, "Which entry records this? {X.q}", [
     {"q": "SELLER: a customer accepts a bill of 300 000 FCFA for what he owes.", "r": "Dr 412 Customers, bills receivable / Cr 411 Customers", "w": ["Dr 411 / Cr 412", "Dr 521 Bank / Cr 411", "Dr 401 / Cr 402"],
      "e": ["Reversed.", "No money has been received yet.", "Those are the buyer's accounts."], "y": "The debt becomes a bill receivable."},
     {"q": "SELLER: the bill of 300 000 FCFA is paid at maturity into the bank.", "r": "Dr 521 Bank / Cr 412 Customers, bills receivable", "w": ["Dr 412 / Cr 521", "Dr 521 / Cr 411", "Dr 521 / Cr 701 Sales"],
      "e": ["Reversed.", "The debt was already moved to 412.", "Not a new sale."], "y": "The bill receivable is settled."},
     {"q": "BUYER: the business accepts a bill of 250 000 FCFA drawn by its supplier.", "r": "Dr 401 Suppliers / Cr 402 Suppliers, bills payable", "w": ["Dr 402 / Cr 401", "Dr 401 / Cr 521 Bank", "Dr 412 / Cr 411"],
      "e": ["Reversed.", "Nothing is paid yet.", "Those are the seller's accounts."], "y": "The debt becomes a bill payable."}]),
   num("a3-10-bal", 2, "At the start of the month, {'412'} Bills receivable has a balance of {o} FCFA. Bills of {a} FCFA are accepted by customers and bills of {p} FCFA are paid. What is the closing balance (FCFA)?", "o + a - p",
       ["New bills increase {'412'}: {o} + {a} = {o + a}.", "Bills paid decrease it: {o + a} − {p} = {answer} FCFA."],
       vars={"o": {"int": [100000, 600000], "step": 50000}, "a": {"int": [100000, 500000], "step": 50000}, "p": {"int": [100000, 400000], "step": 50000}},
       misc=[("swap", "o - a + p", "Accepted bills increase the balance; paid bills decrease it.")],
       unit="FCFA", sources=SRC, where=["o + a - p > 0"]),
   num("a3-10-days", 3, "A bill dated 1 March (non-leap year) is payable {n} days later. Counting 1 January as day 1, what is the day number of its due date?", "60 + n",
       ["1 March is day {60} of a non-leap year ({31} + {28} + {1}).", "Due date = day {60} + {n} = day {answer}."],
       vars={"n": {"pick": [30, 45, 60, 90]}},
       misc=[("nojan", "n", "Count the days in January and February too: {1} March is day {60}.")],
       review="authored", sources=SRC)],
  learn=learn(
    [("Paying later, in writing",
      "When a customer cannot pay at once, the seller may ask for a trade bill (effet de commerce): a document in which the customer promises, or is ordered, to pay a sum on a fixed date, the maturity date.\n"
      "Bills of exchange and promissory notes are common trade bills. They give legal proof of the debt and a clear payment date."),
     ("The seller's entries",
      "• When the customer accepts the bill, the debt changes form: debit {'412 Customers, bills receivable'}, credit {'411 Customers'}.\n"
      "• At maturity, when the bill is paid: debit {'521 Bank'}, credit {'412'}.\n"
      "If the seller needs cash before maturity, it can discount the bill at a bank and receive the amount less interest."),
     ("The buyer's entries",
      "• Accepting a bill drawn by a supplier: debit {'401 Suppliers'}, credit {'402 Suppliers, bills payable'}.\n• Paying it at maturity: debit {'402'}, credit {'521 Bank'}.\n"
      "Each side moves the debt from the ordinary account ({'411'} or {'401'}) to the bills account ({'412'} or {'402'}).")],
    key_words=[("trade bill", "a written promise or order to pay on a fixed date"), ("maturity", "the date payment is due"),
               ("bills receivable", "account {'412'}: bills the business will collect"), ("bills payable", "account {'402'}: bills the business must pay")],
    examples=[E("Dr 412 / Cr 411") + " (seller: bill accepted)", E("Dr 521 / Cr 412") + " (seller: bill paid)", E("Dr 401 / Cr 402") + " (buyer: bill accepted)"],
    mistake=("The seller records a new sale when the bill is accepted", "Accepting a bill only changes the form of the existing debt: Dr {'412'} / Cr {'411'}",
             "The sale was recorded earlier; the bill is just a new way of owing.")))
