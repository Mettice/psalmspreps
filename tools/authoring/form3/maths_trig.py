"""Form 3 Maths, Term 1, rows 13-19 (transposition, variation, Pythagoras, trigonometry).
Run: python tools/authoring/form3/maths_trig.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"


def bank(id, level, prompt, items, sources, figure=None, review="authored"):
    """Multiple choice from a bank of {q, r, w: [3], e: [3], y}: authored items, each wrong option with its own feedback."""
    for it in items:
        assert len(it["w"]) == 3 and len(it["e"]) == 3, it
    kw = {"figure": figure} if figure else {}
    return mcq(id, level, prompt, "{X.r}", [("{X.w[0]}", "w0"), ("{X.w[1]}", "w1"), ("{X.w[2]}", "w2")],
               ["{X.y}", "So the answer is {answer}."], vars={"X": {"pick": items}},
               misc=[("w0", "{X.e[0]}"), ("w1", "{X.e[1]}"), ("w2", "{X.e[2]}")], sources=sources, review=review, **kw)


TRI = {"i": {"int": [0, 11]}, "T": {"expr": "triple(i)"}, "k": {"int": [1, 3]},
       "a": {"expr": "T[0] * k"}, "b": {"expr": "T[1] * k"}, "c": {"expr": "T[2] * k"}}

# ---------------------------------------------------------------- 13. Transposition of formulae
SRC = ["formulae"]
L.lesson(D, S, 13, ("m3-13", "Change the subject of a formula"), [7],
  "The subject of a formula is the letter on its own on one side: in v = u + at, v is the subject.\n"
  "To make another letter the subject, treat the formula like an equation: do the same to both sides, undoing operations in reverse order.\n"
  "• v = u + at → v − u = at → t = (v − u) ÷ a.\n"
  "• A = πr² → r² = A ÷ π → r = √(A ÷ π).\n"
  "• If the new subject appears twice, collect those terms on one side and factorise it out.\n"
  "After rearranging, you can substitute values to find the new subject.",
  worked({"v": 30, "u": 6, "a": 4},
         "Make t the subject of v = u + at, then find t when v = {v}, u = {u} and a = {a}.",
         ["Subtract u from both sides: v − u = at.", "Divide both sides by a: t = (v − u) ÷ a.",
          "Substitute: t = ({v} − {u}) ÷ {a} = {(v - u) / a}."],
         "t = (v − u) ÷ a = {(v - u) / a}", checks=["(v - u) / a == 6"]),
  [card("c3m13-1", "Undo the operations on the new subject in reverse order, doing the same to both sides.",
        ["P = {2}(l + w) → P ÷ {2} = l + w → l = P ÷ {2} − w"], "m3-13-lin"),
   card("c3m13-2", "To undo a square, take the square root.",
        ["A = πr² → r = √(A ÷ π)"], "m3-13-sq"),
   card("c3m13-3", "After rearranging, substitute the values to find the new subject.",
        ["v = u + at with v = {20}, u = {5}, a = {3}: t = ({20} − {5}) ÷ {3} = {5}"], "m3-13-sub")],
  [bank("m3-13-lin", 1, "{X.q}", [
     {"q": "Make t the subject of v = u + at.", "r": "t = (v − u) ÷ a", "w": ["t = v − u − a", "t = (v + u) ÷ a", "t = v ÷ a − u"],
      "e": ["a multiplies t: divide by a, do not subtract it.", "u is added on the right: subtract it, do not add.", "Subtract u first (it is added last), then divide by a."], "y": "Subtract u from both sides, then divide by a."},
     {"q": "Make w the subject of P = 2l + 2w.", "r": "w = (P − 2l) ÷ 2", "w": ["w = P − 2l − 2", "w = (P + 2l) ÷ 2", "w = P ÷ 2 − 2l"],
      "e": ["2 multiplies w: divide by 2, do not subtract it.", "2l is added: subtract it from both sides.", "Divide the whole of P − 2l by 2."], "y": "Subtract 2l, then divide by 2."},
     {"q": "Make x the subject of y = mx + c.", "r": "x = (y − c) ÷ m", "w": ["x = y − c − m", "x = (y + c) ÷ m", "x = y ÷ m − c"],
      "e": ["m multiplies x: divide by m.", "c is added: subtract it.", "Subtract c first, then divide the whole of y − c by m."], "y": "Subtract c, then divide by m."},
     {"q": "Make b the subject of A = ½(a + b)h.", "r": "b = 2A ÷ h − a", "w": ["b = A ÷ 2h − a", "b = 2A − h − a", "b = 2Ah − a"],
      "e": ["Multiply by 2 to undo ½: 2A, then divide by h.", "h multiplies the bracket: divide by h, do not subtract.", "Divide by h, do not multiply."], "y": "Multiply by 2, divide by h, then subtract a."}], SRC),
   num("m3-13-sub", 1, "v = u + at. Find t when v = {u + a * t}, u = {u} and a = {a}.", "t",
       ["t = (v − u) ÷ a.", "t = ({u + a * t} − {u}) ÷ {a} = {answer}."],
       vars={"u": {"int": [0, 20]}, "a": {"int": [2, 10]}, "t": {"int": [2, 12]}},
       misc=[("nodiv", "a * t", "That is v − u = at. Divide by a = {a} to find t."), ("add", "(2 * u + a * t) / a", "Subtract u, do not add it.")],
       sources=SRC, where=["u != 0", "(2 * u + a * t) / a != t"]),
   bank("m3-13-sq", 2, "{X.q}", [
     {"q": "Make r the subject of A = πr².", "r": "r = √(A ÷ π)", "w": ["r = A ÷ π²", "r = √A ÷ π", "r = (A ÷ π)²"],
      "e": ["Only r is squared: divide by π, then take the square root.", "Take the square root of the whole of A ÷ π.", "To undo a square, take the square root, do not square."], "y": "Divide by π, then take the square root."},
     {"q": "Make v the subject of E = ½mv².", "r": "v = √(2E ÷ m)", "w": ["v = 2E ÷ m²", "v = √(E ÷ 2m)", "v = (2E ÷ m)²"],
      "e": ["Only v is squared: undo it with a square root at the end.", "Multiply by 2 to undo ½, do not divide.", "To undo a square, take the square root."], "y": "Multiply by 2, divide by m, then take the square root."},
     {"q": "Make x the subject of y = x² − k.", "r": "x = √(y + k)", "w": ["x = √y − k", "x = (y + k)²", "x = √(y − k)"],
      "e": ["Add k first, then take the square root of the whole of y + k.", "To undo a square, take the square root.", "k is subtracted: add it to both sides."], "y": "Add k to both sides, then take the square root."}], SRC),
   num("m3-13-temp", 2, "F = {9} ÷ {5} × C + {32}. Make C the subject and find C when F = {9 * n + 32}.", "5 * n",
       ["C = {5} × (F − {32}) ÷ {9}.", "C = {5} × ({9 * n + 32} − {32}) ÷ {9} = {5} × {9 * n} ÷ {9} = {answer}."],
       vars={"n": {"int": [-4, 20]}},
       misc=[("order", "(9 * n + 32) * 5 / 9 - 32", "Subtract {32} first, then multiply by {5} ÷ {9}: undo in reverse order."),
             ("frac", "9 * n * 9 / 5", "Undo × {9} ÷ {5} by multiplying by {5} ÷ {9}.")],
       sources=SRC, where=["n != 0"], signed=True),
   bank("m3-13-twice", 3, "{X.q}", [
     {"q": "Make x the subject of ax + b = cx + d.", "r": "x = (d − b) ÷ (a − c)", "w": ["x = (d + b) ÷ (a + c)", "x = (d − b) ÷ a − c", "x = d − b − a + c"],
      "e": ["Move cx by subtracting it and b by subtracting it: signs change.", "Factorise x(a − c), then divide by the whole bracket.", "x is multiplied by (a − c): divide, do not subtract."], "y": "Collect x terms: ax − cx = d − b, factorise x(a − c) = d − b, then divide."},
     {"q": "Make x the subject of y = (x + 1) ÷ (x − 1).", "r": "x = (y + 1) ÷ (y − 1)", "w": ["x = (y − 1) ÷ (y + 1)", "x = y + 1 − y + 1", "x = (1 − y) ÷ (y + 1)"],
      "e": ["Check with y = 3: x = 2 gives (2 + 1) ÷ (2 − 1) = 3, so x = (y + 1) ÷ (y − 1).", "x is a factor: factorise x(y − 1), then divide.", "From xy − x = y + 1, x(y − 1) = y + 1: the signs are as in the answer."],
      "y": "Multiply by (x − 1): xy − y = x + 1. Collect: xy − x = y + 1, so x(y − 1) = y + 1."},
     {"q": "Make a the subject of p = (a + b) ÷ a.", "r": "a = b ÷ (p − 1)", "w": ["a = b ÷ p − 1", "a = (b − 1) ÷ p", "a = b ÷ (p + 1)"],
      "e": ["Divide b by the whole of (p − 1).", "From pa = a + b: pa − a = b, so a(p − 1) = b.", "Moving a to the left subtracts it: p − 1, not p + 1."], "y": "Multiply by a: pa = a + b. Collect: pa − a = b, a(p − 1) = b."}], SRC)],
  learn=learn(
    [("What the subject is",
      "In the formula for the area of a rectangle, A = lw, A is the subject: it is alone on one side, and the formula tells you how to find it.\n"
      "Sometimes you know A and w and want l. Then you rearrange the formula so that l is the subject: l = A ÷ w.\n"
      "Rearranging is called changing the subject or transposing the formula."),
     ("Undo in reverse order",
      "Look at how the new subject was built. In v = u + at, start from t: multiply by a, then add u.\n"
      "To get t back, undo those steps in reverse order, on both sides:\n"
      "• subtract u: v − u = at;\n• divide by a: t = (v − u) ÷ a.\n"
      "Keep brackets where you divide a whole expression. Squares are undone with square roots: A = πr² gives r = √(A ÷ π)."),
     ("When the subject appears twice",
      "In ax + b = cx + d, x appears on both sides. Collect the x terms on one side and the rest on the other: ax − cx = d − b.\n"
      "Now take x out as a common factor: x(a − c) = d − b.\n"
      "Divide by the bracket: x = (d − b) ÷ (a − c). Factorising is the key step.")],
    key_words=[("subject", "the letter on its own on one side of a formula"), ("transpose", "rearrange a formula to change its subject"),
               ("inverse operation", "the operation that undoes another: + and −, × and ÷, squaring and square root")],
    examples=["C = πd → d = C ÷ π", "y = {mono(3, 'x')} − {4} → x = (y + {4}) ÷ {3}", "V = lwh → h = V ÷ (lw)"],
    mistake=("v = u + at → t = v − u − a", "v = u + at → t = (v − u) ÷ a",
             "a multiplies t, so undo it by dividing by a. Subtracting a would undo an addition.")))

# ---------------------------------------------------------------- 14. Direct and inverse variation
SRC = ["variation"]
L.lesson(D, S, 14, ("m3-14", "Direct and inverse variation"), [13],
  "y varies directly as x (y ∝ x) means y = kx for a constant k: when x doubles, y doubles.\n"
  "y varies inversely as x (y ∝ 1/x) means y = k ÷ x: when x doubles, y halves.\n"
  "Variation can be with a power: y ∝ x² means y = kx²; y ∝ √x means y = k√x.\n"
  "Method: write the equation with k, use the given pair of values to find k, write the full formula, then use it.\n"
  "Example: y ∝ x and y = 12 when x = 4: k = 3, so y = 3x; when x = 10, y = 30.",
  worked({"x1": 4, "y1": 12, "x2": 10},
         "y varies directly as x, and y = {y1} when x = {x1}. Find y when x = {x2}.",
         ["y = kx.", "{y1} = k × {x1}, so k = {y1 / x1}.", "The formula is y = {mono(y1 / x1, 'x')}.", "When x = {x2}: y = {y1 / x1} × {x2} = {y1 / x1 * x2}."],
         "y = {y1 / x1 * x2}", checks=["y1 / x1 == 3"]),
  [card("c3m14-1", "Direct variation: y = kx. Find k from one pair of values.",
        ["y = {12} when x = {4}: k = {3}, so y = {mono(3, 'x')}."], "m3-14-direct"),
   card("c3m14-2", "Inverse variation: y = k ÷ x. As x increases, y decreases.",
        ["y = {6} when x = {4}: k = {24}, so y = {24} ÷ x; when x = {8}, y = {3}."], "m3-14-form"),
   card("c3m14-3", "With a square: y = kx². If x doubles, y is multiplied by four.",
        ["y = {mono(2, 'x²')}: x = {3} gives y = {18}; x = {6} gives y = {72}."], "m3-14-square")],
  [num("m3-14-direct", 1, "y varies directly as x, and y = {k * x1} when x = {x1}. Find y when x = {x2}.", "k * x2",
       ["y = kx: {k * x1} = k × {x1}, so k = {k}.", "y = {k} × {x2} = {answer}."],
       vars={"k": {"int": [2, 9]}, "x1": {"int": [2, 12]}, "x2": {"int": [2, 20]}},
       misc=[("inv", "k * x1 * x1 / x2", "That uses inverse variation. Direct: y = kx, so y grows with x."), ("k", "k", "{k} is the constant k. Now use y = {mono(k, 'x')} with x = {x2}.")],
       sources=SRC, where=["x1 != x2", "k * x1 * x1 / x2 != k * x2"]),
   bank("m3-14-form", 1, "{X.q}", [
     {"q": "y varies inversely as x. Which formula is right?", "r": "y = k ÷ x", "w": ["y = kx", "y = k + x", "y = kx²"],
      "e": ["y = kx is direct variation.", "Variation uses multiplying or dividing by k, not adding.", "y = kx² is direct variation with the square of x."], "y": "Inverse variation: y = k ÷ x."},
     {"q": "y varies directly as the square of x. Which formula is right?", "r": "y = kx²", "w": ["y = k ÷ x²", "y = (kx)²", "y = kx"],
      "e": ["Dividing by x² is inverse variation.", "Only x is squared; k is not.", "That is direct variation with x, not x²."], "y": "Directly as the square: y = kx²."},
     {"q": "y varies inversely as the square root of x. Which formula is right?", "r": "y = k ÷ √x", "w": ["y = k√x", "y = √(k ÷ x)", "y = k ÷ x²"],
      "e": ["k√x is direct variation with √x.", "k is not under the root.", "That is the square, not the square root."], "y": "Inversely as √x: y = k ÷ √x."}], SRC),
   num("m3-14-inv", 2, "y varies inversely as x, and y = {K / x1} when x = {x1}. Find y when x = {x2}.", "K / x2",
       ["y = k ÷ x: {K / x1} = k ÷ {x1}, so k = {K}.", "y = {K} ÷ {x2} = {answer}."],
       vars={"K": {"pick": [24, 36, 48, 60, 72, 120]}, "x1": {"pick": [2, 3, 4, 6]}, "x2": {"pick": [2, 3, 4, 6, 8, 12]}},
       misc=[("dir", "K / x1 / x1 * x2", "That uses direct variation. Inverse: as x grows, y gets smaller."), ("k", "K", "{K} is the constant k. Now y = {K} ÷ {x2}.")],
       sources=SRC, where=["x1 != x2", "K % x2 == 0", "K / x1 / x1 * x2 != K / x2", "K / x1 / x1 * x2 != K"]),
   num("m3-14-square", 2, "y varies directly as x², and y = {k * x1 * x1} when x = {x1}. Find y when x = {x2}.", "k * x2 * x2",
       ["y = kx²: {k * x1 * x1} = k × {x1 * x1}, so k = {k}.", "y = {k} × {x2}² = {k} × {x2 * x2} = {answer}."],
       vars={"k": {"int": [2, 5]}, "x1": {"int": [2, 6]}, "x2": {"int": [2, 10]}},
       misc=[("lin", "k * x1 * x1 / x1 * x2", "That treats it as y = kx. Here y = kx²: square x = {x2}."), ("nosq", "k * x2", "Square x first: {x2}² = {x2 * x2}.")],
       sources=SRC, where=["x1 != x2", "x2 != 1"]),
   num("m3-14-work", 3, "{w1} workers can build a classroom wall in {d1} days. Working at the same rate, how many days would {w2} workers take?", "w1 * d1 / w2",
       ["More workers, fewer days: days vary inversely as workers. days = k ÷ workers.", "k = {w1} × {d1} = {w1 * d1}; days = {w1 * d1} ÷ {w2} = {answer}."],
       vars={"w1": {"int": [2, 12]}, "d1": {"int": [3, 20]}, "w2": {"int": [2, 15]}},
       misc=[("dir", "d1 * w2 / w1", "With more workers the wall takes fewer days: this is inverse variation, not direct.")],
       unit="days", sources=SRC, where=["w1 != w2", "(w1 * d1) % w2 == 0", "d1 * w2 / w1 != w1 * d1 / w2"])],
  learn=learn(
    [("Things that grow together",
      "At a market, Bih buys tomatoes at a fixed price per heap. Twice as many heaps cost twice as much: the cost varies directly as the number of heaps.\n"
      "In symbols: cost ∝ heaps, or cost = k × heaps, where k is the price of one heap (the constant of variation).\n"
      "Any direct variation y = kx has a straight-line graph through the origin."),
     ("Things that go opposite ways",
      "A journey of {120} km: at {60} km/h it takes {2} hours, at {40} km/h it takes {3} hours. Faster speed, less time: time varies inversely as speed.\n"
      "In symbols: t = k ÷ v, and here k = {120}. Multiply the two quantities and you always get k.\n"
      "When one doubles, the other halves."),
     ("The method",
      "• Write the variation with k: y = kx, y = k ÷ x, y = kx², …\n"
      "• Put in the pair of values you are given and solve for k.\n"
      "• Write the formula with the value of k.\n"
      "• Use it to answer the question.\n"
      "Example: y ∝ x², and y = {50} when x = {5}: {50} = k × {25}, so k = {2} and y = {mono(2, 'x²')}. When x = {3}, y = {18}.")],
    key_words=[("direct variation", "y = kx: both increase in the same ratio"), ("inverse variation", "y = k ÷ x: one doubles, the other halves"),
               ("constant of variation", "the fixed number k")],
    examples=["Cost of exercise books ∝ number of books", "Time for a journey ∝ {1} ÷ speed", "Area of a circle ∝ r²"],
    mistake=("y ∝ x², y = {12} when x = {2}: k = {6}", "{12} = k × {2}² = {mono(4, 'k')}, so k = {3}",
             "Put the square into the equation before finding k: y = kx² means k = y ÷ x².")))

# ---------------------------------------------------------------- 15. Joint variation and graphs
SRC = ["variation"]
L.lesson(D, S, 15, ("m3-15", "Joint and partial variation, and variation graphs"), [14],
  "Joint variation: one quantity varies as two or more others together.\n"
  "• z varies jointly as x and y: z = kxy.\n"
  "• z varies directly as x and inversely as y: z = kx ÷ y.\n"
  "Find k from one set of values, then use the formula.\n"
  "Graphs: y = kx is a straight line through the origin; y = k ÷ x is a curve (hyperbola) that never meets the axes; y = kx² is a parabola through the origin.\n"
  "Effect of changes: if y ∝ x², multiplying x by n multiplies y by n².",
  worked({"k": 3, "x": 4, "y": 6, "X": 5, "Y": 2},
         "z varies jointly as x and y. z = {k * x * y} when x = {x} and y = {y}. Find z when x = {X} and y = {Y}.",
         ["z = kxy.", "{k * x * y} = k × {x} × {y}, so k = {k}.", "z = {k} × {X} × {Y} = {k * X * Y}."],
         "z = {k * X * Y}", checks=["k == 3"]),
  [card("c3m15-1", "Jointly as x and y: z = kxy.",
        ["z = {24} when x = {2}, y = {4}: k = {3}, so z = {mono(3, 'xy')}."], "m3-15-form"),
   card("c3m15-2", "Directly as x and inversely as y: z = kx ÷ y.",
        ["z = {10} when x = {5}, y = {2}: k = {4}."], "m3-15-k"),
   card("c3m15-3", "The graph of y = kx is a straight line through the origin; y = k ÷ x is a curve.",
        ["Doubling x doubles y on the line, halves y on the curve."], "m3-15-graph")],
  [bank("m3-15-form", 1, "{X.q}", [
     {"q": "z varies jointly as x and y. Which formula is right?", "r": "z = kxy", "w": ["z = k(x + y)", "z = kx ÷ y", "z = xy"],
      "e": ["Jointly means multiply, not add.", "kx ÷ y means inversely as y.", "There must be a constant k."], "y": "Jointly: z = kxy."},
     {"q": "z varies directly as x and inversely as y. Which formula is right?", "r": "z = kx ÷ y", "w": ["z = kxy", "z = ky ÷ x", "z = k(x − y)"],
      "e": ["That is jointly as x and y.", "x and y are the wrong way round.", "Variation uses multiplying or dividing."], "y": "Directly as x (top), inversely as y (bottom)."},
     {"q": "P varies directly as the square of v and inversely as r. Which formula is right?", "r": "P = kv² ÷ r", "w": ["P = kvr²", "P = kr ÷ v²", "P = k(v² − r)"],
      "e": ["r should divide, not multiply.", "v² goes on top, r at the bottom.", "Variation uses multiplying and dividing."], "y": "P = kv² ÷ r."}], SRC),
   num("m3-15-k", 1, "z varies jointly as x and y, and z = {k * x * y} when x = {x} and y = {y}. Find k.", "k",
       ["z = kxy: {k * x * y} = k × {x * y}.", "k = {k * x * y} ÷ {x * y} = {answer}."],
       vars={"k": {"int": [2, 9]}, "x": {"int": [2, 6]}, "y": {"int": [2, 6]}},
       misc=[("one", "k * y", "Divide by both x and y: {x} × {y} = {x * y}.")],
       sources=SRC, where=["x != y", "k * y != k"]),
   num("m3-15-zxy", 2, "z varies directly as x and inversely as y. z = {k * x / y} when x = {x} and y = {y}. Find z when x = {X} and y = {Y}.", "k * X / Y",
       ["z = kx ÷ y: {k * x / y} = k × {x} ÷ {y}, so k = {k}.", "z = {k} × {X} ÷ {Y} = {answer}."],
       vars={"k": {"pick": [6, 12, 24, 36]}, "x": {"pick": [2, 3, 4]}, "y": {"pick": [2, 3, 4, 6]}, "X": {"pick": [2, 4, 5, 6, 8]}, "Y": {"pick": [2, 3, 4, 6]}},
       misc=[("swap", "k * Y / X", "x is on top (direct) and y at the bottom (inverse): z = {k} × {X} ÷ {Y}.")],
       sources=SRC, where=["(k * x) % y == 0", "(k * X) % Y == 0", "X != x || Y != y", "k * Y / X != k * X / Y"]),
   bank("m3-15-graph", 2, "{X.q}", [
     {"q": "What does the graph of y = kx (k > 0) look like?", "r": "A straight line through the origin", "w": ["A curve that never meets the axes", "A straight line that does not pass through the origin", "A U-shaped curve"],
      "e": ["That is y = k ÷ x.", "When x = 0, y = k × 0 = 0: the line passes through the origin.", "That is y = kx²."], "y": "y = kx is a straight line; x = 0 gives y = 0."},
     {"q": "What does the graph of y = k ÷ x (k > 0, x > 0) look like?", "r": "A curve that gets closer to both axes but never meets them", "w": ["A straight line through the origin", "A U-shaped curve through the origin", "A straight line sloping down to the x-axis"],
      "e": ["That is direct variation, y = kx.", "That is y = kx².", "y = k ÷ x is never zero, so it never reaches the x-axis."], "y": "y = k ÷ x: as x grows, y shrinks towards zero but never reaches it."},
     {"q": "What does the graph of y = kx² (k > 0) look like?", "r": "A U-shaped curve (parabola) through the origin", "w": ["A straight line through the origin", "A curve that never meets the axes", "A straight line that does not pass through the origin"],
      "e": ["y doubles when x doubles only for y = kx; here y is four times as big.", "That is y = k ÷ x.", "x = 0 gives y = 0: it passes through the origin."], "y": "y = kx² is a parabola with its lowest point at the origin."}], SRC),
   num("m3-15-scale", 3, "y varies directly as x². By what number is y multiplied when x is multiplied by {n}?", "n * n",
       ["y = kx². Replace x by {n}x: y = k({n}x)² = {n * n}kx².", "y is multiplied by {answer}."],
       vars={"n": {"int": [2, 6]}},
       misc=[("lin", "n", "y varies as the square: ({n})² = {n * n}, not {n}."), ("double", "2 * n", "Square {n}: {n} × {n} = {n * n}.")],
       sources=SRC, where=["2 * n != n * n"])],
  learn=learn(
    [("More than one cause",
      "The cost of fuel for a trip depends on the distance and on the price per litre. Double either one and the cost doubles. "
      "We say the cost varies jointly as distance and price: C = kdp.\n"
      "Joint variation multiplies the quantities. When one quantity varies inversely, it goes on the bottom: "
      "z varies directly as x and inversely as y means z = kx ÷ y."),
     ("Finding k and using it",
      "z varies jointly as x and y, and z = {24} when x = {2} and y = {4}.\n"
      "{24} = k × {2} × {4} = {mono(8, 'k')}, so k = {3} and z = {mono(3, 'xy')}.\n"
      "When x = {5} and y = {2}: z = {3} × {5} × {2} = {30}.\n"
      "The method is always: write the formula with k, find k, then use the formula."),
     ("Pictures of variation",
      "• y = kx: a straight line through the origin. Equal steps in x give equal steps in y.\n"
      "• y = k ÷ x: a curve. As x gets bigger, y gets smaller, but it never reaches zero.\n"
      "• y = kx²: a U-shaped curve, the parabola. If x doubles, y becomes four times as big.\n"
      "Reading a graph tells you which type of variation the data follow.")],
    key_words=[("joint variation", "one quantity varies as the product of others: z = kxy"), ("hyperbola", "the curve of y = k ÷ x"),
               ("parabola", "the U-shaped curve of y = kx²")],
    examples=["Area of a rectangle varies jointly as its length and width (k = {1}).", "Pressure ∝ force ÷ area", "y ∝ x²: x × {3} gives y × {9}"],
    mistake=("z varies jointly as x and y: z = k(x + y)", "z = kxy",
             "Jointly means the quantities are multiplied together, not added.")))

# ---------------------------------------------------------------- 16. Pythagoras' theorem
SRC = ["pythagoras"]
L.lesson(D, S, 16, ("m3-16", "Use Pythagoras' theorem in right-angled triangles"), [],
  "In a right-angled triangle the longest side, opposite the right angle, is the hypotenuse.\n"
  "Pythagoras' theorem: hypotenuse² = sum of the squares of the other two sides, c² = a² + b².\n"
  "• Hypotenuse: c = √(a² + b²).\n• Shorter side: a = √(c² − b²).\n"
  "• Converse: if c² = a² + b², the triangle has a right angle; otherwise it does not.\n"
  "Pythagorean triples are whole-number sides: 3, 4, 5; 5, 12, 13; 8, 15, 17 (and multiples).",
  worked({"a": 6, "b": 8},
         "A right-angled triangle has shorter sides {a} cm and {b} cm. Find the hypotenuse.",
         ["c² = a² + b² = {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b}.", "c = √{a * a + b * b} = {sqrt(a * a + b * b)} cm."],
         "{sqrt(a * a + b * b)} cm", checks=["a * a + b * b == 100"], figure="rightTriFig(a, b, 'c')"),
  [card("c3m16-1", "The hypotenuse is the longest side, opposite the right angle: c² = a² + b².",
        ["Sides {3} cm and {4} cm: c² = {9} + {16} = {25}, c = {5} cm."], "m3-16-hyp"),
   card("c3m16-2", "For a shorter side, subtract: a² = c² − b².",
        ["Hypotenuse {13}, side {5}: a² = {169} − {25} = {144}, a = {12}."], "m3-16-leg"),
   card("c3m16-3", "If c² = a² + b² for the longest side c, the triangle is right-angled.",
        ["{8}, {15}, {17}: {64} + {225} = {289} = {17}². Right-angled."], "m3-16-test")],
  [num("m3-16-hyp", 1, "A right-angled triangle has shorter sides {a} cm and {b} cm. Find the hypotenuse in cm.", "c",
       ["c² = {a}² + {b}² = {a * a} + {b * b} = {c * c}.", "c = √{c * c} = {answer} cm."],
       vars=TRI, misc=[("sum", "a + b", "Add the squares, not the sides: {a * a} + {b * b} = {c * c}, then take the square root."),
                      ("nosqrt", "c * c", "{c * c} is c². Take the square root.")],
       unit="cm", figure="rightTriFig(a, b, 'c')", sources=SRC),
   num("m3-16-leg", 1, "The hypotenuse of a right-angled triangle is {c} cm and one side is {b} cm. Find the third side in cm.", "a",
       ["a² = c² − b² = {c * c} − {b * b} = {a * a}.", "a = √{a * a} = {answer} cm."],
       vars=TRI, misc=[("add", "sqrt(c * c + b * b)", "c is the hypotenuse, the longest side: subtract, a² = c² − b²."),
                      ("diff", "c - b", "Subtract the squares, not the sides, then take the square root.")],
       unit="cm", figure="rightTriFig('a', b, c)", sources=SRC, where=["c - b != a"]),
   num("m3-16-dec", 2, "A right-angled triangle has shorter sides {p} cm and {q} cm. Find the hypotenuse to {1} decimal place.", "roundTo(sqrt(p * p + q * q), 0.1)",
       ["c² = {p * p} + {q * q} = {p * p + q * q}.", "c = √{p * p + q * q} ≈ {roundTo(sqrt(p * p + q * q), 0.0001)} ≈ {answer} cm."],
       vars={"p": {"int": [2, 12]}, "q": {"int": [2, 15]}},
       misc=[("sum", "p + q", "Add the squares, then take the square root: √({p * p} + {q * q}).")],
       unit="cm", figure="rightTriFig(p, q, 'c')", sources=SRC, where=["!isPerfectSquare(p * p + q * q)"]),
   mcq("m3-16-test", 2, "A triangle has sides {s[0]} cm, {s[1]} cm and {s[2]} cm. Is it right-angled?",
       "{isRightTriangle(s[0], s[1], s[2]) ? 'Yes: ' + s[0] * s[0] + ' + ' + s[1] * s[1] + ' = ' + s[2] * s[2] : 'No: ' + s[0] * s[0] + ' + ' + s[1] * s[1] + ' ≠ ' + s[2] * s[2]}",
       [("{isRightTriangle(s[0], s[1], s[2]) ? 'No: ' + s[0] * s[0] + ' + ' + s[1] * s[1] + ' ≠ ' + s[2] * s[2] : 'Yes: ' + s[0] * s[0] + ' + ' + s[1] * s[1] + ' = ' + s[2] * s[2]}", "flip"),
        ("{'Yes: ' + s[0] + ' + ' + s[1] + ' > ' + s[2]}", "sides"), ("{'It cannot be decided without the angles'}", "angles")],
       ["Square the two shorter sides and add: {s[0] * s[0]} + {s[1] * s[1]} = {s[0] * s[0] + s[1] * s[1]}.", "The longest side squared is {s[2] * s[2]}.", "So: {answer}."],
       vars={"s": {"pick": [[6, 8, 10], [5, 12, 13], [8, 15, 17], [7, 24, 25], [9, 12, 15], [6, 8, 11], [5, 11, 13], [7, 9, 12], [8, 14, 17], [4, 6, 7]]}},
       misc=[("flip", "Compare carefully: {s[0] * s[0]} + {s[1] * s[1]} = {s[0] * s[0] + s[1] * s[1]} and {s[2]}² = {s[2] * s[2]}."),
             ("sides", "Compare the squares of the sides, not the sides themselves."),
             ("angles", "The converse of Pythagoras decides it from the sides alone.")],
       sources=SRC),
   num("m3-16-ladder", 3, "A ladder {c} m long leans against a vertical wall. Its foot is {a} m from the wall on level ground. How high up the wall does it reach (m)?", "b",
       ["The ladder is the hypotenuse: h² = {c}² − {a}² = {c * c} − {a * a} = {b * b}.", "h = √{b * b} = {answer} m."],
       vars={"i": {"pick": [0, 2, 4]}, "T": {"expr": "triple(i)"}, "k": {"pick": [0.5, 1]}, "a": {"expr": "T[0] * k"}, "b": {"expr": "T[1] * k"}, "c": {"expr": "T[2] * k"}},
       misc=[("add", "sqrt(c * c + a * a)", "The ladder is the longest side: subtract, h² = {c}² − {a}²."), ("diff", "c - a", "Subtract the squares, then take the square root.")],
       unit="m", figure="rightTriFig(a, 'h', c, 'm')", sources=SRC, where=["c - a != b"])],
  learn=learn(
    [("The longest side",
      "A right-angled triangle has one angle of {90}°. The side opposite it is the longest side, the hypotenuse.\n"
      "Pythagoras (a Greek mathematician) found that the square on the hypotenuse equals the sum of the squares on the other two sides:\n"
      "c² = a² + b², where c is the hypotenuse.\n"
      "With sides {3} cm and {4} cm: c² = {9} + {16} = {25}, so c = {5} cm.", "rightTriFig(3, 4, 5)"),
     ("Finding a shorter side",
      "If you know the hypotenuse and one side, rearrange: a² = c² − b².\n"
      "A ladder {10} m long reaches {8} m up a wall. The foot is √({100} − {64}) = √{36} = {6} m from the wall.\n"
      "Always ask first: which side is the hypotenuse? If you are looking for it, add the squares; if you know it, subtract."),
     ("Is it right-angled?",
      "The theorem also works backwards (its converse). For a triangle with sides {8}, {15} and {17}: {8}² + {15}² = {64} + {225} = {289} = {17}². So it has a right angle.\n"
      "For {6}, {8}, {11}: {36} + {64} = {100}, but {11}² = {121}. Not right-angled.\n"
      "Builders in Cameroon use the {3}-{4}-{5} rule with a rope to set out a square corner for a house.")],
    key_words=[("hypotenuse", "the longest side, opposite the right angle"), ("Pythagorean triple", "three whole numbers that fit c² = a² + b²"),
               ("converse", "the theorem used backwards, to test for a right angle")],
    examples=["{5}, {12}, {13}: {25} + {144} = {169}", "Sides {1} and {1}: hypotenuse √{2} ≈ {1.41}", "{9}, {12}, {15} is {3} × ({3}, {4}, {5})"],
    mistake=("Sides {6} and {8}: hypotenuse = {6} + {8} = {14}", "c² = {36} + {64} = {100}, so c = {10}",
             "Square the sides first, add the squares, then take the square root.")))

# ---------------------------------------------------------------- 17. Trigonometric ratios
SRC = ["trigonometry"]
L.lesson(D, S, 17, ("m3-17", "Sine, cosine and tangent of an acute angle; complementary angles"), [16],
  "In a right-angled triangle, name the sides from the marked angle θ: the hypotenuse (longest), the opposite side (facing θ) and the adjacent side (next to θ, not the hypotenuse).\n"
  "• sin θ = opposite ÷ hypotenuse\n• cos θ = adjacent ÷ hypotenuse\n• tan θ = opposite ÷ adjacent\n"
  "Memory aid: SOH CAH TOA.\n"
  "Complementary angles add to 90°: sin θ = cos(90° − θ) and cos θ = sin(90° − θ). For example sin 40° = cos 50°.",
  worked({"a": 4, "b": 3, "c": 5},
         "In the triangle, write sin θ, cos θ and tan θ as fractions.",
         ["Opposite θ: {b} cm. Adjacent to θ: {a} cm. Hypotenuse: {c} cm.",
          "sin θ = {b} ÷ {c} = {frac(b, c)}.", "cos θ = {a} ÷ {c} = {frac(a, c)}.", "tan θ = {b} ÷ {a} = {frac(b, a)}."],
         "sin θ = {frac(b, c)}, cos θ = {frac(a, c)}, tan θ = {frac(b, a)}", checks=["a * a + b * b == c * c"], figure="trigFig(a, b, c)"),
  [card("c3m17-1", "SOH: sin θ = opposite ÷ hypotenuse.",
        ["Opposite {3}, hypotenuse {5}: sin θ = {frac(3, 5)}."], "m3-17-ratio"),
   card("c3m17-2", "CAH and TOA: cos θ = adjacent ÷ hypotenuse; tan θ = opposite ÷ adjacent.",
        ["Adjacent {4}: cos θ = {frac(4, 5)}, tan θ = {frac(3, 4)}."], "m3-17-name"),
   card("c3m17-3", "Complementary angles: sin θ = cos({90}° − θ).",
        ["sin {40}° = cos {50}°; cos {25}° = sin {65}°"], "m3-17-comp")],
  [mcq("m3-17-ratio", 1, "In the triangle, what is {R}?",
       "{R == 'sin θ' ? frac(b, c) : R == 'cos θ' ? frac(a, c) : frac(b, a)}",
       [("{R == 'sin θ' ? frac(a, c) : R == 'cos θ' ? frac(b, c) : frac(a, b)}", "swap"),
        ("{R == 'sin θ' ? frac(c, b) : R == 'cos θ' ? frac(c, a) : frac(b, c)}", "flip"),
        ("{R == 'sin θ' ? frac(b, a) : R == 'cos θ' ? frac(b, a) : frac(a, c)}", "other")],
       ["Opposite θ: {b}; adjacent: {a}; hypotenuse: {c}.", "{R == 'sin θ' ? 'sin θ = opposite ÷ hypotenuse' : R == 'cos θ' ? 'cos θ = adjacent ÷ hypotenuse' : 'tan θ = opposite ÷ adjacent'} = {answer}."],
       vars={**TRI, "R": {"pick": ["sin θ", "cos θ", "tan θ"]}},
       misc=[("swap", "Name the sides from θ: the opposite side faces θ ({b}), the adjacent side touches θ ({a})."),
             ("flip", "{R == 'tan θ' ? 'tan θ uses opposite and adjacent, not the hypotenuse.' : 'The hypotenuse goes at the bottom: the ratio is less than one.'}"),
             ("other", "Use SOH CAH TOA: {R == 'sin θ' ? 'S = O ÷ H' : R == 'cos θ' ? 'C = A ÷ H' : 'T = O ÷ A'}.")],
       figure="trigFig(a, b, c)", sources=SRC, where=["a != b"]),
   bank("m3-17-name", 1, "{X.q}", [
     {"q": "Which ratio is opposite ÷ hypotenuse?", "r": "sin θ", "w": ["cos θ", "tan θ", "hyp θ"],
      "e": ["cos θ is adjacent ÷ hypotenuse.", "tan θ is opposite ÷ adjacent.", "There is no ratio called hyp θ."], "y": "SOH: sine is opposite over hypotenuse."},
     {"q": "Which ratio is opposite ÷ adjacent?", "r": "tan θ", "w": ["sin θ", "cos θ", "sec θ"],
      "e": ["sin θ is opposite ÷ hypotenuse.", "cos θ is adjacent ÷ hypotenuse.", "Not used in Form 3: TOA gives tan."], "y": "TOA: tangent is opposite over adjacent."},
     {"q": "Which side is the adjacent side for the angle θ?", "r": "The side next to θ that is not the hypotenuse", "w": ["The side facing θ", "The longest side", "Any side touching the right angle"],
      "e": ["The side facing θ is the opposite side.", "The longest side is the hypotenuse.", "One of the sides at the right angle is opposite θ."], "y": "Adjacent means next to: it touches θ but is not the hypotenuse."}], SRC),
   num("m3-17-compnum", 2, "Given that cos {A}° ≈ {roundTo(cosD(A), 0.0001)}, write down the value of sin {90 - A}°.", "roundTo(cosD(A), 0.0001)",
       ["{A}° and {90 - A}° add to {90}°: they are complementary.", "sin({90} − θ) = cos θ, so sin {90 - A}° = cos {A}° ≈ {answer}."],
       vars={"A": {"int": [10, 80]}},
       misc=[("sinA", "roundTo(sinD(A), 0.0001)", "That is sin {A}°. Use sin({90}° − θ) = cos θ.")],
       sources=SRC, where=["A != 45"]),
   num("m3-17-opp", 2, "In a right-angled triangle the hypotenuse is {h} cm and the marked angle is {A}°. Find the side opposite the angle, to {1} decimal place.", "roundTo(h * sinD(A), 0.1)",
       ["sin {A}° = opposite ÷ {h}.", "opposite = {h} × sin {A}° ≈ {h} × {roundTo(sinD(A), 0.0001)} ≈ {answer} cm."],
       vars={"h": {"int": [5, 20]}, "A": {"int": [15, 75]}},
       misc=[("cos", "roundTo(h * cosD(A), 0.1)", "That is the adjacent side (cos). The opposite side uses sin."),
             ("div", "roundTo(h / sinD(A), 0.1)", "opposite = hypotenuse × sin θ: multiply, do not divide.")],
       unit="cm", figure="trigFig('', 'x', h, A)", sources=SRC, where=["A != 45"]),
   mcq("m3-17-comp", 3, "Which statement is true?",
       "{'sin ' + A + '° = cos ' + (90 - A) + '°'}",
       [("{'sin ' + A + '° = cos ' + A + '°'}", "same"), ("{'sin ' + A + '° = sin ' + (90 - A) + '°'}", "sinsin"), ("{'cos ' + A + '° = cos ' + (90 - A) + '°'}", "coscos")],
       ["{A}° + {90 - A}° = {90}°: complementary angles.", "The sine of an angle equals the cosine of its complement. So: {answer}."],
       vars={"A": {"int": [10, 80]}},
       misc=[("same", "sin and cos of the same angle are equal only at {45}°."),
             ("sinsin", "The complement turns sine into cosine: sin θ = cos({90}° − θ)."),
             ("coscos", "The complement turns cosine into sine: cos θ = sin({90}° − θ).")],
       sources=SRC, where=["A != 45"])],
  learn=learn(
    [("Naming the sides from the angle",
      "Mark the angle θ you are interested in. Then name the three sides:\n"
      "• the hypotenuse: the longest side, opposite the right angle;\n• the opposite side: the side facing θ;\n• the adjacent side: the side next to θ that is not the hypotenuse.\n"
      "If you choose the other acute angle, opposite and adjacent swap over.", "trigFig('adjacent', 'opposite', 'hypotenuse')"),
     ("Three ratios",
      "For a given angle, the ratios of the sides are always the same, however big the triangle:\n"
      "• sin θ = opposite ÷ hypotenuse\n• cos θ = adjacent ÷ hypotenuse\n• tan θ = opposite ÷ adjacent\n"
      "Remember SOH CAH TOA. In the triangle with sides {3}, {4}, {5} and θ opposite the side {3}: sin θ = {frac(3, 5)}, cos θ = {frac(4, 5)}, tan θ = {frac(3, 4)}.\n"
      "sin and cos are always less than {1}, because the hypotenuse is the longest side."),
     ("Complementary angles",
      "The two acute angles of a right-angled triangle add up to {90}°: they are complementary.\n"
      "The side opposite one is adjacent to the other. So sin θ = cos({90}° − θ) and cos θ = sin({90}° − θ).\n"
      "For example sin {30}° = cos {60}° = {0.5}, and cos {20}° = sin {70}°.")],
    key_words=[("opposite", "the side facing the angle"), ("adjacent", "the side next to the angle, not the hypotenuse"),
               ("SOH CAH TOA", "sin = O ÷ H, cos = A ÷ H, tan = O ÷ A"), ("complementary angles", "two angles that add up to {90}°")],
    examples=["Sides {5}, {12}, {13}, θ facing {5}: sin θ = {frac(5, 13)}", "tan θ = {frac(12, 5)} for the other angle", "cos {35}° = sin {55}°"],
    mistake=("sin θ = adjacent ÷ hypotenuse", "sin θ = opposite ÷ hypotenuse (SOH)",
             "Name the sides from θ first. The opposite side faces θ; the adjacent side touches it.")))

# ---------------------------------------------------------------- 18. Special angles and calculators
SRC = ["trigonometry"]
L.lesson(D, S, 18, ("m3-18", "Trigonometric ratios of 30°, 45° and 60°; using a calculator"), [17],
  "Exact values to learn:\n"
  "• sin 30° = 1/2, cos 30° = √3/2, tan 30° = 1/√3\n"
  "• sin 45° = cos 45° = 1/√2 (= √2/2), tan 45° = 1\n"
  "• sin 60° = √3/2, cos 60° = 1/2, tan 60° = √3\n"
  "They come from half an equilateral triangle (30°, 60°) and half a square (45°).\n"
  "Calculator: check it is in degree mode (D or DEG). sin 37° ≈ 0.6018. To find an angle from a ratio use the inverse key: sin⁻¹(0.5) = 30°.",
  worked({"d": 25, "A": 35},
         "From a point {d} m from the foot of a tree, the angle of elevation of the top is {A}°. Find the height of the tree to {1} decimal place.",
         ["tan {A}° = height ÷ {d}.", "height = {d} × tan {A}° ≈ {d} × {roundTo(tanD(A), 0.0001)}.", "height ≈ {roundTo(d * tanD(A), 0.1)} m."],
         "{roundTo(d * tanD(A), 0.1)} m", checks=["roundTo(d * tanD(A), 0.1) == 17.5"], figure="trigFig(d, 'h', '', A, 'm')"),
  [card("c3m18-1", "Learn the exact values for {30}°, {45}° and {60}°.",
        ["sin {30}° = {frac(1, 2)}, tan {45}° = {1}, cos {60}° = {frac(1, 2)}"], "m3-18-exact"),
   card("c3m18-2", "Use a calculator in degree mode; round as the question asks.",
        ["sin {37}° ≈ {roundTo(sinD(37), 0.0001)}"], "m3-18-calc"),
   card("c3m18-3", "The inverse key gives the angle: sin⁻¹, cos⁻¹, tan⁻¹.",
        ["tan θ = {1} → θ = tan⁻¹({1}) = {45}°"], "m3-18-inv")],
  [bank("m3-18-exact", 1, "What is the exact value of {X.q}?", [
     {"q": "sin 30°", "r": "1/2", "w": ["√3/2", "1/√2", "√3"], "e": ["√3/2 is sin 60° (or cos 30°).", "1/√2 is sin 45°.", "√3 is tan 60°."], "y": "sin 30° = 1/2 (half an equilateral triangle)."},
     {"q": "cos 30°", "r": "√3/2", "w": ["1/2", "1/√3", "1"], "e": ["1/2 is cos 60°.", "1/√3 is tan 30°.", "cos 30° is less than 1."], "y": "cos 30° = √3/2."},
     {"q": "tan 45°", "r": "1", "w": ["1/√2", "√3", "1/2"], "e": ["1/√2 is sin 45° and cos 45°.", "√3 is tan 60°.", "1/2 is sin 30°."], "y": "In half a square, opposite = adjacent, so tan 45° = 1."},
     {"q": "tan 60°", "r": "√3", "w": ["1/√3", "√3/2", "1"], "e": ["1/√3 is tan 30°.", "√3/2 is sin 60°.", "1 is tan 45°."], "y": "tan 60° = √3."},
     {"q": "sin 45°", "r": "1/√2", "w": ["1", "1/2", "√3/2"], "e": ["1 is tan 45°.", "1/2 is sin 30°.", "√3/2 is sin 60°."], "y": "sin 45° = 1/√2 = √2/2."}], SRC),
   num("m3-18-calc", 1, "Use a calculator: find {R} {A}° to {4} decimal places.", "roundTo(R == 'sin' ? sinD(A) : R == 'cos' ? cosD(A) : tanD(A), 0.0001)",
       ["Set the calculator to degrees (DEG).", "{R} {A}° ≈ {answer}."],
       vars={"R": {"pick": ["sin", "cos", "tan"]}, "A": {"int": [5, 80]}},
       misc=[("other", "roundTo(R == 'sin' ? cosD(A) : sinD(A), 0.0001)", "Check you pressed the right key: {R}, not {R == 'sin' ? 'cos' : 'sin'}.")],
       sources=SRC, where=["A != 30 && A != 45 && A != 60", "A != 45"]),
   num("m3-18-inv", 2, "{R} θ = {r}. Find the acute angle θ to {1} decimal place.", "roundTo(R == 'sin' ? asinD(r) : R == 'cos' ? acosD(r) : atanD(r), 0.1)",
       ["Use the inverse key: θ = {R}⁻¹({r}).", "θ ≈ {answer}°."],
       vars={"R": {"pick": ["sin", "cos", "tan"]}, "n": {"int": [12, 95]}, "r": {"expr": "n / 100"}},
       misc=[("recip", "roundTo(1 / r, 0.1)", "{R}⁻¹ is the inverse function (the angle), not {1} ÷ {r}.")],
       unit="°", sources=SRC),
   num("m3-18-value", 2, "Without a calculator, find the value of {X.e}.", "X.v",
       ["{X.s}", "= {answer}."],
       vars={"X": {"pick": [
         {"e": "sin 30° + cos 60°", "s": "1/2 + 1/2", "v": 1},
         {"e": "4 sin 30° × tan 45°", "s": "4 × 1/2 × 1", "v": 2},
         {"e": "tan 45° − cos 60°", "s": "1 − 1/2", "v": 0.5},
         {"e": "2 cos 60° + 3 tan 45°", "s": "2 × 1/2 + 3 × 1", "v": 4},
         {"e": "sin² 45° + cos² 45°", "s": "(1/√2)² + (1/√2)² = 1/2 + 1/2", "v": 1},
         {"e": "tan 60° × tan 30°", "s": "√3 × 1/√3", "v": 1}]}},
       review="authored", sources=SRC),
   num("m3-18-tree", 3, "From a point {d} m from the foot of a tree on level ground, the angle of elevation of the top of the tree is {A}°. Find the height of the tree to {1} decimal place.", "roundTo(d * tanD(A), 0.1)",
       ["tan {A}° = height ÷ {d}.", "height = {d} × tan {A}° ≈ {d} × {roundTo(tanD(A), 0.0001)} ≈ {answer} m."],
       vars={"d": {"int": [8, 40]}, "A": {"int": [20, 65]}},
       misc=[("sin", "roundTo(d * sinD(A), 0.1)", "The distance {d} m is adjacent to the angle and the height is opposite: use tan."),
             ("div", "roundTo(d / tanD(A), 0.1)", "height = {d} × tan {A}°: multiply.")],
       unit="m", figure="trigFig(d, 'h', '', A, 'm')", sources=SRC, where=["A != 45"])],
  learn=learn(
    [("Where the exact values come from",
      "Half of a square with side {1}: the angles are {45}°, {45}° and {90}°; the diagonal is √{2}. So sin {45}° = cos {45}° = {1} ÷ √{2} and tan {45}° = {1}.\n"
      "Half of an equilateral triangle with side {2}: the angles are {30}°, {60}° and {90}°; the sides are {1}, √{3} and {2}. So:\n"
      "• sin {30}° = {frac(1, 2)}, cos {30}° = √{3} ÷ {2}, tan {30}° = {1} ÷ √{3}\n• sin {60}° = √{3} ÷ {2}, cos {60}° = {frac(1, 2)}, tan {60}° = √{3}."),
     ("Using a calculator",
      "First check the calculator shows D or DEG (degree mode). In radian mode every answer is wrong.\n"
      "To find sin {37}°, press sin {37} = and read about {roundTo(sinD(37), 0.0001)}.\n"
      "To find an angle from a ratio, use the inverse: SHIFT then sin gives sin⁻¹. If sin θ = {0.5}, then θ = sin⁻¹({0.5}) = {30}°.\n"
      "Keep four decimal places while working; round only the final answer."),
     ("Angles of elevation",
      "Look up at the top of a tree: the angle between the level ground and your line of sight is the angle of elevation. Looking down from a cliff gives an angle of depression.\n"
      "If you stand {20} m from a tree and the elevation is {35}°, the height h satisfies tan {35}° = h ÷ {20}, so h = {20} × tan {35}° ≈ {roundTo(20 * tanD(35), 0.1)} m.")],
    key_words=[("exact value", "a value written with fractions and roots, not rounded"), ("degree mode", "the calculator setting for angles in degrees"),
               ("inverse ratio", "sin⁻¹, cos⁻¹, tan⁻¹: from a ratio back to the angle"), ("angle of elevation", "the angle looking up from the horizontal")],
    examples=["cos {60}° = {frac(1, 2)}", "tan {30}° × tan {60}° = {1}", "cos⁻¹({0.5}) = {60}°"],
    mistake=("sin {30}° = {roundTo(sinD(30 * 57.29577951), 0.0001)} on the calculator", "sin {30}° = {0.5}",
             "That value comes from radian mode. Set the calculator to degrees (DEG).")))

# ---------------------------------------------------------------- 19. Solving right-angled triangles
SRC = ["trigonometry"]
L.lesson(D, S, 19, ("m3-19", "Solve right-angled triangles: find missing sides and angles"), [17, 18],
  "To solve a right-angled triangle is to find all its sides and angles.\n"
  "• Label the sides from the known (or wanted) angle: opposite, adjacent, hypotenuse.\n"
  "• Choose the ratio that uses the two sides involved (SOH CAH TOA).\n"
  "• Unknown side on top: multiply (x = 10 × sin 30°). Unknown side at the bottom: divide (x = 10 ÷ tan 30°).\n"
  "• Unknown angle: use the inverse key (θ = tan⁻¹(5/12)).\n"
  "• The two acute angles add up to 90°, and Pythagoras gives the third side.",
  worked({"o": 5, "a": 12},
         "In a right-angled triangle the side opposite θ is {o} cm and the adjacent side is {a} cm. Find θ to {1} decimal place.",
         ["Opposite and adjacent: use tan.", "tan θ = {o} ÷ {a}.", "θ = tan⁻¹({o} ÷ {a}) ≈ {roundTo(atanD(o / a), 0.1)}°."],
         "θ ≈ {roundTo(atanD(o / a), 0.1)}°", checks=["roundTo(atanD(o / a), 0.1) == 22.6"], figure="trigFig(a, o, '')"),
  [card("c3m19-1", "Pick the ratio with the two sides you know or want.",
        ["Opposite and hypotenuse → sin; adjacent and hypotenuse → cos; opposite and adjacent → tan."], "m3-19-angle"),
   card("c3m19-2", "Unknown side on top of the ratio: multiply. At the bottom: divide.",
        ["sin {30}° = x ÷ {10} → x = {10} × sin {30}° = {5}", "tan {45}° = {7} ÷ x → x = {7} ÷ tan {45}° = {7}"], "m3-19-adj"),
   card("c3m19-3", "Find an angle with the inverse key.",
        ["cos θ = {frac(1, 2)} → θ = cos⁻¹({0.5}) = {60}°"], "m3-19-hyp")],
  [num("m3-19-angle", 1, "In a right-angled triangle the side opposite θ is {o} cm and the adjacent side is {a} cm. Find θ to {1} decimal place.", "roundTo(atanD(o / a), 0.1)",
       ["Opposite and adjacent: tan θ = {o} ÷ {a}.", "θ = tan⁻¹({o} ÷ {a}) ≈ {answer}°."],
       vars={"o": {"int": [2, 15]}, "a": {"int": [2, 15]}},
       misc=[("flip", "roundTo(atanD(a / o), 0.1)", "tan θ = opposite ÷ adjacent = {o} ÷ {a}, not {a} ÷ {o}.")],
       unit="°", figure="trigFig(a, o, '')", sources=SRC, where=["o != a"]),
   num("m3-19-adj", 1, "The hypotenuse is {h} cm and θ = {A}°. Find the side adjacent to θ, to {1} decimal place.", "roundTo(h * cosD(A), 0.1)",
       ["Adjacent and hypotenuse: cos {A}° = x ÷ {h}.", "x = {h} × cos {A}° ≈ {answer} cm."],
       vars={"h": {"int": [5, 25]}, "A": {"int": [15, 75]}},
       misc=[("sin", "roundTo(h * sinD(A), 0.1)", "That is the opposite side. The adjacent side uses cos."),
             ("div", "roundTo(h / cosD(A), 0.1)", "x is on top of the ratio: multiply, x = {h} × cos {A}°.")],
       unit="cm", figure="trigFig('x', '', h, A)", sources=SRC, where=["A != 45"]),
   num("m3-19-hyp", 2, "The side opposite θ is {o} cm and θ = {A}°. Find the hypotenuse, to {1} decimal place.", "roundTo(o / sinD(A), 0.1)",
       ["Opposite and hypotenuse: sin {A}° = {o} ÷ x.", "x is at the bottom: x = {o} ÷ sin {A}° ≈ {answer} cm."],
       vars={"o": {"int": [3, 20]}, "A": {"int": [15, 75]}},
       misc=[("mult", "roundTo(o * sinD(A), 0.1)", "x is at the bottom of the ratio: divide, x = {o} ÷ sin {A}°. The hypotenuse must be the longest side."),
             ("cos", "roundTo(o / cosD(A), 0.1)", "{o} cm is opposite θ: use sin.")],
       unit="cm", figure="trigFig('', o, 'x', A)", sources=SRC, where=["A != 45"]),
   num("m3-19-sinangle", 2, "The side opposite θ is {o} cm and the hypotenuse is {h} cm. Find θ to {1} decimal place.", "roundTo(asinD(o / h), 0.1)",
       ["Opposite and hypotenuse: sin θ = {o} ÷ {h}.", "θ = sin⁻¹({o} ÷ {h}) ≈ {answer}°."],
       vars={"o": {"int": [2, 15]}, "h": {"int": [5, 25]}},
       misc=[("cos", "roundTo(acosD(o / h), 0.1)", "{o} cm is opposite θ: use sin⁻¹, not cos⁻¹."), ("tan", "roundTo(atanD(o / h), 0.1)", "{h} cm is the hypotenuse: use sin, not tan.")],
       unit="°", figure="trigFig('', o, h)", sources=SRC, where=["o < h", "o * 2 != h"]),
   num("m3-19-cliff", 3, "From the top of a cliff {h} m high, the angle of depression of a canoe on the sea is {A}°. How far is the canoe from the foot of the cliff, to the nearest metre?", "roundTo(h / tanD(A), 1)",
       ["The angle of depression equals the angle of elevation from the canoe to the top: {A}°.",
        "From the canoe: tan {A}° = {h} ÷ d, so d = {h} ÷ tan {A}°.", "d ≈ {h} ÷ {roundTo(tanD(A), 0.0001)} ≈ {answer} m."],
       vars={"h": {"int": [20, 120]}, "A": {"int": [15, 60]}},
       misc=[("mult", "roundTo(h * tanD(A), 1)", "d is at the bottom of tan {A}° = {h} ÷ d: divide."), ("sin", "roundTo(h / sinD(A), 1)", "That is the line of sight (the hypotenuse). The distance along the sea uses tan.")],
       unit="m", figure="trigFig('d', h, '', A, 'm')", sources=SRC, where=["A != 45"])],
  learn=learn(
    [("Which ratio?",
      "Mark the angle. Label the sides you know and the side you want: opposite, adjacent or hypotenuse. Then pick the ratio that links those two:\n"
      "• opposite and hypotenuse → sin;\n• adjacent and hypotenuse → cos;\n• opposite and adjacent → tan.\n"
      "Write the ratio as an equation, for example sin {35}° = x ÷ {12}."),
     ("Solving the equation",
      "• If x is on top: multiply. sin {35}° = x ÷ {12} gives x = {12} × sin {35}° ≈ {roundTo(12 * sinD(35), 0.1)}.\n"
      "• If x is at the bottom: divide. tan {35}° = {8} ÷ x gives x = {8} ÷ tan {35}° ≈ {roundTo(8 / tanD(35), 0.1)}.\n"
      "• For an angle: tan θ = {5} ÷ {12} gives θ = tan⁻¹({5} ÷ {12}) ≈ {roundTo(atanD(5 / 12), 0.1)}°.\n"
      "A quick check: the hypotenuse must be the longest side."),
     ("Elevation and depression",
      "From the top of a cliff, you look down at a canoe: the angle between the horizontal and your line of sight is the angle of depression. "
      "Because the horizontal at the top is parallel to the sea, it equals the angle of elevation from the canoe up to you.\n"
      "So the triangle at the foot of the cliff has that angle, the cliff height opposite it and the distance along the sea adjacent to it: use tan.")],
    key_words=[("solve a triangle", "find all its unknown sides and angles"), ("angle of depression", "the angle looking down from the horizontal"),
               ("inverse key", "sin⁻¹, cos⁻¹, tan⁻¹ on a calculator")],
    examples=["Hypotenuse {10}, θ = {30}°: opposite = {10} × sin {30}° = {5}",
              "Opposite {6}, adjacent {6}: θ = tan⁻¹({1}) = {45}°"],
    mistake=("sin {40}° = {6} ÷ x → x = {6} × sin {40}°", "x = {6} ÷ sin {40}° ≈ {roundTo(6 / sinD(40), 0.1)}",
             "When x is at the bottom of the fraction, divide. The hypotenuse must come out longer than {6}.")))
