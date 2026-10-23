"""Form 4 Maths, Term 1, rows 7-11: quadratic equations (factorisation, completing the square, the formula, equations
from roots). Run: python tools/authoring/form4/maths_quadratics.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import goal, bank, not_half

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRC = ["quadratic-equations"]

# ---------------------------------------------------------------- 7. Solving quadratic equations by factorisation
L.lesson(D, S, 7, ("m4-7", "Solve quadratic equations by factorisation"), [5, 6],
  "To solve a quadratic equation by factorisation:\n"
  "1. Rearrange so that one side is 0: ax² + bx + c = 0.\n"
  "2. Factorise the left side.\n"
  "3. If a product is 0, one of the factors is 0: set each bracket equal to 0 and solve.\n"
  "Example: x² − x − 12 = 0 → (x − 4)(x + 3) = 0 → x = 4 or x = −3.\n"
  "Never divide both sides by x: in x² = 5x you would lose the root x = 0. Write x² − 5x = 0, x(x − 5) = 0, so x = 0 or x = 5.\n"
  "A quadratic equation has at most two roots. Check each by substituting it back.",
  worked({"p": 4, "q": -3},
         "Solve {quad(1, -(p + q), p * q)} = {0}.",
         ["Factorise: two numbers with product {p * q} and sum {-(p + q)} are {-p} and {-q}.",
          "So {lin2(1, -p, 1, -q)} = {0}.",
          "Either x − {p} = {0}, giving x = {p}, or x + {-q} = {0}, giving x = {q}.",
          "Check x = {p}: {p}² − {p + q} × {p} + {br(p * q)} = {p * p - (p + q) * p + p * q}."],
         "x = {p} or x = {q}",
         checks=["p * p - (p + q) * p + p * q == 0", "q * q - (p + q) * q + p * q == 0"]),
  [card("c4m7-1", "If two factors multiply to give {0}, at least one of them is {0}.",
        ["{lin2(1, -2, 1, 7)} = {0} means x − {2} = {0} or x + {7} = {0}: x = {2} or x = {-7}"], "m4-7-zero"),
   card("c4m7-2", "Make one side {0} and factorise before using that rule.",
        ["{quad(1, 0, 0)} = {mono(6, 'x')} − {8} → {quad(1, -6, 8)} = {0} → {lin2(1, -2, 1, -4)} = {0}"], "m4-7-solve"),
   card("c4m7-3", "Never divide by x: you lose the root x = {0}. Take x out as a common factor instead.",
        ["{quad(1, 0, 0)} = {mono(3, 'x')} → x({poly([1, 'x'], [-3, ''])}) = {0} → x = {0} or x = {3}"], "m4-7-commonx")],
  [num("m4-7-zero", 1, "Solve {lin2(1, -p, 1, -q)} = {0}. Give the larger root.",
       "max(p, q)",
       ["Either x − {br(p)} = {0} or x − {br(q)} = {0}.", "So x = {p} or x = {q}.", "The larger root is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sign", "max(-p, -q)", "x − {br(p)} = {0} gives x = {p}: the root has the opposite sign to the number in the bracket."),
             ("small", "min(p, q)", "That is the smaller root. The larger is {max(p, q)}.")],
       sources=SRC, where=["p != q", "p != 0 && q != 0", "max(-p, -q) != max(p, q)"], signed=True),
   mcq("m4-7-solve", 1, "Solve {quad(1, -(p + q), p * q)} = {0}.",
       "x = {p} or x = {q}",
       [("x = {-p} or x = {-q}", "sign"), ("x = {p * q}", "const"), ("x = {p} only", "one")],
       ["Factorise: {lin2(1, -p, 1, -q)} = {0}.", "Each bracket can be {0}: x = {p} or x = {q}.", "So the answer is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sign", "The factors are {lin2(1, -p, 1, -q)}. x − {br(p)} = {0} gives x = {p}, not {-p}."),
             ("const", "{p * q} is the number term, not a root. Factorise and set each bracket to {0}."),
             ("one", "A quadratic has two roots here: the other bracket gives x = {q}.")],
       sources=SRC, where=["p < q", "p != 0 && q != 0", "p != -q"]),
   mcq("m4-7-commonx", 2, "Solve {quad(1, 0, 0)} = {mono(k, 'x')}.",
       "x = {0} or x = {k}",
       [("x = {k} only", "divide"), ("x = {sqrtFloor(k)}", "root"), ("x = {0} or x = {-k}", "sign")],
       ["Make one side {0}: {quad(1, -k, 0)} = {0}.", "Factorise: x({poly([1, 'x'], [-k, ''])}) = {0}.", "So x = {0} or x = {k}."],
       vars={"k": {"int": [2, 12]}},
       misc=[("divide", "Dividing both sides by x loses the root x = {0}. Factorise x({poly([1, 'x'], [-k, ''])}) = {0} instead."),
             ("root", "x² = {mono(k, 'x')} is not x² = {k}. Bring {mono(k, 'x')} over and factorise."),
             ("sign", "x − {k} = {0} gives x = {k}, not {-k}.")],
       sources=SRC, where=["sqrtFloor(k) != k", "sqrtFloor(k) != 0"]),
   mcq("m4-7-ax", 2, "Solve {quad(r * t, r * u + s * t, s * u)} = {0}.",
       "x = {frac(-s, r)} or x = {frac(-u, t)}",
       [("x = {frac(s, r)} or x = {frac(u, t)}", "sign"), ("x = {-s} or x = {-u}", "noa"), ("x = {frac(-r, s)} or x = {frac(-t, u)}", "flip")],
       ["Factorise: {lin2(r, s, t, u)} = {0}.", "{mono(r, 'x')} + {br(s)} = {0} gives x = {frac(-s, r)}; {mono(t, 'x')} + {br(u)} = {0} gives x = {frac(-u, t)}.", "So the answer is {answer}."],
       vars={"r": {"int": [2, 4]}, "s": {"int": [-5, 5]}, "t": {"int": [1, 3]}, "u": {"int": [-5, 5]}},
       misc=[("sign", "Moving {s} to the other side changes its sign: {mono(r, 'x')} = {-s}."),
             ("noa", "After {mono(r, 'x')} = {-s}, divide by {r}: x = {frac(-s, r)}."),
             ("flip", "{mono(r, 'x')} = {-s} gives x = {-s} ÷ {r} = {frac(-s, r)}, not {r} ÷ {br(-s)}.")],
       sources=SRC, where=["s != 0 && u != 0", "hcf(r, abs(s)) == 1 && hcf(t, abs(u)) == 1", "s * t != u * r", "r * u + s * t != 0"]),
   num("m4-7-area", 3, "A rectangular garden in Bamenda is {d} m longer than it is wide. Its area is {w * (w + d)} m². Write an equation in x, the width in metres, and solve it. What is the width?",
       "w",
       ["x(x + {d}) = {w * (w + d)}, so {quad(1, d, -w * (w + d))} = {0}.",
        "Factorise: {lin2(1, -w, 1, w + d)} = {0}, so x = {w} or x = {-(w + d)}.",
        "A width cannot be negative, so the width is {answer} m."],
       vars={"w": {"int": [3, 15]}, "d": {"int": [2, 9]}},
       misc=[("length", "w + d", "{w + d} m is the length. The width is {d} m less: {w} m."),
             ("neg", "-(w + d)", "A length cannot be negative: reject x = {-(w + d)}.")],
       sources=SRC, unit="m")],
  learn=learn(
    [goal("solve any quadratic equation that factorises, including x² = kx, and reject roots that make no sense.",
          "Lessons {5} and {6} (factorising trinomials) and Form Three linear equations.",
          "completing the square and the quadratic formula, for equations that do not factorise."),
     ("Why a product of {0} helps",
      "If two numbers multiply to give {0}, at least one of them must be {0}. "
      "So once a quadratic is written as a product of two brackets equal to {0}, each bracket gives a root.\n"
      "Solve {quad(1, -1, -12)} = {0}:\n"
      "• Factorise: {lin2(1, -4, 1, 3)} = {0}.\n"
      "• Either x − {4} = {0}, so x = {4}; or x + {3} = {0}, so x = {-3}.\n"
      "Check x = {4}: {16} − {4} − {12} = {0}. Correct.\n"
      "The rule works only when one side is {0}: (x − {1})(x − {2}) = {6} does not mean x − {1} = {6}."),
     ("Rearrange first",
      "Bring every term to one side before factorising.\n"
      "• {quad(1, 0, 0)} + {mono(2, 'x')} = {15} becomes {quad(1, 2, -15)} = {0}, so {lin2(1, 5, 1, -3)} = {0}: x = {-5} or x = {3}.\n"
      "• {quad(1, 0, 0)} = {mono(7, 'x')}: do not divide by x. Write {quad(1, -7, 0)} = {0}, x(x − {7}) = {0}, so x = {0} or x = {7}.\n"
      "• {quad(2, -1, -3)} = {0}: {lin2(2, -3, 1, 1)} = {0}, so x = {frac(3, 2)} or x = {-1}.\n"
      "In a word problem, reject a root that makes no sense, such as a negative length.")],
    key_words=[("root", "a value of x that makes the equation true"),
               ("quadratic equation", "an equation with x² as the highest power, such as {quad(1, -1, -12)} = {0}"),
               ("reject", "leave out a root that does not fit the problem")],
    examples=["{quad(1, -5, 6)} = {0} → x = {2} or x = {3}", "{quad(1, 0, -9)} = {0} → x = {3} or x = {-3}", "{quad(1, 4, 0)} = {0} → x = {0} or x = {-4}"],
    mistake=("{quad(1, 0, 0)} = {mono(5, 'x')}, so x = {5}", "x² − {mono(5, 'x')} = {0}, so x = {0} or x = {5}",
             "Dividing both sides by x throws away the root x = {0}. Factorise instead.")))

# ---------------------------------------------------------------- 8. Completing the square
L.lesson(D, S, 8, ("m4-8", "Solve quadratic equations by completing the square"), [2, 7],
  "Completing the square writes x² + bx + c as (x + b/2)² + something.\n"
  "x² + bx = (x + b/2)² − (b/2)². Add (b/2)² to make a perfect square.\n"
  "Example: x² + 6x + 2 = 0 → (x + 3)² − 9 + 2 = 0 → (x + 3)² = 7 → x + 3 = ±√7 → x = −3 ± √7.\n"
  "Do not forget the ± when you take a square root: both roots count.\n"
  "If the coefficient of x² is not 1, divide the whole equation by it first.\n"
  "The completed square also gives the minimum value of x² + bx + c: it is c − (b/2)², reached when x = −b/2.",
  worked({"h": 3, "c": 2},
         "Solve {quad(1, 2 * h, c)} = {0} by completing the square. Leave the answer as a surd.",
         ["Half the coefficient of x is {h}, and {h}² = {h * h}.",
          "{quad(1, 2 * h, 0)} = (x + {h})² − {h * h}, so the equation is (x + {h})² − {h * h} + {c} = {0}.",
          "(x + {h})² = {h * h - c}.",
          "x + {h} = ±√{h * h - c}, so x = {-h} ± √{h * h - c}."],
         "x = {-h} + √{h * h - c} or x = {-h} − √{h * h - c}",
         checks=["h * h - c == 7"]),
  [card("c4m8-1", "To make x² + bx a perfect square, add the square of half of b.",
        ["{quad(1, 10, 0)} + {25} = ({poly([1, 'x'], [5, ''])})², because half of {10} is {5} and {5}² = {25}"], "m4-8-add"),
   card("c4m8-2", "x² + bx + c = (x + b/{2})² − (b/{2})² + c.",
        ["{quad(1, 8, 3)} = ({poly([1, 'x'], [4, ''])})² − {16} + {3} = ({poly([1, 'x'], [4, ''])})² − {13}"], "m4-8-form"),
   card("c4m8-3", "Taking a square root gives two answers: + and −.",
        ["({poly([1, 'x'], [2, ''])})² = {9} → x + {2} = {3} or x + {2} = {-3} → x = {1} or x = {-5}"], "m4-8-root")],
  [num("m4-8-add", 1, "What number must be added to {quad(1, 2 * h, 0)} to make a perfect square?",
       "h * h",
       ["Half of {2 * h} is {h}.", "{h}² = {answer}, and {quad(1, 2 * h, h * h)} = ({poly([1, 'x'], [h, ''])})²."],
       vars={"h": {"int": [-9, 9]}},
       misc=[("half", "h", "Half of {2 * h} is {h}, but you add its square: {h}² = {h * h}."),
             ("bsq", "4 * h * h", "Square half of b, not b itself: ({h})² = {h * h}.")],
       sources=SRC, where=["h != 0 && h != 1 && h != -1"]),
   mcq("m4-8-form", 1, "Write {quad(1, 2 * h, c)} in the form (x + p)² + q.",
       "({poly([1, 'x'], [h, ''])})² {c - h * h >= 0 ? '+' : '−'} {abs(c - h * h)}",
       [("({poly([1, 'x'], [h, ''])})² {c + h * h >= 0 ? '+' : '−'} {abs(c + h * h)}", "plus"),
        ("({poly([1, 'x'], [2 * h, ''])})² {c - 4 * h * h >= 0 ? '+' : '−'} {abs(c - 4 * h * h)}", "full"),
        ("({poly([1, 'x'], [h, ''])})² {c >= 0 ? '+' : '−'} {abs(c)}", "forgot")],
       ["Half of {2 * h} is {h}: {quad(1, 2 * h, 0)} = ({poly([1, 'x'], [h, ''])})² − {h * h}.",
        "Add {c}: q = {c} − {h * h} = {c - h * h}.", "So the answer is {answer}."],
       vars={"h": {"int": [-6, 6]}, "c": {"int": [-12, 12]}},
       misc=[("plus", "({poly([1, 'x'], [h, ''])})² is {h * h} too big, so subtract {h * h}: q = {c} − {h * h}."),
             ("full", "Use half of {2 * h}, which is {h}, inside the bracket."),
             ("forgot", "({poly([1, 'x'], [h, ''])})² already adds {h * h}. Take it away again: q = {c - h * h}.")],
       sources=SRC, where=["h != 0", "c != 0", "c - h * h != 0", "c + h * h != 0"]),
   num("m4-8-root", 2, "Solve ({poly([1, 'x'], [h, ''])})² = {k * k}. Give the larger root.",
       "k - h",
       ["x + {br(h)} = {k} or x + {br(h)} = {-k}.", "x = {k - h} or x = {-k - h}.", "The larger root is {answer}."],
       vars={"h": {"int": [-9, 9]}, "k": {"int": [2, 9]}},
       misc=[("plush", "k + h", "Subtract {h} from both sides: x = {k} − {br(h)} = {k - h}."),
             ("square", "k * k - h", "First take the square root: x + {br(h)} = ±{k}."),
             ("small", "-k - h", "That is the smaller root. The larger is {k - h}.")],
       sources=SRC, where=["h != 0", "k != h && k != -h"], signed=True),
   mcq("m4-8-surd", 2, "Solve {quad(1, 2 * h, c)} = {0} by completing the square.",
       "x = {-h} ± √{h * h - c}",
       [("x = {h} ± √{h * h - c}", "sign"), ("x = {-h} ± √{h * h + c}", "plus"), ("x = {-h} + √{h * h - c} only", "one")],
       ["(x + {h})² − {h * h} + {br(c)} = {0}, so (x + {h})² = {h * h - c}.", "x + {h} = ±√{h * h - c}.", "So the answer is {answer}."],
       vars={"h": {"int": [1, 6]}, "c": {"int": [-9, 9]}},
       misc=[("sign", "x + {h} = ±√… gives x = {-h} ± √…: move {h} across and its sign changes."),
             ("plus", "(x + {h})² = {h * h} − {br(c)} = {h * h - c}: the {c} moves across with its sign changed."),
             ("one", "A square root has two signs: x + {h} = +√{h * h - c} or −√{h * h - c}.")],
       sources=SRC, where=["c != 0", "h * h - c > 1", "!isPerfectSquare(h * h - c)", "!isPerfectSquare(h * h + c) || h * h + c <= 0", "h * h + c > 0"]),
   num("m4-8-min", 3, "By completing the square, find the minimum value of {quad(1, 2 * h, c)}.",
       "c - h * h",
       ["{quad(1, 2 * h, c)} = ({poly([1, 'x'], [h, ''])})² + {br(c - h * h)}.",
        "A square is never negative, so the smallest it can be is {0}, when x = {-h}.", "The minimum value is {answer}."],
       vars={"h": {"int": [-6, 6]}, "c": {"int": [-12, 12]}},
       misc=[("c", "c", "x = {0} is not where the minimum is. Complete the square: the minimum is {c} − {h * h}."),
             ("x", "-h", "{-h} is the value of x at the minimum. The minimum value itself is {c - h * h}."),
             ("plus", "c + h * h", "({poly([1, 'x'], [h, ''])})² is {h * h} too big: subtract {h * h}, do not add it.")],
       sources=SRC, where=["h != 0", "c - h * h != -h", "c != 0"], signed=True)],
  learn=learn(
    [goal("complete the square for x² + bx + c and use it to solve equations that do not factorise, with exact (surd) answers.",
          "Lesson {2} (the perfect square (a + b)²) and Lesson {7} (solving by factorisation).",
          "Lesson {9}, where completing the square on ax² + bx + c gives the quadratic formula."),
     ("Making a perfect square",
      "From Lesson {2}: ({poly([1, 'x'], [3, ''])})² = {quad(1, 6, 9)}. The {6} is twice {3}, and the {9} is {3}².\n"
      "So to turn {quad(1, 6, 0)} into a perfect square, take half of {6}, which is {3}, and add {3}² = {9}.\n"
      "In general: x² + bx = (x + b/{2})² − (b/{2})².\n"
      "• {quad(1, 6, 2)} = ({poly([1, 'x'], [3, ''])})² − {9} + {2} = ({poly([1, 'x'], [3, ''])})² − {7}.\n"
      "• {quad(1, -4, 1)} = ({poly([1, 'x'], [-2, ''])})² − {4} + {1} = ({poly([1, 'x'], [-2, ''])})² − {3}."),
     ("Solving with it",
      "Solve {quad(1, 6, 2)} = {0}.\n"
      "• Complete the square: ({poly([1, 'x'], [3, ''])})² − {7} = {0}, so ({poly([1, 'x'], [3, ''])})² = {7}.\n"
      "• Take the square root, both signs: x + {3} = ±√{7}.\n"
      "• x = {-3} + √{7} or x = {-3} − √{7}. As decimals: {roundTo(-3 + sqrt(7), 0.01)} or {roundTo(-3 - sqrt(7), 0.01)}.\n"
      "If the number in front of x² is not {1}, divide every term by it first: {quad(2, 8, -6)} = {0} becomes {quad(1, 4, -3)} = {0}.")],
    key_words=[("perfect square", "an expression equal to (x + p)²"),
               ("completing the square", "writing x² + bx + c as (x + p)² + q"),
               ("surd", "a root that is not a whole number, such as √{7}, left exact"),
               ("±", "plus or minus: both signs give a root")],
    examples=["{quad(1, 8, 0)} = ({poly([1, 'x'], [4, ''])})² − {16}", "({poly([1, 'x'], [-1, ''])})² = {5} → x = {1} ± √{5}", "minimum of {quad(1, -6, 11)} = {11} − {9} = {2}"],
    mistake=("({poly([1, 'x'], [3, ''])})² = {7} → x = {-3} + √{7}", "x = {-3} + √{7} or x = {-3} − √{7}",
             "√{7} and −√{7} both square to {7}. Taking the square root needs ±, or one root is lost.")))

# ---------------------------------------------------------------- 9. Developing the quadratic formula
DERIVE = [
    {"q": "Deriving the formula from ax² + bx + c = {0}, what is the first step?", "r": "Divide every term by a",
     "w": ["Take the square root of both sides", "Subtract b from both sides", "Multiply every term by c"],
     "e": ["There is no square yet to take the root of; first make the x² coefficient {1}.",
           "bx is a term with x; subtracting b alone does not keep the equation balanced.",
           "Multiplying by c does not help; the aim is x² with coefficient {1}."],
     "y": "Dividing by a gives x² + (b/a)x + c/a = {0}, ready for completing the square."},
    {"q": "After dividing by a and moving c/a, we have x² + (b/a)x = −c/a. What is added to both sides?", "r": "(b/{2}a)²",
     "w": ["(b/a)²", "b/{2}a", "c/a"],
     "e": ["Half of the coefficient b/a is b/{2}a; square that, not b/a.",
           "b/{2}a must be squared to complete the square.",
           "c/a is already used; the added term comes from the x coefficient."],
     "y": "Half of b/a is b/{2}a; adding (b/{2}a)² makes the left side (x + b/{2}a)²."},
    {"q": "The completed square is (x + b/{2}a)² = (b² − {4}ac)/{4}a². What is the next step?", "r": "Take the square root of both sides, with ±",
     "w": ["Divide both sides by {4}a²", "Square both sides", "Take the square root with + only"],
     "e": ["{4}a² is inside the fraction; the next step removes the square on the left.",
           "Squaring makes it more complicated; we need to undo the square.",
           "Both signs give roots; the ± is the reason a quadratic can have two roots."],
     "y": "x + b/{2}a = ±√(b² − {4}ac)/{2}a, then subtract b/{2}a."},
    {"q": "Which expression decides how many real roots ax² + bx + c = {0} has?", "r": "b² − {4}ac",
     "w": ["b² + {4}ac", "{2}a", "−b"],
     "e": ["The formula has b² minus {4}ac under the root.",
           "{2}a is the denominator; it never changes the number of roots.",
           "−b only shifts both roots together."],
     "y": "b² − {4}ac is under the square root: positive gives two roots, zero one, negative none."},
]

L.lesson(D, S, 9, ("m4-9", "Develop the quadratic formula by completing the square"), [8],
  "Completing the square on ax² + bx + c = 0 gives the quadratic formula:\n"
  "x = (−b ± √(b² − 4ac)) / 2a.\n"
  "Steps: divide by a; move c/a; add (b/2a)² to both sides; write the left side as (x + b/2a)²; take the square root with ±; subtract b/2a.\n"
  "Identify a, b and c with their signs: in 3x² − 5x + 2 = 0, a = 3, b = −5, c = 2.\n"
  "b² − 4ac is called the discriminant. In 3x² − 5x + 2 = 0 it is 25 − 24 = 1.",
  worked({"a": 2, "b": 3, "c": -5},
         "Write the quadratic formula with the numbers of {quad(a, b, c)} = {0} put in.",
         ["Read off a = {a}, b = {b}, c = {c}, with their signs.",
          "b² − {4}ac = {b * b} − {4} × {a} × {br(c)} = {b * b - 4 * a * c}.",
          "{2}a = {2 * a} and −b = {-b}."],
         "x = ({-b} ± √{b * b - 4 * a * c}) / {2 * a}",
         checks=["b * b - 4 * a * c == 49"]),
  [card("c4m9-1", "Read a, b and c with their signs from ax² + bx + c = {0}.",
        ["{quad(3, -5, 2)} = {0}: a = {3}, b = {-5}, c = {2}"], "m4-9-abc"),
   card("c4m9-2", "b² − {4}ac is the discriminant: the number under the square root in the formula.",
        ["{quad(3, -5, 2)}: b² − {4}ac = {25} − {24} = {1}"], "m4-9-disc"),
   card("c4m9-3", "The formula comes from completing the square on ax² + bx + c = {0}.",
        ["divide by a → add (b/{2}a)² → take ± square root → x = (−b ± √(b² − {4}ac))/{2}a"], "m4-9-step")],
  [mcq("m4-9-abc", 1, "In {quad(a, b, c)} = {0}, what are a, b and c?",
       "a = {a}, b = {b}, c = {c}",
       [("a = {a}, b = {-b}, c = {c}", "bsign"), ("a = {a}, b = {b}, c = {-c}", "csign"), ("a = {c}, b = {b}, c = {a}", "swap")],
       ["a is the coefficient of x², b of x, c is the number term, each with its sign.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 7]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("bsign", "The sign in front of the x term belongs to b: b = {b}."),
             ("csign", "The sign in front of the number belongs to c: c = {c}."),
             ("swap", "a goes with x² and c is the number term.")],
       sources=SRC, where=["b != 0 && c != 0", "a != c", "a != abs(c)"]),
   num("m4-9-disc", 1, "Find the discriminant b² − {4}ac of {quad(a, b, c)} = {0}.",
       "b * b - 4 * a * c",
       ["b² = {b * b}.", "{4}ac = {4} × {a} × {br(c)} = {4 * a * c}.", "b² − {4}ac = {b * b} − {br(4 * a * c)} = {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("plus", "b * b + 4 * a * c", "It is b² minus {4}ac: {b * b} − {br(4 * a * c)}."),
             ("bsign", "-(b * b) - 4 * a * c", "b² is always positive: ({b})² = {b * b}."),
             ("twoac", "b * b - 2 * a * c", "Use {4}ac, not {2}ac: {4} × {a} × {br(c)} = {4 * a * c}.")],
       sources=SRC, where=["b != 0 && c != 0", "b * b - 4 * a * c != b * b + 4 * a * c"], signed=True),
   bank("m4-9-step", 2, "{X.q}", DERIVE, SRC),
   mcq("m4-9-sub", 2, "Which is the quadratic formula with the numbers of {quad(a, b, c)} = {0} put in?",
       "x = ({-b} ± √{b * b - 4 * a * c}) / {2 * a}",
       [("x = ({b} ± √{b * b - 4 * a * c}) / {2 * a}", "minusb"), ("x = ({-b} ± √{b * b + 4 * a * c}) / {2 * a}", "plus"), ("x = ({-b} ± √{b * b - 4 * a * c}) / {a}", "twoa")],
       ["a = {a}, b = {b}, c = {c}.", "−b = {-b}; b² − {4}ac = {b * b - 4 * a * c}; {2}a = {2 * a}.", "So the answer is {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("minusb", "The formula starts with −b: −({b}) = {-b}."),
             ("plus", "Under the root it is b² minus {4}ac: {b * b} − {br(4 * a * c)} = {b * b - 4 * a * c}."),
             ("twoa", "Divide by {2}a = {2 * a}, not by a.")],
       sources=SRC, where=["b != 0 && c != 0", "b * b - 4 * a * c > 0", "b * b + 4 * a * c != b * b - 4 * a * c", "a != 2 * a"]),
   num("m4-9-nature", 3, "For {quad(a, b, c)} = {0}, the discriminant is {b * b - 4 * a * c}. How many real roots does the equation have? (Type 0, 1 or 2.)",
       "b * b - 4 * a * c > 0 ? 2 : b * b - 4 * a * c == 0 ? 1 : 0",
       ["Under the square root is b² − {4}ac = {b * b - 4 * a * c}.",
        "Positive: two roots (±). Zero: one repeated root. Negative: no real square root, so no real roots.", "So the answer is {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-8, 8]}, "c": {"int": [-6, 6]}},
       misc=[("always2", "b * b - 4 * a * c > 0 ? 1 : 2", "Look at the sign of {b * b - 4 * a * c}: positive gives {2}, zero {1}, negative {0}.")],
       sources=SRC, where=["c != 0"])],
  learn=learn(
    [goal("explain each step that turns ax² + bx + c = {0} into the quadratic formula, and put the numbers of an equation into it.",
          "Lesson {8} (completing the square, with the ± root).",
          "Lesson {10} (solving any quadratic with the formula) and later the discriminant and the nature of roots."),
     ("Completing the square on letters",
      "Do on ax² + bx + c = {0} what Lesson {8} did with numbers.\n"
      "• Divide by a: x² + (b/a)x + c/a = {0}.\n"
      "• Move c/a: x² + (b/a)x = −c/a.\n"
      "• Add (b/{2}a)², the square of half the x coefficient: (x + b/{2}a)² = b²/{4}a² − c/a = (b² − {4}ac)/{4}a².\n"
      "• Square root with ±: x + b/{2}a = ±√(b² − {4}ac)/{2}a.\n"
      "• Subtract b/{2}a: x = (−b ± √(b² − {4}ac)) / {2}a."),
     ("Reading a, b and c",
      "Write the equation as ax² + bx + c = {0} first, then read each number with its sign.\n"
      "• {quad(3, -5, 2)} = {0}: a = {3}, b = {-5}, c = {2}.\n"
      "• {quad(1, 4, -7)} = {0}: a = {1}, b = {4}, c = {-7}.\n"
      "• {quad(2, 0, -9)} = {0}: a = {2}, b = {0}, c = {-9}.\n"
      "The number under the root, b² − {4}ac, is the discriminant. For {quad(3, -5, 2)} it is {25} − {24} = {1}.")],
    key_words=[("quadratic formula", "x = (−b ± √(b² − {4}ac)) / {2}a"),
               ("discriminant", "b² − {4}ac, the number under the square root"),
               ("derive", "show where a formula comes from, step by step")],
    examples=["{quad(1, 3, -4)} = {0}: a = {1}, b = {3}, c = {-4}, discriminant {9} + {16} = {25}", "{quad(2, -1, -6)} = {0}: discriminant {1} + {48} = {49}"],
    mistake=("{quad(1, -5, 6)} = {0}: b = {5}", "b = {-5}",
             "The sign in front of a term belongs to its coefficient. Here −b = {5} in the formula.")))

# ---------------------------------------------------------------- 10. Using the quadratic formula
L.lesson(D, S, 10, ("m4-10", "Solve quadratic equations using the quadratic formula"), [9],
  "The quadratic formula solves any quadratic equation ax² + bx + c = 0:\n"
  "x = (−b ± √(b² − 4ac)) / 2a.\n"
  "Steps: rearrange to ax² + bx + c = 0; write down a, b, c with signs; work out b² − 4ac; take its square root; "
  "work out the two roots, one with + and one with −; round at the end.\n"
  "Example: 2x² + 3x − 4 = 0: b² − 4ac = 9 + 32 = 41, so x = (−3 ± √41)/4, x ≈ 0.85 or x ≈ −2.35.\n"
  "Divide the whole top by 2a, not just the square root.",
  worked({"a": 2, "b": 3, "c": -4},
         "Solve {quad(a, b, c)} = {0}, giving the roots to {2} decimal places.",
         ["a = {a}, b = {b}, c = {c}.",
          "b² − {4}ac = {b * b} − {4} × {a} × {br(c)} = {b * b - 4 * a * c}; √{b * b - 4 * a * c} ≈ {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}.",
          "x = ({-b} + {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}) / {2 * a} ≈ {roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)}.",
          "x = ({-b} − {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}) / {2 * a} ≈ {roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)}."],
         "x ≈ {roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)} or x ≈ {roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)}",
         checks=["b * b - 4 * a * c == 41"]),
  [card("c4m10-1", "When b² − {4}ac is a square number, the roots are exact.",
        ["{quad(1, -2, -15)} = {0}: b² − {4}ac = {64}, √{64} = {8}, x = ({2} ± {8})/{2} = {5} or {-3}"], "m4-10-exact"),
   card("c4m10-2", "Otherwise use a calculator for the square root and round only at the end.",
        ["{quad(1, 4, 1)} = {0}: x = ({-4} ± √{12})/{2} ≈ {roundTo((-4 + sqrt(12)) / 2, 0.01)} or {roundTo((-4 - sqrt(12)) / 2, 0.01)}"], "m4-10-dp"),
   card("c4m10-3", "Divide the whole top by {2}a, not only the square root.",
        ["({-4} + √{12})/{2} = {-2} + √{3}, not {-4} + √{12}/{2}"], "m4-10-small")],
  [num("m4-10-exact", 1, "Use the quadratic formula to solve {quad(1, -(p + q), p * q)} = {0}. Give the larger root.",
       "max(p, q)",
       ["b² − {4}ac = {(p + q) * (p + q)} − {4 * p * q} = {(p - q) * (p - q)}, and its square root is {abs(p - q)}.",
        "x = ({p + q} ± {abs(p - q)}) / {2}.", "The larger root is ({p + q} + {abs(p - q)}) / {2} = {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("nohalf", "p + q + abs(p - q)", "Divide the whole top by {2}a = {2}: ({p + q} + {abs(p - q)}) / {2}."),
             ("minusb", "max(-p, -q)", "−b = {p + q}, not {-(p + q)}: the sign of b changes.")],
       sources=SRC, where=["p != q", "p + q != 0", "p * q != 0", "max(-p, -q) != max(p, q)"], signed=True),
   num("m4-10-dp", 1, "Solve {quad(a, b, c)} = {0}. Give the larger root to {2} decimal places.",
       "roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)",
       ["b² − {4}ac = {b * b - 4 * a * c}.", "x = ({-b} + √{b * b - 4 * a * c}) / {2 * a}.", "x ≈ {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("plusb", "roundTo((b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)", "The formula starts with −b = {-b}."),
             ("rootonly", "roundTo(-b + sqrt(b * b - 4 * a * c) / (2 * a), 0.01)", "Divide the whole top, ({-b} + √{b * b - 4 * a * c}), by {2 * a}."),
             ("ona", "roundTo((-b + sqrt(b * b - 4 * a * c)) / a, 0.01)", "Divide by {2}a = {2 * a}, not by a.")],
       sources=SRC, where=["b != 0 && c != 0", "b * b - 4 * a * c > 0", "!isPerfectSquare(b * b - 4 * a * c)", not_half("(-b + sqrt(b * b - 4 * a * c)) / (2 * a)")], signed=True),
   num("m4-10-small", 2, "Solve {quad(a, b, c)} = {0}. Give the smaller root to {2} decimal places.",
       "roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)",
       ["b² − {4}ac = {b * b - 4 * a * c}.", "The smaller root uses −: x = ({-b} − √{b * b - 4 * a * c}) / {2 * a}.", "x ≈ {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("big", "roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)", "That is the larger root (with +). The smaller one uses −."),
             ("plusb", "roundTo((b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)", "The formula starts with −b = {-b}."),
             ("ona", "roundTo((-b - sqrt(b * b - 4 * a * c)) / a, 0.01)", "Divide by {2}a = {2 * a}, not by a.")],
       sources=SRC, where=["b != 0 && c != 0", "b * b - 4 * a * c > 0", "!isPerfectSquare(b * b - 4 * a * c)", not_half("(-b - sqrt(b * b - 4 * a * c)) / (2 * a)")], signed=True),
   num("m4-10-rearrange", 2, "Solve x({poly([1, 'x'], [b, ''])}) = {k}. Give the positive root to {2} decimal places.",
       "roundTo((-b + sqrt(b * b + 4 * k)) / 2, 0.01)",
       ["Expand and make one side {0}: {quad(1, b, -k)} = {0}.", "a = {1}, b = {b}, c = {-k}: b² − {4}ac = {b * b + 4 * k}.",
        "x = ({-b} + √{b * b + 4 * k}) / {2} ≈ {answer}."],
       vars={"b": {"int": [-7, 7]}, "k": {"int": [2, 20]}},
       misc=[("csign", "roundTo((-b + sqrt(b * b - 4 * k)) / 2, 0.01)", "Moving {k} to the left makes c = {-k}, so −{4}ac = +{4 * k}.", "b * b - 4 * k > 0")],
       sources=SRC, where=["b != 0", "!isPerfectSquare(b * b + 4 * k)", not_half("(-b + sqrt(b * b + 4 * k)) / 2")]),
   num("m4-10-word", 3, "A ball is thrown up from a cliff. After t seconds its height above the sea is h = {u}t − {5}t² + {s} metres. Use the quadratic formula to find when it reaches the sea (h = {0}). Give t to {2} decimal places.",
       "roundTo((u + sqrt(u * u + 20 * s)) / 10, 0.01)",
       ["Set h = {0}: {quad(-5, u, s, 't')} = {0}, or {quad(5, -u, -s, 't')} = {0}.",
        "a = {5}, b = {-u}, c = {-s}: b² − {4}ac = {u * u} + {20 * s} = {u * u + 20 * s}.",
        "t = ({u} ± √{u * u + 20 * s}) / {10}. Time cannot be negative, so take +.", "t ≈ {answer} s."],
       vars={"u": {"int": [5, 20]}, "s": {"int": [10, 60]}},
       misc=[("neg", "roundTo((u - sqrt(u * u + 20 * s)) / 10, 0.01)", "That root is negative: the ball cannot reach the sea before it is thrown."),
             ("five", "roundTo((u + sqrt(u * u + 20 * s)) / 5, 0.01)", "Divide by {2}a = {10}, not by {5}.")],
       sources=SRC, unit="s", where=["!isPerfectSquare(u * u + 20 * s)", not_half("(u + sqrt(u * u + 20 * s)) / 10")])],
  learn=learn(
    [goal("solve any quadratic equation with the formula, giving exact roots or roots to {2} decimal places.",
          "Lesson {9} (where the formula comes from) and Lesson {7} (rearranging and rejecting roots).",
          "the discriminant and the nature of roots, and solving word problems in physics and business."),
     ("The method",
      "Solve {quad(2, 3, -4)} = {0}.\n"
      "• a = {2}, b = {3}, c = {-4}.\n"
      "• b² − {4}ac = {9} − {4} × {2} × {br(-4)} = {9} + {32} = {41}.\n"
      "• x = ({-3} ± √{41}) / {4}.\n"
      "• √{41} ≈ {roundTo(sqrt(41), 0.0001)}, so x ≈ ({-3} + {roundTo(sqrt(41), 0.0001)})/{4} ≈ {roundTo((-3 + sqrt(41)) / 4, 0.01)} or x ≈ ({-3} − {roundTo(sqrt(41), 0.0001)})/{4} ≈ {roundTo((-3 - sqrt(41)) / 4, 0.01)}.\n"
      "Keep all the calculator digits until the last step, then round."),
     ("Traps to avoid",
      "• −b changes the sign of b: if b = {-6}, then −b = {6}.\n"
      "• −{4}ac with a negative c becomes a plus: c = {-4} gives −{4} × {2} × {br(-4)} = +{32}.\n"
      "• The whole top is divided by {2}a: ({-3} + √{41})/{4}, not {-3} + √{41}/{4}.\n"
      "• Rearrange first: x(x + {3}) = {5} is {quad(1, 3, -5)} = {0}, so c = {-5}.\n"
      "If b² − {4}ac is negative there are no real roots: the calculator gives an error for the square root.")],
    key_words=[("quadratic formula", "x = (−b ± √(b² − {4}ac)) / {2}a"),
               ("decimal places", "digits after the decimal point; {2} d.p. means hundredths"),
               ("exact", "left as a surd or fraction, not rounded")],
    examples=["{quad(1, -6, 4)} = {0} → x = {3} ± √{5} ≈ {roundTo(3 + sqrt(5), 0.01)} or {roundTo(3 - sqrt(5), 0.01)}", "{quad(1, -1, -6)} = {0} → x = ({1} ± {5})/{2} = {3} or {-2}"],
    mistake=("x = {-3} + √{41}/{4}", "x = ({-3} + √{41})/{4}",
             "The fraction line goes under the whole top. Work out {-3} + √{41} first, then divide by {4}.")))

# ---------------------------------------------------------------- 11. Developing quadratic equations from the roots
L.lesson(D, S, 11, ("m4-11", "Form a quadratic equation from its roots; sum and product of roots"), [7, 10],
  "If the roots are p and q, the equation is (x − p)(x − q) = 0, that is x² − (p + q)x + pq = 0.\n"
  "In words: x² − (sum of roots)x + (product of roots) = 0.\n"
  "Example: roots 3 and −5: sum −2, product −15, so x² + 2x − 15 = 0.\n"
  "Fractions: roots ½ and 3 give (2x − 1)(x − 3) = 0, that is 2x² − 7x + 3 = 0.\n"
  "For ax² + bx + c = 0, the sum of the roots is −b/a and the product is c/a. "
  "Then α² + β² = (α + β)² − 2αβ, without finding the roots.",
  worked({"p": 3, "q": -5},
         "Form the quadratic equation whose roots are {p} and {q}.",
         ["Sum of the roots: {p} + {br(q)} = {p + q}.", "Product of the roots: {p} × {br(q)} = {p * q}.",
          "x² − (sum)x + (product) = {0}.", "Check: {lin2(1, -p, 1, -q)} = {quad(1, -(p + q), p * q)}."],
         "{quad(1, -(p + q), p * q)} = {0}",
         checks=["p + q == -2", "p * q == -15"]),
  [card("c4m11-1", "Roots p and q come from the brackets (x − p)(x − q): the sign inside each bracket is opposite to the root.",
        ["roots {4} and {-2}: {lin2(1, -4, 1, 2)} = {0}"], "m4-11-form"),
   card("c4m11-2", "x² − (sum of roots)x + (product of roots) = {0}.",
        ["roots {4} and {-2}: sum {2}, product {-8}: {quad(1, -2, -8)} = {0}"], "m4-11-sum"),
   card("c4m11-3", "For ax² + bx + c = {0}: sum of roots = −b/a, product = c/a.",
        ["{quad(2, -6, 4)} = {0}: sum = {6}/{2} = {3}, product = {4}/{2} = {2}"], "m4-11-prod")],
  [mcq("m4-11-form", 1, "Which equation has roots {p} and {q}?",
       "{quad(1, -(p + q), p * q)} = {0}",
       [("{quad(1, p + q, p * q)} = {0}", "sign"), ("{quad(1, -(p + q), -p * q)} = {0}", "prod"), ("{quad(1, -p * q, p + q)} = {0}", "swap")],
       ["Sum = {p + q}, product = {p * q}.", "x² − (sum)x + (product) = {0}.", "So the answer is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sign", "The x term is minus the sum: −({p + q})x. Check: x = {p} must make it {0}."),
             ("prod", "The number term is the product {p} × {br(q)} = {p * q}."),
             ("swap", "The x coefficient comes from the sum and the number from the product, not the other way round.")],
       sources=SRC, where=["p != q", "p != 0 && q != 0", "p + q != 0", "p * q != p + q", "p * q != -(p + q)"]),
   num("m4-11-sum", 1, "What is the sum of the roots of {quad(1, b, c)} = {0}?",
       "-b",
       ["For x² + bx + c = {0} the sum of the roots is −b.", "Here b = {b}, so the sum is {answer}."],
       vars={"b": {"int": [-12, 12]}, "c": {"int": [-12, 12]}},
       misc=[("b", "b", "The equation is x² − (sum)x + product, so sum = −b = {-b}."),
             ("c", "c", "{c} is the product of the roots. The sum is −b = {-b}.")],
       sources=SRC, where=["b != 0 && c != 0", "b != c && -b != c"], signed=True),
   num("m4-11-prod", 2, "What is the product of the roots of {quad(a, b, a * k)} = {0}?",
       "k",
       ["Divide by a = {a}: product = c/a = {a * k}/{a}.", "So the product is {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [-9, 9]}, "k": {"int": [-6, 6]}},
       misc=[("c", "a * k", "Divide c by a: {a * k} ÷ {a} = {k}."),
             ("neg", "-k", "The product is +c/a = {k}; only the sum has the minus sign."),
             ("sum", "-b / a", "That is the sum of the roots. The product is c/a.")],
       sources=SRC, where=["b != 0 && k != 0", "k != -k", "b % a != 0 || -b / a != k"], signed=True),
   mcq("m4-11-frac", 2, "Which equation with whole-number coefficients has roots {frac(1, d)} and {q}?",
       "{quad(d, -(1 + d * q), q)} = {0}",
       [("{quad(1, -(1 + d * q), q)} = {0}", "noa"), ("{quad(d, 1 + d * q, q)} = {0}", "sign"), ("{quad(d, -(1 + q), q)} = {0}", "mid")],
       ["x = {frac(1, d)} comes from {mono(d, 'x')} − {1} = {0}; x = {q} from x − {br(q)} = {0}.",
        "({poly([d, 'x'], [-1, ''])})({poly([1, 'x'], [-q, ''])}) = {quad(d, -(1 + d * q), q)}.", "So the answer is {answer}."],
       vars={"d": {"int": [2, 5]}, "q": {"int": [-6, 6]}},
       misc=[("noa", "Expand ({poly([d, 'x'], [-1, ''])})({poly([1, 'x'], [-q, ''])}): the x² term is {mono(d, 'x²')}."),
             ("sign", "Put x = {q} in: the equation must give {0}. The middle term needs a minus sign."),
             ("mid", "The middle term is {mono(d, 'x')} × {br(-q)} + {br(-1)} × x = {mono(-(1 + d * q), 'x')}.")],
       sources=SRC, where=["q != 0", "1 + d * q != 0", "1 + q != 1 + d * q", "-(1 + q) != 1 + d * q"]),
   num("m4-11-sym", 3, "α and β are the roots of {quad(1, b, c)} = {0}. Without solving, find α² + β².",
       "b * b - 2 * c",
       ["α + β = −b = {-b} and αβ = c = {c}.", "α² + β² = (α + β)² − {2}αβ = {b * b} − {2} × {br(c)}.", "= {answer}."],
       vars={"b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("sq", "b * b", "(α + β)² also contains {2}αβ: subtract it. α² + β² = {b * b} − {2 * c}."),
             ("plus", "b * b + 2 * c", "(α + β)² = α² + {2}αβ + β², so α² + β² = (α + β)² minus {2}αβ."),
             ("once", "b * b - c", "Subtract {2}αβ = {2 * c}, not just αβ.")],
       sources=SRC, where=["b != 0 && c != 0", "b * b - 2 * c != b * b - c"], signed=True)],
  learn=learn(
    [goal("write the equation that has two given roots, and find the sum, the product and expressions such as α² + β² without solving.",
          "Lesson {7} (roots from factors) and Lesson {10} (the formula).",
          "checking answers to quadratic equations quickly and, in Form Five, harder problems on roots."),
     ("From roots back to the equation",
      "Solving goes from the equation to the roots. Here we go backwards.\n"
      "If x = {3} is a root, then x − {3} is a factor. If x = {-5} is a root, then x + {5} is a factor.\n"
      "So the equation with roots {3} and {-5} is {lin2(1, -3, 1, 5)} = {0}, that is {quad(1, 2, -15)} = {0}.\n"
      "Pattern: x² − (sum of roots)x + (product of roots) = {0}. Sum {-2}, product {-15}: x² − ({-2})x + ({-15}) = {quad(1, 2, -15)}.\n"
      "For a fractional root such as {frac(1, 2)}, use the factor {mono(2, 'x')} − {1} to keep whole numbers."),
     ("Sum and product for any quadratic",
      "Divide ax² + bx + c = {0} by a: x² + (b/a)x + c/a = {0}. Compare with x² − (sum)x + product:\n"
      "• sum of roots α + β = −b/a\n• product αβ = c/a\n"
      "Example: {quad(2, -7, 3)} = {0} has α + β = {frac(7, 2)} and αβ = {frac(3, 2)}.\n"
      "Use these to find other expressions without solving: α² + β² = (α + β)² − {2}αβ = {frac(49, 4)} − {3} = {frac(37, 4)}.")],
    key_words=[("sum of roots", "α + β = −b/a"), ("product of roots", "αβ = c/a"),
               ("α, β", "Greek letters alpha and beta, often used for the two roots")],
    examples=["roots {2} and {7}: {quad(1, -9, 14)} = {0}", "roots {-1} and {-4}: {quad(1, 5, 4)} = {0}", "{quad(1, -3, -10)} = {0}: sum {3}, product {-10}"],
    mistake=("roots {2} and {7}: {quad(1, 9, 14)} = {0}", "{quad(1, -9, 14)} = {0}",
             "Check by putting x = {2} in: {4} + {18} + {14} is not {0}. The x term is minus the sum.")))
