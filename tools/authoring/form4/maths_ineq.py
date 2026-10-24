"""Form 4 Maths, Term 1, rows 16-19: intervals and inequalities. Row 17 (absolute values) and row 18 (its continuation
"of the form", a parser split on the sheet) are taught as absolute-value equations (17) and absolute-value
inequalities (18). Run: python tools/authoring/form4/maths_ineq.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import goal

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRC = ["inequalities"]

# ---------------------------------------------------------------- 16. Interval notation; linear inequalities
L.lesson(D, S, 16, ("m4-16", "Use interval notation and solve linear inequalities in one unknown"), [],
  "Interval notation writes a set of numbers by its ends.\n"
  "• Square bracket: the end is included (≤ or ≥). Round bracket: the end is left out (< or >).\n"
  "• −2 ≤ x < 5 is [−2, 5). x > 3 is (3, +∞). x ≤ 1 is (−∞, 1]. The symbol ∞ always has a round bracket.\n"
  "On a number line, a filled circle means included and an open circle means left out.\n"
  "Solve a linear inequality like an equation, with one extra rule: multiplying or dividing both sides by a negative number turns the sign round.\n"
  "Example: −3x + 4 ≥ 10 → −3x ≥ 6 → x ≤ −2, that is (−∞, −2].",
  worked({"a": 3, "b": -5, "c": 1, "d": 7},
         "Solve {poly([a, 'x'], [b, ''])} < {poly([c, 'x'], [d, ''])} and write the answer in interval notation.",
         ["Subtract {mono(c, 'x')} from both sides: {poly([a - c, 'x'], [b, ''])} < {d}.",
          "Add {-b} to both sides: {mono(a - c, 'x')} < {d - b}.",
          "Divide by {a - c}, a positive number, so the sign stays: x < {(d - b) / (a - c)}."],
         "x < {(d - b) / (a - c)}, that is {interval('-inf', (d - b) / (a - c), false, false)}",
         checks=["(d - b) % (a - c) == 0", "a - c > 0"]),
  [card("c4m16-1", "Square brackets include the end; round brackets leave it out. ∞ always takes a round bracket.",
        ["{-2} ≤ x < {5} is {interval(-2, 5, true, false)}", "x > {3} is {interval(3, 'inf', false, false)}"], "m4-16-interval"),
   card("c4m16-2", "Solve an inequality like an equation: do the same to both sides.",
        ["{poly([2, 'x'], [3, ''])} < {11} → {mono(2, 'x')} < {8} → x < {4}"], "m4-16-solve"),
   card("c4m16-3", "Multiplying or dividing by a negative number turns the inequality sign round.",
        ["{poly([-3, 'x'], [4, ''])} ≥ {10} → {mono(-3, 'x')} ≥ {6} → x ≤ {-2}"], "m4-16-neg")],
  [mcq("m4-16-interval", 1, "Write {intervalIneq(a, b, ca, cb)} in interval notation.",
       "{interval(a, b, ca, cb)}",
       [("{interval(a, b, !ca, !cb)}", "swap"), ("{interval(a, b, true, true)}", "closed"), ("{interval(a, b, false, false)}", "open")],
       ["{ca ? '≤ means the end ' + fmt(a) + ' is included: [' : '< means the end ' + fmt(a) + ' is left out: ('}.",
        "{cb ? '≤ means ' + fmt(b) + ' is included: ]' : '< means ' + fmt(b) + ' is left out: )'}.", "So the answer is {answer}."],
       vars={"a": {"int": [-9, 4]}, "w": {"int": [2, 9]}, "b": {"expr": "a + w"}, "ca": {"pick": [True, False]}, "cb": {"pick": [True, False]}},
       misc=[("swap", "A square bracket means 'included' (≤); a round bracket means 'left out' (<)."),
             ("closed", "Only an end with ≤ gets a square bracket."),
             ("open", "An end with ≤ is included, so it gets a square bracket.")],
       sources=SRC, where=["ca != cb"]),
   num("m4-16-solve", 1, "Solve {poly([a, 'x'], [b, ''])} < {poly([c, 'x'], [d, ''])}. What is the largest whole number x can be?",
       "(d - b) / (a - c) - 1",
       ["Collect x on the left: {mono(a - c, 'x')} < {d - b}.", "Divide by {a - c}: x < {(d - b) / (a - c)}.",
        "x must be less than {(d - b) / (a - c)}, so the largest whole number is {answer}."],
       vars={"a": {"int": [3, 7]}, "c": {"int": [1, 2]}, "b": {"int": [-9, 9]}, "k": {"int": [-4, 8]}, "d": {"expr": "b + k * (a - c)"}},
       misc=[("equal", "(d - b) / (a - c)", "x < {(d - b) / (a - c)} leaves out {(d - b) / (a - c)} itself: the sign is <, not ≤."),
             ("nodiv", "d - b - 1", "Divide by {a - c} as well: {mono(a - c, 'x')} < {d - b} gives x < {(d - b) / (a - c)}.")],
       sources=SRC, where=["a - c != 1", "b != 0"], signed=True),
   mcq("m4-16-neg", 2, "Solve {poly([-a, 'x'], [b, ''])} ≥ {b + a * k}.",
       "{interval('-inf', -k, false, true)}",
       [("{interval(-k, 'inf', true, false)}", "noflip"), ("{interval('-inf', -k, false, false)}", "strict"), ("{interval('-inf', k, false, true)}", "sign")],
       ["Subtract {b}: {mono(-a, 'x')} ≥ {a * k}.", "Divide by {-a}, a negative number, so the sign turns round: x ≤ {-k}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [-9, 9]}, "k": {"int": [-6, 6]}},
       misc=[("noflip", "Dividing by the negative number {-a} turns ≥ into ≤."),
             ("strict", "The sign ≥ includes the end, so it stays included: x ≤ {-k} uses a square bracket."),
             ("sign", "{a * k} ÷ {br(-a)} = {-k}, not {k}.")],
       sources=SRC, where=["k != 0", "b != 0"]),
   num("m4-16-double", 3, "How many whole numbers x satisfy {lo} < {poly([2, 'x'], [q, ''])} ≤ {hi}?",
       "floor((hi - q) / 2) - floor((lo - q) / 2)",
       ["Subtract {q} from all three parts: {lo - q} < {mono(2, 'x')} ≤ {hi - q}.", "Divide by {2}: {(lo - q) / 2} < x ≤ {(hi - q) / 2}.",
        "The whole numbers are {listStr(intsIn((lo - q) / 2, (hi - q) / 2, false, true))}: there are {answer}."],
       vars={"q": {"int": [-5, 5]}, "lo": {"int": [-9, 3]}, "w": {"int": [6, 12]}, "hi": {"expr": "lo + w"}},
       misc=[("both", "floor((hi - q) / 2) - floor((lo - q) / 2) + (abs(lo - q) % 2 == 0 ? 1 : 0)", "The left sign is <, so {(lo - q) / 2} itself is left out.", "abs(lo - q) % 2 == 0"),
             ("nohalf", "hi - lo", "Divide every part by {2} before counting.")],
       sources=SRC)],
  learn=learn(
    [goal("write sets of numbers in interval notation and solve linear inequalities, turning the sign when you multiply or divide by a negative number.",
          "Form Three inequalities and the number line.",
          "absolute values (Lessons {17} and {18}), quadratic inequalities (Lesson {19}) and regions on graphs."),
     ("Interval notation",
      "A set of numbers between two ends can be written with brackets.\n"
      "• [a, b]: a ≤ x ≤ b, both ends included.\n• (a, b): a < x < b, both ends left out.\n• [a, b): a ≤ x < b.\n"
      "• (a, +∞): x > a. (−∞, b]: x ≤ b. The symbol ∞ is never reached, so it always takes a round bracket.\n"
      "Example: the ages of pupils in a class, at least {13} and under {16}, form {interval(13, 16, true, false)}.\n"
      "On a number line: a filled circle for an included end, an open circle for one left out."),
     ("Solving and the negative rule",
      "Treat an inequality like an equation: add, subtract, multiply or divide both sides by the same number.\n"
      "• {poly([3, 'x'], [-5, ''])} < x + {7} → {mono(2, 'x')} < {12} → x < {6}.\n"
      "One extra rule: multiplying or dividing by a negative number turns the sign round. "
      "Check with numbers: {2} < {5}, but {-2} > {-5}.\n"
      "• {poly([-3, 'x'], [4, ''])} ≥ {10} → {mono(-3, 'x')} ≥ {6} → x ≤ {-2}, that is {interval('-inf', -2, false, true)}.")],
    key_words=[("interval", "all the numbers between two ends, such as {interval(-1, 4, true, false)}"),
               ("inequality", "a statement with <, >, ≤ or ≥"),
               ("infinity (∞)", "without end; it is never included")],
    examples=["x ≥ {-3} is {interval(-3, 'inf', true, false)}", "{1} < x ≤ {6} is {interval(1, 6, false, true)}", "{mono(-2, 'x')} < {8} → x > {-4}"],
    mistake=("{mono(-2, 'x')} < {8} → x < {-4}", "{mono(-2, 'x')} < {8} → x > {-4}",
             "Dividing by {-2} turns the sign round. Check: x = {0} makes {mono(-2, 'x')} = {0} < {8}, and {0} > {-4}.")))

# ---------------------------------------------------------------- 17. Absolute value equations
L.lesson(D, S, 17, ("m4-17", "Understand absolute value and solve absolute value equations"), [16],
  "The absolute value |x| is the distance of x from 0 on the number line, so it is never negative: |5| = 5 and |−5| = 5.\n"
  "|x − a| is the distance between x and a.\n"
  "• |x| = k (k > 0) has two solutions: x = k or x = −k.\n"
  "• |x − a| = k: x − a = k or x − a = −k, so x = a + k or x = a − k.\n"
  "• |ax + b| = c: solve ax + b = c and ax + b = −c.\n"
  "If k is negative there is no solution; if k = 0 there is one solution.",
  worked({"a": 2, "b": -3, "c": 7},
         "Solve |{poly([a, 'x'], [b, ''])}| = {c}.",
         ["Either {poly([a, 'x'], [b, ''])} = {c} or {poly([a, 'x'], [b, ''])} = {-c}.",
          "First: {mono(a, 'x')} = {c - b}, so x = {(c - b) / a}.",
          "Second: {mono(a, 'x')} = {-c - b}, so x = {(-c - b) / a}."],
         "x = {(c - b) / a} or x = {(-c - b) / a}",
         checks=["(c - b) % a == 0", "(-c - b) % a == 0"]),
  [card("c4m17-1", "|x| is the distance from {0}: it is never negative.",
        ["|{-6}| = {6} and |{6}| = {6}"], "m4-17-value"),
   card("c4m17-2", "|x − a| = k means x is k units from a: x = a + k or x = a − k.",
        ["|x − {3}| = {5} → x = {8} or x = {-2}"], "m4-17-two"),
   card("c4m17-3", "For |ax + b| = c, solve two equations: ax + b = c and ax + b = −c.",
        ["|{poly([2, 'x'], [1, ''])}| = {7} → {mono(2, 'x')} + {1} = {7} or {-7} → x = {3} or {-4}"], "m4-17-ax")],
  [num("m4-17-value", 1, "Work out |{a}| − |{b}|.",
       "abs(a) - abs(b)",
       ["|{a}| = {abs(a)} and |{b}| = {abs(b)}: absolute values are never negative.", "{abs(a)} − {abs(b)} = {answer}."],
       vars={"a": {"int": [-12, 12]}, "b": {"int": [-12, 12]}},
       misc=[("plain", "a - b", "Take the absolute values first: |{a}| = {abs(a)}, |{b}| = {abs(b)}."),
             ("absdiff", "abs(a - b)", "Work out each absolute value first, then subtract.")],
       sources=SRC, where=["a < 0 || b < 0", "a != 0 && b != 0", "abs(a) - abs(b) != a - b", "abs(a - b) != abs(a) - abs(b)"], signed=True),
   num("m4-17-two", 1, "Solve |x − {br(a)}| = {k}. Give the larger solution.",
       "a + k",
       ["x − {br(a)} = {k} or x − {br(a)} = {-k}.", "x = {a + k} or x = {a - k}.", "The larger solution is {answer}."],
       vars={"a": {"int": [-9, 9]}, "k": {"int": [2, 9]}},
       misc=[("small", "a - k", "That is the smaller solution. The larger is {a} + {k} = {a + k}."),
             ("onlyk", "k", "x is {k} units from {a}, not from {0}: x = {a} + {k}."),
             ("signa", "-a + k", "|x − {br(a)}| is the distance from {a}, so x = {a} ± {k}.")],
       sources=SRC, where=["a != 0", "a + k != k", "-a + k != a + k"], signed=True),
   mcq("m4-17-ax", 2, "Solve |{poly([a, 'x'], [b, ''])}| = {c}.",
       "x = {(c - b) / a} or x = {(-c - b) / a}",
       [("x = {(c - b) / a} only", "one"), ("x = {(c - b) / a} or x = {(c + b) / a}", "signb"), ("x = {c - b} or x = {-c - b}", "nodiv")],
       ["{poly([a, 'x'], [b, ''])} = {c} gives x = {(c - b) / a}.", "{poly([a, 'x'], [b, ''])} = {-c} gives x = {(-c - b) / a}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 4]}, "b": {"int": [-9, 9]}, "c": {"int": [1, 15]}},
       misc=[("one", "The expression inside can also equal {-c}: that gives a second solution."),
             ("signb", "In the second equation, {poly([a, 'x'], [b, ''])} = {-c}: subtract {b} from {-c}."),
             ("nodiv", "After {mono(a, 'x')} = …, divide by {a}.")],
       sources=SRC, where=["b != 0", "(c - b) % a == 0", "(-c - b) % a == 0", "(c + b) % a == 0", "(c + b) / a != (-c - b) / a"]),
   num("m4-17-count", 2, "How many solutions does |x − {br(a)}| = {k} have? (Type 0, 1 or 2.)",
       "k > 0 ? 2 : k == 0 ? 1 : 0",
       ["An absolute value is a distance, so it is never negative.",
        "{k > 0 ? 'The distance ' + fmt(k) + ' is positive: x can be on either side of ' + fmt(a) + ', so two solutions.' : k == 0 ? 'Distance 0: x is exactly ' + fmt(a) + ', one solution.' : 'A distance cannot be ' + fmt(k) + ': no solution.'}",
        "So the answer is {answer}."],
       vars={"a": {"int": [-9, 9]}, "k": {"pick": [-5, -3, -1, 0, 2, 4, 6]}},
       misc=[("two", "k > 0 ? 1 : 2", "Check the sign of {k}: positive gives two solutions, {0} gives one, negative gives none.")],
       sources=SRC, where=["a != 0"]),
   num("m4-17-both", 3, "Solve |{poly([2, 'x'], [-a, ''])}| = |{poly([1, 'x'], [b, ''])}|. Give the larger solution.",
       "max(a + b, (a - b) / 3)",
       ["Either {poly([2, 'x'], [-a, ''])} = {poly([1, 'x'], [b, ''])}, giving x = {a + b},",
        "or {poly([2, 'x'], [-a, ''])} = −({poly([1, 'x'], [b, ''])}), giving {mono(3, 'x')} = {a - b}, x = {(a - b) / 3}.",
        "The larger solution is {answer}."],
       vars={"a": {"int": [-9, 9]}, "b": {"int": [-9, 9]}},
       misc=[("one", "min(a + b, (a - b) / 3)", "That is the smaller solution. Work out both cases and compare.")],
       sources=SRC, where=["(a - b) % 3 == 0", "a + b != (a - b) / 3", "a != 0 && b != 0"], signed=True)],
  learn=learn(
    [goal("explain |x − a| as a distance and solve absolute value equations, finding both solutions or none.",
          "Lesson {16} (inequalities and the number line).",
          "Lesson {18} (absolute value inequalities) and errors and tolerances in measurement."),
     ("Absolute value as distance",
      "|x| is how far x is from {0}, without caring about direction. So |{7}| = {7} and |{-7}| = {7}.\n"
      "|x − a| is the distance between x and a.\n"
      "• |{5} − {2}| = {3}: {5} is {3} units from {2}.\n• |{-1} − {2}| = {3}: {-1} is also {3} units from {2}.\n"
      "A distance is never negative, so |anything| ≥ {0}."),
     ("Solving the equations",
      "|x − {2}| = {3} asks: which numbers are {3} units from {2}? Going right: {5}. Going left: {-1}.\n"
      "In algebra: x − {2} = {3} or x − {2} = {-3}, so x = {5} or x = {-1}.\n"
      "With a coefficient: |{poly([2, 'x'], [-3, ''])}| = {7} → {poly([2, 'x'], [-3, ''])} = {7} or {-7} → x = {5} or x = {-2}.\n"
      "Special cases: |x − {2}| = {0} has one solution (x = {2}); |x − {2}| = {-1} has none.")],
    key_words=[("absolute value", "the size of a number without its sign: |{-4}| = {4}"),
               ("distance", "how far apart two numbers are on the number line"),
               ("modulus", "another name for absolute value")],
    examples=["|x| = {9} → x = {9} or {-9}", "|x + {4}| = {1} → x = {-3} or {-5}", "|x − {6}| = {-2} → no solution"],
    mistake=("|x − {2}| = {3} → x = {5}", "|x − {2}| = {3} → x = {5} or x = {-1}",
             "There are two numbers {3} units from {2}, one on each side.")))

# ---------------------------------------------------------------- 18. Absolute value inequalities
L.lesson(D, S, 18, ("m4-18", "Solve absolute value inequalities |x − a| < b and |x − a| > b"), [17],
  "Think of |x − a| as the distance from x to a.\n"
  "• |x − a| < b: x is closer than b to a, so a − b < x < a + b. One interval: (a − b, a + b).\n"
  "• |x − a| > b: x is further than b from a, so x < a − b or x > a + b. Two pieces.\n"
  "With ≤ or ≥ the ends are included.\n"
  "Example: |x − 3| ≤ 2 → 1 ≤ x ≤ 5, that is [1, 5]. |x + 1| > 4 → x < −5 or x > 3.\n"
  "For |ax + b| < c write −c < ax + b < c and solve all three parts.",
  worked({"a": 3, "k": 2},
         "Solve |x − {a}| ≤ {k} and write the answer in interval notation.",
         ["|x − {a}| ≤ {k} means x is at most {k} away from {a}.", "So {a} − {k} ≤ x ≤ {a} + {k}.", "That is {a - k} ≤ x ≤ {a + k}."],
         "{interval(a - k, a + k, true, true)}",
         checks=["a - k == 1"]),
  [card("c4m18-1", "|x| < k means x lies between −k and k.",
        ["|x| < {4} → {-4} < x < {4}"], "m4-18-zero"),
   card("c4m18-2", "|x − a| ≤ b: the numbers at most b away from a form one interval [a − b, a + b].",
        ["|x − {3}| ≤ {2} → {interval(1, 5, true, true)}"], "m4-18-in"),
   card("c4m18-3", "|x − a| > b: the numbers more than b away from a lie on both sides, outside the interval.",
        ["|x + {1}| > {4} → x < {-5} or x > {3}"], "m4-18-out")],
  [mcq("m4-18-zero", 1, "Solve |x| < {k}.",
       "{-k} < x < {k}",
       [("x < {k}", "half"), ("x < {-k} or x > {k}", "out"), ("{-k} ≤ x ≤ {k}", "ends")],
       ["|x| < {k} means x is less than {k} away from {0}.", "So x lies between {-k} and {k}, ends left out.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 12]}},
       misc=[("half", "x = {-k - 3} is less than {k}, but |{-k - 3}| = {k + 3} is not less than {k}."),
             ("out", "That describes |x| > {k}: the numbers far from {0}."),
             ("ends", "The sign is <, so ±{k} themselves are left out.")],
       sources=SRC),
   mcq("m4-18-in", 1, "Solve |x − {br(a)}| ≤ {k}.",
       "{interval(a - k, a + k, true, true)}",
       [("{interval(-k, k, true, true)}", "centre"), ("{interval(a - k, a + k, false, false)}", "open"), ("{interval(k - a, k + a, true, true)}", "swap")],
       ["The numbers at most {k} away from {a}.", "{a} − {k} ≤ x ≤ {a} + {k}.", "So the answer is {answer}."],
       vars={"a": {"int": [-6, 6]}, "k": {"int": [1, 6]}},
       misc=[("centre", "The centre is {a}, not {0}: start from {a} and go {k} each way."),
             ("open", "≤ includes the ends, so use square brackets."),
             ("swap", "The ends are {a} − {k} and {a} + {k}.")],
       sources=SRC, where=["a != 0", "k != a && k != -a", "a > 0 || k - a != a - k"]),
   mcq("m4-18-out", 2, "Solve |x − {br(a)}| > {k}.",
       "x < {a - k} or x > {a + k}",
       [("{a - k} < x < {a + k}", "inside"), ("x > {a + k}", "half"), ("x < {-k} or x > {k}", "centre")],
       ["The numbers more than {k} away from {a}: on the left below {a - k}, on the right above {a + k}.", "So the answer is {answer}."],
       vars={"a": {"int": [-6, 6]}, "k": {"int": [1, 6]}},
       misc=[("inside", "That is |x − {br(a)}| < {k}: the numbers close to {a}."),
             ("half", "Numbers far away on the left count too: x < {a - k}."),
             ("centre", "The distance is measured from {a}, not from {0}.")],
       sources=SRC, where=["a != 0"]),
   num("m4-18-count", 2, "How many whole numbers satisfy |x − {br(a)}| < {k}?",
       "2 * k - 1",
       ["{a - k} < x < {a + k}.", "The whole numbers from {a - k + 1} to {a + k - 1}.", "There are {answer}."],
       vars={"a": {"int": [-6, 6]}, "k": {"int": [2, 7]}},
       misc=[("ends", "2 * k + 1", "The sign is <, so {a - k} and {a + k} are left out."),
             ("onehalf", "k", "Count both sides of {a}: {k - 1} below, {k - 1} above, and {a} itself.")],
       sources=SRC, where=["a != 0"]),
   mcq("m4-18-ax", 3, "Solve |{poly([m, 'x'], [b, ''])}| ≤ {c}.",
       "{interval((-c - b) / m, (c - b) / m, true, true)}",
       [("{interval(-c - b, c - b, true, true)}", "nodiv"), ("{interval((-c + b) / m, (c + b) / m, true, true)}", "signb"), ("{intervalIneq('-inf', (-c - b) / m, false, true)} or x ≥ {(c - b) / m}", "out")],
       ["Write {-c} ≤ {poly([m, 'x'], [b, ''])} ≤ {c}.", "Subtract {b}: {-c - b} ≤ {mono(m, 'x')} ≤ {c - b}.",
        "Divide by {m}: {(-c - b) / m} ≤ x ≤ {(c - b) / m}.", "So the answer is {answer}."],
       vars={"m": {"int": [2, 3]}, "b": {"int": [-9, 9]}, "c": {"int": [2, 15]}},
       misc=[("nodiv", "Divide every part by {m}."),
             ("signb", "Take {b} away from every part: {-c} − {br(b)} = {-c - b} and {c} − {br(b)} = {c - b}."),
             ("out", "≤ means close to the centre: one interval, not two pieces.")],
       sources=SRC, where=["b != 0", "(c - b) % m == 0", "(-c - b) % m == 0", "(c + b) % m == 0"])],
  learn=learn(
    [goal("turn an absolute value inequality into an interval (or two pieces) and show it on a number line.",
          "Lesson {17} (absolute value as distance) and Lesson {16} (interval notation).",
          "Lesson {19} (quadratic inequalities) and tolerances such as {50} cm ± {2} cm."),
     ("Close to a: one interval",
      "|x − {3}| ≤ {2} asks for the numbers at most {2} away from {3}.\n"
      "Start at {3} and go {2} each way: from {1} to {5}. So {1} ≤ x ≤ {5}, that is {interval(1, 5, true, true)}.\n"
      "In general |x − a| < b gives a − b < x < a + b: one interval, centre a, half-width b.\n"
      "With a coefficient, write it as a double inequality: |{poly([2, 'x'], [1, ''])}| < {7} → {-7} < {poly([2, 'x'], [1, ''])} < {7} → {-4} < x < {3}."),
     ("Far from a: two pieces",
      "|x + {1}| > {4} means x − ({-1}) is more than {4} from {0}: x is more than {4} away from {-1}.\n"
      "On the left: x < {-1} − {4} = {-5}. On the right: x > {-1} + {4} = {3}.\n"
      "So x < {-5} or x > {3}. On a number line this is two arrows pointing away from each other.\n"
      "A tolerance works the same way: a length of {50} cm ± {2} cm means |L − {50}| ≤ {2}, so {48} ≤ L ≤ {52}.")],
    key_words=[("absolute value inequality", "an inequality with |…|, such as |x − {3}| ≤ {2}"),
               ("centre", "the number a in |x − a|"),
               ("tolerance", "the largest allowed difference from a target value")],
    examples=["|x| ≤ {3} → {interval(-3, 3, true, true)}", "|x − {1}| < {4} → {interval(-3, 5, false, false)}", "|x| ≥ {2} → x ≤ {-2} or x ≥ {2}"],
    mistake=("|x − {1}| > {3} → {-2} < x < {4}", "|x − {1}| > {3} → x < {-2} or x > {4}",
             "> means far from the centre: the solutions lie outside the interval, on both sides.")))

# ---------------------------------------------------------------- 19. Quadratic inequalities
L.lesson(D, S, 19, ("m4-19", "Solve quadratic inequalities"), [7, 16],
  "To solve a quadratic inequality:\n"
  "1. Make one side 0 and factorise: (x − p)(x − q), with p < q.\n"
  "2. The roots p and q split the number line into three parts. Test the sign of the product in each part.\n"
  "3. (x − p)(x − q) < 0 between the roots: p < x < q. (x − p)(x − q) > 0 outside: x < p or x > q.\n"
  "Example: x² − x − 6 ≤ 0 → (x + 2)(x − 3) ≤ 0 → −2 ≤ x ≤ 3.\n"
  "Do not take square roots of an inequality: x² < 9 means −3 < x < 3, not just x < 3.",
  worked({"p": -2, "q": 3},
         "Solve {quad(1, -(p + q), p * q)} ≤ {0}.",
         ["Factorise: {lin2(1, -p, 1, -q)} ≤ {0}. The roots are {p} and {q}.",
          "Test x = {0}, between the roots: ({0} + {-p})({0} − {q}) = {-p} × {br(-q)} = {p * q}, negative. So the product is negative between the roots.",
          "≤ {0} means negative or zero: between the roots, ends included."],
         "{p} ≤ x ≤ {q}",
         checks=["p * q < 0"]),
  [card("c4m19-1", "The roots split the number line; the sign of (x − p)(x − q) changes only at the roots.",
        ["(x + {2})(x − {3}): negative for {-2} < x < {3}, positive outside"], "m4-19-inside"),
   card("c4m19-2", "< {0}: between the roots. > {0}: outside the roots.",
        ["(x − {1})(x − {5}) > {0} → x < {1} or x > {5}"], "m4-19-outside"),
   card("c4m19-3", "x² < k² has two ends: −k < x < k.",
        ["x² < {9} → {-3} < x < {3}"], "m4-19-square")],
  [mcq("m4-19-inside", 1, "Solve {lin2(1, -p, 1, -q)} < {0}.",
       "{p} < x < {q}",
       [("x < {p} or x > {q}", "out"), ("{-q} < x < {-p}", "sign"), ("{p} ≤ x ≤ {q}", "ends")],
       ["The roots are {p} and {q}.", "Test x = {(p + q) / 2} between them: the brackets have opposite signs, so the product is negative.", "So the answer is {answer}."],
       vars={"p": {"int": [-8, 5]}, "w": {"pick": [2, 4, 6, 8]}, "q": {"expr": "p + w"}},
       misc=[("out", "That is where the product is positive (> {0}). Test a number between the roots."),
             ("sign", "x − {br(p)} = {0} at x = {p}: the roots have the opposite signs to the numbers in the brackets."),
             ("ends", "< {0} leaves out the roots, where the product is {0}.")],
       sources=SRC, where=["p != 0 && q != 0", "-q != p"]),
   mcq("m4-19-outside", 1, "Solve {lin2(1, -p, 1, -q)} ≥ {0}.",
       "x ≤ {p} or x ≥ {q}",
       [("{p} ≤ x ≤ {q}", "in"), ("x ≥ {q}", "half"), ("x < {p} or x > {q}", "ends")],
       ["The roots are {p} and {q}; the product is positive outside them and {0} at them.", "So the answer is {answer}."],
       vars={"p": {"int": [-8, 5]}, "w": {"int": [2, 8]}, "q": {"expr": "p + w"}},
       misc=[("in", "Between the roots the product is negative. ≥ {0} needs positive or zero."),
             ("half", "Numbers below {p} also give a positive product: both brackets are negative."),
             ("ends", "≥ includes the roots, where the product equals {0}.")],
       sources=SRC, where=["p != 0 && q != 0"]),
   mcq("m4-19-solve", 2, "Solve {quad(1, -(p + q), p * q)} < {0}.",
       "{p} < x < {q}",
       [("x < {p} or x > {q}", "out"), ("{-q} < x < {-p}", "sign"), ("x < {q}", "one")],
       ["Factorise: {lin2(1, -p, 1, -q)} < {0}.", "Negative between the roots {p} and {q}.", "So the answer is {answer}."],
       vars={"p": {"int": [-8, 5]}, "w": {"int": [2, 8]}, "q": {"expr": "p + w"}},
       misc=[("out", "Outside the roots the product is positive. < {0} needs negative."),
             ("sign", "Check: x = {(-p - q) / 2} does not make the expression negative. Factorise and read the roots carefully."),
             ("one", "Numbers below {p} make both brackets negative, so the product is positive: they are not solutions.")],
       sources=SRC, where=["p != 0 && q != 0", "p + q != 0", "(p + q) % 2 == 0"]),
   num("m4-19-count", 2, "How many whole numbers x satisfy {quad(1, -(p + q), p * q)} ≤ {0}?",
       "q - p + 1",
       ["Factorise: {lin2(1, -p, 1, -q)} ≤ {0}, so {p} ≤ x ≤ {q}.", "Whole numbers from {p} to {q}: {q} − {br(p)} + {1} = {answer}."],
       vars={"p": {"int": [-8, 5]}, "w": {"int": [2, 9]}, "q": {"expr": "p + w"}},
       misc=[("strict", "q - p - 1", "≤ includes the roots {p} and {q}."),
             ("noone", "q - p", "Count both ends: from {p} to {q} there are {q} − {br(p)} + {1} numbers.")],
       sources=SRC, where=["p != 0 && q != 0", "p + q != 0"]),
   mcq("m4-19-square", 3, "Solve x² > {k * k}.",
       "x < {-k} or x > {k}",
       [("x > {k}", "root"), ("{-k} < x < {k}", "in"), ("x > {k * k}", "nosq")],
       ["x² − {k * k} > {0}: {lin2(1, k, 1, -k)} > {0}.", "Positive outside the roots {-k} and {k}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 12]}},
       misc=[("root", "x = {-k - 1} also works: ({-k - 1})² = {(k + 1) * (k + 1)} > {k * k}. Do not just take the square root."),
             ("in", "Between {-k} and {k}, x² is less than {k * k}."),
             ("nosq", "Compare x² with {k * k}, so the ends are ±{k}.")],
       sources=SRC)],
  learn=learn(
    [goal("solve quadratic inequalities by factorising and testing the sign between and outside the roots.",
          "Lesson {7} (roots of quadratics) and Lesson {16} (inequalities and intervals).",
          "graphs of quadratic functions (Lesson {23}), where the same answer is read from the curve."),
     ("Signs between and outside the roots",
      "Take (x + {2})(x − {3}). It is {0} at x = {-2} and x = {3}. These roots split the number line into three parts.\n"
      "• x = {-5} (left): ({-3})({-8}) = {24}, positive.\n• x = {0} (middle): ({2})({-3}) = {-6}, negative.\n• x = {5} (right): ({7})({2}) = {14}, positive.\n"
      "So (x + {2})(x − {3}) < {0} for {-2} < x < {3}, and > {0} for x < {-2} or x > {3}.\n"
      "For a positive x² term the pattern is always + − +."),
     ("The method",
      "• Make one side {0}: x² − x > {6} becomes {quad(1, -1, -6)} > {0}.\n"
      "• Factorise: {lin2(1, 2, 1, -3)} > {0}. Roots {-2} and {3}.\n"
      "• > {0}: outside the roots. Answer: x < {-2} or x > {3}.\n"
      "Use ≤ or ≥ to include the roots.\n"
      "Careful with squares: x² < {9} means {-3} < x < {3}. Taking the square root alone would lose the negative side.")],
    key_words=[("quadratic inequality", "an inequality with an x² term, such as {quad(1, -1, -6)} > {0}"),
               ("critical values", "the roots, where the sign can change"),
               ("sign test", "trying one number in each part to see whether the expression is positive or negative")],
    examples=["(x − {1})(x − {4}) < {0} → {1} < x < {4}", "{quad(1, 0, -16)} ≥ {0} → x ≤ {-4} or x ≥ {4}"],
    mistake=("x² < {9} → x < {3}", "x² < {9} → {-3} < x < {3}",
             "x = {-5} is less than {3}, but ({-5})² = {25} is not less than {9}. Both ends are needed.")))
