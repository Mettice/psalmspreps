"""Form 3 Accounting, Term 1 (OHADA), rows 4-8 and 10 (financing, investment, trading, containers, cash settlement, trade bills).
Run: python tools/authoring/form3/acc2.py"""
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


def entries(id, level, prompt, items, figure=None):
    """Which journal entry records this? items: {q, r, w[3], e[3], y}: authored entries, each wrong one explained."""
    return bank(id, level, prompt, items, SRC, figure=figure)


# ---------------------------------------------------------------- 4. Financing transactions
L.lesson(D, S, 4, ("a3-4", "Accounting for financing transactions: capital and loans"), [1, 2],
  "Financing transactions bring long-term money into the enterprise.\n"
  "• Capital contributed by the owner: debit 521 Bank (or 571 Cash, or the asset given), credit 101 Capital.\n"
  "• Loan received from a bank: debit 521 Bank, credit 162 Loans from credit institutions.\n"
  "• Repayment of the loan: debit 162 Loans, credit 521 Bank. Interest paid is an expense: debit 671 Interest, credit 521 Bank.\n"
  "Capital and loans are resources (class 1); the money received is in treasury (class 5).",
  worked({"c": 2000000, "l": 1500000},
         "Ms Ngozi starts a business: she pays {c} FCFA into the business bank account and the bank lends the business {l} FCFA. Give the entries and the bank balance.",
         ["Capital: debit {'521 Bank'} {c}; credit {'101 Capital'} {c}.", "Loan: debit {'521 Bank'} {l}; credit {'162 Loans'} {l}.",
          "Bank balance = {c} + {l} = {c + l} FCFA."], "Bank {c + l} FCFA", checks=["c + l == 3500000"]),
  [card("c3a4-1", "The owner's contribution is credited to Capital.",
        [E("Dr 521 Bank / Cr 101 Capital")], "a3-4-cap"),
   card("c3a4-2", "A bank loan is credited to Loans.",
        [E("Dr 521 Bank / Cr 162 Loans")], "a3-4-loan"),
   card("c3a4-3", "Repaying the loan reduces both Loans and Bank.",
        [E("Dr 162 Loans / Cr 521 Bank")], "a3-4-bank")],
  [entries("a3-4-cap", 1, "Which entry records this? {X.q}", [
     {"q": "The owner pays 1 000 000 FCFA into the business bank account.", "r": "Dr 521 Bank / Cr 101 Capital", "w": ["Dr 101 Capital / Cr 521 Bank", "Dr 521 Bank / Cr 162 Loans", "Dr 571 Cash / Cr 701 Sales"],
      "e": ["Reversed: money comes into the bank, so Bank is debited.", "It is the owner's money, not a loan.", "It is not a sale."], "y": "Bank increases (debit); Capital increases (credit)."},
     {"q": "The owner brings 300 000 FCFA in cash to start the business.", "r": "Dr 571 Cash / Cr 101 Capital", "w": ["Dr 101 Capital / Cr 571 Cash", "Dr 571 Cash / Cr 162 Loans", "Dr 601 Purchases / Cr 571 Cash"],
      "e": ["Reversed.", "Not a loan.", "Not a purchase."], "y": "Cash comes in from the owner."},
     {"q": "The owner contributes a car worth 2 500 000 FCFA to the business.", "r": "Dr 245 Transport equipment / Cr 101 Capital", "w": ["Dr 101 Capital / Cr 245 Transport equipment", "Dr 521 Bank / Cr 101 Capital", "Dr 245 Transport equipment / Cr 162 Loans"],
      "e": ["Reversed.", "No money moves through the bank.", "It is the owner's contribution, not a loan."], "y": "The asset received is debited; capital is credited."}]),
   entries("a3-4-loan", 1, "Which entry records this? {X.q}", [
     {"q": "The business receives a bank loan of 5 000 000 FCFA into its account.", "r": "Dr 521 Bank / Cr 162 Loans", "w": ["Dr 162 Loans / Cr 521 Bank", "Dr 521 Bank / Cr 101 Capital", "Dr 671 Interest / Cr 521 Bank"],
      "e": ["That is a repayment.", "A loan is not the owner's capital.", "Interest is an expense paid later."], "y": "Bank increases; the debt (Loans) increases."},
     {"q": "The business repays 500 000 FCFA of its loan by bank transfer.", "r": "Dr 162 Loans / Cr 521 Bank", "w": ["Dr 521 Bank / Cr 162 Loans", "Dr 101 Capital / Cr 521 Bank", "Dr 162 Loans / Cr 101 Capital"],
      "e": ["That is receiving a loan.", "Capital is not repaid here.", "The money leaves the bank."], "y": "The debt falls (debit Loans); Bank falls (credit)."},
     {"q": "The business pays 60 000 FCFA interest on its loan by bank.", "r": "Dr 671 Interest / Cr 521 Bank", "w": ["Dr 162 Loans / Cr 521 Bank", "Dr 521 Bank / Cr 671 Interest", "Dr 671 Interest / Cr 101 Capital"],
      "e": ["Interest does not reduce the loan itself.", "Reversed.", "It is paid from the bank."], "y": "Interest is an expense (class 6)."}]),
   num("a3-4-bank", 2, "A business receives capital of {c} FCFA and a loan of {l} FCFA into its bank account, then repays {r} FCFA of the loan. What is the bank balance (FCFA)?", "c + l - r",
       ["Bank: + {c} (capital) + {l} (loan) − {r} (repayment).", "= {answer} FCFA."],
       vars={"c": {"int": [500000, 3000000], "step": 100000}, "l": {"int": [500000, 3000000], "step": 100000}, "r": {"int": [100000, 500000], "step": 50000}},
       misc=[("norepay", "c + l", "The repayment reduces the bank balance."), ("noloan", "c - r", "The loan received also adds to the bank.")],
       unit="FCFA", sources=SRC),
   num("a3-4-left", 3, "A loan of {l} FCFA is repaid in equal yearly instalments of {i} FCFA. How much is still owed after {n} instalments (FCFA)?", "l - i * n",
       ["Repaid so far = {i} × {n} = {i * n} FCFA.", "Still owed = {l} − {i * n} = {answer} FCFA (the balance of {'162'} Loans)."],
       vars={"i": {"int": [100000, 500000], "step": 50000}, "m": {"int": [4, 10]}, "l": {"expr": "i * m"}, "n": {"int": [1, 3]}},
       misc=[("paid", "i * n", "That is the amount repaid. The question asks what is still owed.")],
       unit="FCFA", sources=SRC)],
  learn=learn(
    [("Where the money comes from",
      "A new business needs money to start. The two main long-term sources are the owner's capital and loans.\n"
      "Both are resources recorded in class {1}: {'101 Capital'} for what the owner puts in, {'162 Loans from credit institutions'} for money borrowed from a bank."),
     ("The entries",
      "• Capital paid into the bank: debit {'521 Bank'}, credit {'101 Capital'}. Paid in cash: debit {'571 Cash'}. If the owner brings a car, debit {'245 Transport equipment'}.\n"
      "• Loan received: debit {'521 Bank'}, credit {'162 Loans'}.\n"
      "• Loan repaid: debit {'162 Loans'}, credit {'521 Bank'}.\n"
      "• Interest paid: debit {'671 Interest'} (an expense), credit {'521 Bank'}."),
     ("Following the bank balance",
      "Each financing transaction changes the bank balance: capital and loans add to it; repayments and interest take from it.\n"
      "Capital {2000000} + loan {1500000} − repayment {300000} leaves {3200000} FCFA in the bank, and the loan account shows {1200000} FCFA still owed.")],
    key_words=[("capital", "money or assets contributed by the owner"), ("loan", "money borrowed that must be repaid"),
               ("interest", "the cost of borrowing, an expense"), ("financing transaction", "a transaction that brings long-term funds")],
    examples=[E("Dr 521 Bank / Cr 101 Capital"), E("Dr 521 Bank / Cr 162 Loans"), E("Dr 671 Interest / Cr 521 Bank")],
    mistake=("A loan is credited to Capital", "A loan is credited to {'162'} Loans",
             "The loan belongs to the bank and must be repaid; capital belongs to the owner.")))

