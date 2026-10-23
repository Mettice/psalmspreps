"""Form 4 Maths, Term 1, rows 2-6: expansion and factorisation (spine data/spine/form-4/mathematics.json, numbered by seq).
Run: python tools/authoring/form4/maths_algebra.py
Each lesson opens with "Your goal and connections" (AUTHORING section 3, Form 4 on). Row 1 (first contact and
diagnostic) is not a lesson. Rows 5 and 6 have the same title on the sheet: row 5 is x² + bx + c, row 6 is
ax² + bx + c with a ≠ 1 (TEACHER-REVIEW TR-M4-1)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRC = ["algebra-expand"]
SRCF = ["algebra-factorise"]


def goal(by_the_end, builds_on, leads_to):
    return ("Your goal and connections",
            f"By the end, you should be able to {by_the_end}\nBuilds on: {builds_on}\nLeads to: {leads_to}")


# ---------------------------------------------------------------- 2. Expansion of expressions
L.lesson(D, S, 2, ("m4-2", "Expand products of brackets, including the special products"), [],
  "To expand a product of brackets, multiply every term in one bracket by every term in the other, then collect like terms.\n"
  "• (x + 3)(x + 5) = x² + 5x + 3x + 15 = x² + 8x + 15.\n"
  "• (2x + 3)(x − 4) = 2x² − 8x + 3x − 12 = 2x² − 5x − 12.\n"
  "Three special products are worth knowing by heart:\n"
  "• (a + b)² = a² + 2ab + b²\n"
  "• (a − b)² = a² − 2ab + b²\n"
  "• (a + b)(a − b) = a² − b²\n"
  "A common mistake is (x + 3)² = x² + 9: the middle term 2 × 3 × x = 6x is missing.",
  worked({"a": 2, "b": 3, "c": 1, "d": -4},
         "Expand and simplify {lin2(a, b, c, d)}.",
         ["Multiply each term of the first bracket by each term of the second.",
          "{mono(a, 'x')} × {mono(c, 'x')} = {mono(a * c, 'x²')} and {mono(a, 'x')} × {br(d)} = {mono(a * d, 'x')}.",
          "{b} × {mono(c, 'x')} = {mono(b * c, 'x')} and {b} × {br(d)} = {b * d}.",
          "Collect the x terms: {a * d} + {b * c} = {a * d + b * c}."],
         "{quad(a * c, a * d + b * c, b * d)}",
         checks=["a * c == 2", "a * d + b * c == -5", "b * d == -12"]),
  [card("c4m2-1", "Every term in one bracket multiplies every term in the other. Two terms times two terms make four products.",
        ["{lin2(1, 3, 1, 5)} = {poly([1, 'x²'], [5, 'x'], [3, 'x'], [15, ''])} = {quad(1, 8, 15)}"], "m4-2-xpq"),
   card("c4m2-2", "A square of a bracket is the bracket times itself, so it has a middle term: twice the product of the two terms.",
        ["{lin2(1, 3, 1, 3)} = {quad(1, 6, 9)}, not {quad(1, 0, 9)}"], "m4-2-square"),
   card("c4m2-3", "When the brackets differ only by a sign, the middle terms cancel: the answer is a difference of two squares.",
        ["{lin2(1, 4, 1, -4)} = {quad(1, 4, 0)} − {mono(4, 'x')} − {16} = {quad(1, 0, -16)}"], "m4-2-dos")],
  [mcq("m4-2-xpq", 1, "Expand {lin2(1, p, 1, q)}.",
       "{quad(1, p + q, p * q)}",
       [("{quad(1, 0, p * q)}", "nomid"), ("{quad(1, p + q, p + q)}", "addend"), ("{quad(1, p * q, p + q)}", "swap")],
       ["x × x = x²; x × {br(q)} and {br(p)} × x give {p} + {br(q)} = {p + q} lots of x.", "{br(p)} × {br(q)} = {p * q}.", "So the answer is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("nomid", "Two products are missing: x × {br(q)} and {br(p)} × x. Together they give {mono(p + q, 'x')}."),
             ("addend", "The last term is a product: {br(p)} × {br(q)} = {p * q}, not a sum."),
             ("swap", "The x term comes from adding: {p} + {br(q)} = {p + q}. The number term comes from multiplying: {p * q}.")],
       sources=SRC, where=["p != 0 && q != 0", "p + q != 0", "p * q != p + q", "p != q"]),
   num("m4-2-square", 1, "Expand {lin2(1, a, 1, a)}, that is ({poly([1, 'x'], [a, ''])})². What is the coefficient of x?",
       "2 * a",
       ["({poly([1, 'x'], [a, ''])})² = ({poly([1, 'x'], [a, ''])})({poly([1, 'x'], [a, ''])}).",
        "The two middle products are {br(a)} × x and x × {br(a)}: together {mono(2 * a, 'x')}.", "So the coefficient of x is {answer}."],
       vars={"a": {"int": [-9, 9]}},
       misc=[("once", "a", "There are two middle products, x × {br(a)} and {br(a)} × x: {a} + {br(a)} = {2 * a}."),
             ("square", "a * a", "{a * a} is the number term ({br(a)} × {br(a)}). The x term is {2 * a}x.")],
       sources=SRC, where=["a != 0 && a != 2 && a != -2", "a * a != 2 * a"], signed=True),
   mcq("m4-2-pair", 2, "Expand and simplify {lin2(a, b, c, d)}.",
       "{quad(a * c, a * d + b * c, b * d)}",
       [("{quad(a * c, a * b + c * d, b * d)}", "cross"), ("{quad(a * c, 0, b * d)}", "nomid"), ("{quad(a + c, a * d + b * c, b + d)}", "add")],
       ["{mono(a, 'x')} × {mono(c, 'x')} = {mono(a * c, 'x²')}.",
        "Middle: {mono(a, 'x')} × {br(d)} + {b} × {mono(c, 'x')} = {mono(a * d, 'x')} + {mono(b * c, 'x')} = {mono(a * d + b * c, 'x')}.",
        "Last: {b} × {br(d)} = {b * d}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 5]}, "b": {"int": [1, 9]}, "c": {"int": [1, 4]}, "d": {"int": [-9, 9]}},
       misc=[("cross", "Multiply a term of the first bracket by a term of the second: {mono(a, 'x')} × {br(d)} and {b} × {mono(c, 'x')}."),
             ("nomid", "The two middle products are missing: {mono(a * d, 'x')} and {mono(b * c, 'x')}."),
             ("add", "Terms are multiplied, not added: {mono(a, 'x')} × {mono(c, 'x')} = {mono(a * c, 'x²')} and {b} × {br(d)} = {b * d}.")],
       sources=SRC, where=["d != 0", "a * d + b * c != 0", "a * b + c * d != a * d + b * c", "a + c != a * c", "b + d != b * d"]),
   mcq("m4-2-dos", 2, "Expand {lin2(p, q, p, -q)}.",
       "{quad(p * p, 0, -q * q)}",
       [("{quad(p * p, 0, q * q)}", "plus"), ("{quad(p * p, -2 * p * q, -q * q)}", "mid"), ("{quad(p, 0, -q * q)}", "nosq")],
       ["The middle products are {mono(-p * q, 'x')} and {mono(p * q, 'x')}: they cancel.",
        "First: {mono(p, 'x')} × {mono(p, 'x')} = {mono(p * p, 'x²')}. Last: {q} × {br(-q)} = {-q * q}.", "So the answer is {answer}."],
       vars={"p": {"int": [1, 6]}, "q": {"int": [1, 9]}},
       misc=[("plus", "The last product is {q} × {br(-q)}: a positive times a negative is negative, so {-q * q}."),
             ("mid", "The middle products are {mono(-p * q, 'x')} and {mono(p * q, 'x')}: they cancel to zero."),
             ("nosq", "{mono(p, 'x')} × {mono(p, 'x')} = {mono(p * p, 'x²')}: the {p} is squared too.")],
       sources=SRC, where=["p != 1"]),
   num("m4-2-three", 3, "Expand ({poly([1, 'x'], [a, ''])})({quad(1, b, c)}). What is the coefficient of x?",
       "c + a * b",
       ["The x terms come from x × {br(c)} and {br(a)} × {mono(b, 'x')}.",
        "That gives {mono(c, 'x')} and {mono(a * b, 'x')}.", "So the coefficient of x is {c} + {br(a * b)} = {answer}."],
       vars={"a": {"int": [-6, 6]}, "b": {"int": [-6, 6]}, "c": {"int": [-9, 9]}},
       misc=[("onlyc", "c", "There is a second x term: {br(a)} × {mono(b, 'x')} = {mono(a * b, 'x')}."),
             ("onlyab", "a * b", "There is a second x term: x × {br(c)} = {mono(c, 'x')}."),
             ("x2", "b + a", "{b} + {br(a)} is the coefficient of x². For x add {c} and {a} × {br(b)}.")],
       sources=SRC, where=["a != 0 && b != 0 && c != 0", "c + a * b != 0", "a * b != c + a * b", "b + a != c + a * b", "c != c + a * b"], signed=True)],
  learn=learn(
    [goal("expand any product of two brackets and spot the three special products on sight.",
          "Form Three expansion of a(b + c) and of (x + a)(x + b); collecting like terms.",
          "factorisation (the next lessons undo expansion) and solving quadratic equations."),
     ("Every term times every term",
      "To expand ({poly([2, 'x'], [3, ''])})({poly([1, 'x'], [-4, ''])}), multiply each term of the first bracket by each term of the second.\n"
      "• {mono(2, 'x')} × x = {mono(2, 'x²')}\n• {mono(2, 'x')} × {br(-4)} = {mono(-8, 'x')}\n• {3} × x = {mono(3, 'x')}\n• {3} × {br(-4)} = {-12}\n"
      "Two terms times two terms always make four products. Then collect the like terms: {mono(-8, 'x')} + {mono(3, 'x')} = {mono(-5, 'x')}, "
      "so the answer is {quad(2, -5, -12)}."),
     ("Three special products",
      "Some products appear so often that it is worth knowing them by heart.\n"
      "• (a + b)² = a² + {2}ab + b²: for example ({poly([1, 'x'], [5, ''])})² = {quad(1, 10, 25)}.\n"
      "• (a − b)² = a² − {2}ab + b²: for example ({poly([1, 'x'], [-3, ''])})² = {quad(1, -6, 9)}.\n"
      "• (a + b)(a − b) = a² − b²: for example {lin2(1, 7, 1, -7)} = {quad(1, 0, -49)}.\n"
      "In the last one the middle terms cancel. This is called the difference of two squares, and the next lesson uses it backwards.")],
    key_words=[("expand", "remove the brackets by multiplying every term inside"),
               ("product", "the result of a multiplication"),
               ("perfect square", "a bracket times itself, such as ({poly([1, 'x'], [5, ''])})²"),
               ("difference of two squares", "an expression a² − b², which equals (a + b)(a − b)")],
    examples=["{lin2(1, 2, 1, 6)} = {quad(1, 8, 12)}", "({poly([3, 'x'], [-1, ''])})² = {quad(9, -6, 1)}", "{lin2(2, 5, 2, -5)} = {quad(4, 0, -25)}"],
    mistake=("({poly([1, 'x'], [3, ''])})² = {quad(1, 0, 9)}", "({poly([1, 'x'], [3, ''])})² = {quad(1, 6, 9)}",
             "Squaring a bracket means multiplying it by itself. The two middle products {mono(3, 'x')} + {mono(3, 'x')} give {mono(6, 'x')}.")))

# ---------------------------------------------------------------- 3. Factorisation by grouping and difference of two squares
L.lesson(D, S, 3, ("m4-3", "Factorise by grouping and as a difference of two squares"), [2],
  "Factorising is expanding backwards: write an expression as a product.\n"
  "• Grouping, for four terms: pair them, take a common factor from each pair, then take out the common bracket. "
  "ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y).\n"
  "• Difference of two squares: a² − b² = (a + b)(a − b). For example x² − 49 = (x + 7)(x − 7) and 9x² − 4 = (3x + 2)(3x − 2).\n"
  "Always take out a common number factor first: 2x² − 18 = 2(x² − 9) = 2(x + 3)(x − 3).\n"
  "A sum of two squares, such as x² + 9, does not factorise this way.\n"
  "Check any factorisation by expanding it again.",
  worked({"p": 3, "q": 5},
         "Factorise xy + {p}x + {q}y + {p * q}.",
         ["Group the terms in pairs: (xy + {mono(p, 'x')}) + ({mono(q, 'y')} + {p * q}).",
          "Take x out of the first pair and {q} out of the second: x({poly([1, 'y'], [p, ''])}) + {q}({poly([1, 'y'], [p, ''])}).",
          "The bracket ({poly([1, 'y'], [p, ''])}) is common to both: take it out.",
          "Check: ({poly([1, 'x'], [q, ''])})({poly([1, 'y'], [p, ''])}) = xy + {mono(p, 'x')} + {mono(q, 'y')} + {p * q}."],
         "({poly([1, 'x'], [q, ''])})({poly([1, 'y'], [p, ''])})",
         checks=["p * q == 15"]),
  [card("c4m3-1", "Grouping: pair the four terms, take a common factor out of each pair, then take out the bracket they share.",
        ["{mono(1, 'ax')} + {mono(1, 'ay')} + {mono(2, 'x')} + {mono(2, 'y')} = a(x + y) + {2}(x + y) = (a + {2})(x + y)"], "m4-3-group"),
   card("c4m3-2", "A difference of two squares factorises as (first + second)(first − second), where first and second are the square roots.",
        ["{quad(1, 0, -36)} = {lin2(1, 6, 1, -6)}", "{quad(25, 0, -1)} = {lin2(5, 1, 5, -1)}"], "m4-3-dos"),
   card("c4m3-3", "Look for a common number factor first. What is left is often a difference of two squares.",
        ["{quad(3, 0, -12)} = {3}({quad(1, 0, -4)}) = {3}{lin2(1, 2, 1, -2)}"], "m4-3-common")],
  [mcq("m4-3-dos", 1, "Factorise {quad(1, 0, -a * a)}.",
       "{lin2(1, a, 1, -a)}",
       [("({poly([1, 'x'], [-a, ''])})²", "square"), ("{lin2(1, a * a, 1, -1)}", "noroot"), ("x({poly([1, 'x'], [-a * a, ''])})", "commonx")],
       ["{a * a} = {a}², so {quad(1, 0, -a * a)} = x² − {a}².", "a² − b² = (a + b)(a − b).", "So the answer is {answer}."],
       vars={"a": {"int": [2, 12]}},
       misc=[("square", "({poly([1, 'x'], [-a, ''])})² = {quad(1, -2 * a, a * a)}: it has a middle term and a plus sign at the end."),
             ("noroot", "Use the square root of {a * a}, which is {a}: {lin2(1, a, 1, -a)}."),
             ("commonx", "{a * a} has no x, so x is not a common factor.")],
       sources=SRCF),
   mcq("m4-3-group", 1, "Factorise {mono(1, 'ax')} + {mono(p, 'a')} + {mono(q, 'x')} + {p * q}.",
       "({poly([1, 'a'], [q, ''])})({poly([1, 'x'], [p, ''])})",
       [("({poly([1, 'a'], [p, ''])})({poly([1, 'x'], [q, ''])})", "swap"), ("a({poly([1, 'x'], [p, ''])}) + {q}", "half"), ("({poly([1, 'a'], [q, ''])})({poly([1, 'x'], [p * q, ''])})", "keep")],
       ["Group: a(x + {p}) + {q}(x + {p}).", "Take out the common bracket (x + {p}).", "So the answer is {answer}."],
       vars={"p": {"int": [2, 9]}, "q": {"int": [2, 9]}},
       misc=[("swap", "Expand it: (a + {p})(x + {q}) gives {mono(q, 'a')} + {mono(p, 'x')}, not {mono(p, 'a')} + {mono(q, 'x')}."),
             ("half", "That is only part way: {q}(x + {p}) also has the bracket (x + {p}), so take it out of both."),
             ("keep", "Taking {q} out of {mono(q, 'x')} + {p * q} leaves x + {p}, not x + {p * q}.")],
       sources=SRCF, where=["p != q"]),
   mcq("m4-3-squares", 2, "Factorise {quad(a * a, 0, -b * b)}.",
       "{lin2(a, b, a, -b)}",
       [("{lin2(a * a, b, 1, -b)}", "half"), ("{lin2(a, b * b, a, -1)}", "noroot"), ("{lin2(a, b, a, b)}", "signs")],
       ["{mono(a * a, 'x²')} = ({mono(a, 'x')})² and {b * b} = {b}².", "a² − b² = (a + b)(a − b) with a = {mono(a, 'x')} and b = {b}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 7]}, "b": {"int": [1, 9]}},
       misc=[("half", "Take the square root of the whole term {mono(a * a, 'x²')}: it is {mono(a, 'x')}, in both brackets."),
             ("noroot", "Use {b}, the square root of {b * b}, in both brackets."),
             ("signs", "{lin2(a, b, a, b)} = ({poly([a, 'x'], [b, ''])})², which ends with +{b * b}. One bracket needs a minus sign.")],
       sources=SRCF, where=["hcf(a, b) == 1"]),
   mcq("m4-3-common", 2, "Factorise completely {quad(k, 0, -k * a * a)}.",
       "{k}{lin2(1, a, 1, -a)}",
       [("{k}({quad(1, 0, -a * a)})", "stop"), ("{lin2(k, a, 1, -a)}", "onebr"), ("{k}({poly([1, 'x'], [-a, ''])})²", "square")],
       ["Take out the common factor {k}: {k}({quad(1, 0, -a * a)}).", "x² − {a * a} is a difference of two squares: {lin2(1, a, 1, -a)}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 7]}, "a": {"int": [2, 9]}},
       misc=[("stop", "'Completely' means keep going: x² − {a * a} still factorises as {lin2(1, a, 1, -a)}."),
             ("onebr", "Expand it: {lin2(k, a, 1, -a)} has a middle term. Take {k} out in front instead."),
             ("square", "{k}({poly([1, 'x'], [-a, ''])})² = {k}({quad(1, -2 * a, a * a)}): that has a middle term.")],
       sources=SRCF),
   num("m4-3-calc", 3, "Use a difference of two squares to calculate {n}² − {m}² without squaring the large numbers.",
       "(n + m) * (n - m)",
       ["{n}² − {m}² = ({n} + {m})({n} − {m}).", "= {n + m} × {n - m}.", "= {answer}."],
       vars={"n": {"int": [51, 99]}, "d": {"int": [1, 9]}, "m": {"expr": "n - d"}},
       misc=[("diffsq", "(n - m) * (n - m)", "a² − b² is not (a − b)². Use ({n} + {m})({n} − {m})."),
             ("sub", "n - m", "{n}² − {m}² is not {n} − {m}. Multiply the sum by the difference: {n + m} × {n - m}.")],
       sources=SRCF, where=["d > 1"])],
  learn=learn(
    [goal("factorise four-term expressions by grouping and any difference of two squares, taking out common factors first.",
          "Lesson {2} (expansion and the product (a + b)(a − b)); Form Three common factors.",
          "factorising quadratic trinomials and solving quadratic equations by factorisation."),
     ("Grouping four terms",
      "Some expressions have four terms and no factor common to all of them, such as xy + {mono(3, 'x')} + {mono(5, 'y')} + {15}.\n"
      "• Pair the terms: (xy + {mono(3, 'x')}) + ({mono(5, 'y')} + {15}).\n"
      "• Take a factor out of each pair: x(y + {3}) + {5}(y + {3}).\n"
      "• Both parts now share the bracket (y + {3}). Take it out: (x + {5})(y + {3}).\n"
      "If the brackets do not match, try pairing the terms differently. Expand your answer to check it."),
     ("The difference of two squares",
      "Lesson {2} showed that (a + b)(a − b) = a² − b². Read backwards, this factorises any difference of two squares.\n"
      "• {quad(1, 0, -64)} = x² − {8}² = {lin2(1, 8, 1, -8)}\n"
      "• {quad(9, 0, -4)} = ({mono(3, 'x')})² − {2}² = {lin2(3, 2, 3, -2)}\n"
      "Always look for a common factor first: {quad(5, 0, -45)} = {5}({quad(1, 0, -9)}) = {5}{lin2(1, 3, 1, -3)}.\n"
      "A sum such as {quad(1, 0, 9)} has no factors of this kind.")],
    key_words=[("factorise", "write an expression as a product of factors"),
               ("common factor", "a number or letter that divides every term"),
               ("grouping", "pairing terms so that each pair has a common factor and the pairs share a bracket"),
               ("factorise completely", "go on until no factor can be split further")],
    examples=["{quad(1, 0, -100)} = {lin2(1, 10, 1, -10)}", "{mono(1, 'ab')} + {mono(4, 'a')} + {mono(2, 'b')} + {8} = (a + {2})(b + {4})", "{quad(2, 0, -50)} = {2}{lin2(1, 5, 1, -5)}"],
    mistake=("{quad(1, 0, -25)} = ({poly([1, 'x'], [-5, ''])})²", "{quad(1, 0, -25)} = {lin2(1, 5, 1, -5)}",
             "({poly([1, 'x'], [-5, ''])})² expands to {quad(1, -10, 25)}. A difference of two squares needs one plus and one minus bracket.")))

# ---------------------------------------------------------------- 4. Sum and difference of two cubes
L.lesson(D, S, 4, ("m4-4", "Use the identities for the sum and the difference of two cubes"), [2, 3],
  "Two identities factorise a sum or a difference of two cubes:\n"
  "• a³ + b³ = (a + b)(a² − ab + b²)\n"
  "• a³ − b³ = (a − b)(a² + ab + b²)\n"
  "Write each term as a cube first: 8 = 2³, 27x³ = (3x)³.\n"
  "For example x³ − 8 = (x − 2)(x² + 2x + 4) and 27x³ + 1 = (3x + 1)(9x² − 3x + 1).\n"
  "Sign rule: the small bracket has the same sign as the expression; the middle term of the long bracket has the opposite sign; the last term is always +.\n"
  "The long bracket does not factorise further. Check by expanding.",
  worked({"a": 2},
         "Factorise {poly([1, 'x³'], [-a ^ 3, ''])}.",
         ["Write each term as a cube: x³ and {a ^ 3} = {a}³.",
          "Use a³ − b³ = (a − b)(a² + ab + b²) with a = x and b = {a}.",
          "a² = x², ab = {mono(a, 'x')}, b² = {a * a}.",
          "Check: x × ({quad(1, a, a * a)}) − {a} × ({quad(1, a, a * a)}) = {poly([1, 'x³'], [-a ^ 3, ''])}."],
         "({poly([1, 'x'], [-a, ''])})({quad(1, a, a * a)})",
         checks=["a ^ 3 == 8"]),
  [card("c4m4-1", "Before using an identity, write each term as a cube: {8} = {2}³, {64} = {4}³, {mono(27, 'x³')} = ({mono(3, 'x')})³.",
        ["{125} = {5}³ and {mono(8, 'x³')} = ({mono(2, 'x')})³"], "m4-4-cube"),
   card("c4m4-2", "Difference of two cubes: a³ − b³ = (a − b)(a² + ab + b²).",
        ["{poly([1, 'x³'], [-27, ''])} = ({poly([1, 'x'], [-3, ''])})({quad(1, 3, 9)})"], "m4-4-diff"),
   card("c4m4-3", "Sum of two cubes: a³ + b³ = (a + b)(a² − ab + b²). Only the small bracket keeps the + sign.",
        ["{poly([1, 'x³'], [64, ''])} = ({poly([1, 'x'], [4, ''])})({quad(1, -4, 16)})"], "m4-4-sum")],
  [num("m4-4-cube", 1, "{n} is a cube number. It is the cube of which whole number?",
       "a",
       ["Try whole numbers: {a} × {a} × {a} = {n}.", "So {n} = {a}³ and the answer is {answer}."],
       vars={"a": {"int": [2, 10]}, "n": {"expr": "a ^ 3"}},
       misc=[("third", "n / 3", "Cubing is not multiplying by {3}: {a}³ = {a} × {a} × {a}."),
             ("square", "sqrtFloor(n)", "That is near the square root. The cube root of {n} is {a}, because {a} × {a} × {a} = {n}.")],
       sources=SRCF),
   mcq("m4-4-diff", 1, "Factorise {poly([1, 'x³'], [-a ^ 3, ''])}.",
       "({poly([1, 'x'], [-a, ''])})({quad(1, a, a * a)})",
       [("({poly([1, 'x'], [-a, ''])})({quad(1, -a, a * a)})", "midsign"), ("({poly([1, 'x'], [a, ''])})({quad(1, -a, a * a)})", "sum"), ("({poly([1, 'x'], [-a, ''])})³", "cube")],
       ["{a ^ 3} = {a}³, so use a³ − b³ = (a − b)(a² + ab + b²).", "a = x, b = {a}: a² = x², ab = {mono(a, 'x')}, b² = {a * a}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 6]}},
       misc=[("midsign", "For a difference of cubes the long bracket is all plus: a² + ab + b²."),
             ("sum", "That is the factorisation of x³ + {a ^ 3}, a sum. Here there is a minus sign."),
             ("cube", "({poly([1, 'x'], [-a, ''])})³ expands to four terms with x² and x terms. It is not x³ − {a ^ 3}.")],
       sources=SRCF),
   mcq("m4-4-sum", 2, "Factorise {poly([k ^ 3, 'x³'], [1, ''])}.",
       "({poly([k, 'x'], [1, ''])})({quad(k * k, -k, 1)})",
       [("({poly([k, 'x'], [1, ''])})({quad(k * k, k, 1)})", "midsign"), ("({poly([k, 'x'], [1, ''])})({quad(k, -k, 1)})", "nosq"), ("({poly([k ^ 3, 'x'], [1, ''])})({quad(1, -1, 1)})", "nocube")],
       ["{mono(k ^ 3, 'x³')} = ({mono(k, 'x')})³ and {1} = {1}³.", "a³ + b³ = (a + b)(a² − ab + b²) with a = {mono(k, 'x')}, b = {1}.",
        "a² = {mono(k * k, 'x²')}, ab = {mono(k, 'x')}, b² = {1}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 5]}},
       misc=[("midsign", "For a sum of cubes the middle term of the long bracket is minus: a² − ab + b²."),
             ("nosq", "a² = ({mono(k, 'x')})² = {mono(k * k, 'x²')}: square the {k} too."),
             ("nocube", "First write {mono(k ^ 3, 'x³')} as a cube: ({mono(k, 'x')})³. Then a = {mono(k, 'x')}.")],
       sources=SRCF),
   mcq("m4-4-which", 2, "Which identity factorises {poly([1, 'x³'], [s * a ^ 3, ''])}?",
       "{s > 0 ? 'a³ + b³ = (a + b)(a² − ab + b²)' : 'a³ − b³ = (a − b)(a² + ab + b²)'}",
       [("{s > 0 ? 'a³ + b³ = (a + b)(a² + ab + b²)' : 'a³ − b³ = (a − b)(a² − ab + b²)'}", "mid"),
        ("{s > 0 ? 'a³ + b³ = (a + b)³' : 'a³ − b³ = (a − b)³'}", "cube"),
        ("a² − b² = (a + b)(a − b)", "squares")],
       ["{a ^ 3} = {a}³, so the expression is {s > 0 ? 'a sum' : 'a difference'} of two cubes.",
        "The small bracket keeps the sign; the middle of the long bracket has the opposite sign.", "So the answer is: {answer}."],
       vars={"a": {"int": [2, 6]}, "s": {"pick": [1, -1]}},
       misc=[("mid", "The middle term of the long bracket has the opposite sign to the small bracket."),
             ("cube", "(a ± b)³ expands to four terms. It is not a³ ± b³."),
             ("squares", "That identity is for squares. x³ and {a ^ 3} = {a}³ are cubes.")],
       sources=SRCF),
   num("m4-4-value", 3, "Given that a + b = {s} and ab = {p}, use a³ + b³ = (a + b)(a² − ab + b²) to find a³ + b³. (Hint: a² + b² = (a + b)² − {2}ab.)",
       "s * (s * s - 3 * p)",
       ["a² + b² = (a + b)² − {2}ab = {s * s} − {2 * p} = {s * s - 2 * p}.",
        "a² − ab + b² = {s * s - 2 * p} − {p} = {s * s - 3 * p}.", "a³ + b³ = {s} × {s * s - 3 * p} = {answer}."],
       vars={"s": {"int": [3, 9]}, "p": {"int": [1, 8]}},
       misc=[("cube", "s ^ 3", "(a + b)³ is not a³ + b³: it also has the terms {3}a²b + {3}ab²."),
             ("noab", "s * (s * s - 2 * p)", "That is (a + b)(a² + b²). The long bracket is a² − ab + b²: subtract ab = {p} once more."),
             ("plusab", "s * (s * s - p)", "a² + b² is (a + b)² − {2}ab, not (a + b)²; then subtract ab.")],
       sources=SRCF, where=["s * s - 3 * p > 0"])],
  learn=learn(
    [goal("factorise a sum or a difference of two cubes with the right signs, and check by expanding.",
          "Lesson {3} (difference of two squares); Form Three cubes and cube roots.",
          "factorising cubic polynomials with the factor theorem and solving cubic equations."),
     ("Two identities",
      "A cube is a number times itself three times: {2}³ = {8}, ({mono(3, 'x')})³ = {mono(27, 'x³')}.\n"
      "Expand (a − b)(a² + ab + b²): a³ + a²b + ab² − a²b − ab² − b³. Four terms cancel, leaving a³ − b³.\n"
      "So:\n• a³ − b³ = (a − b)(a² + ab + b²)\n• a³ + b³ = (a + b)(a² − ab + b²)\n"
      "Sign rule: the small bracket has the same sign as the expression. The middle term of the long bracket has the opposite sign. "
      "The last term is always plus."),
     ("Using them",
      "First write each term as a cube, then read off a and b.\n"
      "• {poly([1, 'x³'], [-125, ''])}: a = x, b = {5}, so ({poly([1, 'x'], [-5, ''])})({quad(1, 5, 25)}).\n"
      "• {poly([8, 'x³'], [27, ''])}: a = {mono(2, 'x')}, b = {3}, so ({poly([2, 'x'], [3, ''])})({quad(4, -6, 9)}).\n"
      "The long bracket never factorises further with whole numbers. Take out a common factor first if there is one: "
      "{poly([2, 'x³'], [-16, ''])} = {2}({poly([1, 'x³'], [-8, ''])}).")],
    key_words=[("cube", "a number multiplied by itself three times, such as {4}³ = {64}"),
               ("cube root", "the number whose cube is given: the cube root of {64} is {4}"),
               ("identity", "an equation that is true for every value of the letters")],
    examples=["{poly([1, 'x³'], [1, ''])} = ({poly([1, 'x'], [1, ''])})({quad(1, -1, 1)})", "{poly([1, 'x³'], [-64, ''])} = ({poly([1, 'x'], [-4, ''])})({quad(1, 4, 16)})"],
    mistake=("{poly([1, 'x³'], [-8, ''])} = ({poly([1, 'x'], [-2, ''])})³", "{poly([1, 'x³'], [-8, ''])} = ({poly([1, 'x'], [-2, ''])})({quad(1, 2, 4)})",
             "({poly([1, 'x'], [-2, ''])})³ = {poly([1, 'x³'], [-6, 'x²'], [12, 'x'], [-8, ''])}. A difference of cubes needs the long bracket.")))

# ---------------------------------------------------------------- 5. Quadratic trinomials x² + bx + c
L.lesson(D, S, 5, ("m4-5", "Factorise quadratic trinomials x² + bx + c"), [2, 3],
  "To factorise x² + bx + c, find two numbers that multiply to c and add to b. Then x² + bx + c = (x + p)(x + q).\n"
  "• x² + 7x + 12: 3 × 4 = 12 and 3 + 4 = 7, so (x + 3)(x + 4).\n"
  "• x² − 2x − 15: −5 × 3 = −15 and −5 + 3 = −2, so (x − 5)(x + 3).\n"
  "Signs: if c is positive, both numbers have the sign of b. If c is negative, the numbers have opposite signs and the larger one has the sign of b.\n"
  "Check by expanding: the middle term must come back.",
  worked({"p": -5, "q": 3},
         "Factorise {quad(1, p + q, p * q)}.",
         ["Look for two numbers with product {p * q} and sum {p + q}.",
          "The product is negative, so the numbers have opposite signs.",
          "Pairs with product {p * q}: … {p} and {q} add to {p + q}.",
          "Check: {lin2(1, p, 1, q)} = {quad(1, p + q, p * q)}."],
         "{lin2(1, p, 1, q)}",
         checks=["p * q == -15", "p + q == -2"]),
  [card("c4m5-1", "For x² + bx + c, look for two numbers whose product is c and whose sum is b.",
        ["{quad(1, 9, 20)}: {4} × {5} = {20} and {4} + {5} = {9}, so {lin2(1, 4, 1, 5)}"], "m4-5-pos"),
   card("c4m5-2", "If c is positive and b is negative, both numbers are negative.",
        ["{quad(1, -8, 15)}: {br(-3)} × {br(-5)} = {15}, {-3} + {br(-5)} = {-8}, so {lin2(1, -3, 1, -5)}"], "m4-5-neg"),
   card("c4m5-3", "If c is negative, the two numbers have opposite signs; the larger one has the sign of b.",
        ["{quad(1, 2, -24)}: {6} × {br(-4)} = {-24} and {6} + {br(-4)} = {2}, so {lin2(1, 6, 1, -4)}"], "m4-5-mixed")],
  [mcq("m4-5-pos", 1, "Factorise {quad(1, p + q, p * q)}.",
       "{lin2(1, p, 1, q)}",
       [("{lin2(1, p * q, 1, 1)}", "one"), ("{lin2(1, p + q, 1, p * q)}", "bc"), ("{lin2(1, -p, 1, -q)}", "sign")],
       ["Two numbers with product {p * q} and sum {p + q}: {p} and {q}.", "So the answer is {answer}."],
       vars={"p": {"int": [1, 9]}, "q": {"int": [2, 9]}},
       misc=[("one", "{p * q} × {1} = {p * q}, but {p * q} + {1} = {p * q + 1}, not {p + q}."),
             ("bc", "The numbers in the brackets must multiply to {p * q} and add to {p + q}. {p + q} and {p * q} do not."),
             ("sign", "{br(-p)} + {br(-q)} = {-p - q}. The middle term is +{p + q}x, so both numbers are positive.")],
       sources=SRCF, where=["p < q", "p * q != p + q"]),
   mcq("m4-5-neg", 1, "Factorise {quad(1, -(p + q), p * q)}.",
       "{lin2(1, -p, 1, -q)}",
       [("{lin2(1, p, 1, q)}", "sign"), ("{lin2(1, p, 1, -q)}", "mixed"), ("{lin2(1, -p * q, 1, -1)}", "one")],
       ["The product +{p * q} is positive and the sum {-(p + q)} is negative: both numbers are negative.",
        "{br(-p)} × {br(-q)} = {p * q} and {-p} + {br(-q)} = {-(p + q)}.", "So the answer is {answer}."],
       vars={"p": {"int": [1, 9]}, "q": {"int": [2, 9]}},
       misc=[("sign", "{lin2(1, p, 1, q)} expands to {quad(1, p + q, p * q)}: the middle sign is wrong."),
             ("mixed", "One plus and one minus give a negative product, {-p * q}. Here the product is +{p * q}."),
             ("one", "{br(-p * q)} + {br(-1)} = {-p * q - 1}, not {-(p + q)}.")],
       sources=SRCF, where=["p < q", "p * q != p + q", "p * q + 1 != p + q"]),
   mcq("m4-5-mixed", 2, "Factorise {quad(1, p + q, p * q)}.",
       "{lin2(1, p, 1, q)}",
       [("{lin2(1, -p, 1, -q)}", "swap"), ("{lin2(1, -p, 1, q)}", "pos"), ("{lin2(1, p, 1, -q)}", "pos2")],
       ["The product {p * q} is negative: the numbers have opposite signs.", "{p} × {br(q)} = {p * q} and {p} + {br(q)} = {p + q}.", "So the answer is {answer}."],
       vars={"p": {"int": [1, 12]}, "q": {"int": [-12, -1]}},
       misc=[("swap", "Expand it: the middle term would be {mono(-(p + q), 'x')}. Swap the signs."),
             ("pos", "{br(-p)} × {br(q)} = {-p * q}: the product would be positive."),
             ("pos2", "{p} × {br(-q)} = {-p * q}: the product would be positive.")],
       sources=SRCF, where=["p + q != 0", "p != -q"]),
   num("m4-5-find", 2, "{quad(1, p + q, p * q)} = (x + {br(p)})(x + k). What is k?",
       "q",
       ["The two numbers multiply to {p * q}: {p} × k = {p * q}, so k = {q}.", "Check the sum: {p} + {br(q)} = {p + q}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sum", "p + q", "k is not the middle coefficient. The two numbers multiply to {p * q}: k = {q}."),
             ("neg", "-q", "Check: {p} × {br(-q)} = {-p * q}, not {p * q}.")],
       sources=SRCF, where=["p != 0 && q != 0", "p + q != 0", "p != q", "p + q != q"], signed=True),
   mcq("m4-5-spot", 3, "Ayuk factorised {quad(1, p + q, p * q)} as {lin2(1, -p, 1, -q)}. What went wrong?",
       "The signs are swapped: the answer is {lin2(1, p, 1, q)}",
       [("Nothing: it is correct", "ok"), ("The numbers should be {p * q} and {1}", "one"), ("It cannot be factorised", "none")],
       ["Expand Ayuk's answer: {lin2(1, -p, 1, -q)} = {quad(1, -(p + q), p * q)}.", "The middle term has the wrong sign. The right factorisation is {lin2(1, p, 1, q)}.", "So the answer is: {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("ok", "Expand it: Ayuk's brackets give {mono(-(p + q), 'x')}, not {mono(p + q, 'x')}."),
             ("one", "{p * q} + {1} = {p * q + 1}, not {p + q}."),
             ("none", "It does factorise: {p} and {q} multiply to {p * q} and add to {p + q}.")],
       sources=SRCF, where=["p != 0 && q != 0", "p + q != 0", "p * q + 1 != p + q", "p < q"])],
  learn=learn(
    [goal("factorise any trinomial x² + bx + c with whole numbers, choosing the signs correctly.",
          "Lesson {2} (expanding (x + p)(x + q)) and Lesson {3} (factorising by grouping).",
          "Lesson {6} (trinomials with a number in front of x²) and solving quadratic equations by factorisation."),
     ("Product and sum",
      "Expand {lin2(1, 3, 1, 4)}: x² + {mono(4, 'x')} + {mono(3, 'x')} + {12} = {quad(1, 7, 12)}.\n"
      "The two numbers {3} and {4} multiply to give {12} and add to give {7}. So to factorise {quad(1, 7, 12)}, ask: "
      "which two numbers multiply to {12} and add to {7}?\n"
      "List the factor pairs of {12}: {1} × {12}, {2} × {6}, {3} × {4}. Only {3} and {4} add to {7}.\n"
      "Then {quad(1, 7, 12)} = {lin2(1, 3, 1, 4)}."),
     ("Getting the signs right",
      "• c positive, b positive: both numbers positive. {quad(1, 8, 15)} = {lin2(1, 3, 1, 5)}.\n"
      "• c positive, b negative: both negative. {quad(1, -8, 15)} = {lin2(1, -3, 1, -5)}.\n"
      "• c negative: one positive, one negative. The larger has the sign of b. {quad(1, -2, -15)} = {lin2(1, -5, 1, 3)}.\n"
      "Always expand to check. Common factors come out first: {quad(2, 14, 24)} = {2}({quad(1, 7, 12)}).")],
    key_words=[("trinomial", "an expression with three terms, such as {quad(1, 5, 6)}"),
               ("quadratic", "with x² as the highest power of x"),
               ("factor pair", "two whole numbers that multiply to a given number")],
    examples=["{quad(1, 5, 6)} = {lin2(1, 2, 1, 3)}", "{quad(1, -9, 14)} = {lin2(1, -2, 1, -7)}", "{quad(1, 4, -21)} = {lin2(1, 7, 1, -3)}"],
    mistake=("{quad(1, -2, -15)} = {lin2(1, 5, 1, -3)}", "{quad(1, -2, -15)} = {lin2(1, -5, 1, 3)}",
             "{5} + {br(-3)} = {2}, but the middle term is {mono(-2, 'x')}. The larger number takes the sign of b: {-5} and {3}.")))

# ---------------------------------------------------------------- 6. Quadratic trinomials ax² + bx + c
L.lesson(D, S, 6, ("m4-6", "Factorise quadratic trinomials ax² + bx + c with a ≠ 1"), [5],
  "To factorise ax² + bx + c when a is not 1, use the ac method.\n"
  "• Multiply a × c.\n• Find two numbers that multiply to ac and add to b.\n• Split the middle term with them, then factorise by grouping.\n"
  "Example: 2x² + 7x + 3. ac = 6; 6 and 1 multiply to 6 and add to 7. "
  "2x² + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3).\n"
  "Take out any common factor first. Check by expanding.",
  worked({"a": 3, "b": -10, "c": -8},
         "Factorise {quad(a, b, c)}.",
         ["Multiply a × c: {a} × {br(c)} = {a * c}.",
          "Find two numbers with product {a * c} and sum {b}: {-12} and {2}.",
          "Split the middle term: {poly([a, 'x²'], [-12, 'x'], [2, 'x'], [c, ''])}.",
          "Group: {mono(3, 'x')}({poly([1, 'x'], [-4, ''])}) + {2}({poly([1, 'x'], [-4, ''])}) = {lin2(3, 2, 1, -4)}."],
         "{lin2(3, 2, 1, -4)}",
         checks=["a * c == -24", "-12 + 2 == b", "-12 * 2 == a * c"]),
  [card("c4m6-1", "The ac method starts by multiplying the first and last coefficients.",
        ["{quad(2, 7, 3)}: a × c = {2} × {3} = {6}"], "m4-6-ac"),
   card("c4m6-2", "Find two numbers that multiply to ac and add to b, and use them to split the middle term.",
        ["{6} = {6} × {1} and {6} + {1} = {7}: {quad(2, 7, 3)} = {poly([2, 'x²'], [6, 'x'], [1, 'x'], [3, ''])}"], "m4-6-split"),
   card("c4m6-3", "Group the four terms; the two brackets must match.",
        ["{mono(2, 'x')}(x + {3}) + {1}(x + {3}) = {lin2(2, 1, 1, 3)}"], "m4-6-full")],
  [num("m4-6-ac", 1, "To factorise {quad(a, b, c)} by the ac method, which number do the two numbers multiply to?",
       "a * c",
       ["Multiply the coefficient of x² by the number term: {a} × {br(c)} = {answer}."],
       vars={"r": {"int": [2, 4]}, "s": {"int": [-5, 5]}, "t": {"int": [1, 2]}, "u": {"int": [-5, 5]},
             "a": {"expr": "r * t"}, "b": {"expr": "r * u + s * t"}, "c": {"expr": "s * u"}},
       misc=[("c", "c", "With a ≠ {1}, the numbers multiply to a × c = {a} × {br(c)}, not to c alone."),
             ("b", "b", "{b} is what they add to. They multiply to a × c = {a * c}.")],
       sources=SRCF, where=["s != 0 && u != 0", "b != 0", "a * c != b", "hcf(r, abs(s)) == 1 && hcf(t, abs(u)) == 1"], signed=True),
   mcq("m4-6-split", 1, "To factorise {quad(a, p + q, c)}, the middle term is split using two numbers with product {a * c} and sum {p + q}. Which pair?",
       "{p} and {q}",
       [("{a} and {c}", "ac"), ("{p * q} and {1}", "one"), ("{-p} and {-q}", "sign")],
       ["Product: {p} × {br(q)} = {p * q} = {a} × {br(c)}.", "Sum: {p} + {br(q)} = {p + q}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 5]}, "p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}, "c": {"expr": "p * q / a"}},
       misc=[("ac", "{a} and {c} multiply to {a * c}, but they add to {a + c}, not {p + q}."),
             ("one", "{p * q} + {1} = {p * q + 1}, not {p + q}."),
             ("sign", "{-p} + {br(-q)} = {-p - q}: the sum has the wrong sign.")],
       sources=SRCF, where=["p != 0 && q != 0", "(p * q) % a == 0", "p + q != 0", "a + c != p + q", "p * q + 1 != p + q", "p < q", "p != -q", "hcf3(a, abs(p + q), abs(c)) == 1"]),
   mcq("m4-6-full", 2, "Factorise {quad(r * t, r * u + s * t, s * u)}.",
       "{lin2(r, s, t, u)}",
       [("{lin2(r, u, t, s)}", "cross"), ("{lin2(r * t, s, 1, u)}", "aone"), ("{lin2(r, -s, t, -u)}", "sign")],
       ["a × c = {r * t} × {br(s * u)} = {r * t * s * u}; the numbers {r * u} and {s * t} multiply to {r * t * s * u} and add to {r * u + s * t}.",
        "Split and group, then check: {lin2(r, s, t, u)} = {quad(r * t, r * u + s * t, s * u)}.", "So the answer is {answer}."],
       vars={"r": {"int": [2, 4]}, "s": {"int": [-5, 5]}, "t": {"int": [1, 3]}, "u": {"int": [-5, 5]}},
       misc=[("cross", "Expand it: {lin2(r, u, t, s)} gives the middle term {mono(r * s + u * t, 'x')}, not {mono(r * u + s * t, 'x')}."),
             ("aone", "Expand it: {lin2(r * t, s, 1, u)} gives the middle term {mono(r * t * u + s, 'x')}."),
             ("sign", "Expand it: the middle term would be {mono(-(r * u + s * t), 'x')}.")],
       sources=SRCF, where=["s != 0 && u != 0", "r * u + s * t != 0", "r * s + u * t != r * u + s * t", "r * t * u + s != r * u + s * t", "hcf(r, abs(s)) == 1 && hcf(t, abs(u)) == 1", "s != u"]),
   num("m4-6-find", 2, "{quad(r * t, r * u + s * t, s * u)} = ({poly([r, 'x'], [s, ''])})({mono(t, 'x')} + k). What is k?",
       "u",
       ["The last terms multiply to {s * u}: {s} × k = {s * u}, so k = {u}.",
        "Check the middle: {mono(r, 'x')} × {br(u)} + {s} × {mono(t, 'x')} = {mono(r * u + s * t, 'x')}."],
       vars={"r": {"int": [2, 4]}, "s": {"int": [-5, 5]}, "t": {"int": [1, 3]}, "u": {"int": [-5, 5]}},
       misc=[("prod", "s * u", "{s * u} is the whole number term. k is the number that times {s} gives {s * u}: {u}."),
             ("neg", "-u", "Check: {s} × {br(-u)} = {-s * u}, not {s * u}.")],
       sources=SRCF, where=["s != 0 && u != 0", "r * u + s * t != 0", "s * u != u", "hcf(r, abs(s)) == 1 && hcf(t, abs(u)) == 1"], signed=True),
   mcq("m4-6-common", 3, "Factorise completely {quad(k * r * t, k * (r * u + s * t), k * s * u)}.",
       "{k}{lin2(r, s, t, u)}",
       [("{lin2(r, s, t, u)}", "lost"), ("{k}({quad(r * t, r * u + s * t, s * u)})", "stop"), ("{lin2(k * r, s, t, k * u)}", "both")],
       ["Every coefficient is a multiple of {k}: take {k} out first.", "Then factorise {quad(r * t, r * u + s * t, s * u)} = {lin2(r, s, t, u)}.", "So the answer is {answer}."],
       vars={"k": {"int": [2, 4]}, "r": {"int": [2, 3]}, "s": {"int": [-5, 5]}, "t": {"int": [1, 2]}, "u": {"int": [-5, 5]}},
       misc=[("lost", "Expand it: that gives {quad(r * t, r * u + s * t, s * u)}. The common factor {k} is missing."),
             ("stop", "'Completely' means factorise the trinomial too: {quad(r * t, r * u + s * t, s * u)} = {lin2(r, s, t, u)}."),
             ("both", "{k} was put into both brackets, which multiplies by {k * k}. Put it in front once.")],
       sources=SRCF, where=["s != 0 && u != 0", "r * u + s * t != 0", "hcf(r, abs(s)) == 1 && hcf(t, abs(u)) == 1", "s != u"])],
  learn=learn(
    [goal("factorise trinomials such as {quad(2, 7, 3)} and {quad(3, -10, -8)} by the ac method, and check by expanding.",
          "Lesson {5} (product and sum for x² + bx + c) and Lesson {3} (grouping).",
          "solving quadratic equations by factorisation (Lesson {7}) and the factor theorem."),
     ("The ac method",
      "When the number in front of x² is not {1}, the product-and-sum trick needs one extra step.\n"
      "Take {quad(2, 7, 3)}.\n"
      "• Multiply a × c: {2} × {3} = {6}.\n"
      "• Find two numbers that multiply to {6} and add to {7}: {6} and {1}.\n"
      "• Split {mono(7, 'x')} into {mono(6, 'x')} + x: {poly([2, 'x²'], [6, 'x'], [1, 'x'], [3, ''])}.\n"
      "• Group: {mono(2, 'x')}(x + {3}) + {1}(x + {3}) = {lin2(2, 1, 1, 3)}."),
     ("Negative numbers and checking",
      "The sign rules from Lesson {5} still apply to the two numbers.\n"
      "For {quad(3, -10, -8)}: a × c = {-24}. The numbers {-12} and {2} multiply to {-24} and add to {-10}.\n"
      "{poly([3, 'x²'], [-12, 'x'], [2, 'x'], [-8, ''])} = {mono(3, 'x')}(x − {4}) + {2}(x − {4}) = {lin2(3, 2, 1, -4)}.\n"
      "Check: {mono(3, 'x')} × {br(-4)} + {2} × x = {mono(-10, 'x')}. The middle term comes back, so the answer is right.")],
    key_words=[("coefficient", "the number multiplying a term, such as {3} in {mono(3, 'x²')}"),
               ("ac method", "splitting the middle term using two numbers that multiply to a × c and add to b"),
               ("split the middle term", "write bx as the sum of two x terms so that grouping works")],
    examples=["{quad(2, 5, 2)} = {lin2(2, 1, 1, 2)}", "{quad(3, 1, -2)} = {lin2(3, -2, 1, 1)}", "{quad(6, -7, 2)} = {lin2(2, -1, 3, -2)}"],
    mistake=("{quad(2, 7, 3)} = {lin2(2, 3, 1, 1)}", "{quad(2, 7, 3)} = {lin2(2, 1, 1, 3)}",
             "Expand to check: {lin2(2, 3, 1, 1)} gives {mono(5, 'x')} in the middle, not {mono(7, 'x')}. The position of each number matters.")))
