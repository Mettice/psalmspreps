"""Form 4 Maths, Term 1, rows 12-15: polynomials (long division, the factor and remainder theorems, factorising and
solving cubics). Run: python tools/authoring/form4/maths_poly.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import goal, bank

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRC = ["polynomials"]

# (x − p)(x − q)(x − r) = x³ − (p + q + r)x² + (pq + pr + qr)x − pqr
E2, E1, E0 = "-(p + q + r)", "p * q + p * r + q * r", "-p * q * r"

# ---------------------------------------------------------------- 12. Long division with algebraic expressions
L.lesson(D, S, 12, ("m4-12", "Divide a polynomial by x − k using long division"), [2],
  "Long division of polynomials works like long division of numbers.\n"
  "1. Divide the first term of what is left by x: that gives the next term of the quotient.\n"
  "2. Multiply the whole divisor by that term and write it underneath.\n"
  "3. Subtract, and bring down the next term.\n"
  "Repeat until the degree of what is left is less than the divisor's. What is left is the remainder.\n"
  "Example: (x² + 5x + 7) ÷ (x + 2) = x + 3, remainder 1, because (x + 2)(x + 3) + 1 = x² + 5x + 7.\n"
  "Write missing powers with 0: x³ − 8 is x³ + 0x² + 0x − 8.",
  worked({"k": 2, "p": 1, "q": -3, "r": 5},
         "Divide {cubic(1, p - k, q - p * k, r - q * k)} by ({poly([1, 'x'], [-k, ''])}).",
         ["x³ ÷ x = x². Multiply: x²({poly([1, 'x'], [-k, ''])}) = {poly([1, 'x³'], [-k, 'x²'])}. Subtract: {poly([p, 'x²'], [q - p * k, 'x'])} is left.",
          "{mono(p, 'x²')} ÷ x = {mono(p, 'x')}. Multiply: {mono(p, 'x')}({poly([1, 'x'], [-k, ''])}) = {poly([p, 'x²'], [-p * k, 'x'])}. Subtract: {poly([q, 'x'], [r - q * k, ''])} is left.",
          "{mono(q, 'x')} ÷ x = {q}. Multiply: {q}({poly([1, 'x'], [-k, ''])}) = {poly([q, 'x'], [-q * k, ''])}. Subtract: {r} is left.",
          "The quotient is {quad(1, p, q)} and the remainder is {r}."],
         "{quad(1, p, q)}, remainder {r}",
         checks=["r == 5"]),
  [card("c4m12-1", "Each step: divide the first term by x, multiply the whole divisor by the result, subtract.",
        ["{quad(1, 5, 6)} ÷ (x + {2}): x² ÷ x = x; x(x + {2}) = {quad(1, 2, 0)}; subtract: {mono(3, 'x')} + {6}"], "m4-12-exact"),
   card("c4m12-2", "What is left at the end, with a lower power than the divisor, is the remainder.",
        ["{quad(1, 5, 7)} ÷ (x + {2}) = x + {3}, remainder {1}"], "m4-12-rem"),
   card("c4m12-3", "Fill missing powers with zero terms so that the columns line up.",
        ["{poly([1, 'x³'], [-8, ''])} = x³ + {0}x² + {0}x − {8}"], "m4-12-gap")],
  [mcq("m4-12-exact", 1, "Divide {quad(1, m - k, -m * k)} by ({poly([1, 'x'], [-k, ''])}).",
       "{poly([1, 'x'], [m, ''])}",
       [("{poly([1, 'x'], [-m, ''])}", "sign"), ("{poly([1, 'x'], [-k, ''])}", "divisor"), ("{poly([1, 'x'], [m - k, ''])}", "middle")],
       ["x² ÷ x = x; x({poly([1, 'x'], [-k, ''])}) = {quad(1, -k, 0)}; subtract: {poly([m, 'x'], [-m * k, ''])} is left.",
        "{mono(m, 'x')} ÷ x = {m}; {m}({poly([1, 'x'], [-k, ''])}) = {poly([m, 'x'], [-m * k, ''])}; nothing is left.", "So the answer is {answer}."],
       vars={"k": {"int": [-6, 6]}, "m": {"int": [-9, 9]}},
       misc=[("sign", "Check: ({poly([1, 'x'], [-k, ''])})({poly([1, 'x'], [-m, ''])}) has number term {m * k}, not {-m * k}."),
             ("divisor", "The quotient times the divisor must give the expression; ({poly([1, 'x'], [-k, ''])})² does not."),
             ("middle", "Subtract x({poly([1, 'x'], [-k, ''])}) first: what is left starts {mono(m, 'x')}, so the quotient is x + {br(m)}.")],
       sources=SRC, where=["k != 0 && m != 0", "m != k && m != -k", "m - k != 0", "m - k != -m"]),
   num("m4-12-rem", 1, "Divide {quad(1, b, c)} by ({poly([1, 'x'], [-k, ''])}). What is the remainder?",
       "k * k + b * k + c",
       ["x² ÷ x = x; subtract x({poly([1, 'x'], [-k, ''])}): {poly([b + k, 'x'], [c, ''])} is left.",
        "{mono(b + k, 'x')} ÷ x = {b + k}; subtract {b + k}({poly([1, 'x'], [-k, ''])}): {c} + {br((b + k) * k)} is left.", "The remainder is {answer}."],
       vars={"b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}, "k": {"int": [-5, 5]}},
       misc=[("c", "c", "{c} is not the remainder: after both subtractions {c} + {br((b + k) * k)} is left."),
             ("negk", "k * k - b * k + c", "Divide by ({poly([1, 'x'], [-k, ''])}): the remainder is the value at x = {k}, not {-k}.")],
       sources=SRC, where=["k != 0 && b != 0 && c != 0", "k * k + b * k + c != 0", "b * k != 0"], signed=True),
   mcq("m4-12-cubic", 2, "Divide {cubic(1, p - k, q - p * k, -q * k)} by ({poly([1, 'x'], [-k, ''])}).",
       "{quad(1, p, q)}",
       [("{quad(1, -p, q)}", "sign"), ("{quad(1, p - k, q)}", "first"), ("{quad(1, p, -q * k)}", "last")],
       ["x³ ÷ x = x²; subtract x²({poly([1, 'x'], [-k, ''])}): {poly([p, 'x²'], [q - p * k, 'x'])} is left.",
        "{mono(p, 'x²')} ÷ x = {mono(p, 'x')}; subtract: {poly([q, 'x'], [-q * k, ''])} is left; ÷ x gives {q}, remainder {0}.", "So the answer is {answer}."],
       vars={"k": {"int": [-4, 4]}, "p": {"int": [-6, 6]}, "q": {"int": [-9, 9]}},
       misc=[("sign", "Multiply back: ({poly([1, 'x'], [-k, ''])})({quad(1, -p, q)}) does not give {mono(p - k, 'x²')}."),
             ("first", "Subtract x²({poly([1, 'x'], [-k, ''])}) before dividing again: {mono(p - k, 'x²')} + {mono(k, 'x²')} = {mono(p, 'x²')}."),
             ("last", "The last term of the quotient is {mono(q, 'x')} ÷ x = {q}, not the whole number term.")],
       sources=SRC, where=["k != 0 && p != 0 && q != 0", "p - k != 0", "q - p * k != 0", "p != k", "-q * k != q"]),
   num("m4-12-plus", 2, "Find the remainder when {cubic(1, b, c, d)} is divided by ({poly([1, 'x'], [k, ''])}).",
       "cval(1, b, c, d, -k)",
       ["Long division by ({poly([1, 'x'], [k, ''])}) ends with what is left after the x term.",
        "Quotient: {quad(1, b - k, c - (b - k) * k)}.", "Remainder: {d} − {br(k)} × {br(c - (b - k) * k)} = {answer}."],
       vars={"b": {"int": [-5, 5]}, "c": {"int": [-9, 9]}, "d": {"int": [-9, 9]}, "k": {"int": [1, 4]}},
       misc=[("plusk", "cval(1, b, c, d, k)", "Dividing by (x + {k}) matches x = {-k}, not x = {k}."),
             ("d", "d", "{d} is the last term, not the remainder: subtract {k} × the last quotient term from it.")],
       sources=SRC, where=["b != 0 && c != 0 && d != 0", "cval(1, b, c, d, -k) != 0", "cval(1, b, c, d, k) != cval(1, b, c, d, -k)"], signed=True),
   mcq("m4-12-gap", 3, "Divide {poly([1, 'x³'], [-c, ''])} by ({poly([1, 'x'], [-k, ''])}).",
       "{quad(1, k, k * k)}, remainder {k ^ 3 - c}",
       [("{quad(1, k, k * k)}, remainder {-c}", "rem"), ("{quad(1, 0, 0)}, remainder {k * 0 - c}", "nogap"), ("{quad(1, -k, k * k)}, remainder {k ^ 3 - c}", "sign")],
       ["Write {poly([1, 'x³'], [-c, ''])} as x³ + {0}x² + {0}x − {c}.",
        "x³ ÷ x = x²: subtract x²({poly([1, 'x'], [-k, ''])}) to leave {mono(k, 'x²')}; then {mono(k, 'x')}: leave {mono(k * k, 'x')}; then {k * k}: leave {k ^ 3} − {c}.",
        "So the answer is {answer}."],
       vars={"k": {"int": [2, 4]}, "c": {"int": [1, 70]}},
       misc=[("rem", "The {0}x² and {0}x terms still get filled: the last subtraction leaves {k ^ 3} − {c} = {k ^ 3 - c}."),
             ("nogap", "Without zero terms the columns slip. Write x³ + {0}x² + {0}x − {c} first."),
             ("sign", "x² × ({poly([1, 'x'], [-k, ''])}) = x³ − {mono(k, 'x²')}; subtracting it from x³ + {0}x² leaves +{mono(k, 'x²')}.")],
       sources=SRC, where=["c != k ^ 3", "k ^ 3 - c != -c"])],
  learn=learn(
    [goal("divide a polynomial by x − k or x + k by long division and state the quotient and the remainder.",
          "Form One long division of numbers and Lesson {2} (expanding brackets).",
          "Lesson {13} (the remainder and factor theorems) and factorising cubics."),
     ("The same steps as with numbers",
      "Divide {quad(1, 5, 7)} by x + {2}.\n"
      "• Divide the first term by x: x² ÷ x = x. Write x in the quotient.\n"
      "• Multiply the divisor by it: x(x + {2}) = {quad(1, 2, 0)}. Write it underneath.\n"
      "• Subtract: ({quad(1, 5, 7)}) − ({quad(1, 2, 0)}) = {mono(3, 'x')} + {7}.\n"
      "• Again: {mono(3, 'x')} ÷ x = {3}; {3}(x + {2}) = {mono(3, 'x')} + {6}; subtract: {1}.\n"
      "So the quotient is x + {3} and the remainder is {1}. Check: (x + {2})(x + {3}) + {1} = {quad(1, 5, 7)}."),
     ("Zero terms and checking",
      "If a power is missing, write it with {0} so that like terms stay in the same column: "
      "{poly([1, 'x³'], [-8, ''])} becomes x³ + {0}x² + {0}x − {8}.\n"
      "Dividing it by x − {2} gives {quad(1, 2, 4)} with remainder {0}, which matches the difference of cubes from Lesson {4}.\n"
      "Always check: divisor × quotient + remainder must give back the original polynomial.")],
    key_words=[("polynomial", "a sum of terms in powers of x, such as {cubic(1, -2, 0, 5)}"),
               ("quotient", "the result of the division"),
               ("remainder", "what is left at the end; zero if the divisor goes exactly"),
               ("degree", "the highest power of x")],
    examples=["({quad(1, 7, 10)}) ÷ (x + {2}) = x + {5}", "({quad(1, 1, -4)}) ÷ (x − {2}) = x + {3}, remainder {2}"],
    mistake=("x² × (x − {2}) = x³ − {2}", "x² × (x − {2}) = x³ − {mono(2, 'x²')}",
             "Multiply the whole divisor by the new term: x² × x and x² × {br(-2)}. Each term gets a power of x.")))

# ---------------------------------------------------------------- 13. Factor theorem and remainder theorem
L.lesson(D, S, 13, ("m4-13", "Use the remainder theorem and the factor theorem"), [12],
  "Remainder theorem: when f(x) is divided by (x − k), the remainder is f(k).\n"
  "Dividing by (x + k) means x − (−k), so the remainder is f(−k).\n"
  "Factor theorem: (x − k) is a factor of f(x) exactly when f(k) = 0.\n"
  "Example: f(x) = x³ − 7x + 6. f(1) = 1 − 7 + 6 = 0, so (x − 1) is a factor. f(3) = 27 − 21 + 6 = 12, so dividing by (x − 3) leaves 12.\n"
  "Unknown coefficients: if (x − 2) is a factor, put f(2) = 0 and solve for the unknown.",
  worked({"a": 1, "b": 0, "c": -7, "d": 6, "k": 3},
         "Find the remainder when f(x) = {cubic(a, b, c, d)} is divided by ({poly([1, 'x'], [-k, ''])}).",
         ["By the remainder theorem the remainder is f({k}).",
          "f({k}) = {k}³ + {br(c)} × {k} + {d}.",
          "= {k ^ 3} + {br(c * k)} + {d}."],
         "{cval(a, b, c, d, k)}",
         checks=["cval(a, b, c, d, k) == 12"]),
  [card("c4m13-1", "The remainder on dividing f(x) by (x − k) is f(k): no long division needed.",
        ["f(x) = {quad(1, 3, -1)}, divisor (x − {2}): remainder f({2}) = {4} + {6} − {1} = {9}"], "m4-13-rem"),
   card("c4m13-2", "If f(k) = {0}, then (x − k) is a factor of f(x).",
        ["f(x) = {cubic(1, 0, -7, 6)}: f({1}) = {0}, so (x − {1}) is a factor"], "m4-13-factor"),
   card("c4m13-3", "For a divisor (x + k), put x = −k.",
        ["f(x) = {quad(1, 3, -1)}, divisor (x + {2}): remainder f({-2}) = {4} − {6} − {1} = {-3}"], "m4-13-plus")],
  [num("m4-13-rem", 1, "Find the remainder when f(x) = {cubic(1, b, c, d)} is divided by ({poly([1, 'x'], [-k, ''])}).",
       "cval(1, b, c, d, k)",
       ["Remainder theorem: the remainder is f({k}).", "f({k}) = {k ^ 3} + {br(b * k * k)} + {br(c * k)} + {br(d)}.", "= {answer}."],
       vars={"b": {"int": [-5, 5]}, "c": {"int": [-9, 9]}, "d": {"int": [-9, 9]}, "k": {"int": [1, 3]}},
       misc=[("neg", "cval(1, b, c, d, -k)", "For (x − {k}) put x = {k}, not {-k}."),
             ("d", "d", "Substitute x = {k} into every term, not just the last.")],
       sources=SRC, where=["b != 0 && c != 0 && d != 0", "cval(1, b, c, d, k) != 0", "cval(1, b, c, d, k) != cval(1, b, c, d, -k)"], signed=True),
   mcq("m4-13-factor", 1, "f(x) = {cubic(1, b, c, d)}. Is ({poly([1, 'x'], [-k, ''])}) a factor of f(x)?",
       "{cval(1, b, c, d, k) == 0 ? 'Yes, because f(' + k + ') = 0' : 'No, because f(' + k + ') = ' + fmt(cval(1, b, c, d, k))}",
       [("{cval(1, b, c, d, k) == 0 ? 'No, because f(' + k + ') = 0' : 'Yes, because f(' + k + ') = ' + fmt(cval(1, b, c, d, k))}", "rule"),
        ("{cval(1, b, c, d, -k) == 0 ? 'No, because f(' + fmt(-k) + ') = 0' : 'Yes, because f(' + fmt(-k) + ') = ' + fmt(cval(1, b, c, d, -k))}", "negk"),
        ("You cannot tell without long division", "const")],
       ["Factor theorem: (x − {k}) is a factor exactly when f({k}) = {0}.", "f({k}) = {cval(1, b, c, d, k)}.", "So the answer is: {answer}."],
       vars={"k": {"int": [1, 3]}, "z": {"pick": [0, 1]}, "pp": {"int": [-3, 3]}, "p": {"expr": "z == 0 ? k : pp"}, "q": {"int": [-4, 4]}, "r": {"int": [-5, 5]},
             "b": {"expr": E2}, "c": {"expr": E1}, "d": {"expr": f"{E0} + z * (k + 2)"}},
       misc=[("rule", "The rule is: a factor exactly when the value is {0}. Here f({k}) = {cval(1, b, c, d, k)}."),
             ("negk", "For (x − {k}) substitute x = {k}, not {-k}."),
             ("const", "The factor theorem tells you at once: work out f({k}) and see whether it is {0}.")],
       sources=SRC, where=["d != 0", "b != 0 && c != 0", "z == 0 || cval(1, b, c, d, k) != 0", "cval(1, b, c, d, -k) != 0 || z == 1"]),
   num("m4-13-plus", 2, "Find the remainder when f(x) = {cubic(1, b, c, d)} is divided by ({poly([1, 'x'], [k, ''])}).",
       "cval(1, b, c, d, -k)",
       ["(x + {k}) = (x − {br(-k)}), so the remainder is f({-k}).", "f({-k}) = {(-k) ^ 3} + {br(b * k * k)} + {br(-c * k)} + {br(d)}.", "= {answer}."],
       vars={"b": {"int": [-5, 5]}, "c": {"int": [-9, 9]}, "d": {"int": [-9, 9]}, "k": {"int": [1, 3]}},
       misc=[("plusk", "cval(1, b, c, d, k)", "For (x + {k}) put x = {-k}: x + {k} = {0} when x = {-k}."),
             ("cube", "cval(1, b, c, d, -k) + 2 * k ^ 3", "({-k})³ = {(-k) ^ 3}: an odd power of a negative number is negative.")],
       sources=SRC, where=["b != 0 && c != 0 && d != 0", "cval(1, b, c, d, -k) != 0", "cval(1, b, c, d, k) != cval(1, b, c, d, -k)"], signed=True),
   num("m4-13-unknown", 2, "({poly([1, 'x'], [-k, ''])}) is a factor of x³ + ax² {q - p * k > 0 ? '+' : '−'} {poly([abs(q - p * k), 'x'], [-q * k, ''])}. Find a.",
       "p - k",
       ["Factor theorem: f({k}) = {0}.", "{k ^ 3} + a × {k * k} + {br((q - p * k) * k)} + {br(-q * k)} = {0}.",
        "{mono(k * k, 'a')} = {-(k ^ 3) - (q - p * k) * k + q * k}, so a = {answer}."],
       vars={"k": {"int": [1, 3]}, "p": {"int": [-5, 5]}, "q": {"int": [-6, 6]}},
       misc=[("negk", "(-(-k) ^ 3 + (q - p * k) * k + q * k) / (k * k)", "Substitute x = {k}, not {-k}.", "(-(-k) ^ 3 + (q - p * k) * k + q * k) % (k * k) == 0"),
             ("noa", "-(k ^ 3) - (q - p * k) * k + q * k", "Divide by {k * k}, the coefficient of a.")],
       sources=SRC, where=["q != 0", "q - p * k != 0", "p - k != 0", "k != 1 || p - k != -(k ^ 3) - (q - p * k) * k + q * k"], signed=True),
   num("m4-13-two", 3, "f(x) = x³ + ax + b. (x + {2}) is a factor of f(x), and the remainder on dividing f(x) by (x − {1}) is {9 + 3 * a}. Find a.",
       "a",
       ["f({-2}) = {0}: {-8} − {2}a + b = {0}, so b = {8} + {2}a.", "f({1}) = {9 + 3 * a}: {1} + a + b = {9 + 3 * a}.",
        "Substitute b: {1} + a + {8} + {2}a = {9 + 3 * a}, so {3}a = {3 * a} and a = {answer}."],
       vars={"a": {"int": [-6, 6]}},
       misc=[("b", "8 + 2 * a", "{8 + 2 * a} is b. The question asks for a."),
             ("sign", "-a", "f({-2}) uses x = {-2}: ({-2})³ = {-8} and a × {br(-2)} = −{2}a.")],
       sources=SRC, where=["a != 0", "8 + 2 * a != a"], signed=True)],
  learn=learn(
    [goal("find a remainder without dividing, decide whether (x − k) is a factor, and find an unknown coefficient.",
          "Lesson {12} (dividing a polynomial by x − k).",
          "Lesson {14} (factorising cubics) and Lesson {15} (solving cubic equations)."),
     ("Why the remainder is f(k)",
      "Long division gives f(x) = (x − k) × quotient + remainder.\n"
      "Put x = k: the bracket (x − k) becomes {0}, so f(k) = {0} × quotient + remainder = remainder.\n"
      "So to find the remainder when f(x) = {cubic(1, 0, -7, 6)} is divided by x − {3}, just work out f({3}) = {27} − {21} + {6} = {12}.\n"
      "For a divisor x + {2}, think of it as x − ({-2}): the remainder is f({-2})."),
     ("The factor theorem",
      "If the remainder is {0}, the divisor goes exactly: it is a factor.\n"
      "• f(x) = {cubic(1, 0, -7, 6)}: f({1}) = {1} − {7} + {6} = {0}, so x − {1} is a factor.\n"
      "• f({2}) = {8} − {14} + {6} = {0}, so x − {2} is a factor too.\n"
      "Finding an unknown: if x − {2} is a factor of x³ + ax − {6}, then f({2}) = {8} + {2}a − {6} = {0}, so a = {-1}.")],
    key_words=[("remainder theorem", "the remainder on dividing f(x) by (x − k) is f(k)"),
               ("factor theorem", "(x − k) is a factor of f(x) exactly when f(k) = {0}"),
               ("f(k)", "the value of f(x) when x = k")],
    examples=["f(x) = {quad(1, -4, 7)}: remainder on ÷ (x − {1}) is f({1}) = {4}", "f(x) = {cubic(1, 0, 0, -27)}: f({3}) = {0}, so (x − {3}) is a factor"],
    mistake=("remainder on ÷ (x + {2}) is f({2})", "remainder on ÷ (x + {2}) is f({-2})",
             "x + {2} = {0} when x = {-2}. Use the value that makes the divisor zero.")))

# ---------------------------------------------------------------- 14. Factorising polynomials of degree 3
L.lesson(D, S, 14, ("m4-14", "Factorise cubic polynomials using the factor theorem"), [13, 5],
  "To factorise a cubic f(x):\n"
  "1. Find one root k by trial: try the factors of the number term (±1, ±2, …) until f(k) = 0.\n"
  "2. Then (x − k) is a factor. Divide f(x) by (x − k) to get a quadratic.\n"
  "3. Factorise the quadratic.\n"
  "Example: x³ − 2x² − 5x + 6. f(1) = 0, so (x − 1) is a factor; x³ − 2x² − 5x + 6 = (x − 1)(x² − x − 6) = (x − 1)(x − 3)(x + 2).\n"
  "Check by expanding, or by checking that f(3) = 0 and f(−2) = 0.",
  worked({"p": 1, "q": 3, "r": -2},
         "Factorise f(x) = {cubic(1, -(p + q + r), p * q + p * r + q * r, -p * q * r)}.",
         ["Try factors of {-p * q * r}: f({p}) = {cval(1, -(p + q + r), p * q + p * r + q * r, -p * q * r, p)}, so (x − {p}) is a factor.",
          "Divide by (x − {p}): the quotient is {quad(1, -(q + r), q * r)}.",
          "Factorise the quadratic: {quad(1, -(q + r), q * r)} = {lin2(1, -q, 1, -r)}."],
         "({poly([1, 'x'], [-p, ''])}){lin2(1, -q, 1, -r)}",
         checks=["cval(1, -(p + q + r), p * q + p * r + q * r, -p * q * r, p) == 0"]),
  [card("c4m14-1", "Try the factors of the number term until f(k) = {0}: that gives a first factor (x − k).",
        ["f(x) = {cubic(1, -2, -5, 6)}: f({1}) = {1} − {2} − {5} + {6} = {0}"], "m4-14-try"),
   card("c4m14-2", "Divide by (x − k) to reduce the cubic to a quadratic.",
        ["{cubic(1, -2, -5, 6)} = (x − {1})({quad(1, -1, -6)})"], "m4-14-quot"),
   card("c4m14-3", "Factorise the quadratic to finish.",
        ["(x − {1})({quad(1, -1, -6)}) = (x − {1}){lin2(1, -3, 1, 2)}"], "m4-14-full")],
  [mcq("m4-14-try", 1, "f(x) = {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")}. Which of these makes f(x) = {0}?",
       "x = {p}",
       [("x = {-p}", "neg"), ("x = {w1}", "w"), ("x = {w2}", "w2")],
       ["f({p}) = {cval(1, " + E2 + ", " + E1 + ", " + E0 + ", p)}.", "So the answer is {answer}."],
       vars={"p": {"int": [-4, 4]}, "q": {"int": [-4, 4]}, "r": {"int": [-4, 4]}, "w1": {"int": [-5, 5]}, "w2": {"int": [-5, 5]}},
       misc=[("neg", "f({-p}) = {cval(1, " + E2 + ", " + E1 + ", " + E0 + ", -p)}, not {0}."),
             ("w", "f({w1}) = {cval(1, " + E2 + ", " + E1 + ", " + E0 + ", w1)}, not {0}."),
             ("w2", "f({w2}) = {cval(1, " + E2 + ", " + E1 + ", " + E0 + ", w2)}, not {0}.")],
       sources=SRC, where=["p != 0 && q != 0 && r != 0", "p != q && p != r && q != r", "-p != q && -p != r",
                           "w1 != p && w1 != q && w1 != r && w1 != -p", "w2 != p && w2 != q && w2 != r && w2 != -p && w2 != w1",
                           f"{E2} != 0 && {E1} != 0"]),
   num("m4-14-quot", 1, "({poly([1, 'x'], [-p, ''])}) is a factor of {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")}. Then the cubic = ({poly([1, 'x'], [-p, ''])})(x² + Bx + C). Find C.",
       "q * r",
       ["Compare number terms: {br(-p)} × C = {" + E0 + "}.", "So C = {" + E0 + "} ÷ {br(-p)} = {answer}."],
       vars={"p": {"int": [-4, 4]}, "q": {"int": [-4, 4]}, "r": {"int": [-4, 4]}},
       misc=[("const", E0, "C times {br(-p)} gives {" + E0 + "}: divide by {br(-p)}."),
             ("sign", "-q * r", "{br(-p)} × C = {" + E0 + "}, so C = {q * r}. Check the signs.")],
       sources=SRC, where=["p != 0 && q != 0 && r != 0", "p != q && p != r && q != r", "q * r != " + E0, f"{E2} != 0"], signed=True),
   mcq("m4-14-full", 2, "Factorise completely {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")}.",
       "({poly([1, 'x'], [-p, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])})",
       [("({poly([1, 'x'], [p, ''])})({poly([1, 'x'], [q, ''])})({poly([1, 'x'], [r, ''])})", "sign"),
        ("({poly([1, 'x'], [-p, ''])})({quad(1, -(q + r), q * r)})", "stop"),
        ("({poly([1, 'x'], [-p, ''])})({poly([1, 'x'], [q, ''])})({poly([1, 'x'], [r, ''])})", "half")],
       ["f({p}) = {0}, so ({poly([1, 'x'], [-p, ''])}) is a factor; dividing gives {quad(1, -(q + r), q * r)}.",
        "{quad(1, -(q + r), q * r)} = ({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])}).", "So the answer is {answer}."],
       vars={"p": {"int": [-4, 4]}, "q": {"int": [-4, 4]}, "r": {"int": [-4, 4]}},
       misc=[("sign", "A root k gives the factor (x − k): the signs in the brackets are opposite to the roots."),
             ("stop", "'Completely': the quadratic {quad(1, -(q + r), q * r)} still factorises."),
             ("half", "Expand the last two brackets: their product has the wrong middle sign.")],
       sources=SRC, where=["p != 0 && q != 0 && r != 0", "p < q && q < r", "-q != r", f"{E2} != 0 && {E1} != 0", "q + r != 0"]),
   num("m4-14-largest", 2, "Factorise {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")} and give the largest value of x that makes it zero.",
       "max(p, max(q, r))",
       ["Find a root by trial, divide, and factorise the quadratic: ({poly([1, 'x'], [-p, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])}).",
        "The values that make it zero are {p}, {q} and {r}.", "The largest is {answer}."],
       vars={"p": {"int": [-5, 5]}, "q": {"int": [-5, 5]}, "r": {"int": [-5, 5]}},
       misc=[("sign", "max(-p, max(-q, -r))", "(x − k) is zero when x = k: the signs of the roots are opposite to the numbers in the brackets.")],
       sources=SRC, where=["p != 0 && q != 0 && r != 0", "p != q && p != r && q != r", f"{E2} != 0 && {E1} != 0", "max(-p, max(-q, -r)) != max(p, max(q, r))"], signed=True),
   mcq("m4-14-two", 3, "Factorise completely {cubic(2, -(1 + 2 * (q + r)), q + r + 2 * q * r, -q * r)}.",
       "({poly([2, 'x'], [-1, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])})",
       [("({poly([1, 'x'], [-2, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])})", "two"),
        ("({poly([2, 'x'], [1, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])})", "sign"),
        ("({poly([1, 'x'], [-q, ''])})({quad(2, -(1 + 2 * r), r)})", "stop")],
       ["Try factors: f({q}) = {0}, so ({poly([1, 'x'], [-q, ''])}) is a factor; f({r}) = {0} too.",
        "Dividing by both leaves a linear factor with {mono(2, 'x')}: f({frac(1, 2)}) = {0}, so ({poly([2, 'x'], [-1, ''])}) is a factor.",
        "So the answer is {answer}."],
       vars={"q": {"int": [-4, 4]}, "r": {"int": [-4, 4]}},
       misc=[("two", "Check x = {2}: f({2}) = {cval(2, -(1 + 2 * (q + r)), q + r + 2 * q * r, -q * r, 2)}, not {0}. The root is {frac(1, 2)}."),
             ("sign", "({poly([2, 'x'], [1, ''])}) is zero at x = {frac(-1, 2)}, but f({frac(-1, 2)}) is not {0}."),
             ("stop", "'Completely': {quad(2, -(1 + 2 * r), r)} = ({poly([2, 'x'], [-1, ''])})({poly([1, 'x'], [-r, ''])}).")],
       sources=SRC, where=["q != 0 && r != 0", "q < r", "q * r != 0", "cval(2, -(1 + 2 * (q + r)), q + r + 2 * q * r, -q * r, 2) != 0", "q + r + 2 * q * r != 0"])],
  learn=learn(
    [goal("factorise a cubic completely by finding one root with the factor theorem, dividing, and factorising the quadratic.",
          "Lesson {13} (factor theorem), Lesson {12} (division) and Lesson {5} (trinomials).",
          "Lesson {15} (solving cubic equations) and sketching cubic graphs."),
     ("Finding the first factor",
      "A cubic such as f(x) = {cubic(1, -2, -5, 6)} has no common factor and no grouping. Use the factor theorem.\n"
      "If (x − k) is a factor with whole numbers, then k divides the number term {6}. So try {1}, {-1}, {2}, {-2}, {3}, {-3}, …\n"
      "• f({1}) = {1} − {2} − {5} + {6} = {0}. Found: (x − {1}) is a factor.\n"
      "Stop at the first value that gives {0}."),
     ("Dividing and finishing",
      "Divide f(x) by (x − {1}) (long division or by matching terms): {cubic(1, -2, -5, 6)} = (x − {1})({quad(1, -1, -6)}).\n"
      "Now factorise the quadratic as in Lesson {5}: {quad(1, -1, -6)} = {lin2(1, -3, 1, 2)}.\n"
      "So f(x) = (x − {1})(x − {3})(x + {2}).\n"
      "Check with the factor theorem: f({3}) = {27} − {18} − {15} + {6} = {0} and f({-2}) = {-8} − {8} + {10} + {6} = {0}.")],
    key_words=[("cubic", "a polynomial of degree {3}, such as {cubic(1, -2, -5, 6)}"),
               ("trial", "trying values one by one until one works"),
               ("factorise completely", "go on until every factor is linear or cannot be split")],
    examples=["{cubic(1, -6, 11, -6)} = (x − {1})(x − {2})(x − {3})", "{cubic(1, 0, -7, 6)} = (x − {1})(x − {2})(x + {3})"],
    mistake=("f({2}) = {0}, so (x + {2}) is a factor", "f({2}) = {0}, so (x − {2}) is a factor",
             "x − {2} is zero when x = {2}. The factor has the opposite sign to the root.")))

# ---------------------------------------------------------------- 15. Solving cubic equations
L.lesson(D, S, 15, ("m4-15", "Solve cubic equations"), [14, 7],
  "To solve a cubic equation f(x) = 0:\n"
  "1. Make one side 0.\n2. Factorise f(x) completely (Lesson 14).\n3. Set each factor equal to 0.\n"
  "A cubic equation has at most three real roots.\n"
  "Example: x³ − 2x² − 5x + 6 = 0 → (x − 1)(x − 3)(x + 2) = 0 → x = 1, 3 or −2.\n"
  "If x is a common factor, take it out; never divide by x: x³ = 4x → x(x − 2)(x + 2) = 0 → x = 0, 2 or −2.\n"
  "If the quadratic factor has a negative discriminant, it gives no real roots, and the cubic has only one.",
  worked({"p": 1, "q": 3, "r": -2},
         "Solve {cubic(1, -(p + q + r), p * q + p * r + q * r, -p * q * r)} = {0}.",
         ["f({p}) = {0}, so (x − {p}) is a factor.",
          "Divide: f(x) = (x − {p})({quad(1, -(q + r), q * r)}) = (x − {p}){lin2(1, -q, 1, -r)}.",
          "Each factor can be {0}: x − {p} = {0}, x − {q} = {0} or x + {-r} = {0}."],
         "x = {p}, x = {q} or x = {r}",
         checks=["cval(1, -(p + q + r), p * q + p * r + q * r, -p * q * r, r) == 0"]),
  [card("c4m15-1", "When a cubic is written as three factors equal to {0}, each factor gives a root.",
        ["(x − {1})(x − {3})(x + {2}) = {0} → x = {1}, {3} or {-2}"], "m4-15-roots"),
   card("c4m15-2", "Take out x as a common factor instead of dividing by x.",
        ["x³ = {mono(4, 'x')} → x(x² − {4}) = {0} → x = {0}, {2} or {-2}"], "m4-15-x"),
   card("c4m15-3", "If the quadratic factor has b² − {4}ac < {0}, it has no real roots.",
        ["(x − {2})({quad(1, 1, 3)}) = {0}: {1} − {12} < {0}, so only x = {2}"], "m4-15-one")],
  [num("m4-15-roots", 1, "Solve ({poly([1, 'x'], [-p, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])}) = {0}. Give the smallest root.",
       "min(p, min(q, r))",
       ["Each bracket can be {0}: x = {p}, x = {q} or x = {r}.", "The smallest is {answer}."],
       vars={"p": {"int": [-6, 6]}, "q": {"int": [-6, 6]}, "r": {"int": [-6, 6]}},
       misc=[("sign", "min(-p, min(-q, -r))", "x − {br(p)} = {0} gives x = {p}: the root has the opposite sign to the number in the bracket."),
             ("large", "max(p, max(q, r))", "That is the largest root. The smallest is {min(p, min(q, r))}.")],
       sources=SRC, where=["p != q && q != r && p != r", "p != 0 && q != 0 && r != 0", "min(-p, min(-q, -r)) != min(p, min(q, r))"], signed=True),
   mcq("m4-15-x", 1, "Solve x³ = {mono(k * k, 'x')}.",
       "x = {0}, {k} or {-k}",
       [("x = {k} or {-k}", "divide"), ("x = {k}", "one"), ("x = {0} or {k * k}", "noroot")],
       ["Make one side {0}: x³ − {mono(k * k, 'x')} = {0}.", "Factorise: x(x² − {k * k}) = x(x − {k})(x + {k}) = {0}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 9]}},
       misc=[("divide", "Dividing by x loses the root x = {0}. Take x out as a factor instead."),
             ("one", "x² = {k * k} has two roots, {k} and {-k}, and x = {0} is a root too."),
             ("noroot", "x² = {k * k} gives x = ±{k}: take the square root.")],
       sources=SRC),
   num("m4-15-solve", 2, "Solve {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")} = {0}. Give the largest root.",
       "max(p, max(q, r))",
       ["Try factors of {" + E0 + "} to find one root, divide, and factorise the quadratic.",
        "({poly([1, 'x'], [-p, ''])})({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])}) = {0}.", "The roots are {p}, {q}, {r}; the largest is {answer}."],
       vars={"p": {"int": [-5, 5]}, "q": {"int": [-5, 5]}, "r": {"int": [-5, 5]}},
       misc=[("sign", "max(-p, max(-q, -r))", "The roots have the opposite signs to the numbers in the brackets.")],
       sources=SRC, where=["p != q && q != r && p != r", "p != 0 && q != 0 && r != 0", f"{E2} != 0 && {E1} != 0", "max(-p, max(-q, -r)) != max(p, max(q, r))"], signed=True),
   num("m4-15-other", 2, "x = {p} is a root of {cubic(1, " + E2 + ", " + E1 + ", " + E0 + ")} = {0}. Find the other two roots and give the smaller one.",
       "min(q, r)",
       ["({poly([1, 'x'], [-p, ''])}) is a factor. Dividing gives {quad(1, -(q + r), q * r)}.", "{quad(1, -(q + r), q * r)} = ({poly([1, 'x'], [-q, ''])})({poly([1, 'x'], [-r, ''])}) = {0}.",
        "The other roots are {q} and {r}; the smaller is {answer}."],
       vars={"p": {"int": [-5, 5]}, "q": {"int": [-5, 5]}, "r": {"int": [-5, 5]}},
       misc=[("sign", "min(-q, -r)", "The roots are opposite in sign to the numbers in the brackets."),
             ("p", "p", "x = {p} is the root you were given. The question asks for one of the other two.")],
       sources=SRC, where=["p != q && q != r && p != r", "p != 0 && q != 0 && r != 0", f"{E2} != 0", "min(-q, -r) != min(q, r)", "p < min(q, r) || p > min(q, r)"], signed=True),
   mcq("m4-15-one", 3, "Solve ({poly([1, 'x'], [-p, ''])})({quad(1, b, c)}) = {0}.",
       "x = {p} only",
       [("x = {p}, and two more roots from the quadratic", "more"), ("x = {-p} only", "sign"), ("There are no real roots", "none")],
       ["x − {br(p)} = {0} gives x = {p}.", "For {quad(1, b, c)}: b² − {4}ac = {b * b} − {4 * c} = {b * b - 4 * c} < {0}, so it has no real roots.", "So the answer is {answer}."],
       vars={"p": {"int": [-6, 6]}, "b": {"int": [-5, 5]}, "c": {"int": [2, 12]}},
       misc=[("more", "Check the quadratic: b² − {4}ac = {b * b - 4 * c} is negative, so it has no real roots."),
             ("sign", "x − {br(p)} = {0} gives x = {p}, not {-p}."),
             ("none", "The bracket x − {br(p)} still gives the root x = {p}.")],
       sources=SRC, where=["p != 0", "b * b - 4 * c < 0", "b != 0"])],
  learn=learn(
    [goal("solve a cubic equation by factorising, find all its real roots, and say when there is only one.",
          "Lesson {14} (factorising cubics) and Lesson {7} (solving by factorisation).",
          "drawing cubic graphs, where the roots are the points on the x-axis."),
     ("Three factors, three roots",
      "Once a cubic equation is factorised, the rule from Lesson {7} still works: if a product is {0}, a factor is {0}.\n"
      "Solve {cubic(1, -2, -5, 6)} = {0}.\n"
      "• f({1}) = {0}, so (x − {1}) is a factor; dividing gives {quad(1, -1, -6)} = (x − {3})(x + {2}).\n"
      "• (x − {1})(x − {3})(x + {2}) = {0}, so x = {1}, x = {3} or x = {-2}.\n"
      "Take x out first if every term has an x: x³ − {mono(9, 'x')} = x(x − {3})(x + {3}) = {0} gives x = {0}, {3}, {-3}."),
     ("Fewer than three roots",
      "Sometimes the quadratic factor does not factorise. Check its discriminant.\n"
      "• (x − {2})({quad(1, 1, 3)}) = {0}: for the quadratic, b² − {4}ac = {1} − {12} = {-11}, negative.\n"
      "• So it has no real roots, and the only solution is x = {2}.\n"
      "If the discriminant is positive but not a square number, use the formula (Lesson {10}) for the last two roots.")],
    key_words=[("cubic equation", "an equation whose highest power is x³"),
               ("real root", "a root that is an ordinary number on the number line"),
               ("discriminant", "b² − {4}ac; negative means no real roots")],
    examples=["x(x − {4})(x + {1}) = {0} → x = {0}, {4} or {-1}", "{cubic(1, 0, -4, 0)} = {0} → x = {0}, {2} or {-2}"],
    mistake=("x³ = {mono(9, 'x')} → x² = {9} → x = ±{3}", "x(x² − {9}) = {0} → x = {0}, {3} or {-3}",
             "Dividing by x throws away x = {0}. Take x out as a common factor instead.")))
