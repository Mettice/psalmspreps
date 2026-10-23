"""Form 3 Maths, Term 1, rows 8-12 (simultaneous equations, word problems, quadratic equations).
Run: python tools/authoring/form3/maths_equations.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"


def eq(a, b, c, x="x", y="y"):
    """{…} for the equation a·x + b·y = c."""
    return "{poly([" + a + ", '" + x + "'], [" + b + ", '" + y + "'])} = {" + c + "}"


def lin(a, c="1", v="x"):
    return f"'(' + poly([{c}, '{v}'], [{a}, '']) + ')'"


PAIR = "{'x = ' + fmt(s) + ', y = ' + fmt(t)}"


def pair(x, y):
    return "{'x = ' + fmt(" + x + ") + ', y = ' + fmt(" + y + ")}"


SIM = {"s": {"int": [-6, 9]}, "t": {"int": [-6, 9]}}

# ---------------------------------------------------------------- 8. Simultaneous equations: elimination
SRC = ["simultaneous"]
L.lesson(D, S, 8, ("m3-8", "Solve simultaneous linear equations by elimination"), [7],
  "Two equations with two unknowns, solved together, are simultaneous equations. The solution is a pair (x, y) that makes both true.\n"
  "Elimination method:\n"
  "• Make the coefficients of one unknown the same size (multiply one or both equations if needed).\n"
  "• Same signs → subtract the equations; opposite signs → add them. That unknown disappears.\n"
  "• Solve for the other unknown, then substitute back to find the first.\n"
  "• Check in both original equations.",
  worked({"s": 3, "t": -1, "a": 2, "b": 3, "c": 5, "d": 1},
         "Solve " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "d", "c * s + d * t") + ".",
         ["Multiply the second equation by {b} so both have {mono(b, 'y')}: " + eq("c * b", "d * b", "(c * s + d * t) * b") + ".",
          "Same sign: subtract the first equation from it: {mono(c * b - a, 'x')} = {(c * s + d * t) * b - (a * s + b * t)}, so x = {s}.",
          "Substitute x = {s} in the second equation: {c * s} + y = {c * s + d * t}, so y = {t}.",
          "Check in the first: {a} × {s} + {b} × {br(t)} = {a * s + b * t}. ✓"],
         PAIR, checks=["c * b - a == 13"]),
  [card("c3m8-1", "Opposite signs in front of the same unknown: add the equations to eliminate it.",
        ["{poly([1, 'x'], [1, 'y'])} = {7} and {poly([1, 'x'], [-1, 'y'])} = {1}: adding gives {mono(2, 'x')} = {8}, so x = {4}, y = {3}."], "m3-8-which"),
   card("c3m8-2", "Same sign: subtract one equation from the other.",
        ["{poly([3, 'x'], [2, 'y'])} = {12} and {poly([1, 'x'], [2, 'y'])} = {8}: subtracting gives {mono(2, 'x')} = {4}, so x = {2}, y = {3}."], "m3-8-add"),
   card("c3m8-3", "If no coefficients match, multiply an equation first so that they do.",
        ["{poly([2, 'x'], [1, 'y'])} = {7} times {3} gives {poly([6, 'x'], [3, 'y'])} = {21}, which matches {mono(3, 'y')} in another equation."], "m3-8-mult")],
  [mcq("m3-8-which", 1, "To eliminate y from " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "g * b", "c * s + g * b * t") + ", what should you do?",
       "{g == -1 ? 'Add the two equations' : 'Subtract one equation from the other'}",
       [("{g == -1 ? 'Subtract one equation from the other' : 'Add the two equations'}", "op"), ("{'Multiply the first equation by ' + b}", "mult"), ("Divide both equations by y", "div")],
       ["The y terms are {mono(b, 'y')} and {mono(g * b, 'y')}.", "{g == -1 ? 'Opposite signs: adding makes them cancel.' : 'Same sign: subtracting makes them cancel.'}", "So: {answer}."],
       vars={"a": {"int": [1, 6]}, "b": {"int": [2, 6]}, "c": {"int": [1, 6]}, "g": {"pick": [1, -1]}, **SIM},
       misc=[("op", "{g == -1 ? 'Subtracting gives ' + mono(2 * b, 'y') + ': y is still there. Opposite signs cancel when you add.' : 'Adding gives ' + mono(2 * b, 'y') + ': y is still there. Equal terms cancel when you subtract.'}"),
             ("mult", "The y coefficients already have the same size, {b}: no need to multiply."),
             ("div", "You cannot divide by an unknown; eliminate y by adding or subtracting the equations.")],
       sources=SRC, where=["a != c"]),
   num("m3-8-add", 1, "Solve " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "-b", "c * s - b * t") + ". What is x?", "s",
       ["Add the equations: the y terms cancel. {mono(a + c, 'x')} = {(a + c) * s}.", "Divide by {a + c}: x = {answer}."],
       vars={"a": {"int": [1, 6]}, "b": {"int": [1, 6]}, "c": {"int": [1, 6]}, **SIM},
       misc=[("sub", "((a * s + b * t) - (c * s - b * t)) / (a - c)", "Subtracting keeps the y terms: {mono(b, 'y')} − ({mono(-b, 'y')}) = {mono(2 * b, 'y')}. Add instead.")],
       sources=SRC, where=["a != c", "s != 0", "((a * s + b * t) - (c * s - b * t)) / (a - c) != s"], signed=True),
   num("m3-8-mult", 2, "Solve " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "1", "c * s + t") + ". What is y?", "t",
       ["Multiply the second equation by {a}: " + eq("a * c", "a", "a * (c * s + t)") + ".",
        "Multiply the first by {c}: " + eq("a * c", "b * c", "c * (a * s + b * t)") + ".",
        "Subtract: {mono(b * c - a, 'y')} = {c * (a * s + b * t) - a * (c * s + t)}, so y = {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [2, 6]}, "c": {"int": [2, 6]}, **SIM},
       misc=[("x", "s", "That is x. The question asks for y."),
             ("nomult", "(a * s + b * t - (c * s + t)) / (b - 1)", "Subtracting without first making the x coefficients equal leaves x in the equation.")],
       sources=SRC, where=["b * c != a", "a != c", "s != t", "b != 1", "(a * s + b * t - (c * s + t)) / (b - 1) != t"], signed=True),
   num("m3-8-x", 2, "Solve " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "d", "c * s + d * t") + ". What is x?", "s",
       ["Make the y coefficients equal: multiply the first equation by {d} and the second by {b}.",
        "{mono(a * d, 'x')} − {mono(c * b, 'x')} = {d * (a * s + b * t)} − {b * (c * s + d * t)}, so {mono(a * d - b * c, 'x')} = {(a * d - b * c) * s}.",
        "x = {answer}."],
       vars={"a": {"int": [2, 7]}, "b": {"int": [2, 5]}, "c": {"int": [2, 7]}, "d": {"int": [2, 5]}, **SIM},
       misc=[("y", "t", "That is y. The question asks for x.")],
       sources=SRC, where=["a * d != b * c", "b != d", "s != t"], signed=True),
   mcq("m3-8-pair", 3, "Solve " + eq("a", "b", "a * s + b * t") + " and " + eq("c", "-d", "c * s - d * t") + ".",
       PAIR,
       [(pair("t", "s"), "swap"), (pair("-s", "-t"), "sign"), (pair("s", "-t"), "ysign")],
       ["Multiply to match the y coefficients, then add (the signs are opposite).", "x = {s}; substitute back: y = {t}.",
        "Check: {a} × {br(s)} + {b} × {br(t)} = {a * s + b * t}. ✓", "So {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [2, 5]}, "c": {"int": [2, 6]}, "d": {"int": [2, 5]}, "s": {"int": [-6, 9]}, "t": {"int": [1, 9]}},
       misc=[("swap", "Check in the first equation: {a} × {br(t)} + {b} × {br(s)} = {a * t + b * s}, not {a * s + b * t}."),
             ("sign", "Check in the first equation: {a} × {br(-s)} + {b} × {br(-t)} = {-(a * s + b * t)}, not {a * s + b * t}."),
             ("ysign", "Check in the first equation: {a} × {br(s)} + {b} × {br(-t)} = {a * s - b * t}, not {a * s + b * t}.")],
       sources=SRC, where=["a * d != -b * c", "a * d + b * c != 0", "s != t", "s != 0", "a * t + b * s != a * s + b * t", "a * s - b * t != a * s + b * t"])],
  learn=learn(
    [("Two equations, two unknowns",
      "Ayuk buys pens and books. One equation such as x + y = {7} has many solutions ({1} and {6}, {2} and {5}…). "
      "A second fact, such as x − y = {1}, narrows it down to one pair that makes both true: x = {4}, y = {3}.\n"
      "Equations solved together like this are simultaneous equations. The solution is always a pair of values."),
     ("Elimination: make one unknown disappear",
      "Look at the coefficients of one unknown.\n"
      "• Opposite signs, same size ({mono(2, 'y')} and {mono(-2, 'y')}): add the equations.\n"
      "• Same sign, same size ({mono(3, 'x')} and {mono(3, 'x')}): subtract them.\n"
      "That unknown is eliminated, leaving one equation with one unknown. Solve it, then substitute the value into either original equation to find the other unknown."),
     ("When nothing matches yet",
      "In {poly([2, 'x'], [3, 'y'])} = {13} and {poly([5, 'x'], [1, 'y'])} = {13}, no coefficients match. Multiply the second equation by {3}: {poly([15, 'x'], [3, 'y'])} = {39}.\n"
      "Now both have {mono(3, 'y')}. Subtract the first: {mono(13, 'x')} = {26}, so x = {2}. Then {5} × {2} + y = {13} gives y = {3}.\n"
      "Remember to multiply every term, including the number on the right.")],
    key_words=[("simultaneous equations", "two equations solved together for the same unknowns"),
               ("eliminate", "remove one unknown by adding or subtracting the equations"),
               ("substitute", "put a known value in place of a letter")],
    examples=["{poly([1, 'x'], [1, 'y'])} = {10}, {poly([1, 'x'], [-1, 'y'])} = {2} → x = {6}, y = {4}",
              "{poly([2, 'x'], [1, 'y'])} = {8}, {poly([1, 'x'], [1, 'y'])} = {5} → subtract: x = {3}, y = {2}"],
    mistake=("{poly([2, 'x'], [1, 'y'])} = {7} times {3}: {poly([6, 'x'], [3, 'y'])} = {7}", "{poly([6, 'x'], [3, 'y'])} = {21}",
             "Multiplying an equation means multiplying every term on both sides, the number on the right too.")))

# ---------------------------------------------------------------- 9. Simultaneous equations: substitution
SRC = ["simultaneous"]
L.lesson(D, S, 9, ("m3-9", "Solve simultaneous linear equations by substitution"), [8],
  "Substitution method:\n"
  "• Make one unknown the subject of one equation (choose one with a coefficient of 1 if you can): y = 2x − 1.\n"
  "• Substitute that expression into the other equation, in brackets: 3x + 2(2x − 1) = 12.\n"
  "• Solve for the remaining unknown, then substitute back to find the other.\n"
  "Substitution is easiest when one equation already gives y = … or x = …. Both methods give the same answer.",
  worked({"m": 2, "c": -1, "a": 3, "b": 2, "s": 2},
         "Solve y = {poly([m, 'x'], [c, ''])} and " + eq("a", "b", "a * s + b * (m * s + c)") + ".",
         ["Substitute y = {poly([m, 'x'], [c, ''])} into the second equation: {mono(a, 'x')} + {b}{" + lin("c", "m") + "} = {a * s + b * (m * s + c)}.",
          "Expand: {poly([a + b * m, 'x'], [b * c, ''])} = {a * s + b * (m * s + c)}, so {mono(a + b * m, 'x')} = {(a + b * m) * s} and x = {s}.",
          "Back-substitute: y = {m} × {s} + {br(c)} = {m * s + c}."],
         pair("s", "m * s + c"), checks=["a + b * m == 7"]),
  [card("c3m9-1", "Substitute the expression for y into the other equation, in brackets.",
        ["y = {poly([2, 'x'], [1, ''])} into {poly([1, 'x'], [1, 'y'])} = {7}: x + {" + lin(1, 2) + "} = {7}, so {mono(3, 'x')} = {6}, x = {2}."], "m3-9-x"),
   card("c3m9-2", "Make a letter the subject first if neither equation gives it.",
        ["x + {mono(3, 'y')} = {10} → x = {10} − {mono(3, 'y')}"], "m3-9-subject"),
   card("c3m9-3", "After finding one unknown, substitute back to find the other.",
        ["x = {2} in y = {poly([3, 'x'], [-1, ''])}: y = {6} − {1} = {5}."], "m3-9-y")],
  [num("m3-9-x", 1, "Solve y = {poly([m, 'x'], [c, ''])} and " + eq("a", "1", "a * s + m * s + c") + ". What is x?", "s",
       ["Substitute: {mono(a, 'x')} + {" + lin("c", "m") + "} = {a * s + m * s + c}.", "{mono(a + m, 'x')} = {(a + m) * s}, so x = {answer}."],
       vars={"m": {"int": [1, 5]}, "c": {"int": [-9, 9]}, "a": {"int": [1, 5]}, "s": {"int": [-5, 8]}},
       misc=[("y", "m * s + c", "That is y. Find x first: substitute y into the second equation.")],
       sources=SRC, where=["c != 0", "s != 0", "m * s + c != s"], signed=True),
   mcq("m3-9-subject", 1, "Make x the subject of " + eq("1", "b", "c") + ".",
       "{'x = ' + c + ' − ' + mono(b, 'y')}",
       [("{'x = ' + c + ' + ' + mono(b, 'y')}", "sign"), ("{'x = ' + mono(b, 'y') + ' − ' + c}", "order"), ("{'x = ' + c + ' − y'}", "coef")],
       ["Subtract {mono(b, 'y')} from both sides.", "So {answer}."],
       vars={"b": {"int": [2, 9]}, "c": {"int": [3, 30]}},
       misc=[("sign", "{mono(b, 'y')} is added on the left, so subtract it from both sides."),
             ("order", "Check with y = {0}: x would be {-c}, but the equation gives x = {c}."),
             ("coef", "Subtract the whole term {mono(b, 'y')}, not just y.")],
       sources=SRC),
   num("m3-9-y", 2, "Solve y = {poly([m, 'x'], [c, ''])} and " + eq("a", "b", "a * s + b * (m * s + c)") + ". What is y?", "m * s + c",
       ["Substitute: {mono(a, 'x')} + {b}{" + lin("c", "m") + "} = {a * s + b * (m * s + c)}.",
        "{poly([a + b * m, 'x'], [b * c, ''])} = {a * s + b * (m * s + c)}, so x = {s}.", "y = {m} × {br(s)} + {br(c)} = {answer}."],
       vars={"m": {"int": [-3, 4]}, "c": {"int": [-9, 9]}, "a": {"int": [1, 5]}, "b": {"int": [2, 4]}, "s": {"int": [-5, 6]}},
       misc=[("x", "s", "That is x. Substitute it back into y = {poly([m, 'x'], [c, ''])} to find y.")],
       sources=SRC, where=["m != 0", "c != 0", "a + b * m != 0", "m * s + c != s"], signed=True),
   num("m3-9-xsub", 2, "Solve x = {poly([p, 'y'], [q, ''])} and " + eq("a", "b", "a * (p * t + q) + b * t") + ". What is y?", "t",
       ["Substitute: {a}{" + lin("q", "p", "y") + "} + {mono(b, 'y')} = {a * (p * t + q) + b * t}.",
        "{poly([a * p + b, 'y'], [a * q, ''])} = {a * (p * t + q) + b * t}, so {mono(a * p + b, 'y')} = {(a * p + b) * t} and y = {answer}."],
       vars={"p": {"int": [1, 4]}, "q": {"int": [-8, 8]}, "a": {"int": [2, 5]}, "b": {"int": [1, 5]}, "t": {"int": [-5, 7]}},
       misc=[("noexp", "(a * (p * t + q) + b * t - q) / (p + b)", "Multiply the whole bracket by {a}: {a} × {br(q)} = {a * q}.")],
       sources=SRC, where=["q != 0", "t != 0", "(a * (p * t + q) + b * t - q) / (p + b) != t"], signed=True),
   mcq("m3-9-meet", 3, "The lines y = {poly([m, 'x'], [c, ''])} and y = {poly([n, 'x'], [d, ''])} meet at one point. Find it.",
       pair("s", "m * s + c"),
       [(pair("m * s + c", "s"), "swap"), (pair("s", "n * s + c"), "mix"), (pair("-s", "m * s + c"), "sign")],
       ["At the meeting point both y values are equal: {poly([m, 'x'], [c, ''])} = {poly([n, 'x'], [d, ''])}.",
        "{mono(m - n, 'x')} = {d - c}, so x = {s}; y = {m} × {br(s)} + {br(c)} = {m * s + c}.", "The point is {answer}."],
       vars={"m": {"int": [-4, 5]}, "n": {"int": [-4, 5]}, "s": {"int": [-5, 6]}, "c": {"int": [-9, 9]}, "d": {"expr": "c + (m - n) * s"}},
       misc=[("swap", "x comes first in a coordinate pair: the point has x = {s}."),
             ("mix", "Substitute x = {s} into one whole equation: y = {m} × {br(s)} + {br(c)} = {m * s + c}."),
             ("sign", "Check the sign: dividing {d - c} by {m - n} gives x = {s}, not {-s}.")],
       sources=SRC, where=["m != n", "m != 0 && n != 0", "s != 0", "m * s + c != s", "n * s + c != m * s + c", "c != d"])],
  learn=learn(
    [("Using what one equation tells you",
      "If one equation already says what y is, for example y = {poly([2, 'x'], [1, ''])}, you can replace y in the other equation by that expression.\n"
      "Take {poly([1, 'x'], [1, 'y'])} = {7}. Replace y: x + {" + lin(1, 2) + "} = {7}.\n"
      "Now there is only one unknown: {poly([3, 'x'], [1, ''])} = {7}, so x = {2}. Then y = {2} × {2} + {1} = {5}.\n"
      "Always put the expression in brackets, so that every term is multiplied correctly."),
     ("Making a subject first",
      "If neither equation starts with y = or x =, rearrange one. Choose the unknown whose coefficient is {1}.\n"
      "From x + {mono(3, 'y')} = {10}, subtract {mono(3, 'y')} from both sides: x = {10} − {mono(3, 'y')}.\n"
      "Then substitute that into the other equation, solve for y, and come back for x."),
     ("Where two lines meet",
      "Each linear equation is a straight line. The solution of the pair is the point where the lines cross.\n"
      "If y = {poly([2, 'x'], [1, ''])} and y = {poly([-1, 'x'], [7, ''])}, both y values are equal there: {poly([2, 'x'], [1, ''])} = {poly([-1, 'x'], [7, ''])}, so {mono(3, 'x')} = {6} and x = {2}.\n"
      "Then y = {5}: the lines meet at ({2}, {5}).")],
    key_words=[("substitute", "replace a letter by a value or an expression"), ("subject", "the letter on its own on one side, as y in y = …"),
               ("point of intersection", "where two lines cross: the solution of their equations")],
    examples=["y = x + {3} and {poly([2, 'x'], [1, 'y'])} = {12}: {mono(2, 'x')} + x + {3} = {12}, x = {3}, y = {6}",
              "x = {mono(2, 'y')} and {poly([1, 'x'], [1, 'y'])} = {9}: {mono(3, 'y')} = {9}, y = {3}, x = {6}"],
    mistake=("y = x − {2} into {poly([3, 'x'], [-1, 'y'])} = {10}: {mono(3, 'x')} − x − {2} = {10}", "{mono(3, 'x')} − (x − {2}) = {10}, so {mono(2, 'x')} + {2} = {10}",
             "Without brackets the sign of {2} is wrong: subtracting (x − {2}) gives − x + {2}.")))

# ---------------------------------------------------------------- 10. Equations from real-life problems
SRC = ["word-problems"]
L.lesson(D, S, 10, ("m3-10", "Build and solve equations from real-life problems"), [7, 8],
  "To solve a word problem with algebra:\n"
  "1. Choose a letter for the unknown and say what it means (let x be Bih's age in years).\n"
  "2. Write every other quantity in terms of it (her brother: x + 3).\n"
  "3. Use the fact in the problem to write an equation (x + x + 3 = 25).\n"
  "4. Solve it, and answer the question in words with units.\n"
  "5. Check the answer makes sense (an age cannot be negative, a price is in FCFA).\n"
  "Two unknowns need two facts: write two equations and solve them simultaneously.",
  worked({"w": 6, "k": 4},
         "A rectangular garden in Buea is {k} m longer than it is wide. Its perimeter is {4 * w + 2 * k} m. Find its width.",
         ["Let the width be x m. Then the length is (x + {k}) m.",
          "Perimeter: {2}(x + x + {k}) = {4 * w + 2 * k}, so {poly([4, 'x'], [2 * k, ''])} = {4 * w + 2 * k}.",
          "{mono(4, 'x')} = {4 * w}, so x = {w}.",
          "Check: width {w} m, length {w + k} m, perimeter {2} × ({w} + {w + k}) = {4 * w + 2 * k} m. ✓"],
         "The width is {w} m.", checks=["w == 6"]),
  [card("c3m10-1", "Say what the letter stands for, then write the other quantities with it.",
        ["Let x be Bih's age. Her brother is {3} years older: x + {3}."], "m3-10-model"),
   card("c3m10-2", "The fact in the problem becomes the equation.",
        ["Together they are {25}: x + x + {3} = {25}, so x = {11}."], "m3-10-consec"),
   card("c3m10-3", "Answer in words, with units, and check it makes sense.",
        ["Bih is {11} years old and her brother {14}: {11} + {14} = {25}. ✓"], "m3-10-rect")],
  [mcq("m3-10-model", 1, "Bih is x years old. Her brother is {d} years older. Together their ages add up to {2 * x0 + d}. Which equation is right?",
       "{'x + (x + ' + d + ') = ' + (2 * x0 + d)}",
       [("{'x + ' + d + ' = ' + (2 * x0 + d)}", "one"), ("{'x(x + ' + d + ') = ' + (2 * x0 + d)}", "times"), ("{'x + (x − ' + d + ') = ' + (2 * x0 + d)}", "minus")],
       ["Bih: x. Her brother is {d} years older: x + {d}.", "Together: {answer}."],
       vars={"d": {"int": [2, 9]}, "x0": {"int": [8, 16]}},
       misc=[("one", "x + {d} is only the brother's age. Add Bih's age x too."),
             ("times", "\"Together\" means add the ages, not multiply them."),
             ("minus", "Older means more years: the brother's age is x + {d}.")],
       sources=SRC),
   num("m3-10-consec", 1, "Three consecutive whole numbers add up to {3 * n + 3}. What is the smallest?", "n",
       ["Let the smallest be x. The numbers are x, x + {1}, x + {2}.", "{mono(3, 'x')} + {3} = {3 * n + 3}, so x = {answer}."],
       vars={"n": {"int": [5, 60]}},
       misc=[("mid", "n + 1", "{n + 1} is the middle number. The smallest is {n}."), ("third", "n + 2", "{n + 2} is the largest of the three numbers.")],
       sources=SRC),
   num("m3-10-rect", 2, "A rectangular classroom floor is {k} m longer than it is wide. Its perimeter is {4 * w + 2 * k} m. What is its width in metres?", "w",
       ["Let the width be x m; the length is (x + {k}) m.", "{2}(x + x + {k}) = {4 * w + 2 * k} → {mono(4, 'x')} + {2 * k} = {4 * w + 2 * k} → x = {answer}."],
       vars={"w": {"int": [3, 15]}, "k": {"int": [1, 9]}},
       misc=[("len", "w + k", "{w + k} m is the length. The question asks for the width."),
             ("half", "(4 * w + 2 * k - k) / 2", "The perimeter goes round all four sides: {2}(x + x + {k}).")],
       unit="m", sources=SRC, where=["(4 * w + 2 * k - k) / 2 != w"]),
   num("m3-10-shop", 2, "At Mile 17 market, {a} pens and {b} exercise books cost {a * p + b * q} FCFA. {c} pens and {d} exercise books cost {c * p + d * q} FCFA. What does one exercise book cost (FCFA)?", "q",
       ["Let a pen cost x FCFA and a book y FCFA: " + eq("a", "b", "a * p + b * q") + " and " + eq("c", "d", "c * p + d * q") + ".",
        "Eliminate x: multiply the first by {c} and the second by {a}, then subtract: {mono(b * c - a * d, 'y')} = {c * (a * p + b * q) - a * (c * p + d * q)}.",
        "y = {answer} FCFA."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [1, 5]}, "c": {"int": [1, 5]}, "d": {"int": [1, 5]}, "p": {"int": [100, 400], "step": 50}, "q": {"int": [150, 600], "step": 50}},
       misc=[("pen", "p", "That is the price of a pen. The question asks for an exercise book.")],
       sources=SRC, where=["a * d != b * c", "p != q"]),
   num("m3-10-age", 3, "A father is {m} times as old as his son. In {y} years' time he will be {k} times as old as his son. How old is the son now?", "s",
       ["Let the son be x years old; the father is {mono(m, 'x')}.", "In {y} years: {mono(m, 'x')} + {y} = {k}(x + {y}).",
        "{poly([m, 'x'], [y, ''])} = {poly([k, 'x'], [k * y, ''])} → {mono(m - k, 'x')} = {k * y - y} → x = {answer}."],
       vars={"s": {"int": [3, 15]}, "m": {"int": [3, 7]}, "y": {"int": [2, 24]}, "k": {"expr": "(m * s + y) / (s + y)"}},
       misc=[("father", "m * s", "{m * s} is the father's age. The question asks for the son's."),
             ("future", "s + y", "That is the son's age in {y} years. The question asks for his age now.")],
       unit="years", sources=SRC, where=["isInt(k)", "k > 1", "k < m"])],
  learn=learn(
    [("From words to algebra",
      "Many everyday problems hide an equation. The skill is to translate the words.\n"
      "• \"{3} more than x\" is x + {3}; \"{3} less than x\" is x − {3}.\n• \"twice x\" is {mono(2, 'x')}; \"half of x\" is x ÷ {2}.\n"
      "• \"together\" or \"in total\" means add; \"is\" or \"equals\" gives the equals sign.\n"
      "Start by writing \"Let x be …\" with the quantity and its unit. It keeps your work clear and earns marks in exams."),
     ("A worked story",
      "Ngozi and Tabe share {5000} FCFA. Tabe gets {1000} FCFA more than Ngozi. How much does Ngozi get?\n"
      "Let Ngozi's share be x FCFA. Tabe's is x + {1000}.\n"
      "Together: x + x + {1000} = {5000}, so {mono(2, 'x')} = {4000} and x = {2000}.\n"
      "Ngozi gets {2000} FCFA and Tabe {3000} FCFA. Check: {2000} + {3000} = {5000}. ✓"),
     ("Two unknowns",
      "When two quantities are unknown, such as the price of a pen and of a book, give each a letter and look for two facts.\n"
      "{2} pens and {1} book cost {700} FCFA; {1} pen and {1} book cost {500} FCFA.\n"
      "{poly([2, 'x'], [1, 'y'])} = {700} and {poly([1, 'x'], [1, 'y'])} = {500}. Subtract: x = {200}, so y = {300}.\n"
      "A pen costs {200} FCFA and a book {300} FCFA.")],
    key_words=[("unknown", "the quantity you are looking for, given a letter"), ("consecutive", "following one after another: {5}, {6}, {7}"),
               ("perimeter", "the distance all the way round a shape")],
    examples=["Two consecutive numbers add to {41}: x + x + {1} = {41}, x = {20}",
              "A number doubled plus {7} is {31}: {mono(2, 'x')} + {7} = {31}, x = {12}"],
    mistake=("\"{4} less than x\" written as {4} − x", "\"{4} less than x\" is x − {4}",
             "Start from x and take {4} away. {4} − x is a different number (try x = {10}: {6} or {-6}).")))

# ---------------------------------------------------------------- 11. Quadratic equations by factorisation
SRC = ["quadratic-equations"]
L.lesson(D, S, 11, ("m3-11", "Solve quadratic equations by factorisation"), [5, 6],
  "A quadratic equation has x² as its highest power: x² − 5x + 6 = 0.\n"
  "• Make one side zero.\n• Factorise the other side: (x − 2)(x − 3) = 0.\n"
  "• If a product is zero, one of the factors is zero: x − 2 = 0 or x − 3 = 0.\n"
  "• So x = 2 or x = 3. A quadratic usually has two solutions (roots).\n"
  "• x² = 5x: do not divide by x (you would lose x = 0). Write x² − 5x = 0, x(x − 5) = 0, so x = 0 or x = 5.\n"
  "• Check each root in the original equation.",
  worked({"p": 2, "q": -5},
         "Solve {poly([1, 'x²'], [-(p + q), 'x'], [p * q, ''])} = {0}.",
         ["Two numbers with product {p * q} and sum {-(p + q)}: {-p} and {-q}.",
          "So {" + lin("-p") + " + " + lin("-q") + "} = {0}.",
          "Either x − {p} = {0}, so x = {p}; or x + {-q} = {0}, so x = {q}."],
         "x = {p} or x = {q}", checks=["p * q == -10"]),
  [card("c3m11-1", "If a product is zero, one of the factors must be zero.",
        ["{" + lin(-3) + " + " + lin(4) + "} = {0} → x = {3} or x = {-4}"], "m3-11-roots"),
   card("c3m11-2", "Make one side zero and factorise the other.",
        ["x² + {mono(2, 'x')} = {15} → {poly([1, 'x²'], [2, 'x'], [-15, ''])} = {0} → {" + lin(5) + " + " + lin(-3) + "} = {0}"], "m3-11-solve"),
   card("c3m11-3", "Never divide by x: you would lose the root x = {0}.",
        ["x² = {mono(4, 'x')} → x(x − {4}) = {0} → x = {0} or x = {4}"], "m3-11-zero")],
  [mcq("m3-11-roots", 1, "Solve {" + lin("-p") + " + " + lin("-q") + "} = {0}.",
       "{'x = ' + fmt(p) + ' or x = ' + fmt(q)}",
       [("{'x = ' + fmt(-p) + ' or x = ' + fmt(-q)}", "sign"), ("{'x = ' + fmt(p * q)}", "prod"), ("{'x = ' + fmt(p + q)}", "sum")],
       ["Either x − {br(p)} = {0} or x − {br(q)} = {0}.", "So {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("sign", "x − {br(p)} = {0} means x = {p}: the root has the opposite sign to the number in the bracket."),
             ("prod", "Set each bracket equal to zero separately: there are two roots."),
             ("sum", "Set each bracket equal to zero separately: there are two roots.")],
       sources=SRC, where=["p != q", "p != 0 && q != 0", "p != -q", "p * q != p + q", "p * q != -p && p * q != -q", "p + q != -p && p + q != -q"]),
   num("m3-11-solve", 1, "Solve {poly([1, 'x²'], [-(p + q), 'x'], [p * q, ''])} = {0}. Give the larger root.", "max(p, q)",
       ["Factorise: {" + lin("-p") + " + " + lin("-q") + "} = {0}.", "x = {p} or x = {q}. The larger is {answer}."],
       vars={"p": {"int": [-9, 9]}, "q": {"int": [-9, 9]}},
       misc=[("small", "min(p, q)", "That is the smaller root."), ("sign", "-max(p, q)", "x − {br(max(p, q))} = {0} gives x = {max(p, q)}: watch the sign.")],
       sources=SRC, where=["p != q", "p != 0 && q != 0", "p != -q", "-max(p, q) != min(p, q)"], signed=True),
   mcq("m3-11-zero", 2, "Solve x² = {mono(k, 'x')}.",
       "{'x = 0 or x = ' + k}",
       [("{'x = ' + k}", "lost"), ("{'x = ' + fmt(sqrt(k))}", "sqrt"), ("{'x = 0 or x = ' + fmt(-k)}", "sign")],
       ["Make one side zero: x² − {mono(k, 'x')} = {0}.", "Factorise: x(x − {k}) = {0}, so {answer}."],
       vars={"k": {"pick": [4, 9, 16, 25, 36]}},
       misc=[("lost", "Dividing by x loses the root x = {0}. Factorise x(x − {k}) = {0} instead."),
             ("sqrt", "x² = {mono(k, 'x')} is not x² = {k}: factorise x(x − {k}) = {0}."),
             ("sign", "x − {k} = {0} gives x = {k}, positive.")],
       sources=SRC),
   num("m3-11-a", 2, "Solve {poly([a, 'x²'], [a * n + m, 'x'], [m * n, ''])} = {0}. One root is a whole number: give it.", "-n",
       ["Factorise: {" + lin("m", "a") + " + " + lin("n") + "} = {0}.", "{mono(a, 'x')} + {m} = {0} gives x = {-m} ÷ {a}; x + {n} = {0} gives x = {answer}."],
       vars={"a": {"int": [2, 5]}, "m": {"int": [1, 7]}, "n": {"int": [1, 7]}},
       misc=[("sign", "n", "x + {n} = {0} gives x = {-n}, negative."), ("m", "-m", "{mono(a, 'x')} + {m} = {0} gives x = {-m} ÷ {a}, not a whole number.")],
       sources=SRC, where=["m % a != 0", "hcf(a, m) == 1", "m != n"], signed=True),
   num("m3-11-area", 3, "A rectangular plot in Bamenda is {k} m longer than it is wide. Its area is {w * (w + k)} m². Find its width in metres.", "w",
       ["Let the width be x m: x(x + {k}) = {w * (w + k)}.", "{poly([1, 'x²'], [k, 'x'], [-w * (w + k), ''])} = {0} → {" + lin("-w") + " + " + lin("w + k") + "} = {0}.",
        "x = {w} or x = {-(w + k)}. A width cannot be negative, so the width is {answer} m."],
       vars={"w": {"int": [3, 15]}, "k": {"int": [1, 9]}},
       misc=[("neg", "-(w + k)", "A width cannot be negative: reject x = {-(w + k)}."), ("len", "w + k", "{w + k} m is the length; the question asks for the width.")],
       unit="m", sources=SRC)],
  learn=learn(
    [("The zero product rule",
      "If two numbers multiply to give zero, at least one of them is zero. ({3} × {0} = {0}; but {3} × {2} is never {0}.)\n"
      "So if (x − {2})(x − {3}) = {0}, either x − {2} = {0} or x − {3} = {0}. That gives x = {2} or x = {3}.\n"
      "This only works with zero. If (x − {2})(x − {3}) = {6}, you cannot say x − {2} = {6}: first expand, make one side zero, and factorise again."),
     ("The method",
      "Solve x² + {mono(2, 'x')} = {15}.\n"
      "• Make one side zero: {poly([1, 'x²'], [2, 'x'], [-15, ''])} = {0}.\n"
      "• Factorise: {" + lin(5) + " + " + lin(-3) + "} = {0}.\n"
      "• Each factor zero: x = {-5} or x = {3}.\n"
      "• Check: ({3})² + {2} × {3} = {15}. ✓ and ({-5})² + {2} × ({-5}) = {15}. ✓\n"
      "Notice the sign change: the bracket (x + {5}) gives the root x = {-5}."),
     ("Roots that make sense",
      "In real problems, a quadratic may give one root that cannot be right, such as a negative length or a fraction of a person. "
      "State both roots, then reject the impossible one with a reason: \"x = {-8} is rejected because a width cannot be negative.\"\n"
      "And remember: never divide both sides by x. In x² = {mono(6, 'x')}, factorise x(x − {6}) = {0}: the roots are {0} and {6}.")],
    key_words=[("quadratic equation", "an equation whose highest power of x is x²"), ("root", "a value of x that makes the equation true"),
               ("zero product rule", "if A × B = {0} then A = {0} or B = {0}")],
    examples=["{poly([1, 'x²'], [-7, 'x'], [12, ''])} = {0} → x = {3} or x = {4}",
              "{poly([1, 'x²'], [-25, ''])} = {0} → x = {5} or x = {-5}",
              "{poly([2, 'x²'], [-8, 'x'])} = {0} → {mono(2, 'x')}(x − {4}) = {0} → x = {0} or x = {4}"],
    mistake=("x² = {mono(3, 'x')} → divide by x → x = {3}", "x² − {mono(3, 'x')} = {0} → x(x − {3}) = {0} → x = {0} or x = {3}",
             "Dividing by x throws away the root x = {0}. Make one side zero and factorise instead.")))

# ---------------------------------------------------------------- 12. Quadratic formula
SRC = ["quadratic-equations"]
L.lesson(D, S, 12, ("m3-12", "Solve quadratic equations with the quadratic formula"), [11],
  "For ax² + bx + c = 0 (a ≠ 0), the solutions are x = (−b ± √(b² − 4ac)) ÷ 2a.\n"
  "• Write the equation with zero on one side and read a, b, c with their signs.\n"
  "• Work out the discriminant D = b² − 4ac first.\n"
  "• D > 0: two different roots; D = 0: one repeated root; D < 0: no real roots.\n"
  "• The formula works even when the quadratic does not factorise; give roots to the accuracy asked (often 2 decimal places).",
  worked({"a": 2, "b": -3, "c": -4},
         "Solve {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0}, giving the roots to {2} decimal places.",
         ["a = {a}, b = {b}, c = {c}.",
          "D = b² − {4}ac = {br(b)}² − {4} × {a} × {br(c)} = {b * b - 4 * a * c}.",
          "x = ({-b} ± √{b * b - 4 * a * c}) ÷ {2 * a}, and √{b * b - 4 * a * c} ≈ {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}.",
          "x ≈ {roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)} or x ≈ {roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)}."],
         "x ≈ {roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)} or x ≈ {roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)}",
         checks=["b * b - 4 * a * c == 41"]),
  [card("c3m12-1", "Read a, b and c with their signs from ax² + bx + c = {0}.",
        ["{poly([3, 'x²'], [-5, 'x'], [-2, ''])} = {0}: a = {3}, b = {-5}, c = {-2}"], "m3-12-abc"),
   card("c3m12-2", "Work out the discriminant D = b² − {4}ac first.",
        ["a = {1}, b = {5}, c = {3}: D = {25} − {12} = {13}"], "m3-12-disc"),
   card("c3m12-3", "The sign of D tells you how many real roots there are.",
        ["D = {13} > {0}: two roots.  D = {0}: one root.  D = {-7}: none."], "m3-12-count")],
  [mcq("m3-12-abc", 1, "For {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0}, what are a, b and c?",
       "{'a = ' + fmt(a) + ', b = ' + fmt(b) + ', c = ' + fmt(c)}",
       [("{'a = ' + fmt(a) + ', b = ' + fmt(abs(b)) + ', c = ' + fmt(abs(c))}", "signs"), ("{'a = ' + fmt(c) + ', b = ' + fmt(b) + ', c = ' + fmt(a)}", "order"), ("{'a = ' + fmt(a) + ', b = ' + fmt(c) + ', c = ' + fmt(b)}", "bc")],
       ["a is the coefficient of x², b of x, and c is the number term, each with its sign.", "So {answer}."],
       vars={"a": {"int": [2, 6]}, "b": {"int": [-9, -1]}, "c": {"int": [-9, -1]}},
       misc=[("signs", "Keep the signs: b = {b} and c = {c} are negative."), ("order", "a goes with x², c is the number term."), ("bc", "b goes with x and c is the number term.")],
       sources=SRC, where=["a != c", "b != c"]),
   num("m3-12-disc", 1, "Work out the discriminant b² − 4ac for {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0}.", "b * b - 4 * a * c",
       ["a = {a}, b = {b}, c = {c}.", "b² − {4}ac = {b * b} − {4} × {a} × {br(c)} = {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, 9]}},
       misc=[("csign", "b * b + 4 * a * c", "Keep the sign of c: {4} × {a} × {br(c)} = {4 * a * c}."), ("bsq", "-b * b - 4 * a * c", "b² is never negative: {br(b)}² = {b * b}.")],
       sources=SRC, where=["b != 0", "c != 0", "b * b - 4 * a * c != b * b + 4 * a * c", "b * b - 4 * a * c != -b * b - 4 * a * c"], signed=True),
   num("m3-12-big", 2, "Solve {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0} with the formula. Give the larger root to {2} decimal places.",
       "roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)",
       ["D = {br(b)}² − {4} × {a} × {br(c)} = {b * b - 4 * a * c}.",
        "x = ({-b} + √{b * b - 4 * a * c}) ÷ {2 * a} ≈ ({-b} + {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}) ÷ {2 * a} ≈ {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, -1]}},
       misc=[("half", "roundTo(-b + sqrt(b * b - 4 * a * c), 0.01)", "Divide the whole top by {2 * a}."),
             ("bsign", "roundTo((b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)", "The formula starts with −b = {-b}, not {b}.")],
       sources=SRC, where=["b != 0", "!isPerfectSquare(b * b - 4 * a * c)", "roundTo(-b + sqrt(b * b - 4 * a * c), 0.01) != roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)"], signed=True),
   num("m3-12-small", 2, "Solve {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0} with the formula. Give the smaller root to {2} decimal places.",
       "roundTo((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)",
       ["D = {b * b - 4 * a * c}, √D ≈ {roundTo(sqrt(b * b - 4 * a * c), 0.0001)}.",
        "The smaller root uses minus: x = ({-b} − √{b * b - 4 * a * c}) ÷ {2 * a} ≈ {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-9, 9]}, "c": {"int": [-9, -1]}},
       misc=[("plus", "roundTo((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 0.01)", "That is the larger root (with +). The smaller one uses −√D.")],
       sources=SRC, where=["b != 0", "!isPerfectSquare(b * b - 4 * a * c)"], signed=True),
   mcq("m3-12-count", 3, "How many real roots does {poly([a, 'x²'], [b, 'x'], [c, ''])} = {0} have?",
       "{b * b - 4 * a * c > 0 ? 'Two different roots' : b * b - 4 * a * c == 0 ? 'One repeated root' : 'No real roots'}",
       [("{b * b - 4 * a * c > 0 ? 'One repeated root' : 'Two different roots'}", "w1"),
        ("{b * b - 4 * a * c < 0 ? 'One repeated root' : 'No real roots'}", "w2"),
        ("{'It depends on the value of x'}", "w3")],
       ["D = b² − {4}ac = {b * b} − {4 * a * c} = {b * b - 4 * a * c}.",
        "{b * b - 4 * a * c > 0 ? 'D > 0' : b * b - 4 * a * c == 0 ? 'D = 0' : 'D < 0'}, so: {answer}."],
       vars={"a": {"int": [1, 4]}, "K": {"pick": [{"b": 6, "c": 9}, {"b": 4, "c": 4}, {"b": 2, "c": 5}, {"b": 3, "c": 1}, {"b": -5, "c": 2}, {"b": 1, "c": 3}, {"b": -4, "c": 1}]},
             "b": {"expr": "K.b * a"}, "c": {"expr": "K.c * a"}},
       misc=[("w1", "Use D = b² − {4}ac = {b * b - 4 * a * c}: positive gives two roots, zero one, negative none."),
             ("w2", "Use D = b² − {4}ac = {b * b - 4 * a * c}: positive gives two roots, zero one, negative none."),
             ("w3", "The number of roots is fixed by a, b and c through D = b² − {4}ac, not by x.")],
       sources=SRC)],
  learn=learn(
    [("When factorising fails",
      "Some quadratics, such as {poly([1, 'x²'], [3, 'x'], [-1, ''])} = {0}, have no whole-number factors. The quadratic formula always works:\n"
      "x = (−b ± √(b² − {4}ac)) ÷ {2}a\n"
      "Here a is the coefficient of x², b of x, and c is the number term, each read with its sign after making one side zero.\n"
      "The ± means: do it once with + and once with −. That gives the two roots."),
     ("Step by step",
      "Solve {poly([2, 'x²'], [-3, 'x'], [-4, ''])} = {0}. a = {2}, b = {-3}, c = {-4}.\n"
      "• Discriminant: D = ({-3})² − {4} × {2} × ({-4}) = {9} + {32} = {41}.\n"
      "• x = ({3} ± √{41}) ÷ {4}, and √{41} ≈ {6.4031}.\n"
      "• x ≈ ({3} + {6.4031}) ÷ {4} ≈ {2.35} or x ≈ ({3} − {6.4031}) ÷ {4} ≈ {-0.85}.\n"
      "Careful with −b: if b is negative, −b is positive."),
     ("What the discriminant tells you",
      "D = b² − {4}ac is under the square root.\n"
      "• D positive: two different real roots.\n• D zero: √{0} = {0}, so both roots are the same (one repeated root).\n"
      "• D negative: there is no real square root, so no real roots.\n"
      "Check D first: it tells you what to expect before you finish the calculation.")],
    key_words=[("quadratic formula", "x = (−b ± √(b² − {4}ac)) ÷ {2}a"), ("discriminant", "D = b² − {4}ac, the part under the square root"),
               ("decimal places", "digits after the decimal point")],
    examples=["{poly([1, 'x²'], [-6, 'x'], [9, ''])} = {0}: D = {0}, one root x = {3}",
              "{poly([1, 'x²'], [1, 'x'], [1, ''])} = {0}: D = {-3}, no real roots"],
    mistake=("For {poly([1, 'x²'], [-5, 'x'], [2, ''])} = {0}: x = ({-5} ± √{17}) ÷ {2}", "x = ({5} ± √{17}) ÷ {2}",
             "The formula starts with −b. Here b = {-5}, so −b = {5}.")))
