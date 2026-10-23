"""Form 3 Maths, Term 1, rows 31-34 (indices and logarithms). Run: python tools/authoring/form3/maths_logs.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import bank

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"
SRC = ["indices-logs"]
LOG = "{'log' + sub(b)}"  # log₂, log₃ … written with a subscript base

# ---------------------------------------------------------------- 31. Laws of indices
L.lesson(D, S, 31, ("m3-31", "Use the laws of indices, including zero, negative and fractional indices"), [],
  "Laws of indices (same base a):\n"
  "• aᵐ × aⁿ = aᵐ⁺ⁿ   • aᵐ ÷ aⁿ = aᵐ⁻ⁿ   • (aᵐ)ⁿ = aᵐⁿ\n"
  "• a⁰ = 1 (a ≠ 0)   • a⁻ⁿ = 1/aⁿ, so 2⁻³ = 1/8\n"
  "• a^(1/n) is the nth root of a: 8^(1/3) = 2\n"
  "• a^(m/n) = (nth root of a)ᵐ: 8^(2/3) = 2² = 4. Take the root first, then the power.\n"
  "On a phone we write a^(2/3) for a to the power two-thirds.",
  worked({"N": 27, "r": 3, "p": 2, "q": 3},
         "Evaluate {N}^({p}/{q}).",
         ["The denominator {q} means the cube root: the cube root of {N} is {r}.", "The numerator {p} means square it: {r}² = {r ^ p}."],
         "{r ^ p}", checks=["r ^ q == N"]),
  [card("c3m31-1", "Multiplying powers of the same base: add the indices.",
        ["{pw('x', 3)} × {pw('x', 4)} = {pw('x', 7)}"], "m3-31-mult"),
   card("c3m31-2", "A negative index means one over: a⁻ⁿ = {1}/aⁿ.",
        ["{5}⁻{sup(2)} = {frac(1, 25)}"], "m3-31-neg"),
   card("c3m31-3", "A fractional index is a root: the bottom of the fraction is the root, the top is the power.",
        ["{16}^({1}/{2}) = {4};  {8}^({2}/{3}) = {4}"], "m3-31-frac")],
  [mcq("m3-31-mult", 1, "Simplify {pw('x', a)} × {pw('x', b)}.", "{pw('x', a + b)}",
       [("{pw('x', a * b)}", "times"), ("{mono(2, pw('x', a + b))}", "two"), ("{pw('x', abs(a - b))}", "sub")],
       ["Same base: add the indices, {a} + {b} = {a + b}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [2, 9]}},
       misc=[("times", "Multiplying powers adds the indices; multiplying the indices is for a power of a power."),
             ("two", "x × x is x², not {2}x: there is no number in front."),
             ("sub", "Subtract indices when dividing; here we multiply, so add.")],
       sources=SRC, where=["a * b != a + b", "a != b"]),
   num("m3-31-neg", 1, "Evaluate {a}⁻{sup(n)}. Give the answer as a fraction.", "frac(1, a ^ n)",
       ["A negative index means one over: {a}⁻{sup(n)} = {1}/{a}{sup(n)}.", "{a}{sup(n)} = {a ^ n}, so the answer is {answer}."],
       vars={"a": {"int": [2, 6]}, "n": {"int": [1, 3]}},
       misc=[("neg", "-(a ^ n)", "A negative index does not make the number negative: it means one over."), ("mul", "-a * n", "{a}⁻{sup(n)} is not {a} × ({-n}).")],
       answer_kind="fraction", sources=SRC, where=["a ^ n <= 216", "-(a ^ n) != -a * n"]),
   num("m3-31-frac", 2, "Evaluate {r ^ q}^({p}/{q}).", "r ^ p",
       ["Root first: the {q == 2 ? 'square' : q == 3 ? 'cube' : 'fourth'} root of {r ^ q} is {r}.", "Then the power: {r}{sup(p)} = {answer}."],
       vars={"r": {"int": [2, 5]}, "q": {"int": [2, 3]}, "p": {"int": [2, 3]}},
       misc=[("times", "r ^ q * p / q", "A fractional index is a root and a power, not a multiplication."),
             ("nroot", "(r ^ q) ^ p", "The denominator {q} means a root: take the root before the power.")],
       sources=SRC, where=["p != q", "r ^ q <= 125"]),
   mcq("m3-31-pow", 2, "Simplify ({pw('x', a)}){sup(b)}.", "{pw('x', a * b)}",
       [("{pw('x', a + b)}", "add"), ("{mono(b, pw('x', a))}", "times"), ("{pw('x', a ^ b)}", "power")],
       ["A power of a power: multiply the indices, {a} × {b} = {a * b}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 5]}, "b": {"int": [2, 4]}},
       misc=[("add", "Adding indices is for multiplying powers; a power of a power multiplies them."),
             ("times", "({pw('x', a)}){sup(b)} means {pw('x', a)} multiplied by itself {b} times, not {b} × {pw('x', a)}."),
             ("power", "Multiply the indices: {a} × {b}, not {a} to the power {b}.")],
       sources=SRC, where=["a * b != a + b", "a ^ b != a * b"]),
   num("m3-31-combo", 3, "{c}{sup(a)} × {c}{sup(b)} ÷ {c}{sup(d)} = {c}ⁿ. Find n.", "a + b - d",
       ["Multiplying: add the indices, {a} + {b} = {a + b}.", "Dividing: subtract, {a + b} − {d} = {answer}."],
       vars={"c": {"int": [2, 7]}, "a": {"int": [2, 9]}, "b": {"int": [2, 9]}, "d": {"int": [2, 12]}},
       misc=[("all", "a + b + d", "Dividing subtracts the index: {a + b} − {d}."), ("mult", "a * b - d", "Multiplying powers adds the indices.")],
       sources=SRC, where=["a + b != d", "a * b - d != a + b - d"], signed=True)],
  learn=learn(
    [("Index notation",
      "{pw(2, 5)} means {2} × {2} × {2} × {2} × {2}: the base is {2} and the index (power) is {5}.\n"
      "When you multiply powers of the same base, you are just counting how many times the base appears: "
      "{pw(2, 3)} × {pw(2, 2)} = ({2} × {2} × {2}) × ({2} × {2}) = {pw(2, 5)}. So add the indices.\n"
      "Dividing cancels: {pw(2, 5)} ÷ {pw(2, 2)} = {pw(2, 3)}. So subtract. A power of a power multiplies: ({pw(2, 3)}){sup(2)} = {pw(2, 6)}."),
     ("Zero and negative indices",
      "Keep dividing by {2}: {pw(2, 3)} = {8}, {pw(2, 2)} = {4}, {pw(2, 1)} = {2}, then {pw(2, 0)} = {1}, and next {2}⁻{sup(1)} = {frac(1, 2)}, {2}⁻{sup(2)} = {frac(1, 4)}.\n"
      "So any number (except {0}) to the power zero is {1}, and a negative index means one over: a⁻ⁿ = {1}/aⁿ.\n"
      "A negative index never makes the answer negative."),
     ("Fractional indices",
      "Since a^({1}/{2}) × a^({1}/{2}) = a¹ = a, the index {1}/{2} means the square root. Similarly a^({1}/{3}) is the cube root.\n"
      "For a^(m/n), take the nth root first, then raise to the power m:\n"
      "{27}^({2}/{3}) = (cube root of {27})² = {3}² = {9}.\n"
      "Taking the root first keeps the numbers small.")],
    key_words=[("index (power)", "the small number showing how many times the base is multiplied"), ("base", "the number being multiplied"),
               ("reciprocal", "one over a number: the reciprocal of {4} is {frac(1, 4)}")],
    examples=["{pw('a', 6)} ÷ {pw('a', 2)} = {pw('a', 4)}", "{7}{sup(0)} = {1}", "{10}⁻{sup(3)} = {0.001}", "{32}^({1}/{5}) = {2}"],
    mistake=("{3}⁻{sup(2)} = {-9}", "{3}⁻{sup(2)} = {frac(1, 9)}",
             "A negative index means one over the power. The answer is a small positive fraction.")))

# ---------------------------------------------------------------- 32. Exponential equations
L.lesson(D, S, 32, ("m3-32", "Solve simple exponential equations"), [31],
  "An exponential equation has the unknown in the index: 2ˣ = 32.\n"
  "• Write both sides as powers of the same base: 2ˣ = 2⁵.\n"
  "• If the bases are equal, the indices are equal: x = 5.\n"
  "• 3^(x + 1) = 81 = 3⁴ → x + 1 = 4 → x = 3.\n"
  "• Different bases: 4ˣ = 8 → (2²)ˣ = 2³ → 2x = 3 → x = 3/2.\n"
  "• Fractions: 5ˣ = 1/25 = 5⁻² → x = −2.",
  worked({"p": 2, "m": 2, "n": 3},
         "Solve {p ^ m}ˣ = {p ^ n}.",
         ["Write both as powers of {p}: {p ^ m} = {p}{sup(m)} and {p ^ n} = {p}{sup(n)}.",
          "({p}{sup(m)})ˣ = {p}{sup(n)}, so {p}^({m}x) = {p}{sup(n)}.", "Equal bases, equal indices: {mono(m, 'x')} = {n}, so x = {frac(n, m)}."],
         "x = {frac(n, m)}", checks=["n / m == 1.5"]),
  [card("c3m32-1", "Write both sides as powers of the same base, then set the indices equal.",
        ["{2}ˣ = {32} = {pw(2, 5)} → x = {5}"], "m3-32-same"),
   card("c3m32-2", "If the index is an expression, solve the equation it gives.",
        ["{3}^(x + {1}) = {81} = {pw(3, 4)} → x + {1} = {4} → x = {3}"], "m3-32-shift"),
   card("c3m32-3", "One over a power is a negative index.",
        ["{5}ˣ = {frac(1, 25)} = {5}⁻{sup(2)} → x = {-2}"], "m3-32-neg")],
  [num("m3-32-same", 1, "Solve {b}ˣ = {b ^ n}.", "n",
       ["{b ^ n} = {b}{sup(n)}.", "So {b}ˣ = {b}{sup(n)} and x = {answer}."],
       vars={"b": {"int": [2, 5]}, "n": {"int": [2, 6]}},
       misc=[("div", "b ^ n / b", "x is the index: count how many {b}s multiply to {b ^ n}.")],
       sources=SRC, where=["b ^ n <= 3125", "b ^ n / b != n"]),
   num("m3-32-shift", 1, "Solve {b}^(x + {k}) = {b ^ n}.", "n - k",
       ["{b ^ n} = {b}{sup(n)}, so x + {k} = {n}.", "x = {n} − {k} = {answer}."],
       vars={"b": {"int": [2, 5]}, "n": {"int": [2, 6]}, "k": {"int": [1, 4]}},
       misc=[("add", "n + k", "x + {k} = {n} gives x = {n} − {k}."), ("nok", "n", "{n} is x + {k}. Subtract {k}.")],
       sources=SRC, where=["b ^ n <= 3125", "n != k"], signed=True),
   num("m3-32-diff", 2, "Solve {p ^ m}ˣ = {p ^ n}. Give x as a fraction if it is not whole.", "frac(n, m)",
       ["Both are powers of {p}: ({p}{sup(m)})ˣ = {p}{sup(n)}.", "{mono(m, 'x')} = {n}, so x = {answer}."],
       vars={"p": {"int": [2, 3]}, "m": {"int": [2, 3]}, "n": {"int": [1, 5]}},
       misc=[("flip", "frac(m, n)", "From {mono(m, 'x')} = {n}, x = {n} ÷ {m}, not {m} ÷ {n}.")],
       answer_kind="fraction", sources=SRC, where=["m != n", "p ^ n <= 243", "n % m != 0"]),
   num("m3-32-lin", 2, "Solve {b}^({mono(c, 'x')} − {k}) = {b ^ n}.", "(n + k) / c",
       ["{b ^ n} = {b}{sup(n)}, so {mono(c, 'x')} − {k} = {n}.", "{mono(c, 'x')} = {n + k}, x = {answer}."],
       vars={"b": {"int": [2, 4]}, "c": {"int": [2, 3]}, "k": {"int": [1, 5]}, "n": {"int": [2, 6]}},
       misc=[("sub", "(n - k) / c", "Add {k} to both sides: {mono(c, 'x')} = {n} + {k}.")],
       sources=SRC, where=["(n + k) % c == 0", "b ^ n <= 1024", "n != k"]),
   num("m3-32-neg", 3, "Solve {b}ˣ = {frac(1, b ^ n)}.", "-n",
       ["{frac(1, b ^ n)} = {1}/{b}{sup(n)} = {b}⁻{sup(n)}.", "So x = {answer}."],
       vars={"b": {"int": [2, 5]}, "n": {"int": [1, 4]}},
       misc=[("pos", "n", "One over a power is a negative index: x = {-n}."), ("frac", "1 / n", "x is the index: {frac(1, b ^ n)} = {b}⁻{sup(n)}.")],
       sources=SRC, where=["b ^ n <= 625", "1 / n != -n"], signed=True)],
  learn=learn(
    [("The unknown in the index",
      "In {2}ˣ = {32}, x tells how many {2}s are multiplied. Count: {2}, {4}, {8}, {16}, {32}: five of them, so x = {5}.\n"
      "In general: write both sides as powers of the same base. If {2}ˣ = {pw(2, 5)}, the bases are the same, so the indices must be equal: x = {5}."),
     ("When the index is an expression",
      "{3}^(x + {1}) = {81}. Write {81} = {pw(3, 4)}, so x + {1} = {4} and x = {3}.\n"
      "With a different base, look for a common base: {4}ˣ = {8}. Both are powers of {2}: {4} = {pw(2, 2)} and {8} = {pw(2, 3)}.\n"
      "So {2}^({2}x) = {pw(2, 3)}, {mono(2, 'x')} = {3} and x = {frac(3, 2)}."),
     ("Fractions and negative answers",
      "If the right-hand side is a fraction with a power on the bottom, use a negative index:\n"
      "{5}ˣ = {frac(1, 125)} = {5}⁻{sup(3)}, so x = {-3}.\n"
      "And {7}ˣ = {1} gives x = {0}, because any base to the power zero is {1}.")],
    key_words=[("exponential equation", "an equation with the unknown in the index"), ("common base", "a number of which both sides are powers")],
    examples=["{10}ˣ = {1000} → x = {3}", "{9}ˣ = {27} → x = {frac(3, 2)}", "{2}ˣ = {frac(1, 8)} → x = {-3}"],
    mistake=("{2}ˣ = {16} → x = {8}", "{16} = {pw(2, 4)}, so x = {4}",
             "x is the number of {2}s multiplied together, not {16} ÷ {2}.")))

# ---------------------------------------------------------------- 33. Laws of logarithms
L.lesson(D, S, 33, ("m3-33", "Logarithms and the laws of logarithms"), [31],
  "A logarithm is an index: log_b x = n means bⁿ = x. So log₂ 8 = 3 because 2³ = 8.\n"
  "log without a base means base 10: log 1000 = 3.\n"
  "• log_b b = 1 and log_b 1 = 0.\n"
  "Laws (same base):\n"
  "• log a + log b = log (ab)\n• log a − log b = log (a ÷ b)\n• log (aⁿ) = n log a\n"
  "Example: log 2 + log 5 = log 10 = 1.",
  worked({"p": 4, "q": 25},
         "Without a calculator, find log {p} + log {q}.",
         ["log {p} + log {q} = log ({p} × {q}).", "= log {p * q} = log {10}² = {2}."],
         "{2}", checks=["p * q == 100"]),
  [card("c3m33-1", "log_b x = n means bⁿ = x: a logarithm is an index.",
        ["log₂ {32} = {5} because {pw(2, 5)} = {32}"], "m3-33-eval"),
   card("c3m33-2", "Adding logs multiplies the numbers; subtracting divides them.",
        ["log {2} + log {5} = log {10} = {1}"], "m3-33-law"),
   card("c3m33-3", "A power inside a log comes out in front: log aⁿ = n log a.",
        ["log {8} = log {pw(2, 3)} = {3} log {2}"], "m3-33-pow")],
  [num("m3-33-eval", 1, "Find " + LOG + " {b ^ n}.", "n",
       ["{b}{sup(n)} = {b ^ n}.", "So " + LOG + " {b ^ n} = {answer}."],
       vars={"b": {"int": [2, 5]}, "n": {"int": [2, 5]}},
       misc=[("div", "b ^ n / b", "A logarithm is the index: the power of {b} that gives {b ^ n}.")],
       sources=SRC, where=["b ^ n <= 625", "b ^ n / b != n"]),
   num("m3-33-ten", 1, "Find log {X.s} (base {10}).", "X.v",
       ["{X.w}", "So log {X.s} = {answer}."],
       vars={"X": {"pick": [{"s": "1000", "w": "10³ = 1000", "v": 3}, {"s": "100 000", "w": "10⁵ = 100 000", "v": 5}, {"s": "0.01", "w": "10⁻² = 1/100 = 0.01", "v": -2},
                            {"s": "1", "w": "10⁰ = 1", "v": 0}, {"s": "0.001", "w": "10⁻³ = 0.001", "v": -3}, {"s": "10", "w": "10¹ = 10", "v": 1}]}},
       review="authored", sources=SRC, signed=True),
   mcq("m3-33-law", 2, "Write as a single logarithm: log {p} + log {q} − log {r}.", "{'log ' + fmt(p * q / r)}",
       [("{'log ' + fmt(p + q - r)}", "add"), ("{'log ' + fmt(p * q - r)}", "sub"), ("{'log ' + fmt(p * q * r)}", "mult")],
       ["Adding logs multiplies: log {p} + log {q} = log {p * q}.", "Subtracting divides: log {p * q} − log {r} = log ({p * q} ÷ {r}) = {answer}."],
       vars={"p": {"int": [2, 12]}, "q": {"int": [2, 12]}, "r": {"int": [2, 6]}},
       misc=[("add", "log a + log b is log (ab), not log (a + b)."), ("sub", "log a − log b is log (a ÷ b): divide by {r}."),
             ("mult", "Subtracting a log divides by the number: ÷ {r}, not × {r}.")],
       sources=SRC, where=["(p * q) % r == 0", "p * q / r != p + q - r", "p * q / r != p * q - r", "p + q - r > 0", "p * q - r != p + q - r"]),
   num("m3-33-sum", 2, LOG + " {x} + " + LOG + " {y}: find the value.", "logb(b, x * y)",
       [LOG + " {x} + " + LOG + " {y} = " + LOG + " ({x} × {y}) = " + LOG + " {x * y}.", "{b}{sup(logb(b, x * y))} = {x * y}, so the value is {answer}."],
       vars={"b": {"pick": [2, 3]}, "i": {"int": [1, 4]}, "j": {"int": [1, 4]}, "x": {"expr": "b ^ i * 1"}, "y": {"expr": "b ^ j"}},
       misc=[("prod", "i * j", "Adding logs multiplies the numbers, so the indices add: {i} + {j}.")],
       sources=SRC, where=["i * j != i + j", "x != y || i == j"]),
   num("m3-33-pow", 3, "Given that log {2} ≈ {'0.3010'}, find log {X.n} to {4} decimal places without a calculator.", "roundTo(X.k * 0.3010 + X.c, 0.0001)",
       ["{X.s}", "≈ {answer}."],
       vars={"X": {"pick": [{"n": 8, "s": "log 8 = log 2³ = 3 log 2 = 3 × 0.3010", "k": 3, "c": 0},
                            {"n": 16, "s": "log 16 = log 2⁴ = 4 log 2 = 4 × 0.3010", "k": 4, "c": 0},
                            {"n": 20, "s": "log 20 = log 2 + log 10 = 0.3010 + 1", "k": 1, "c": 1},
                            {"n": 5, "s": "log 5 = log 10 − log 2 = 1 − 0.3010", "k": -1, "c": 1},
                            {"n": 200, "s": "log 200 = log 2 + log 100 = 0.3010 + 2", "k": 1, "c": 2},
                            {"n": 32, "s": "log 32 = log 2⁵ = 5 log 2 = 5 × 0.3010", "k": 5, "c": 0}]}},
       review="authored", sources=SRC)],
  learn=learn(
    [("A logarithm is an index",
      "We know {pw(2, 3)} = {8}. The logarithm turns this round: log₂ {8} = {3}, read \"log to base {2} of {8} is {3}\".\n"
      "log_b x asks: what power of b gives x?\n"
      "• log₃ {81} = {4} because {pw(3, 4)} = {81};\n• log₅ {1} = {0} because {5}{sup(0)} = {1};\n• log b to base b is always {1}.\n"
      "Without a base written, log means base {10}: log {1000} = {3}."),
     ("The laws come from the index laws",
      "Since multiplying powers adds indices, logs turn multiplication into addition:\n"
      "• log a + log b = log (ab)\n• log a − log b = log (a ÷ b)\n• log aⁿ = n log a\n"
      "Example: log {4} + log {25} = log {100} = {2}.\n"
      "Before calculators, people used log tables and these laws to multiply large numbers by adding."),
     ("Using a known value",
      "If you know log {2} ≈ {'0.3010'}, you can find others:\n"
      "• log {8} = log {pw(2, 3)} = {3} log {2} ≈ {0.9030}\n• log {5} = log ({10} ÷ {2}) = {1} − {0.3010} = {0.6990}\n"
      "Careful: log (a + b) is not log a + log b. log ({2} + {8}) = log {10} = {1}, but log {2} + log {8} = log {16}.")],
    key_words=[("logarithm", "log_b x is the power of b that gives x"), ("base", "the number being raised to the power"),
               ("common logarithm", "log to base {10}, written log")],
    examples=["log₂ {64} = {6}", "log {0.1} = {-1}", "log {3} + log {4} = log {12}", "log {pw(5, 3)} = {3} log {5}"],
    mistake=("log {3} + log {4} = log {7}", "log {3} + log {4} = log {12}",
             "Adding logarithms multiplies the numbers inside.")))

# ---------------------------------------------------------------- 34. Logarithmic equations
L.lesson(D, S, 34, ("m3-34", "Solve simple logarithmic equations"), [32, 33],
  "To solve a logarithmic equation, change it to index form, or combine the logs into one first.\n"
  "• log₂ x = 5 → x = 2⁵ = 32.\n• log_x 81 = 4 → x⁴ = 81 → x = 3.\n"
  "• log x + log 4 = log 20 → log 4x = log 20 → 4x = 20 → x = 5.\n"
  "• log₂ (x − 3) = 4 → x − 3 = 16 → x = 19.\n"
  "Check every answer: you cannot take the log of zero or of a negative number, so reject such solutions.",
  worked({"a": 2, "r": 5, "b": 15},
         "Solve log₃ x + log₃ (x − {a}) = log₃ {b}.",
         ["Combine: log₃ [x(x − {a})] = log₃ {b}, so x(x − {a}) = {b}.",
          "{poly([1, 'x²'], [-a, 'x'], [-b, ''])} = {0} → (x − {r})(x + {r - a}) = {0}.",
          "x = {r} or x = {a - r}. x − {a} must be positive, so reject x = {a - r}."],
         "x = {r}", checks=["r * (r - a) == b"]),
  [card("c3m34-1", "Change to index form: log_b x = n means x = bⁿ.",
        ["log₂ x = {5} → x = {pw(2, 5)} = {32}"], "m3-34-index"),
   card("c3m34-2", "Combine logs with the laws, then remove the log from both sides.",
        ["log x + log {4} = log {20} → {mono(4, 'x')} = {20} → x = {5}"], "m3-34-comb"),
   card("c3m34-3", "Reject any answer that makes you take the log of zero or a negative number.",
        ["log (x − {2}) needs x > {2}."], "m3-34-base")],
  [num("m3-34-index", 1, LOG + " x = {n}. Find x.", "b ^ n",
       ["Index form: x = {b}{sup(n)}.", "x = {answer}."],
       vars={"b": {"int": [2, 5]}, "n": {"int": [2, 5]}},
       misc=[("mult", "b * n", "x = {b}{sup(n)}, a power, not {b} × {n}."), ("rev", "n ^ b", "The base is {b}: x = {b}{sup(n)}, not {n}{sup(b)}.")],
       sources=SRC, where=["b ^ n <= 1024", "b * n != b ^ n", "n ^ b != b ^ n"]),
   num("m3-34-base", 1, "Solve logₓ {r ^ n} = {n}.", "r",
       ["Index form: x{sup(n)} = {r ^ n}.", "x = the {n == 2 ? 'square' : n == 3 ? 'cube' : 'fourth'} root of {r ^ n} = {answer}."],
       vars={"r": {"int": [2, 6]}, "n": {"int": [2, 4]}},
       misc=[("div", "r ^ n / n", "x{sup(n)} = {r ^ n}: take the root, do not divide by {n}.")],
       sources=SRC, where=["r ^ n <= 1296", "r ^ n / n != r"]),
   num("m3-34-comb", 2, "Solve log x + log {a} = log {a * k}.", "k",
       ["log x + log {a} = log ({a}x).", "So {mono(a, 'x')} = {a * k} and x = {answer}."],
       vars={"a": {"int": [2, 9]}, "k": {"int": [2, 15]}},
       misc=[("sub", "a * k - a", "log x + log {a} = log ({a}x): the {a} multiplies x, it is not added.")],
       sources=SRC, where=["a * k - a != k"]),
   num("m3-34-shift", 2, LOG + " (x − {a}) = {n}. Find x.", "b ^ n + a",
       ["Index form: x − {a} = {b}{sup(n)} = {b ^ n}.", "x = {b ^ n} + {a} = {answer}."],
       vars={"b": {"int": [2, 3]}, "n": {"int": [2, 5]}, "a": {"int": [1, 9]}},
       misc=[("sub", "b ^ n - a", "x − {a} = {b ^ n}, so add {a}: x = {b ^ n} + {a}."), ("noexp", "n + a", "Change to index form first: x − {a} = {b}{sup(n)}.")],
       sources=SRC, where=["b ^ n <= 243", "b ^ n - a != n + a"]),
   num("m3-34-quad", 3, "Solve " + LOG + " x + " + LOG + " (x − {a}) = " + LOG + " {r * (r - a)}.", "r",
       ["Combine: x(x − {a}) = {r * (r - a)}, so {poly([1, 'x²'], [-a, 'x'], [-r * (r - a), ''])} = {0}.",
        "(x − {r})(x + {r - a}) = {0}: x = {r} or x = {a - r}.", "x − {a} must be positive, so x = {answer}."],
       vars={"b": {"pick": [2, 3, 10]}, "a": {"int": [1, 5]}, "r": {"int": [3, 10]}},
       misc=[("neg", "a - r", "x = {a - r} would make you take the log of a negative number: reject it."),
             ("lin", "r * (r - a) / a + 0", "x(x − {a}) is not {a}x: expand and solve the quadratic.")],
       sources=SRC, where=["r > a", "a - r != r", "r * (r - a) / a != r"], signed=True)],
  learn=learn(
    [("Index form",
      "Every log statement is an index statement in disguise: log_b x = n means x = bⁿ.\n"
      "So log₂ x = {5} gives x = {pw(2, 5)} = {32}, and logₓ {49} = {2} gives x² = {49}, so x = {7} (a base must be positive).\n"
      "When the unknown is inside a bracket, log₃ (x + {1}) = {2} gives x + {1} = {9}, so x = {8}."),
     ("Combining logs",
      "If there are several logs, use the laws to make one log on each side:\n"
      "log x + log {4} = log {20} → log ({4}x) = log {20} → {mono(4, 'x')} = {20} → x = {5}.\n"
      "When both sides are a single log of the same base, the insides must be equal."),
     ("Checking answers",
      "Logs exist only for positive numbers. In log₂ x + log₂ (x − {2}) = log₂ {15}, you get x(x − {2}) = {15}, so x = {5} or x = {-3}.\n"
      "x = {-3} would need log₂ ({-3}), which does not exist, so the only solution is x = {5}.\n"
      "Always substitute back to check.")],
    key_words=[("index form", "writing log_b x = n as bⁿ = x"), ("logarithmic equation", "an equation with the unknown inside a log"),
               ("reject", "discard a solution that does not fit the original equation")],
    examples=["log₃ x = {4} → x = {81}", "log x − log {3} = log {5} → x = {15}", "log₅ (x + {2}) = {2} → x = {23}"],
    mistake=("log₂ x = {3} → x = {6}", "log₂ x = {3} → x = {pw(2, 3)} = {8}",
             "The log is the index: x is {2} raised to the power {3}, not {2} × {3}.")))
