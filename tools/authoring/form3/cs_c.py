"""Form 3 Computer Science, Term 1, rows 21-32 (algorithmic instructions, flowcharts, application software, IP, DRM,
Creative Commons, off-the-shelf and bespoke software). Run: python tools/authoring/form3/cs_c.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"

# ---------------------------------------------------------------- 21. Algorithmic instructions
SRC = ["algorithms"]
L.lesson(D, S, 21, ("s3-21", "Algorithmic instructions: input, output, assignment, selection and iteration"), [20],
  "Basic instructions used in pseudocode:\n"
  "• INPUT / READ: get data. OUTPUT / PRINT: show results.\n• Assignment: store a value in a variable, e.g. total ← total + mark.\n"
  "• Sequence: steps carried out one after another.\n• Selection: IF condition THEN … ELSE … ENDIF chooses between paths.\n"
  "• Iteration (loops): FOR i ← 1 TO n … NEXT i (a fixed number of times); WHILE condition DO … ENDWHILE (while a condition is true); REPEAT … UNTIL condition.\n"
  "Comparison operators: =, <>, <, >, <=, >=.",
  worked({"m": 13},
         "What is output? INPUT mark (mark = {m}); IF mark >= {10} THEN OUTPUT 'Pass' ELSE OUTPUT 'Fail' ENDIF.",
         ["mark = {m}.", "Is {m} >= {10}? {m >= 10 ? 'Yes' : 'No'}.", "So the output is {m >= 10 ? 'Pass' : 'Fail'}."], "{m >= 10 ? 'Pass' : 'Fail'}"),
  [card("c3s21-1", "Selection: IF … THEN … ELSE chooses what to do.",
        ["IF age >= {18} THEN OUTPUT 'Adult'"], "s3-21-if"),
   card("c3s21-2", "Iteration repeats steps: FOR, WHILE, REPEAT … UNTIL.",
        ["FOR i ← {1} TO {5}: OUTPUT i prints {1} to {5}."], "s3-21-loop"),
   card("c3s21-3", "Assignment stores a value: total ← total + x.",
        ["The arrow means 'becomes'."], "s3-21-kind")],
  [mcq("s3-21-if", 1, "What is output? mark ← {m}; IF mark >= {p} THEN OUTPUT 'Pass' ELSE OUTPUT 'Fail' ENDIF",
       "{traceIf(m, p - 1, 'Pass', 'Fail')}", [("{traceIf(m, p - 1, 'Fail', 'Pass')}", "flip"), ("{str(m)}", "mark"), ("{'Pass Fail'}", "both")],
       ["Is {m} >= {p}? {m >= p ? 'Yes' : 'No'}.", "So {answer} is output."],
       vars={"m": {"int": [0, 20]}, "p": {"pick": [10, 12]}},
       misc=[("flip", "Check the condition: {m} >= {p} is {m >= p ? 'true' : 'false'}."), ("mark", "The mark itself is not output; only Pass or Fail."),
             ("both", "Only one branch of IF … ELSE runs.")],
       sources=SRC),
   num("s3-21-loop", 1, "How many times is 'Hello' printed? FOR i ← {a} TO {b}: OUTPUT 'Hello' NEXT i", "b - a + 1",
       ["i takes the values {a}, {a + 1}, …, {b}.", "That is {b} − {a} + {1} = {answer} times."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [6, 15]}},
       misc=[("minus", "b - a", "Count both ends: add {1}."), ("b", "b", "The loop starts at {a}, not {1}.")],
       sources=SRC, where=["a != 1"]),
   bank("s3-21-kind", 2, "Which kind of instruction is this? {X.q}", [
     {"q": "IF temperature > 30 THEN OUTPUT 'Hot' ENDIF", "r": "selection", "w": ["iteration", "assignment", "input"],
      "e": ["Nothing is repeated.", "No value is stored.", "No data is read."], "y": "IF chooses a path."},
     {"q": "WHILE balance > 0 DO … ENDWHILE", "r": "iteration", "w": ["selection", "output", "assignment"],
      "e": ["It repeats, not just chooses once.", "It does not print.", "It does not store a value by itself."], "y": "A loop repeats while the condition is true."},
     {"q": "total ← total + price", "r": "assignment", "w": ["selection", "iteration", "output"],
      "e": ["No choice is made.", "Nothing repeats here.", "Nothing is displayed."], "y": "A new value is stored in total."},
     {"q": "INPUT name", "r": "input", "w": ["output", "selection", "iteration"],
      "e": ["Nothing is displayed.", "No choice is made.", "Nothing repeats."], "y": "Data is read into the variable name."}], SRC),
   num("s3-21-sum", 3, "What is output? total ← {0}; FOR i ← {1} TO {n}: total ← total + i NEXT i; OUTPUT total", "n * (n + 1) / 2",
       ["The loop adds {1} + {2} + … + {n}.", "Sum = {n} × {n + 1} ÷ {2} = {answer}."],
       vars={"n": {"int": [3, 12]}},
       misc=[("n", "n", "That is the last value of i. total adds up every i."), ("square", "n * n", "Add {1} + {2} + … + {n}, not {n} × {n}.")],
       sources=SRC)],
  learn=learn(
    [("The building blocks",
      "Every algorithm is made from a few kinds of instruction:\n• Input (INPUT, READ): get data, e.g. INPUT mark.\n• Output (OUTPUT, PRINT): show results.\n"
      "• Assignment: store a value in a variable, e.g. total ← total + mark (read the arrow as 'becomes').\n• Sequence: carry out steps in order, one after another."),
     ("Selection",
      "Selection lets an algorithm choose. IF condition THEN … ELSE … ENDIF.\n"
      "IF mark >= {10} THEN OUTPUT 'Pass' ELSE OUTPUT 'Fail' ENDIF.\n"
      "Conditions use comparison operators: = (equal), <> (not equal), <, >, <=, >=. Only one branch runs."),
     ("Iteration (loops)",
      "Loops repeat steps:\n• FOR i ← {1} TO {5} … NEXT i: repeats a fixed number of times ({5}).\n• WHILE condition DO … ENDWHILE: repeats while the condition is true (it may run zero times).\n"
      "• REPEAT … UNTIL condition: runs at least once, until the condition becomes true.\n"
      "total ← {0}; FOR i ← {1} TO {4}: total ← total + i gives {1} + {2} + {3} + {4} = {10}.")],
    key_words=[("assignment", "storing a value in a variable"), ("selection", "choosing between paths with IF"), ("iteration", "repeating steps in a loop"),
               ("condition", "a test that is true or false")],
    examples=["IF x > {0} THEN OUTPUT 'positive'", "FOR i ← {1} TO {3}: OUTPUT i", "count ← count + {1}"],
    mistake=("FOR i ← {2} TO {5} runs {3} times", "It runs {4} times: {2}, {3}, {4}, {5}",
             "Count both the first and last values: last − first + {1}.")))

# ---------------------------------------------------------------- 22. Flowcharts
L.lesson(D, S, 22, ("s3-22", "Flowcharts"), [21],
  "A flowchart shows an algorithm as a diagram. Standard symbols:\n"
  "• Oval (terminal): Start and Stop.\n• Parallelogram: input or output.\n• Rectangle: process (calculation, assignment).\n"
  "• Diamond: decision (a yes/no question), with two exits.\n• Arrows (flow lines): show the order of steps.\n"
  "A loop is drawn as an arrow going back to an earlier step. Every flowchart has one Start and at least one Stop.",
  worked({"l": 6, "w": 4},
         "A flowchart: Start → Input L, W → A ← L × W → Output A → Stop. What is output when L = {l} and W = {w}?",
         ["Input: L = {l}, W = {w}.", "Process: A = {l} × {w} = {l * w}.", "Output: {l * w}."], "{l * w}", checks=["l * w == 24"]),
  [card("c3s22-1", "Diamond = decision; rectangle = process; parallelogram = input/output; oval = start/stop.",
        ["'Is mark >= {10}?' goes in a diamond."], "s3-22-symbol"),
   card("c3s22-2", "Arrows show the order; an arrow going back makes a loop.",
        ["Repeat until a correct PIN is entered."], "s3-22-trace"),
   card("c3s22-3", "A decision has two exits: Yes and No.",
        ["Yes → 'Pass'; No → 'Fail'"], "s3-22-dec")],
  [bank("s3-22-symbol", 1, "Which flowchart symbol is used for this? {X.q}", [
     {"q": "'Is the number greater than 50?'", "r": "diamond (decision)", "w": ["rectangle (process)", "parallelogram (input/output)", "oval (terminal)"],
      "e": ["A process does a calculation.", "Input/output reads or shows data.", "Terminals are Start and Stop."], "y": "A yes/no question is a decision."},
     {"q": "'Read the price'", "r": "parallelogram (input/output)", "w": ["diamond (decision)", "rectangle (process)", "oval (terminal)"],
      "e": ["No question is asked.", "Reading data is input.", "It is not Start or Stop."], "y": "Input and output use parallelograms."},
     {"q": "'total ← price × quantity'", "r": "rectangle (process)", "w": ["parallelogram (input/output)", "diamond (decision)", "oval (terminal)"],
      "e": ["Nothing is read or shown.", "No question is asked.", "It is not Start or Stop."], "y": "Calculations are processes."},
     {"q": "'Start'", "r": "oval (terminal)", "w": ["rectangle (process)", "diamond (decision)", "parallelogram (input/output)"],
      "e": ["Not a calculation.", "Not a question.", "Not input or output."], "y": "Start and Stop are terminals."}], SRC),
   num("s3-22-trace", 2, "Flowchart: Start → Input n → Is n > {k}? Yes → n ← n − {d}, then go back to the question; No → Output n → Stop. What is output when n = {n}?", "k + r - d",
       ["While n > {k}, subtract {d}: {n} goes down in steps of {d}.", "The first value that is not greater than {k} is {k + r - d}.", "Output: {answer}."],
       vars={"k": {"int": [5, 15]}, "d": {"int": [2, 5]}, "j": {"int": [1, 5]}, "r": {"int": [1, "d - 1"]}, "n": {"expr": "k + d * j + r"}},
       misc=[("once", "n - d", "The arrow goes back: keep subtracting while n > {k}."), ("k", "k", "{k} is never reached exactly here: list the values {n}, {n - d}, … until one is not greater than {k}.")],
       sources=SRC),
   bank("s3-22-dec", 1, "{X.q}", [
     {"q": "How many exits does a decision symbol have?", "r": "two (Yes and No)", "w": ["one", "none", "four"],
      "e": ["A decision chooses between two paths.", "It must lead somewhere.", "Only two answers to a yes/no question."], "y": "One path for Yes, one for No."},
     {"q": "How is a loop shown on a flowchart?", "r": "by an arrow going back to an earlier step", "w": ["by a double oval", "by a red rectangle", "it cannot be shown"],
      "e": ["Not a standard symbol.", "Colour does not mean anything.", "Loops are common in flowcharts."], "y": "Flow returns to repeat steps."},
     {"q": "Which symbol starts every flowchart?", "r": "an oval labelled Start", "w": ["a diamond", "a parallelogram", "a rectangle"],
      "e": ["Diamonds are decisions.", "Parallelograms are input/output.", "Rectangles are processes."], "y": "Terminals mark the beginning and end."}], SRC),
   num("s3-22-max", 3, "Flowchart: Start → Input a, b → Is a > b? Yes → Output a; No → Output b → Stop. What is output when a = {a} and b = {b}?", "max(a, b)",
       ["Is {a} > {b}? {a > b ? 'Yes' : 'No'}.", "So {answer} is output: the larger number."],
       vars={"a": {"int": [1, 50]}, "b": {"int": [1, 50]}},
       misc=[("min", "min(a, b)", "The Yes branch outputs a only when a is bigger; this flowchart outputs the larger number.")],
       sources=SRC, where=["a != b"])],
  learn=learn(
    [("Algorithms as diagrams",
      "A flowchart shows the steps of an algorithm with standard shapes joined by arrows. It makes the order of steps and the decisions easy to see.\n"
      "• Oval (terminal): Start and Stop.\n• Parallelogram: input or output (Read mark, Print result).\n• Rectangle: process (total ← total + mark).\n"
      "• Diamond: decision, a yes/no question with two exits.\n• Arrows (flow lines): the order to follow."),
     ("Decisions and loops",
      "A decision diamond asks a question such as 'Is mark ≥ {10}?'. One arrow leaves for Yes and another for No.\n"
      "A loop is made by an arrow that goes back to an earlier step: for example, 'Is the PIN correct?' No → back to 'Input PIN'.\n"
      "Make sure every loop can end, or the algorithm will run forever."),
     ("Reading a flowchart",
      "Follow the arrows from Start with the given values, writing down each variable as it changes, until you reach Stop.\n"
      "Start → Input L, W → A ← L × W → Output A → Stop. With L = {6} and W = {4}, the output is {24}.")],
    key_words=[("flowchart", "a diagram of an algorithm using standard symbols"), ("terminal", "Start or Stop (oval)"), ("decision", "a yes/no question (diamond)"),
               ("process", "a calculation or assignment (rectangle)"), ("flow line", "an arrow showing the order of steps")],
    examples=["Diamond: 'Is age ≥ {18}?'", "Parallelogram: 'Input name'", "Rectangle: 'A ← L × W'"],
    mistake=("Using a rectangle for a yes/no question", "Use a diamond for every decision",
             "Diamonds have two exits for the two answers.")))

# ---------------------------------------------------------------- 24-26. Application software
SRC = ["software"]
L.lesson(D, S, 24, ("s3-24", "Common application software 1: word processors and spreadsheets"), [],
  "Application software helps users do particular tasks.\n"
  "• Word processor (e.g. Microsoft Word, LibreOffice Writer): letters, reports, CVs; features: formatting, spell check, tables, mail merge, headers and footers.\n"
  "• Spreadsheet (e.g. Microsoft Excel, LibreOffice Calc): data in rows and columns of cells; formulas and functions calculate automatically; charts; sorting.\n"
  "Cells have references such as B3 (column B, row 3). Formulas start with =: =B2*C2, =SUM(B2:B6), =AVERAGE(C2:C10), =MAX(…), =MIN(…).",
  worked({"a": 250, "b": 400, "c": 150},
         "Cells {'B2'}, {'B3'} and {'B4'} contain {a}, {b} and {c}. What does =SUM({'B2'}:{'B4'}) display?",
         ["SUM adds every cell from {'B2'} to {'B4'}.", "{a} + {b} + {c} = {a + b + c}."], "{a + b + c}", checks=["a + b + c == 800"]),
  [card("c3s24-1", "A word processor is for documents; a spreadsheet is for calculations with data.",
        ["Letter: word processor. Budget: spreadsheet."], "s3-24-which"),
   card("c3s24-2", "Spreadsheet formulas start with = and update automatically.",
        ["=SUM({'A1'}:{'A5'}) adds five cells."], "s3-24-sum"),
   card("c3s24-3", "A cell reference names a column letter and a row number.",
        ["{'C4'}: column C, row {4}"], "s3-24-formula")],
  [bank("s3-24-which", 1, "Which software is best? {X.q}", [
     {"q": "Writing a letter of application for a job", "r": "word processor", "w": ["spreadsheet", "web browser", "antivirus"],
      "e": ["Spreadsheets are for numbers and tables of data.", "Browsers display web pages.", "Antivirus protects the computer."], "y": "Word processors format text documents."},
     {"q": "Keeping the monthly accounts of a provision store", "r": "spreadsheet", "w": ["word processor", "presentation software", "photo editor"],
      "e": ["Word processors are weak at calculations.", "Presentations show slides.", "Photo editors change images."], "y": "Spreadsheets calculate totals automatically."},
     {"q": "Sending the same letter to 200 parents with each name filled in", "r": "word processor with mail merge", "w": ["spreadsheet only", "a drawing program", "a calculator"],
      "e": ["A spreadsheet can hold the names, but the letters are merged in a word processor.", "Not for letters.", "Not for documents."], "y": "Mail merge combines a letter with a list of names."}], SRC),
   num("s3-24-sum", 1, "Cells {'A1'} to {'A4'} contain {a}, {b}, {c} and {d}. What does =SUM({'A1'}:{'A4'}) display?", "a + b + c + d",
       ["SUM adds all the cells from {'A1'} to {'A4'}.", "{a} + {b} + {c} + {d} = {answer}."],
       vars={"a": {"int": [10, 500], "step": 10}, "b": {"int": [10, 500], "step": 10}, "c": {"int": [10, 500], "step": 10}, "d": {"int": [10, 500], "step": 10}},
       misc=[("two", "a + d", "{'A1'}:{'A4'} means all cells from {'A1'} to {'A4'}, not just the two ends.")],
       sources=SRC),
   num("s3-24-formula", 2, "{'B2'} holds the price {p} FCFA and {'C2'} the quantity {q}. What does ={'B2'}*{'C2'} display?", "p * q",
       ["* means multiply.", "{p} × {q} = {answer}."],
       vars={"p": {"int": [100, 2000], "step": 50}, "q": {"int": [2, 20]}},
       misc=[("add", "p + q", "* is multiplication, not addition.")],
       sources=SRC),
   num("s3-24-avg", 3, "Cells {'D2'} to {'D5'} hold the marks {a}, {b}, {c} and {d}. What does =AVERAGE({'D2'}:{'D5'}) display?", "(a + b + c + d) / 4",
       ["AVERAGE adds the four marks and divides by {4}.", "({a} + {b} + {c} + {d}) ÷ {4} = {answer}."],
       vars={"a": {"int": [4, 20]}, "b": {"int": [4, 20]}, "c": {"int": [4, 20]}, "d": {"int": [4, 20]}},
       misc=[("sum", "a + b + c + d", "That is the SUM. AVERAGE divides by the number of cells."), ("max", "max(max(a, b), max(c, d))", "That is the MAX.")],
       sources=SRC, where=["(a + b + c + d) % 4 == 0", "max(max(a, b), max(c, d)) != (a + b + c + d) / 4"])],
  learn=learn(
    [("Software for tasks",
      "Application software lets users do jobs on a computer: write, calculate, present, draw, browse. System software (like the operating system) runs the computer itself.\n"
      "Two of the most used applications are the word processor and the spreadsheet."),
     ("Word processors",
      "Microsoft Word or LibreOffice Writer are used for letters, reports, CVs and notices. Features:\n• formatting text (bold, size, font, alignment);\n• spell and grammar check;\n• tables, pictures, headers and footers, page numbers;\n"
      "• mail merge: the same letter sent to many people with their own names and addresses filled in."),
     ("Spreadsheets",
      "Microsoft Excel or LibreOffice Calc arrange data in a grid of cells. Each cell has a reference: column letter + row number, such as {'B3'}.\n"
      "Formulas start with = and recalculate automatically when data changes: ={'B2'}*{'C2'} (multiply), =SUM({'B2'}:{'B6'}) (add a range), =AVERAGE({'C2'}:{'C10'}), =MAX(…), =MIN(…).\n"
      "Spreadsheets also sort data and draw charts: ideal for budgets, sales records and class marks.")],
    key_words=[("application software", "programs that help users do tasks"), ("cell reference", "the address of a cell, e.g. {'B3'}"),
               ("formula", "a calculation in a spreadsheet, starting with ="), ("mail merge", "combining a letter with a list of names")],
    examples=["=SUM({'A1'}:{'A4'})", "={'B2'}*{'C2'}", "=AVERAGE({'D2'}:{'D5'})", "Mail merge for {200} parents"],
    mistake=("=SUM({'A1'}:{'A4'}) adds only {'A1'} and {'A4'}", "It adds {'A1'}, {'A2'}, {'A3'} and {'A4'}",
             "The colon means 'from … to …': every cell in the range.")))

L.lesson(D, S, 25, ("s3-25", "Common application software 2: presentations and databases"), [24],
  "• Presentation software (e.g. Microsoft PowerPoint, LibreOffice Impress): slides with text, pictures, charts, animations and transitions, for talks and lessons. Good slides: few words, large clear text, relevant images.\n"
  "• Database management software (e.g. Microsoft Access): stores large amounts of organised data so it can be searched, sorted and reported.\n"
  "Database terms: a table holds data about one kind of thing; a record is one row (one pupil); a field is one column (Surname); a key field (primary key) is unique for each record (Pupil ID).\n"
  "Queries find records that match conditions (e.g. Class = 'Form 3' AND Mark > 15).",
  worked({},
         "A school database table holds pupils' ID, name, class and fee balance. Name the key field and explain why.",
         ["Names can be repeated (two pupils called Ngozi).", "The ID is different for every pupil.", "So Pupil ID is the key field: it identifies each record uniquely."],
         "Pupil ID (unique for each pupil)"),
  [card("c3s25-1", "Presentation software makes slides for talks.",
        ["A science fair presentation"], "s3-25-which"),
   card("c3s25-2", "A record is a row; a field is a column; the key field is unique.",
        ["Record: one pupil. Field: Class."], "s3-25-term"),
   card("c3s25-3", "A query finds the records that match conditions.",
        ["Mark > {15}"], "s3-25-query")],
  [bank("s3-25-which", 1, "Which software is best? {X.q}", [
     {"q": "Showing slides at a school science fair", "r": "presentation software", "w": ["database software", "spreadsheet", "antivirus"],
      "e": ["Databases store and search data.", "Spreadsheets calculate.", "Antivirus protects."], "y": "Slides with pictures and animation."},
     {"q": "Storing and searching the records of 1500 pupils", "r": "database software", "w": ["presentation software", "word processor", "drawing program"],
      "e": ["Presentations are for showing slides.", "Hard to search many records.", "Not for records."], "y": "Databases search and sort large data sets."},
     {"q": "Finding all pupils who still owe fees", "r": "a database query", "w": ["a slide transition", "a word count", "a spell check"],
      "e": ["Transitions are for slides.", "Word count is for documents.", "Spell check is for text."], "y": "Queries select matching records."}], SRC),
   bank("s3-25-term", 1, "{X.q}", [
     {"q": "In a database table of pupils, what is a record?", "r": "all the data about one pupil (one row)", "w": ["one column, such as Surname", "the whole database", "a printed report"],
      "e": ["That is a field.", "A database can have many tables.", "A report is output."], "y": "Each row is a record."},
     {"q": "What is a field?", "r": "one category of data, such as Date of birth (a column)", "w": ["one pupil's data", "a slide", "a formula"],
      "e": ["That is a record.", "Slides are for presentations.", "Formulas are for spreadsheets."], "y": "Each column is a field."},
     {"q": "Why is Pupil ID used as the key field rather than Surname?", "r": "IDs are unique; surnames can be repeated", "w": ["Surnames are too long", "IDs are always numbers less than 10", "Key fields must be names"],
      "e": ["Length is not the reason.", "IDs can be any length.", "Key fields must be unique."], "y": "A primary key identifies each record."}], SRC),
   num("s3-25-query", 2, "A table has these marks: {a}, {b}, {c}, {d}, {e}, {f}. A query selects records with Mark > {k}. How many records are found?", "(a > k ? 1 : 0) + (b > k ? 1 : 0) + (c > k ? 1 : 0) + (d > k ? 1 : 0) + (e > k ? 1 : 0) + (f > k ? 1 : 0)",
       ["Check each mark against > {k}.", "Records found: {answer}."],
       vars={"a": {"int": [5, 20]}, "b": {"int": [5, 20]}, "c": {"int": [5, 20]}, "d": {"int": [5, 20]}, "e": {"int": [5, 20]}, "f": {"int": [5, 20]}, "k": {"int": [10, 15]}},
       misc=[("ge", "(a >= k ? 1 : 0) + (b >= k ? 1 : 0) + (c >= k ? 1 : 0) + (d >= k ? 1 : 0) + (e >= k ? 1 : 0) + (f >= k ? 1 : 0)", "> means greater than: a mark equal to {k} is not selected.")],
       sources=SRC, where=["a == k || b == k || c == k || d == k || e == k || f == k"]),
   bank("s3-25-slides", 3, "{X.q}", [
     {"q": "Which is good advice for presentation slides?", "r": "Use few words, large clear text and relevant pictures", "w": ["Fill every slide with long paragraphs", "Use tiny text to fit more", "Add as many animations as possible"],
      "e": ["Audiences cannot read long paragraphs while listening.", "Tiny text cannot be read from the back.", "Too many animations distract."], "y": "Slides support the speaker; they do not replace the talk."},
     {"q": "What is a slide transition?", "r": "the visual effect when moving from one slide to the next", "w": ["a type of database", "a spreadsheet formula", "a printer setting"],
      "e": ["Not a database.", "Not a formula.", "Not a printer setting."], "y": "Transitions are applied between slides."},
     {"q": "Why is a database better than a word-processed list for 1500 pupils' records?", "r": "It can quickly search, sort and report on the data", "w": ["It makes the text bold", "It checks spelling", "It adds animations"],
      "e": ["Formatting is a word-processing feature.", "That is not the main benefit.", "That is presentation software."], "y": "Databases manage large, structured data."}], SRC)],
  learn=learn(
    [("Presentation software",
      "PowerPoint, LibreOffice Impress and Google Slides make slides for talks, lessons and meetings. You can add text, pictures, charts, video, animations and transitions.\n"
      "Good slides use few words, big clear text, good contrast and relevant pictures. The speaker explains; the slides support."),
     ("Databases",
      "A database stores large amounts of organised data so it can be searched, sorted and reported. Schools, hospitals and banks use them.\n"
      "• A table holds data about one kind of thing (pupils).\n• A record is one row: everything about one pupil.\n• A field is one column: Surname, Class, Fee balance.\n"
      "• The key field (primary key) is unique for each record, such as Pupil ID."),
     ("Queries and reports",
      "A query asks the database for records that match conditions: Class = 'Form {3}' AND Fee balance > {0} finds Form {3} pupils who still owe fees.\n"
      "Remember: > means 'greater than', so a mark equal to the limit is not included; >= includes it.\n"
      "Reports present the results neatly for printing.")],
    key_words=[("presentation software", "software for making slide shows"), ("database", "an organised collection of data that can be searched"),
               ("record", "one row of data about one item"), ("field", "one column of data"), ("key field", "a field unique for each record")],
    examples=["Science fair: slides", "School register: database", "Query: Mark > {15}"],
    mistake=("A field is all the data about one pupil", "That is a record; a field is one column",
             "Records are rows; fields are columns.")))

L.lesson(D, S, 26, ("s3-26", "Common application software 3: graphics, multimedia, communication and utilities"), [24, 25],
  "Other common applications:\n• Graphics: drawing and photo editing (Paint, GIMP, Photoshop); design (Canva, Publisher) for posters and flyers.\n"
  "• Multimedia: playing and editing audio and video (VLC, Audacity, video editors).\n• Web browsers (Chrome, Firefox, Edge) to view websites; search engines to find information.\n"
  "• Communication: e-mail, messaging (WhatsApp), video calls (Zoom, Google Meet).\n• Utilities (system tools): antivirus, file compression (zip), backup, disk clean-up.\n"
  "General-purpose software does many tasks (a word processor); specialist software does one job (accounting or hospital software).",
  worked({},
         "A youth club in Buea wants to make a colourful poster and share it with members by phone. Which software would they use?",
         ["To design the poster: graphics/desktop publishing software (e.g. Canva or Publisher).", "To share it: a messaging app such as WhatsApp, or e-mail."],
         "Design software, then a messaging or e-mail app"),
  [card("c3s26-1", "Graphics software edits images and designs posters.",
        ["Removing red-eye from a photo"], "s3-26-which"),
   card("c3s26-2", "Utilities look after the computer: antivirus, backup, compression.",
        ["Zipping a folder before e-mailing it"], "s3-26-util"),
   card("c3s26-3", "General-purpose software does many tasks; specialist software does one.",
        ["Hospital patient software is specialist."], "s3-26-type")],
  [bank("s3-26-which", 1, "Which software is best? {X.q}", [
     {"q": "Cutting and joining clips for a school video", "r": "video editing software", "w": ["spreadsheet", "database", "antivirus"],
      "e": ["Spreadsheets calculate.", "Databases store records.", "Antivirus protects."], "y": "Multimedia software edits audio and video."},
     {"q": "Finding information about volcanoes online", "r": "a web browser with a search engine", "w": ["a word processor", "a photo editor", "a compression utility"],
      "e": ["Word processors write documents.", "Photo editors change images.", "Zip tools shrink files."], "y": "Browsers display web pages; search engines find them."},
     {"q": "Holding a lesson by video call with pupils at home", "r": "video-conferencing software (e.g. Zoom, Google Meet)", "w": ["a spreadsheet", "a drawing program", "a database"],
      "e": ["Not for calls.", "Not for calls.", "Not for calls."], "y": "Communication software connects people live."}], SRC),
   bank("s3-26-util", 1, "{X.q}", [
     {"q": "What does antivirus software do?", "r": "detects and removes malicious software", "w": ["edits photos", "writes letters", "speeds up the internet connection"],
      "e": ["That is graphics software.", "That is a word processor.", "It does not change the connection speed."], "y": "A utility that protects the system."},
     {"q": "Why compress (zip) a folder before e-mailing it?", "r": "To make the file smaller and send it as one file", "w": ["To make it bigger", "To delete it", "To print it"],
      "e": ["Compression reduces size.", "The data is kept.", "Printing is separate."], "y": "Smaller files send faster."},
     {"q": "Which is a utility program?", "r": "backup software", "w": ["a game", "a web browser", "a presentation program"],
      "e": ["Games are entertainment.", "Browsers are applications.", "Presentations are applications."], "y": "Utilities maintain and protect the computer."}], SRC),
   bank("s3-26-type", 2, "{X.q}", [
     {"q": "Which is specialist software?", "r": "software for managing patients in a hospital", "w": ["a word processor", "a spreadsheet", "a web browser"],
      "e": ["A word processor is general-purpose.", "A spreadsheet is general-purpose.", "A browser is general-purpose."], "y": "It is made for one particular job."},
     {"q": "Which is general-purpose software?", "r": "a spreadsheet", "w": ["a school timetabling program", "payroll software for one company", "airline booking software"],
      "e": ["That does one specific job.", "That does one specific job.", "That does one specific job."], "y": "Spreadsheets can be used for many tasks."},
     {"q": "A photographer wants to brighten and crop photos. Which kind of software?", "r": "photo-editing (graphics) software", "w": ["database software", "accounting software", "an e-mail program"],
      "e": ["Databases store records.", "Accounting software keeps accounts.", "E-mail sends messages."], "y": "Graphics software changes images."}], SRC),
   bank("s3-26-choose", 3, "{X.q}", [
     {"q": "A small business sells clothes in Bafoussam market. Which pair of software would help it most?", "r": "a spreadsheet for sales and stock, and a messaging app for customers", "w": ["a video game and a photo editor", "a flight simulator and a database of stars", "only an antivirus"],
      "e": ["Not useful for running the shop.", "Not relevant.", "Protection alone does not run the business."], "y": "Choose software that matches the tasks."},
     {"q": "Why should you keep antivirus software updated?", "r": "New viruses appear all the time and updates help detect them", "w": ["Updates make the screen brighter", "Old versions are faster", "Updates delete your files"],
      "e": ["Not related.", "Speed is not the reason.", "They should not delete your files."], "y": "Up-to-date definitions recognise new threats."},
     {"q": "Why might a school choose free open-source software like LibreOffice?", "r": "It does the same everyday tasks without licence fees", "w": ["It cannot open any files", "It needs no computer", "It is illegal"],
      "e": ["It opens common file types.", "It runs on a computer.", "It is legal and free."], "y": "Saves money on licences."}], SRC)],
  learn=learn(
    [("Images, sound and video",
      "• Graphics software: drawing (Paint), photo editing (GIMP, Photoshop) and design (Canva, Publisher) for posters, flyers and certificates.\n"
      "• Multimedia software: playing and editing music and video (VLC, Audacity, video editors) for school events, music and adverts."),
     ("Internet and communication",
      "• Web browsers (Chrome, Firefox, Edge) display websites; search engines find them.\n• E-mail sends letters and files.\n"
      "• Messaging apps (WhatsApp) and video-call software (Zoom, Google Meet) let people talk and share instantly.\n"
      "Use them responsibly: protect personal data and think before sharing."),
     ("Utilities and choosing software",
      "Utilities look after the computer: antivirus (removes malware), compression (zip files smaller), backup (copies of files), disk clean-up.\n"
      "General-purpose software can do many jobs (word processors, spreadsheets); specialist software does one job (hospital, banking or school-fees software).\n"
      "Choose software by the task, cost, ease of use and the files it must open. Free open-source programs such as LibreOffice and GIMP can save money.")],
    key_words=[("utility", "a program that maintains or protects the computer"), ("multimedia", "combining text, sound, images and video"),
               ("general-purpose software", "software for many kinds of task"), ("specialist software", "software for one particular job")],
    examples=["Poster: Canva", "Antivirus: utility", "Hospital records: specialist software"],
    mistake=("Antivirus is an application for writing letters", "Antivirus is a utility that protects against malware",
             "Utilities look after the computer; applications do users' tasks.")))

# ---------------------------------------------------------------- 28. Protection of intellectual property
SRC = ["software"]
L.lesson(D, S, 28, ("s3-28", "Protection of intellectual property"), [],
  "Intellectual property (IP) is a creation of the mind: inventions, books, music, films, software, designs, brand names.\n"
  "Protection:\n• Copyright protects creative works (books, music, software code) automatically; copying or sharing without permission is illegal.\n"
  "• Patents protect inventions for a number of years.\n• Trademarks protect brand names and logos.\n"
  "Breaking IP rights: software piracy (illegal copies), plagiarism (presenting others' work as yours), counterfeiting.\n"
  "In Cameroon, copyright is protected by law and organisations such as SOCAM (music); OAPI handles patents and trademarks for member states.\n"
  "Respect IP: buy or use licensed software, cite your sources, ask permission.",
  worked({},
         "Kum copies a paragraph from a website into his project without saying where it came from. What has he done, and what should he do?",
         ["Using someone else's words as if they were his own is plagiarism.", "He should put the words in quotation marks and give the source, or write the idea in his own words and cite the source."],
         "Plagiarism; he should quote and cite the source"),
  [card("c3s28-1", "Copyright protects creative works such as music and software.",
        ["Copying a film to sell is illegal."], "s3-28-type"),
   card("c3s28-2", "Patents protect inventions; trademarks protect brand names and logos.",
        ["A company logo is a trademark."], "s3-28-which"),
   card("c3s28-3", "Always cite your sources to avoid plagiarism.",
        ["Write where the information came from."], "s3-28-ethic")],
  [bank("s3-28-type", 1, "{X.q}", [
     {"q": "What is intellectual property?", "r": "A creation of the mind, such as an invention, song or program", "w": ["Land owned by a school", "A computer's hard disk", "Money in a bank"],
      "e": ["That is physical property.", "That is hardware.", "That is money."], "y": "Ideas and creative works can belong to their creators."},
     {"q": "Which protects a new song?", "r": "copyright", "w": ["a patent", "a trademark", "a warranty"],
      "e": ["Patents protect inventions.", "Trademarks protect brands.", "Warranties cover faulty products."], "y": "Creative works are protected by copyright."},
     {"q": "What is software piracy?", "r": "Copying or using software without a licence", "w": ["Buying software legally", "Writing your own program", "Updating your software"],
      "e": ["That respects copyright.", "That creates new IP.", "That is maintenance."], "y": "It is illegal and can spread malware."}], SRC),
   bank("s3-28-which", 1, "Which kind of protection fits? {X.q}", [
     {"q": "A new design of solar water pump", "r": "patent", "w": ["trademark", "copyright of a song", "nothing is needed"],
      "e": ["A trademark protects a brand.", "It is not a creative work like a song.", "Inventions can be protected."], "y": "Inventions are protected by patents."},
     {"q": "The name and logo of a drink company", "r": "trademark", "w": ["patent", "copyright", "warranty"],
      "e": ["It is not an invention.", "Brand names are trademarks.", "A warranty is a promise about quality."], "y": "Trademarks protect brand identity."},
     {"q": "The code of a mobile app", "r": "copyright", "w": ["trademark", "patent only", "nothing"],
      "e": ["The app's name may be a trademark, but the code is copyright.", "Code is usually protected by copyright.", "It is protected."], "y": "Software code is a creative work."}], SRC),
   bank("s3-28-ethic", 2, "{X.q}", [
     {"q": "Which action respects intellectual property?", "r": "Quoting a text and naming the author and source", "w": ["Copying a classmate's homework", "Downloading a film from an illegal site", "Selling copied CDs"],
      "e": ["That is plagiarism.", "That is piracy.", "That is piracy and counterfeiting."], "y": "Citing gives credit to the creator."},
     {"q": "What is plagiarism?", "r": "Presenting someone else's work as your own", "w": ["Writing a story yourself", "Asking a teacher for help", "Reading a library book"],
      "e": ["That is original work.", "Asking for help is fine.", "Reading is fine."], "y": "Always credit your sources."},
     {"q": "Why does IP protection matter?", "r": "It rewards creators so they keep inventing and creating", "w": ["It stops all sharing of ideas", "It makes software free for everyone", "It protects only rich people"],
      "e": ["Sharing with permission is allowed.", "Creators may charge for their work.", "It protects all creators."], "y": "Creators earn from their work."}], SRC),
   bank("s3-28-case", 3, "{X.q}", [
     {"q": "A street seller in Douala sells copied DVDs of Nollywood films. What is the problem?", "r": "It is piracy: the film makers lose money and it breaks copyright law", "w": ["Nothing, films are free", "It is legal if the price is low", "Only the buyer breaks the law"],
      "e": ["Films are protected by copyright.", "Price does not make it legal.", "Selling pirated copies is illegal."], "y": "Copyright protects the creators' income."},
     {"q": "A school wants to install software on 30 computers but bought one licence. What should it do?", "r": "Buy enough licences or use free open-source software", "w": ["Copy the one licence to all computers", "Install it and hide the computers", "Use a pirated version"],
      "e": ["That breaks the licence.", "Hiding does not make it legal.", "That is piracy."], "y": "Use software within its licence terms."},
     {"q": "Which organisation helps protect patents and trademarks for Cameroon and other member states?", "r": "OAPI (African Intellectual Property Organisation)", "w": ["FIFA", "the World Health Organisation", "MTN"],
      "e": ["FIFA governs football.", "WHO works on health.", "MTN is a telecom company."], "y": "OAPI is based in Yaoundé."}], SRC)],
  learn=learn(
    [("Ideas can be owned",
      "Intellectual property (IP) means creations of the mind: inventions, books, songs, films, photographs, software and brand names. Creators have rights over how their work is used.\n"
      "Protecting IP rewards people for their creativity and encourages them to keep creating."),
     ("Kinds of protection",
      "• Copyright: protects creative works (books, music, films, software code). It exists as soon as the work is made.\n"
      "• Patent: protects an invention, such as a new machine, for a number of years.\n• Trademark: protects brand names and logos.\n"
      "In Cameroon, copyright is protected by law; OAPI, based in Yaoundé, handles patents and trademarks for its member states."),
     ("Respecting IP",
      "• Software piracy (using unlicensed copies) and selling copied films or music are illegal and harm creators.\n"
      "• Plagiarism means presenting someone else's work as yours. Quote with quotation marks and give the source, or explain in your own words and cite where it came from.\n"
      "• Use licensed or free open-source software, and ask permission before using others' photos or music.")],
    key_words=[("intellectual property", "creations of the mind that belong to their creators"), ("copyright", "the right that protects creative works"),
               ("patent", "protection for an invention"), ("trademark", "protection for a brand name or logo"), ("piracy", "illegal copying or use of protected work")],
    examples=["Song: copyright", "New pump design: patent", "Company logo: trademark"],
    mistake=("Anything on the internet is free to copy", "Most online content is protected by copyright",
             "Being easy to copy does not make it free to copy.")))

# ---------------------------------------------------------------- 29. Digital rights management
L.lesson(D, S, 29, ("s3-29", "Digital rights management (DRM)"), [28],
  "Digital rights management (DRM) is technology that controls how digital content (music, films, e-books, software, games) can be used, to protect copyright.\n"
  "Examples:\n• Licence keys and product activation for software.\n• Streaming services that let you watch but not download, or only on registered devices.\n"
  "• E-books that cannot be copied or printed; encrypted DVDs; region codes.\n• Watermarks that identify the owner.\n"
  "Advantages: protects creators' income, reduces piracy. Disadvantages: can stop fair uses, may need internet to check licences, content may become unusable if the service closes.",
  worked({},
         "Bih buys a film on a streaming app. She can watch it on her phone but cannot copy it to her friend's laptop. Why?",
         ["The film is protected by DRM.", "The licence allows viewing only on her registered account or device.", "This stops unlicensed copies being shared."],
         "DRM limits copying to protect the film's copyright"),
  [card("c3s29-1", "DRM controls how digital content can be used.",
        ["Licence keys, encryption, watermarks"], "s3-29-def"),
   card("c3s29-2", "DRM protects creators but can limit users.",
        ["You may need the internet to activate software."], "s3-29-pro"),
   card("c3s29-3", "A licence key proves software was paid for.",
        ["A code typed in during installation"], "s3-29-ex")],
  [bank("s3-29-def", 1, "{X.q}", [
     {"q": "What is DRM?", "r": "Technology that controls how digital content can be used and copied", "w": ["A kind of computer virus", "A type of printer", "A way to make files bigger"],
      "e": ["It protects content; it is not malware.", "Not hardware.", "Not about size."], "y": "Digital rights management protects copyright."},
     {"q": "What is the main purpose of DRM?", "r": "to protect copyright and reduce piracy", "w": ["to speed up downloads", "to fix spelling", "to cool the computer"],
      "e": ["Not about speed.", "Not about spelling.", "Not hardware."], "y": "Creators control how their work is used."},
     {"q": "Which content commonly uses DRM?", "r": "films on streaming services", "w": ["a handwritten letter", "a chalkboard lesson", "a paper newspaper"],
      "e": ["Not digital.", "Not digital.", "Not digital."], "y": "DRM applies to digital content."}], SRC),
   bank("s3-29-ex", 1, "Which DRM method is this? {X.q}", [
     {"q": "A code must be typed in before a program can be used.", "r": "licence key / product activation", "w": ["watermark", "region code", "a strong password for your e-mail"],
      "e": ["A watermark marks content.", "Region codes limit where discs play.", "That protects an account, not a product licence."], "y": "The key proves the copy is licensed."},
     {"q": "A faint logo is printed across a photo.", "r": "watermark", "w": ["licence key", "encryption", "region code"],
      "e": ["Keys unlock software.", "Encryption scrambles data.", "Region codes restrict playback by region."], "y": "Watermarks show ownership."},
     {"q": "An e-book can be read in its app but cannot be copied or printed.", "r": "copy and print restrictions", "w": ["a patent", "a virus", "a backup"],
      "e": ["Patents protect inventions.", "Not malware.", "A backup is a copy, the opposite."], "y": "The app enforces the licence."}], SRC),
   bank("s3-29-pro", 2, "{X.q}", [
     {"q": "Which is an advantage of DRM for a musician?", "r": "It helps stop illegal copies, protecting income", "w": ["It makes all music free", "It improves the sound quality", "It removes the need for a licence"],
      "e": ["It controls, not frees, use.", "It does not change the sound.", "It enforces the licence."], "y": "Less piracy, more sales."},
     {"q": "Which is a disadvantage of DRM for users?", "r": "Content may stop working if the service closes or there is no internet to check the licence", "w": ["It makes films longer", "It adds viruses", "It always costs nothing"],
      "e": ["It does not change length.", "It is not malware.", "That is not a disadvantage."], "y": "Users depend on the provider."},
     {"q": "Why do some people say DRM is too strict?", "r": "It can stop legal uses, like moving a song you bought to a new device", "w": ["It allows unlimited copying", "It is never used", "It makes files smaller"],
      "e": ["It restricts copying.", "It is widely used.", "Not related."], "y": "Strict controls can affect honest buyers."}], SRC),
   bank("s3-29-case", 3, "{X.q}", [
     {"q": "A friend offers a 'cracked' version of a paid game that removes the licence check. What should you do?", "r": "Refuse: it breaks copyright and may contain malware", "w": ["Install it, it is free", "Share it with the class", "Sell copies"],
      "e": ["Free does not make it legal.", "That spreads piracy.", "That is illegal."], "y": "Cracked software is illegal and risky."},
     {"q": "Why do streaming apps limit the number of devices per account?", "r": "To stop one paid account being shared by many people", "w": ["To save battery", "To make videos clearer", "Because phones cannot play videos"],
      "e": ["Not the reason.", "Not related.", "Phones can play videos."], "y": "The licence is for the subscriber."},
     {"q": "Which is a fair balance between creators and users?", "r": "Paying for content while having reasonable rights to use what you bought", "w": ["All content always free", "Users have no rights at all", "Copying everything for friends"],
      "e": ["Creators need income.", "Buyers deserve fair use.", "That is piracy."], "y": "Both creators' and users' interests matter."}], SRC)],
  learn=learn(
    [("Protecting digital content",
      "Digital files can be copied perfectly in seconds. Digital rights management (DRM) is technology that controls how music, films, e-books, games and software may be used, so copyright holders are paid."),
     ("How DRM works",
      "• Licence keys and activation: a code proves you bought the software.\n• Streaming limits: watch or listen online, often without downloading, on a limited number of devices.\n"
      "• Copy and print restrictions on e-books; encryption on DVDs; region codes.\n• Watermarks: visible or hidden marks showing who owns or bought the content."),
     ("For and against",
      "For: it reduces piracy and protects the income of musicians, film makers and programmers.\n"
      "Against: it can stop honest uses (moving a song you bought to a new phone), may need the internet to check licences, and content can become unusable if the service closes.\n"
      "Avoid 'cracked' software that removes DRM: it is illegal and often carries malware.")],
    key_words=[("DRM", "digital rights management: technology controlling use of digital content"), ("licence key", "a code that activates paid software"),
               ("watermark", "a mark showing ownership"), ("encryption", "scrambling data so only authorised users can read it")],
    examples=["Streaming film: watch only", "Software activation key", "E-book: no copying"],
    mistake=("DRM makes content free to copy", "DRM controls and limits copying",
             "Its purpose is to protect copyright.")))

# ---------------------------------------------------------------- 30. Creative Commons licences
L.lesson(D, S, 30, ("s3-30", "Creative Commons licences"), [28],
  "Creative Commons (CC) licences let creators share their work while keeping some rights. Others may use it if they follow the conditions:\n"
  "• BY (Attribution): give credit to the creator. • SA (ShareAlike): share new works under the same licence.\n"
  "• NC (NonCommercial): no use to make money. • ND (NoDerivatives): no changes; share only as it is.\n"
  "Licences combine these, e.g. CC BY-SA, CC BY-NC-ND. CC0 means 'no rights reserved' (public domain).\n"
  "Many images on Wikipedia and many free educational resources use CC licences.",
  worked({},
         "A photo is licensed CC BY-NC. Can a school use it on a free poster? Can a shop use it in a paid advert?",
         ["BY: give credit to the photographer.", "NC: no commercial use.", "The free school poster is allowed with credit; the shop's paid advert is not allowed without permission."],
         "School poster: yes, with credit; shop advert: no"),
  [card("c3s30-1", "BY: always credit the creator.",
        ["'Photo: A. Tabe, CC BY'"], "s3-30-term"),
   card("c3s30-2", "NC: no commercial use; ND: no changes; SA: share alike.",
        ["CC BY-NC-ND is the strictest combination."], "s3-30-can"),
   card("c3s30-3", "{'CC0'} means the work is free for any use.",
        ["Public-domain images"], "s3-30-cc0")],
  [bank("s3-30-term", 1, "What does this Creative Commons term mean? {X.q}", [
     {"q": "BY", "r": "Attribution: give credit to the creator", "w": ["Buy before using", "No changes allowed", "No commercial use"],
      "e": ["CC licences do not require buying.", "That is ND.", "That is NC."], "y": "Every CC licence except {'CC0'} needs attribution."},
     {"q": "NC", "r": "NonCommercial: not for making money", "w": ["No credit needed", "New copies only", "No changes allowed"],
      "e": ["Credit is BY.", "Not a CC term.", "That is ND."], "y": "Use only for non-commercial purposes."},
     {"q": "ND", "r": "NoDerivatives: share only as it is, without changes", "w": ["No downloading", "No credit", "No sharing at all"],
      "e": ["Downloading is allowed.", "Credit is still needed (BY).", "Sharing is allowed."], "y": "You may not adapt or remix it."},
     {"q": "SA", "r": "ShareAlike: share new versions under the same licence", "w": ["Sell anywhere", "Secret access", "Same author only"],
      "e": ["Not a CC term.", "Not a CC term.", "Not a CC term."], "y": "Adaptations keep the same freedoms."}], SRC),
   bank("s3-30-can", 2, "Is this use allowed? {X.q}", [
     {"q": "Using a CC BY-ND photo, with credit, unchanged, in a school magazine", "r": "Yes", "w": ["No, CC works can never be used", "No, credit is not allowed", "Only if you change the photo"],
      "e": ["CC licences allow use under conditions.", "Credit is required (BY).", "ND forbids changes."], "y": "Credit given and no changes: allowed."},
     {"q": "Cropping and colouring a CC BY-ND drawing for a poster", "r": "No", "w": ["Yes, always", "Yes, if you do not give credit", "Yes, if the poster is pink"],
      "e": ["ND forbids changes.", "Credit is still required, and changes are still forbidden.", "Colour is irrelevant."], "y": "ND means no derivatives."},
     {"q": "Selling T-shirts printed with a CC BY-NC image", "r": "No (without the creator's permission)", "w": ["Yes, always", "Yes, if you give credit", "Yes, if sold cheaply"],
      "e": ["NC forbids commercial use.", "Credit does not remove the NC condition.", "Any sale is commercial."], "y": "Commercial use needs permission."}], SRC),
   bank("s3-30-cc0", 1, "{X.q}", [
     {"q": "What does {'CC0'} mean?", "r": "No rights reserved: anyone may use it for any purpose", "w": ["Copyright zero years", "Cannot copy at all", "Credit required on page 0"],
      "e": ["It means the creator gives up rights.", "The opposite.", "No such rule."], "y": "{'CC0'} places work in the public domain."},
     {"q": "Why do creators use Creative Commons licences?", "r": "To share their work while keeping some rights", "w": ["To stop anyone using it", "To make it illegal to share", "To earn money from every use automatically"],
      "e": ["All rights reserved would do that.", "CC encourages sharing.", "CC does not collect payments."], "y": "Easy, clear permission to reuse."},
     {"q": "Where are many CC-licensed images found?", "r": "Wikipedia and Wikimedia Commons", "w": ["Only in paid magazines", "Inside computer processors", "On bank cards"],
      "e": ["Paid magazines are usually all rights reserved.", "Not relevant.", "Not relevant."], "y": "Their licence is shown with each file."}], SRC),
   bank("s3-30-choose", 3, "Which licence should the creator choose? {X.q}", [
     {"q": "Ayuk wants anyone to use and change his photos, even for business, as long as he is credited.", "r": "CC BY", "w": ["CC BY-NC-ND", "all rights reserved", "CC BY-ND"],
      "e": ["That forbids business use and changes.", "That forbids reuse without permission.", "That forbids changes."], "y": "BY alone allows any use with credit."},
     {"q": "A teacher wants other teachers to adapt her worksheets for free, and share their versions the same way, but not sell them.", "r": "CC BY-NC-SA", "w": ["{'CC0'}", "CC BY-ND", "all rights reserved"],
      "e": ["{'CC0'} would allow selling.", "ND forbids adapting.", "That forbids reuse."], "y": "Credit, non-commercial, share alike."},
     {"q": "A photographer wants people to share his photos unchanged and never use them for business.", "r": "CC BY-NC-ND", "w": ["CC BY", "CC BY-SA", "{'CC0'}"],
      "e": ["That allows business use and changes.", "That allows changes and business use.", "That gives up all rights."], "y": "The strictest Creative Commons licence."}], SRC)],
  learn=learn(
    [("Sharing with conditions",
      "Normally, copyright means 'all rights reserved': you need permission to reuse a work. Creative Commons (CC) licences let creators say in advance 'you may use this, if…'.\n"
      "This makes it easy for teachers, students and artists to share and reuse legally."),
     ("The building blocks",
      "• BY (Attribution): give credit to the creator.\n• SA (ShareAlike): if you adapt it, share your version under the same licence.\n"
      "• NC (NonCommercial): do not use it to make money.\n• ND (NoDerivatives): share it only as it is; no changes.\n"
      "They combine: CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND (the strictest)."),
     ("Public domain and practice",
      "{'CC0'} means 'no rights reserved': the creator gives the work to the public domain for any use.\n"
      "When you use a CC work, write the title, creator, source and licence, e.g. 'Photo: Mount Cameroon by A. Tabe, CC BY-SA, Wikimedia Commons'.\n"
      "Check the conditions before changing a work or using it for business.")],
    key_words=[("Creative Commons", "licences that let creators share work with conditions"), ("attribution", "giving credit to the creator"),
               ("non-commercial", "not used to make money"), ("public domain", "free for anyone to use")],
    examples=["CC BY: any use with credit", "CC BY-NC: not for sale", "{'CC0'}: no rights reserved"],
    mistake=("A CC licence means you can do anything without credit", "Most CC licences require credit (BY) and may forbid changes or sale",
             "Always read the letters of the licence.")))

# ---------------------------------------------------------------- 32. Off-the-shelf and bespoke software
L.lesson(D, S, 32, ("s3-32", "Off-the-shelf and bespoke (custom) software"), [26],
  "• Off-the-shelf (packaged) software is ready-made for many users (word processors, accounting packages, antivirus). Advantages: cheaper, available at once, well tested, lots of help and training. Disadvantages: may have features you do not need or lack ones you do; you cannot change it.\n"
  "• Bespoke (custom-written) software is made for one organisation's exact needs (a hospital's patient system, a bank's mobile-money platform). Advantages: fits exactly, can be changed, can give a business advantage. Disadvantages: expensive, takes time to develop, may have more bugs at first, depends on the developers for support.\n"
  "Choose by cost, time, how special the needs are, and support.",
  worked({},
         "A small shop in Kumba needs to keep its accounts. Should it buy off-the-shelf software or pay for bespoke software? Explain.",
         ["Its needs are common to many shops.", "Off-the-shelf accounting software already does this, is cheaper and available at once.", "Bespoke software would cost much more and take time."],
         "Off-the-shelf: cheaper, ready now, and the needs are standard"),
  [card("c3s32-1", "Off-the-shelf software is ready-made for many users.",
        ["A word processor bought from a shop or online"], "s3-32-which"),
   card("c3s32-2", "Bespoke software is written for one organisation.",
        ["A bank's own mobile-money platform"], "s3-32-adv"),
   card("c3s32-3", "Choose by cost, time and how special the needs are.",
        ["Common needs: off-the-shelf. Unique needs: bespoke."], "s3-32-choose")],
  [bank("s3-32-which", 1, "Is this off-the-shelf or bespoke? {X.q}", [
     {"q": "A school buys LibreOffice for its computers.", "r": "off-the-shelf", "w": ["bespoke", "hardware", "a utility only"],
      "e": ["It was not written specially for the school.", "It is software.", "It is an office suite, not just a utility."], "y": "Ready-made for many users."},
     {"q": "A hospital pays programmers to build a system for its own patient records.", "r": "bespoke", "w": ["off-the-shelf", "open-source game", "an antivirus"],
      "e": ["It is made for one client.", "It is not a game.", "It is not a security utility."], "y": "Custom-written for one organisation."},
     {"q": "A family installs a popular antivirus program.", "r": "off-the-shelf", "w": ["bespoke", "firmware", "a database"],
      "e": ["Millions use the same program.", "Firmware is built into hardware.", "It is a utility."], "y": "Packaged for many users."}], SRC),
   bank("s3-32-adv", 1, "{X.q}", [
     {"q": "Which is an advantage of off-the-shelf software?", "r": "It is cheaper and available immediately", "w": ["It is made exactly for one user", "Only one company can use it", "It never needs updates"],
      "e": ["That is bespoke.", "Many can use it.", "It is updated often."], "y": "Costs are shared among many buyers."},
     {"q": "Which is an advantage of bespoke software?", "r": "It does exactly what the organisation needs", "w": ["It is always cheaper", "It is ready at once", "It has many unused features"],
      "e": ["It is usually more expensive.", "It takes time to develop.", "It is built to need."], "y": "Designed around the user's processes."},
     {"q": "Which is a disadvantage of bespoke software?", "r": "It is expensive and takes a long time to develop", "w": ["It cannot be changed", "It is used by millions", "It has lots of online tutorials"],
      "e": ["It can be changed by the developers.", "It is for one organisation.", "Help may be limited."], "y": "Paying developers for months costs a lot."}], SRC),
   bank("s3-32-choose", 2, "Which should they choose? {X.q}", [
     {"q": "A student needs software to type assignments.", "r": "off-the-shelf word processor", "w": ["bespoke software built for her", "a custom bank system", "no software at all"],
      "e": ["Far too costly for a common need.", "Not relevant.", "She needs a word processor."], "y": "Common needs are met by packaged software."},
     {"q": "A national electricity company needs to bill millions of customers with its own tariffs and meters.", "r": "bespoke software (or heavily customised)", "w": ["a simple word processor", "a free game", "a photo editor"],
      "e": ["Not suitable for billing millions.", "Not relevant.", "Not relevant."], "y": "Unique, large-scale needs justify custom software."},
     {"q": "A new business must start next week with standard needs and little money.", "r": "off-the-shelf software", "w": ["bespoke software", "wait two years for custom software", "write code by hand on paper"],
      "e": ["It takes too long and costs too much.", "The business cannot wait.", "Not practical."], "y": "Fast and cheap."}], SRC),
   bank("s3-32-compare", 3, "{X.q}", [
     {"q": "Why might off-the-shelf software be more reliable than new bespoke software?", "r": "Many users have already tested it and bugs have been fixed", "w": ["It is written by one person", "It is never updated", "It has no users"],
      "e": ["Big teams usually make it.", "It is updated often.", "It has many users."], "y": "Wide use finds and fixes bugs."},
     {"q": "A company using bespoke software finds its developer has closed down. What is the main risk?", "r": "No one may be able to fix or update the software", "w": ["The software becomes free", "The computer stops working", "Nothing changes"],
      "e": ["Price is not the issue.", "Hardware is not affected.", "Support is lost."], "y": "Bespoke software depends on its developers."},
     {"q": "What is customised off-the-shelf software?", "r": "Packaged software whose settings or add-ons are adjusted for one organisation", "w": ["Software written from nothing", "A computer virus", "Hardware only"],
      "e": ["That is fully bespoke.", "Not malware.", "It is software."], "y": "A middle way: cheaper than bespoke, closer to needs than plain packaged software."}], SRC)],
  learn=learn(
    [("Ready-made software",
      "Off-the-shelf (packaged) software is written once and sold or given to many users: word processors, spreadsheets, antivirus, accounting packages.\n"
      "Advantages: cheaper (the cost is shared), available at once, well tested, with plenty of manuals, videos and help.\n"
      "Disadvantages: it may not do exactly what you need, may have many features you never use, and you cannot change its code."),
     ("Made to measure",
      "Bespoke (custom-written) software is made for one organisation's exact needs: a hospital's patient system, a university's results system, a mobile-money platform.\n"
      "Advantages: it fits the way the organisation works, can be changed later, and can give an advantage over competitors.\n"
      "Disadvantages: expensive, slow to develop, may have bugs at first, and depends on the developers for support."),
     ("Choosing",
      "Ask: Are our needs common or special? How much money and time do we have? Who will support it?\n"
      "Common needs and small budgets → off-the-shelf. Unique, large-scale needs → bespoke, or customised off-the-shelf software as a middle way.")],
    key_words=[("off-the-shelf software", "ready-made software sold to many users"), ("bespoke software", "software written for one organisation"),
               ("customised software", "packaged software adjusted for one user's needs")],
    examples=["LibreOffice: off-the-shelf", "Hospital records system: bespoke", "Accounting package with add-ons: customised"],
    mistake=("Bespoke software is always the best choice", "It is best only when needs are special and the budget allows",
             "For common needs, off-the-shelf software is cheaper, faster and well tested.")))
