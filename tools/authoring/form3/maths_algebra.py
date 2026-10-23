"""Form 3 Maths, Term 1, rows 3-7 (simple algebra: expansion, factorisation, linear equations).
Run: python tools/authoring/form3/maths_algebra.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"


def lin(a, c="1", v="x"):
    """Expression text for one bracket (c·v + a), e.g. lin("p") -> "(x + p)" with signs handled by poly."""
    return f"'(' + poly([{c}, '{v}'], [{a}, '']) + ')'"


def F(a, b, c="1", d="1"):
    """{…} for the product (c·x + a)(d·x + b)."""
    return "{" + lin(a, c) + " + " + lin(b, d) + "}"


# ---------------------------------------------------------------- 3. Expansions of algebraic expressions
SRC = ["algebra-expand"]
L.lesson(D, S, 3, ("m3-3", "Expand products of brackets and the special products"), [2],
  "To expand (x + a)(x + b), multiply each term of the first bracket by each term of the second, then collect like terms:\n"
  "(x + a)(x + b) = x² + bx + ax + ab = x² + (a + b)x + ab.\n"
  "Special products (learn them):\n"
  "• (a + b)² = a² + 2ab + b²\n"
  "• (a − b)² = a² − 2ab + b²\n"
  "• (a + b)(a − b) = a² − b²\n"
  "A square is not the square of each term: (x + 3)² is x² + 6x + 9, not x² + 9.",
  worked({"p": 2, "a": 3, "b": -4},
         "Expand and simplify {" + lin("a", "p") + " + " + lin("b") + "}.",
         ["Multiply each term of the first bracket by each term of the second.",
          "{mono(p, 'x')} × x = {mono(p, 'x²')};  {mono(p, 'x')} × {br(b)} = {mono(p * b, 'x')};  {a} × x = {mono(a, 'x')};  {a} × {br(b)} = {a * b}.",
          "Collect the x terms: {p * b} + {a} = {p * b + a}."],
         "{poly([p, 'x²'], [p * b + a, 'x'], [a * b, ''])}",
         checks=["p * b + a == -5", "a * b == -12"]),
  [card("c3m3-1", "Multiply every term of the first bracket by every term of the second: four products, then collect.",
        ["{'(x + ' + 2 + ')(x + ' + 5 + ')'} = {poly([1, 'x²'], [5, 'x'], [2, 'x'], [10, ''])} = {poly([1, 'x²'], [7, 'x'], [10, ''])}"], "m3-3-pair"),
   card("c3m3-2", "The square of a sum has a middle term: (a + b)² = a² + {2}ab + b².",
        ["{'(x + ' + 3 + ')²'} = {poly([1, 'x²'], [6, 'x'], [9, ''])}, not {poly([1, 'x²'], [9, ''])}."], "m3-3-square"),
   card("c3m3-3", "Sum times difference: (a + b)(a − b) = a² − b². The middle terms cancel.",
        ["{'(x + ' + 5 + ')(x − ' + 5 + ')'} = {poly([1, 'x²'], [-25, ''])}"], "m3-3-diff")],
  [mcq("m3-3-pair", 1, "Expand {" + lin("a") + " + " + lin("b") + "}.",
       "{poly([1, 'x²'], [a + b, 'x'], [a * b, ''])}",
       [("{poly([1, 'x²'], [a * b, ''])}", "middle"), ("{poly([1, 'x²'], [a + b, 'x'], [a + b, ''])}", "addconst"), ("{poly([1, 'x²'], [a * b, 'x'], [a * b, ''])}", "mulx")],
       ["x × x = x²; x × {br(b)} + {a} × x gives {mono(a + b, 'x')}; {a} × {br(b)} = {a * b}.", "So the answer is {answer}."],
       vars={"a": {"int": [1, 9]}, "b": {"int": [-9, 9]}},
       misc=[("middle", "There are four products: x × {br(b)} and {a} × x make the middle term {mono(a + b, 'x')}."),
             ("addconst", "The last term is a product: {a} × {br(b)} = {a * b}, not a sum."),
             ("mulx", "The x terms are added: {mono(b, 'x')} + {mono(a, 'x')} = {mono(a + b, 'x')}.")],
       sources=SRC, where=["b != 0", "a + b != 0", "a * b != a + b", "a != b", "a + b != a * b"]),
   num("m3-3-coef", 1, "Expand {" + lin("a") + " + " + lin("b") + "}. What is the coefficient of x?", "a + b",
       ["x × {br(b)} = {mono(b, 'x')} and {a} × x = {mono(a, 'x')}.", "{a} + {br(b)} = {answer}."],
       vars={"a": {"int": [-9, 9]}, "b": {"int": [-9, 9]}},
       misc=[("prod", "a * b", "{a * b} is the number term (the product). The x terms come from x × {br(b)} and {a} × x.")],
       sources=SRC, where=["a != 0 && b != 0", "a + b != 0", "a * b != a + b"], signed=True),
   mcq("m3-3-square", 2, "Expand {" + lin("a") + " + '²'}.",
       "{poly([1, 'x²'], [2 * a, 'x'], [a * a, ''])}",
       [("{poly([1, 'x²'], [a * a, ''])}", "noterm"), ("{poly([1, 'x²'], [a, 'x'], [a * a, ''])}", "once"), ("{poly([1, 'x²'], [2 * a, 'x'], [2 * a, ''])}", "double")],
       ["{" + lin("a") + " + '²'} = {" + lin("a") + " + " + lin("a") + "}.", "x² + {mono(a, 'x')} + {mono(a, 'x')} + {a * a} = {answer}."],
       vars={"a": {"int": [-9, 9]}},
       misc=[("noterm", "Squaring a bracket is not squaring each term: write it twice and expand; there is a middle term {mono(2 * a, 'x')}."),
             ("once", "The middle term appears twice: {mono(a, 'x')} + {mono(a, 'x')} = {mono(2 * a, 'x')}."),
             ("double", "The last term is {br(a)} × {br(a)} = {a * a}, not {2 * a}.")],
       sources=SRC, where=["a != 0", "abs(a) != 1", "abs(a) != 2"]),
   num("m3-3-two", 2, "Expand {" + lin("a", "p") + " + " + lin("b", "q") + "}. What is the coefficient of x?", "p * b + q * a",
       ["{mono(p, 'x')} × {br(b)} = {mono(p * b, 'x')} and {a} × {mono(q, 'x')} = {mono(q * a, 'x')}.", "{p * b} + {br(q * a)} = {answer}."],
       vars={"p": {"int": [2, 5]}, "q": {"int": [1, 4]}, "a": {"int": [-9, 9]}, "b": {"int": [-9, 9]}},
       misc=[("pq", "p * q", "{p * q} is the coefficient of x² ({mono(p, 'x')} × {mono(q, 'x')})."),
             ("plain", "a + b", "Multiply first: the x terms are {mono(p, 'x')} × {br(b)} and {a} × {mono(q, 'x')}.")],
       sources=SRC, where=["a != 0 && b != 0", "p * b + q * a != 0", "p * b + q * a != a + b", "p * b + q * a != p * q"], signed=True),
   mcq("m3-3-diff", 3, "Expand {" + lin("a") + " + " + lin("-a") + "}.",
       "{poly([1, 'x²'], [-a * a, ''])}",
       [("{poly([1, 'x²'], [a * a, ''])}", "plus"), ("{poly([1, 'x²'], [-2 * a, 'x'], [-a * a, ''])}", "middle"), ("{poly([1, 'x²'], [-2 * a, ''])}", "twice")],
       ["The middle terms cancel: {mono(-a, 'x')} + {mono(a, 'x')} = {0}.", "{a} × {br(-a)} = {-a * a}, so the answer is {answer}."],
       vars={"a": {"int": [2, 12]}},
       misc=[("plus", "{a} × {br(-a)} is negative: the last term is {-a * a}."),
             ("middle", "The x terms {mono(-a, 'x')} and {mono(a, 'x')} cancel: there is no middle term."),
             ("twice", "The last term is {a} × {br(-a)} = {-a * a}, a product, not {-2 * a}.")],
       sources=SRC)],
  learn=learn(
    [("Every term times every term",
      "To expand means to remove the brackets. In {'(x + ' + 2 + ')(x + ' + 5 + ')'} each term of the first bracket multiplies each term of the second:\n"
      "• x × x = x²\n• x × {5} = {mono(5, 'x')}\n• {2} × x = {mono(2, 'x')}\n• {2} × {5} = {10}\n"
      "Four products. Then collect the like terms: {poly([1, 'x²'], [7, 'x'], [10, ''])}.\n"
      "Signs come with their terms: in {'(x + ' + 3 + ')(x − ' + 4 + ')'} the products are x², {mono(-4, 'x')}, {mono(3, 'x')} and {-12}, giving {poly([1, 'x²'], [-1, 'x'], [-12, ''])}."),
     ("Squares of brackets",
      "{'(x + ' + 3 + ')²'} means {'(x + ' + 3 + ')(x + ' + 3 + ')'}. Expand it like any product: x² + {mono(3, 'x')} + {mono(3, 'x')} + {9} = {poly([1, 'x²'], [6, 'x'], [9, ''])}.\n"
      "The pattern is always: first squared, twice the product, last squared.\n"
      "• (a + b)² = a² + {2}ab + b²\n• (a − b)² = a² − {2}ab + b²\n"
      "A common mistake is to write only x² + {9}: the middle term {mono(6, 'x')} is missing."),
     ("Sum times difference",
      "When the brackets differ only in the sign, the middle terms cancel:\n"
      "{'(x + ' + 5 + ')(x − ' + 5 + ')'} = x² − {mono(5, 'x')} + {mono(5, 'x')} − {25} = {poly([1, 'x²'], [-25, ''])}.\n"
      "So (a + b)(a − b) = a² − b², the difference of two squares. You will use it backwards to factorise.")],
    key_words=[("expand", "remove the brackets by multiplying out"), ("product", "the result of a multiplication"),
               ("like terms", "terms with the same letters and powers, which can be added"),
               ("perfect square", "an expression like (a + b)², a bracket multiplied by itself")],
    examples=["{'(x + ' + 1 + ')(x + ' + 6 + ')'} = {poly([1, 'x²'], [7, 'x'], [6, ''])}",
              "{'(x − ' + 2 + ')²'} = {poly([1, 'x²'], [-4, 'x'], [4, ''])}",
              "{'(y + ' + 4 + ')(y − ' + 4 + ')'} = {poly([1, 'y²'], [-16, ''])}"],
    mistake=("{'(x + ' + 4 + ')²'} = {poly([1, 'x²'], [16, ''])}", "{'(x + ' + 4 + ')²'} = {poly([1, 'x²'], [8, 'x'], [16, ''])}",
             "A square is the bracket times itself. The two middle products x × {4} and {4} × x give {mono(8, 'x')}.")))

# ---------------------------------------------------------------- 4. Factorisation (common factors, grouping)
SRC = ["algebra-factorise"]
L.lesson(D, S, 4, ("m3-4", "Factorise by a common factor and by grouping"), [3],
  "Factorising is the reverse of expanding: write the expression as a product.\n"
  "• Common factor: find the highest common factor (HCF) of all the terms, numbers and letters, and take it outside a bracket: 6x + 9 = 3(2x + 3); 4x² − 10x = 2x(2x − 5).\n"
  "• Check by expanding: the bracket must give back the original expression.\n"
  "• Fully factorised: nothing more can be taken out of the bracket.\n"
  "• Grouping (four terms): factorise pairs, then take out the common bracket: ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y).",
  worked({"g": 3, "m": 2, "n": 5},
         "Factorise fully {poly([g * m, 'x²'], [g * n, 'x'])}.",
         ["HCF of the numbers {g * m} and {g * n} is {g}.", "Both terms contain x, so x is common too: the HCF is {mono(g, 'x')}.",
          "{mono(g * m, 'x²')} ÷ {mono(g, 'x')} = {mono(m, 'x')} and {mono(g * n, 'x')} ÷ {mono(g, 'x')} = {n}.",
          "Check: {mono(g, 'x')} × {mono(m, 'x')} + {mono(g, 'x')} × {n} gives back the expression."],
         "{mono(g, 'x') + '(' + poly([m, 'x'], [n, '']) + ')'}",
         checks=["hcf(m, n) == 1"]),
  [card("c3m4-1", "Take the highest common factor outside the bracket and divide each term by it.",
        ["{poly([6, 'x'], [9, ''])} = {bracket(3, [2, 'x'], [3, ''])}"], "m3-4-hcf"),
   card("c3m4-2", "Letters can be common factors too: x is a factor of x² and of x.",
        ["{poly([4, 'x²'], [-10, 'x'])} = {mono(2, 'x') + '(' + poly([2, 'x'], [-5, '']) + ')'}"], "m3-4-letter"),
   card("c3m4-3", "With four terms, factorise in pairs, then take out the common bracket.",
        ["{poly([1, 'x²'], [3, 'x'], [2, 'x'], [6, ''])} = x{" + lin(3) + "} + {2}{" + lin(3) + "} = {" + lin(3) + " + " + lin(2) + "}"], "m3-4-group")],
  [mcq("m3-4-hcf", 1, "Factorise {poly([k * m, 'x'], [k * n, ''])}.",
       "{bracket(k, [m, 'x'], [n, ''])}",
       [("{bracket(k, [m, 'x'], [k * n, ''])}", "one"), ("{bracket(m, [k, 'x'], [k * n / m, ''])}", "wrongf"), ("{mono(k, 'x') + '(' + poly([m, ''], [n, '']) + ')'}", "xout")],
       ["The HCF of {k * m} and {k * n} is {k}.", "{k * m} ÷ {k} = {m} and {k * n} ÷ {k} = {n}, so the answer is {answer}."],
       vars={"k": {"int": [2, 9]}, "m": {"int": [2, 9]}, "n": {"int": [1, 9]}},
       misc=[("one", "Divide every term by {k}: {k * n} ÷ {k} = {n}."),
             ("wrongf", "Not fully factorised: the bracket still has a common factor. Take out the highest common factor, {k}."),
             ("xout", "x is only in one term, so it cannot be taken out.")],
       sources=SRC, where=["hcf(m, n) == 1", "m != k", "(k * n) % m == 0 ? true : false", "n != m"]),
   num("m3-4-which", 1, "{poly([k * m, 'x'], [k * n, 'y'])} = k(…). What is the number k taken out (the highest common factor)?", "k",
       ["The HCF of {k * m} and {k * n} is {k}: {k * m} = {k} × {m} and {k * n} = {k} × {n}.", "So k = {answer}."],
       vars={"k": {"int": [2, 12]}, "m": {"int": [2, 9]}, "n": {"int": [2, 9]}},
       misc=[("prod", "k * m * n", "{k * m * n} is too big: it does not divide {k * m}.")],
       sources=SRC, where=["hcf(m, n) == 1", "m != n"]),
   mcq("m3-4-letter", 2, "Factorise fully {poly([g * m, 'x²'], [g * n, 'x'])}.",
       "{mono(g, 'x') + '(' + poly([m, 'x'], [n, '']) + ')'}",
       [("{bracket(g, [m, 'x²'], [n, 'x'])}", "noletter"), ("{'x(' + poly([g * m, 'x'], [g * n, '']) + ')'}", "nonumber"), ("{mono(g, 'x') + '(' + poly([m, 'x²'], [n, 'x']) + ')'}", "nodivide")],
       ["The HCF is {mono(g, 'x')}: {g} divides both numbers and x is in both terms.", "{mono(g * m, 'x²')} ÷ {mono(g, 'x')} = {mono(m, 'x')}; {mono(g * n, 'x')} ÷ {mono(g, 'x')} = {n}.", "So the answer is {answer}."],
       vars={"g": {"int": [2, 7]}, "m": {"int": [1, 9]}, "n": {"int": [-9, 9]}},
       misc=[("noletter", "Not fully factorised: x is also common to both terms."),
             ("nonumber", "Not fully factorised: {g} is also common to both terms."),
             ("nodivide", "Divide each term by {mono(g, 'x')}: {mono(g * m, 'x²')} ÷ {mono(g, 'x')} = {mono(m, 'x')}.")],
       sources=SRC, where=["n != 0", "hcf(m, abs(n)) == 1"]),
   mcq("m3-4-group", 2, "Factorise {poly([1, 'x²'], [a, 'x'], [b, 'x'], [a * b, ''])} by grouping.",
       F("a", "b"),
       [("{'x' + " + lin("a") + " + ' + ' + b + " + lin("a") + "}", "unfinished"), (F("a * b", "1"), "product"), (F("-a", "-b"), "signs")],
       ["Group in pairs: x{" + lin("a") + "} + {b}{" + lin("a") + "}.", "Take out the common bracket {" + lin("a") + "}: the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [2, 9]}},
       misc=[("unfinished", "Not finished: {" + lin("a") + "} is common to both parts; take it out."),
             ("product", "Check by expanding: that gives a middle term {mono(a * b + 1, 'x')}, not {mono(a + b, 'x')}."),
             ("signs", "Check by expanding: that gives {mono(-a - b, 'x')}, but the expression has {mono(a + b, 'x')}.")],
       sources=SRC, where=["a != b"]),
   mcq("m3-4-full", 3, "Factorise fully {poly([g * m, 'x²y'], [g * n, 'xy²'])}.",
       "{mono(g, 'xy') + '(' + poly([m, 'x'], [n, 'y']) + ')'}",
       [("{bracket(g, [m, 'x²y'], [n, 'xy²'])}", "num"), ("{'xy(' + poly([g * m, 'x'], [g * n, 'y']) + ')'}", "let"), ("{mono(g, 'x') + '(' + poly([m, 'xy'], [n, 'y²']) + ')'}", "half")],
       ["Numbers: HCF of {g * m} and {g * n} is {g}. Letters: both terms contain x and y, so xy is common.",
        "Divide: {mono(g * m, 'x²y')} ÷ {mono(g, 'xy')} = {mono(m, 'x')}; {mono(g * n, 'xy²')} ÷ {mono(g, 'xy')} = {mono(n, 'y')}.", "So the answer is {answer}."],
       vars={"g": {"int": [2, 8]}, "m": {"int": [1, 9]}, "n": {"int": [1, 9]}},
       misc=[("num", "Not fully factorised: x and y are common to both terms too."),
             ("let", "Not fully factorised: {g} is also a common factor."),
             ("half", "Not fully factorised: y is also in both terms.")],
       sources=SRC, where=["hcf(m, n) == 1", "m != n"])],
  learn=learn(
    [("Factorising undoes expanding",
      "Expanding turns a product into a sum: {bracket(3, [2, 'x'], [5, ''])} = {poly([6, 'x'], [15, ''])}.\n"
      "Factorising goes back: from {poly([6, 'x'], [15, ''])} we find {bracket(3, [2, 'x'], [5, ''])}.\n"
      "Step one is the highest common factor (HCF) of all the terms. {3} divides both {6} and {15}, and nothing bigger does. "
      "Write the HCF outside, and inside the bracket write each term divided by it.\n"
      "Always check by expanding your answer: you must get the original expression back."),
     ("Letters can be common factors",
      "Look at the letters as well as the numbers. In {poly([8, 'x²'], [12, 'x'])}:\n"
      "• numbers: the HCF of {8} and {12} is {4};\n• letters: x² = x × x, so x is in both terms.\n"
      "The HCF is {mono(4, 'x')}, so {poly([8, 'x²'], [12, 'x'])} = {mono(4, 'x') + '(' + poly([2, 'x'], [3, '']) + ')'}.\n"
      "If you take out only {4} or only x, the answer is factorised but not fully factorised: something common is still inside."),
     ("Four terms: grouping",
      "Sometimes no factor is common to all four terms, as in {poly([1, 'x²'], [3, 'x'], [2, 'x'], [6, ''])}.\n"
      "Group the terms in pairs and factorise each pair: x{" + lin(3) + "} + {2}{" + lin(3) + "}.\n"
      "Now the bracket {" + lin(3) + "} is common, so take it out: {" + lin(3) + " + " + lin(2) + "}.")],
    key_words=[("factorise", "write as a product of factors"), ("factor", "a number or expression that divides exactly"),
               ("HCF", "highest common factor: the biggest factor shared by all the terms"),
               ("fully factorised", "no common factor is left inside the bracket")],
    examples=["{poly([5, 'a'], [20, ''])} = {bracket(5, [1, 'a'], [4, ''])}",
              "{poly([9, 'y²'], [-6, 'y'])} = {mono(3, 'y') + '(' + poly([3, 'y'], [-2, '']) + ')'}",
              "{poly([1, 'a'], [1, 'b'])} times two: {poly([2, 'a'], [2, 'b'])} = {bracket(2, [1, 'a'], [1, 'b'])}"],
    mistake=("{poly([6, 'x²'], [9, 'x'])} = {bracket(3, [2, 'x²'], [3, 'x'])}", "{poly([6, 'x²'], [9, 'x'])} = {mono(3, 'x') + '(' + poly([2, 'x'], [3, '']) + ')'}",
             "The first answer is not fully factorised: x is still common to both terms in the bracket.")))

# ---------------------------------------------------------------- 5. Factorising quadratic trinomials
SRC = ["algebra-factorise"]
L.lesson(D, S, 5, ("m3-5", "Factorise quadratic trinomials"), [3, 4],
  "A quadratic trinomial x² + bx + c factorises as (x + p)(x + q), where p + q = b and p × q = c.\n"
  "• List the factor pairs of c and choose the pair that adds to b.\n"
  "• Signs: c positive → p and q have the same sign as b; c negative → one is positive and one negative.\n"
  "• When the coefficient of x² is not 1 (ax² + bx + c), try factor pairs of a and of c until the middle term is right.\n"
  "• Always check by expanding.",
  worked({"p": 5, "q": -2},
         "Factorise {poly([1, 'x²'], [p + q, 'x'], [p * q, ''])}.",
         ["We need two numbers with product {p * q} and sum {p + q}.",
          "The product is negative, so one number is negative. Pairs for {abs(p * q)}: {1} and {10}, {2} and {5}.",
          "{p} + {br(q)} = {p + q}: the numbers are {p} and {q}.",
          "Check: {" + lin("p") + " + " + lin("q") + "} = {poly([1, 'x²'], [p + q, 'x'], [p * q, ''])}."],
         F("p", "q"), checks=["p * q == -10"]),
  [card("c3m5-1", "x² + bx + c = (x + p)(x + q) when p + q = b and p × q = c.",
        ["{poly([1, 'x²'], [7, 'x'], [12, ''])}: {3} + {4} = {7} and {3} × {4} = {12}, so {" + lin(3) + " + " + lin(4) + "}."], "m3-5-pos"),
   card("c3m5-2", "If c is negative, one number is negative and one positive.",
        ["{poly([1, 'x²'], [2, 'x'], [-15, ''])} = {" + lin(5) + " + " + lin(-3) + "}"], "m3-5-neg"),
   card("c3m5-3", "Check a factorisation by expanding it.",
        ["{" + lin(4) + " + " + lin(-1) + "} = {poly([1, 'x²'], [3, 'x'], [-4, ''])}"], "m3-5-pair")],
  [mcq("m3-5-pos", 1, "Factorise {poly([1, 'x²'], [p + q, 'x'], [p * q, ''])}.",
       F("p", "q"),
       [(F("p * q", "1"), "prod"), (F("-p", "-q"), "sign"), (F("p + q", "p * q"), "both")],
       ["Two numbers with sum {p + q} and product {p * q}: {p} and {q}.", "So the answer is {answer}."],
       vars={"p": {"int": [1, 9]}, "q": {"int": [2, 9]}},
       misc=[("prod", "Expand it: the middle term would be {mono(p * q + 1, 'x')}. The numbers must also add to {p + q}."),
             ("sign", "With these signs the middle term is {mono(-p - q, 'x')}; we need {mono(p + q, 'x')}."),
             ("both", "Those are the sum and the product themselves; find two numbers that give them.")],
       sources=SRC, where=["p < q", "p * q + 1 != p + q"]),
   num("m3-5-pair", 1, "Find two numbers whose sum is {p + q} and whose product is {p * q}. Give the larger one.", "max(p, q)",
       ["Try factor pairs of {p * q}: {p} × {q} = {p * q} and {p} + {br(q)} = {p + q}.", "The larger one is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("small", "min(p, q)", "That is the smaller of the two numbers: {min(p, q)} and {max(p, q)}.")],
       sources=SRC, where=["p != q", "p != 0 && q != 0", "abs(p) != 1 || abs(q) != 1"], signed=True),
   mcq("m3-5-neg", 2, "Factorise {poly([1, 'x²'], [p + q, 'x'], [p * q, ''])}.",
       F("p", "q"),
       [(F("-p", "-q"), "swap"), (F("p", "-q"), "bothpos"), (F("-p", "q"), "bothneg")],
       ["Product {p * q} is negative, so one number is negative; their sum is {p + q}.", "{p} + {br(q)} = {p + q} and {p} × {br(q)} = {p * q}, so the answer is {answer}."],
       vars={"p": {"int": [2, 9]}, "q": {"int": [-9, -1]}},
       misc=[("swap", "Expand it: the middle term would be {mono(-p - q, 'x')}; the signs are the wrong way round."),
             ("bothpos", "Expand it: the last term would be {p * -q}, positive; we need {p * q}."),
             ("bothneg", "Expand it: the last term would be {-p * q}, positive; we need {p * q}.")],
       sources=SRC, where=["p + q != 0", "p != -q"]),
   num("m3-5-k", 2, "{poly([1, 'x²'], [p + q, 'x'], [p * q, ''])} = {" + lin("p") + "}(x + k). Find k.", "q",
       ["{p} × k = {p * q}, so k = {p * q} ÷ {p} = {q}.", "Check the sum: {p} + {br(q)} = {p + q}. k = {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sum", "p + q", "{p + q} is the sum; k must multiply with {p} to give {p * q}."),
             ("sgn", "-q", "Check the sign: {p} × {br(-q)} = {-p * q}, not {p * q}.")],
       sources=SRC, where=["p != 0 && q != 0", "p + q != 0", "p != q", "abs(p) != 1"], signed=True),
   mcq("m3-5-a", 3, "Factorise {poly([a, 'x²'], [a * n + m, 'x'], [m * n, ''])}.",
       F("m", "n", "a"),
       [(F("n", "m", "a"), "swap"), (F("m", "n"), "noa"), (F("m * n", "1", "a"), "prod")],
       ["Try {" + lin("m", "a") + " + " + lin("n") + "}: {mono(a, 'x')} × {n} + {m} × x = {mono(a * n + m, 'x')}. ✓", "So the answer is {answer}."],
       vars={"a": {"int": [2, 5]}, "m": {"int": [1, 7]}, "n": {"int": [1, 7]}},
       misc=[("swap", "Expand it: the middle term would be {mono(a * m + n, 'x')}, not {mono(a * n + m, 'x')}."),
             ("noa", "Expand it: the x² term would be x², not {mono(a, 'x²')}."),
             ("prod", "Expand it: the middle term would be {mono(a + m * n, 'x')}, not {mono(a * n + m, 'x')}.")],
       sources=SRC, where=["m != n", "a * m + n != a * n + m", "a + m * n != a * n + m", "hcf(a, m) == 1"])],
  learn=learn(
    [("Reading the pattern",
      "Expand {" + lin(2) + " + " + lin(5) + "}: you get {poly([1, 'x²'], [7, 'x'], [10, ''])}. Look where the numbers went:\n"
      "• {7} is {2} + {5}, the sum;\n• {10} is {2} × {5}, the product.\n"
      "So to factorise x² + bx + c, look for two numbers that multiply to c and add to b. "
      "Then x² + bx + c = (x + first)(x + second)."),
     ("Finding the two numbers",
      "Factorise {poly([1, 'x²'], [-1, 'x'], [-12, ''])}. Product {-12}, sum {-1}.\n"
      "The product is negative, so one number is negative. List the pairs for {12}: {1} and {12}, {2} and {6}, {3} and {4}.\n"
      "Which pair, with one negative, adds to {-1}? {3} and {-4}.\n"
      "Answer: {" + lin(3) + " + " + lin(-4) + "}.\n"
      "Sign guide: c positive and b positive → both positive; c positive and b negative → both negative; c negative → different signs."),
     ("When x² has a coefficient",
      "For {poly([2, 'x²'], [7, 'x'], [3, ''])} the first terms of the brackets must multiply to {mono(2, 'x²')}: so ({mono(2, 'x')} …)(x …).\n"
      "The last terms must multiply to {3}: try {1} and {3}.\n"
      "{" + lin(1, 2) + " + " + lin(3) + "} gives {mono(6, 'x')} + x = {mono(7, 'x')}. ✓\n"
      "If the middle term is wrong, swap the numbers and try again. Expanding is the check.")],
    key_words=[("trinomial", "an expression with three terms"), ("quadratic", "the highest power of x is x²"),
               ("factor pair", "two numbers that multiply to a given number")],
    examples=["{poly([1, 'x²'], [5, 'x'], [6, ''])} = {" + lin(2) + " + " + lin(3) + "}",
              "{poly([1, 'x²'], [-6, 'x'], [8, ''])} = {" + lin(-2) + " + " + lin(-4) + "}",
              "{poly([1, 'x²'], [3, 'x'], [-10, ''])} = {" + lin(5) + " + " + lin(-2) + "}"],
    mistake=("{poly([1, 'x²'], [2, 'x'], [-8, ''])} = {" + lin(-4) + " + " + lin(2) + "}", "{poly([1, 'x²'], [2, 'x'], [-8, ''])} = {" + lin(4) + " + " + lin(-2) + "}",
             "Both pairs multiply to {-8}, but only {4} and {-2} add to {2}. Always check the sum.")))

# ---------------------------------------------------------------- 6. Difference of two squares
SRC = ["algebra-factorise"]
L.lesson(D, S, 6, ("m3-6", "Factorise a difference of two squares"), [3, 4],
  "A difference of two squares factorises as a² − b² = (a + b)(a − b).\n"
  "• Recognise it: two terms, both perfect squares, with a minus between them: x² − 25, 9y² − 4.\n"
  "• Take the square roots: x² − 25 = (x + 5)(x − 5); 9y² − 4 = (3y + 2)(3y − 2).\n"
  "• Take out a common factor first: 2x² − 18 = 2(x² − 9) = 2(x + 3)(x − 3).\n"
  "• A sum of two squares, x² + 25, does not factorise this way.\n"
  "• It helps in arithmetic: 53² − 47² = (53 + 47)(53 − 47) = 100 × 6 = 600.",
  worked({"k": 3, "m": 4},
         "Factorise fully {poly([k, 'x²'], [-k * m * m, ''])}.",
         ["Common factor first: {poly([k, 'x²'], [-k * m * m, ''])} = {bracket(k, [1, 'x²'], [-m * m, ''])}.",
          "x² − {m * m} is a difference of two squares: x² and {m}².",
          "So x² − {m * m} = {" + lin("m") + " + " + lin("-m") + "}."],
         "{k}{" + lin("m") + " + " + lin("-m") + "}", checks=["k * m * m == 48"]),
  [card("c3m6-1", "a² − b² = (a + b)(a − b): one bracket with plus, one with minus.",
        ["{poly([1, 'x²'], [-49, ''])} = {" + lin(7) + " + " + lin(-7) + "}"], "m3-6-x"),
   card("c3m6-2", "Find the square root of each term, including the numbers in front.",
        ["{poly([9, 'y²'], [-4, ''])} = {" + lin(2, 3, "y") + " + " + lin(-2, 3, "y") + "}"], "m3-6-coef"),
   card("c3m6-3", "Use the pattern to work out differences of squares quickly.",
        ["{53}² − {47}² = ({53} + {47})({53} − {47}) = {100} × {6} = {600}"], "m3-6-calc")],
  [mcq("m3-6-x", 1, "Factorise {poly([1, 'x²'], [-k * k, ''])}.",
       "{" + lin("k") + " + " + lin("-k") + "}",
       [("{" + lin("-k") + " + '²'}", "square"), ("{" + lin("k * k") + " + " + lin("-k * k") + "}", "noroot"), ("{" + lin("k") + " + '²'}", "plus")],
       ["x² − {k * k} = x² − {k}².", "a² − b² = (a + b)(a − b), so the answer is {answer}."],
       vars={"k": {"int": [2, 12]}},
       misc=[("square", "Expand it: you get a middle term {mono(-2 * k, 'x')} and +{k * k}."),
             ("noroot", "Take the square root of {k * k}: it is {k}."),
             ("plus", "Expand it: you get +{k * k}, but we need −{k * k}.")],
       sources=SRC),
   num("m3-6-calc", 1, "Use a² − b² = (a + b)(a − b) to work out {N + d}² − {N - d}².", "4 * N * d",
       ["({N + d} + {N - d})({N + d} − {N - d}) = {2 * N} × {2 * d}.", "= {answer}."],
       vars={"N": {"int": [20, 90], "step": 10}, "d": {"int": [1, 5]}},
       misc=[("sq", "4 * d * d", "That is ({N + d} − {N - d})² only; multiply the sum by the difference.")],
       sources=SRC),
   mcq("m3-6-coef", 2, "Factorise {poly([p * p, 'x²'], [-q * q, 'y²'])}.",
       "{'(' + poly([p, 'x'], [q, 'y']) + ')(' + poly([p, 'x'], [-q, 'y']) + ')'}",
       [("{'(' + poly([p, 'x'], [-q, 'y']) + ')²'}", "square"), ("{'(' + poly([p * p, 'x'], [q * q, 'y']) + ')(' + poly([p * p, 'x'], [-q * q, 'y']) + ')'}", "noroot"),
        ("{'(' + poly([p, 'x'], [q, 'y']) + ')²'}", "plus")],
       ["{mono(p * p, 'x²')} = ({mono(p, 'x')})² and {mono(q * q, 'y²')} = ({mono(q, 'y')})².", "So the answer is {answer}."],
       vars={"p": {"int": [2, 9]}, "q": {"int": [1, 9]}},
       misc=[("square", "Expand it: there is a middle term {mono(-2 * p * q, 'xy')}."),
             ("noroot", "Take square roots: √{p * p} = {p} and √{q * q} = {q}."),
             ("plus", "Expand it: the last term is +{mono(q * q, 'y²')}, but we need −{mono(q * q, 'y²')}.")],
       sources=SRC, where=["p != q"]),
   num("m3-6-find", 2, "{poly([1, 'x²'], [-k * k, ''])} = (x + a)(x − a) with a positive. Find a.", "k",
       ["x² − {k * k} = x² − {k}².", "So a = {answer}."],
       vars={"k": {"int": [3, 15]}},
       misc=[("half", "k * k / 2", "Halving is not the square root: {k} × {k} = {k * k}."), ("sq", "k * k", "a is the square root of {k * k}, not {k * k} itself.")],
       sources=SRC),
   mcq("m3-6-full", 3, "Factorise fully {poly([k, 'x²'], [-k * m * m, ''])}.",
       "{k}{" + lin("m") + " + " + lin("-m") + "}",
       [("{" + lin("m") + " + " + lin("-m") + "}", "lostk"), ("{bracket(k, [1, 'x²'], [-m * m, ''])}", "notfull"), ("{k}{" + lin("-m") + " + '²'}", "square")],
       ["Common factor first: {bracket(k, [1, 'x²'], [-m * m, ''])}.", "Then x² − {m * m} = {" + lin("m") + " + " + lin("-m") + "}. So the answer is {answer}."],
       vars={"k": {"int": [2, 7]}, "m": {"int": [2, 9]}},
       misc=[("lostk", "Expand it: you get {poly([1, 'x²'], [-m * m, ''])}, not {poly([k, 'x²'], [-k * m * m, ''])}. Keep the {k}."),
             ("notfull", "Not fully factorised: x² − {m * m} is a difference of two squares."),
             ("square", "Expand it: a square gives a middle term. The difference of squares needs one + bracket and one − bracket.")],
       sources=SRC, where=["k != m * m"])],
  learn=learn(
    [("Spotting a difference of two squares",
      "Last lesson's pattern backwards: (a + b)(a − b) = a² − b². So any expression of the form a² − b² can be factorised at once.\n"
      "Check three things:\n• exactly two terms;\n• each term is a perfect square ({mono(1, 'x²')}, {mono(25, '')}, {mono(9, 'y²')}, {mono(4, 'a²')} …);\n• a minus sign between them.\n"
      "Perfect squares to know: {1}, {4}, {9}, {16}, {25}, {36}, {49}, {64}, {81}, {100}, {121}, {144}."),
     ("Factorising it",
      "Take the square root of each term. One bracket gets plus, the other minus.\n"
      "• {poly([1, 'x²'], [-36, ''])} = {" + lin(6) + " + " + lin(-6) + "}\n"
      "• {poly([4, 'a²'], [-25, ''])} = {" + lin(5, 2, "a") + " + " + lin(-5, 2, "a") + "}, because {mono(4, 'a²')} = ({mono(2, 'a')})².\n"
      "Look for a common factor first: {poly([3, 'x²'], [-12, ''])} = {bracket(3, [1, 'x²'], [-4, ''])} = {3}{" + lin(2) + " + " + lin(-2) + "}.\n"
      "A sum such as x² + {9} cannot be factorised this way."),
     ("A shortcut in arithmetic",
      "The same pattern makes some sums easy without a calculator:\n"
      "{38}² − {32}² = ({38} + {32})({38} − {32}) = {70} × {6} = {420}.\n"
      "That is much quicker than squaring both numbers. Examiners like this type of question.")],
    key_words=[("perfect square", "a number or term that is something squared, like {49} = {7}²"),
               ("difference", "the result of a subtraction"), ("square root", "the number that was squared")],
    examples=["{poly([1, 'y²'], [-81, ''])} = {" + lin(9, 1, "y") + " + " + lin(-9, 1, "y") + "}",
              "{poly([16, 'x²'], [-1, ''])} = {" + lin(1, 4) + " + " + lin(-1, 4) + "}",
              "{75}² − {25}² = {100} × {50} = {5000}"],
    mistake=("{poly([1, 'x²'], [-16, ''])} = {" + lin(-4) + " + '²'}", "{poly([1, 'x²'], [-16, ''])} = {" + lin(4) + " + " + lin(-4) + "}",
             "{" + lin(-4) + " + '²'} expands to {poly([1, 'x²'], [-8, 'x'], [16, ''])}. A difference of squares needs one plus bracket and one minus bracket.")))

# ---------------------------------------------------------------- 7. Solving simple linear equations
SRC = ["algebra-equations"]
L.lesson(D, S, 7, ("m3-7", "Solve linear equations, with brackets, unknowns on both sides and fractions"), [2],
  "An equation stays true if you do the same thing to both sides.\n"
  "• Undo additions and subtractions first, then multiplications and divisions: 3x + 5 = 20 → 3x = 15 → x = 5.\n"
  "• Brackets: expand first. 4(x − 2) = 12 → 4x − 8 = 12 → x = 5.\n"
  "• Unknown on both sides: collect the x terms on one side and numbers on the other: 5x + 3 = 2x + 15 → 3x = 12 → x = 4.\n"
  "• Fractions: multiply both sides by the LCM of the denominators.\n"
  "• Check by substituting the answer into the original equation.",
  worked({"a": 5, "b": 3, "c": 2, "s": 4},
         "Solve {poly([a, 'x'], [b, ''])} = {poly([c, 'x'], [(a - c) * s + b, ''])}.",
         ["Subtract {mono(c, 'x')} from both sides: {poly([a - c, 'x'], [b, ''])} = {(a - c) * s + b}.",
          "Subtract {b} from both sides: {mono(a - c, 'x')} = {(a - c) * s}.",
          "Divide both sides by {a - c}: x = {s}.",
          "Check: {a} × {s} + {b} = {a * s + b} and {c} × {s} + {(a - c) * s + b} = {a * s + b}. ✓"],
         "x = {s}", checks=["s == 4"]),
  [card("c3m7-1", "Do the same to both sides. Undo + and − first, then × and ÷.",
        ["{poly([3, 'x'], [5, ''])} = {20} → {mono(3, 'x')} = {15} → x = {5}"], "m3-7-one"),
   card("c3m7-2", "With x on both sides, move the x terms to one side and the numbers to the other.",
        ["{poly([5, 'x'], [3, ''])} = {poly([2, 'x'], [15, ''])} → {mono(3, 'x')} = {12} → x = {4}"], "m3-7-both"),
   card("c3m7-3", "Fractions: multiply every term by the LCM of the denominators.",
        ["x ÷ {2} + x ÷ {3} = {5} → ×{6}: {mono(3, 'x')} + {mono(2, 'x')} = {30} → x = {6}"], "m3-7-frac")],
  [num("m3-7-one", 1, "Solve {poly([a, 'x'], [b, ''])} = {a * s + b}.", "s",
       ["{b < 0 ? 'Add ' + (0 - b) : 'Subtract ' + b} on both sides: {mono(a, 'x')} = {a * s}.", "Divide by {a}: x = {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [-20, 20]}, "s": {"int": [-9, 12]}},
       misc=[("add", "(a * s + 2 * b) / a", "Do the opposite on both sides: {b < 0 ? 'add ' + (0 - b) : 'subtract ' + b}, not {b < 0 ? 'subtract ' + (0 - b) : 'add ' + b}."),
             ("mul", "a * (a * s + b) - b", "Divide by {a} to undo multiplying by {a}.")],
       sources=SRC, where=["b != 0", "s != 0", "(a * s + 2 * b) / a != s"], signed=True),
   num("m3-7-br", 1, "Solve {bracket(a, [1, 'x'], [-b, ''])} = {a * (s - b)}.", "s",
       ["Expand: {poly([a, 'x'], [-a * b, ''])} = {a * (s - b)}.", "Add {a * b}: {mono(a, 'x')} = {a * s}. Divide by {a}: x = {answer}."],
       vars={"a": {"int": [2, 7]}, "b": {"int": [1, 9]}, "s": {"int": [-5, 15]}},
       misc=[("once", "(a * (s - b) + b) / a", "Expand the bracket fully: {a} × {br(-b)} = {-a * b}.")],
       sources=SRC, where=["s != b", "(a * (s - b) + b) / a != s"], signed=True),
   num("m3-7-both", 2, "Solve {poly([a, 'x'], [b, ''])} = {poly([c, 'x'], [(a - c) * s + b, ''])}.", "s",
       ["Subtract {mono(c, 'x')} from both sides: {poly([a - c, 'x'], [b, ''])} = {(a - c) * s + b}.",
        "{b < 0 ? 'Add ' + (0 - b) : 'Subtract ' + b} on both sides: {mono(a - c, 'x')} = {(a - c) * s}. Divide by {a - c}: x = {answer}."],
       vars={"a": {"int": [3, 9]}, "c": {"int": [1, 8]}, "b": {"int": [-15, 15]}, "s": {"int": [-8, 10]}},
       misc=[("addc", "((a - c) * s + 2 * b) / (a - c)", "{b < 0 ? 'Add ' + (0 - b) : 'Subtract ' + b} on both sides, do not {b < 0 ? 'subtract ' + (0 - b) : 'add ' + b}."),
             ("sumx", "((a - c) * s) / (a + c)", "Moving {mono(c, 'x')} to the left subtracts it: {a} − {c} = {a - c}.")],
       sources=SRC, where=["a > c", "b != 0", "s != 0", "((a - c) * s + 2 * b) / (a - c) != s"], signed=True),
   num("m3-7-frac", 2, "Solve x ÷ {m} + x ÷ {n} = {(m + n) * t}.", "m * n * t",
       ["Multiply every term by {m * n}: {mono(n, 'x')} + {mono(m, 'x')} = {(m + n) * t * m * n}.",
        "{mono(m + n, 'x')} = {(m + n) * t * m * n}, so x = {answer}."],
       vars={"m": {"pick": [2, 3, 4, 5]}, "n": {"pick": [3, 5, 7]}, "t": {"int": [1, 4]}},
       misc=[("one", "(m + n) * t * n", "Multiply every term by the LCM {m * n}, not just one term.")],
       sources=SRC, where=["m != n", "hcf(m, n) == 1"]),
   num("m3-7-fracbr", 3, "Solve {'(' + poly([1, 'x'], [m * t - s, '']) + ')'} ÷ {m} = {'(' + poly([1, 'x'], [n * t - s, '']) + ')'} ÷ {n}.", "s",
       ["Multiply both sides by {m * n}: {n}{'(' + poly([1, 'x'], [m * t - s, '']) + ')'} = {m}{'(' + poly([1, 'x'], [n * t - s, '']) + ')'}.",
        "Expand: {poly([n, 'x'], [n * (m * t - s), ''])} = {poly([m, 'x'], [m * (n * t - s), ''])}.",
        "Collect: {mono(n - m, 'x')} = {m * (n * t - s) - n * (m * t - s)}, so x = {answer}."],
       vars={"m": {"int": [2, 6]}, "n": {"int": [2, 7]}, "t": {"int": [1, 4]}, "s": {"int": [-6, 9]}},
       misc=[("nocross", "(m * (n * t - s) - (m * t - s)) / (n - m)", "Multiply the whole bracket by {n}, every term inside.")],
       sources=SRC, where=["m != n", "m * t - s != 0", "n * t - s != 0", "s != 0", "(m * (n * t - s) - (m * t - s)) / (n - m) != s"], signed=True)],
  learn=learn(
    [("The balance rule",
      "An equation is like a balance: both sides weigh the same. Whatever you do to one side, do to the other, and it stays balanced.\n"
      "To find x, undo what has been done to it, in reverse order. In {poly([3, 'x'], [5, ''])} = {20}, x was multiplied by {3}, then {5} was added. So:\n"
      "• subtract {5} from both sides: {mono(3, 'x')} = {15};\n• divide both sides by {3}: x = {5}.\n"
      "Check: {3} × {5} + {5} = {20}. ✓"),
     ("Brackets and x on both sides",
      "Expand brackets first: {bracket(4, [1, 'x'], [-2, ''])} = {12} becomes {poly([4, 'x'], [-8, ''])} = {12}, so {mono(4, 'x')} = {20} and x = {5}.\n"
      "If x is on both sides, gather the x terms on the side with more x:\n"
      "{poly([5, 'x'], [3, ''])} = {poly([2, 'x'], [15, ''])}: subtract {mono(2, 'x')} from both sides → {poly([3, 'x'], [3, ''])} = {15} → {mono(3, 'x')} = {12} → x = {4}."),
     ("Fractions",
      "Clear fractions by multiplying every term by the LCM of the denominators.\n"
      "x ÷ {2} + x ÷ {3} = {10}: the LCM of {2} and {3} is {6}.\n"
      "{6} × x ÷ {2} = {mono(3, 'x')}, {6} × x ÷ {3} = {mono(2, 'x')}, {6} × {10} = {60}.\n"
      "So {mono(5, 'x')} = {60} and x = {12}. Multiply every term, including the number on the right.")],
    key_words=[("equation", "a statement that two expressions are equal"), ("solve", "find the value of the unknown that makes it true"),
               ("unknown", "the letter whose value we look for"), ("LCM", "lowest common multiple of the denominators")],
    examples=["{poly([7, 'x'], [-4, ''])} = {31} → x = {5}",
              "{bracket(2, [1, 'x'], [3, ''])} = {poly([1, 'x'], [10, ''])} → x = {4}",
              "x ÷ {4} = {6} → x = {24}"],
    mistake=("{poly([3, 'x'], [4, ''])} = {19} → {mono(3, 'x')} = {23}", "{poly([3, 'x'], [4, ''])} = {19} → {mono(3, 'x')} = {15} → x = {5}",
             "To remove + {4} you subtract {4} from both sides. Doing the opposite operation is what keeps the balance.")))
