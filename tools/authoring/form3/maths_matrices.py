"""Form 3 Maths, Term 1, rows 20-24 (matrices). Run: python tools/authoring/form3/maths_matrices.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import bank

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"
SRC = ["matrices"]

AB = {"a": {"int": [-5, 9]}, "b": {"int": [-5, 9]}, "c": {"int": [-5, 9]}, "d": {"int": [-5, 9]},
      "e": {"int": [-5, 9]}, "f": {"int": [-5, 9]}, "g": {"int": [-5, 9]}, "h": {"int": [-5, 9]},
      "A": {"expr": "[[a, b], [c, d]]"}, "B": {"expr": "[[e, f], [g, h]]"}}
FIG_A = "matFig([['A', A]])"
FIG_AB = "matFig([['A', A], ['B', B]])"
RC = {"r": {"int": [1, 2]}, "s": {"int": [1, 2]}}
POS = "row {r}, column {s}"

# ---------------------------------------------------------------- 20. Definition and types of matrices
L.lesson(D, S, 20, ("m3-20", "Matrices: order, elements and types"), [],
  "A matrix is a rectangular array of numbers in rows and columns, written in brackets.\n"
  "• Its order is (number of rows) × (number of columns): a matrix with 2 rows and 3 columns is 2 × 3.\n"
  "• Each number is an element; aᵢⱼ is the element in row i, column j.\n"
  "• Types: row matrix (one row), column matrix (one column), square matrix (rows = columns), zero matrix (all zeros), diagonal matrix (zeros off the leading diagonal), identity matrix I (ones on the leading diagonal, zeros elsewhere).\n"
  "• Two matrices are equal when they have the same order and equal corresponding elements.",
  worked({"M": [[2, -1, 5], [0, 4, 3]]},
         "For the matrix A in the figure, give its order and the element in row {2}, column {3}.",
         ["Count the rows: {len(M)}. Count the columns: {len(M[0])}.", "The order is {len(M)} × {len(M[0])}.",
          "Row {2}: {M[1][0]}, {M[1][1]}, {M[1][2]}. The third element is {M[1][2]}."],
         "Order {len(M)} × {len(M[0])}; a₂₃ = {M[1][2]}", checks=["M[1][2] == 3"], figure="matFig([['A', M]])"),
  [card("c3m20-1", "The order is rows × columns, rows first.",
        ["A matrix with {2} rows and {3} columns has order {2} × {3}."], "m3-20-order"),
   card("c3m20-2", "The element in row i, column j is written aᵢⱼ.",
        ["In {matStr([[4, 7], [1, 9]])}, the element in row {1}, column {2} is {7}."], "m3-20-elem"),
   card("c3m20-3", "A square matrix with ones on the leading diagonal and zeros elsewhere is the identity matrix I.",
        ["I = {matStr([[1, 0], [0, 1]])}"], "m3-20-type")],
  [mcq("m3-20-order", 1, "What is the order of matrix A?", "{len(M) + ' × ' + len(M[0])}",
       [("{len(M[0]) + ' × ' + len(M)}", "swap"), ("{str(len(M) * len(M[0]))}", "count"), ("{len(M) + ' × ' + len(M)}", "rows")],
       ["A has {len(M)} rows and {len(M[0])} columns.", "Order = rows × columns = {answer}."],
       vars={"M": {"pick": [[[2, -1, 5], [0, 4, 3]], [[7], [-2], [4]], [[1, 6, 0, 3]], [[3, 1], [5, -2], [0, 8]], [[9, 2, 4], [1, 0, 7], [6, 5, 2], [3, 3, 1]], [[4, 0, 1, 2], [5, 6, 7, 8]]]}},
       misc=[("swap", "Count the rows first ({len(M)}), then the columns ({len(M[0])})."), ("count", "{len(M) * len(M[0])} is the number of elements. The order is written rows × columns."),
             ("rows", "Count the columns too: there are {len(M[0])}.")],
       figure="matFig([['A', M]])", sources=SRC),
   num("m3-20-elem", 1, "What is the element in " + POS + " of A?", "A[r - 1][s - 1]",
       ["Row {r} of A: {A[r - 1][0]}, {A[r - 1][1]}.", "Column {s} of that row: {answer}."],
       vars={**AB, **RC}, misc=[("swap", "A[s - 1][r - 1]", "Rows go across and columns go down: row {r} first, then column {s}.")],
       figure=FIG_A, sources=SRC, where=["r != s", "A[s - 1][r - 1] != A[r - 1][s - 1]"], signed=True),
   bank("m3-20-type", 1, "What type of matrix is A?", [
     {"m": [[1, 0], [0, 1]], "r": "Identity matrix", "w": ["Zero matrix", "Row matrix", "Column matrix"],
      "e": ["A zero matrix has every element 0.", "A row matrix has only one row.", "A column matrix has only one column."], "y": "Ones on the leading diagonal, zeros elsewhere: the identity matrix I."},
     {"m": [[0, 0], [0, 0]], "r": "Zero matrix", "w": ["Identity matrix", "Diagonal matrix with ones", "Row matrix"],
      "e": ["The identity has ones on the leading diagonal.", "Every element here is zero.", "It has two rows."], "y": "Every element is 0: the zero (null) matrix."},
     {"m": [[5, -2, 7]], "r": "Row matrix", "w": ["Column matrix", "Square matrix", "Identity matrix"],
      "e": ["A column matrix has one column; this has one row.", "A square matrix has as many rows as columns: this is 1 × 3.", "The identity is square with ones on the diagonal."], "y": "One row: a row matrix (order 1 × 3)."},
     {"m": [[4], [0], [-3]], "r": "Column matrix", "w": ["Row matrix", "Square matrix", "Zero matrix"],
      "e": ["It has one column, not one row.", "It is 3 × 1, not square.", "Not every element is 0."], "y": "One column: a column matrix (order 3 × 1)."},
     {"m": [[3, 0], [0, -2]], "r": "Diagonal matrix", "w": ["Identity matrix", "Zero matrix", "Row matrix"],
      "e": ["The identity has ones on the diagonal; here they are 3 and −2.", "Not every element is 0.", "It has two rows."], "y": "Zeros everywhere except the leading diagonal: a diagonal matrix."}],
     SRC, figure="matFig([['A', X.m]])"),
   num("m3-20-equal", 2, "Matrices P and Q are equal. Find x.", "a - p",
       ["Equal matrices have equal corresponding elements.", "x + {p} = {a}, so x = {a} − {p} = {answer}."],
       vars={"a": {"int": [-5, 15]}, "p": {"int": [1, 9]}, "b": {"int": [-5, 9]}, "c": {"int": [-5, 9]}, "y": {"int": [-5, 9]}},
       misc=[("add", "a + p", "Subtract {p} from both sides: x = {a} − {p}.")],
       figure="matFig([['P', [['x + ' + p, b], [c, 'y']]], ['Q', [[a, b], [c, y]]]])", sources=SRC, signed=True),
   num("m3-20-count", 3, "A matrix has {m * n} elements arranged in {m} rows. How many columns does it have?", "n",
       ["Number of elements = rows × columns.", "{m * n} = {m} × columns, so there are {answer} columns. Its order is {m} × {n}."],
       vars={"m": {"int": [1, 5]}, "n": {"int": [1, 6]}},
       misc=[("rows", "m", "{m} is the number of rows. Divide the elements by the rows."), ("count", "m * n", "{m * n} is the number of elements.")],
       sources=SRC, where=["m != n", "m * n != n"])],
  learn=learn(
    [("What a matrix is",
      "A matrix is a table of numbers in rows and columns, written inside brackets. "
      "A shop in Limbe might record sales of bread and milk on Monday and Tuesday in a matrix: each row a day, each column a product.\n"
      "Rows go across (left to right). Columns go down (top to bottom).", "matFig([['S', [[12, 5], [9, 8]]]])"),
     ("Order and elements",
      "The order of a matrix is rows × columns, always rows first. A matrix with {2} rows and {3} columns has order {2} × {3} and {6} elements.\n"
      "Each number is an element. We name it by its row and column: a₁₂ is the element in row {1}, column {2}.\n"
      "In S above, s₂₁ = {9}: row {2} (Tuesday), column {1} (bread)."),
     ("Special matrices",
      "• Row matrix: one row, like {matStr([[3, 1, 4]])}.\n• Column matrix: one column.\n"
      "• Square matrix: as many rows as columns.\n• Zero matrix: every element {0}.\n"
      "• Diagonal matrix: square, zero except on the leading diagonal (top left to bottom right).\n"
      "• Identity matrix I: diagonal with every diagonal element {1}, like {matStr([[1, 0], [0, 1]])}. It behaves like the number {1} in multiplication.")],
    key_words=[("matrix", "a rectangular array of numbers in rows and columns"), ("order", "rows × columns"),
               ("element", "one number in a matrix"), ("leading diagonal", "from the top left to the bottom right of a square matrix")],
    examples=["{matStr([[2, 5, 1], [0, 3, 7]])} has order {2} × {3}", "{matStr([[6], [1]])} is a {2} × {1} column matrix",
              "{matStr([[1, 0], [0, 1]])} is the identity I"],
    mistake=("{matStr([[2, 5, 1], [0, 3, 7]])} has order {3} × {2}", "its order is {2} × {3}",
             "Rows come first in the order. This matrix has {2} rows and {3} columns.")))

# ---------------------------------------------------------------- 21. Addition, subtraction, scalar multiplication
L.lesson(D, S, 21, ("m3-21", "Add and subtract matrices; multiply by a scalar"), [20],
  "• Add or subtract matrices of the same order by adding or subtracting corresponding elements.\n"
  "• Matrices of different orders cannot be added or subtracted.\n"
  "• Scalar multiplication: kA multiplies every element of A by the number k.\n"
  "• Combine them: 2A − 3B means double every element of A, triple every element of B, then subtract.\n"
  "• Matrix equations: A + X = B gives X = B − A.",
  worked({"A": [[3, -1], [2, 5]], "B": [[1, 4], [-2, 0]]},
         "Given A and B in the figure, find {2}A − B.",
         ["{2}A = {matStr(matScale(2, A))}: every element doubled.", "{2}A − B: subtract corresponding elements.",
          "{2 * A[0][0]} − {B[0][0]} = {2 * A[0][0] - B[0][0]}, {2 * A[0][1]} − {B[0][1]} = {2 * A[0][1] - B[0][1]}, {2 * A[1][0]} − {br(B[1][0])} = {2 * A[1][0] - B[1][0]}, {2 * A[1][1]} − {B[1][1]} = {2 * A[1][1] - B[1][1]}."],
         "{2}A − B = {matStr(matSub(matScale(2, A), B))}", checks=["2 * A[0][1] - B[0][1] == -6"], figure=FIG_AB),
  [card("c3m21-1", "Add matrices of the same order element by element.",
        ["{matStr([[1, 2], [3, 4]])} + {matStr([[5, 0], [1, 2]])} = {matStr([[6, 2], [4, 6]])}"], "m3-21-add"),
   card("c3m21-2", "kA multiplies every element by k.",
        ["{3} × {matStr([[2, -1], [0, 4]])} = {matStr([[6, -3], [0, 12]])}"], "m3-21-scalar"),
   card("c3m21-3", "Only matrices of the same order can be added or subtracted.",
        ["A {2} × {2} matrix and a {2} × {3} matrix cannot be added."], "m3-21-can")],
  [mcq("m3-21-add", 1, "Given A and B in the figure, find A + B.", "{matStr(matAdd(A, B))}",
       [("{matStr(matSub(A, B))}", "sub"), ("{matStr(matAdd(A, matT(B)))}", "cross"), ("{matStr(matScale(2, A))}", "double")],
       ["Add corresponding elements: {a} + {br(e)}, {b} + {br(f)}, {c} + {br(g)}, {d} + {br(h)}.", "A + B = {answer}."],
       vars=AB, misc=[("sub", "That subtracts B. Add the corresponding elements."), ("cross", "Add the element in the same position: row {1}, column {2} of A goes with row {1}, column {2} of B."),
                      ("double", "That is A + A. Add the elements of B.")],
       figure=FIG_AB, sources=SRC, where=["f != g", "e != 0 || f != 0", "matStr(matAdd(A, B)) != matStr(matScale(2, A))", "matStr(matSub(A, B)) != matStr(matAdd(A, B))"]),
   num("m3-21-scalar", 1, "Find the element in " + POS + " of {k}A.", "k * A[r - 1][s - 1]",
       ["{k}A multiplies every element of A by {k}.", "The element of A in " + POS + " is {A[r - 1][s - 1]}; × {k} = {answer}."],
       vars={**AB, **RC, "k": {"int": [-4, 6]}},
       misc=[("add", "k + A[r - 1][s - 1]", "Scalar multiplication multiplies, it does not add.")],
       figure=FIG_A, sources=SRC, where=["k != 0 && k != 1 && k != -1", "A[r - 1][s - 1] != 0", "k + A[r - 1][s - 1] != k * A[r - 1][s - 1]"], signed=True),
   num("m3-21-combo", 2, "Find the element in " + POS + " of {p}A − {q}B.", "p * A[r - 1][s - 1] - q * B[r - 1][s - 1]",
       ["In " + POS + ": A has {A[r - 1][s - 1]} and B has {B[r - 1][s - 1]}.", "{p} × {br(A[r - 1][s - 1])} − {q} × {br(B[r - 1][s - 1])} = {answer}."],
       vars={**AB, **RC, "p": {"int": [2, 4]}, "q": {"int": [2, 4]}},
       misc=[("plus", "p * A[r - 1][s - 1] + q * B[r - 1][s - 1]", "Subtract {q}B: {p} × {br(A[r - 1][s - 1])} − {q} × {br(B[r - 1][s - 1])}."),
             ("noscale", "A[r - 1][s - 1] - B[r - 1][s - 1]", "Multiply by {p} and {q} first.")],
       figure=FIG_AB, sources=SRC, where=["B[r - 1][s - 1] != 0", "A[r - 1][s - 1] != B[r - 1][s - 1]"], signed=True),
   bank("m3-21-can", 2, "{X.q}", [
     {"q": "A is a 2 × 2 matrix and B is a 2 × 3 matrix. Can you work out A + B?", "r": "No: they have different orders", "w": ["Yes: add the elements that match and leave the rest", "Yes: the answer is 2 × 3", "Yes: the answer is 2 × 5"],
      "e": ["Every element must have a partner: the orders must be the same.", "Addition needs the same order for both matrices.", "Orders are not added."], "y": "Only matrices of the same order can be added."},
     {"q": "A and B are both 3 × 2 matrices. What is the order of A − B?", "r": "3 × 2", "w": ["6 × 4", "2 × 3", "3 × 4"],
      "e": ["Orders are not added: subtracting element by element keeps the order.", "Rows stay rows: 3 × 2.", "The number of columns does not change."], "y": "Adding or subtracting keeps the order: 3 × 2."},
     {"q": "A is a 2 × 3 matrix. What is the order of 5A?", "r": "2 × 3", "w": ["10 × 15", "2 × 15", "10 × 3"],
      "e": ["The scalar multiplies the elements, not the order.", "The number of columns does not change.", "The number of rows does not change."], "y": "Scalar multiplication keeps the order."}], SRC),
   num("m3-21-solve", 3, "A + X = B. Find the element in " + POS + " of X.", "B[r - 1][s - 1] - A[r - 1][s - 1]",
       ["X = B − A.", "In " + POS + ": {B[r - 1][s - 1]} − {br(A[r - 1][s - 1])} = {answer}."],
       vars={**AB, **RC},
       misc=[("add", "B[r - 1][s - 1] + A[r - 1][s - 1]", "X = B − A: subtract A, do not add it."), ("rev", "A[r - 1][s - 1] - B[r - 1][s - 1]", "That is A − B. X = B − A.")],
       figure=FIG_AB, sources=SRC, where=["A[r - 1][s - 1] != 0", "A[r - 1][s - 1] != B[r - 1][s - 1]"], signed=True)],
  learn=learn(
    [("Adding element by element",
      "To add two matrices, add the elements in the same position. The answer has the same order.\n"
      "{matStr([[1, 2], [3, 4]])} + {matStr([[5, 0], [1, 2]])} = {matStr([[6, 2], [4, 6]])}.\n"
      "Subtracting works the same way. Each element needs a partner in the same position, so the two matrices must have the same order. "
      "A {2} × {2} and a {2} × {3} matrix cannot be added."),
     ("Multiplying by a number",
      "A scalar is an ordinary number. kA means multiply every element of A by k:\n"
      "{3} × {matStr([[2, -1], [0, 4]])} = {matStr([[6, -3], [0, 12]])}.\n"
      "If two shops have the same price list matrix and prices rise by a factor, every price is multiplied: that is scalar multiplication."),
     ("Combining and solving",
      "For {2}A − B, first double every element of A, then subtract B element by element.\n"
      "Matrix equations work like ordinary equations: A + X = B gives X = B − A, and {2}X = C gives X = ½C.\n"
      "Always keep track of positions: row first, then column.")],
    key_words=[("corresponding elements", "elements in the same row and column of two matrices"), ("scalar", "an ordinary number that multiplies a matrix"),
               ("same order", "the same number of rows and the same number of columns")],
    examples=["{matStr([[4, 1], [2, 0]])} − {matStr([[1, 3], [2, 5]])} = {matStr([[3, -2], [0, -5]])}",
              "{-2} × {matStr([[1, -3]])} = {matStr([[-2, 6]])}"],
    mistake=("{2} × {matStr([[1, 3], [4, 2]])} = {matStr([[2, 3], [4, 2]])}", "{2} × {matStr([[1, 3], [4, 2]])} = {matStr([[2, 6], [8, 4]])}",
             "A scalar multiplies every element, not just the first one.")))

# ---------------------------------------------------------------- 22. Matrix multiplication
L.lesson(D, S, 22, ("m3-22", "Multiply matrices"), [21],
  "To multiply AB, multiply each row of A by each column of B: multiply the pairs of elements and add.\n"
  "• Row 1 of A × column 1 of B gives the element in row 1, column 1 of AB, and so on.\n"
  "• AB exists only if the number of columns of A equals the number of rows of B. An m × n matrix times an n × p matrix gives an m × p matrix.\n"
  "• In general AB ≠ BA: the order of multiplication matters.\n"
  "• The identity matrix leaves a matrix unchanged: AI = IA = A.",
  worked({"A": [[2, 1], [3, 4]], "B": [[1, 5], [2, 0]]},
         "Find AB for A and B in the figure.",
         ["Row {1} × column {1}: {A[0][0]} × {B[0][0]} + {A[0][1]} × {B[1][0]} = {matMul(A, B)[0][0]}.",
          "Row {1} × column {2}: {A[0][0]} × {B[0][1]} + {A[0][1]} × {B[1][1]} = {matMul(A, B)[0][1]}.",
          "Row {2} × column {1}: {A[1][0]} × {B[0][0]} + {A[1][1]} × {B[1][0]} = {matMul(A, B)[1][0]}.",
          "Row {2} × column {2}: {A[1][0]} × {B[0][1]} + {A[1][1]} × {B[1][1]} = {matMul(A, B)[1][1]}."],
         "AB = {matStr(matMul(A, B))}", checks=["matMul(A, B)[1][0] == 11"], figure=FIG_AB),
  [card("c3m22-1", "Each element of AB is a row of A times a column of B: multiply pairs and add.",
        ["Row ({2}, {1}) × column ({1}, {2}): {2} × {1} + {1} × {2} = {4}"], "m3-22-first"),
   card("c3m22-2", "An m × n matrix times an n × p matrix gives an m × p matrix; the inside numbers must match.",
        ["({2} × {3}) × ({3} × {1}) gives {2} × {1}."], "m3-22-order"),
   card("c3m22-3", "The order matters: AB is usually not equal to BA.",
        ["Always multiply rows of the first by columns of the second."], "m3-22-full")],
  [num("m3-22-first", 1, "Find the element in row {1}, column {1} of AB.", "a * e + b * g",
       ["Row {1} of A is ({a}, {b}); column {1} of B is ({e}, {g}).", "{a} × {br(e)} + {b} × {br(g)} = {answer}."],
       vars=AB, misc=[("same", "a * e + b * f", "Use column {1} of B, going down: {e} and {g}."), ("each", "a * e", "Multiply each pair and add both products.")],
       figure=FIG_AB, sources=SRC, where=["f != g", "b != 0", "a * e + b * f != a * e + b * g", "a * e != a * e + b * g"], signed=True),
   mcq("m3-22-order", 1, "A is a {m} × {n} matrix and B is a {p} × {q} matrix. What can you say about AB?",
       "{n == p ? 'AB is a ' + m + ' × ' + q + ' matrix' : 'AB cannot be found'}",
       [("{n == p ? 'AB is a ' + n + ' × ' + p + ' matrix' : 'AB is a ' + m + ' × ' + q + ' matrix'}", "w1"),
        ("{n == p ? 'AB cannot be found' : 'AB is a ' + n + ' × ' + p + ' matrix'}", "w2"),
        ("{'AB is a ' + (m + p) + ' × ' + (n + q) + ' matrix'}", "w3")],
       ["AB needs the columns of A ({n}) to equal the rows of B ({p}).", "{n == p ? 'They match, and the order of AB is rows of A × columns of B.' : 'They do not match.'} So: {answer}."],
       vars={"m": {"int": [1, 4]}, "n": {"int": [1, 4]}, "p": {"int": [1, 4]}, "q": {"int": [1, 4]}},
       misc=[("w1", "{n == p ? 'The order of AB is (rows of A) × (columns of B): ' + m + ' × ' + q + '.' : 'Columns of A (' + n + ') must equal rows of B (' + p + '): they do not.'}"),
             ("w2", "{n == p ? 'Columns of A (' + n + ') equal rows of B (' + p + '), so AB exists.' : 'AB does not exist, so it has no order.'}"),
             ("w3", "Orders are not added. Check whether the inside numbers match.")],
       sources=SRC, where=["!(n == p && m == n && p == q)", "!(n != p && m == n && q == p)"]),
   num("m3-22-elem", 2, "Find the element in " + POS + " of AB.", "matMul(A, B)[r - 1][s - 1]",
       ["Row {r} of A: ({A[r - 1][0]}, {A[r - 1][1]}). Column {s} of B: ({B[0][s - 1]}, {B[1][s - 1]}).",
        "{A[r - 1][0]} × {br(B[0][s - 1])} + {A[r - 1][1]} × {br(B[1][s - 1])} = {answer}."],
       vars={**AB, **RC},
       misc=[("ba", "matMul(B, A)[r - 1][s - 1]", "That is the element of BA. AB uses rows of A and columns of B."),
             ("elementwise", "A[r - 1][s - 1] * B[r - 1][s - 1]", "Matrices are not multiplied element by element: use row × column.")],
       figure=FIG_AB, sources=SRC, where=["matMul(B, A)[r - 1][s - 1] != matMul(A, B)[r - 1][s - 1]", "A[r - 1][s - 1] * B[r - 1][s - 1] != matMul(A, B)[r - 1][s - 1]"], signed=True),
   mcq("m3-22-full", 2, "Find AB.", "{matStr(matMul(A, B))}",
       [("{matStr(matMul(B, A))}", "ba"), ("{matStr([[a * e, b * f], [c * g, d * h]])}", "elementwise"), ("{matStr(matMul(A, matT(B)))}", "rows")],
       ["Each element is a row of A times a column of B.", "AB = {answer}."],
       vars=AB, misc=[("ba", "That is BA. The order matters: rows of A, columns of B."), ("elementwise", "Multiplying element by element is not matrix multiplication."),
                      ("rows", "That multiplies rows of A by rows of B. Use the columns of B.")],
       figure=FIG_AB, sources=SRC, where=["matStr(matMul(A, B)) != matStr(matMul(B, A))", "f != g", "matStr(matMul(A, B)) != matStr([[a * e, b * f], [c * g, d * h]])",
                                          "matStr(matMul(B, A)) != matStr([[a * e, b * f], [c * g, d * h]])", "matStr(matMul(A, matT(B))) != matStr(matMul(B, A))", "matStr(matMul(A, matT(B))) != matStr([[a * e, b * f], [c * g, d * h]])"]),
   num("m3-22-square", 3, "Find the element in " + POS + " of A² (that is, A × A).", "matMul(A, A)[r - 1][s - 1]",
       ["A² = A × A. Row {r} of A: ({A[r - 1][0]}, {A[r - 1][1]}); column {s} of A: ({A[0][s - 1]}, {A[1][s - 1]}).",
        "{A[r - 1][0]} × {br(A[0][s - 1])} + {A[r - 1][1]} × {br(A[1][s - 1])} = {answer}."],
       vars={**AB, **RC},
       misc=[("sq", "A[r - 1][s - 1] * A[r - 1][s - 1]", "A² is not found by squaring each element: multiply A by A, row × column.")],
       figure=FIG_A, sources=SRC, where=["A[r - 1][s - 1] * A[r - 1][s - 1] != matMul(A, A)[r - 1][s - 1]"], signed=True)],
  learn=learn(
    [("Row times column",
      "Matrix multiplication is not done element by element. Each element of AB comes from a row of A and a column of B:\n"
      "multiply the first elements, multiply the second elements, and add.\n"
      "For A = {matStr([[2, 1], [3, 4]])} and B = {matStr([[1, 5], [2, 0]])}: row {1} of A is ({2}, {1}) and column {1} of B is ({1}, {2}), "
      "so the top-left element of AB is {2} × {1} + {1} × {2} = {4}."),
     ("When can we multiply?",
      "Each row of A must have as many elements as each column of B. So the number of columns of A must equal the number of rows of B.\n"
      "Write the orders side by side: ({2} × {3})({3} × {1}). The inside numbers match ({3} and {3}), so AB exists, and its order is the outside numbers: {2} × {1}.\n"
      "If the inside numbers differ, AB cannot be found."),
     ("Order matters",
      "With numbers, {3} × {5} = {5} × {3}. With matrices, AB and BA are usually different, and one of them may not even exist.\n"
      "The identity matrix I = {matStr([[1, 0], [0, 1]])} is special: AI = IA = A for any {2} × {2} matrix A.\n"
      "A² means A × A, row times column, not each element squared.")],
    key_words=[("product AB", "rows of A times columns of B"), ("compatible", "columns of the first = rows of the second"),
               ("identity matrix", "I: AI = IA = A")],
    examples=["{matStr([[1, 2]])} × {matStr([[3], [4]])} = {matStr([[11]])}", "({3} × {2})({2} × {2}) gives a {3} × {2} matrix"],
    mistake=("{matStr([[1, 2], [3, 4]])} × {matStr([[5, 0], [1, 2]])} = {matStr([[5, 0], [3, 8]])}", "= {matStr(matMul([[1, 2], [3, 4]], [[5, 0], [1, 2]]))}",
             "Do not multiply element by element. Each element is a row of the first times a column of the second, added up.")))

# ---------------------------------------------------------------- 23. Transpose, determinant and adjoint
L.lesson(D, S, 23, ("m3-23", "Transpose, determinant and adjoint of a matrix"), [22],
  "• The transpose Aᵀ turns rows into columns: the first row of A becomes the first column of Aᵀ. A 2 × 3 matrix has a 3 × 2 transpose.\n"
  "• For A = (a b ; c d), the determinant is |A| = ad − bc (leading diagonal product minus the other diagonal product).\n"
  "• A matrix with determinant 0 is singular; otherwise it is non-singular.\n"
  "• The adjoint of (a b ; c d) is (d −b ; −c a): swap the elements of the leading diagonal and change the signs of the other two.\n"
  "• A × adj A = |A| × I.",
  worked({"A": [[4, 3], [2, 5]]},
         "For A in the figure, find |A| and adj A.",
         ["|A| = {A[0][0]} × {A[1][1]} − {A[0][1]} × {A[1][0]} = {A[0][0] * A[1][1]} − {A[0][1] * A[1][0]} = {det2(A)}.",
          "adj A: swap {A[0][0]} and {A[1][1]}, change the signs of {A[0][1]} and {A[1][0]}.", "adj A = {matStr(adj2(A))}."],
         "|A| = {det2(A)}, adj A = {matStr(adj2(A))}", checks=["det2(A) == 14"], figure=FIG_A),
  [card("c3m23-1", "The transpose turns rows into columns.",
        ["A = {matStr([[1, 2, 3], [4, 5, 6]])}, Aᵀ = {matStr([[1, 4], [2, 5], [3, 6]])}"], "m3-23-t"),
   card("c3m23-2", "|A| = ad − bc for A = (a b ; c d).",
        ["|{matStr([[3, 1], [4, 2]])}| = {6} − {4} = {2}"], "m3-23-det"),
   card("c3m23-3", "Adjoint: swap a and d, change the signs of b and c.",
        ["adj {matStr([[3, 1], [4, 2]])} = {matStr([[2, -1], [-4, 3]])}"], "m3-23-adj")],
  [mcq("m3-23-t", 1, "Find the transpose of M.", "{matStr(matT(M))}",
       [("{matStr(M)}", "same"), ("{matStr([M[1], M[0]])}", "swaprows"), ("{matStr(matT([M[1], M[0]]))}", "flip")],
       ["The first row ({M[0][0]}, {M[0][1]}, {M[0][2]}) becomes the first column; the second row becomes the second column.", "Mᵀ = {answer}."],
       vars={"p": {"int": [-5, 9]}, "q": {"int": [-5, 9]}, "u": {"int": [-5, 9]}, "v": {"int": [-5, 9]}, "w": {"int": [-5, 9]}, "z": {"int": [-5, 9]},
             "M": {"expr": "[[p, q, u], [v, w, z]]"}},
       misc=[("same", "That is M itself. The transpose turns rows into columns."), ("swaprows", "Swapping the rows is not the transpose: rows become columns."),
             ("flip", "Row {1} of M must become column {1}: the first column starts {M[0][0]}.")],
       figure="matFig([['M', M]])", sources=SRC, where=["p != v", "q != w || u != z"]),
   num("m3-23-det", 1, "Find the determinant of A.", "det2(A)",
       ["|A| = ad − bc = {a} × {br(d)} − {b} × {br(c)}.", "= {a * d} − {br(b * c)} = {answer}."],
       vars=AB, misc=[("plus", "a * d + b * c", "Subtract the second product: ad − bc."), ("other", "b * c - a * d", "Start with the leading diagonal (top left × bottom right): ad − bc.")],
       figure=FIG_A, sources=SRC, where=["b * c != 0", "a * d != 0", "a * d - b * c != 0", "a * d + b * c != a * d - b * c", "a * d + b * c != b * c - a * d"], signed=True),
   mcq("m3-23-adj", 2, "Find the adjoint of A.", "{matStr(adj2(A))}",
       [("{matStr([[d, b], [c, a]])}", "nosign"), ("{matStr([[a, -b], [-c, d]])}", "noswap"), ("{matStr([[-d, b], [c, -a]])}", "wrongsigns")],
       ["Swap the leading diagonal: {a} and {d}.", "Change the signs of the other two: {b} → {-b}, {c} → {-c}.", "adj A = {answer}."],
       vars=AB, misc=[("nosign", "Change the signs of b and c as well."), ("noswap", "Swap a and d as well."),
                      ("wrongsigns", "The leading diagonal keeps its signs; it is b and c that change sign.")],
       figure=FIG_A, sources=SRC, where=["a != d", "b != 0 && c != 0", "a != -d", "a != 0 && d != 0"]),
   num("m3-23-sing", 2, "The matrix A in the figure is singular. Find k.", "b * c / d",
       ["Singular: |A| = {0}, so k × {d} − {b} × {br(c)} = {0}.", "k × {d} = {b * c}, so k = {answer}."],
       vars={"d": {"int": [1, 6]}, "c": {"int": [-6, 6]}, "b": {"int": [-6, 9]}, "A": {"expr": "[['k', b], [c, d]]"}},
       misc=[("sign", "-b * c / d", "kd − bc = {0} gives k = bc ÷ d = {b * c} ÷ {d}.")],
       figure=FIG_A, sources=SRC, where=["(b * c) % d == 0", "b * c != 0"], signed=True),
   num("m3-23-prod", 3, "Find |AB| for A and B in the figure (use |AB| = |A| × |B|, or work out AB first).", "det2(A) * det2(B)",
       ["|A| = {a * d} − {br(b * c)} = {det2(A)}; |B| = {e * h} − {br(f * g)} = {det2(B)}.", "|AB| = {det2(A)} × {br(det2(B))} = {answer}."],
       vars=AB, misc=[("sum", "det2(A) + det2(B)", "|AB| = |A| × |B|: multiply the determinants.")],
       figure=FIG_AB, sources=SRC, where=["det2(A) != 0 && det2(B) != 0", "det2(A) * det2(B) != det2(A) + det2(B)"], signed=True)],
  learn=learn(
    [("The transpose",
      "Write the rows of A as columns and you get its transpose, Aᵀ. A {2} × {3} matrix becomes {3} × {2}:\n"
      "A = {matStr([[1, 2, 3], [4, 5, 6]])} gives Aᵀ = {matStr([[1, 4], [2, 5], [3, 6]])}.\n"
      "The element in row i, column j of A moves to row j, column i."),
     ("The determinant",
      "Every square matrix has a number called its determinant. For a {2} × {2} matrix A = (a b ; c d):\n"
      "|A| = ad − bc: the product of the leading diagonal minus the product of the other diagonal.\n"
      "|{matStr([[3, 1], [4, 2]])}| = {3} × {2} − {1} × {4} = {2}.\n"
      "If |A| = {0}, A is called singular. You will see next lesson that a singular matrix has no inverse."),
     ("The adjoint",
      "The adjoint of A = (a b ; c d) is adj A = (d −b ; −c a): swap a and d, and change the signs of b and c.\n"
      "adj {matStr([[3, 1], [4, 2]])} = {matStr([[2, -1], [-4, 3]])}.\n"
      "Check: A × adj A = {matStr(matMul([[3, 1], [4, 2]], [[2, -1], [-4, 3]]))} = |A| × I. This fact gives the inverse.")],
    key_words=[("transpose", "Aᵀ: rows written as columns"), ("determinant", "|A| = ad − bc for a {2} × {2} matrix"),
               ("singular", "having determinant {0}"), ("adjoint", "adj A = (d −b ; −c a)")],
    examples=["|{matStr([[5, 2], [3, 1]])}| = {5} − {6} = {-1}", "adj {matStr([[1, 4], [2, 7]])} = {matStr([[7, -4], [-2, 1]])}"],
    mistake=("|{matStr([[3, 1], [4, 2]])}| = {3} × {2} + {1} × {4} = {10}", "|A| = {3} × {2} − {1} × {4} = {2}",
             "The determinant is a difference: ad minus bc.")))

# ---------------------------------------------------------------- 24. Inverse of a matrix
L.lesson(D, S, 24, ("m3-24", "Find and use the inverse of a 2 × 2 matrix"), [23],
  "The inverse A⁻¹ of a square matrix A satisfies AA⁻¹ = A⁻¹A = I.\n"
  "For a 2 × 2 matrix: A⁻¹ = (1 ÷ |A|) × adj A. For A = (a b ; c d), A⁻¹ = 1/(ad − bc) × (d −b ; −c a).\n"
  "• If |A| = 0 (A singular), A has no inverse.\n"
  "• Check: AA⁻¹ = I.\n"
  "• Simultaneous equations ax + by = p, cx + dy = q can be written A(x ; y) = (p ; q), so (x ; y) = A⁻¹(p ; q).",
  worked({"A": [[5, 2], [7, 3]]},
         "Find the inverse of A in the figure.",
         ["|A| = {A[0][0]} × {A[1][1]} − {A[0][1]} × {A[1][0]} = {A[0][0] * A[1][1]} − {A[0][1] * A[1][0]} = {det2(A)}.",
          "adj A = {matStr(adj2(A))}.", "A⁻¹ = ({1} ÷ {det2(A)}) × adj A = {matStr(adj2(A))}.",
          "Check: A × A⁻¹ = {matStr(matMul(A, adj2(A)))} = I. ✓"],
         "A⁻¹ = {matStr(adj2(A))}", checks=["det2(A) == 1"], figure=FIG_A),
  [card("c3m24-1", "A⁻¹ = ({1} ÷ |A|) × adj A; a matrix with |A| = {0} has no inverse.",
        ["|{matStr([[2, 4], [1, 2]])}| = {0}: no inverse."], "m3-24-exists"),
   card("c3m24-2", "When |A| = {1}, the inverse is just the adjoint.",
        ["A = {matStr([[3, 5], [1, 2]])}: |A| = {1}, A⁻¹ = {matStr([[2, -5], [-1, 3]])}."], "m3-24-one"),
   card("c3m24-3", "Use A⁻¹ to solve simultaneous equations: (x ; y) = A⁻¹(p ; q).",
        ["Write the coefficients as A and the right-hand sides as a column."], "m3-24-solve")],
  [mcq("m3-24-exists", 1, "Does the matrix A in the figure have an inverse?",
       "{det2(A) == 0 ? 'No: |A| = 0' : 'Yes: |A| = ' + fmt(det2(A))}",
       [("{det2(A) == 0 ? 'Yes: |A| = ' + fmt(a * (k * b) + b * (k * a)) : 'No: |A| = 0'}", "w1"),
        ("{'Yes: every square matrix has an inverse'}", "w2"), ("{'No: only the identity has an inverse'}", "w3")],
       ["|A| = {a} × {br(k * b + t)} − {b} × {br(k * a)} = {det2(A)}.", "{det2(A) == 0 ? 'A singular matrix has no inverse.' : 'The determinant is not zero, so A⁻¹ exists.'} So: {answer}."],
       vars={"a": {"int": [1, 5]}, "b": {"int": [1, 6]}, "k": {"int": [2, 3]}, "t": {"pick": [0, 0, 1, 2, -1]}, "A": {"expr": "[[a, b], [k * a, k * b + t]]"}},
       misc=[("w1", "Work out ad − bc carefully: {a} × {br(k * b + t)} − {b} × {br(k * a)} = {det2(A)}."), ("w2", "A matrix with determinant {0} has no inverse."),
             ("w3", "Any matrix with a non-zero determinant has an inverse.")],
       figure=FIG_A, sources=SRC, where=[]),
   num("m3-24-one", 1, "|A| = {1}. Find the element in " + POS + " of A⁻¹.", "adj2(A)[r - 1][s - 1]",
       ["|A| = {det2(A)}, so A⁻¹ = adj A = {matStr(adj2(A))}.", "The element in " + POS + " is {answer}."],
       vars={**RC, "p": {"int": [1, 4]}, "q": {"int": [1, 5]}, "A": {"expr": "[[p * q + 1, p], [q, 1]]"}},
       misc=[("orig", "A[r - 1][s - 1]", "That is the element of A. The inverse here is the adjoint: swap a and d, and change the signs of b and c.")],
       figure=FIG_A, sources=SRC, where=["r != s"], signed=True),
   num("m3-24-frac", 2, "Find the element in " + POS + " of A⁻¹. Give it as a fraction in its simplest form.", "frac(adj2(A)[r - 1][s - 1], det2(A))",
       ["|A| = {a * d} − {br(b * c)} = {det2(A)}; adj A = {matStr(adj2(A))}.", "A⁻¹ = adj A ÷ {det2(A)}: the element is {adj2(A)[r - 1][s - 1]} ÷ {det2(A)} = {answer}."],
       vars={**AB, **RC},
       misc=[("nodet", "adj2(A)[r - 1][s - 1]", "Divide the adjoint by the determinant {det2(A)}."), ("orig", "frac(A[r - 1][s - 1], det2(A))", "Use the adjoint, not A itself.")],
       answer_kind="fraction", figure=FIG_A, sources=SRC,
       where=["abs(det2(A)) > 1", "adj2(A)[r - 1][s - 1] % det2(A) != 0", "A[r - 1][s - 1] != adj2(A)[r - 1][s - 1]", "frac(A[r - 1][s - 1], det2(A)) != frac(adj2(A)[r - 1][s - 1], det2(A))"], signed=True),
   num("m3-24-solve", 2, "Use the inverse matrix to solve {poly([p * q + 1, 'x'], [p, 'y'])} = {(p * q + 1) * x + p * y} and {poly([q, 'x'], [1, 'y'])} = {q * x + y}. What is x?", "x",
       ["A = {matStr([[p * q + 1, p], [q, 1]])}, |A| = {1}, A⁻¹ = {matStr([[1, -p], [-q, p * q + 1]])}.",
        "x = {1} × {(p * q + 1) * x + p * y} + {br(-p)} × {q * x + y} = {answer}."],
       vars={"p": {"int": [1, 4]}, "q": {"int": [1, 4]}, "x": {"int": [-5, 8]}, "y": {"int": [-5, 8]}},
       misc=[("y", "y", "That is y. x comes from the first row of A⁻¹.")],
       sources=SRC, where=["x != y"], signed=True),
   mcq("m3-24-inv", 3, "Find the inverse of A.", "{frac(1, det2(A)) + ' × ' + matStr(adj2(A))}",
       [("{frac(1, det2(A)) + ' × ' + matStr(A)}", "noadj"), ("{fmt(det2(A)) + ' × ' + matStr(adj2(A))}", "times"), ("{frac(1, det2(A)) + ' × ' + matStr(matT(A))}", "transpose")],
       ["|A| = {a * d} − {br(b * c)} = {det2(A)}.", "adj A = {matStr(adj2(A))}.", "A⁻¹ = ({1} ÷ |A|) × adj A = {answer}."],
       vars=AB, misc=[("noadj", "Use the adjoint (swap a and d, change the signs of b and c), not A."), ("times", "Divide by the determinant: multiply by {1} ÷ |A|."),
                      ("transpose", "The transpose is not the adjoint: swap a and d and change the signs of b and c.")],
       figure=FIG_A, sources=SRC, where=["abs(det2(A)) > 1", "b != c", "a != d", "b != 0 && c != 0"])],
  learn=learn(
    [("Undoing a matrix",
      "For numbers, {5} × {frac(1, 5)} = {1}: {frac(1, 5)} is the inverse of {5}. For matrices, the identity I plays the part of {1}.\n"
      "The inverse of A is the matrix A⁻¹ with AA⁻¹ = A⁻¹A = I.\n"
      "From the last lesson, A × adj A = |A| × I. Divide by |A|: A⁻¹ = ({1} ÷ |A|) × adj A."),
     ("Finding it",
      "A = {matStr([[5, 2], [7, 3]])}.\n• |A| = {15} − {14} = {1}.\n• adj A = {matStr([[3, -2], [-7, 5]])}.\n"
      "• A⁻¹ = ({1} ÷ {1}) × adj A = {matStr([[3, -2], [-7, 5]])}.\n"
      "If |A| is, say, {2}, every element of the adjoint is divided by {2}. If |A| = {0}, you cannot divide: a singular matrix has no inverse."),
     ("Solving equations",
      "{poly([5, 'x'], [2, 'y'])} = {16} and {poly([7, 'x'], [3, 'y'])} = {23} can be written A(x ; y) = ({16} ; {23}).\n"
      "Multiply both sides by A⁻¹: (x ; y) = A⁻¹({16} ; {23}).\n"
      "x = {3} × {16} + ({-2}) × {23} = {2}; y = ({-7}) × {16} + {5} × {23} = {3}.\n"
      "Check: {5} × {2} + {2} × {3} = {16}. ✓")],
    key_words=[("inverse matrix", "A⁻¹, with AA⁻¹ = I"), ("non-singular", "determinant not {0}: the inverse exists"),
               ("identity matrix", "I = {matStr([[1, 0], [0, 1]])}")],
    examples=["{matStr([[2, 1], [1, 1]])}⁻¹ = {matStr([[1, -1], [-1, 2]])} (determinant {1})", "{matStr([[4, 2], [2, 1]])} has no inverse (determinant {0})"],
    mistake=("A⁻¹ = |A| × adj A", "A⁻¹ = ({1} ÷ |A|) × adj A",
             "You divide by the determinant. Check by multiplying: AA⁻¹ must give I.")))
