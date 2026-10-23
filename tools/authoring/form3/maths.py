"""Form 3 Maths, Term 1 (spine data/spine/form-3/mathematics.json, numbered by seq). Run: python tools/authoring/form3/maths.py
Reference lesson for every Form 3+ author (2026-10-23): Learn screens, 3 cards, a worked example, 5 practice questions
(levels 1, 1, 2, 2, 3), every wrong option with its own feedback, every number computed."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"
SRC = ["algebra-simplify"]

# ---------------------------------------------------------------- 2. Algebraic expressions (simplification)
L.lesson(D, S, 2, ("m3-2", "Simplify algebraic expressions: powers, products, quotients and brackets"), [],
  "To simplify an expression, write it with as few terms as possible.\n"
  "• Like terms have exactly the same letters and powers: 3x² and −5x² are like; 3x² and 3x are not.\n"
  "• Add or subtract like terms by their coefficients: 4x² + 2x² = 6x².\n"
  "• Multiply terms: multiply the numbers, then the letters; the same letter adds its powers: 2x × 3x = 6x², 2x × 5y = 10xy.\n"
  "• Divide terms: divide the numbers, then cancel letters: 12x²y ÷ 4x = 3xy.\n"
  "• Brackets: multiply every term inside by the number outside, sign included: −2(x − 3) = −2x + 6. Then collect like terms.",
  worked({"a": 3, "b": 2, "c": 1, "d": 2, "e": 4},
         "Simplify {bracket(a, [b, 'x'], [-c, ''])} − {bracket(d, [1, 'x'], [-e, ''])}.",
         ["Open the first bracket: {a} × {mono(b, 'x')} = {mono(a * b, 'x')} and {a} × {br(-c)} = {-a * c}.",
          "Open the second bracket with −{d}: −{d} × x = {mono(-d, 'x')} and −{d} × {br(-e)} = +{d * e}.",
          "Now {poly([a * b, 'x'], [-a * c, ''], [-d, 'x'], [d * e, ''])}.",
          "Collect: x terms {a * b} − {d} = {a * b - d}; numbers {br(-a * c)} + {d * e} = {d * e - a * c}."],
         "{poly([a * b - d, 'x'], [d * e - a * c, ''])}",
         checks=["a * b - d == 4", "d * e - a * c == 5"]),
  [card("c3m2-1", "Like terms have the same letters with the same powers. Only like terms can be added.",
        ["{mono(4, 'x²')} + {mono(2, 'x²')} = {mono(6, 'x²')}, but {mono(4, 'x²')} + {mono(2, 'x')} stays as it is."], "m3-2-powers"),
   card("c3m2-2", "To multiply terms, multiply the numbers, then the letters. The same letter twice gives a square.",
        ["{mono(2, 'x')} × {mono(3, 'x')} = {mono(6, 'x²')}", "{mono(2, 'x')} × {mono(5, 'y')} = {mono(10, 'xy')}"], "m3-2-times"),
   card("c3m2-3", "A number outside a bracket multiplies every term inside, with its sign.",
        ["{bracket(-2, [1, 'x'], [-3, ''])} = {poly([-2, 'x'], [6, ''])}"], "m3-2-minus")],
  [mcq("m3-2-powers", 1, "Simplify {poly([a, 'x²'], [b, 'x'], [c, 'x²'], [d, 'x'])}.",
       "{poly([a + c, 'x²'], [b + d, 'x'])}",
       [("{mono(a + b + c + d, 'x³')}", "join"), ("{poly([a + c, 'x⁴'], [b + d, 'x²'])}", "addpow"), ("{poly([a + b, 'x²'], [c + d, 'x'])}", "mix")],
       ["x² terms: {a} + {br(c)} = {a + c}.", "x terms: {b} + {br(d)} = {b + d}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [2, 9]}, "c": {"int": [-6, 6]}, "d": {"int": [-6, 6]}},
       misc=[("join", "x² and x are unlike terms: they stay separate."),
             ("addpow", "Adding like terms does not change the power: x² stays x²."),
             ("mix", "Add x² terms to x² terms and x terms to x terms only.")],
       sources=SRC, where=["c != 0 && d != 0", "a + c != 0 && b + d != 0", "a + b != a + c", "c < 0 || d < 0"]),
   mcq("m3-2-times", 1, "Simplify {mono(a, V[0])} × {mono(b, V[1])}.",
       "{mono(a * b, V[0] + V[1])}",
       [("{mono(a + b, V[0] + V[1])}", "add"), ("{poly([a * b, V[0]], [1, V[1]])}", "split"), ("{mono(a * b, V[0] + '²' + V[1])}", "square")],
       ["Multiply the numbers: {a} × {b} = {a * b}.", "Multiply the letters: {V[0]} × {V[1]} = {V[0]}{V[1]}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [2, 9]}, "V": {"pick": [["x", "y"], ["a", "b"], ["m", "n"], ["p", "q"]]}},
       misc=[("add", "Multiply the numbers, do not add them: {a} × {b} = {a * b}."),
             ("split", "The product of two letters is one term, {V[0]}{V[1]}, not a sum."),
             ("square", "Only the same letter twice gives a square; {V[0]} × {V[1]} = {V[0]}{V[1]}.")],
       sources=SRC, where=["a != b", "a * b != a + b"]),
   mcq("m3-2-minus", 2, "Expand and simplify {bracket(a, [1, 'x'], [b, ''])} − {bracket(c, [1, 'x'], [-d, ''])}.",
       "{poly([a - c, 'x'], [a * b + c * d, ''])}",
       [("{poly([a - c, 'x'], [a * b - c * d, ''])}", "sign"), ("{poly([a - c, 'x'], [a * b + d, ''])}", "once"), ("{poly([a + c, 'x'], [a * b + c * d, ''])}", "xsign")],
       ["Open the brackets: {poly([a, 'x'], [a * b, ''])} and −{c} × x = {mono(-c, 'x')}, −{c} × {br(-d)} = +{c * d}.",
        "x terms: {a} − {c} = {a - c}; numbers: {a * b} + {c * d} = {a * b + c * d}.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [1, 9]}, "c": {"int": [2, 9]}, "d": {"int": [1, 9]}},
       misc=[("sign", "−{c} × −{d} = +{c * d}: two negatives give a positive."),
             ("once", "Multiply every term in the bracket by {c}: −{c} × {br(-d)} = +{c * d}, not +{d}."),
             ("xsign", "The second bracket is subtracted: −{c} × x = {mono(-c, 'x')}.")],
       sources=SRC, where=["a != c", "d != 1", "c * d != d", "a * b - c * d != a * b + d"]),
   num("m3-2-coef", 2, "Expand and simplify {bracket(a, [b, 'x'], [c, ''])} + {bracket(d, [e, 'x'], [-f, ''])}. What is the coefficient of x?",
       "a * b + d * e",
       ["{a} × {mono(b, 'x')} = {mono(a * b, 'x')} and {d} × {mono(e, 'x')} = {mono(d * e, 'x')}.",
        "Add the x terms: {a * b} + {d * e} = {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [1, 5]}, "c": {"int": [1, 9]}, "d": {"int": [2, 6]}, "e": {"int": [1, 5]}, "f": {"int": [1, 9]}},
       misc=[("nomult", "b + e", "Multiply each x term by the number outside its bracket first: {a} × {b} and {d} × {e}."),
             ("const", "a * b + d * e + a * c - d * f", "That adds the numbers too; the coefficient of x counts only the x terms.")],
       sources=SRC, where=["a * b + d * e != b + e", "a * c != d * f"]),
   mcq("m3-2-divide", 3, "Simplify {mono(a * b, V[0] + '²' + V[1])} ÷ {mono(a, V[0])}.",
       "{mono(b, V[0] + V[1])}",
       [("{mono(b, V[0] + '²' + V[1])}", "keep"), ("{mono(b, V[1])}", "all"), ("{mono(a * b - a, V[0] + V[1])}", "subtract")],
       ["Divide the numbers: {a * b} ÷ {a} = {b}.", "{V[0]}² ÷ {V[0]} = {V[0]}; {V[1]} stays.", "So the answer is {answer}."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [2, 9]}, "V": {"pick": [["x", "y"], ["a", "b"], ["m", "n"], ["p", "q"]]}},
       misc=[("keep", "Dividing by {V[0]} removes one {V[0]}: {V[0]}² ÷ {V[0]} = {V[0]}."),
             ("all", "{V[0]}² is {V[0]} × {V[0]}: dividing by {V[0]} leaves one {V[0]}."),
             ("subtract", "Divide the numbers, do not subtract them: {a * b} ÷ {a} = {b}.")],
       sources=SRC, where=["b != 1", "a * b - a != b"])],
  learn=learn(
    [("Like terms, now with powers",
      "Last year you collected like terms such as {mono(3, 'x')} + {mono(5, 'x')}. Now the terms can have powers. "
      "Two terms are like terms only if they have exactly the same letters with exactly the same powers.\n"
      "• {mono(3, 'x²')} and {mono(-5, 'x²')} are like terms: {mono(3, 'x²')} − {mono(5, 'x²')} = {mono(-2, 'x²')}.\n"
      "• {mono(3, 'x²')} and {mono(3, 'x')} are not like terms: x² means x × x, a different quantity from x.\n"
      "• {mono(4, 'xy')} and {mono(2, 'yx')} are like terms, because xy = yx.\n"
      "Adding like terms changes only the coefficient, never the letters or the power."),
     ("Multiplying and dividing terms",
      "Multiplying is different from adding: any two terms can be multiplied, like or not.\n"
      "Multiply the numbers, then put the letters together. The same letter twice makes a square.\n"
      "• {mono(4, 'x')} × {mono(3, 'y')} = {mono(12, 'xy')}\n"
      "• {mono(2, 'x')} × {mono(5, 'x')} = {mono(10, 'x²')}\n"
      "Dividing works backwards: divide the numbers, then cancel the letters that appear above and below.\n"
      "• {mono(12, 'x²y')} ÷ {mono(4, 'x')} = {mono(3, 'xy')}, because x² ÷ x = x."),
     ("Brackets with a minus sign",
      "The number in front of a bracket multiplies every term inside it, and its sign comes too.\n"
      "{bracket(-3, [1, 'x'], [-4, ''])} = {-3} × x + {br(-3)} × {br(-4)} = {poly([-3, 'x'], [12, ''])}.\n"
      "Remember: a negative times a negative is positive.\n"
      "After opening all brackets, collect the like terms to finish:\n"
      "{bracket(2, [1, 'x'], [5, ''])} − {bracket(3, [1, 'x'], [-1, ''])} = {poly([2, 'x'], [10, ''], [-3, 'x'], [3, ''])} = {poly([-1, 'x'], [13, ''])}.")],
    key_words=[("like terms", "terms with the same letters and the same powers"),
               ("coefficient", "the number in front of the letters, with its sign"),
               ("expand", "remove the brackets by multiplying every term inside"),
               ("simplify", "write with as few terms as possible")],
    examples=["{mono(7, 'a²')} − {mono(2, 'a²')} + {mono(3, 'a')} = {poly([5, 'a²'], [3, 'a'])}",
              "{mono(6, 'p')} × {mono(2, 'q')} = {mono(12, 'pq')}",
              "{mono(15, 'm²n')} ÷ {mono(5, 'm')} = {mono(3, 'mn')}"],
    mistake=("{mono(5, 'x²')} + {mono(3, 'x')} = {mono(8, 'x³')}", "{poly([5, 'x²'], [3, 'x'])} cannot be simplified",
             "x² and x are unlike terms. Only like terms can be added, and adding never changes the power.")))