# ---------------------------------------------------------------- 5. Investment transactions
L.lesson(D, S, 5, ("a3-5", "Accounting for investment transactions: fixed assets acquired"), [3, 4],
  "Investment transactions buy fixed assets: items kept and used for more than one year (class 2): 231 Buildings, 241 Equipment, 244 Office furniture and equipment, 245 Transport equipment, 2183 Computer equipment.\n"
  "Purchase on credit: debit the asset account (HT), debit 4451 VAT recoverable on fixed assets, credit 481 Suppliers of fixed assets (TTC).\n"
  "Payment by bank: debit 481 Suppliers of fixed assets, credit 521 Bank.\n"
  "Purchase paid at once: credit 521 Bank (or 571 Cash) directly.\n"
  "Fixed assets are not expenses: they are recorded in class 2.",
  worked({"ht": 4000000},
         "A business buys a delivery van for {ht} FCFA HT on credit (VAT {19.25}%). Give the entry.",
         ["VAT = {19.25}% × {ht} = {ht * 0.1925} FCFA; TTC = {ht * 1.1925} FCFA.",
          "Debit {'245 Transport equipment'} {ht}; debit {'4451 VAT recoverable'} {ht * 0.1925}.", "Credit {'481 Suppliers of fixed assets'} {ht * 1.1925}."],
         "Dr {'245'} {ht}, Dr {'4451'} {ht * 0.1925} / Cr {'481'} {ht * 1.1925}", checks=["ht * 0.1925 == 770000"]),
  [card("c3a5-1", "A fixed asset is kept and used for more than a year.",
        ["A computer, a vehicle, a building"], "a3-5-asset"),
   card("c3a5-2", "Fixed assets bought on credit: credit Suppliers of fixed assets.",
        [E("Cr 481 Suppliers of fixed assets")], "a3-5-entry"),
   card("c3a5-3", "The VAT on fixed assets is recoverable.",
        [E("Dr 4451 VAT recoverable on fixed assets")], "a3-5-ttc")],
  [bank("a3-5-asset", 1, "Is this a fixed asset? {X.q}", [
     {"q": "A photocopier bought for the office, to be used for five years", "r": "Yes: office equipment (class 2)", "w": ["No: it is an expense of the month", "No: it is stock for sale", "No: it is treasury"],
      "e": ["Items used for years are capitalised.", "It is not bought to resell.", "Treasury is cash and bank."], "y": "Long-term use makes it a fixed asset."},
     {"q": "Reams of paper used up in a month", "r": "No: it is an expense (class 6)", "w": ["Yes: office equipment", "Yes: a building", "Yes: transport equipment"],
      "e": ["Paper is consumed quickly.", "Not a building.", "Not a vehicle."], "y": "Consumables are expenses."},
     {"q": "A lorry bought by a transport company", "r": "Yes: transport equipment (245)", "w": ["No: it is a purchase of goods (601)", "No: it is capital", "No: it is a loan"],
      "e": ["The company uses it, it does not resell it.", "Capital is the owner's contribution.", "A loan is borrowed money."], "y": "Used for many years: fixed asset."}], SRC),
   entries("a3-5-entry", 1, "Which entry records this? {X.q}", [
     {"q": "Office furniture is bought on credit for 500 000 FCFA HT (VAT 96 250).", "r": "Dr 244 Office furniture 500 000; Dr 4451 VAT 96 250 / Cr 481 Suppliers of fixed assets 596 250", "w": ["Dr 601 Purchases 596 250 / Cr 401 Suppliers 596 250", "Dr 481 Suppliers 596 250 / Cr 244 Office furniture 596 250", "Dr 244 Office furniture 596 250 / Cr 521 Bank 596 250"],
      "e": ["Furniture used by the business is a fixed asset, not goods for resale.", "Reversed.", "It was bought on credit, and the VAT is recorded separately."], "y": "Asset HT and recoverable VAT debited; supplier of fixed assets credited TTC."},
     {"q": "The supplier of fixed assets is paid 596 250 FCFA by cheque.", "r": "Dr 481 Suppliers of fixed assets / Cr 521 Bank", "w": ["Dr 521 Bank / Cr 481 Suppliers of fixed assets", "Dr 244 Office furniture / Cr 521 Bank", "Dr 401 Suppliers / Cr 571 Cash"],
      "e": ["Reversed: money leaves the bank.", "The asset was already recorded.", "Paid by cheque from the bank, to the supplier of fixed assets."], "y": "The debt falls; the bank falls."},
     {"q": "A computer is bought and paid at once by bank: 800 000 FCFA HT, VAT 154 000.", "r": "Dr 2183 Computer equipment 800 000; Dr 4451 VAT 154 000 / Cr 521 Bank 954 000", "w": ["Dr 601 Purchases 954 000 / Cr 521 Bank 954 000", "Dr 2183 Computer equipment 954 000 / Cr 481 Suppliers 954 000", "Dr 521 Bank 954 000 / Cr 2183 Computer equipment 954 000"],
      "e": ["A computer for use is a fixed asset.", "It was paid at once by bank, and VAT is separate.", "Reversed."], "y": "Paid immediately: credit Bank."}]),
   num("a3-5-ttc", 2, "Equipment is bought for {ht} FCFA HT (VAT {19.25}%). What amount is credited to {'481'} Suppliers of fixed assets (FCFA)?", "ht + vat",
       ["VAT = {vat} FCFA.", "TTC = {ht} + {vat} = {answer} FCFA."],
       vars=HT, misc=[("ht", "ht", "The supplier is owed the amount including tax."), ("vat", "vat", "That is only the VAT.")],
       unit="FCFA", sources=SRC),
   num("a3-5-total", 3, "During the year a business buys a building for {b} FCFA and a vehicle for {v} FCFA (HT), and pays {r} FCFA to suppliers of fixed assets. If nothing was owed before, how much is still owed to suppliers of fixed assets, including VAT ({19.25}%) (FCFA)?", "(b + v) * 11925 / 10000 - r",
       ["TTC owed = ({b} + {v}) × {1.1925} = {(b + v) * 11925 / 10000} FCFA.", "Still owed = {(b + v) * 11925 / 10000} − {r} = {answer} FCFA."],
       vars={"bk": {"int": [5, 25]}, "vk": {"int": [2, 10]}, "b": {"expr": "bk * 400000"}, "v": {"expr": "vk * 400000"}, "r": {"int": [1000000, 4000000], "step": 500000}},
       misc=[("ht", "b + v - r", "The suppliers are owed the amounts including VAT."), ("all", "(b + v) * 11925 / 10000", "Subtract what has been paid.")],
       unit="FCFA", sources=SRC, where=["(b + v) * 11925 / 10000 > r"])],
  learn=learn(
    [("Investing in fixed assets",
      "A fixed asset is something the enterprise keeps and uses for more than one year to do its work: buildings, machines, office furniture, computers, vehicles. They are recorded in class {2}, not as expenses.\n"
      "Paper, ink and fuel, used up quickly, are expenses (class {6})."),
     ("The entries",
      "Bought on credit:\n• debit the asset account with the amount excluding tax (e.g. {'245 Transport equipment'});\n• debit {'4451 VAT recoverable on fixed assets'} with the VAT;\n"
      "• credit {'481 Suppliers of fixed assets'} with the amount including tax.\n"
      "When the supplier is paid: debit {'481'}, credit {'521 Bank'}. Paid at once: credit {'521 Bank'} directly instead of {'481'}."),
     ("Why a separate supplier account?",
      "{'401 Suppliers'} is for suppliers of goods and services used in daily trading; {'481'} is for suppliers of fixed assets. Keeping them apart shows clearly how much the business owes for investments.\n"
      "Example: a van at {4000000} FCFA HT: VAT {770000} FCFA, TTC {4770000} FCFA owed to the supplier of fixed assets.")],
    key_words=[("fixed asset", "an item kept and used for more than a year"), ("investment transaction", "the purchase of fixed assets"),
               ("supplier of fixed assets", "account {'481'}: amounts owed for fixed assets bought on credit")],
    examples=[E("245 Transport equipment"), E("244 Office furniture"), E("2183 Computer equipment"), E("481 Suppliers of fixed assets")],
    mistake=("A delivery van is recorded in {'601'} Purchases of goods", "It is a fixed asset: {'245'} Transport equipment",
             "{'601'} is for goods bought to resell; the van is used for years.")))
