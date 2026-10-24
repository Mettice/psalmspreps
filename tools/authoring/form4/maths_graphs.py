"""Form 4 Maths, Term 1, rows 20-25: graphs (simultaneous equations, half planes, regions, quadratic graphs, the
discriminant, graphical solutions of quadratics). Figures come from graphFig (src/engine/lib/maths2.js); in a region,
the UNWANTED part is shaded, as in GCE answers (TEACHER-REVIEW TR-M4-6). Run: python tools/authoring/form4/maths_graphs.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import goal

L.use_class("form-4", "Form 4")
D, S = "maths", "mathematics"
SRC = ["graphs"]
R6 = "[-6, 6]"

# two lines y = m1·x + c1 and y = m2·x + c2 crossing at (h, k)
TWO = {"h": {"int": [-4, 4]}, "k": {"int": [-4, 4]}, "m1": {"pick": [-2, -1, 1, 2, 3]}, "m2": {"pick": [-3, -2, -1, 1, 2]},
       "c1": {"expr": "k - m1 * h"}, "c2": {"expr": "k - m2 * h"}}
TWOFIG = f"graphFig({R6}, {R6}, [[-m1, 1, c1, false, 'A'], [-m2, 1, c2, false, 'B']])"
TWOWHERE = ["m1 != m2", "h != k", "c1 != 0 && c2 != 0", "abs(c1) <= 9 && abs(c2) <= 9", "h != 0 && k != 0"]

# ---------------------------------------------------------------- 20. Graphical solution of simultaneous linear equations
L.lesson(D, S, 20, ("m4-20", "Solve simultaneous linear equations by drawing graphs"), [16],
  "To solve two linear equations with graphs:\n"
  "1. Make a table of values for each line (three points are enough; the third is a check).\n"
  "2. Draw both lines on the same axes.\n"
  "3. The point where they cross gives the solution: its x-coordinate and its y-coordinate.\n"
  "Example: y = x + 1 and y = −x + 5 cross at (2, 3), so x = 2 and y = 3.\n"
  "Check by substituting into both equations. Parallel lines (same gradient) never cross: no solution.",
  worked({"h": 2, "k": 3, "m1": 1, "m2": -1, "c1": 1, "c2": 5},
         "Solve y = {poly([m1, 'x'], [c1, ''])} and y = {poly([m2, 'x'], [c2, ''])} graphically.",
         ["Table for y = {poly([m1, 'x'], [c1, ''])}: x = {0}, y = {c1}; x = {2}, y = {2 * m1 + c1}; x = {4}, y = {4 * m1 + c1}.",
          "Table for y = {poly([m2, 'x'], [c2, ''])}: x = {0}, y = {c2}; x = {2}, y = {2 * m2 + c2}; x = {4}, y = {4 * m2 + c2}.",
          "Draw both lines. They cross at ({h}, {k}).",
          "Check: {m1 * h + c1} = {k} and {m2 * h + c2} = {k}."],
         "x = {h}, y = {k}",
         figure=f"graphFig([-1, 6], [-1, 6], [[-m1, 1, c1, false, 'A'], [-m2, 1, c2, false, 'B']], [], [], [['P', h, k]])",
         checks=["m1 * h + c1 == k", "m2 * h + c2 == k"]),
  [card("c4m20-1", "Each line is the picture of all the solutions of one equation.",
        ["Every point on y = x + {1} satisfies the equation: ({0}, {1}), ({1}, {2}), ({2}, {3}) …"], "m4-20-table"),
   card("c4m20-2", "The crossing point satisfies both equations at once: it is the solution.",
        ["y = x + {1} and y = −x + {5} cross at ({2}, {3}): x = {2}, y = {3}"], "m4-20-read"),
   card("c4m20-3", "Parallel lines never cross, so the equations have no solution.",
        ["y = {mono(2, 'x')} + {1} and y = {mono(2, 'x')} − {3}: same gradient, no crossing"], "m4-20-parallel")],
  [num("m4-20-table", 1, "Complete the table of values for y = {poly([m, 'x'], [c, ''])}. What is y when x = {t}?",
       "m * t + c",
       ["y = {m} × {br(t)} + {br(c)}.", "= {m * t} + {br(c)} = {answer}."],
       vars={"m": {"int": [-3, 3]}, "c": {"int": [-5, 5]}, "t": {"int": [-3, 3]}},
       misc=[("noc", "m * t", "Add the {c} after multiplying: {m * t} + {br(c)}."),
             ("add", "m + t + c", "{mono(m, 'x')} means {m} × x: multiply by {t}.")],
       sources=SRC, where=["m != 0 && c != 0 && t != 0", "m * t + c != m + t + c"], signed=True),
   mcq("m4-20-read", 1, "The graph shows lines A and B. Use it to solve their two equations.",
       "x = {h}, y = {k}",
       [("x = {k}, y = {h}", "swap"), ("x = {0}, y = {c1}", "icept"), ("x = {h}, y = {0}", "axis")],
       ["The solution is where the lines cross.", "They cross at ({h}, {k}): x = {h}, y = {k}.", "So the answer is {answer}."],
       vars=TWO, figure=TWOFIG,
       misc=[("swap", "Read x across (horizontal) first, then y up: the point is ({h}, {k})."),
             ("icept", "({0}, {c1}) is where line A meets the y-axis. Line B does not pass through it."),
             ("axis", "The crossing is at height y = {k}, not on the x-axis.")],
       sources=SRC, where=TWOWHERE),
   num("m4-20-meet", 2, "The lines y = {poly([m1, 'x'], [c1, ''])} and y = {poly([m2, 'x'], [c2, ''])} are drawn. At what value of x do they cross?",
       "h",
       ["At the crossing both y values are equal: {poly([m1, 'x'], [c1, ''])} = {poly([m2, 'x'], [c2, ''])}.",
        "{mono(m1 - m2, 'x')} = {c2 - c1}, so x = {answer}.", "Check on the graph: at x = {h} both lines have y = {k}."],
       vars=TWO, figure=TWOFIG,
       misc=[("y", "k", "{k} is the y-coordinate of the crossing. The question asks for x."),
             ("c", "c2 - c1", "Divide by {m1 - m2}: x = {c2 - c1} ÷ {br(m1 - m2)} = {h}.")],
       sources=SRC, where=TWOWHERE + ["m1 - m2 != 1"], signed=True),
   mcq("m4-20-check", 2, "Asong drew y = {poly([m1, 'x'], [c1, ''])} and y = {poly([m2, 'x'], [c2, ''])} and read off the crossing as ({h + 1}, {k}). Is that right?",
       "No: x = {h + 1} gives y = {m1 * (h + 1) + c1} on the first line and {m2 * (h + 1) + c2} on the second. The lines cross at ({h}, {k})",
       [("Yes: the point is on both lines", "yes"), ("No: the lines are parallel and never cross", "par"), ("No: the crossing is at ({k}, {h})", "swap")],
       ["Substitute x = {h + 1}: the two lines give different y values, so it is not on both.",
        "At x = {h} both give y = {k}.", "So the answer is: {answer}."],
       vars=TWO,
       misc=[("yes", "Substitute x = {h + 1}: y = {m1 * (h + 1) + c1} and y = {m2 * (h + 1) + c2} are different."),
             ("par", "The gradients {m1} and {m2} are different, so the lines do cross."),
             ("swap", "({k}, {h}) has x and y swapped. Check: it does not satisfy y = {poly([m1, 'x'], [c1, ''])}.")],
       sources=SRC, where=TWOWHERE + ["m1 * k + c1 != h || m2 * k + c2 != h"]),
   mcq("m4-20-parallel", 3, "How many solutions do y = {poly([m, 'x'], [c1, ''])} and y = {poly([m, 'x'], [c2, ''])} have?",
       "None: the lines are parallel",
       [("One: the lines cross once", "one"), ("Two", "two"), ("Infinitely many: the lines are the same", "same")],
       ["Both lines have gradient {m}, so they are parallel.", "The y-intercepts {c1} and {c2} are different, so they are not the same line.", "So the answer is: {answer}."],
       vars={"m": {"int": [-3, 3]}, "c1": {"int": [-6, 6]}, "c2": {"int": [-6, 6]}},
       figure=f"graphFig({R6}, {R6}, [[-m, 1, c1, false, 'A'], [-m, 1, c2, false, 'B']])",
       misc=[("one", "Lines with the same gradient never meet."),
             ("two", "Two straight lines can cross at most once."),
             ("same", "The lines cross the y-axis at {c1} and {c2}: different lines.")],
       sources=SRC, where=["m != 0", "c1 != c2", "abs(c1 - c2) >= 2"])],
  learn=learn(
    [goal("draw two straight lines from tables of values and read the solution of the simultaneous equations from where they cross.",
          "Form Three straight-line graphs (y = mx + c) and Lesson {16}.",
          "Lessons {21} and {22} (regions), where lines become the edges of a solution set."),
     ("From equation to line",
      "Each linear equation, such as y = x + {1}, has many solutions: ({0}, {1}), ({1}, {2}), ({2}, {3}) … On a graph they make a straight line.\n"
      "To draw it, make a table with three values of x, work out y, plot the points and join them with a ruler. "
      "The third point is a check: if it is not in line, a value is wrong.\n"
      "For y = −x + {5}: x = {0} gives {5}, x = {2} gives {3}, x = {4} gives {1}."),
     ("Reading the solution",
      "Draw y = x + {1} and y = −x + {5} on the same axes. They cross at ({2}, {3}).\n"
      "That point is on both lines, so it satisfies both equations: x = {2}, y = {3}.\n"
      "Check: {2} + {1} = {3} and −{2} + {5} = {3}.\n"
      "Read the x-coordinate first (across), then y (up). If the crossing is between grid lines, give the closest reading and check algebraically. "
      "Lines with the same gradient are parallel: no solution.")],
    key_words=[("simultaneous equations", "two equations that must both be true at once"),
               ("table of values", "chosen x values with the y values worked out"),
               ("point of intersection", "where two lines cross"),
               ("gradient", "the steepness m in y = mx + c")],
    examples=["y = {mono(2, 'x')} and y = x + {3} cross at ({3}, {6})", "y = x − {1} and y = {mono(-2, 'x')} + {5} cross at ({2}, {1})"],
    mistake=("crossing at ({2}, {3}) → x = {3}, y = {2}", "crossing at ({2}, {3}) → x = {2}, y = {3}",
             "Coordinates are written (x, y): across first, then up.")))

# ---------------------------------------------------------------- 21. Linear inequalities on a graph: half planes
HALF = {"m": {"pick": [-2, -1, 1, 2]}, "c": {"int": [-3, 3]}, "op": {"pick": ["<", "≤", ">", "≥"]},
        "below": {"expr": "op == '<' || op == '≤'"}, "strict": {"expr": "op == '<' || op == '>'"}}
HALFFIG = f"graphFig({R6}, {R6}, [[-m, 1, c, strict, '']], [below ? [-m, 1, c] : [m, -1, -c]])"

L.lesson(D, S, 21, ("m4-21", "Show a linear inequality as a region (half plane) on a graph"), [20],
  "A line divides the plane into two half planes. An inequality such as y ≤ 2x + 1 describes one of them.\n"
  "1. Draw the boundary line y = 2x + 1: solid if the line is included (≤, ≥), broken if not (<, >).\n"
  "2. Test a point not on the line, usually O(0, 0): 0 ≤ 1 is true, so O is in the wanted region.\n"
  "3. Shade the unwanted side (the convention in GCE answers), leaving the wanted region clear.\n"
  "x ≥ 3 is the region to the right of the vertical line x = 3; y < −1 is below the horizontal line y = −1.",
  worked({"m": 2, "c": 1},
         "Show y ≤ {poly([m, 'x'], [c, ''])} on a graph.",
         ["Boundary y = {poly([m, 'x'], [c, ''])}: x = {0}, y = {c}; x = {1}, y = {m + c}. ≤ includes the line, so draw it solid.",
          "Test O({0}, {0}): {0} ≤ {c} is true, so O is in the wanted region.",
          "Shade the other side, above the line: that is the unwanted region."],
         "the unshaded region below the solid line y = {poly([m, 'x'], [c, ''])}",
         figure="graphFig([-4, 4], [-4, 4], [[-m, 1, c, false, '']], [[-m, 1, c]])",
         checks=["c > 0"]),
  [card("c4m21-1", "≤ and ≥ include the line: draw it solid. < and > leave it out: draw it broken.",
        ["y < x + {2}: broken line; y ≥ x + {2}: solid line"], "m4-21-line"),
   card("c4m21-2", "Test a point such as O({0}, {0}): if it makes the inequality true, it is in the wanted region.",
        ["y ≤ {mono(2, 'x')} + {1}: {0} ≤ {1} is true, so O is wanted"], "m4-21-point"),
   card("c4m21-3", "Shade the unwanted side; the clear region is the solution.",
        ["for y ≤ {mono(2, 'x')} + {1}, shade above the line"], "m4-21-read")],
  [mcq("m4-21-line", 1, "When you draw the boundary of {mono(a, 'x')} + {mono(b, 'y')} {op} {c} on a graph, how should the line be drawn?",
       "{op == '<' || op == '>' ? 'Broken, because the line itself is not included' : 'Solid, because the line itself is included'}",
       [("{op == '<' || op == '>' ? 'Solid, because the line itself is included' : 'Broken, because the line itself is not included'}", "swap"),
        ("Solid, because every boundary is drawn solid", "always"), ("{op == '<' || op == '>' ? 'Broken, because the region is below the line' : 'Solid, because the region is above the line'}", "side")],
       ["{op} {op == '<' || op == '>' ? 'leaves out the equals case' : 'includes the equals case'}.", "So the answer is: {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [1, 4]}, "c": {"int": [2, 12]}, "op": {"pick": ["<", "≤", ">", "≥"]}},
       misc=[("swap", "≤ and ≥ include the line (solid); < and > do not (broken)."),
             ("always", "A boundary that is not part of the solution is drawn broken."),
             ("side", "Solid or broken depends on whether the line is included, not on which side the region is.")],
       sources=SRC),
   mcq("m4-21-point", 1, "Is the point ({px}, {py}) in the region y {op} {poly([m, 'x'], [c, ''])}?",
       "{holds(py, op, m * px + c) ? 'Yes: ' + fmt(py) + ' ' + op + ' ' + fmt(m * px + c) + ' is true' : 'No: ' + fmt(py) + ' ' + op + ' ' + fmt(m * px + c) + ' is false'}",
       [("{holds(py, op, m * px + c) ? 'No: ' + fmt(py) + ' ' + op + ' ' + fmt(m * px + c) + ' is false' : 'Yes: ' + fmt(py) + ' ' + op + ' ' + fmt(m * px + c) + ' is true'}", "flip"),
        ("Yes: every point with a positive x is in it", "posx"), ("No: points on the boundary are never included", "edge")],
       ["Substitute x = {px}: {poly([m, 'x'], [c, ''])} = {m * px + c}.", "Compare with y = {py}: is {py} {op} {m * px + c}? {holds(py, op, m * px + c) ? 'Yes.' : 'No.'}", "So the answer is: {answer}."],
       vars={**HALF, "px": {"int": [-3, 3]}, "py": {"int": [-4, 4]}},
       misc=[("flip", "Substitute and compare: {py} {op} {m * px + c} is {holds(py, op, m * px + c) ? 'true' : 'false'}."),
             ("posx", "Whether a point is in the region depends on the inequality, not just on x."),
             ("edge", "With ≤ or ≥ the boundary is included. Substitute and compare.")],
       sources=SRC, where=["py != m * px + c"]),
   mcq("m4-21-read", 2, "The graph shows a line and a shaded (unwanted) region. Which inequality describes the unshaded region?",
       "y {op} {poly([m, 'x'], [c, ''])}",
       [("y {flipOp(op)} {poly([m, 'x'], [c, ''])}", "side"), ("y {strict ? looseOp(op) : strictOp(op)} {poly([m, 'x'], [c, ''])}", "line"), ("y {op} {poly([-m, 'x'], [c, ''])}", "grad")],
       ["The boundary is y = {poly([m, 'x'], [c, ''])}, drawn {strict ? 'broken (not included)' : 'solid (included)'}.",
        "The clear region is {below ? 'below' : 'above'} the line.", "So the answer is {answer}."],
       vars=HALF, figure=HALFFIG,
       misc=[("side", "The shading is the unwanted side. The clear region is {below ? 'below' : 'above'} the line."),
             ("line", "Look at the line: {strict ? 'broken, so it is not included' : 'solid, so it is included'}."),
             ("grad", "The line slopes {m > 0 ? 'up' : 'down'} to the right, so its gradient is {m}.")],
       sources=SRC, where=["c != 0"]),
   mcq("m4-21-vert", 2, "The graph shows the region {v == 'x' ? 'beside a vertical line' : 'beside a horizontal line'}. The unshaded part is wanted. Which inequality describes it?",
       "{v} {op} {k}",
       [("{v} {flipOp(op)} {k}", "side"), ("{v == 'x' ? 'y' : 'x'} {op} {k}", "axis"), ("{v} {strict ? looseOp(op) : strictOp(op)} {k}", "line")],
       ["The boundary is the {v == 'x' ? 'vertical' : 'horizontal'} line {v} = {k}, drawn {strict ? 'broken' : 'solid'}.",
        "The clear side is where {v} is {op == '<' || op == '≤' ? 'smaller' : 'larger'}.", "So the answer is {answer}."],
       vars={"v": {"pick": ["x", "y"]}, "k": {"int": [-3, 3]}, "op": {"pick": ["<", "≤", ">", "≥"]},
             "strict": {"expr": "op == '<' || op == '>'"}, "lo": {"expr": "op == '<' || op == '≤'"}},
       figure=f"graphFig({R6}, {R6}, [v == 'x' ? [1, 0, k, strict, ''] : [0, 1, k, strict, '']], [v == 'x' ? (lo ? [1, 0, k] : [-1, 0, -k]) : (lo ? [0, 1, k] : [0, -1, -k])])",
       misc=[("side", "The shaded side is unwanted; the wanted side is where {v} is {op == '<' || op == '≤' ? 'smaller' : 'larger'} than {k}."),
             ("axis", "A {v == 'x' ? 'vertical' : 'horizontal'} line has the equation {v} = {k}."),
             ("line", "The line is {strict ? 'broken: not included' : 'solid: included'}.")],
       sources=SRC, where=["k != 0"]),
   mcq("m4-21-origin", 3, "To show {mono(a, 'x')} + {mono(b, 'y')} {op} {c} you draw the line {mono(a, 'x')} + {mono(b, 'y')} = {c}. Which side do you shade (unwanted)?",
       "{holds(0, op, c) ? 'The side that does not contain O(0, 0), because O satisfies the inequality' : 'The side that contains O(0, 0), because O does not satisfy the inequality'}",
       [("{holds(0, op, c) ? 'The side that contains O(0, 0), because O satisfies the inequality' : 'The side that does not contain O(0, 0), because O does not satisfy the inequality'}", "swap"),
        ("Always the side above the line", "above"), ("Always the side containing O(0, 0)", "origin")],
       ["Test O: {a} × {0} + {b} × {0} = {0}, and {0} {op} {c} is {holds(0, op, c) ? 'true' : 'false'}.",
        "{holds(0, op, c) ? 'O is wanted, so shade the other side.' : 'O is unwanted, so shade its side.'}", "So the answer is: {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [1, 5]}, "c": {"int": [-12, 12]}, "op": {"pick": ["<", "≤", ">", "≥"]}},
       misc=[("swap", "If O satisfies the inequality, O's side is wanted and stays clear."),
             ("above", "'Above' depends on the inequality. Test a point such as O."),
             ("origin", "O's side is shaded only if O does not satisfy the inequality.")],
       sources=SRC, where=["c != 0"])],
  learn=learn(
    [goal("draw the region for a linear inequality: the right boundary (solid or broken) and the right side, tested with a point.",
          "Lesson {20} (drawing lines) and Lesson {16} (inequalities).",
          "Lesson {22} (regions for several inequalities) and linear programming in Form Five."),
     ("Boundary and side",
      "The inequality y ≤ {mono(2, 'x')} + {1} is true for the points on the line y = {mono(2, 'x')} + {1} and for every point on one side of it.\n"
      "• Boundary: draw the line. With ≤ or ≥ it is included, so draw it solid. With < or > draw it broken.\n"
      "• Side: test a point that is not on the line. O({0}, {0}): {0} ≤ {mono(2, 'x')} + {1} becomes {0} ≤ {1}, true. So O's side is wanted.\n"
      "• Shade the unwanted side. The clear region shows all the solutions."),
     ("Vertical and horizontal boundaries",
      "x ≥ {3}: the boundary is the vertical line x = {3}; the wanted region is to the right of it.\n"
      "y < {-1}: the boundary is the horizontal line y = {-1}, broken; the wanted region is below it.\n"
      "If the line passes through O, test another point such as ({1}, {0}).\n"
      "Some books shade the wanted region instead. Always say which convention you use; here the shaded part is unwanted.")],
    key_words=[("half plane", "all the points on one side of a line"),
               ("boundary", "the line that separates the two sides"),
               ("unwanted region", "the part shaded because it does not satisfy the inequality")],
    examples=["x + y < {4}: broken line x + y = {4}; O is wanted", "y ≥ {-2}: solid horizontal line; wanted above"],
    mistake=("y < x + {2}: draw the line solid", "y < x + {2}: draw the line broken",
             "< leaves out the equals case, so the points on the line are not solutions.")))

# ---------------------------------------------------------------- 22. Simultaneous linear inequalities: regions
# R: x ≥ 0, y ≥ 0, a·x + b·y ≤ n (and optionally y ≤ x + d)
REG = {"a": {"int": [1, 2]}, "b": {"int": [1, 2]}, "n": {"int": [4, 8]}}
CONS = "[[1, 0, 0, '≥'], [0, 1, 0, '≥'], [a, b, n, '≤']]"
REGFIG = "graphFig([-1, 8], [-1, 8], [[1, 0, 0, false, ''], [0, 1, 0, false, ''], [a, b, n, false, '']], [[-1, 0, 0], [0, -1, 0], [a, b, n]], [], [['R', n / (3 * a), n / (3 * b), false]])"

L.lesson(D, S, 22, ("m4-22", "Find the region that satisfies several linear inequalities"), [21],
  "For several inequalities at once, draw each boundary and shade the unwanted side of each. "
  "The region left clear satisfies all of them; it is often labelled R.\n"
  "Example: x ≥ 0, y ≥ 0, x + y ≤ 4. The clear region is the triangle with corners (0, 0), (4, 0), (0, 4).\n"
  "A point is in R only if it satisfies every inequality.\n"
  "To find the whole-number points in R, check each grid point inside or on the boundary (if the boundary is included).\n"
  "The greatest value of an expression such as 2x + y over R is found at a corner of R.",
  worked({"a": 1, "b": 1, "n": 4},
         "Show the region R given by x ≥ {0}, y ≥ {0} and {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}, and count the whole-number points in R.",
         ["x ≥ {0}: shade the left of the y-axis. y ≥ {0}: shade below the x-axis.",
          "Boundary {mono(a, 'x')} + {mono(b, 'y')} = {n} through ({n}, {0}) and ({0}, {n}), solid; O satisfies it, so shade the side away from O.",
          "R is the clear triangle. Count the grid points in it, edges included: {n + 1} + {n} + … + {1}."],
         "{latticeCount([[1, 0, 0, '≥'], [0, 1, 0, '≥'], [a, b, n, '≤']], [0, 8], [0, 8])} points",
         figure="graphFig([-1, 6], [-1, 6], [[1, 0, 0, false, ''], [0, 1, 0, false, ''], [a, b, n, false, '']], [[-1, 0, 0], [0, -1, 0], [a, b, n]], [], [['R', n / (3 * a), n / (3 * b), false]])",
         checks=["latticeCount([[1, 0, 0, '≥'], [0, 1, 0, '≥'], [a, b, n, '≤']], [0, 8], [0, 8]) == 15"]),
  [card("c4m22-1", "R is the clear region left when the unwanted side of every boundary is shaded.",
        ["x ≥ {0}, y ≥ {0}, x + y ≤ {4}: R is the triangle ({0}, {0}), ({4}, {0}), ({0}, {4})"], "m4-22-in"),
   card("c4m22-2", "A point is in R only if it satisfies every inequality.",
        ["({1}, {2}): {1} ≥ {0}, {2} ≥ {0}, {1} + {2} ≤ {4}: in R. ({3}, {2}): {3} + {2} > {4}: not in R"], "m4-22-count"),
   card("c4m22-3", "The greatest value of an expression like {mono(2, 'x')} + y over R is at a corner of R.",
        ["corners ({0}, {0}), ({4}, {0}), ({0}, {4}): {mono(2, 'x')} + y = {0}, {8}, {4}; greatest {8}"], "m4-22-max")],
  [mcq("m4-22-in", 1, "R is the region where x ≥ {0}, y ≥ {0} and {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}. Which point is in R?",
       "({px}, {py})",
       [("({qx}, {qy})", "big"), ("({-1}, {py})", "neg"), ("({px}, {-1})", "negy")],
       ["Check each inequality for ({px}, {py}): {px} ≥ {0}, {py} ≥ {0}, {a * px + b * py} ≤ {n}.", "All three hold, so the answer is {answer}."],
       vars={**REG, "px": {"int": [0, 3]}, "py": {"int": [0, 3]}, "qx": {"int": [1, 6]}, "qy": {"int": [1, 6]}},
       misc=[("big", "{mono(a, 'x')} + {mono(b, 'y')} = {a * qx + b * qy}, which is more than {n}."),
             ("neg", "x = {-1} breaks x ≥ {0}."), ("negy", "y = {-1} breaks y ≥ {0}.")],
       sources=SRC, figure=REGFIG, where=["a * px + b * py <= n", "a * qx + b * qy > n", "qx != px || qy != py"]),
   num("m4-22-count", 1, "The unshaded region R satisfies x ≥ {0}, y ≥ {0} and {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}. How many points with whole-number coordinates are in R (edges included)?",
       f"latticeCount({CONS}, [0, 8], [0, 8])",
       ["Go along each row: for y = {0}, x can be {0} up to {floor(n / a)}; then y = {1}, and so on.",
        "Check each point with {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}.", "There are {answer} points."],
       vars=REG, figure=REGFIG,
       misc=[("strict", f"latticeCount([[1, 0, 0, '>'], [0, 1, 0, '>'], [a, b, n, '<']], [0, 8], [0, 8])", "The edges are solid lines: points on them are in R."),
             ("noaxes", f"latticeCount([[1, 0, 1, '≥'], [0, 1, 1, '≥'], [a, b, n, '≤']], [0, 8], [0, 8])", "x ≥ {0} and y ≥ {0} include the axes: count the points on them too.")],
       sources=SRC),
   mcq("m4-22-which", 2, "Which three inequalities define the unshaded region R in the graph?",
       "x ≥ {0}, y ≥ {0}, {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}",
       [("x ≥ {0}, y ≥ {0}, {mono(a, 'x')} + {mono(b, 'y')} ≥ {n}", "side"), ("x ≤ {0}, y ≤ {0}, {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}", "axes"),
        ("x ≥ {0}, y ≥ {0}, {mono(b, 'x')} + {mono(a, 'y')} ≤ {n}", "swap")],
       ["R is to the right of the y-axis (x ≥ {0}) and above the x-axis (y ≥ {0}).",
        "The slanted line meets the axes at ({n / a}, {0}) and ({0}, {n / b}): it is {mono(a, 'x')} + {mono(b, 'y')} = {n}, and R is on O's side.", "So the answer is: {answer}."],
       vars={"a": {"int": [1, 2]}, "b": {"int": [1, 2]}, "n": {"pick": [4, 6, 8]}}, figure=REGFIG,
       misc=[("side", "R contains points near O, and O gives {0} ≤ {n}: the sign is ≤."),
             ("axes", "R lies to the right of the y-axis and above the x-axis: x ≥ {0}, y ≥ {0}."),
             ("swap", "Check the intercepts: the line meets the x-axis at x = {n / a}, so the x coefficient is {a}.")],
       sources=SRC, where=["a != b"]),
   num("m4-22-max", 2, "R is given by x ≥ {0}, y ≥ {0} and {mono(a, 'x')} + {mono(b, 'y')} ≤ {n}. Find the greatest value of {mono(p, 'x')} + {mono(q, 'y')} for points (x, y) in R with whole-number coordinates.",
       f"latticeMax({CONS}, [0, 8], [0, 8], p, q)",
       ["The greatest value is at a corner of R: ({0}, {0}), ({floor(n / a)}, {0}) or ({0}, {floor(n / b)}) (or a whole-number point next to the slanted edge).",
        "Work out {mono(p, 'x')} + {mono(q, 'y')} at each and compare.", "The greatest value is {answer}."],
       vars={**REG, "p": {"int": [1, 4]}, "q": {"int": [1, 4]}}, figure=REGFIG,
       misc=[("origin", "0", "({0}, {0}) gives the smallest value, not the greatest."),
             ("sum", "n", "{n} is the limit for {mono(a, 'x')} + {mono(b, 'y')}, not the value of {mono(p, 'x')} + {mono(q, 'y')}.")],
       sources=SRC, where=["p != q", f"latticeMax({CONS}, [0, 8], [0, 8], p, q) != n"]),
   mcq("m4-22-word", 3, "A trader in Kumba buys x bags of rice and y bags of beans. She buys at least {r} bags of rice, at least {s} bags of beans, and at most {t} bags in all. Which inequalities describe this?",
       "x ≥ {r}, y ≥ {s}, x + y ≤ {t}",
       [("x ≤ {r}, y ≤ {s}, x + y ≤ {t}", "least"), ("x ≥ {r}, y ≥ {s}, x + y ≥ {t}", "most"), ("x ≥ {s}, y ≥ {r}, x + y ≤ {t}", "swap")],
       ["'At least {r}' means {r} or more: x ≥ {r}. Likewise y ≥ {s}.", "'At most {t} in all' means x + y ≤ {t}.", "So the answer is: {answer}."],
       vars={"r": {"int": [1, 5]}, "s": {"int": [1, 5]}, "t": {"int": [10, 20]}},
       misc=[("least", "'At least' means 'this many or more': ≥."), ("most", "'At most' means 'this many or fewer': ≤."),
             ("swap", "x counts rice (at least {r}) and y counts beans (at least {s}).")],
       sources=SRC, where=["r != s"])],
  learn=learn(
    [goal("find and describe the region R that satisfies several inequalities, count its whole-number points and find the greatest value of an expression in it.",
          "Lesson {21} (one inequality as a half plane).",
          "linear programming (best buys, greatest profit) in Form Five."),
     ("Several boundaries",
      "Show x ≥ {0}, y ≥ {0}, x + y ≤ {4}.\n"
      "• x ≥ {0}: boundary the y-axis; shade the left side.\n• y ≥ {0}: boundary the x-axis; shade below.\n"
      "• x + y ≤ {4}: draw the solid line through ({4}, {0}) and ({0}, {4}); O gives {0} ≤ {4}, true, so shade the far side.\n"
      "What stays clear is the triangle with corners ({0}, {0}), ({4}, {0}), ({0}, {4}). Label it R.\n"
      "A point is in R only if it passes every test."),
     ("Points in R and best values",
      "Count whole-number points row by row. For the triangle above: y = {0} gives {5} points, y = {1} gives {4}, … y = {4} gives {1}: {15} in all.\n"
      "In a real problem, x and y are often numbers of items, so only whole-number points count.\n"
      "To find the greatest value of {mono(2, 'x')} + y in R, try the corners: ({0}, {0}) gives {0}, ({4}, {0}) gives {8}, ({0}, {4}) gives {4}. The greatest is {8}.\n"
      "Words: 'at least' means ≥, 'at most' and 'not more than' mean ≤.")],
    key_words=[("region R", "the set of points that satisfy all the inequalities"),
               ("vertex (corner)", "a point where two boundaries meet"),
               ("at least / at most", "≥ / ≤")],
    examples=["x ≥ {1}, y ≥ {1}, x + y ≤ {5}: corners ({1}, {1}), ({4}, {1}), ({1}, {4})", "at most {20} pupils: x ≤ {20}"],
    mistake=("'at least {3} bags' → x ≤ {3}", "'at least {3} bags' → x ≥ {3}",
             "At least {3} means {3} or more.")))

# ---------------------------------------------------------------- 23. Graphs of quadratic functions
QFIG = "graphFig([h - 4, h + 4], [-8, 8], [], [], [[s, -2 * s * h, s * h * h + v, '']], [])"

L.lesson(D, S, 23, ("m4-23", "Study the graph of a quadratic function y = ax² + bx + c"), [20, 8],
  "The graph of y = ax² + bx + c is a parabola.\n"
  "• If a > 0 it is ∪-shaped and has a lowest point (minimum). If a < 0 it is ∩-shaped with a highest point (maximum).\n"
  "• It crosses the y-axis at (0, c).\n"
  "• It is symmetrical about the vertical line x = −b/2a, the axis of symmetry. The turning point is on this line.\n"
  "• Completing the square gives the turning point: y = (x − h)² + k turns at (h, k).\n"
  "To draw it: make a table of values, plot the points and join them with a smooth curve, not with straight lines.",
  worked({"b": -2, "c": -3},
         "For y = {quad(1, b, c)}, find the y-intercept, the axis of symmetry and the turning point.",
         ["y-intercept: put x = {0}: y = {c}, so ({0}, {c}).",
          "Axis of symmetry: x = −b/{2}a = {-b} ÷ {2} = {-b / 2}.",
          "Turning point: y at x = {-b / 2} is {(-b / 2) * (-b / 2) + b * (-b / 2) + c}. a = {1} > {0}, so it is a minimum."],
         "y-intercept ({0}, {c}); axis x = {-b / 2}; minimum ({-b / 2}, {(-b / 2) * (-b / 2) + b * (-b / 2) + c})",
         figure="graphFig([-3, 5], [-5, 7], [], [], [[1, b, c, '']], [['T', -b / 2, (-b / 2) * (-b / 2) + b * (-b / 2) + c]])",
         checks=["-b / 2 == 1", "(-b / 2) * (-b / 2) + b * (-b / 2) + c == -4"]),
  [card("c4m23-1", "The y-intercept of y = ax² + bx + c is c: put x = {0}.",
        ["y = {quad(1, -2, -3)} meets the y-axis at ({0}, {-3})"], "m4-23-icept"),
   card("c4m23-2", "The axis of symmetry is x = −b/{2}a; the turning point lies on it.",
        ["y = {quad(1, -2, -3)}: x = {2}/{2} = {1}; turning point ({1}, {-4})"], "m4-23-axis"),
   card("c4m23-3", "a > {0}: ∪ shape with a minimum. a < {0}: ∩ shape with a maximum.",
        ["y = {quad(-1, 4, 0)} is ∩-shaped: it has a maximum"], "m4-23-turn")],
  [num("m4-23-icept", 1, "Where does y = {quad(a, b, c)} cross the y-axis? Give the y-coordinate.",
       "c",
       ["On the y-axis x = {0}.", "y = {a} × {0} + {b} × {0} + {br(c)} = {answer}."],
       vars={"a": {"pick": [-2, -1, 1, 2, 3]}, "b": {"int": [-6, 6]}, "c": {"int": [-9, 9]}},
       misc=[("a", "a", "Put x = {0}: the x² and x terms vanish, leaving c = {c}."),
             ("b", "b", "Put x = {0}: only the number term c = {c} is left.")],
       sources=SRC, where=["b != 0 && c != 0", "a != c && b != c"], signed=True),
   num("m4-23-table", 1, "Complete the table of values for y = {quad(a, b, c)}. What is y when x = {t}?",
       "a * t * t + b * t + c",
       ["x² = ({t})² = {t * t}, so {a} × {t * t} = {a * t * t}.", "{b} × {br(t)} = {b * t}.", "y = {a * t * t} + {br(b * t)} + {br(c)} = {answer}."],
       vars={"a": {"pick": [-2, -1, 1, 2]}, "b": {"int": [-5, 5]}, "c": {"int": [-6, 6]}, "t": {"int": [-3, 3]}},
       misc=[("negsq", "-a * t * t + b * t + c", "({t})² = {t * t} is positive: squaring a negative number gives a positive one.", "t < 0"),
             ("double", "2 * a * t + b * t + c", "x² means x × x = {t * t}, not {2} × {br(t)}.")],
       sources=SRC, where=["t != 0 && t != 1 && t != 2", "b != 0 && c != 0"], signed=True),
   num("m4-23-axis", 2, "What is the equation of the axis of symmetry of y = {quad(a, -2 * a * h, a * h * h + v)}? Give x = ? as a number.",
       "h",
       ["x = −b/{2}a = −({-2 * a * h}) ÷ ({2} × {br(a)}).", "= {2 * a * h} ÷ {2 * a} = {answer}."],
       vars={"a": {"pick": [-2, -1, 1, 2]}, "h": {"int": [-4, 4]}, "v": {"int": [-6, 6]}},
       misc=[("sign", "-h", "x = −b/{2}a: the minus sign changes the sign of b = {-2 * a * h}."),
             ("nohalf", "2 * h", "Divide by {2}a = {2 * a}, not by a.")],
       sources=SRC, where=["h != 0", "-2 * a * h != 0"], signed=True),
   mcq("m4-23-turn", 2, "What is the turning point of y = {quad(s, -2 * s * h, s * h * h + v)}, and is it a maximum or a minimum?",
       "({h}, {v}), {s > 0 ? 'minimum' : 'maximum'}",
       [("({h}, {v}), {s > 0 ? 'maximum' : 'minimum'}", "kind"), ("({-h}, {v}), {s > 0 ? 'minimum' : 'maximum'}", "sign"), ("({h}, {s * h * h + v}), {s > 0 ? 'minimum' : 'maximum'}", "c")],
       ["Axis of symmetry: x = −b/{2}a = {h}.", "y at x = {h}: {s * h * h} + {br(-2 * s * h * h)} + {br(s * h * h + v)} = {v}.",
        "a = {s} is {s > 0 ? 'positive: ∪ shape, minimum' : 'negative: ∩ shape, maximum'}.", "So the answer is {answer}."],
       vars={"s": {"pick": [-1, 1]}, "h": {"int": [-3, 3]}, "v": {"int": [-6, 6]}}, figure=QFIG,
       misc=[("kind", "a = {s} is {s > 0 ? 'positive, so the curve opens upwards: a minimum' : 'negative, so the curve opens downwards: a maximum'}."),
             ("sign", "x = −b/{2}a = {h}, not {-h}."),
             ("c", "The turning point is not the y-intercept. Put x = {h} into the equation.")],
       sources=SRC, where=["h != 0", "s * h * h + v != v"]),
   mcq("m4-23-match", 3, "Which equation could the graph show?",
       "y = {quad(s, -2 * s * h, s * h * h + v)}",
       [("y = {quad(-s, 2 * s * h, -s * h * h + v)}", "shape"), ("y = {quad(s, 2 * s * h, s * h * h + v)}", "axis"), ("y = {quad(s, -2 * s * h, s * h * h - v)}", "height")],
       ["The curve is {s > 0 ? '∪-shaped, so a > 0' : '∩-shaped, so a < 0'}.",
        "It turns at x = {h} and y = {v}; y = {quad(s, -2 * s * h, s * h * h + v)} = {s > 0 ? '' : '−'}(x − {br(h)})² + {br(v)} fits.", "So the answer is {answer}."],
       vars={"s": {"pick": [-1, 1]}, "h": {"int": [-3, 3]}, "v": {"int": [-5, 5]}}, figure=QFIG,
       misc=[("shape", "That parabola opens the other way: the sign of a decides ∪ or ∩."),
             ("axis", "That parabola turns at x = {-h}, the mirror image."),
             ("height", "That parabola turns at y = {-v}, not {v}.")],
       sources=SRC, where=["h != 0", "v != 0"])],
  learn=learn(
    [goal("describe the parabola y = ax² + bx + c: its shape, y-intercept, axis of symmetry and turning point, and draw it from a table.",
          "Lesson {8} (completing the square) and Lesson {20} (drawing graphs from tables).",
          "Lessons {24} and {25} (the discriminant and solving quadratics with graphs)."),
     ("The shape of a parabola",
      "Plot y = {quad(1, -2, -3)} from a table:\n"
      "x: {-2}, {-1}, {0}, {1}, {2}, {3}, {4}\ny: {5}, {0}, {-3}, {-4}, {-3}, {0}, {5}\n"
      "Joined with a smooth curve, the points make a ∪ shape. The y values repeat on each side of x = {1}: the curve is symmetrical about the line x = {1}.\n"
      "The lowest point ({1}, {-4}) is the turning point. When a is negative, the curve is ∩-shaped and the turning point is a maximum."),
     ("Reading the features",
      "For y = ax² + bx + c:\n"
      "• y-intercept: ({0}, c).\n• axis of symmetry: x = −b/{2}a.\n• turning point: put that x into the equation.\n"
      "For y = {quad(1, -2, -3)}: c = {-3}; x = {2}/{2} = {1}; y = {1} − {2} − {3} = {-4}. So the minimum is ({1}, {-4}).\n"
      "Completing the square gives the same answer: {quad(1, -2, -3)} = (x − {1})² − {4}.")],
    key_words=[("parabola", "the curve of a quadratic function"),
               ("turning point (vertex)", "the lowest or highest point of the parabola"),
               ("axis of symmetry", "the vertical line through the turning point"),
               ("minimum / maximum", "smallest / greatest value of y")],
    examples=["y = {quad(1, 0, -4)}: minimum ({0}, {-4}), axis x = {0}", "y = {quad(-1, 6, -5)}: maximum ({3}, {4}), axis x = {3}"],
    mistake=("y = {quad(1, -2, -3)}: axis x = {-1}", "axis x = {1}",
             "x = −b/{2}a with b = {-2}: −({-2})/{2} = {1}. The minus sign in the formula matters.")))

# ---------------------------------------------------------------- 24. The discriminant and the nature of roots
L.lesson(D, S, 24, ("m4-24", "Use the discriminant to decide the nature of the roots"), [9, 23],
  "For ax² + bx + c = 0 the discriminant is D = b² − 4ac.\n"
  "• D > 0: two different real roots; the parabola crosses the x-axis twice.\n"
  "• D = 0: one repeated (equal) root; the parabola touches the x-axis at its turning point.\n"
  "• D < 0: no real roots; the parabola does not meet the x-axis.\n"
  "If D is a perfect square, the roots are rational and the quadratic factorises.\n"
  "Unknown coefficients: equal roots means D = 0; real roots means D ≥ 0.",
  worked({"m": 3},
         "Find the positive value of k for which x² + kx + {m * m} = {0} has equal roots.",
         ["Equal roots means D = {0}: a = {1}, b = k, c = {m * m}.", "k² − {4} × {1} × {m * m} = {0}, so k² = {4 * m * m}.",
          "k = {2 * m} or k = {-2 * m}. Check: x² + {mono(2 * m, 'x')} + {m * m} = (x + {m})², one repeated root."],
         "k = {2 * m}",
         checks=["(2 * m) * (2 * m) - 4 * m * m == 0"]),
  [card("c4m24-1", "The sign of D = b² − {4}ac decides how many real roots there are.",
        ["D > {0}: two; D = {0}: one (equal); D < {0}: none"], "m4-24-nature"),
   card("c4m24-2", "On the graph: D > {0} crosses the x-axis twice, D = {0} touches it, D < {0} misses it.",
        ["y = {quad(1, 0, 4)}: D = {-16} < {0}, the curve stays above the x-axis"], "m4-24-graph"),
   card("c4m24-3", "Equal roots: set D = {0} and solve for the unknown.",
        ["x² + kx + {9} = {0} has equal roots when k² = {36}: k = {6} or {-6}"], "m4-24-equal")],
  [mcq("m4-24-nature", 1, "Describe the roots of {quad(a, b, c)} = {0}.",
       "{b * b - 4 * a * c > 0 ? 'Two different real roots' : b * b - 4 * a * c == 0 ? 'Two equal real roots (one repeated root)' : 'No real roots'}",
       [("{b * b - 4 * a * c > 0 ? 'No real roots' : 'Two different real roots'}", "w1"),
        ("{b * b - 4 * a * c == 0 ? 'No real roots' : 'Two equal real roots (one repeated root)'}", "w2"),
        ("Three real roots", "three")],
       ["D = b² − {4}ac = {b * b} − {4 * a * c} = {b * b - 4 * a * c}.", "So the answer is: {answer}."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [-8, 8]}, "c": {"int": [-6, 6]}},
       misc=[("w1", "Work out D = {b * b - 4 * a * c} and look at its sign."), ("w2", "D = {b * b - 4 * a * c}: equal roots need D = {0} exactly."),
             ("three", "A quadratic has at most two roots.")],
       sources=SRC, where=["c != 0", "b * b - 4 * a * c != 0 || b != 0"]),
   mcq("m4-24-graph", 1, "How many times does the graph of y = {quad(a, b, c)} meet the x-axis?",
       "{b * b - 4 * a * c > 0 ? 'Twice' : b * b - 4 * a * c == 0 ? 'Once (it touches the axis)' : 'Never'}",
       [("{b * b - 4 * a * c > 0 ? 'Never' : 'Twice'}", "w1"), ("{b * b - 4 * a * c == 0 ? 'Twice' : 'Once (it touches the axis)'}", "w2"), ("Three times", "three")],
       ["D = {b * b - 4 * a * c}.", "The number of crossings is the number of real roots of {quad(a, b, c)} = {0}.", "So the answer is: {answer}."],
       vars={"a": {"pick": [1, 2]}, "h": {"int": [-3, 3]}, "z": {"pick": [-1, 0, 1]}, "b": {"expr": "-2 * a * h"}, "c": {"expr": "a * h * h + z * (abs(h) + 1)"}},
       misc=[("w1", "Look at the sign of D = {b * b - 4 * a * c}."), ("w2", "Touching needs D = {0}; here D = {b * b - 4 * a * c}."),
             ("three", "A parabola meets a straight line at most twice.")],
       figure="graphFig([h - 4, h + 4], [-6, 8], [], [], [[a, b, c, '']], [])", sources=SRC),
   num("m4-24-equal", 2, "Find the positive value of k for which x² + kx + {m * m} = {0} has equal roots.",
       "2 * m",
       ["Equal roots: D = k² − {4} × {1} × {m * m} = {0}.", "k² = {4 * m * m}, so k = ±{2 * m}.", "The positive value is {answer}."],
       vars={"m": {"int": [1, 9]}},
       misc=[("sq", "m", "k² = {4} × {m * m} = {4 * m * m}, so k = {2 * m}, not {m}."),
             ("four", "4 * m * m", "That is k². Take the square root: k = {2 * m}.")],
       sources=SRC, where=["m != 2"]),
   mcq("m4-24-real", 2, "For which values of k does x² + {mono(2 * h, 'x')} + k = {0} have real roots?",
       "k ≤ {h * h}",
       [("k ≥ {h * h}", "sign"), ("k < {h * h}", "strict"), ("k ≤ {2 * h}", "nosq")],
       ["Real roots: D ≥ {0}.", "D = ({2 * h})² − {4}k = {4 * h * h} − {4}k ≥ {0}.", "So {4}k ≤ {4 * h * h}: k ≤ {h * h}."],
       vars={"h": {"int": [-6, 6]}},
       misc=[("sign", "D = {4 * h * h} − {4}k ≥ {0} gives k ≤ {h * h}: larger k makes D negative."),
             ("strict", "Equal roots (D = {0}) are real too, so k = {h * h} is allowed."),
             ("nosq", "Square the coefficient of x: ({2 * h})² = {4 * h * h}.")],
       sources=SRC, where=["h != 0 && h != 2 && h != -2", "h * h != 2 * h"]),
   num("m4-24-kx", 3, "Find k if kx² + {mono(b, 'x')} + {1} = {0} has equal roots.",
       "b * b / 4",
       ["Equal roots: D = {0}.", "D = {b * b} − {4} × k × {1} = {0}.", "So k = {b * b} ÷ {4} = {answer}."],
       vars={"b": {"pick": [-10, -8, -6, -4, 4, 6, 8, 10]}},
       misc=[("b", "abs(b) / 2", "D = b² − {4}ac with a = k: {b * b} − {4}k = {0}, so k = {b * b / 4}."),
             ("four", "b * b", "Divide by {4}: {4}k = {b * b}.")],
       sources=SRC)],
  learn=learn(
    [goal("use D = b² − {4}ac to say whether a quadratic equation has two, one or no real roots, and find unknown coefficients from that.",
          "Lesson {9} (the quadratic formula) and Lesson {23} (parabolas).",
          "Lesson {25} (solving with graphs) and, in Form Five, intersections of lines and curves."),
     ("Why the discriminant decides",
      "In x = (−b ± √D)/{2}a, the number D = b² − {4}ac sits under the square root.\n"
      "• D positive: √D is a real number, and ± gives two different roots.\n"
      "• D = {0}: ±{0} changes nothing: one repeated root.\n"
      "• D negative: there is no real square root: no real roots.\n"
      "On the graph of y = ax² + bx + c these are: crosses the x-axis twice, touches it, misses it.\n"
      "Example: {quad(1, -6, 9)}: D = {36} − {36} = {0}, one root x = {3}."),
     ("Finding unknowns",
      "• Equal roots: x² + kx + {9} = {0}: D = k² − {36} = {0}, so k = {6} or {-6}.\n"
      "• Real roots: x² + {mono(4, 'x')} + k = {0}: D = {16} − {4}k ≥ {0}, so k ≤ {4}.\n"
      "• No real roots: use D < {0}.\n"
      "When D is a perfect square ({1}, {4}, {9}, …), the roots are rational and the quadratic factorises.")],
    key_words=[("discriminant (D)", "b² − {4}ac"), ("real roots", "roots that are ordinary numbers"),
               ("equal (repeated) roots", "both roots the same; D = {0}")],
    examples=["{quad(1, 1, -6)}: D = {25} > {0}, two roots", "{quad(1, 2, 5)}: D = {-16} < {0}, no real roots"],
    mistake=("D = {0} means no roots", "D = {0} means one repeated root",
             "√{0} = {0}, so the formula gives x = −b/{2}a: one root, counted twice.")))

# ---------------------------------------------------------------- 25. Graphical solution of quadratic equations
GFIG = "graphFig([-5, 6], [-9, 9], [], [], [[1, -(p + q), p * q, '']], [])"
GV = {"p": {"int": [-4, 0]}, "w": {"int": [2, 6]}, "q": {"expr": "p + w"}}

L.lesson(D, S, 25, ("m4-25", "Solve quadratic equations using graphs"), [23, 20],
  "On the graph of y = ax² + bx + c, the roots of ax² + bx + c = 0 are the x-coordinates where the curve crosses the x-axis (y = 0).\n"
  "To solve ax² + bx + c = k with the same graph, draw the horizontal line y = k and read the x-coordinates where it meets the curve.\n"
  "To solve a different quadratic, rearrange it as (the graphed expression) = (a straight line), draw that line, and read the crossings.\n"
  "Example: with y = x² − 2x − 3 drawn, x² − 3x − 1 = 0 becomes x² − 2x − 3 = x − 2: draw y = x − 2.\n"
  "Graph readings are approximate; give them to the nearest grid line or as the question asks.",
  worked({"p": -1, "q": 3, "k": 5},
         "The graph of y = {quad(1, -(p + q), p * q)} is drawn. Use it to solve {quad(1, -(p + q), p * q)} = {k}.",
         ["Draw the horizontal line y = {k}.",
          "Read the x-coordinates where it meets the curve: x = {-2} and x = {4}.",
          "Check x = {4}: {16} − {8} − {3} = {5}. Correct."],
         "x = {-2} or x = {4}",
         figure="graphFig([-3, 5], [-5, 7], [[0, 1, k, false, 'y = ' + k]], [], [[1, -(p + q), p * q, '']], [])",
         checks=["16 - 2 * 4 - 3 == k", "4 + 4 - 3 == k"]),
  [card("c4m25-1", "The roots of ax² + bx + c = {0} are where the graph crosses the x-axis.",
        ["y = {quad(1, -2, -3)} crosses at x = {-1} and x = {3}"], "m4-25-roots"),
   card("c4m25-2", "To solve ax² + bx + c = k, draw the line y = k and read where it meets the curve.",
        ["{quad(1, -2, -3)} = {5}: y = {5} meets the curve at x = {-2} and x = {4}"], "m4-25-k"),
   card("c4m25-3", "For another equation, rearrange it as (the graphed expression) = (a line), and draw the line.",
        ["x² − {mono(3, 'x')} − {1} = {0} ↔ {quad(1, -2, -3)} = x − {2}: draw y = x − {2}"], "m4-25-line")],
  [mcq("m4-25-roots", 1, "The graph shows y = {quad(1, -(p + q), p * q)}. What are the roots of {quad(1, -(p + q), p * q)} = {0}?",
       "x = {p} or x = {q}",
       [("x = {-p} or x = {-q}", "sign"), ("x = {p * q}", "icept"), ("x = {(p + q) / 2}", "axis")],
       ["The roots are where the curve crosses the x-axis.", "It crosses at x = {p} and x = {q}.", "So the answer is {answer}."],
       vars=GV, figure=GFIG,
       misc=[("sign", "Read the crossings off the x-axis: they are at {p} and {q}."),
             ("icept", "{p * q} is where the curve meets the y-axis, not the x-axis."),
             ("axis", "That is the axis of symmetry, halfway between the roots.")],
       sources=SRC, where=["p != 0", "(p + q) % 2 == 0", "p != -q"]),
   num("m4-25-large", 1, "The graph shows y = {quad(1, -(p + q), p * q)}. Use it to find the larger root of {quad(1, -(p + q), p * q)} = {0}.",
       "q",
       ["Look for where the curve crosses the x-axis.", "The crossings are at x = {p} and x = {q}.", "The larger root is {answer}."],
       vars=GV, figure=GFIG,
       misc=[("small", "p", "That is the smaller root."), ("icept", "p * q", "{p * q} is the y-intercept. The roots are on the x-axis.")],
       sources=SRC, where=["p != 0", "q != -p * q"], signed=True),
   mcq("m4-25-k", 2, "The graph of y = {quad(1, -(p + q), p * q)} is drawn. Which line do you draw to solve {quad(1, -(p + q), p * q)} = {k}?",
       "y = {k}",
       [("y = {-k}", "sign"), ("x = {k}", "vert"), ("y = x + {k}", "slant")],
       ["The left side is the graphed expression y. So y = {k}.", "Draw the horizontal line y = {k} and read where it meets the curve.", "So the answer is {answer}."],
       vars={**GV, "k": {"int": [-3, 6]}}, figure=GFIG,
       misc=[("sign", "The equation says the expression equals {k}: draw y = {k}."),
             ("vert", "x = {k} is a vertical line: it gives only one point on the curve, not the solutions."),
             ("slant", "The right side is just the number {k}, so the line is horizontal.")],
       sources=SRC, where=["p != 0", "k != 0"]),
   num("m4-25-solvek", 2, "The graph of y = {quad(1, -(p + q), p * q)} is drawn. Draw y = {t * t - (p + q) * t + p * q} and use it to solve {quad(1, -(p + q), p * q)} = {t * t - (p + q) * t + p * q}. Give the larger solution.",
       "max(t, p + q - t)",
       ["The line y = {t * t - (p + q) * t + p * q} meets the curve at x = {t} and x = {p + q - t} (symmetric about x = {(p + q) / 2}).",
        "Check x = {t}: {t * t} − {(p + q) * t} + {br(p * q)} = {t * t - (p + q) * t + p * q}.", "The larger solution is {answer}."],
       vars={**GV, "t": {"int": [-3, 5]}},
       figure="graphFig([-5, 6], [-9, 9], [[0, 1, t * t - (p + q) * t + p * q, false, '']], [], [[1, -(p + q), p * q, '']], [])",
       misc=[("small", "min(t, p + q - t)", "That is the smaller solution."), ("roots", "q", "{q} is a root of the curve = {0}. Here the curve equals {t * t - (p + q) * t + p * q}.")],
       sources=SRC, where=["p != 0", "t != p && t != q", "t != p + q - t", "abs(t * t - (p + q) * t + p * q) <= 8"], signed=True),
   mcq("m4-25-line", 3, "The graph of y = {quad(1, b, c)} is drawn. Which straight line must you draw to solve {quad(1, b2, c2)} = {0}?",
       "y = {poly([b - b2, 'x'], [c - c2, ''])}",
       [("y = {poly([b2 - b, 'x'], [c2 - c, ''])}", "sign"), ("y = {poly([b2, 'x'], [c2, ''])}", "whole"), ("y = {0}", "axis")],
       ["Rearrange so that the left side is the graphed expression: {quad(1, b2, c2)} = {0}.",
        "Add {poly([b - b2, 'x'], [c - c2, ''])} to both sides: {quad(1, b, c)} = {poly([b - b2, 'x'], [c - c2, ''])}.",
        "So draw y = {poly([b - b2, 'x'], [c - c2, ''])}."],
       vars={"b": {"int": [-4, 4]}, "c": {"int": [-6, 6]}, "b2": {"int": [-4, 4]}, "c2": {"int": [-6, 6]}},
       misc=[("sign", "Move the terms the right way: x² + {mono(b, 'x')} + {c} − ({poly([b - b2, 'x'], [c - c2, ''])}) must give {quad(1, b2, c2)}."),
             ("whole", "Subtract the two quadratics: the line is the difference, not the new x and number terms."),
             ("axis", "y = {0} solves {quad(1, b, c)} = {0}, a different equation.")],
       sources=SRC, where=["b != b2", "c != c2", "b - b2 != b2 - b"])],
  learn=learn(
    [goal("read the roots of a quadratic equation from its graph and solve related equations by drawing a straight line.",
          "Lesson {23} (drawing parabolas) and Lesson {20} (crossings of graphs).",
          "intersections of curves and lines in Form Five, and solving equations that algebra cannot."),
     ("Roots on the x-axis",
      "The graph of y = {quad(1, -2, -3)} crosses the x-axis at x = {-1} and x = {3}.\n"
      "On the x-axis y = {0}, so these x values make {quad(1, -2, -3)} = {0}: they are the roots.\n"
      "Check: ({-1})² − {2} × ({-1}) − {3} = {1} + {2} − {3} = {0}.\n"
      "If the curve crosses between grid lines, estimate: x ≈ {2.6}, for example."),
     ("Other equations with the same graph",
      "To solve {quad(1, -2, -3)} = {5}, draw the horizontal line y = {5}. It meets the curve at x = {-2} and x = {4}.\n"
      "To solve x² − {mono(3, 'x')} − {1} = {0}, make the left side match the graph:\n"
      "x² − {mono(3, 'x')} − {1} = {0} is the same as {quad(1, -2, -3)} = x − {2} (add x − {2} to both sides).\n"
      "So draw y = x − {2} and read the x values where it crosses the curve.")],
    key_words=[("graphical solution", "an answer read from a graph"),
               ("intersection", "where two graphs meet"),
               ("estimate", "read as closely as the grid allows")],
    examples=["y = {quad(1, 0, -4)}: roots x = {-2}, {2}", "{quad(1, 0, -4)} = {5}: draw y = {5}, x = {-3} or {3}"],
    mistake=("to solve {quad(1, -2, -3)} = {5}, read where the curve crosses the x-axis", "draw y = {5} and read where it meets the curve",
             "The x-axis is y = {0}. For = {5}, use the line y = {5}.")))
