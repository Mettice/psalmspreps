"""Form 4 Maths, Term 1, rows 26-35: surds, indices and exponential equations, logarithms, matrices, approximations,
errors and bounds, standard form. Rows 33 and 34 split the sheet's "significant figures, absolute error, relative
error, | percentage error, max and min values" (a parser split). Run: python tools/authoring/form4/maths_numbers.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import goal, not_half

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRCS, SRCI, SRCM, SRCA = ["surds"], ["indices-logs"], ["matrices"], ["approximation"]

SQF = [2, 3, 5, 6, 7, 10, 11]

# ---------------------------------------------------------------- 26. Surds
L.lesson(D, S, 26, ("m4-26", "Simplify surds, rationalise denominators and bound an irrational number"), [],
  "A surd is a root that is not a whole number, such as √2 or 3√5. Leave it exact unless a decimal is asked for.\n"
  "• Simplify: take out the largest square factor. √72 = √(36 × 2) = 6√2.\n"
  "• Like surds add like terms: 3√2 + 5√2 = 8√2. √8 + √18 = 2√2 + 3√2 = 5√2.\n"
  "• √a × √b = √(ab); √a × √a = a.\n"
  "• Rationalise a denominator: 6/√3 = 6√3/3 = 2√3. For 1/(√5 − 2) multiply top and bottom by √5 + 2: (√5 + 2)/(5 − 4) = √5 + 2.\n"
  "• Bounds: 36 < 40 < 49, so 6 < √40 < 7.",
  worked({"k": 6, "m": 2},
         "Simplify √{k * k * m}.",
         ["Look for the largest square number that divides {k * k * m}: {k * k}.",
          "√{k * k * m} = √({k * k} × {m}) = √{k * k} × √{m}.",
          "√{k * k} = {k}."],
         "{surd(k * k * m)}",
         checks=["k * k * m == 72"]),
  [card("c4m26-1", "Take out the largest square factor: √(a²b) = a√b.",
        ["√{50} = √({25} × {2}) = {surd(50)}"], "m4-26-simp"),
   card("c4m26-2", "Like surds can be added: they work like like terms.",
        ["{surd(8)} + {surd(18)} = {surd(2, 5)}"], "m4-26-add"),
   card("c4m26-3", "To rationalise a/√b, multiply top and bottom by √b.",
        ["{6}/√{3} = {6}√{3}/{3} = {surd(3, 2)}"], "m4-26-rat")],
  [mcq("m4-26-simp", 1, "Simplify √{k * k * m}.",
       "{surd(k * k * m)}",
       [("{k * k}√{m}", "noroot"), ("{m}√{k}", "swap"), ("{surd(m, k * m)}", "times")],
       ["√{k * k * m} = √({k * k} × {m}) = √{k * k} × √{m}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 7]}, "m": {"pick": SQF}},
       misc=[("noroot", "Take the square root of {k * k}: it is {k}, not {k * k}."),
             ("swap", "{k * k} is the square factor, so {k} comes out and {m} stays under the root."),
             ("times", "Only the square root of the square factor comes out: {k}, not {k * m}.")],
       sources=SRCS, where=["k != m"]),
   num("m4-26-bound", 1, "√{n} lies between two consecutive whole numbers. What is the smaller one?",
       "sqrtFloor(n)",
       ["{sqrtFloor(n) * sqrtFloor(n)} < {n} < {(sqrtFloor(n) + 1) * (sqrtFloor(n) + 1)}.", "So {sqrtFloor(n)} < √{n} < {sqrtFloor(n) + 1}.", "The smaller is {answer}."],
       vars={"n": {"int": [10, 150]}},
       misc=[("half", "floor(n / 2)", "√{n} is not half of {n}: find the squares on each side of {n}."),
             ("upper", "sqrtFloor(n) + 1", "That is the larger one.")],
       sources=SRCS, where=["!isPerfectSquare(n)"]),
   mcq("m4-26-add", 2, "Simplify √{a * a * m} + √{b * b * m}.",
       "{surd(m, a + b)}",
       [("√{a * a * m + b * b * m}", "addunder"), ("{surd(2 * m, a + b)}", "double"), ("{surd(m, a * b)}", "mult")],
       ["√{a * a * m} = {surd(a * a * m)} and √{b * b * m} = {surd(b * b * m)}.", "Like surds: {a} + {b} = {a + b} lots of √{m}.", "So the answer is {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [2, 6]}, "m": {"pick": [2, 3, 5, 6, 7]}},
       misc=[("addunder", "√x + √y is not √(x + y). Simplify each surd, then add."),
             ("double", "Adding √{m} to √{m} gives {2}√{m}, not √{2 * m}."),
             ("mult", "Add the coefficients, do not multiply: {a} + {b} = {a + b}.")],
       sources=SRCS, where=["a != b", "a * b != a + b"]),
   mcq("m4-26-rat", 2, "Rationalise the denominator of {j * b}/√{b}.",
       "{surd(b, j)}",
       [("{surd(b, j * b)}", "nodiv"), ("{j}/√{b}", "half"), ("{j * b}", "drop")],
       ["Multiply top and bottom by √{b}: {j * b}√{b}/{b}.", "{j * b} ÷ {b} = {j}.", "So the answer is {answer}."],
       vars={"j": {"int": [2, 6]}, "b": {"pick": [2, 3, 5, 6, 7]}},
       misc=[("nodiv", "After multiplying, the bottom is √{b} × √{b} = {b}: divide {j * b} by it."),
             ("half", "The denominator still has a root. Multiply top and bottom by √{b}."),
             ("drop", "√{b} × √{b} = {b}, and {j * b}√{b} ÷ {b} still has √{b}.")],
       sources=SRCS, where=["j != b"]),
   mcq("m4-26-conj", 3, "Rationalise {1}/(√{a} − {b}).",
       "{a - b * b == 1 ? '√' + a + ' + ' + b : '(√' + a + ' + ' + b + ')/' + fmt(a - b * b)}",
       [("{a - b * b == 1 ? '√' + a + ' − ' + b : '(√' + a + ' − ' + b + ')/' + fmt(a - b * b)}", "sign"),
        ("{'(√' + a + ' + ' + b + ')/' + fmt(a + b * b)}", "plus"),
        ("{'(√' + a + ' + ' + b + ')/' + fmt(a - b)}", "nosq")],
       ["Multiply top and bottom by √{a} + {b}.", "Bottom: (√{a} − {b})(√{a} + {b}) = {a} − {b * b} = {a - b * b}.", "So the answer is {answer}."],
       vars={"a": {"pick": [2, 3, 5, 6, 7, 10, 11, 13, 15]}, "b": {"int": [1, 3]}},
       misc=[("sign", "Multiply by the conjugate √{a} + {b}: the sign changes."),
             ("plus", "(√{a} − {b})(√{a} + {b}) = {a} − {b}², a difference of two squares."),
             ("nosq", "The second term is squared too: {b}² = {b * b}.")],
       sources=SRCS, where=["a - b * b != 0", "a - b * b != a - b", "a - b * b != a + b * b"])],
  learn=learn(
    [goal("simplify and add surds, rationalise denominators (including √a − b) and place a root between two whole numbers.",
          "Form Three square roots and Lesson {3} (the difference of two squares).",
          "exact answers in trigonometry, the quadratic formula and Form Five surd equations."),
     ("Simplifying and adding",
      "√{72} is not a whole number, but it can be simplified. Look for the largest square factor: {72} = {36} × {2}.\n"
      "√{72} = √{36} × √{2} = {surd(72)}.\n"
      "Surds with the same root are like terms: {surd(8)} + {surd(18)} = {surd(2, 2)} + {surd(2, 3)} = {surd(2, 5)}.\n"
      "But √{2} + √{3} cannot be combined, and √{9} + √{16} = {7}, not √{25}.\n"
      "Bounds: {36} < {40} < {49}, so {6} < √{40} < {7}."),
     ("Rationalising",
      "A root in the denominator is usually removed.\n"
      "• {6}/√{3}: multiply top and bottom by √{3}: {6}√{3}/{3} = {surd(3, 2)}.\n"
      "• {1}/(√{5} − {2}): multiply by the conjugate √{5} + {2}. The bottom becomes {5} − {4} = {1} (a difference of two squares), "
      "so the answer is √{5} + {2}.\n"
      "Multiplying top and bottom by the same thing does not change the value, only its form.")],
    key_words=[("surd", "an exact root that is not a whole number, such as √{2}"),
               ("rationalise", "rewrite with no root in the denominator"),
               ("conjugate", "the same two terms with the middle sign changed: √{5} + {2} for √{5} − {2}")],
    examples=["√{48} = {surd(48)}", "{surd(5, 3)} − √{5} = {surd(5, 2)}", "{10}/√{5} = {surd(5, 2)}"],
    mistake=("√{9} + √{16} = √{25} = {5}", "√{9} + √{16} = {3} + {4} = {7}",
             "Roots do not add under one root sign. Simplify each first.")))

# ---------------------------------------------------------------- 27. Laws of indices and exponential equations
L.lesson(D, S, 27, ("m4-27", "Use the laws of indices and solve simple exponential equations"), [],
  "Laws of indices: aᵐ × aⁿ = aᵐ⁺ⁿ; aᵐ ÷ aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ; a⁰ = 1; a⁻ⁿ = 1/aⁿ; a^(1/n) is the nth root.\n"
  "An exponential equation has the unknown in the index, such as 2ˣ = 32.\n"
  "Method: write both sides as powers of the same base, then the indices are equal.\n"
  "• 2ˣ = 32 = 2⁵, so x = 5.\n• 3ˣ⁺¹ = 81 = 3⁴, so x + 1 = 4 and x = 3.\n"
  "• 4ˣ = 8: 4 = 2², 8 = 2³, so 2²ˣ = 2³ and x = 3/2.\n• 9ˣ = 1/27: 3²ˣ = 3⁻³, so x = −3/2.",
  worked({"p": 2, "q": 3},
         "Solve {2 ^ p}ˣ = {2 ^ q}.",
         ["Write both sides as powers of {2}: {2 ^ p} = {2}{sup(p)} and {2 ^ q} = {2}{sup(q)}.",
          "So ({2}{sup(p)})ˣ = {2}{sup(q)}, that is {2}{sup('2x')} = {2}{sup(q)}.",
          "The indices are equal: {p}x = {q}."],
         "x = {frac(q, p)}",
         checks=["2 ^ p == 4", "2 ^ q == 8"]),
  [card("c4m27-1", "Multiplying powers of the same base adds the indices; dividing subtracts them.",
        ["{2}{sup(5)} × {2}{sup(3)} ÷ {2}{sup(4)} = {2}{sup(4)}"], "m4-27-laws"),
   card("c4m27-2", "If both sides are powers of the same base, the indices are equal.",
        ["{3}ˣ = {81} = {3}{sup(4)}, so x = {4}"], "m4-27-solve"),
   card("c4m27-3", "Change both sides to a common base first.",
        ["{4}ˣ = {8}: {2}{sup('2x')} = {2}{sup(3)}, so x = {frac(3, 2)}"], "m4-27-common")],
  [num("m4-27-laws", 1, "Write {b}{sup(m)} × {b}{sup(n)} ÷ {b}{sup(p)} as a single power of {b}. What is the index?",
       "m + n - p",
       ["Multiplying adds the indices: {m} + {n} = {m + n}.", "Dividing subtracts: {m + n} − {p} = {answer}."],
       vars={"b": {"pick": [2, 3, 5, 7]}, "m": {"int": [2, 9]}, "n": {"int": [2, 9]}, "p": {"int": [1, 8]}},
       misc=[("mult", "m * n - p", "Multiplying powers adds the indices; it does not multiply them."),
             ("div", "(m + n) / p", "Dividing powers subtracts the indices.", "(m + n) % p == 0")],
       sources=SRCI, where=["m + n - p != 0", "m * n - p != m + n - p"], signed=True),
   num("m4-27-solve", 1, "Solve {b}ˣ = {b ^ k}.",
       "k",
       ["Write {b ^ k} as a power of {b}: {b ^ k} = {b}{sup(k)}.", "So x = {answer}."],
       vars={"b": {"pick": [2, 3, 5]}, "k": {"int": [2, 7]}},
       misc=[("div", "b ^ k / b", "{b ^ k} ÷ {b} is not the index. Count how many {b}s multiply to give {b ^ k}.")],
       sources=SRCI, where=["b ^ k <= 3125"]),
   num("m4-27-shift", 2, "Solve {b}{sup('x + ' + d)} = {b ^ k}.",
       "k - d",
       ["{b ^ k} = {b}{sup(k)}, so x + {d} = {k}.", "x = {answer}."],
       vars={"b": {"pick": [2, 3, 5]}, "k": {"int": [3, 7]}, "d": {"int": [1, 3]}},
       misc=[("nod", "k", "The index is x + {d}, so x + {d} = {k}: subtract {d}."),
             ("add", "k + d", "Subtract {d} from {k}, do not add it.")],
       sources=SRCI, where=["b ^ k <= 3125", "k - d != 0"], signed=True),
   mcq("m4-27-common", 2, "Solve {B}ˣ = {C}.",
       "x = {frac(q, p)}",
       [("x = {frac(p, q)}", "flip"), ("x = {frac(C, B)}", "divide"), ("x = {q - p}", "sub")],
       ["{B} = {g}{sup(p)} and {C} = {g}{sup(q)}.", "So {g}{sup(p + 'x')} = {g}{sup(q)}, and {p}x = {q}.", "So the answer is {answer}."],
       vars={"P": {"pick": [[2, 2, 3], [2, 3, 2], [2, 2, 5], [3, 2, 3], [2, 4, 3], [5, 2, 3], [3, 3, 2], [2, 3, 4]]},
             "g": {"expr": "P[0]"}, "p": {"expr": "P[1]"}, "q": {"expr": "P[2]"}, "B": {"expr": "g ^ p"}, "C": {"expr": "g ^ q"}},
       misc=[("flip", "{p}x = {q} gives x = {q} ÷ {p}, not {p} ÷ {q}."),
             ("divide", "Write both sides as powers of {g} first; dividing {C} by {B} does not give the index."),
             ("sub", "The index on the left is {p}x, a product: divide, do not subtract.")],
       sources=SRCI, where=["frac(C, B) != frac(q, p)", "q - p != q / p"]),
   mcq("m4-27-neg", 3, "Solve {g ^ p}ˣ = {1}/{g ^ q}.",
       "x = {frac(-q, p)}",
       [("x = {frac(q, p)}", "pos"), ("x = {frac(-p, q)}", "flip"), ("x = {-q}", "nop")],
       ["{1}/{g ^ q} = {g}{sup(-q)}, and {g ^ p} = {g}{sup(p)}.", "So {g}{sup(p + 'x')} = {g}{sup(-q)}: {p}x = {-q}.", "So the answer is {answer}."],
       vars={"P": {"pick": [[3, 2, 3], [2, 2, 3], [2, 3, 2], [5, 2, 1], [2, 2, 5], [3, 2, 1], [2, 3, 4]]},
             "g": {"expr": "P[0]"}, "p": {"expr": "P[1]"}, "q": {"expr": "P[2]"}},
       misc=[("pos", "A reciprocal gives a negative index: {1}/{g ^ q} = {g}{sup(-q)}."),
             ("flip", "{p}x = {-q} gives x = {-q} ÷ {p}."),
             ("nop", "Write {g ^ p} as {g}{sup(p)} too: then {p}x = {-q}.")],
       sources=SRCI, where=["p != q", "frac(-q, p) != -q"])],
  learn=learn(
    [goal("use the laws of indices and solve exponential equations by writing both sides as powers of the same base.",
          "Form Three laws of indices (zero, negative and fractional indices).",
          "Lesson {28} (logarithms), which solves exponential equations when the bases cannot be matched."),
     ("The laws, revised",
      "For any base a:\n• aᵐ × aⁿ = a{sup('m+n')}  • aᵐ ÷ aⁿ = a{sup('m−n')}  • (aᵐ)ⁿ = a{sup('mn')}\n"
      "• a{sup(0)} = {1}  • a{sup(-1)} = {1}/a, a{sup(-2)} = {1}/a²  • a{sup('1/2')} = √a\n"
      "Example: {2}{sup(5)} × {2}{sup(3)} ÷ {2}{sup(4)} = {2}{sup(4)} = {16}.\n"
      "These work only for the same base: {2}{sup(3)} × {3}{sup(2)} cannot be combined into one power."),
     ("Exponential equations",
      "When x is in the index, make the bases match, then the indices must be equal.\n"
      "• {3}{sup('x+1')} = {81}: {81} = {3}{sup(4)}, so x + {1} = {4}, x = {3}.\n"
      "• {4}ˣ = {8}: {4} = {2}{sup(2)} and {8} = {2}{sup(3)}, so {2}{sup('2x')} = {2}{sup(3)}, {2}x = {3}, x = {frac(3, 2)}.\n"
      "• {9}ˣ = {1}/{27}: {3}{sup('2x')} = {3}{sup(-3)}, so x = {frac(-3, 2)}.\n"
      "Check by putting the answer back: {4}{sup('3/2')} = (√{4})³ = {8}.")],
    key_words=[("index (power)", "the small raised number: the {3} in {2}{sup(3)}"),
               ("base", "the number being raised to the power"),
               ("exponential equation", "an equation with the unknown in the index")],
    examples=["{5}ˣ = {125} → x = {3}", "{8}ˣ = {4} → {2}{sup('3x')} = {2}{sup(2)} → x = {frac(2, 3)}", "{2}ˣ = {frac(1, 8)} → x = {-3}"],
    mistake=("{4}ˣ = {8} → x = {2}", "{4}ˣ = {8} → x = {frac(3, 2)}",
             "{4}{sup(2)} = {16}, not {8}. Write both as powers of {2}: {2}{sup('2x')} = {2}{sup(3)}.")))

# ---------------------------------------------------------------- 28. Logarithms and logarithmic equations
L.lesson(D, S, 28, ("m4-28", "Use the laws of logarithms and solve logarithmic and exponential equations"), [27],
  "log_b x = y means bʸ = x. So log_2 8 = 3 because 2³ = 8.\n"
  "Laws: log(xy) = log x + log y; log(x/y) = log x − log y; log xⁿ = n log x; log_b b = 1; log_b 1 = 0.\n"
  "Logarithmic equations: rewrite as a power. log_3(x + 1) = 2 → x + 1 = 3² → x = 8.\n"
  "Exponential equations with unmatched bases: take logs. 2ˣ = 7 → x log 2 = log 7 → x = log 7 ÷ log 2 ≈ 2.81.\n"
  "Note: log x + log y is NOT log(x + y).",
  worked({"b": 2, "n": 7},
         "Solve {b}ˣ = {n}, giving x to {2} decimal places.",
         ["{n} is not a power of {b}, so take logs of both sides: log({b}ˣ) = log {n}.",
          "Power law: x log {b} = log {n}.",
          "x = log {n} ÷ log {b} = {roundTo(log10(n), 0.0001)} ÷ {roundTo(log10(b), 0.0001)}."],
         "x ≈ {roundTo(log10(n) / log10(b), 0.01)}",
         checks=["roundTo(log10(n) / log10(b), 0.01) == 2.81"]),
  [card("c4m28-1", "log_b x asks: b to what power gives x?",
        ["log₂ {32} = {5}, because {2}{sup(5)} = {32}"], "m4-28-value"),
   card("c4m28-2", "Adding logs multiplies the numbers inside; subtracting divides them.",
        ["log₆ {4} + log₆ {9} = log₆ {36} = {2}"], "m4-28-law"),
   card("c4m28-3", "Take logs to bring an unknown index down: log(bˣ) = x log b.",
        ["{3}ˣ = {20} → x = log {20} ÷ log {3} ≈ {roundTo(log10(20) / log10(3), 0.01)}"], "m4-28-exp")],
  [num("m4-28-value", 1, "Find log{sub(b)} {b ^ k}.",
       "k",
       ["log{sub(b)} {b ^ k} asks: {b} to what power gives {b ^ k}?", "{b}{sup(k)} = {b ^ k}, so the answer is {answer}."],
       vars={"b": {"pick": [2, 3, 4, 5, 10]}, "k": {"int": [2, 5]}},
       misc=[("div", "b ^ k / b", "The log is the index, not {b ^ k} ÷ {b}.")],
       sources=SRCI, where=["b ^ k <= 100000"]),
   num("m4-28-law", 1, "Find log{sub(b)} {x} + log{sub(b)} {y}.",
       "k",
       ["log{sub(b)} {x} + log{sub(b)} {y} = log{sub(b)} ({x} × {y}) = log{sub(b)} {x * y}.", "{x * y} = {b}{sup(k)}, so the answer is {answer}."],
       vars={"b": {"pick": [2, 3, 6, 10]}, "k": {"int": [2, 4]}, "x": {"pick": [2, 3, 4, 5, 8, 9, 20, 25, 50]}, "y": {"expr": "b ^ k / x"}},
       sources=SRCI, where=["y == round(y)", "y > 1"]),
   num("m4-28-eq", 2, "Solve log{sub(b)}(x + {d}) = {k}.",
       "b ^ k - d",
       ["Rewrite as a power: x + {d} = {b}{sup(k)} = {b ^ k}.", "x = {b ^ k} − {d} = {answer}."],
       vars={"b": {"pick": [2, 3, 5, 10]}, "k": {"int": [2, 4]}, "d": {"int": [1, 9]}},
       misc=[("times", "b * k - d", "{b}{sup(k)} means {b} to the power {k}, not {b} × {k}."),
             ("plus", "b ^ k + d", "Subtract {d} from both sides.")],
       sources=SRCI, where=["b ^ k <= 10000", "b * k != b ^ k", "b ^ k > d"]),
   num("m4-28-two", 2, "Solve log{sub(b)} x + log{sub(b)} {c} = {k}.",
       "b ^ k / c",
       ["Combine: log{sub(b)} ({c}x) = {k}.", "{c}x = {b}{sup(k)} = {b ^ k}.", "x = {b ^ k} ÷ {c} = {answer}."],
       vars={"b": {"pick": [2, 3, 10]}, "k": {"int": [2, 4]}, "c": {"pick": [2, 4, 5, 9, 25]}},
       misc=[("sub", "b ^ k - c", "log x + log {c} = log({c}x): divide by {c}, do not subtract."),
             ("power", "b ^ (k - 1)", "Rewrite the whole equation first: {c}x = {b ^ k}.", "c != b")],
       sources=SRCI, where=["(b ^ k) % c == 0", "b ^ k / c > 1", "b ^ k <= 10000"]),
   num("m4-28-exp", 3, "Solve {b}ˣ = {n}, giving x to {2} decimal places.",
       "roundTo(log10(n) / log10(b), 0.01)",
       ["Take logs: x log {b} = log {n}.", "x = log {n} ÷ log {b} = {roundTo(log10(n), 0.0001)} ÷ {roundTo(log10(b), 0.0001)}.", "x ≈ {answer}."],
       vars={"b": {"pick": [2, 3, 5, 7]}, "n": {"int": [5, 90]}},
       misc=[("div", "roundTo(n / b, 0.01)", "Divide the logs, not the numbers: log {n} ÷ log {b}."),
             ("sub", "roundTo(log10(n) - log10(b), 0.01)", "x log {b} = log {n}: divide by log {b}; log {n} − log {b} is log({n}/{b}).")],
       sources=SRCI, where=["abs(logb(b, n) - round(logb(b, n))) > 0.01", not_half("log10(n) / log10(b)")])],
  learn=learn(
    [goal("use the laws of logarithms, solve log equations by rewriting them as powers, and solve bˣ = n by taking logs.",
          "Form Three logarithms and Lesson {27} (exponential equations).",
          "growth and decay problems (interest, populations) and Form Five logarithmic functions."),
     ("Laws, revised",
      "log_b x = y means b{sup('y')} = x. For example log₂ {8} = {3} and log₁₀ {1000} = {3}.\n"
      "• log x + log y = log(xy)  • log x − log y = log(x/y)  • log xⁿ = n log x\n"
      "• log_b b = {1} and log_b {1} = {0}.\n"
      "Example: log₆ {4} + log₆ {9} = log₆ {36} = {2}.\n"
      "Warning: log x + log y is not log(x + y), and log x ÷ log y is not log(x − y)."),
     ("Solving",
      "• A log equation: rewrite as a power. log₃(x + {1}) = {2} → x + {1} = {3}{sup(2)} = {9} → x = {8}.\n"
      "• Combine logs first: log₂ x + log₂ {4} = {5} → log₂ {4}x = {5} → {4}x = {32} → x = {8}.\n"
      "• An exponential equation whose sides are not powers of the same base: take logs.\n"
      "{2}ˣ = {7} → x log {2} = log {7} → x = {roundTo(log10(7), 0.0001)} ÷ {roundTo(log10(2), 0.0001)} ≈ {roundTo(log10(7) / log10(2), 0.01)}.\n"
      "Check: {2}{sup(2)} = {4} < {7} < {8} = {2}{sup(3)}, so x is between {2} and {3}.")],
    key_words=[("logarithm", "the index: log_b x is the power of b that gives x"),
               ("base", "b in log_b x; log means log₁₀ on a calculator"),
               ("take logs", "apply log to both sides of an equation")],
    examples=["log₅ {125} = {3}", "log {2} + log {50} = log {100} = {2}", "{5}ˣ = {30} → x ≈ {roundTo(log10(30) / log10(5), 0.01)}"],
    mistake=("log {2} + log {3} = log {5}", "log {2} + log {3} = log {6}",
             "Adding logs multiplies the numbers inside: {2} × {3} = {6}.")))

# ---------------------------------------------------------------- 29. Operations with matrices
M2 = {"a": {"int": [-4, 5]}, "b": {"int": [-4, 5]}, "c": {"int": [-4, 5]}, "d": {"int": [-4, 5]},
      "e": {"int": [-4, 5]}, "f": {"int": [-4, 5]}, "g": {"int": [-4, 5]}, "h": {"int": [-4, 5]}}
AB = "matFig([['A', [[a, b], [c, d]]], ['B', [[e, f], [g, h]]]])"

L.lesson(D, S, 29, ("m4-29", "Multiply matrices, including non-square ones, and use matrix equations"), [],
  "Matrices can be multiplied when the number of columns of the first equals the number of rows of the second: "
  "(m × n)(n × p) gives an m × p matrix.\n"
  "Each element of AB = (row of A) · (column of B): multiply in pairs and add.\n"
  "Example: (1 2; 3 4)(5; 6) = (1×5 + 2×6; 3×5 + 4×6) = (17; 39).\n"
  "Matrix multiplication is not commutative: usually AB ≠ BA.\n"
  "A² means A × A. The identity I = (1 0; 0 1) has AI = IA = A.\n"
  "In a matrix equation, equal matrices have equal elements in the same places.",
  worked({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6},
         "Find ({a}  {b} ; {c}  {d}) × ({e} ; {f}).",
         ["The first matrix is {2} × {2}, the second {2} × {1}: the product is {2} × {1}.",
          "Top: row ({a}, {b}) · column ({e}, {f}) = {a} × {e} + {b} × {f} = {a * e + b * f}.",
          "Bottom: row ({c}, {d}) · column = {c} × {e} + {d} × {f} = {c * e + d * f}."],
         "({a * e + b * f} ; {c * e + d * f})",
         checks=["a * e + b * f == 17"]),
  [card("c4m29-1", "A product exists only when columns of the first = rows of the second; the answer has the outside sizes.",
        ["({2} × {3})({3} × {1}) gives {2} × {1}; ({2} × {3})({2} × {3}) does not exist"], "m4-29-order"),
   card("c4m29-2", "Each element of AB is a row of A times a column of B, multiplied in pairs and added.",
        ["row ({1}, {2}), column ({5}, {6}): {1} × {5} + {2} × {6} = {17}"], "m4-29-elem"),
   card("c4m29-3", "Usually AB ≠ BA: the order matters.",
        ["({1}  {1} ; {0}  {1})({1}  {0} ; {1}  {1}) = ({2}  {1} ; {1}  {1}), but the other order gives ({1}  {1} ; {1}  {2})"], "m4-29-order2")],
  [mcq("m4-29-order", 1, "A is a {m} × {n} matrix and B is a {n} × {p} matrix. What is the order of AB?",
       "{m} × {p}",
       [("{n} × {n}", "inner"), ("{p} × {m}", "swap"), ("AB does not exist", "none")],
       ["Columns of A ({n}) = rows of B ({n}), so AB exists.", "Its order is the outside numbers: {m} × {p}."],
       vars={"m": {"int": [1, 4]}, "n": {"int": [1, 4]}, "p": {"int": [1, 4]}},
       misc=[("inner", "The matching inside numbers disappear: the answer has rows of A and columns of B."),
             ("swap", "Rows come from A ({m}), columns from B ({p})."),
             ("none", "A has {n} columns and B has {n} rows, so the product exists.")],
       sources=SRCM, where=["m != p", "n != m || n != p", "m != n || p != n"]),
   num("m4-29-elem", 1, "Find the element in row {i} and column {j} of AB.",
       "(i == 1 ? [a, b] : [c, d])[0] * (j == 1 ? e : f) + (i == 1 ? [a, b] : [c, d])[1] * (j == 1 ? g : h)",
       ["Row {i} of A is ({i == 1 ? a : c}, {i == 1 ? b : d}); column {j} of B is ({j == 1 ? e : f}, {j == 1 ? g : h}).",
        "{i == 1 ? a : c} × {br(j == 1 ? e : f)} + {i == 1 ? b : d} × {br(j == 1 ? g : h)} = {answer}."],
       vars={**M2, "i": {"int": [1, 2]}, "j": {"int": [1, 2]}}, figure=AB,
       misc=[("elementwise", "(i == 1 ? (j == 1 ? a * e : b * f) : (j == 1 ? c * g : d * h))", "Multiply a whole row by a whole column and add, not just one pair."),
             ("rowrow", "(i == 1 ? a * (j == 1 ? e : g) + b * (j == 1 ? f : h) : c * (j == 1 ? e : g) + d * (j == 1 ? f : h))", "Use a column of B, read downwards, not a row.")],
       sources=SRCM, where=["a * d - b * c != 0", "b != 0 && g != 0 && f != 0"], signed=True),
   mcq("m4-29-order2", 2, "Find AB.",
       "{matStr(matMul([[a, b], [c, d]], [[e, f], [g, h]]))}",
       [("{matStr(matMul([[e, f], [g, h]], [[a, b], [c, d]]))}", "ba"), ("{matStr([[a * e, b * f], [c * g, d * h]])}", "elem"), ("{matStr(matAdd([[a, b], [c, d]], [[e, f], [g, h]]))}", "add")],
       ["Top left: {a} × {br(e)} + {b} × {br(g)} = {a * e + b * g}; top right: {a} × {br(f)} + {b} × {br(h)} = {a * f + b * h}.",
        "Bottom: {c * e + d * g} and {c * f + d * h}.", "So the answer is {answer}."],
       vars=M2, figure=AB,
       misc=[("ba", "That is BA. The order matters: AB uses the rows of A."),
             ("elem", "Matrices are not multiplied element by element: row times column."),
             ("add", "That is A + B.")],
       sources=SRCM, where=["matStr(matMul([[a, b], [c, d]], [[e, f], [g, h]])) != matStr(matMul([[e, f], [g, h]], [[a, b], [c, d]]))", "b != 0 && c != 0 && f != 0 && g != 0"]),
   num("m4-29-square", 2, "A = ({a}  {b} ; {c}  {d}). Find the top-left element of A².",
       "a * a + b * c",
       ["A² = A × A. Top left: row ({a}, {b}) · column ({a}, {c}).", "{a} × {br(a)} + {b} × {br(c)} = {answer}."],
       vars={"a": {"int": [-5, 5]}, "b": {"int": [-5, 5]}, "c": {"int": [-5, 5]}, "d": {"int": [-5, 5]}},
       misc=[("sq", "a * a", "A² is not each element squared: top left is {a}² + {b} × {br(c)}."),
             ("bd", "a * a + b * d", "Use column {1} of A, ({a}, {c}), not ({b}, {d}).")],
       sources=SRCM, where=["b != 0 && c != 0", "b * c != b * d"], signed=True),
   num("m4-29-unknown", 3, "({a}  x ; {c}  {d}) × ({p} ; {q}) = ({a * p + x0 * q} ; {c * p + d * q}). Find x.",
       "x0",
       ["Top row: {a} × {p} + x × {q} = {a * p + x0 * q}.", "{q}x = {a * p + x0 * q} − {a * p} = {x0 * q}.", "x = {answer}."],
       vars={"a": {"int": [1, 5]}, "c": {"int": [-4, 4]}, "d": {"int": [-4, 4]}, "p": {"int": [1, 4]}, "q": {"int": [2, 5]}, "x0": {"int": [-6, 6]}},
       misc=[("nodiv", "x0 * q", "After {q}x = {x0 * q}, divide by {q}."),
             ("row2", "(c * p + d * q - a * p) / q", "x is in the top row: use the top element.", "(c * p + d * q - a * p) % q == 0")],
       sources=SRCM, where=["x0 != 0", "c != 0"], signed=True)],
  learn=learn(
    [goal("multiply matrices of any compatible orders, explain why AB ≠ BA, and find unknowns in matrix equations.",
          "Form Three matrices: addition, scalar multiples and {2} × {2} products.",
          "Lesson {30} (determinants and inverses) and Lesson {31} (solving simultaneous equations with matrices)."),
     ("When a product exists",
      "A {2} × {3} matrix has {2} rows and {3} columns. To multiply A by B, each row of A must meet a column of B of the same length.\n"
      "So: columns of A = rows of B. The answer takes the outside sizes:\n"
      "• ({2} × {3})({3} × {1}) → {2} × {1}.  • ({1} × {2})({2} × {2}) → {1} × {2}.  • ({2} × {3})({2} × {3}): not possible.\n"
      "Even when both AB and BA exist, they are usually different. Order matters."),
     ("Row times column",
      "({1}  {2} ; {3}  {4}) × ({5} ; {6}):\n"
      "• top: ({1}, {2}) · ({5}, {6}) = {1} × {5} + {2} × {6} = {17};\n• bottom: ({3}, {4}) · ({5}, {6}) = {15} + {24} = {39}.\n"
      "Answer ({17} ; {39}).\n"
      "Matrix equations: equal matrices have equal elements. If ({2}  x)({1} ; {2}) = ({8}), then {2} + {2}x = {8}, so x = {3}.")],
    key_words=[("order", "rows × columns, such as {2} × {3}"),
               ("compatible", "able to be multiplied: columns of the first = rows of the second"),
               ("identity matrix I", "({1}  {0} ; {0}  {1}); AI = IA = A")],
    examples=["({2}  {0} ; {1}  {3})({1} ; {4}) = ({2} ; {13})", "({1}  {2})({3} ; {4}) = ({11})"],
    mistake=("({1}  {2} ; {3}  {4})({5}  {6} ; {7}  {8}) = ({5}  {12} ; {21}  {32})", "row × column: ({19}  {22} ; {43}  {50})",
             "Matrices are not multiplied element by element. Each answer element is a row times a column.")))

# ---------------------------------------------------------------- 30. Determinant, adjugate, inverse
L.lesson(D, S, 30, ("m4-30", "Find the determinant, the adjugate and the inverse of a 2 × 2 matrix"), [29],
  "For A = (a b; c d):\n"
  "• Determinant: det A = ad − bc.\n"
  "• Adjugate (adjoint): adj A = (d −b; −c a): swap the main diagonal, change the signs of the other two.\n"
  "• Inverse: A⁻¹ = (1/det A) × adj A, if det A ≠ 0. Check: A A⁻¹ = I.\n"
  "• If det A = 0 the matrix is singular and has no inverse.\n"
  "Example: A = (3 1; 5 2): det = 6 − 5 = 1, A⁻¹ = (2 −1; −5 3).",
  worked({"a": 3, "b": 1, "c": 5, "d": 2},
         "Find the inverse of A = ({a}  {b} ; {c}  {d}).",
         ["det A = {a} × {d} − {b} × {c} = {a * d - b * c}.",
          "adj A: swap {a} and {d}, change the signs of {b} and {c}: ({d}  {-b} ; {-c}  {a}).",
          "A⁻¹ = ({1}/{a * d - b * c}) × adj A."],
         "A⁻¹ = ({d}  {-b} ; {-c}  {a})",
         checks=["a * d - b * c == 1"]),
  [card("c4m30-1", "det (a b; c d) = ad − bc: the main diagonal product minus the other.",
        ["det ({4}  {3} ; {2}  {5}) = {20} − {6} = {14}"], "m4-30-det"),
   card("c4m30-2", "adj (a b; c d) = (d −b; −c a).",
        ["adj ({4}  {3} ; {2}  {5}) = ({5}  {-3} ; {-2}  {4})"], "m4-30-adj"),
   card("c4m30-3", "A⁻¹ = ({1}/det A) × adj A; no inverse when det A = {0}.",
        ["({2}  {4} ; {1}  {2}): det = {4} − {4} = {0}, so it has no inverse"], "m4-30-sing")],
  [num("m4-30-det", 1, "Find the determinant of ({a}  {b} ; {c}  {d}).",
       "a * d - b * c",
       ["det = ad − bc = {a} × {br(d)} − {b} × {br(c)}.", "= {a * d} − {br(b * c)} = {answer}."],
       vars={"a": {"int": [-6, 6]}, "b": {"int": [-6, 6]}, "c": {"int": [-6, 6]}, "d": {"int": [-6, 6]}},
       misc=[("plus", "a * d + b * c", "Subtract bc: ad − bc."), ("cross", "b * c - a * d", "It is the main diagonal (ad) minus the other (bc), not the other way round."),
             ("rows", "a * b - c * d", "Multiply along the diagonals: a × d and b × c.")],
       sources=SRCM, where=["b != 0 && c != 0", "a * d - b * c != 0", "a * b - c * d != a * d - b * c"], signed=True),
   mcq("m4-30-adj", 1, "Find the adjugate of ({a}  {b} ; {c}  {d}).",
       "{matStr([[d, -b], [-c, a]])}",
       [("{matStr([[d, b], [c, a]])}", "nosign"), ("{matStr([[-a, b], [c, -d]])}", "wrong"), ("{matStr([[a, c], [b, d]])}", "trans")],
       ["Swap the main diagonal: {a} and {d}.", "Change the signs of the other two: {-b} and {-c}.", "So the answer is {answer}."],
       vars={"a": {"int": [-6, 6]}, "b": {"int": [-6, 6]}, "c": {"int": [-6, 6]}, "d": {"int": [-6, 6]}},
       misc=[("nosign", "The other two elements change sign."), ("wrong", "Swap a and d; change the signs of b and c."),
             ("trans", "That is the transpose (rows and columns swapped).")],
       sources=SRCM, where=["b != 0 && c != 0", "a != d", "b != c", "a != 0 && d != 0"]),
   num("m4-30-sing", 2, "Find k so that ({k}  {b} ; {c}  {d}) — that is (k  {b} ; {c}  {d}) — has no inverse.".replace("({k}  {b} ; {c}  {d}) — that is ", ""),
       "b * c / d",
       ["No inverse means det = {0}: k × {br(d)} − {b} × {br(c)} = {0}.", "{mono(d, 'k')} = {b * c}, so k = {answer}."],
       vars={"b": {"int": [-6, 6]}, "c": {"int": [-6, 6]}, "d": {"pick": [-3, -2, 2, 3, 4]}},
       misc=[("prod", "b * c", "Divide by {d}: {mono(d, 'k')} = {b * c}."), ("sign", "-b * c / d", "det = kd − bc = {0}, so kd = bc.")],
       sources=SRCM, where=["b != 0 && c != 0", "(b * c) % d == 0", "b * c / d != 0"], signed=True),
   mcq("m4-30-inv", 2, "Find the inverse of A = ({a}  {b} ; {c}  {d}).",
       "{(a * d - b * c) == 1 ? matStr([[d, -b], [-c, a]]) : '(' + 1 + '/' + fmt(a * d - b * c) + ') × ' + matStr([[d, -b], [-c, a]])}",
       [("{matStr([[d, -b], [-c, a]])}{(a * d - b * c) == 1 ? ' × ' + fmt(a * d - b * c + 1) : ''}", "nodet"),
        ("{(a * d - b * c) == 1 ? '' : '(' + 1 + '/' + fmt(a * d - b * c) + ') × '}{matStr([[a, -b], [-c, d]])}", "noswap"),
        ("{(a * d - b * c) == 1 ? '' : '(' + 1 + '/' + fmt(a * d - b * c) + ') × '}{matStr([[d, b], [c, a]])}", "nosign")],
       ["det A = {a * d} − {b * c} = {a * d - b * c}.", "adj A = {matStr([[d, -b], [-c, a]])}.", "A⁻¹ = ({1}/det A) × adj A. So the answer is {answer}."],
       vars={"a": {"int": [1, 6]}, "b": {"int": [1, 5]}, "c": {"int": [1, 5]}, "d": {"int": [1, 6]}},
       misc=[("nodet", "Divide by the determinant {a * d - b * c}."), ("noswap", "Swap a and d in the adjugate."), ("nosign", "Change the signs of b and c in the adjugate.")],
       sources=SRCM, where=["a * d - b * c > 0", "a != d", "a * d - b * c != 0"]),
   num("m4-30-prod", 3, "A = ({a}  {b} ; {c}  {d}) and B = ({e}  {f} ; {g}  {h}). Find det(AB) without working out AB.",
       "(a * d - b * c) * (e * h - f * g)",
       ["det(AB) = det A × det B.", "det A = {a * d - b * c}; det B = {e * h - f * g}.", "det(AB) = {answer}."],
       vars=M2,
       misc=[("sum", "(a * d - b * c) + (e * h - f * g)", "det(AB) = det A × det B: multiply, do not add.")],
       sources=SRCM, where=["a * d - b * c != 0 && e * h - f * g != 0", "abs((a * d - b * c) * (e * h - f * g)) <= 400", "(a * d - b * c) * (e * h - f * g) != (a * d - b * c) + (e * h - f * g)"], signed=True)],
  learn=learn(
    [goal("find the determinant, adjugate and inverse of a {2} × {2} matrix, and recognise a singular matrix.",
          "Form Three determinant and inverse, and Lesson {29} (matrix products).",
          "Lesson {31} (solving simultaneous equations) and transformations in Form Five."),
     ("Determinant and adjugate",
      "For A = (a  b ; c  d):\n"
      "• det A = ad − bc. For ({4}  {3} ; {2}  {5}): {20} − {6} = {14}.\n"
      "• adj A = (d  −b ; −c  a): swap the two on the main diagonal, change the signs of the other two.\n"
      "For ({4}  {3} ; {2}  {5}): adj = ({5}  {-3} ; {-2}  {4}).\n"
      "A × adj A = det A × I. That is why dividing by the determinant gives the inverse."),
     ("The inverse",
      "A⁻¹ = ({1}/det A) × adj A.\n"
      "• A = ({3}  {1} ; {5}  {2}): det = {1}, so A⁻¹ = ({2}  {-1} ; {-5}  {3}). Check: A A⁻¹ = ({1}  {0} ; {0}  {1}).\n"
      "• If det A = {0}, you cannot divide by it: A is singular and has no inverse. ({2}  {4} ; {1}  {2}) is singular.\n"
      "Useful: det(AB) = det A × det B, and (AB)⁻¹ = B⁻¹A⁻¹.")],
    key_words=[("determinant", "ad − bc for (a  b ; c  d)"), ("adjugate (adjoint)", "(d  −b ; −c  a)"),
               ("inverse", "A⁻¹ with A A⁻¹ = I"), ("singular", "determinant {0}; no inverse")],
    examples=["det ({2}  {1} ; {7}  {4}) = {1}; inverse ({4}  {-1} ; {-7}  {2})", "({6}  {3} ; {4}  {2}) is singular"],
    mistake=("det ({4}  {3} ; {2}  {5}) = {12} − {10}", "det = {4} × {5} − {3} × {2} = {14}",
             "Multiply along the diagonals: main diagonal a × d, other diagonal b × c.")))

# ---------------------------------------------------------------- 31. Solving simultaneous equations with matrices
SIM = {"a": {"int": [1, 5]}, "b": {"int": [-4, 4]}, "c": {"int": [-4, 4]}, "d": {"int": [1, 5]}, "x": {"int": [-5, 5]}, "y": {"int": [-5, 5]},
       "e": {"expr": "a * x + b * y"}, "f": {"expr": "c * x + d * y"}}
SIMW = ["a * d - b * c != 0", "abs(a * d - b * c) <= 12", "b != 0 && c != 0", "x != y"]
EQS = "{poly([a, 'x'], [b, 'y'])} = {e} and {poly([c, 'x'], [d, 'y'])} = {f}"

L.lesson(D, S, 31, ("m4-31", "Solve simultaneous linear equations using matrices"), [30],
  "The equations ax + by = e, cx + dy = f can be written as one matrix equation: (a b; c d)(x; y) = (e; f), or AX = B.\n"
  "If det A ≠ 0, multiply both sides on the left by A⁻¹: X = A⁻¹B.\n"
  "So (x; y) = (1/det A) × (d −b; −c a)(e; f), which gives x = (de − bf)/det A and y = (af − ce)/det A.\n"
  "Example: 2x + y = 7, x + y = 4: det = 1, (x; y) = (1 −1; −1 2)(7; 4) = (3; 1).\n"
  "If det A = 0 there is no unique solution: the lines are parallel or the same line.",
  worked({"a": 2, "b": 1, "c": 1, "d": 1, "x": 3, "y": 1},
         "Solve {poly([a, 'x'], [b, 'y'])} = {a * x + b * y} and {poly([c, 'x'], [d, 'y'])} = {c * x + d * y} using matrices.",
         ["Matrix form: ({a}  {b} ; {c}  {d})(x ; y) = ({a * x + b * y} ; {c * x + d * y}).",
          "det = {a * d} − {b * c} = {a * d - b * c}; inverse = ({d}  {-b} ; {-c}  {a}) (dividing by {a * d - b * c}).",
          "({d}  {-b} ; {-c}  {a})({a * x + b * y} ; {c * x + d * y}) = ({d * (a * x + b * y) - b * (c * x + d * y)} ; {-c * (a * x + b * y) + a * (c * x + d * y)})."],
         "x = {x}, y = {y}",
         checks=["a * d - b * c == 1"]),
  [card("c4m31-1", "Write the coefficients as a matrix A, the unknowns as (x ; y) and the right-hand sides as B.",
        ["{mono(2, 'x')} + y = {7}, x + y = {4} → ({2}  {1} ; {1}  {1})(x ; y) = ({7} ; {4})"], "m4-31-form"),
   card("c4m31-2", "X = A⁻¹B: the inverse undoes A.",
        ["({1}  {-1} ; {-1}  {2})({7} ; {4}) = ({3} ; {1}), so x = {3}, y = {1}"], "m4-31-x"),
   card("c4m31-3", "If det A = {0}, there is no unique solution.",
        ["x + {mono(2, 'y')} = {3}, {mono(2, 'x')} + {mono(4, 'y')} = {5}: det = {0}"], "m4-31-none")],
  [mcq("m4-31-form", 1, "Write " + EQS + " as a matrix equation.",
       "({a}  {b} ; {c}  {d})(x ; y) = ({e} ; {f})",
       [("({a}  {c} ; {b}  {d})(x ; y) = ({e} ; {f})", "trans"), ("({a}  {b} ; {c}  {d})(x ; y) = ({f} ; {e})", "swap"), ("({e}  {b} ; {f}  {d})(x ; y) = ({a} ; {c})", "const")],
       ["Each row of the matrix holds one equation's coefficients: ({a}, {b}) and ({c}, {d}).", "The right-hand sides make the column ({e} ; {f}).", "So the answer is {answer}."],
       vars=SIM,
       misc=[("trans", "Each row is one equation; the first row is ({a}, {b})."), ("swap", "The first equation's answer {e} goes in the first row."),
             ("const", "The numbers on the right go in the column on the right, not in the matrix.")],
       sources=SRCM, where=SIMW + ["b != c", "e != f"]),
   num("m4-31-det", 1, "For " + EQS + ", find the determinant of the matrix of coefficients.",
       "a * d - b * c",
       ["The matrix is ({a}  {b} ; {c}  {d}).", "det = {a} × {d} − {b} × {br(c)} = {answer}."],
       vars=SIM,
       misc=[("rhs", "a * f - c * e", "Use the coefficients of x and y only, not the right-hand sides."), ("plus", "a * d + b * c", "det = ad − bc.")],
       sources=SRCM, where=SIMW + ["a * f - c * e != a * d - b * c"], signed=True),
   num("m4-31-x", 2, "Solve " + EQS + " using matrices. What is x?",
       "x",
       ["det = {a * d - b * c}.", "x = (d × e − b × f) ÷ det = ({d} × {br(e)} − {b} × {br(f)}) ÷ {br(a * d - b * c)}.", "x = {answer}."],
       vars=SIM,
       misc=[("y", "y", "{y} is the value of y. x comes from the top row of A⁻¹B."), ("nodet", "d * e - b * f", "Divide by the determinant {a * d - b * c}.", "a * d - b * c != 1")],
       sources=SRCM, where=SIMW, signed=True),
   num("m4-31-y", 2, "Solve " + EQS + " using matrices. What is y?",
       "y",
       ["det = {a * d - b * c}.", "y = (a × f − c × e) ÷ det = ({a} × {br(f)} − {c} × {br(e)}) ÷ {br(a * d - b * c)}.", "y = {answer}."],
       vars=SIM,
       misc=[("x", "x", "{x} is the value of x. y comes from the bottom row of A⁻¹B."), ("sign", "-y", "Bottom row of the adjugate is (−c, a): −{c} × {e} + {a} × {f}.")],
       sources=SRCM, where=SIMW, signed=True),
   mcq("m4-31-none", 3, "What happens when you try to solve " + "{poly([a, 'x'], [b, 'y'])} = {e} and {poly([k * a, 'x'], [k * b, 'y'])} = {f2}" + " using matrices?",
       "det = {0}, so there is no inverse and no unique solution",
       [("det = {k}, so x = {e}", "det"), ("The inverse gives x = {0}, y = {0}", "zero"), ("There is exactly one solution", "one")],
       ["det = {a} × {k * b} − {b} × {k * a} = {0}.", "The second equation's left side is {k} times the first: the lines are parallel (or the same).", "So the answer is: {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [1, 4]}, "k": {"int": [2, 3]}, "e": {"int": [1, 9]}, "f2": {"int": [1, 20]}},
       misc=[("det", "Work it out: {a} × {k * b} − {b} × {k * a} = {0}."), ("zero", "A matrix with determinant {0} has no inverse."),
             ("one", "The lines have the same gradient, so they do not cross at exactly one point.")],
       sources=SRCM, where=["f2 != k * e"])],
  learn=learn(
    [goal("write a pair of simultaneous equations as AX = B and solve them with X = A⁻¹B, recognising when there is no unique solution.",
          "Lesson {30} (inverse matrices) and Form Three simultaneous equations.",
          "larger systems with matrices in further mathematics and transformation problems."),
     ("One matrix equation",
      "{mono(2, 'x')} + y = {7} and x + y = {4} have the same shape: numbers times x, numbers times y.\n"
      "Put the coefficients in a matrix A, the unknowns in X and the right-hand sides in B:\n"
      "({2}  {1} ; {1}  {1})(x ; y) = ({7} ; {4}).\n"
      "Multiply out the left to check: ({mono(2, 'x')} + y ; x + y). It matches the equations."),
     ("Solving with the inverse",
      "AX = B. Multiply both sides on the left by A⁻¹: A⁻¹AX = A⁻¹B, and A⁻¹A = I, so X = A⁻¹B.\n"
      "For our A: det = {2} − {1} = {1}, A⁻¹ = ({1}  {-1} ; {-1}  {2}).\n"
      "X = ({1}  {-1} ; {-1}  {2})({7} ; {4}) = ({7} − {4} ; {-7} + {8}) = ({3} ; {1}). So x = {3}, y = {1}.\n"
      "Check in both equations: {6} + {1} = {7} and {3} + {1} = {4}.\n"
      "If det A = {0}, A has no inverse: the equations describe parallel lines (no solution) or the same line (many).")],
    key_words=[("coefficient matrix", "the matrix of the numbers multiplying x and y"),
               ("A⁻¹B", "the inverse times the right-hand sides: the solution"),
               ("unique solution", "exactly one pair (x, y)")],
    examples=["x + y = {5}, x − y = {1} → x = {3}, y = {2}", "{mono(3, 'x')} + {mono(2, 'y')} = {12}, x + y = {5} → x = {2}, y = {3}"],
    mistake=("X = BA⁻¹", "X = A⁻¹B",
             "Matrix order matters: A⁻¹ goes on the left, where A was, so that A⁻¹A = I.")))

# ---------------------------------------------------------------- 32. Approximations
L.lesson(D, S, 32, ("m4-32", "Approximate numbers: place value, rounding, rounding up and down"), [],
  "The value of a digit depends on its place: in 3.4567 the 5 stands for 5 hundredths, 0.05.\n"
  "To round, look at the next digit: 5 or more, round up; 4 or less, keep.\n"
  "• 3.4567 to 1 decimal place: 3.5. To 2 decimal places: 3.46. To the nearest whole number: 3.\n"
  "• 4 682 to the nearest hundred: 4 700.\n"
  "In real problems you sometimes must round up (buses needed for 130 pupils, 50 per bus: 3) "
  "or down (full boxes of 12 from 130 eggs: 10), whatever the next digit is.\n"
  "A rounded value has bounds: 4.7 to 1 d.p. means 4.65 ≤ x < 4.75.",
  worked({"n": 130, "c": 50},
         "{n} pupils travel on buses that each carry {c}. How many buses are needed?",
         ["{n} ÷ {c} = {n / c}.", "{floor(n / c)} buses carry only {floor(n / c) * c} pupils; the others still need a seat.", "So round up."],
         "{floor((n + c - 1) / c)} buses",
         checks=["floor((n + c - 1) / c) == 3"]),
  [card("c4m32-1", "Rounding: look at the next digit. {5} or more, round up; less than {5}, keep.",
        ["{3.4567} to {1} d.p.: next digit {5}, so {3.5}"], "m4-32-dp"),
   card("c4m32-2", "In a problem, decide whether to round up or down from the meaning.",
        ["{130} pupils, {50} per bus: {3} buses (up). {130} eggs, boxes of {12}: {10} full boxes (down)"], "m4-32-context"),
   card("c4m32-3", "A rounded number stands for a range: half a unit either side.",
        ["{4.7} to {1} d.p.: from {4.65} up to (not including) {4.75}"], "m4-32-bounds")],
  [num("m4-32-place", 1, "What is the value of the digit {dig} in {fmt(x)}?",
       "dig / 10 ^ pos",
       ["{dig} is in the {pos == 1 ? 'tenths' : pos == 2 ? 'hundredths' : 'thousandths'} place.", "So it stands for {dig} ÷ {10 ^ pos} = {answer}."],
       vars={"w": {"int": [1, 9]}, "d1": {"int": [1, 9]}, "d2": {"int": [1, 9]}, "d3": {"int": [1, 9]}, "pos": {"int": [1, 3]},
             "x": {"expr": "dec(w + d1 / 10 + d2 / 100 + d3 / 1000)"}, "dig": {"expr": "pos == 1 ? d1 : pos == 2 ? d2 : d3"}},
       misc=[("face", "dig", "{dig} is not in the units place: it stands for {dig} ÷ {10 ^ pos}."),
             ("tens", "dig * 10 ^ pos", "Places after the point are tenths, hundredths, thousandths: divide, do not multiply.")],
       sources=SRCA, where=["d1 != d2 && d2 != d3 && d1 != d3", "dig != w"]),
   num("m4-32-dp", 1, "Round {fmt(x)} to {k} decimal place{k == 1 ? '' : 's'}.",
       "roundTo(x, 10 ^ -k)",
       ["Look at decimal place {k + 1}.", "It is {k == 1 ? d2 : d3}: {(k == 1 ? d2 : d3) >= 5 ? 'round up' : 'keep'}.", "{fmt(x)} ≈ {answer}."],
       vars={"w": {"int": [0, 30]}, "d1": {"int": [0, 9]}, "d2": {"int": [0, 9]}, "d3": {"int": [0, 9]}, "d4": {"int": [1, 9]}, "k": {"int": [1, 2]},
             "x": {"expr": "dec(w + d1 / 10 + d2 / 100 + d3 / 1000 + d4 / 10000)"}},
       misc=[("trunc", "floor(x * 10 ^ k) / 10 ^ k", "The next digit is {k == 1 ? d2 : d3}, so round up.", "(k == 1 ? d2 : d3) >= 5"),
             ("other", "roundTo(x, 10 ^ -(3 - k))", "Count the decimal places carefully: {k} place{k == 1 ? '' : 's'} after the point.")],
       sources=SRCA, where=["roundTo(x, 10 ^ -k) != floor(x * 10 ^ k) / 10 ^ k || (k == 1 ? d2 : d3) < 5"]),
   num("m4-32-hundred", 2, "Round {n} to the nearest {u}.",
       "roundTo(n, u)",
       ["Look at the digit after the {u == 10 ? 'tens' : u == 100 ? 'hundreds' : 'thousands'} place.", "{n} ≈ {answer}."],
       vars={"n": {"int": [1001, 98999]}, "u": {"pick": [10, 100, 1000]}},
       misc=[("down", "floor(n / u) * u", "The next digit is {floor(n / (u / 10)) % 10}: {floor(n / (u / 10)) % 10 >= 5 ? 'round up' : 'keep'}.", "floor(n / (u / 10)) % 10 >= 5"),
             ("drop", "floor(n / u)", "Keep the size of the number: write the zeros, {roundTo(n, u)}.")],
       sources=SRCA, where=["n % (u / 10) != 0", "floor(n / (u / 10)) % 10 != 5 || n % (u / 10) != 0"]),
   num("m4-32-context", 2, "{up ? n + ' people need transport in vans that carry ' + c + ' each. How many vans are needed?' : 'Mangoes are packed ' + c + ' to a crate. How many full crates can be made from ' + n + ' mangoes?'}",
       "up ? floor((n + c - 1) / c) : floor(n / c)",
       ["{n} ÷ {c} = {roundTo(n / c, 0.01)}.", "{up ? 'Everyone needs a seat, so round up' : 'Only full crates count, so round down'}.", "The answer is {answer}."],
       vars={"up": {"pick": [True, False]}, "c": {"int": [6, 20]}, "n": {"int": [40, 300]}},
       misc=[("near", "round(n / c)", "{up ? 'Rounding down leaves people behind' : 'A part-filled crate is not full'}: round {up ? 'up' : 'down'}.", "round(n / c) != (up ? floor((n + c - 1) / c) : floor(n / c))")],
       sources=SRCA, where=["n % c != 0", "round(n / c) == (up ? floor(n / c) : floor((n + c - 1) / c))"]),
   mcq("m4-32-bounds", 3, "A length is {fmt(x)} cm, correct to {1} decimal place. Which range contains the true length L?",
       "{fmt(dec(x - 0.05))} ≤ L < {fmt(dec(x + 0.05))}",
       [("{fmt(dec(x - 0.1))} ≤ L < {fmt(dec(x + 0.1))}", "unit"), ("{fmt(x)} ≤ L < {fmt(dec(x + 0.1))}", "up"), ("{fmt(dec(x - 0.5))} ≤ L < {fmt(dec(x + 0.5))}", "whole")],
       ["To {1} d.p. the unit is {0.1}; half of it is {0.05}.", "L is within {0.05} of {fmt(x)}.", "So the answer is {answer}."],
       vars={"w": {"int": [2, 30]}, "t": {"int": [1, 9]}, "x": {"expr": "dec(w + t / 10)"}},
       misc=[("unit", "Go half a unit each way: {0.05}, not {0.1}."), ("up", "Rounding works both ways: values just below {fmt(x)} also round to it."),
             ("whole", "The accuracy is {1} d.p., so the half-unit is {0.05}.")],
       sources=SRCA)],
  learn=learn(
    [goal("give the value of any digit, round to a number of decimal places or to the nearest {10}, {100}, {1000}, and decide when to round up or down.",
          "Form One place value and rounding.",
          "Lessons {33} and {34} (significant figures, errors and bounds) and every measured answer in science."),
     ("Place value and rounding",
      "In {3.4567}: {3} units, {4} tenths, {5} hundredths, {6} thousandths, {7} ten-thousandths. The {5} stands for {0.05}.\n"
      "To round, keep the digits you need and look at the next one:\n"
      "• {3.4567} to {1} d.p.: next digit {5} → {3.5}.\n• to {2} d.p.: next digit {6} → {3.46}.\n• {4682} to the nearest {100}: next digit {8} → {4700}.\n"
      "Keep the size: {4682} to the nearest {100} is {4700}, not {47}."),
     ("Up, down and bounds",
      "Sometimes the meaning decides, not the digit:\n"
      "• {130} pupils, {50} per bus: {130} ÷ {50} = {2.6}, but {2} buses leave pupils behind: {3} buses.\n"
      "• {130} eggs, boxes of {12}: {10.8}, but only {10} boxes are full.\n"
      "A rounded value stands for a range. {4.7} to {1} d.p. could be anything from {4.65} up to just below {4.75}: "
      "half a unit each way. These are its lower and upper bounds.")],
    key_words=[("decimal place (d.p.)", "a place after the point"), ("round up / round down", "go to the next value above / below"),
               ("bounds", "the smallest and largest values that round to a given number")],
    examples=["{12.749} to {1} d.p. = {12.7}", "{0.0386} to {2} d.p. = {0.04}", "{25} to the nearest {10} = {30}"],
    mistake=("{4682} to the nearest {100} = {47}", "{4682} to the nearest {100} = {4700}",
             "Rounding keeps the size of the number: fill the places with zeros.")))

# ---------------------------------------------------------------- 33. Significant figures, absolute and relative error
L.lesson(D, S, 33, ("m4-33", "Use significant figures, absolute error and relative error"), [32],
  "Significant figures count from the first non-zero digit. 0.004 507 to 2 s.f. is 0.0045; 38 260 to 2 s.f. is 38 000.\n"
  "Zeros between non-zero digits count (4 507 has 4 s.f.); leading zeros never count (0.004 has 1 s.f.); "
  "zeros at the end after a decimal point count (0.0450 has 3 s.f.).\n"
  "Absolute error = |measured value − true value|.\n"
  "Relative error = absolute error ÷ true value.\n"
  "For a measurement given to a unit, the maximum absolute error is half the unit: 3.4 cm to the nearest 0.1 cm has a maximum error of 0.05 cm.",
  worked({"t": 50, "m": 52},
         "A pupil measures a table as {m} cm; its true length is {t} cm. Find the absolute error and the relative error.",
         ["Absolute error = |{m} − {t}| = {abs(m - t)} cm.", "Relative error = {abs(m - t)} ÷ {t}."],
         "absolute error {abs(m - t)} cm; relative error {dec(abs(m - t) / t)}",
         checks=["dec(abs(m - t) / t) == 0.04"]),
  [card("c4m33-1", "Count significant figures from the first non-zero digit; then round as usual.",
        ["{0.004507} to {2} s.f. = {0.0045}; {38260} to {2} s.f. = {38000}"], "m4-33-sf"),
   card("c4m33-2", "Absolute error = |measured − true|.",
        ["measured {52} cm, true {50} cm: absolute error {2} cm"], "m4-33-abs"),
   card("c4m33-3", "Relative error = absolute error ÷ true value.",
        ["{2} ÷ {50} = {0.04}"], "m4-33-rel")],
  [num("m4-33-sf", 1, "Round {fmt(x)} to {k} significant figures.",
       "sigFig(x, k)",
       ["The first significant figure is the first non-zero digit.", "Keep {k} figures and look at the next: {fmt(x)} ≈ {answer}."],
       vars={"m": {"int": [1001, 9999]}, "e": {"int": [-5, 2]}, "k": {"int": [2, 3]}, "x": {"expr": "dec(m * 10 ^ e)"}},
       misc=[("dp", "roundTo(x, 10 ^ -k)", "Significant figures are not decimal places: start counting at the first non-zero digit.", "roundTo(x, 10 ^ -k) != sigFig(x, k)")],
       sources=SRCA, where=["m % 10 != 0", "x < 100000", "floor(m / 10 ^ (4 - k - 1)) % 10 != 5"]),
   num("m4-33-count", 1, "How many significant figures does {X.s} have?",
       "X.n",
       ["{X.y}", "So it has {answer}."],
       vars={"X": {"pick": [
           {"s": "0.004 50", "n": 3, "w": 2, "y": "Leading zeros do not count; the final zero after the point does: 4, 5, 0."},
           {"s": "4 507", "n": 4, "w": 3, "y": "Zeros between non-zero digits count: 4, 5, 0, 7."},
           {"s": "0.000 3", "n": 1, "w": 4, "y": "Leading zeros do not count: only the 3."},
           {"s": "12.0", "n": 3, "w": 2, "y": "A final zero after the point counts: 1, 2, 0."},
           {"s": "0.020 4", "n": 3, "w": 2, "y": "Leading zeros do not count; the zero between 2 and 4 does: 2, 0, 4."},
           {"s": "3.010", "n": 4, "w": 3, "y": "All four digits count: the middle and the final zeros both count."}]}},
       misc=[("count", "X.w", "Count from the first non-zero digit: zeros between digits count, and so do final zeros after the point; leading zeros never do.")],
       sources=SRCA),
   num("m4-33-abs", 2, "The true mass of a bag of rice is {t} kg. A trader's scale shows {fmt(m)} kg. What is the absolute error, in kg?",
       "dec(abs(m - t))",
       ["Absolute error = |{fmt(m)} − {t}|.", "= {answer} kg."],
       vars={"t": {"pick": [5, 10, 25, 50]}, "d": {"int": [-15, 15]}, "m": {"expr": "dec(t + d / 10)"}},
       misc=[("signed", "dec(m - t)", "Absolute error is a size: it is never negative.", "m < t"),
             ("rel", "dec(abs(m - t) / t)", "That is the relative error. The absolute error is the difference itself.")],
       sources=SRCA, where=["d != 0"], unit="kg"),
   num("m4-33-rel", 2, "A length of {t} m is measured as {m} m. Find the relative error as a decimal.",
       "dec(abs(m - t) / t)",
       ["Absolute error = |{m} − {t}| = {abs(m - t)} m.", "Relative error = {abs(m - t)} ÷ {t} = {answer}."],
       vars={"t": {"pick": [20, 25, 40, 50, 80, 100, 200]}, "d": {"int": [-8, 8]}, "m": {"expr": "t + d"}},
       misc=[("meas", "dec(abs(m - t) / m)", "Divide by the true value {t}, not the measured value."),
             ("abs", "abs(m - t)", "That is the absolute error. Divide it by the true value.")],
       sources=SRCA, where=["d != 0", "(abs(d) * 1000) % t == 0"]),
   num("m4-33-max", 3, "A length is measured as {fmt(x)} cm, correct to the nearest {fmt(u)} cm. What is the maximum absolute error, in cm?",
       "dec(u / 2)",
       ["The true length is within half a unit of {fmt(x)}.", "Half of {fmt(u)} = {answer} cm."],
       vars={"u": {"pick": [0.1, 0.5, 1, 2, 10]}, "q": {"int": [3, 60]}, "x": {"expr": "dec(q * u)"}},
       misc=[("unit", "u", "The measurement could be wrong by up to half a unit either way, not a whole unit."),
             ("tenth", "dec(x / 10)", "The error depends on the unit of accuracy, {fmt(u)} cm, not on the size of the measurement.")],
       sources=SRCA, unit="cm")],
  learn=learn(
    [goal("round to significant figures, count the significant figures in a number, and find absolute, relative and maximum errors.",
          "Lesson {32} (rounding and bounds).",
          "Lesson {34} (percentage error and greatest and least values) and measurement in Physics."),
     ("Significant figures",
      "Significant figures (s.f.) start at the first non-zero digit, wherever the decimal point is.\n"
      "• {0.004507} to {2} s.f.: the first two are {4} and {5}; next is {0}, so {0.0045}.\n"
      "• {38260} to {2} s.f.: {3}, {8}; next {2} → {38000}. Keep the place value with zeros.\n"
      "Counting: leading zeros never count; zeros between digits count; final zeros after a decimal point count. "
      "So {0.0450} has three s.f. and {4507} has four."),
     ("Errors",
      "No measurement is perfect.\n"
      "• Absolute error = |measured − true|: a table of {50} cm measured as {52} cm has an error of {2} cm.\n"
      "• Relative error = absolute error ÷ true value = {2} ÷ {50} = {0.04}. It compares the error with the size: {2} cm on a table matters less than {2} cm on a pencil.\n"
      "• A value given to the nearest {0.1} cm can be wrong by up to {0.05} cm: half the unit. That is the maximum absolute error.")],
    key_words=[("significant figure (s.f.)", "a digit that carries meaning, counted from the first non-zero digit"),
               ("absolute error", "|measured − true|"), ("relative error", "absolute error ÷ true value")],
    examples=["{0.07362} to {2} s.f. = {0.074}", "{619500} to {3} s.f. = {620000}", "true {200} g, measured {196} g: relative error {0.02}"],
    mistake=("{0.004507} to {2} s.f. = {0.00}", "{0.004507} to {2} s.f. = {0.0045}",
             "Significant figures start at the first non-zero digit, not at the decimal point.")))

# ---------------------------------------------------------------- 34. Percentage error; greatest and least values
L.lesson(D, S, 34, ("m4-34", "Find percentage errors and the greatest and least values from approximations"), [33],
  "Percentage error = relative error × 100% = (absolute error ÷ true value) × 100%.\n"
  "A value rounded to a unit has a lower bound (half a unit below) and an upper bound (half a unit above): 7 cm to the nearest cm is between 6.5 cm and 7.5 cm.\n"
  "Greatest and least values of a calculation:\n"
  "• sum: greatest = upper + upper; least = lower + lower.\n"
  "• difference a − b: greatest = upper a − lower b; least = lower a − upper b.\n"
  "• product (positive numbers): greatest = upper × upper; least = lower × lower.",
  worked({"l": 12, "w": 8},
         "A rectangle measures {l} cm by {w} cm, each to the nearest cm. Find the greatest possible perimeter.",
         ["Upper bounds: {l} + {0.5} = {l + 0.5} cm and {w} + {0.5} = {w + 0.5} cm.",
          "Perimeter = {2} × (length + width).", "Greatest = {2} × ({l + 0.5} + {w + 0.5}) = {2 * (l + w + 1)} cm."],
         "{2 * (l + w + 1)} cm",
         checks=["2 * (l + w + 1) == 42"]),
  [card("c4m34-1", "Percentage error = (absolute error ÷ true value) × {100}%.",
        ["true {50}, measured {52}: {2} ÷ {50} × {100}% = {4}%"], "m4-34-pct"),
   card("c4m34-2", "To the nearest unit, the bounds are half a unit below and above.",
        ["{7} cm to the nearest cm: from {6.5} cm to {7.5} cm"], "m4-34-lower"),
   card("c4m34-3", "Greatest sum: add the upper bounds. Greatest difference: upper minus lower.",
        ["{12} cm and {8} cm (nearest cm): greatest sum {21} cm; greatest difference {12.5} − {7.5} = {5} cm"], "m4-34-sum")],
  [num("m4-34-pct", 1, "The true volume of a bottle is {t} ml. It is measured as {m} ml. What is the percentage error?",
       "abs(m - t) / t * 100",
       ["Absolute error = |{m} − {t}| = {abs(m - t)} ml.", "Percentage error = {abs(m - t)} ÷ {t} × {100}% = {answer}%."],
       vars={"t": {"pick": [50, 200, 250, 500, 1000]}, "d": {"int": [-20, 20]}, "m": {"expr": "t + d"}},
       misc=[("rel", "abs(m - t) / t", "Multiply the relative error by {100} to get a percentage."),
             ("meas", "abs(m - t) / m * 100", "Divide by the true value {t}, not the measured value.", "(abs(m - t) * 100) % m == 0")],
       sources=SRCA, where=["d != 0", "(abs(d) * 100) % t == 0"], unit="%"),
   num("m4-34-lower", 1, "A mass is {x} kg to the nearest {u} kg. What is its lower bound, in kg?",
       "dec(x - u / 2)",
       ["Half the unit is {fmt(dec(u / 2))} kg.", "Lower bound = {x} − {fmt(dec(u / 2))} = {answer} kg."],
       vars={"u": {"pick": [1, 2, 10]}, "q": {"int": [3, 40]}, "x": {"expr": "q * u"}},
       misc=[("unit", "x - u", "Go down half a unit, not a whole unit."), ("upper", "dec(x + u / 2)", "That is the upper bound.")],
       sources=SRCA, unit="kg"),
   num("m4-34-sum", 2, "Two lengths are {a} cm and {b} cm, each to the nearest cm. What is the greatest possible total length?",
       "a + b + 1",
       ["Upper bounds: {a + 0.5} cm and {b + 0.5} cm.", "Greatest total = {a + 0.5} + {b + 0.5} = {answer} cm."],
       vars={"a": {"int": [5, 40]}, "b": {"int": [5, 40]}},
       misc=[("plain", "a + b", "Each length could be up to {0.5} cm more: add the upper bounds."),
             ("half", "a + b + 0.5", "Both lengths can be {0.5} cm more: add {0.5} twice.")],
       sources=SRCA, unit="cm"),
   num("m4-34-area", 2, "A rectangular plot is {l} m by {w} m, each to the nearest metre. What is the least possible area, in m²?",
       "(l - 0.5) * (w - 0.5)",
       ["Lower bounds: {l - 0.5} m and {w - 0.5} m.", "Least area = {l - 0.5} × {w - 0.5} = {answer} m²."],
       vars={"l": {"int": [6, 30]}, "w": {"int": [4, 20]}},
       misc=[("plain", "l * w", "Each side could be up to {0.5} m less: use the lower bounds."),
             ("upper", "(l + 0.5) * (w + 0.5)", "That is the greatest area."),
             ("sub", "l * w - 0.5", "Use the lower bound of each side, then multiply.")],
       sources=SRCA, unit="m²"),
   num("m4-34-diff", 3, "A plank {a} cm long (to the nearest cm) has {b} cm (to the nearest cm) cut off. What is the greatest possible length left?",
       "a - b + 1",
       ["Greatest left = greatest start − least cut.", "= {a + 0.5} − {b - 0.5} = {answer} cm."],
       vars={"a": {"int": [60, 200]}, "b": {"int": [10, 50]}},
       misc=[("both", "a - b", "Using upper − upper keeps the same difference. For the greatest, subtract the least cut."),
             ("least", "a - b - 1", "That is the least length left (lower − upper).")],
       sources=SRCA, unit="cm")],
  learn=learn(
    [goal("work out percentage errors and the greatest and least values of sums, differences and products of rounded measurements.",
          "Lesson {33} (absolute and relative error) and Lesson {32} (bounds).",
          "accuracy in Physics practicals and upper and lower bounds in Form Five."),
     ("Percentage error",
      "Percentage error = (absolute error ÷ true value) × {100}%.\n"
      "A bottle holding {500} ml measured as {490} ml: absolute error {10} ml, relative error {10} ÷ {500} = {0.02}, percentage error {2}%.\n"
      "Always divide by the true value."),
     ("Greatest and least values",
      "{12} cm to the nearest cm lies between {11.5} cm and {12.5} cm. Use these bounds to find the extreme answers.\n"
      "• Sum {12} + {8}: greatest {12.5} + {8.5} = {21}; least {11.5} + {7.5} = {19}.\n"
      "• Difference {12} − {8}: greatest {12.5} − {7.5} = {5}; least {11.5} − {8.5} = {3}.\n"
      "• Area {12} × {8}: greatest {12.5} × {8.5} = {106.25}; least {11.5} × {7.5} = {86.25}.\n"
      "For a difference, the greatest uses the larger value's upper bound and the smaller value's lower bound.")],
    key_words=[("percentage error", "(absolute error ÷ true value) × {100}%"), ("upper bound", "the largest value that rounds to the given value"),
               ("lower bound", "the smallest value that rounds to the given value")],
    examples=["{20} m to the nearest m: bounds {19.5} m and {20.5} m", "true {80}, measured {84}: percentage error {5}%"],
    mistake=("greatest of {12} − {8} (nearest cm) = {12.5} − {8.5}", "greatest = {12.5} − {7.5} = {5}",
             "To make a difference as large as possible, take as much as possible away from as little as possible.")))

# ---------------------------------------------------------------- 35. Standard form
L.lesson(D, S, 35, ("m4-35", "Write numbers in standard form and calculate with them"), [33],
  "Standard form is A × 10ⁿ with 1 ≤ A < 10 and n a whole number.\n"
  "• 45 000 = 4.5 × 10⁴; 0.000 32 = 3.2 × 10⁻⁴.\n"
  "• Multiply: multiply the A's and add the indices, then adjust: (3 × 10⁴)(5 × 10³) = 15 × 10⁷ = 1.5 × 10⁸.\n"
  "• Divide: divide the A's and subtract the indices: (6 × 10⁵) ÷ (2 × 10²) = 3 × 10³.\n"
  "• Add or subtract: write both with the same power first: 3 × 10⁴ + 5 × 10³ = 30 × 10³ + 5 × 10³ = 3.5 × 10⁴.",
  worked({"a": 3, "m": 4, "b": 5, "n": 3},
         "Work out ({a} × {10}{sup(m)}) × ({b} × {10}{sup(n)}), giving the answer in standard form.",
         ["Multiply the numbers: {a} × {b} = {a * b}.", "Add the indices: {10}{sup(m)} × {10}{sup(n)} = {10}{sup(m + n)}.",
          "{a * b} × {10}{sup(m + n)} is not in standard form: {a * b} = {dec(a * b / 10)} × {10}."],
         "{dec(a * b / 10)} × {10}{sup(m + n + 1)}",
         checks=["a * b == 15"]),
  [card("c4m35-1", "In standard form the first number is at least {1} and less than {10}.",
        ["{45000} = {4.5} × {10}{sup(4)}; {0.00032} = {3.2} × {10}{sup(-4)}"], "m4-35-write"),
   card("c4m35-2", "Multiplying: multiply the numbers, add the indices, then adjust to standard form.",
        ["({3} × {10}{sup(4)})({5} × {10}{sup(3)}) = {15} × {10}{sup(7)} = {1.5} × {10}{sup(8)}"], "m4-35-mult"),
   card("c4m35-3", "Adding: make the powers the same first.",
        ["{3} × {10}{sup(4)} + {5} × {10}{sup(3)} = {30} × {10}{sup(3)} + {5} × {10}{sup(3)} = {3.5} × {10}{sup(4)}"], "m4-35-add")],
  [mcq("m4-35-write", 1, "Write {fmt(x)} in standard form.",
       "{fmt(A)} × {10}{sup(k)}",
       [("{fmt(dec(A * 10))} × {10}{sup(k - 1)}", "big"), ("{fmt(A)} × {10}{sup(-k)}", "sign"), ("{fmt(A)} × {10}{sup(k + 1)}", "count")],
       ["Move the point so that one non-zero digit is in front: {fmt(A)}.", "The point moved {abs(k)} place{abs(k) == 1 ? '' : 's'} {k > 0 ? 'left, so n = ' + k : 'right, so n = ' + fmt(k)}.", "So the answer is {answer}."],
       vars={"m": {"int": [11, 99]}, "k": {"pick": [-5, -4, -3, -2, 3, 4, 5, 6, 7]}, "A": {"expr": "dec(m / 10)"}, "x": {"expr": "dec(A * 10 ^ k)"}},
       misc=[("big", "The first number must be less than {10}: {fmt(dec(A * 10))} is too big."),
             ("sign", "{k > 0 ? 'A large number has a positive index.' : 'A small number (less than 1) has a negative index.'}"),
             ("count", "Count the places the point moves: {abs(k)}.")],
       sources=SRCA, where=["m % 10 != 0"]),
   num("m4-35-index", 1, "{fmt(x)} = {fmt(A)} × {10}ⁿ. What is n?",
       "k",
       ["The point moves {abs(k)} place{abs(k) == 1 ? '' : 's'} to give {fmt(A)}.", "n = {answer}."],
       vars={"m": {"int": [11, 99]}, "k": {"pick": [-6, -4, -3, -2, 2, 3, 5, 6]}, "A": {"expr": "dec(m / 10)"}, "x": {"expr": "dec(A * 10 ^ k)"}},
       misc=[("sign", "-k", "{k > 0 ? 'The number is large: the index is positive.' : 'The number is less than 1: the index is negative.'}")],
       sources=SRCA, where=["m % 10 != 0"], signed=True),
   mcq("m4-35-mult", 2, "Work out ({fmt(a)} × {10}{sup(m)}) × ({fmt(b)} × {10}{sup(n)}).",
       "{fmt(a * b >= 10 ? dec(a * b / 10) : dec(a * b))} × {10}{sup(a * b >= 10 ? m + n + 1 : m + n)}",
       [("{fmt(dec(a * b))} × {10}{sup(m * n)}", "multidx"), ("{fmt(a * b >= 10 ? dec(a * b / 10) : dec(a * b))} × {10}{sup(a * b >= 10 ? m + n : m + n + 1)}", "adjust"),
        ("{fmt(dec(a + b))} × {10}{sup(m + n)}", "addnum")],
       ["Multiply the numbers: {fmt(a)} × {fmt(b)} = {fmt(dec(a * b))}.", "Add the indices: {m} + {n} = {m + n}.",
        "{a * b >= 10 ? 'Adjust: ' + fmt(dec(a * b)) + ' = ' + fmt(dec(a * b / 10)) + ' × 10, so the index goes up by 1.' : fmt(dec(a * b)) + ' is already between 1 and 10.'}", "So the answer is {answer}."],
       vars={"a": {"pick": [1.5, 2, 2.5, 3, 4, 5, 6, 8]}, "b": {"pick": [1.2, 2, 3, 4, 5, 7]}, "m": {"int": [2, 8]}, "n": {"int": [-4, 6]}},
       misc=[("multidx", "Multiplying powers of {10} adds the indices: {m} + {n}."),
             ("adjust", "{a * b >= 10 ? fmt(dec(a * b)) + ' is 10 or more: write it as ' + fmt(dec(a * b / 10)) + ' × 10 and add 1 to the index.' : 'No adjustment is needed: ' + fmt(dec(a * b)) + ' is less than 10.'}"),
             ("addnum", "Multiply the front numbers, do not add them.")],
       sources=SRCA, where=["m * n != m + n", "dec(a + b) < 10", "dec(a * b) != dec(a + b)"]),
   mcq("m4-35-div", 2, "Work out ({fmt(dec(a * b))} × {10}{sup(m)}) ÷ ({fmt(b)} × {10}{sup(n)}).",
       "{fmt(a)} × {10}{sup(m - n)}",
       [("{fmt(a)} × {10}{sup(m + n)}", "add"), ("{fmt(a)} × {10}{sup(m / n)}", "divi"), ("{fmt(dec(a * b - b))} × {10}{sup(m - n)}", "subnum")],
       ["Divide the numbers: {fmt(dec(a * b))} ÷ {fmt(b)} = {fmt(a)}.", "Subtract the indices: {m} − {br(n)} = {m - n}.", "So the answer is {answer}."],
       vars={"a": {"pick": [1.5, 2, 2.5, 3, 4]}, "b": {"pick": [2, 3]}, "m": {"int": [3, 9]}, "n": {"int": [-3, 5]}},
       misc=[("add", "Dividing subtracts the indices."), ("divi", "Subtract the indices, do not divide them."), ("subnum", "Divide the front numbers.")],
       sources=SRCA, where=["n != 0", "m % n == 0", "m - n != m / n", "dec(a * b) < 10"]),
   mcq("m4-35-add", 3, "Work out {fmt(a)} × {10}{sup(m)} + {fmt(b)} × {10}{sup(m - 1)}, in standard form.",
       "{fmt(dec((a * 10 + b) / 10 >= 10 ? (a * 10 + b) / 100 : (a * 10 + b) / 10))} × {10}{sup((a * 10 + b) / 10 >= 10 ? m + 1 : m)}",
       [("{fmt(dec(a + b))} × {10}{sup(m)}", "addnums"), ("{fmt(dec(a + b))} × {10}{sup(2 * m - 1)}", "addidx"), ("{fmt(dec((a * 10 + b) / 10))} × {10}{sup(m - 1)}", "power")],
       ["Write both with {10}{sup(m - 1)}: {fmt(dec(a * 10))} × {10}{sup(m - 1)} + {fmt(b)} × {10}{sup(m - 1)} = {fmt(dec(a * 10 + b))} × {10}{sup(m - 1)}.",
        "Adjust to standard form.", "So the answer is {answer}."],
       vars={"a": {"pick": [2, 3, 4.5, 6, 7.2]}, "b": {"pick": [1, 3, 5, 8]}, "m": {"int": [3, 7]}},
       misc=[("addnums", "The powers are different: make them the same before adding."),
             ("addidx", "Adding numbers does not add their indices."),
             ("power", "Adjust: {fmt(dec(a * 10 + b))} × {10}{sup(m - 1)} = {fmt(dec((a * 10 + b) / 10))} × {10}{sup(m)}.")],
       sources=SRCA, where=["dec(a + b) != dec((a * 10 + b) / 10)"])],
  learn=learn(
    [goal("write very large and very small numbers in standard form and multiply, divide, add and subtract them.",
          "Lesson {27} (laws of indices) and Lesson {33} (significant figures).",
          "Physics and Chemistry calculations (the mole, wavelengths) and the use of a calculator's EXP key."),
     ("Writing standard form",
      "A × {10}ⁿ with {1} ≤ A < {10}.\n"
      "• {45000}: move the point {4} places left to get {4.5}, so {4.5} × {10}{sup(4)}.\n"
      "• {0.00032}: move it {4} places right to get {3.2}, so {3.2} × {10}{sup(-4)}.\n"
      "Big numbers have a positive index; numbers between {0} and {1} have a negative one.\n"
      "{15} × {10}{sup(7)} is not standard form: {15} = {1.5} × {10}, so it is {1.5} × {10}{sup(8)}."),
     ("Calculating",
      "• Multiply: ({3} × {10}{sup(4)})({5} × {10}{sup(3)}) = {15} × {10}{sup(7)} = {1.5} × {10}{sup(8)}.\n"
      "• Divide: ({6} × {10}{sup(5)}) ÷ ({2} × {10}{sup(2)}) = {3} × {10}{sup(3)}.\n"
      "• Add: make the powers equal first. {3} × {10}{sup(4)} + {5} × {10}{sup(3)} = {30} × {10}{sup(3)} + {5} × {10}{sup(3)} = {35} × {10}{sup(3)} = {3.5} × {10}{sup(4)}.\n"
      "Check the size roughly: {30000} + {5000} = {35000}.")],
    key_words=[("standard form", "A × {10}ⁿ with {1} ≤ A < {10}"), ("index", "the power of {10}"),
               ("adjust", "rewrite so that A is between {1} and {10}")],
    examples=["{602000} = {6.02} × {10}{sup(5)}", "{0.0071} = {7.1} × {10}{sup(-3)}", "({2} × {10}{sup(3)})² = {4} × {10}{sup(6)}"],
    mistake=("{3} × {10}{sup(4)} + {5} × {10}{sup(3)} = {8} × {10}{sup(7)}", "= {3.5} × {10}{sup(4)}",
             "Only multiplying adds indices. For adding, make the powers the same, then add the front numbers.")))
