"""Form 3 Maths, Term 1, rows 25-30 (congruency and similarity). Run: python tools/authoring/form3/maths_similar.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn
from common import bank

L.use_class("form-3", "Form 3")
D, S = "maths", "mathematics"

# ---------------------------------------------------------------- 25. Congruency
SRC = ["congruence"]
L.lesson(D, S, 25, ("m3-25", "Congruent plane figures"), [],
  "Two figures are congruent if they have exactly the same shape and the same size: one fits exactly on top of the other.\n"
  "• Corresponding sides are equal and corresponding angles are equal.\n"
  "• We write ΔABC ≅ ΔPQR. The order of the letters shows which vertices correspond: A ↔ P, B ↔ Q, C ↔ R, so AB = PQ, BC = QR, CA = RP.\n"
  "• Translations, rotations and reflections give congruent images; an enlargement (scale factor not 1) does not.\n"
  "• Similar figures have the same shape but may differ in size.",
  worked({"p": 5, "q": 7, "r": 6, "x": 48, "y": 70},
         "ΔABC ≅ ΔPQR. AB = {p} cm, BC = {q} cm, CA = {r} cm, angle A = {x}° and angle B = {y}°. Find QR and angle R.",
         ["The letters match in order: A ↔ P, B ↔ Q, C ↔ R.", "QR corresponds to BC, so QR = {q} cm.",
          "Angle R corresponds to angle C = {180} − {x} − {y} = {180 - x - y}°."],
         "QR = {q} cm, angle R = {180 - x - y}°", checks=["180 - x - y == 62"]),
  [card("c3m25-1", "Congruent figures have the same shape and the same size.",
        ["Two copies of the same exercise book cover are congruent."], "m3-25-def"),
   card("c3m25-2", "In ΔABC ≅ ΔPQR the letters match in order: AB = PQ, BC = QR, CA = RP.",
        ["Angle B = angle Q."], "m3-25-side"),
   card("c3m25-3", "Translations, rotations and reflections keep the size: the image is congruent.",
        ["An enlargement changes the size: the image is only similar."], "m3-25-move")],
  [bank("m3-25-def", 1, "{X.q}", [
     {"q": "What does it mean for two figures to be congruent?", "r": "Same shape and same size", "w": ["Same shape, possibly a different size", "Same area only", "Same perimeter only"],
      "e": ["That describes similar figures.", "Different shapes can have the same area.", "Different shapes can have the same perimeter."], "y": "Congruent figures fit exactly on top of each other."},
     {"q": "Two triangles have the same angles but one is twice as big. They are…", "r": "similar, not congruent", "w": ["congruent", "neither similar nor congruent", "congruent and similar"],
      "e": ["Congruent figures must also be the same size.", "Equal angles make them similar.", "Different sizes: not congruent."], "y": "Same shape, different size: similar."},
     {"q": "Which pair is always congruent?", "r": "Two squares with sides of 5 cm", "w": ["Two squares", "Two rectangles with the same area", "Two triangles with the same angles"],
      "e": ["Squares of different sizes are only similar.", "A 2 × 8 and a 4 × 4 rectangle have the same area but different shapes.", "Equal angles give similar triangles; they can differ in size."], "y": "Same shape and the same side length: congruent."}], SRC),
   num("m3-25-side", 1, "ΔABC ≅ ΔPQR. AB = {p} cm, BC = {q} cm and CA = {r} cm. Find {X.n}.", "X.v == 'p' ? p : X.v == 'q' ? q : r",
       ["The letters match in order: A ↔ P, B ↔ Q, C ↔ R.", "{X.n} corresponds to {X.m}, so {X.n} = {answer} cm."],
       vars={"p": {"int": [3, 12]}, "q": {"int": [3, 12]}, "r": {"int": [3, 12]},
             "X": {"pick": [{"n": "PQ", "m": "AB", "v": "p"}, {"n": "QR", "m": "BC", "v": "q"}, {"n": "RP", "m": "CA", "v": "r"}]}},
       misc=[("next", "X.v == 'p' ? q : X.v == 'q' ? r : p", "Match the letters in order: {X.n} goes with {X.m}.")],
       unit="cm", sources=SRC, where=["p != q && q != r && p != r", "p + q > r && q + r > p && p + r > q"]),
   num("m3-25-angle", 2, "ΔABC ≅ ΔDEF. Angle A = {x}° and angle B = {y}°. Find angle F.", "180 - x - y",
       ["F corresponds to C.", "Angle C = {180} − {x} − {y} = {answer}°, so angle F = {answer}°."],
       vars={"x": {"int": [30, 80]}, "y": {"int": [30, 80]}},
       misc=[("a", "x", "F matches C, not A: the third letters correspond."), ("b", "y", "F matches C, not B.")],
       unit="°", sources=SRC, where=["x != y", "180 - x - y != x && 180 - x - y != y"]),
   bank("m3-25-move", 2, "{X.q}", [
     {"q": "Which transformation always gives an image congruent to the object?", "r": "A rotation", "w": ["An enlargement with scale factor 2", "An enlargement with scale factor ½", "A stretch in one direction"],
      "e": ["Scale factor 2 doubles the lengths: similar, not congruent.", "Scale factor ½ halves the lengths.", "A stretch changes the shape."], "y": "Rotations keep lengths and angles."},
     {"q": "A triangle is reflected in a line. The image is…", "r": "congruent to the triangle", "w": ["larger than the triangle", "similar but smaller", "a different shape"],
      "e": ["A reflection keeps every length.", "A reflection keeps the size.", "A reflection keeps the shape."], "y": "Reflections keep lengths and angles: the image is congruent."},
     {"q": "Which of these does NOT give a congruent image?", "r": "An enlargement with scale factor 3", "w": ["A translation", "A rotation of 90°", "A reflection"],
      "e": ["A translation slides the shape without changing it.", "A rotation turns the shape without changing it.", "A reflection flips the shape without changing its size."], "y": "An enlargement changes the size."}], SRC),
   bank("m3-25-match", 3, "{X.q}", [
     {"q": "ΔKLM ≅ ΔXYZ. Which side equals LM?", "r": "YZ", "w": ["XY", "XZ", "LZ"],
      "e": ["XY matches KL.", "XZ matches KM.", "Sides are named within one triangle."], "y": "L ↔ Y and M ↔ Z, so LM = YZ."},
     {"q": "ΔABC ≅ ΔRTS. Which angle equals angle C?", "r": "Angle S", "w": ["Angle T", "Angle R", "Angle C is not matched"],
      "e": ["T matches B.", "R matches A.", "Every angle has a partner."], "y": "The third letters correspond: C ↔ S."},
     {"q": "ΔPQR ≅ ΔMNO. Which side equals RP?", "r": "OM", "w": ["MN", "NO", "PO"],
      "e": ["MN matches PQ.", "NO matches QR.", "Sides are named within one triangle."], "y": "R ↔ O and P ↔ M, so RP = OM."}], SRC)],
  learn=learn(
    [("Same shape, same size",
      "Two figures are congruent if one can be placed exactly on top of the other. Their corresponding sides are equal and their corresponding angles are equal.\n"
      "Two {500} FCFA coins are congruent. A large and a small photo of the same picture are not: they have the same shape but different sizes. Those are similar."),
     ("Naming the matching parts",
      "When we write ΔABC ≅ ΔPQR, the order of the letters tells us which vertices match: A ↔ P, B ↔ Q, C ↔ R.\n"
      "So AB = PQ, BC = QR and CA = RP, and angle A = angle P, angle B = angle Q, angle C = angle R.\n"
      "Always match the letters in order; do not just look at the picture."),
     ("Moving without changing",
      "Translation (sliding), rotation (turning) and reflection (flipping) move a figure without changing its lengths or angles, so the image is congruent to the object.\n"
      "An enlargement with a scale factor other than {1} changes the size: the image is similar, not congruent.")],
    key_words=[("congruent", "same shape and same size (≅)"), ("corresponding", "in the matching position"),
               ("similar", "same shape, possibly a different size")],
    examples=["ΔABC ≅ ΔDEF: AB = DE, angle C = angle F", "A reflected triangle is congruent to the original."],
    mistake=("ΔABC ≅ ΔPQR, so BC = PR", "BC = QR",
             "Match the letters in order: B ↔ Q and C ↔ R.")))

# ---------------------------------------------------------------- 26. Congruency tests
SRC = ["congruence"]
L.lesson(D, S, 26, ("m3-26", "Prove triangles congruent: SSS, SAS, ASA, RHS"), [25],
  "Two triangles are congruent if any one of these is true:\n"
  "• SSS: the three sides of one equal the three sides of the other.\n"
  "• SAS: two sides and the included angle (the angle between them) are equal.\n"
  "• ASA (or AAS): two angles and a corresponding side are equal.\n"
  "• RHS: both have a right angle, equal hypotenuses and one other equal side.\n"
  "AAA is not a test (it only shows similarity), and SSA (angle not between the sides) is not a test.",
  worked({},
         "ABCD is a parallelogram with diagonal AC. Show that ΔABC ≅ ΔCDA.",
         ["AB = CD (opposite sides of a parallelogram are equal).", "BC = DA (opposite sides).", "AC is common to both triangles.",
          "So ΔABC ≅ ΔCDA (SSS)."], "Congruent by SSS"),
  [card("c3m26-1", "SSS: three pairs of equal sides.",
        ["Sides {5}, {7}, {9} and {9}, {5}, {7}: congruent (SSS)."], "m3-26-test"),
   card("c3m26-2", "SAS needs the included angle: the angle between the two sides.",
        ["The angle between AB and BC is angle B."], "m3-26-incl"),
   card("c3m26-3", "AAA and SSA are not tests of congruence.",
        ["Equal angles alone give similar triangles, which can differ in size."], "m3-26-not")],
  [bank("m3-26-test", 1, "{X.q} Which condition proves the triangles congruent?", [
     {"q": "All three sides of one triangle equal the three sides of the other.", "r": "SSS", "w": ["SAS", "RHS", "AAA"],
      "e": ["SAS needs an angle.", "RHS needs a right angle.", "AAA is not a congruence test."], "y": "Three pairs of sides: SSS."},
     {"q": "Two sides and the angle between them are equal.", "r": "SAS", "w": ["SSS", "ASA", "SSA"],
      "e": ["Only two sides are known.", "Only one side is known in ASA.", "SSA is not a test; here the angle is between the sides."], "y": "Two sides and the included angle: SAS."},
     {"q": "Two angles and the side between them are equal.", "r": "ASA", "w": ["SAS", "SSS", "AAA"],
      "e": ["Only one side is known.", "Only one side is known.", "A side is known too: that makes it ASA."], "y": "Two angles and a side: ASA."},
     {"q": "Both are right-angled, the hypotenuses are equal and one other pair of sides is equal.", "r": "RHS", "w": ["SAS", "SSS", "ASA"],
      "e": ["The right angle is not between the two given sides.", "Only two pairs of sides are given.", "Only one angle (the right angle) is given."], "y": "Right angle, hypotenuse, side: RHS."}], SRC),
   bank("m3-26-not", 1, "{X.q}", [
     {"q": "Which of these is NOT a test for congruent triangles?", "r": "AAA", "w": ["SSS", "SAS", "RHS"],
      "e": ["SSS is a test.", "SAS is a test.", "RHS is a test."], "y": "Equal angles only show the triangles are similar; they can be different sizes."},
     {"q": "Which of these is NOT a test for congruent triangles?", "r": "SSA (angle not between the sides)", "w": ["ASA", "SSS", "SAS (angle between the sides)"],
      "e": ["ASA is a test.", "SSS is a test.", "SAS with the included angle is a test."], "y": "With the angle not between the two sides, two different triangles can be drawn."},
     {"q": "Two triangles have equal angles of 40°, 60° and 80°. Are they congruent?", "r": "Not necessarily: they are similar", "w": ["Yes, by AAA", "Yes, by ASA", "No, they cannot be similar either"],
      "e": ["AAA is not a congruence test.", "ASA needs a pair of equal sides as well.", "Equal angles make them similar."], "y": "Equal angles give the same shape, not necessarily the same size."}], SRC),
   bank("m3-26-incl", 2, "{X.q}", [
     {"q": "In ΔPQR, which angle is included between sides PQ and QR?", "r": "Angle Q", "w": ["Angle P", "Angle R", "No angle is included"],
      "e": ["Angle P is between PQ and PR.", "Angle R is between PR and QR.", "Two sides always meet at an angle."], "y": "PQ and QR meet at Q."},
     {"q": "In ΔABC, which angle is included between sides CA and AB?", "r": "Angle A", "w": ["Angle B", "Angle C", "Angle ABC"],
      "e": ["Angle B is between AB and BC.", "Angle C is between BC and CA.", "Angle ABC is angle B."], "y": "CA and AB meet at A."},
     {"q": "In ΔXYZ, which angle is included between sides YZ and ZX?", "r": "Angle Z", "w": ["Angle X", "Angle Y", "Angle XYZ"],
      "e": ["Angle X is between XY and XZ.", "Angle Y is between XY and YZ.", "Angle XYZ is angle Y."], "y": "YZ and ZX meet at Z."}], SRC),
   bank("m3-26-which", 2, "{X.q}", [
     {"q": "In ΔABC and ΔDEF: AB = DE, angle B = angle E and BC = EF. Which test shows they are congruent?", "r": "SAS", "w": ["SSS", "ASA", "They are not congruent"],
      "e": ["Only two sides are given.", "Only one angle is given.", "Angle B is between AB and BC: SAS applies."], "y": "Two sides and the included angle."},
     {"q": "In ΔPQR and ΔXYZ: angle P = angle X, PQ = XY, angle Q = angle Y. Which test applies?", "r": "ASA", "w": ["SAS", "AAA", "RHS"],
      "e": ["Two angles and one side are given, not two sides.", "A side is also given, so it is ASA.", "No right angle is given."], "y": "Two angles and the side between them."},
     {"q": "The diagonal AC of a kite ABCD (AB = AD, CB = CD) splits it into two triangles. Which test shows ΔABC ≅ ΔADC?", "r": "SSS", "w": ["SAS", "RHS", "ASA"],
      "e": ["No angle is known to be equal yet.", "No right angle is given.", "No angles are given."], "y": "AB = AD, CB = CD and AC is common: SSS."}], SRC),
   bank("m3-26-proof", 3, "{X.q}", [
     {"q": "O is the midpoint of AB and of CD. Why are ΔAOC and ΔBOD congruent?", "r": "SAS: OA = OB, angle AOC = angle BOD (vertically opposite), OC = OD", "w": ["SSS: all sides equal", "AAA: all angles equal", "RHS: both are right-angled"],
      "e": ["AC = BD is not given.", "AAA is not a test.", "Nothing says the angles are right angles."], "y": "Two sides from the midpoints and the vertically opposite angles between them."},
     {"q": "In an isosceles triangle ABC (AB = AC), M is the midpoint of BC. Why is ΔABM ≅ ΔACM?", "r": "SSS: AB = AC, BM = CM, AM is common", "w": ["SAS: AB = AC and angle B = angle C", "AAA", "RHS without a right angle"],
      "e": ["The angle given is not between the given sides.", "AAA is not a test.", "RHS needs a right angle that is not given."], "y": "Three pairs of equal sides."},
     {"q": "AD is the perpendicular from A to BC in triangle ABC, and AB = AC. Why is ΔABD ≅ ΔACD?", "r": "RHS: right angles at D, AB = AC (hypotenuses), AD common", "w": ["SAS: AB = AC and AD common", "ASA: two right angles", "SSA"],
      "e": ["The right angle is not between AB and AD.", "One side and only the right angle are known.", "SSA is not a test; RHS is the special case that works."], "y": "Right angle, equal hypotenuses, a common side: RHS."}], SRC)],
  learn=learn(
    [("You do not need everything",
      "To show two triangles are congruent, you do not need all six measurements to match. Some sets of three are enough to fix the triangle completely.\n"
      "If you know three sides, there is only one triangle you can draw with them. That gives the first test, SSS."),
     ("The four tests",
      "• SSS: three pairs of equal sides.\n"
      "• SAS: two pairs of equal sides and the angle between them (the included angle).\n"
      "• ASA: two pairs of equal angles and a pair of corresponding sides.\n"
      "• RHS: a right angle, equal hypotenuses and one more pair of equal sides.\n"
      "In a proof, give a reason for each equal part: \"given\", \"common side\", \"vertically opposite angles\", \"opposite sides of a parallelogram\"…"),
     ("Two that do not work",
      "AAA: triangles with the same three angles have the same shape but can be different sizes. They are similar, not necessarily congruent.\n"
      "SSA: two sides and an angle that is not between them. Sometimes two different triangles fit, so it proves nothing. "
      "The exception is RHS, where the angle is a right angle.")],
    key_words=[("included angle", "the angle between two given sides"), ("common side", "a side shared by both triangles"),
               ("proof", "a chain of facts, each with a reason, leading to the result")],
    examples=["AB = DE, BC = EF, CA = FD → SSS", "angle A = angle D, AB = DE, angle B = angle E → ASA"],
    mistake=("Equal angles, so the triangles are congruent (AAA)", "Equal angles only show the triangles are similar",
             "AAA does not fix the size. You need at least one pair of equal sides too.")))

# ---------------------------------------------------------------- 27. Similar figures
SRC = ["similarity"]
L.lesson(D, S, 27, ("m3-27", "Similar figures and the scale factor"), [25],
  "Similar figures have the same shape: corresponding angles are equal and corresponding sides are in the same ratio.\n"
  "• The scale factor (constant of proportionality) k = a side of the image ÷ the corresponding side of the object.\n"
  "• Every length of the image = k × the matching length of the object.\n"
  "• Two triangles with equal angles are always similar.\n"
  "• All squares, all circles and all equilateral triangles are similar; rectangles in general are not.\n"
  "Shadows: at the same time of day, heights are proportional to shadow lengths.",
  worked({"a": 4, "b": 6, "c": 10},
         "Two similar triangles: a side of {a} cm in the small one matches {b} cm in the large one. Another side of the small triangle is {c} cm. Find the matching side of the large one.",
         ["Scale factor k = {b} ÷ {a} = {b / a}.", "Large side = {b / a} × {c} = {b / a * c} cm."],
         "{b / a * c} cm", checks=["b / a * c == 15"]),
  [card("c3m27-1", "Scale factor k = image side ÷ matching object side.",
        ["{3} cm becomes {12} cm: k = {4}."], "m3-27-k"),
   card("c3m27-2", "Multiply every length by k to get the matching length.",
        ["k = {4}: a {5} cm side becomes {20} cm."], "m3-27-side"),
   card("c3m27-3", "Similar means the same shape: equal angles, sides in the same ratio.",
        ["All circles are similar; not all rectangles are."], "m3-27-which")],
  [num("m3-27-k", 1, "A side of {a} cm in one figure matches a side of {a * k} cm in a similar, larger figure. What is the scale factor?", "k",
       ["k = {a * k} ÷ {a} = {answer}."],
       vars={"a": {"int": [2, 12]}, "k": {"int": [2, 6]}},
       misc=[("diff", "a * k - a", "The scale factor multiplies: divide, do not subtract."), ("inv", "1 / k", "Divide the larger by the smaller to enlarge: {a * k} ÷ {a}.")],
       sources=SRC, where=["a * k - a != k"]),
   num("m3-27-side", 1, "Triangle PQR is similar to triangle ABC with scale factor {k}. AB = {x} cm. Find PQ.", "k * x",
       ["PQ matches AB.", "PQ = {k} × {x} = {answer} cm."],
       vars={"k": {"int": [2, 5]}, "x": {"int": [2, 15]}},
       misc=[("add", "k + x", "Scale factors multiply lengths, they do not add to them.")],
       unit="cm", sources=SRC, where=["k + x != k * x"]),
   num("m3-27-ratio", 2, "Two similar rectangles: the small one is {a} cm by {b} cm. The long side of the large one is {c} cm. Find its short side.", "a * c / b",
       ["Long sides: k = {c} ÷ {b} = {c / b}.", "Short side = {c / b} × {a} = {answer} cm."],
       vars={"a": {"int": [2, 9]}, "b": {"int": [3, 12]}, "c": {"int": [4, 30]}},
       misc=[("add", "a + c - b", "Similar figures are in proportion: multiply by the scale factor, do not add the difference."),
             ("wrongpair", "b * c / a", "Match short with short and long with long.")],
       unit="cm", sources=SRC, where=["a < b", "c > b", "(a * c) % b == 0", "a + c - b != a * c / b"]),
   bank("m3-27-which", 2, "{X.q}", [
     {"q": "Which pair of figures is always similar?", "r": "Any two circles", "w": ["Any two rectangles", "Any two isosceles triangles", "Any two right-angled triangles"],
      "e": ["A long thin rectangle is not the same shape as a square-like one.", "Isosceles triangles can have different angles.", "Right-angled triangles can have different other angles."], "y": "Every circle is an enlargement of every other circle."},
     {"q": "Which pair of figures is always similar?", "r": "Any two squares", "w": ["Any two rhombuses", "Any two parallelograms", "Any two trapeziums"],
      "e": ["Rhombuses can have different angles.", "Parallelograms can have different angles and side ratios.", "Trapeziums can have many shapes."], "y": "All angles are 90° and all sides are equal: squares differ only in size."},
     {"q": "Two triangles have angles 50°, 60°, 70° and 70°, 50°, 60°. They are…", "r": "similar", "w": ["congruent", "neither similar nor congruent", "similar only if they are right-angled"],
      "e": ["Equal angles do not fix the size.", "Equal angles always make triangles similar.", "Any triangles with equal angles are similar."], "y": "Equal corresponding angles: similar triangles."}], SRC),
   num("m3-27-shadow", 3, "At {X.t}, a {h} m pole in Bamenda casts a shadow {s} m long. At the same time a tree casts a shadow {s * m} m long. How tall is the tree (m)?", "h * m",
       ["The sun's rays make similar triangles: height ÷ shadow is the same.", "Scale factor = {s * m} ÷ {s} = {m}.", "Tree = {m} × {h} = {answer} m."],
       vars={"h": {"int": [2, 4]}, "s": {"int": [3, 6]}, "m": {"int": [3, 8]}, "X": {"pick": [{"t": "10 a.m."}, {"t": "3 p.m."}, {"t": "4 p.m."}]}},
       misc=[("inv", "s * m * s / h", "Height ÷ shadow is the same for both: tree = {h} ÷ {s} × {s * m}."), ("add", "h + s * m - s", "Use the ratio, not the difference.")],
       unit="m", sources=SRC, where=["h != s"])],
  learn=learn(
    [("Same shape, different size",
      "A photo printed small and large shows the same picture: the shape is the same, only the size changes. Such figures are similar.\n"
      "In similar figures:\n• corresponding angles are equal;\n• corresponding sides are in the same ratio.\n"
      "That common ratio is the scale factor k (also called the constant of proportionality)."),
     ("Finding lengths",
      "Find k from one pair of matching sides: k = side in the image ÷ matching side in the object.\n"
      "If a {4} cm side becomes {6} cm, k = {6} ÷ {4} = {1.5}. Then a {10} cm side becomes {1.5} × {10} = {15} cm.\n"
      "Match short with short and long with long. If k is less than {1}, the image is smaller."),
     ("Shadows and heights",
      "At the same moment, the sun's rays hit all objects at the same angle. A pole and a tree with their shadows form similar right-angled triangles.\n"
      "If a {2} m pole has a {3} m shadow and a tree has a {15} m shadow, the scale factor is {5}, so the tree is {5} × {2} = {10} m tall.")],
    key_words=[("similar", "same shape: equal angles, sides in the same ratio"), ("scale factor", "k = image length ÷ object length"),
               ("corresponding sides", "sides in matching positions")],
    examples=["k = {3}: a {2} cm side becomes {6} cm", "All equilateral triangles are similar."],
    mistake=("A {4} cm by {6} cm rectangle grows to {8} cm by {10} cm (add {4})", "{8} cm by {12} cm (multiply by {2})",
             "Similar figures are enlarged by multiplying, not by adding the same amount.")))

# ---------------------------------------------------------------- 28. Areas and volumes of similar figures
SRC = ["similarity"]
L.lesson(D, S, 28, ("m3-28", "Areas and volumes of similar figures"), [27],
  "If two figures are similar with linear scale factor k:\n"
  "• lengths are multiplied by k;\n• areas are multiplied by k²;\n• volumes (and masses of the same material) are multiplied by k³.\n"
  "Going back: if areas are in the ratio 4 : 9, lengths are in the ratio 2 : 3 (square roots); if volumes are in the ratio 8 : 27, lengths are 2 : 3 (cube roots).",
  worked({"k": 3, "A": 5},
         "Two similar triangles have corresponding sides {2} cm and {2 * k} cm. The smaller has area {A} cm². Find the area of the larger.",
         ["Linear scale factor k = {2 * k} ÷ {2} = {k}.", "Area scale factor = k² = {k * k}.", "Larger area = {k * k} × {A} = {k * k * A} cm²."],
         "{k * k * A} cm²", checks=["k * k * A == 45"]),
  [card("c3m28-1", "Area scale factor = k².",
        ["k = {2}: areas are multiplied by {4}."], "m3-28-area"),
   card("c3m28-2", "Volume scale factor = k³.",
        ["k = {2}: volumes are multiplied by {8}."], "m3-28-vol"),
   card("c3m28-3", "From an area ratio, take square roots to get the length ratio.",
        ["Areas {9} : {25} → lengths {3} : {5}"], "m3-28-back")],
  [num("m3-28-area", 1, "Two similar shapes have linear scale factor {k}. The smaller has area {A} cm². Find the area of the larger (cm²).", "k * k * A",
       ["Area scale factor = {k}² = {k * k}.", "Area = {k * k} × {A} = {answer} cm²."],
       vars={"k": {"int": [2, 5]}, "A": {"int": [2, 20]}},
       misc=[("lin", "k * A", "Areas use k², not k: {k} × {k} = {k * k}."), ("cube", "k * k * k * A", "k³ is for volumes; areas use k².")],
       unit="cm²", sources=SRC),
   num("m3-28-vol", 2, "Two similar tins of tomato paste have heights {h} cm and {h * k} cm. The small tin holds {V} cm³. How much does the large tin hold (cm³)?", "k * k * k * V",
       ["k = {h * k} ÷ {h} = {k}.", "Volume scale factor = {k}³ = {k * k * k}.", "Volume = {k * k * k} × {V} = {answer} cm³."],
       vars={"h": {"int": [4, 10]}, "k": {"int": [2, 4]}, "V": {"int": [50, 400], "step": 50}},
       misc=[("lin", "k * V", "Volumes use k³."), ("sq", "k * k * V", "k² is for areas; volumes use k³.")],
       unit="cm³", sources=SRC),
   num("m3-28-back", 2, "Two similar figures have areas {a * a * m} cm² and {b * b * m} cm². The smaller has a side of {a * n} cm. Find the matching side of the larger (cm).", "b * n",
       ["Area ratio {a * a * m} : {b * b * m} = {a * a} : {b * b}.", "Length ratio = √ = {a} : {b}, so k = {b} ÷ {a}.", "Side = {a * n} × {b} ÷ {a} = {answer} cm."],
       vars={"a": {"int": [1, 4]}, "b": {"int": [2, 6]}, "m": {"int": [1, 3]}, "n": {"int": [1, 5]}},
       misc=[("nosqrt", "a * n * b * b / (a * a)", "The area ratio is k²: take the square root to get the length ratio.")],
       unit="cm", sources=SRC, where=["a < b", "a * n * b * b / (a * a) != b * n"]),
   num("m3-28-mass", 2, "Two similar statues are made of the same wood. Their heights are {p} cm and {q} cm. The small one has mass {M} g. Find the mass of the large one (g).", "M * q * q * q / (p * p * p)",
       ["Mass is proportional to volume: factor k³.", "k = {q} ÷ {p}; k³ = {q * q * q} ÷ {p * p * p}.", "Mass = {M} × {q * q * q} ÷ {p * p * p} = {answer} g."],
       vars={"p": {"int": [1, 3]}, "q": {"int": [2, 6]}, "M": {"int": [1, 9]}},
       misc=[("lin", "M * q / p", "Mass goes with volume: use k³, not k.")],
       unit="g", sources=SRC, where=["p < q", "(M * q * q * q) % (p * p * p) == 0"]),
   num("m3-28-volarea", 3, "Two similar jugs have volumes {a * a * a} litres and {b * b * b} litres. The surface area of the small jug is {A} cm². Find the surface area of the large jug (cm²).", "A * b * b / (a * a)",
       ["Volume ratio = k³ = {b * b * b} ÷ {a * a * a}, so k = {b} ÷ {a} (cube root).", "Area factor = k² = {b * b} ÷ {a * a}.", "Area = {A} × {b * b} ÷ {a * a} = {answer} cm²."],
       vars={"a": {"int": [1, 3]}, "b": {"int": [2, 5]}, "A": {"int": [36, 900], "step": 36}},
       misc=[("vol", "A * b * b * b / (a * a * a)", "Areas use k², not k³: first find k from the cube root."), ("lin", "A * b / a", "Areas use k².")],
       unit="cm²", sources=SRC, where=["a < b", "(A * b * b) % (a * a) == 0"])],
  learn=learn(
    [("Why areas grow faster",
      "Double every length of a {1} cm square: it becomes {2} cm by {2} cm, and its area goes from {1} cm² to {4} cm².\n"
      "Area is length × length, so a length factor k gives an area factor k × k = k².\n"
      "For k = {3}, areas are multiplied by {9}. A floor plan drawn three times larger needs nine times as much paper."),
     ("And volumes faster still",
      "Volume is length × length × length, so the volume factor is k³.\n"
      "Double the sides of a cube: the volume is multiplied by {8}. A tin twice as tall (and similar) holds eight times as much.\n"
      "Objects made of the same material have mass proportional to volume, so masses also go up by k³."),
     ("Working backwards",
      "If you know the ratio of areas, take square roots to get the length ratio: areas {16} : {25} → lengths {4} : {5}.\n"
      "If you know the ratio of volumes, take cube roots: volumes {8} : {125} → lengths {2} : {5}.\n"
      "Then use the length ratio to find whatever you need.")],
    key_words=[("linear scale factor", "k, for lengths"), ("area factor", "k²"), ("volume factor", "k³")],
    examples=["k = {4}: area × {16}, volume × {64}", "Volumes {27} : {64} → lengths {3} : {4} → areas {9} : {16}"],
    mistake=("Lengths doubled, so the area is doubled", "The area is multiplied by {2}² = {4}",
             "Area uses two lengths, so the factor is applied twice.")))

# ---------------------------------------------------------------- 29. Thales
SRC = ["similarity"]
L.lesson(D, S, 29, ("m3-29", "The Thales (intercept) property and its converse"), [27],
  "Thales property: in triangle ABC, if D is on AB and E is on AC with DE parallel to BC, then\n"
  "AD/AB = AE/AC = DE/BC (triangle ADE is similar to triangle ABC), and also AD/DB = AE/EC.\n"
  "Converse: if AD/AB = AE/AC (or AD/DB = AE/EC), then DE is parallel to BC.\n"
  "Use it to find lengths: write the equal ratios, then cross-multiply.",
  worked({"ad": 4, "db": 6, "ae": 5},
         "In the figure DE ∥ BC, AD = {ad} cm, DB = {db} cm and AE = {ae} cm. Find EC.",
         ["Thales: AD/DB = AE/EC.", "{ad}/{db} = {ae}/EC.", "EC = {ae} × {db} ÷ {ad} = {ae * db / ad} cm."],
         "EC = {ae * db / ad} cm", checks=["ae * db / ad == 7.5"], figure="thalesFig(ad, db, ae, 'EC', '', '')"),
  [card("c3m29-1", "If DE ∥ BC, then AD/DB = AE/EC.",
        ["AD = {2}, DB = {4}, AE = {3}: EC = {6}"], "m3-29-ec"),
   card("c3m29-2", "Triangle ADE is similar to ABC: DE/BC = AD/AB.",
        ["AD = {3}, AB = {9}, BC = {12}: DE = {4}"], "m3-29-de"),
   card("c3m29-3", "Converse: if AD/DB = AE/EC, then DE ∥ BC.",
        ["{2}/{3} = {4}/{6}: parallel."], "m3-29-conv")],
  [num("m3-29-ec", 1, "In the figure DE ∥ BC. AD = {ad} cm, DB = {db} cm and AE = {ae} cm. Find EC (cm).", "ae * db / ad",
       ["AD/DB = AE/EC: {ad}/{db} = {ae}/EC.", "EC = {ae} × {db} ÷ {ad} = {answer} cm."],
       vars={"ad": {"int": [2, 8]}, "db": {"int": [2, 10]}, "ae": {"int": [2, 12]}},
       misc=[("flip", "ae * ad / db", "Keep the same order on both sides: AD/DB = AE/EC."), ("diff", "ae + db - ad", "Thales uses equal ratios, not equal differences.")],
       unit="cm", figure="thalesFig(ad, db, ae, 'EC', '', '')", sources=SRC, where=["ad != db", "(ae * db) % ad == 0", "ae * ad / db != ae * db / ad", "ae + db - ad != ae * db / ad"]),
   num("m3-29-de", 1, "In the figure DE ∥ BC. AD = {ad} cm, DB = {db} cm and BC = {bc} cm. Find DE (cm).", "bc * ad / (ad + db)",
       ["AB = {ad} + {db} = {ad + db} cm.", "DE/BC = AD/AB, so DE = {bc} × {ad} ÷ {ad + db} = {answer} cm."],
       vars={"ad": {"int": [2, 8]}, "db": {"int": [2, 10]}, "bc": {"int": [5, 30]}},
       misc=[("db", "bc * ad / db", "Compare with the whole side: DE/BC = AD/AB, and AB = AD + DB = {ad + db}.")],
       unit="cm", figure="thalesFig(ad, db, '', '', 'DE', bc)", sources=SRC, where=["(bc * ad) % (ad + db) == 0", "bc * ad / db != bc * ad / (ad + db)"]),
   num("m3-29-ae", 2, "In the figure DE ∥ BC. AD = {ad} cm, AB = {ad + db} cm and AC = {(ad + db) * t} cm. Find AE (cm).", "ad * t",
       ["AD/AB = AE/AC: {ad}/{ad + db} = AE/{(ad + db) * t}.", "AE = {(ad + db) * t} × {ad} ÷ {ad + db} = {answer} cm."],
       vars={"ad": {"int": [2, 8]}, "db": {"int": [2, 8]}, "t": {"int": [2, 4]}},
       misc=[("ec", "db * t", "That is EC. AE goes with AD.")],
       unit="cm", figure="thalesFig(ad, '', 'AE', '', '', '')", sources=SRC, where=["ad != db"]),
   mcq("m3-29-conv", 2, "In triangle ABC, D is on AB and E is on AC. AD = {p} cm, DB = {q} cm, AE = {r} cm and EC = {s} cm. Is DE parallel to BC?",
       "{p * s == q * r ? 'Yes: AD/DB = AE/EC = ' + frac(p, q) : 'No: AD/DB = ' + frac(p, q) + ' but AE/EC = ' + frac(r, s)}",
       [("{p * s == q * r ? 'No: AD/DB = ' + frac(p, q) + ' but AE/EC = ' + frac(r, s + 1) : 'Yes: AD/DB = AE/EC = ' + frac(p, q)}", "flip"),
        ("{'Yes: AD + DB = ' + (p + q) + ' cm'}", "sum"), ("{'It cannot be decided without measuring the angles'}", "angles")],
       ["Compare the ratios: AD/DB = {p}/{q} = {frac(p, q)} and AE/EC = {r}/{s} = {frac(r, s)}.", "So: {answer}."],
       vars={"p": {"int": [2, 6]}, "q": {"int": [2, 6]}, "m": {"int": [1, 3]}, "w": {"pick": [0, 0, 1]}, "r": {"expr": "p * m + w"}, "s": {"expr": "q * m"}},
       misc=[("flip", "Work out both ratios: {frac(p, q)} and {frac(r, s)}."), ("sum", "Adding the lengths says nothing about parallel lines: compare the ratios."),
             ("angles", "The converse of Thales decides it from the lengths alone.")],
       figure="thalesFig(p, q, r, s, '', '')", sources=SRC, where=["p != q"]),
   num("m3-29-river", 3, "To measure a river, Tabe marks points so that triangles ADE and ABC are similar (DE ∥ BC). AD = {ad} m, DB (the river width) is unknown, DE = {de} m and BC = {bc} m. Find the width DB (m).", "ad * bc / de - ad",
       ["DE/BC = AD/AB, so AB = {ad} × {bc} ÷ {de} = {ad * bc / de} m.", "DB = AB − AD = {ad * bc / de} − {ad} = {answer} m."],
       vars={"ad": {"int": [4, 20]}, "de": {"int": [3, 12]}, "bc": {"int": [5, 30]}},
       misc=[("ab", "ad * bc / de", "That is AB, the whole side. The width is AB − AD."), ("flip", "ad * de / bc", "AB is longer than AD: multiply by {bc} ÷ {de}.")],
       unit="m", figure="thalesFig(ad, 'width', '', '', de, bc, 'm')", sources=SRC, where=["bc > de", "(ad * bc) % de == 0"])],
  learn=learn(
    [("A line parallel to a side",
      "Draw triangle ABC and a line DE parallel to BC, with D on AB and E on AC. The small triangle ADE has the same angles as ABC (corresponding angles), so it is similar to ABC.\n"
      "Therefore AD/AB = AE/AC = DE/BC.\n"
      "This is the Thales (intercept) property. It also gives AD/DB = AE/EC: the parallel line cuts the two sides in the same ratio.", "thalesFig('AD', 'DB', 'AE', 'EC', 'DE', 'BC', '')"),
     ("Finding a length",
      "If AD = {4} cm, DB = {6} cm and AE = {5} cm, then {4}/{6} = {5}/EC.\n"
      "Cross-multiply: {mono(4, 'EC')} = {30}, so EC = {7.5} cm.\n"
      "For DE use the whole sides: DE/BC = AD/AB, with AB = AD + DB. Mixing AD/DB with DE/BC is a common error."),
     ("The converse",
      "Thales works backwards too: if D and E cut AB and AC in the same ratio, then DE is parallel to BC.\n"
      "AD = {2}, DB = {3}, AE = {4}, EC = {6}: {2}/{3} = {4}/{6}, so DE ∥ BC.\n"
      "If the ratios differ, the lines are not parallel.")],
    key_words=[("parallel", "lines that never meet (∥)"), ("ratio", "a comparison by division, such as AD/DB"),
               ("converse", "the statement turned round: equal ratios give parallel lines")],
    examples=["AD = {3}, AB = {9}, BC = {12}: DE = {4}", "AD/DB = AE/EC = {frac(2, 3)}: DE ∥ BC"],
    mistake=("DE/BC = AD/DB", "DE/BC = AD/AB",
             "DE and BC are sides of the small and the large triangles, so compare them with AD and the whole side AB.")))

# ---------------------------------------------------------------- 30. Applications to areas and volumes
SRC = ["similarity"]
L.lesson(D, S, 30, ("m3-30", "Use similarity: maps, models, areas and volumes"), [28],
  "Scale drawings, maps and models are similar to the real objects.\n"
  "• A map scale 1 : n means 1 cm on the map is n cm on the ground. Lengths × n; areas × n².\n"
  "• Convert units carefully: 100 000 cm = 1 km, so 1 cm² on a 1 : 100 000 map is 1 km².\n"
  "• Models: a model car on a scale 1 : 20 is 20 times shorter, 400 times smaller in area, 8000 times smaller in volume.\n"
  "• Costs that depend on area (paint) scale by k²; those that depend on volume (contents, mass) by k³.",
  worked({"n": 50000, "A": 6},
         "A map of a farm near Kumba has scale {1} : {n}. A field has area {A} cm² on the map. Find its real area in hectares ({1} ha = {10000} m²).",
         ["{1} cm on the map = {n} cm = {n / 100} m on the ground.", "{1} cm² on the map = {n / 100} × {n / 100} = {n * n / 10000} m².",
          "{A} cm² → {A} × {n * n / 10000} = {A * n * n / 10000} m² = {A * n * n / 100000000} ha."],
         "{A * n * n / 100000000} ha", checks=["A * n * n / 100000000 == 150"]),
  [card("c3m30-1", "On a map {1} : n, lengths are multiplied by n and areas by n².",
        ["{1} : {1000}: {2} cm → {2000} cm = {20} m."], "m3-30-map"),
   card("c3m30-2", "Convert units at the end: {1} km = {100000} cm.",
        ["{1} : {100000}: {1} cm² represents {1} km²."], "m3-30-km"),
   card("c3m30-3", "Paint depends on area (k²); contents and mass depend on volume (k³).",
        ["A tank twice as wide, long and high needs {4} times the paint and holds {8} times the water."], "m3-30-paint")],
  [num("m3-30-map", 1, "A map has scale {1} : {n}. A road is {d} cm long on the map. How long is it in real life, in metres?", "d * n / 100",
       ["Real length = {d} × {n} = {d * n} cm.", "{d * n} cm ÷ {100} = {answer} m."],
       vars={"n": {"pick": [500, 1000, 2000, 5000]}, "d": {"int": [2, 15]}},
       misc=[("cm", "d * n", "That is in centimetres. Divide by {100} for metres."), ("div", "d / n", "Multiply by the scale number: the real road is longer.")],
       unit="m", sources=SRC),
   num("m3-30-km", 1, "On a map of scale {1} : {100000}, a lake covers {A} cm². What is its real area in km²?", "A",
       ["{1} cm on the map = {100000} cm = {1} km.", "So {1} cm² on the map = {1} km², and {A} cm² = {answer} km²."],
       vars={"A": {"int": [2, 30]}},
       misc=[("big", "A * 100000", "Convert: {100000} cm is {1} km, so each cm² is {1} km².")],
       unit="km²", sources=SRC),
   num("m3-30-model", 2, "A model of a minibus is made on a scale of {1} : {k}. The real minibus has a floor area of {F} m². What is the floor area of the model, in cm²?", "F * 10000 / (k * k)",
       ["Area scale factor = {k}² = {k * k}.", "Real floor = {F} m² = {F * 10000} cm².", "Model = {F * 10000} ÷ {k * k} = {answer} cm²."],
       vars={"k": {"pick": [10, 20, 25, 50]}, "F": {"int": [5, 12]}},
       misc=[("lin", "F * 10000 / k", "Areas scale by k², not k."), ("units", "F / (k * k)", "Convert m² to cm²: {1} m² = {10000} cm².")],
       unit="cm²", sources=SRC, where=["(F * 10000) % (k * k) == 0"]),
   num("m3-30-paint", 2, "A tin of paint covers a small model water tank. A similar real tank is {k} times as long. How many tins are needed for the real tank?", "k * k",
       ["Paint covers area: area factor = {k}² = {k * k}.", "Tins needed = {answer}."],
       vars={"k": {"int": [2, 9]}},
       misc=[("lin", "k", "Paint depends on area: use k², not k."), ("cube", "k * k * k", "k³ would be for the water it holds; paint covers area.")],
       unit="tins", sources=SRC),
   num("m3-30-cost", 3, "A small tin of groundnut oil, {h} cm tall, costs {c} FCFA. A similar large tin is {h * k} cm tall. If the price is proportional to the amount of oil, what does the large tin cost (FCFA)?", "c * k * k * k",
       ["k = {h * k} ÷ {h} = {k}; the amount of oil goes with volume, factor {k}³ = {k * k * k}.", "Price = {c} × {k * k * k} = {answer} FCFA."],
       vars={"h": {"int": [5, 10]}, "k": {"int": [2, 3]}, "c": {"int": [150, 600], "step": 50}},
       misc=[("sq", "c * k * k", "Oil fills the volume: use k³, not k²."), ("lin", "c * k", "Use k³ for volume.")],
       unit="FCFA", sources=SRC)],
  learn=learn(
    [("Maps and scale",
      "A map is a similar copy of the land, shrunk by its scale. A scale of {1} : {50000} means {1} cm on the map stands for {50000} cm on the ground, which is {500} m.\n"
      "Lengths: multiply by {50000}. Areas: multiply by {50000}² because area uses two lengths.\n"
      "Change units at the end: {100} cm = {1} m, {100000} cm = {1} km, {10000} m² = {1} hectare."),
     ("Models",
      "A model built on a scale of {1} : {20} has every length {20} times smaller than the real thing.\n"
      "• Its surface area is {20}² = {400} times smaller.\n• Its volume is {20}³ = {8000} times smaller.\n"
      "A model car may look the same, but it would hold only a tiny amount of fuel."),
     ("Paying for area or volume",
      "Ask what the quantity depends on.\n• Paint, cloth, tiles: area, so factor k².\n• Contents, mass, amount of oil or water: volume, so factor k³.\n"
      "A tin twice as tall (and similar) holds {8} times as much oil, so it should cost about {8} times as much, not twice.")],
    key_words=[("map scale", "{1} : n, one map unit for n real units"), ("hectare", "{10000} m²"), ("model", "a similar copy, usually smaller")],
    examples=["{1} : {1000}, {3} cm → {30} m", "{1} : {100000}, {5} cm² → {5} km²"],
    mistake=("Map {1} : {1000}: {4} cm² on the map is {4000} cm² on the ground", "{4} × {1000}² = {4000000} cm² = {400} m²",
             "Areas scale by the square of the map scale.")))
