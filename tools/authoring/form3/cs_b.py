"""Form 3 Computer Science, Term 1, rows 15-22 (data capture, program development, algorithms, flowcharts).
Run: python tools/authoring/form3/cs_b.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"

# ---------------------------------------------------------------- 15. Data capture technologies 1 (devices)
SRC = ["data-capture"]
L.lesson(D, S, 15, ("s3-15", "Data capture technologies: automatic input devices"), [13],
  "Data capture means getting data into a computer system. Automatic (direct) methods are fast and reduce typing errors:\n"
  "• Barcode reader: reads product codes at supermarket tills. • QR code: square code read by phone cameras (payments, links).\n"
  "• OCR (optical character recognition): turns scanned printed text into editable text. • OMR (optical mark recognition): reads pencil marks on multiple-choice answer sheets and forms.\n"
  "• MICR (magnetic ink character recognition): reads the numbers printed in magnetic ink on cheques.\n"
  "• Magnetic stripe and chip cards (with PIN): bank and ID cards. • RFID: radio tags read without contact (tickets, livestock, toll cards).\n"
  "• Biometrics: fingerprints, face or iris to identify people. • Sensors: temperature, light, pressure for automatic monitoring.",
  worked({},
         "Which data capture method is best for marking {2000} multiple-choice answer sheets for a mock exam, and why?",
         ["The pupils shade boxes with a pencil.", "OMR reads the position of the marks automatically.", "It is fast and accurate for large numbers of sheets."],
         "OMR (optical mark recognition)"),
  [card("c3s15-1", "Barcodes and QR codes are read by scanners or cameras.",
        ["Supermarket tills scan barcodes."], "s3-15-match"),
   card("c3s15-2", "OMR reads marks; OCR reads printed characters.",
        ["Exam answer sheets: OMR. Scanned letters: OCR."], "s3-15-omr"),
   card("c3s15-3", "Automatic capture is faster and has fewer typing errors.",
        ["Scanning a barcode beats typing a {13}-digit number."], "s3-15-why")],
  [bank("s3-15-match", 1, "Which data capture method is used? {X.q}", [
     {"q": "A cashier scans the striped code on a tin of milk.", "r": "barcode reader", "w": ["OMR", "MICR", "biometrics"],
      "e": ["OMR reads pencil marks.", "MICR reads magnetic ink on cheques.", "Biometrics identify people."], "y": "Barcodes identify products."},
     {"q": "A bank reads the special numbers at the bottom of a cheque.", "r": "MICR", "w": ["OCR", "RFID", "QR code"],
      "e": ["OCR reads ordinary print.", "RFID uses radio tags.", "QR codes are square patterns."], "y": "Magnetic ink is hard to forge."},
     {"q": "A phone camera reads a square pattern to pay for goods.", "r": "QR code", "w": ["barcode", "OMR", "magnetic stripe"],
      "e": ["Barcodes are lines.", "OMR reads marks on forms.", "A stripe is swiped."], "y": "QR codes are two-dimensional and read by cameras."},
     {"q": "A worker's attendance is recorded by placing a finger on a scanner.", "r": "biometrics", "w": ["RFID", "OCR", "barcode reader"],
      "e": ["RFID uses a tag.", "OCR reads text.", "A barcode is printed."], "y": "Fingerprints are unique to each person."}], SRC),
   bank("s3-15-omr", 1, "{X.q}", [
     {"q": "What is the difference between OMR and OCR?", "r": "OMR reads the position of marks; OCR reads printed letters and numbers", "w": ["They are exactly the same", "OMR reads magnetic ink; OCR reads barcodes", "OCR reads pencil marks only"],
      "e": ["They do different jobs.", "Magnetic ink is MICR; barcodes have their own readers.", "OCR reads characters, not just marks."], "y": "Marks vs characters."},
     {"q": "Which method turns a scanned printed page into text you can edit?", "r": "OCR", "w": ["OMR", "MICR", "RFID"],
      "e": ["OMR reads marks.", "MICR reads magnetic ink.", "RFID reads radio tags."], "y": "Optical character recognition."},
     {"q": "Which method reads a tag on a cow's ear without touching it?", "r": "RFID", "w": ["OMR", "barcode reader", "MICR"],
      "e": ["OMR needs a paper form.", "Barcodes need line of sight and can get dirty.", "MICR is for cheques."], "y": "Radio waves read the tag from a distance."}], SRC),
   bank("s3-15-why", 2, "{X.q}", [
     {"q": "Why is scanning barcodes better than typing product codes at a till?", "r": "It is faster and reduces typing errors", "w": ["It is slower but prettier", "It needs no computer", "It works without electricity"],
      "e": ["It is faster.", "A computer looks up the price.", "Scanners need power."], "y": "Automatic capture is quick and accurate."},
     {"q": "Which is a disadvantage of biometric attendance systems?", "r": "They store personal data that must be protected and can fail with dirty or injured fingers", "w": ["They are always slower than paper", "They never need power", "They cannot identify anyone"],
      "e": ["They are usually faster.", "They need power.", "They identify people well."], "y": "Privacy and reliability must be considered."},
     {"q": "Why do banks use chip-and-PIN cards instead of only magnetic stripes?", "r": "The chip is harder to copy, and the PIN proves the user", "w": ["Chips are cheaper than paper", "Stripes hold more money", "PINs make cards heavier"],
      "e": ["Cost is not the reason.", "Cards do not hold money physically.", "Weight is irrelevant."], "y": "Better security against fraud."}], SRC),
   bank("s3-15-best", 3, "Which method is best? {X.q}", [
     {"q": "Recording the temperature of a vaccine fridge every 10 minutes, day and night", "r": "a temperature sensor with data logging", "w": ["a person writing it down", "OMR forms", "a barcode reader"],
      "e": ["A person cannot do it all night reliably.", "OMR is for marked forms.", "Barcodes identify products."], "y": "Sensors record automatically and continuously."},
     {"q": "Charging motorists at a toll gate without stopping", "r": "RFID tags on the vehicles", "w": ["MICR", "OCR of handwritten notes", "OMR sheets"],
      "e": ["MICR is for cheques.", "Handwriting is slow and unreliable.", "OMR needs forms."], "y": "RFID is read at a distance."},
     {"q": "Turning an old printed school register into a computer document", "r": "scanning with OCR", "w": ["RFID", "biometrics", "MICR"],
      "e": ["RFID reads tags.", "Biometrics identify people.", "MICR reads magnetic ink."], "y": "OCR converts printed text."}], SRC)],
  learn=learn(
    [("Getting data in automatically",
      "Typing data by hand is slow and causes mistakes. Data capture technologies read data straight into the computer.\n"
      "• Barcode readers scan the striped codes on products at supermarket tills.\n• QR codes are square patterns read by phone cameras, used for mobile payments and links.\n"
      "• Magnetic stripe and chip cards (with a PIN) are used by banks and for ID."),
     ("Reading paper",
      "• OMR (optical mark recognition) detects where pencil marks are on a form: multiple-choice answer sheets, lottery tickets, surveys.\n"
      "• OCR (optical character recognition) turns scanned printed text into text you can edit.\n"
      "• MICR (magnetic ink character recognition) reads the special numbers on cheques, printed in magnetic ink that is hard to forge."),
     ("Radio, bodies and sensors",
      "• RFID (radio frequency identification) reads tags without contact: transport cards, library books, livestock ear tags, toll gates.\n"
      "• Biometrics identify people by fingerprint, face or iris: phone unlocking, staff attendance, ID cards.\n"
      "• Sensors measure temperature, light, pressure or movement automatically.\n"
      "Choose the method that is fastest and most accurate for the job, and protect any personal data collected.")],
    key_words=[("data capture", "getting data into a computer system"), ("OMR", "optical mark recognition"), ("OCR", "optical character recognition"),
               ("MICR", "magnetic ink character recognition"), ("RFID", "radio frequency identification"), ("biometrics", "identifying people by body features")],
    examples=["Till: barcode", "Exam sheets: OMR", "Cheques: MICR", "Toll gate: RFID"],
    mistake=("OCR reads the pencil marks on multiple-choice answer sheets", "OMR reads the marks; OCR reads printed characters",
             "Marks → OMR; characters → OCR.")))

# ---------------------------------------------------------------- 16. Data capture technologies 2 (forms, logging, checks)
SRC = ["data-capture"]
L.lesson(D, S, 16, ("s3-16", "Data capture: forms, data logging, validation and verification"), [15],
  "Manual (indirect) data capture: data is collected first (paper forms, questionnaires, interviews), then typed in. A good form has clear questions, boxes for each character, tick boxes where possible and instructions.\n"
  "Data logging: sensors take readings automatically at regular intervals and store them (weather stations, river levels, hospital monitors).\n"
  "Validation: the computer checks that data is sensible and allowed (range check, type check, length check, presence check, format check). It cannot prove data is correct.\n"
  "Verification: checks that data was copied correctly (double entry, or visual check against the original).",
  worked({"n": 144, "h": 24},
         "A weather station in Garoua logs the temperature every {60 * h / n} minutes. How many readings does it store in {h} hours?",
         ["Readings per hour = {60} ÷ {60 * h / n} = {n / h}.", "In {h} hours: {n / h} × {h} = {n} readings."], "{n} readings", checks=["60 * h / n == 10"]),
  [card("c3s16-1", "Validation checks data is sensible; verification checks it was copied correctly.",
        ["Age {250}: rejected by a range check."], "s3-16-vv"),
   card("c3s16-2", "Range, type, length, presence and format checks.",
        ["A phone number must have {9} digits: length check."], "s3-16-check"),
   card("c3s16-3", "Data logging: sensors record readings at set intervals.",
        ["River level logged every hour"], "s3-16-log")],
  [bank("s3-16-vv", 1, "{X.q}", [
     {"q": "What is validation?", "r": "An automatic check that data is sensible and allowed", "w": ["Proof that data is correct", "Copying data twice", "Printing the data"],
      "e": ["Sensible data can still be wrong.", "That is double-entry verification.", "Printing is output."], "y": "Validation rejects impossible data."},
     {"q": "What is verification?", "r": "Checking that data has been copied or entered correctly", "w": ["Checking that data is within a range", "Deleting old data", "Encrypting data"],
      "e": ["That is a validation range check.", "Not related.", "That is security."], "y": "Double entry or comparing with the original."},
     {"q": "A pupil's age is entered as 14 instead of 15. Validation accepts it. Why?", "r": "14 is a sensible age, so validation cannot tell it is wrong", "w": ["Validation is broken", "Ages are never checked", "14 is not a number"],
      "e": ["It worked as designed.", "A range check was applied.", "It is a number."], "y": "Validation checks sense, not truth: verification catches copying errors."}], SRC),
   bank("s3-16-check", 1, "Which validation check is this? {X.q}", [
     {"q": "A mark must be between 0 and 20.", "r": "range check", "w": ["length check", "type check", "presence check"],
      "e": ["Length counts characters.", "Type checks numbers vs text.", "Presence checks a field is not empty."], "y": "Limits on the value: range check."},
     {"q": "The 'surname' box cannot be left empty.", "r": "presence check", "w": ["range check", "format check", "type check"],
      "e": ["No limits on value.", "No pattern is required.", "Not about number vs text."], "y": "Something must be entered."},
     {"q": "A phone number must contain exactly 9 digits.", "r": "length check", "w": ["range check", "presence check", "spell check"],
      "e": ["It is the number of characters that matters.", "It is more than just not empty.", "Not about spelling."], "y": "Counting characters: length check."},
     {"q": "A date must be written DD/MM/YYYY.", "r": "format check", "w": ["length check", "presence check", "range check"],
      "e": ["The pattern matters, not just the length.", "More than presence.", "Not just limits."], "y": "A required pattern: format check."}], SRC),
   num("s3-16-log", 2, "A data logger records the level of the river Benue every {m} minutes. How many readings are stored in {d} days?", "d * 24 * 60 / m",
       ["Readings per hour = {60} ÷ {m} = {60 / m}.", "Hours in {d} days = {d * 24}.", "Readings = {60 / m} × {d * 24} = {answer}."],
       vars={"m": {"pick": [5, 10, 15, 20, 30, 60]}, "d": {"int": [1, 7]}},
       misc=[("hours", "d * 24", "That is the number of hours. Multiply by readings per hour.")],
       sources=SRC, where=["d * 24 * 60 / m != d * 24"]),
   bank("s3-16-form", 3, "{X.q}", [
     {"q": "Which is a feature of a well-designed data capture form?", "r": "Separate boxes for each character and tick boxes for choices", "w": ["One large box for all the answers", "Questions with no instructions", "Very small writing to save paper"],
      "e": ["One box makes data hard to read and enter.", "Instructions reduce mistakes.", "Small writing causes errors."], "y": "Clear, structured forms reduce errors."},
     {"q": "Why might a researcher use a questionnaire instead of sensors?", "r": "To collect people's opinions, which sensors cannot measure", "w": ["Questionnaires are always faster", "Sensors cannot measure temperature", "Questionnaires need no reading"],
      "e": ["They are often slower.", "Sensors measure temperature well.", "People must read them."], "y": "Opinions and personal information need questions."},
     {"q": "Why is data logging better than a person taking readings for a week?", "r": "It works continuously and accurately without breaks", "w": ["It is always cheaper than everything", "It never needs power", "It makes the weather better"],
      "e": ["Equipment has costs.", "Loggers need batteries or power.", "It only records."], "y": "No missed readings, no tired observer."}], SRC)],
  learn=learn(
    [("Collecting data by hand",
      "Some data must be collected from people: opinions, personal details, survey answers. This is done with forms, questionnaires and interviews, and the data is typed in later (indirect capture).\n"
      "A good form has clear questions and instructions, a box for each character, tick boxes for choices, and enough space. Good forms mean fewer errors when the data is entered."),
     ("Data logging",
      "Data logging uses sensors connected to a logger or computer to take readings automatically at fixed intervals, for example every {10} minutes.\n"
      "Uses: weather stations, river and flood levels, temperature of vaccine fridges, patients' heart rates.\n"
      "Readings per hour = {60} ÷ interval in minutes. Every {10} minutes gives {6} an hour and {144} a day."),
     ("Checking data",
      "• Validation is done by the computer: is the data sensible? Range check (mark {0}–{20}), type check (a number, not text), length check (exactly {9} digits), presence check (not empty), format check (DD/MM/YYYY).\n"
      "• Verification checks that data was copied correctly: typing it twice (double entry) or comparing with the original document.\n"
      "Validation can accept data that is sensible but wrong; verification helps catch those mistakes.")],
    key_words=[("validation", "automatic check that data is sensible"), ("verification", "check that data was entered correctly"),
               ("data logging", "automatic recording of sensor readings over time"), ("questionnaire", "a set of questions to collect information from people")],
    examples=["Mark {25} out of {20}: range check fails", "Typing a password twice: verification", "Logger every {30} minutes: {48} readings a day"],
    mistake=("Validation proves the data is correct", "Validation only checks the data is sensible",
             "A wrong but sensible value passes validation.")))

# ---------------------------------------------------------------- 18. Program development life cycle
SRC = ["algorithms"]
L.lesson(D, S, 18, ("s3-18", "The program development life cycle"), [],
  "Programs are developed in stages:\n"
  "• Analysis: understand the problem and the requirements (inputs, processes, outputs).\n• Design: plan the solution with algorithms, flowcharts or pseudocode, and the user interface.\n"
  "• Coding: write the program in a programming language.\n• Testing: run it with normal, boundary and erroneous data to find and fix errors (debugging).\n"
  "• Implementation/deployment: install it for users and train them.\n• Maintenance: fix new errors, update and improve it over time.\n"
  "Documentation is written throughout (user guide, technical notes).",
  worked({},
         "A school wants a program to calculate pupils' averages. In which stage do the programmers find out which subjects and marks it must handle?",
         ["Finding out what the program must do comes first, before any planning or coding.", "That is analysis: identifying inputs (marks), processes (averaging) and outputs (reports)."],
         "Analysis"),
  [card("c3s18-1", "Analysis → design → coding → testing → implementation → maintenance.",
        ["Then the cycle may start again."], "s3-18-order"),
   card("c3s18-2", "Design plans the solution before coding.",
        ["Algorithms, flowcharts, pseudocode"], "s3-18-stage"),
   card("c3s18-3", "Testing uses normal, boundary and erroneous data.",
        ["For marks {0}–{20}: test {12}, {20} and {-5}."], "s3-18-test")],
  [order("s3-18-order", 1, "Put the stages of the program development life cycle in order.",
         ["Analysis", "Design", "Coding", "Testing", "Implementation", "Maintenance"], hint="Understand, plan, write, check, install, look after.", sources=SRC, review="authored"),
   bank("s3-18-stage", 1, "Which stage is this? {X.q}", [
     {"q": "Programmers draw a flowchart of the solution.", "r": "design", "w": ["analysis", "coding", "maintenance"],
      "e": ["Analysis finds the requirements.", "Coding writes the program.", "Maintenance comes after release."], "y": "Planning the solution is design."},
     {"q": "The program is updated a year later to add a new feature.", "r": "maintenance", "w": ["testing", "analysis", "coding"],
      "e": ["Testing is before release.", "Analysis is at the start.", "Coding is the first writing of the program."], "y": "Changes after release are maintenance."},
     {"q": "The team writes instructions in Python.", "r": "coding", "w": ["design", "implementation", "analysis"],
      "e": ["Design plans; it does not write the language.", "Implementation installs the finished program.", "Analysis studies the problem."], "y": "Writing program code is coding."}], SRC),
   bank("s3-18-test", 2, "{X.q}", [
     {"q": "A program accepts marks from 0 to 20. Which is boundary test data?", "r": "20", "w": ["12", "-5", "abc"],
      "e": ["12 is normal data.", "-5 is erroneous (out of range).", "abc is erroneous (wrong type)."], "y": "Boundary data is at the edge of the allowed range."},
     {"q": "Which is erroneous test data for the same program?", "r": "25", "w": ["0", "10", "20"],
      "e": ["0 is a boundary value.", "10 is normal.", "20 is a boundary value."], "y": "Erroneous data should be rejected."},
     {"q": "Why do programmers test with erroneous data?", "r": "To check the program rejects bad data correctly", "w": ["To make it crash on purpose for fun", "Because normal data is never used", "To slow the program down"],
      "e": ["It is to check robustness.", "Normal data is also tested.", "Speed is not the aim."], "y": "Good programs handle mistakes safely."}], SRC),
   bank("s3-18-why", 3, "{X.q}", [
     {"q": "Why is analysis done before coding?", "r": "To understand exactly what the program must do, so effort is not wasted", "w": ["Because coding is easy", "Analysis is optional", "To choose the colour of the screen only"],
      "e": ["Coding without understanding leads to the wrong program.", "Skipping it causes problems.", "It covers much more."], "y": "A clear problem statement guides everything after."},
     {"q": "Why is maintenance part of the cycle?", "r": "Users find errors and needs change after the program is released", "w": ["Programs never change", "It replaces testing", "It is the first stage"],
      "e": ["They often need updates.", "Testing still happens before release.", "It is the last stage."], "y": "Software is updated throughout its life."},
     {"q": "What is debugging?", "r": "Finding and fixing errors in a program", "w": ["Removing insects from the computer", "Writing the user guide", "Installing the program"],
      "e": ["The name comes from that story, but it means fixing errors.", "That is documentation.", "That is implementation."], "y": "Debugging happens mainly during testing."}], SRC)],
  learn=learn(
    [("From problem to program",
      "Good programs are not written in one go. Developers follow a cycle of stages.\n"
      "• Analysis: understand the problem and what the users need. What are the inputs, processes and outputs?\n"
      "• Design: plan the solution as an algorithm, a flowchart or pseudocode, and design the screens."),
     ("Building and checking",
      "• Coding: write the program in a programming language such as Python.\n"
      "• Testing: run it with test data and fix errors (debugging). Use normal data (typical values), boundary data (at the edges, e.g. {0} and {20} for marks out of {20}) and erroneous data (values that should be rejected, e.g. {25} or 'abc')."),
     ("After release",
      "• Implementation: install the program, move existing data into it and train the users.\n• Maintenance: fix errors found later, adapt to new needs and improve it.\n"
      "Documentation (a user guide and technical notes) is written along the way. When big changes are needed, the cycle starts again with analysis.")],
    key_words=[("analysis", "understanding the problem and requirements"), ("design", "planning the solution"), ("testing", "checking the program with test data"),
               ("maintenance", "keeping the program working and up to date"), ("boundary data", "values at the edge of the allowed range")],
    examples=["Flowchart drawing: design", "Typing code: coding", "Fixing a bug reported by users: maintenance"],
    mistake=("Start by writing code straight away", "Start with analysis and design",
             "Without a clear plan, the program may solve the wrong problem.")))

# ---------------------------------------------------------------- 19. Decomposition and representing solutions
L.lesson(D, S, 19, ("s3-19", "Decomposition and ways of representing solutions"), [18],
  "Decomposition: breaking a big problem into smaller sub-problems that are easier to solve, then combining their solutions.\n"
  "Example: 'organise a school sports day' → plan events, prepare the field, register athletes, record results, award prizes.\n"
  "Solutions can be represented as:\n• structure diagrams (showing the sub-problems);\n• algorithms in plain steps;\n• pseudocode (structured English-like statements);\n• flowcharts (diagrams with standard symbols).\n"
  "Each part should have clear inputs, processing and outputs (IPO).",
  worked({},
         "Decompose the problem 'calculate and print a pupil's report card'.",
         ["Input: read the pupil's name and marks.", "Process: work out the total, average and grade for each subject.", "Output: print the report card."],
         "Input marks → process (total, average, grade) → output report"),
  [card("c3s19-1", "Decomposition breaks a big problem into smaller parts.",
        ["Cooking a meal: buy food, prepare, cook, serve."], "s3-19-decomp"),
   card("c3s19-2", "Every part has inputs, processing and outputs.",
        ["Input: marks; process: average; output: report"], "s3-19-ipo"),
   card("c3s19-3", "Solutions can be shown as pseudocode or flowcharts.",
        ["Both describe the same algorithm."], "s3-19-rep")],
  [bank("s3-19-decomp", 1, "{X.q}", [
     {"q": "What is decomposition?", "r": "Breaking a problem into smaller, easier sub-problems", "w": ["Letting a problem rot", "Writing a program in one long line", "Deleting parts of a program"],
      "e": ["Not in computing.", "That is the opposite.", "It is about planning, not deleting."], "y": "Small parts are easier to understand, solve and test."},
     {"q": "Which is a good sub-problem of 'run a school shop'?", "r": "Record the daily sales", "w": ["Do everything", "Buy a computer game", "Go on holiday"],
      "e": ["That is the whole problem.", "Not part of running the shop.", "Not part of the problem."], "y": "A sub-problem is one clear part of the whole."},
     {"q": "Why does decomposition help teams of programmers?", "r": "Different people can work on different parts at the same time", "w": ["It means no one needs to test", "It makes programs longer for no reason", "It removes the need for design"],
      "e": ["Each part must still be tested.", "Clarity, not length, is the aim.", "It is part of design."], "y": "Smaller tasks can be shared out."}], SRC),
   bank("s3-19-ipo", 1, "In 'calculate the area of a rectangle and display it', which is the {X.q}?", [
     {"q": "input", "r": "the length and the width", "w": ["length × width", "showing the area on the screen", "the rectangle's colour"],
      "e": ["That is the process.", "That is the output.", "Colour is not needed."], "y": "Inputs are the data the program needs."},
     {"q": "process", "r": "multiplying length by width", "w": ["typing the length", "displaying the answer", "turning on the computer"],
      "e": ["That is input.", "That is output.", "Not part of the algorithm."], "y": "Processing changes inputs into results."},
     {"q": "output", "r": "displaying the area", "w": ["entering the width", "multiplying the numbers", "saving the keyboard"],
      "e": ["That is input.", "That is processing.", "Not meaningful."], "y": "Outputs are the results shown or stored."}], SRC),
   bank("s3-19-rep", 2, "{X.q}", [
     {"q": "What is pseudocode?", "r": "A structured, English-like way of writing an algorithm", "w": ["A real programming language that runs", "A drawing with shapes", "A secret code"],
      "e": ["It does not run on a computer.", "That is a flowchart.", "It is meant to be easy to read."], "y": "It lets you plan without worrying about a language's rules."},
     {"q": "What does a structure diagram show?", "r": "How a problem is broken into sub-problems", "w": ["The colours of a program's screens", "The wiring inside a computer", "A list of test results"],
      "e": ["That is screen design.", "That is hardware.", "That is a test log."], "y": "A top-down view of the decomposition."},
     {"q": "Which way of representing a solution uses standard symbols joined by arrows?", "r": "a flowchart", "w": ["pseudocode", "a paragraph", "a spreadsheet"],
      "e": ["Pseudocode uses text.", "A paragraph is plain prose.", "A spreadsheet is application software."], "y": "Ovals, rectangles, diamonds and parallelograms."}], SRC),
   order("s3-19-avg", 3, "Put the steps of an algorithm to find the average of three marks in order.",
         ["Start", "Input the three marks", "Add the marks to get the total", "Divide the total by three", "Output the average", "Stop"],
         hint="Input, process, output, between start and stop.", sources=SRC, review="authored")],
  learn=learn(
    [("Breaking problems down",
      "Big problems are hard to solve in one go. Decomposition means splitting a problem into smaller sub-problems, solving each, and putting the solutions together.\n"
      "'Organise the school sports day' becomes: plan the events, prepare the field, register athletes, record results, award prizes. Each part can be given to a different team."),
     ("Input, process, output",
      "For each part, ask:\n• Input: what data does it need?\n• Process: what must be done with the data?\n• Output: what result must be shown or stored?\n"
      "For a report card: input the marks, process them (total, average, grade), output the printed report."),
     ("Showing the solution",
      "• A structure diagram shows the problem at the top and its sub-problems below.\n• An algorithm can be written as numbered steps.\n"
      "• Pseudocode uses structured English-like statements such as INPUT, OUTPUT, IF … THEN … ELSE, FOR … NEXT.\n• A flowchart shows the same steps with standard shapes and arrows.\n"
      "All of them describe the steps before any real code is written.")],
    key_words=[("decomposition", "breaking a problem into smaller parts"), ("sub-problem", "one smaller part of a big problem"),
               ("pseudocode", "structured English-like description of an algorithm"), ("IPO", "input, process, output")],
    examples=["Report card: input marks, average, print", "Sports day: five sub-problems", "Pseudocode: INPUT mark"],
    mistake=("Decomposition makes the problem bigger", "Decomposition makes each part smaller and easier",
             "The whole problem is the same; it is just tackled piece by piece.")))

# ---------------------------------------------------------------- 20. Notions of algorithms
L.lesson(D, S, 20, ("s3-20", "Algorithms: meaning and properties"), [19],
  "An algorithm is a finite, ordered set of clear steps that solves a problem.\n"
  "Properties of a good algorithm:\n• Finite: it ends after a number of steps.\n• Definite (unambiguous): each step has one clear meaning.\n• Ordered: steps are in the right sequence.\n"
  "• Has inputs and outputs.\n• Effective: each step can actually be done.\n"
  "Everyday examples: a recipe, directions to a friend's house, the steps to make a mobile-money transfer.\n"
  "Tracing an algorithm means following it step by step with values to check what it does.",
  worked({"a": 7, "b": 4},
         "Trace: SET x TO {a}; SET y TO {b}; SET x TO x + y; SET y TO x − y; OUTPUT x, y.",
         ["x = {a}, y = {b}.", "x = {a} + {b} = {a + b}.", "y = {a + b} − {b} = {a}."], "x = {a + b}, y = {a}", checks=["a + b == 11"]),
  [card("c3s20-1", "An algorithm is a finite, ordered list of clear steps.",
        ["A recipe for puff-puff is an algorithm."], "s3-20-def"),
   card("c3s20-2", "Each step must be clear (unambiguous) and possible.",
        ["'Add some salt' is vague; 'add {5} g of salt' is clear."], "s3-20-prop"),
   card("c3s20-3", "Trace an algorithm by following it with values.",
        ["Keep a table of each variable's value."], "s3-20-trace")],
  [bank("s3-20-def", 1, "{X.q}", [
     {"q": "What is an algorithm?", "r": "A finite, ordered set of clear steps to solve a problem", "w": ["A type of computer", "A programming language", "A random list of ideas"],
      "e": ["Hardware is not an algorithm.", "Languages are used to code algorithms.", "The steps must be ordered and clear."], "y": "Algorithms can be followed by people or computers."},
     {"q": "Which is an example of an algorithm in daily life?", "r": "the steps to send money with mobile money", "w": ["a photograph", "a song's tune", "a football"],
      "e": ["A photo is not a set of steps.", "A tune is not instructions.", "An object is not a process."], "y": "Ordered steps that achieve a goal."},
     {"q": "Why must an algorithm be finite?", "r": "It must end after a number of steps and give a result", "w": ["It must run forever", "It must have exactly ten steps", "It must use a computer"],
      "e": ["Then there would be no result.", "Any number of steps is allowed, but it must end.", "People can follow algorithms too."], "y": "An endless process never produces an answer."}], SRC),
   bank("s3-20-prop", 1, "{X.q}", [
     {"q": "Which step is too ambiguous for an algorithm?", "r": "Cook the rice for a while.", "w": ["Cook the rice for 20 minutes.", "Add 2 cups of water.", "Turn off the gas."],
      "e": ["20 minutes is clear.", "2 cups is clear.", "That is clear."], "y": "'A while' has no definite meaning."},
     {"q": "Why does the order of steps matter?", "r": "Doing steps in the wrong order can give a wrong result", "w": ["It never matters", "Computers sort the steps themselves", "Only the first step matters"],
      "e": ["It does: you cannot drain rice before cooking it.", "Computers follow the given order.", "Every step matters."], "y": "Sequence is a key property."},
     {"q": "An algorithm has no output. What is wrong?", "r": "It gives no result, so it does not solve the problem", "w": ["Nothing: outputs are optional", "It is too short", "It has too many inputs"],
      "e": ["A useful algorithm produces a result.", "Length is not the problem.", "Inputs are not the issue."], "y": "Algorithms must produce an output."}], SRC),
   num("s3-20-trace", 2, "Trace: SET total TO {s}; REPEAT {n} TIMES: total ← total + {d}; OUTPUT total. What is output?", "traceAdd(s, d, n)",
       ["Start: total = {s}.", "Each of the {n} repeats adds {d}: {n} × {d} = {n * d}.", "Output: {s} + {n * d} = {answer}."],
       vars={"s": {"int": [0, 20]}, "d": {"int": [2, 9]}, "n": {"int": [2, 8]}},
       misc=[("once", "s + d", "The addition happens {n} times, not once."), ("nostart", "n * d", "Remember the starting value {s}.")],
       sources=SRC, where=["s != 0"]),
   num("s3-20-swap", 3, "Trace: SET x TO {a}; SET y TO {b}; SET x TO x + y; SET y TO x − y; SET x TO x − y; OUTPUT x. What is output?", "b",
       ["x = {a}, y = {b}.", "x = {a} + {b} = {a + b}; y = {a + b} − {b} = {a}.", "x = {a + b} − {a} = {b}. Output: {answer}."],
       vars={"a": {"int": [2, 30]}, "b": {"int": [2, 30]}},
       misc=[("first", "a", "Follow each step: the values have been swapped."), ("sum", "a + b", "That is x after the third line; there are more steps.")],
       sources=SRC, where=["a != b"])],
  learn=learn(
    [("What an algorithm is",
      "An algorithm is a finite, ordered set of clear steps that solves a problem. Computers run algorithms written as programs, but people use algorithms every day too: a recipe for puff-puff, directions to a friend's house, the steps for a mobile-money transfer."),
     ("A good algorithm is…",
      "• Finite: it stops after a number of steps.\n• Definite: every step is clear. 'Add some salt' is vague; 'add {5} g of salt' is definite.\n"
      "• Ordered: the steps come in the correct sequence.\n• It takes inputs and produces outputs.\n• Effective: each step can actually be carried out."),
     ("Tracing",
      "To check an algorithm, trace it: follow it step by step with real values and record each variable in a table.\n"
      "SET total TO {10}; REPEAT {3} TIMES: total ← total + {5}; OUTPUT total. Trace: {10} → {15} → {20} → {25}. Output {25}.\n"
      "Tracing finds mistakes before the algorithm is coded.")],
    key_words=[("algorithm", "a finite, ordered set of clear steps to solve a problem"), ("trace", "follow an algorithm step by step with values"),
               ("variable", "a named store whose value can change"), ("ambiguous", "having more than one possible meaning")],
    examples=["Recipe: an everyday algorithm", "Trace: {10} → {15} → {20} → {25}", "Swap two variables using a sum"],
    mistake=("'Fry until ready' is a precise step", "Say exactly when: 'fry for {5} minutes or until golden brown'",
             "Each step must have one clear meaning.")))
