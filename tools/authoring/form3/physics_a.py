"""Form 3 Physics, Term 1, rows 1-9 (physical quantities, measurement, density). Run: python tools/authoring/form3/physics_a.py
g = 10 N/kg throughout (as in Forms 1 and 2, TR-P03)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "physics", "physics"
SRC = ["measurement"]

# ---------------------------------------------------------------- 1. Physical quantities, units, prefixes, standard form
L.lesson(D, S, 1, ("p3-1", "Physical quantities, SI units, prefixes and standard form"), [],
  "A physical quantity can be measured and has a number and a unit: 25 kg, 3.5 m.\n"
  "Base quantities and SI units: length (metre, m), mass (kilogram, kg), time (second, s), temperature (kelvin, K), electric current (ampere, A).\n"
  "Derived quantities come from base ones: area (m²), volume (m³), density (kg/m³), speed (m/s).\n"
  "Prefixes: mega M = 1 000 000, kilo k = 1000, centi c = 1/100, milli m = 1/1000, micro µ = 1/1 000 000.\n"
  "Standard form: a × 10ⁿ with 1 ≤ a < 10, e.g. 340 000 m = 3.4 × 10⁵ m; 0.0025 s = 2.5 × 10⁻³ s.",
  worked({"a": 4.7, "n": 4},
         "Write {a * 10 ^ n} m in standard form.",
         ["Move the decimal point to get a number between {1} and {10}: {a}.", "The point moved {n} places to the left, so the power is {n}.",
          "{a * 10 ^ n} = {a} × {10}{sup(n)}."], "{a} × {10}{sup(n)} m", checks=["a * 10 ^ n == 47000"]),
  [card("c3p1-1", "Every measurement has a number and a unit; the SI unit of mass is the kilogram.",
        ["Length: metre (m). Time: second (s). Temperature: kelvin (K)."], "p3-1-si"),
   card("c3p1-2", "Prefixes are multipliers: kilo = {1000}, milli = {1} ÷ {1000}.",
        ["{3.2} km = {3200} m;  {450} mm = {0.45} m"], "p3-1-prefix"),
   card("c3p1-3", "Standard form: a × {10}ⁿ with a between {1} and {10}.",
        ["{340000} = {3.4} × {10}{sup(5)}"], "p3-1-std")],
  [bank("p3-1-si", 1, "{X.q}", [
     {"q": "What is the SI unit of mass?", "r": "kilogram (kg)", "w": ["gram (g)", "newton (N)", "litre (L)"],
      "e": ["The gram is a smaller unit; the SI base unit is the kilogram.", "The newton is the unit of force (weight).", "The litre measures volume."], "y": "Mass is measured in kilograms in SI."},
     {"q": "What is the SI unit of temperature?", "r": "kelvin (K)", "w": ["degree Celsius (°C)", "joule (J)", "degree Fahrenheit (°F)"],
      "e": ["°C is used every day, but the SI unit is the kelvin.", "The joule is the unit of energy.", "°F is not an SI unit."], "y": "The SI unit of temperature is the kelvin."},
     {"q": "Which is a base quantity (not derived)?", "r": "time", "w": ["speed", "area", "density"],
      "e": ["Speed = distance ÷ time: derived.", "Area = length × length: derived.", "Density = mass ÷ volume: derived."], "y": "Time is one of the base quantities; its unit is the second."},
     {"q": "What is the SI unit of electric current?", "r": "ampere (A)", "w": ["volt (V)", "watt (W)", "ohm (Ω)"],
      "e": ["The volt measures voltage.", "The watt measures power.", "The ohm measures resistance."], "y": "Current is a base quantity measured in amperes."}], SRC),
   num("p3-1-prefix", 1, "Convert {v} {X.f} to {X.t}.", "convertUnit(v, X.f, X.t)",
       ["{1} {X.f} = {factor(X.f, X.t)} {X.t}.", "{v} × {factor(X.f, X.t)} = {answer} {X.t}."],
       vars={"v": {"int": [2, 95]}, "X": {"pick": [{"f": "km", "t": "m"}, {"f": "m", "t": "cm"}, {"f": "mm", "t": "m"}, {"f": "cm", "t": "m"}, {"f": "kg", "t": "g"}, {"f": "g", "t": "kg"}, {"f": "mg", "t": "g"}]}},
       misc=[("flip", "convertUnit(v, X.t, X.f)", "Check the direction: a {X.f} is {factor(X.f, X.t) > 1 ? 'bigger' : 'smaller'} than a {X.t}, so the number gets {factor(X.f, X.t) > 1 ? 'bigger' : 'smaller'}.")],
       sources=SRC),
   num("p3-1-std", 2, "Write {a * 10 ^ n} in standard form, a × {10}ⁿ. What is n?", "n",
       ["a must be between {1} and {10}: a = {a}.", "The decimal point moves {n} places, so n = {answer}."],
       vars={"m": {"int": [11, 99]}, "a": {"expr": "m / 10"}, "n": {"int": [3, 8]}},
       misc=[("digits", "n + 1", "Count the places the point moves, not the number of digits: {a * 10 ^ n} = {a} × {10}{sup(n)}.")],
       sources=SRC, where=["m % 10 != 0"]),
   mcq("p3-1-small", 2, "Write {a / 10 ^ n} in standard form.", "{a + ' × 10⁻' + sup(n)}",
       [("{a * 10 + ' × 10⁻' + sup(n + 1)}", "big"), ("{a + ' × 10' + sup(n)}", "sign"), ("{a / 10 + ' × 10⁻' + sup(n - 1)}", "small")],
       ["Move the point right until the number is between {1} and {10}: {a}.", "It moved {n} places to the right, so the power is −{n}: {answer}."],
       vars={"m": {"int": [11, 99]}, "a": {"expr": "m / 10"}, "n": {"int": [2, 6]}},
       misc=[("big", "{a * 10} is not between {1} and {10}."), ("sign", "A small number (less than {1}) has a negative power of {10}."), ("small", "{a / 10} is less than {1}: a must be at least {1}.")],
       sources=SRC, where=["m % 10 != 0"]),
   num("p3-1-micro", 3, "A hair is {d} µm thick. What is this in millimetres?", "d / 1000",
       ["{1} µm = {1} ÷ {1000000} m and {1} mm = {1} ÷ {1000} m, so {1} µm = {0.001} mm.", "{d} µm = {d} ÷ {1000} = {answer} mm."],
       vars={"d": {"int": [40, 120]}},
       misc=[("m", "d / 1000000", "That is in metres. {1} mm = {1000} µm, so divide by {1000}."), ("mult", "d * 1000", "Millimetres are bigger than micrometres: the number gets smaller.")],
       unit="mm", sources=SRC)],
  learn=learn(
    [("What a physical quantity is",
      "Anything we can measure is a physical quantity: the length of a desk, the mass of a bag of rice, the time of a race.\n"
      "A measurement always has two parts, a number and a unit: {25} kg. Without the unit, \"{25}\" means nothing.\n"
      "Scientists everywhere use the SI system so that results can be shared. Its base quantities are length (m), mass (kg), time (s), temperature (K) and electric current (A). "
      "All others, such as area, volume, speed and density, are derived from these."),
     ("Prefixes",
      "Prefixes make big and small numbers easier:\n"
      "• mega (M) = {1000000}\n• kilo (k) = {1000}\n• centi (c) = {1} ÷ {100}\n• milli (m) = {1} ÷ {1000}\n• micro (µ) = {1} ÷ {1000000}\n"
      "So {3.2} km = {3200} m, and {450} mm = {0.45} m. To change to a smaller unit the number gets bigger, and the other way round."),
     ("Standard form",
      "Very large or very small values are written a × {10}ⁿ, with a between {1} and {10}.\n"
      "• {340000} m = {3.4} × {10}{sup(5)} m (the point moves {5} places left).\n"
      "• {0.0025} s = {2.5} × {10}⁻{sup(3)} s (the point moves {3} places right, so the power is negative).\n"
      "The distance from the Earth to the Sun is about {1.5} × {10}{sup(11)} m.")],
    key_words=[("physical quantity", "something that can be measured, with a number and a unit"), ("SI unit", "the international standard unit"),
               ("prefix", "a word in front of a unit that multiplies it, like kilo"), ("standard form", "a × {10}ⁿ with {1} ≤ a < {10}")],
    examples=["{2.5} kg = {2500} g", "{0.00034} m = {3.4} × {10}⁻{sup(4)} m", "{6} MW = {6000000} W"],
    mistake=("{3.4} × {10}{sup(5)} written as {34} × {10}{sup(4)}", "{3.4} × {10}{sup(5)}",
             "In standard form the first number must be between {1} and {10}.")))

# ---------------------------------------------------------------- 2. Scalars, vectors and force equipment
SRC = ["forces"]
L.lesson(D, S, 2, ("p3-2", "Scalar and vector quantities; measuring force"), [1],
  "A scalar quantity has size (magnitude) only: mass, time, distance, speed, temperature, energy.\n"
  "A vector quantity has size and direction: force, weight, displacement, velocity, acceleration.\n"
  "Forces are measured in newtons (N) with a newton meter (spring balance). A beam balance compares masses.\n"
  "Combining forces along a line: same direction → add; opposite directions → subtract, and the resultant acts in the direction of the larger force.\n"
  "Two forces at right angles: the resultant is found with Pythagoras.",
  worked({"a": 12, "b": 5},
         "Two boys pull a cart: one with {a} N to the east, the other with {b} N to the west. Find the resultant force.",
         ["Opposite directions: subtract.", "{a} − {b} = {a - b} N.", "The larger force is to the east, so the resultant is {a - b} N to the east."],
         "{a - b} N to the east", checks=["a - b == 7"]),
  [card("c3p2-1", "A vector has a direction; a scalar does not.",
        ["Force {20} N upwards is a vector; a mass of {20} kg is a scalar."], "p3-2-type"),
   card("c3p2-2", "A newton meter measures force in newtons.",
        ["The spring stretches more for a bigger pull."], "p3-2-tool"),
   card("c3p2-3", "Forces in the same direction add; in opposite directions they subtract.",
        ["{6} N and {4} N east: {10} N east. {6} N east and {4} N west: {2} N east."], "p3-2-line")],
  [bank("p3-2-type", 1, "{X.q}", [
     {"q": "Which of these is a vector quantity?", "r": "force", "w": ["mass", "time", "temperature"],
      "e": ["Mass has size only.", "Time has size only.", "Temperature has size only."], "y": "A force always acts in a direction."},
     {"q": "Which of these is a scalar quantity?", "r": "speed", "w": ["velocity", "weight", "displacement"],
      "e": ["Velocity is speed in a given direction.", "Weight acts downwards: it has a direction.", "Displacement is distance in a given direction."], "y": "Speed has size only."},
     {"q": "Why is weight a vector quantity?", "r": "It has size and always acts downwards", "w": ["It is measured in kilograms", "It can be large or small", "It is measured with a balance"],
      "e": ["Weight is measured in newtons.", "Every quantity can be large or small: that does not make it a vector.", "A balance measures mass."], "y": "Weight is a force towards the centre of the Earth."}], SRC),
   bank("p3-2-tool", 1, "{X.q}", [
     {"q": "Which instrument measures force directly?", "r": "a newton meter (spring balance)", "w": ["a beam balance", "a metre rule", "a measuring cylinder"],
      "e": ["A beam balance compares masses.", "A metre rule measures length.", "A measuring cylinder measures volume."], "y": "The spring stretches in proportion to the force."},
     {"q": "What does a beam balance measure?", "r": "mass", "w": ["weight in newtons", "volume", "density"],
      "e": ["It compares masses, so the answer does not change with g.", "Volume needs a measuring cylinder.", "Density needs mass and volume."], "y": "A beam balance compares an unknown mass with known masses."},
     {"q": "A spring balance reads {30} N. What does it show?", "r": "a force of 30 N", "w": ["a mass of 30 kg", "a mass of 30 g", "a volume of 30 cm³"],
      "e": ["N is the unit of force, not mass.", "N is the unit of force, not mass.", "N is the unit of force."], "y": "A spring balance shows force in newtons."}], SRC),
   num("p3-2-line", 2, "Forces of {a} N and {b} N act on a box {X.d}. Find the size of the resultant force (N).", "X.s == 1 ? a + b : abs(a - b)",
       ["{X.s == 1 ? 'Same direction: add.' : 'Opposite directions: subtract.'}", "{X.s == 1 ? a + ' + ' + b : max(a, b) + ' − ' + min(a, b)} = {answer} N."],
       vars={"a": {"int": [3, 40]}, "b": {"int": [2, 30]}, "X": {"pick": [{"d": "in the same direction", "s": 1}, {"d": "in opposite directions", "s": -1}]}},
       misc=[("other", "X.s == 1 ? abs(a - b) : a + b", "{X.s == 1 ? 'In the same direction the forces add.' : 'In opposite directions one force cancels part of the other: subtract.'}")],
       unit="N", sources=SRC, where=["a != b"]),
   bank("p3-2-dir", 2, "{X.q}", [
     {"q": "A {20} N force pulls a box east and a {35} N force pulls it west. What is the resultant?", "r": "15 N west", "w": ["15 N east", "55 N west", "55 N east"],
      "e": ["The larger force is to the west, so the resultant points west.", "Opposite directions: subtract.", "Opposite directions: subtract, and the larger force decides the direction."], "y": "35 − 20 = 15 N, in the direction of the larger force."},
     {"q": "Two equal forces of {10} N pull a rope in opposite directions. What is the resultant?", "r": "0 N", "w": ["20 N", "10 N", "5 N"],
      "e": ["They act in opposite directions: subtract.", "Each force cancels the other.", "Opposite equal forces cancel completely."], "y": "Equal and opposite forces are balanced: no resultant."},
     {"q": "A {50} N push forward and {50} N friction act on a cart. The cart…", "r": "has no resultant force", "w": ["has a resultant of 100 N", "has a resultant of 50 N forward", "has a resultant of 50 N backward"],
      "e": ["Friction acts in the opposite direction: subtract.", "Friction cancels the push.", "The push and friction are equal."], "y": "Equal and opposite forces balance."}], SRC),
   num("p3-2-right", 3, "Forces of {a} N (east) and {b} N (north) act on the same point. Find the size of the resultant force (N).", "c",
       ["The forces are at right angles: use Pythagoras.", "R² = {a}² + {b}² = {a * a} + {b * b} = {c * c}.", "R = {answer} N."],
       vars={"i": {"pick": [0, 1, 2, 3, 4]}, "T": {"expr": "triple(i)"}, "k": {"int": [1, 3]}, "a": {"expr": "T[0] * k"}, "b": {"expr": "T[1] * k"}, "c": {"expr": "T[2] * k"}},
       misc=[("add", "a + b", "At right angles the forces do not simply add: use Pythagoras."), ("sub", "b - a", "At right angles use Pythagoras: R² = a² + b².")],
       unit="N", sources=SRC)],
  learn=learn(
    [("Size only, or size and direction?",
      "Some quantities are fully described by a number and a unit: a mass of {50} kg, a time of {12} s, a temperature of {30} °C. These are scalars.\n"
      "Others also need a direction: a force of {20} N to the left, a displacement of {3} km north. These are vectors.\n"
      "Weight is a vector: it is a force and it always acts downwards, towards the centre of the Earth."),
     ("Measuring force",
      "A newton meter (spring balance) has a spring that stretches when you pull it; the scale shows the force in newtons (N).\n"
      "A beam balance compares an unknown mass with known masses. It gives mass, not force, so it reads the same on the Moon.\n"
      "In the laboratory, handle these instruments gently: overloading a spring damages it."),
     ("Adding forces",
      "Forces on the same line combine simply:\n• same direction: add them ({6} N + {4} N = {10} N);\n• opposite directions: subtract, and the resultant acts in the direction of the larger force ({6} N east and {4} N west give {2} N east).\n"
      "Forces at right angles combine like the sides of a right-angled triangle: {3} N east and {4} N north give a resultant of {5} N.")],
    key_words=[("scalar", "a quantity with size only"), ("vector", "a quantity with size and direction"),
               ("resultant", "the single force with the same effect as several forces"), ("newton (N)", "the unit of force")],
    examples=["Scalars: mass, time, speed, energy", "Vectors: force, weight, velocity, displacement", "{8} N and {8} N in opposite directions: resultant {0} N"],
    mistake=("{6} N east and {4} N west give {10} N", "They give {2} N east",
             "Forces in opposite directions work against each other: subtract them.")))

# ---------------------------------------------------------------- 3. Mass and weight, safety
SRC = ["forces"]
L.lesson(D, S, 3, ("p3-3", "Mass and weight; safety in the laboratory"), [2],
  "Mass is the amount of matter in a body; it is measured in kg with a balance and does not change from place to place.\n"
  "Weight is the force of gravity on the body; it is measured in N with a newton meter and depends on the gravitational field strength g.\n"
  "W = m × g. On Earth g ≈ 10 N/kg; on the Moon g ≈ 1.6 N/kg.\n"
  "Safety: follow the teacher's instructions, wear goggles when needed, never taste chemicals, report breakages, keep the bench tidy, do not overload springs or balances.",
  worked({"m": 45, "g": 10},
         "Ngozi has a mass of {m} kg. Find her weight on Earth (g = {g} N/kg).",
         ["W = m × g.", "W = {m} × {g} = {weight(m, g)} N."], "{weight(m, g)} N", checks=["weight(m, g) == 450"]),
  [card("c3p3-1", "Weight = mass × g; on Earth g = {10} N/kg.",
        ["{5} kg weighs {5} × {10} = {50} N."], "p3-3-w"),
   card("c3p3-2", "Mass stays the same everywhere; weight changes with g.",
        ["On the Moon the same {5} kg weighs only {8} N."], "p3-3-diff"),
   card("c3p3-3", "Safety first: follow instructions and report accidents at once.",
        ["Never taste or smell chemicals directly."], "p3-3-safe")],
  [num("p3-3-w", 1, "Find the weight of a {m} kg bag of rice on Earth (g = {10} N/kg).", "weight(m)",
       ["W = m × g = {m} × {10}.", "W = {answer} N."],
       vars={"m": {"int": [2, 60]}},
       misc=[("same", "m", "{m} kg is the mass. Weight is a force: multiply by g = {10} N/kg."), ("div", "m / 10", "Multiply by g, do not divide.")],
       unit="N", sources=SRC),
   bank("p3-3-diff", 1, "{X.q}", [
     {"q": "Which statement about mass is true?", "r": "It is the same on the Earth and on the Moon", "w": ["It is measured in newtons", "It is smaller on the Moon", "It is measured with a newton meter"],
      "e": ["Mass is measured in kilograms.", "The amount of matter does not change.", "A newton meter measures force (weight)."], "y": "Mass is the amount of matter: it does not depend on place."},
     {"q": "Which statement about weight is true?", "r": "It is a force measured in newtons", "w": ["It is measured in kilograms", "It is the same everywhere", "It is a scalar"],
      "e": ["Kilograms measure mass.", "Weight depends on g, which changes from place to place.", "Weight has a direction (down): it is a vector."], "y": "Weight is the pull of gravity, a force."},
     {"q": "An astronaut goes to the Moon. What happens?", "r": "Her weight decreases but her mass stays the same", "w": ["Her mass decreases but her weight stays the same", "Both decrease", "Both stay the same"],
      "e": ["Mass does not change with place.", "Mass does not change with place.", "Weight changes because g is smaller on the Moon."], "y": "g is smaller on the Moon, so W = mg is smaller; m is unchanged."}], SRC),
   num("p3-3-grams", 2, "A tin of tomato paste has a mass of {m} g. Find its weight on Earth (N).", "weight(m / 1000)",
       ["Change the mass to kilograms: {m} g = {m / 1000} kg.", "W = {m / 1000} × {10} = {answer} N."],
       vars={"m": {"int": [100, 900], "step": 50}},
       misc=[("nog", "m * 10", "Change grams to kilograms first: divide by {1000}."), ("mass", "m / 1000", "That is the mass in kg. Multiply by g = {10} N/kg.")],
       unit="N", sources=SRC),
   num("p3-3-moon", 2, "A rock has a mass of {m} kg. What is its weight on the Moon, where g = {1.6} N/kg?", "weight(m, 1.6)",
       ["W = m × g = {m} × {1.6}.", "W = {answer} N."],
       vars={"m": {"int": [2, 50]}},
       misc=[("earth", "weight(m)", "That is its weight on Earth. On the Moon g = {1.6} N/kg."), ("div", "m / 1.6", "Multiply the mass by g, do not divide.")],
       unit="N", sources=SRC),
   bank("p3-3-safe", 3, "{X.q}", [
     {"q": "A thermometer breaks and mercury spills on the bench. What should you do first?", "r": "Tell the teacher at once and keep away from the mercury", "w": ["Pick up the mercury with your fingers", "Wipe it into the sink with water", "Carry on with the experiment"],
      "e": ["Mercury is poisonous: never touch it.", "Mercury must not go down the drain.", "Spills must be reported straight away."], "y": "Report accidents immediately; some substances are dangerous."},
     {"q": "Which is a safe practice in the laboratory?", "r": "Wearing goggles when heating liquids", "w": ["Tasting a solution to identify it", "Running between benches", "Hanging a heavy load on a small spring balance"],
      "e": ["Never taste chemicals.", "Running causes accidents.", "Overloading damages the spring and the load may fall."], "y": "Goggles protect your eyes from splashes."},
     {"q": "Why must you not overload a spring balance?", "r": "The spring can be stretched past its limit and be damaged", "w": ["It makes the reading in kilograms", "It changes the value of g", "It makes the spring lighter"],
      "e": ["A spring balance reads newtons.", "g depends on the planet, not on the balance.", "Mass of the spring does not change."], "y": "Beyond its elastic limit a spring does not return to its shape."}], SRC)],
  learn=learn(
    [("Mass: how much matter",
      "Mass measures how much matter is in a body. A {50} kg bag of cement has the same mass in Douala, on Mount Cameroon or on the Moon.\n"
      "Its SI unit is the kilogram (kg), and it is measured with a balance (beam balance, electronic balance)."),
     ("Weight: the pull of gravity",
      "Weight is the force with which gravity pulls a body towards the Earth. Being a force, it is measured in newtons (N) with a newton meter.\n"
      "Weight = mass × gravitational field strength: W = mg. On Earth g ≈ {10} N/kg, so a {5} kg mass weighs {50} N.\n"
      "On the Moon g ≈ {1.6} N/kg, so the same mass weighs only {8} N. That is why astronauts can jump so high there."),
     ("Working safely",
      "Physics practicals use glassware, heaters, springs and electricity.\n"
      "• Follow the teacher's instructions and read the steps first.\n• Wear goggles when heating or when something can splash.\n"
      "• Never taste or directly smell chemicals.\n• Report breakages and spills at once (mercury is poisonous).\n• Do not overload springs and balances; keep the bench tidy.")],
    key_words=[("mass", "the amount of matter in a body (kg)"), ("weight", "the force of gravity on a body (N)"),
               ("gravitational field strength", "g, the weight of each kilogram ({10} N/kg on Earth)")],
    examples=["{2} kg of sugar weighs {20} N on Earth", "{600} g weighs {6} N", "{60} kg on the Moon weighs {96} N"],
    mistake=("\"My weight is {55} kg\"", "\"My mass is {55} kg; my weight is {550} N\"",
             "Kilograms measure mass. Weight is a force, measured in newtons.")))

# ---------------------------------------------------------------- 4. Measuring mass
SRC = ["measurement"]
L.lesson(D, S, 4, ("p3-4", "Measure mass and convert between units of mass"), [3],
  "Mass is measured with a beam balance, a lever arm balance or an electronic (top-pan) balance.\n"
  "Before weighing, check the balance reads zero (adjust or press 'tare').\n"
  "Units: 1 t = 1000 kg, 1 kg = 1000 g, 1 g = 1000 mg.\n"
  "Mass of a liquid by difference: weigh the empty container, then container + liquid, and subtract.",
  worked({"e": 85, "f": 233},
         "An empty beaker has a mass of {e} g. With some palm oil in it, the mass is {f} g. Find the mass of the oil.",
         ["Mass of oil = (beaker + oil) − beaker.", "= {f} − {e} = {f - e} g."], "{f - e} g", checks=["f - e == 148"]),
  [card("c3p4-1", "Zero the balance first, then read the mass.",
        ["An electronic balance with a beaker on it: press tare to read {0}."], "p3-4-tool"),
   card("c3p4-2", "Convert: {1} kg = {1000} g; {1} t = {1000} kg.",
        ["{2.5} kg = {2500} g"], "p3-4-conv"),
   card("c3p4-3", "Mass of a liquid = (container + liquid) − empty container.",
        ["{250} g − {90} g = {160} g"], "p3-4-diff")],
  [bank("p3-4-tool", 1, "{X.q}", [
     {"q": "Before weighing on an electronic balance, what should you do?", "r": "Check that it reads zero (tare it)", "w": ["Put the object on it first", "Shake it", "Add a known mass"],
      "e": ["Zero the balance before adding the object.", "Shaking gives false readings.", "That would add to the reading."], "y": "A balance that does not start at zero gives a zero error."},
     {"q": "Which instrument is used to measure mass in the laboratory?", "r": "a beam balance", "w": ["a newton meter", "a measuring cylinder", "a vernier caliper"],
      "e": ["A newton meter measures force.", "A measuring cylinder measures volume.", "Calipers measure length."], "y": "Balances measure mass."},
     {"q": "A balance reads {5} g with nothing on it. What is this called?", "r": "a zero error", "w": ["the mass of the air", "the tare", "a parallax error"],
      "e": ["The balance should read {0} with nothing on it.", "Taring is how you remove the error.", "Parallax is about reading a scale from the side."], "y": "Subtract {5} g from every reading, or tare the balance."}], SRC),
   num("p3-4-conv", 1, "Convert {v} {X.f} to {X.t}.", "convertUnit(v, X.f, X.t)",
       ["{1} {X.f} = {factor(X.f, X.t)} {X.t}.", "{v} {X.f} = {answer} {X.t}."],
       vars={"v": {"int": [2, 90]}, "X": {"pick": [{"f": "kg", "t": "g"}, {"f": "g", "t": "kg"}, {"f": "t", "t": "kg"}, {"f": "kg", "t": "t"}, {"f": "g", "t": "mg"}, {"f": "mg", "t": "g"}]}},
       misc=[("flip", "convertUnit(v, X.t, X.f)", "Check the direction: {1} {X.f} = {factor(X.f, X.t)} {X.t}.")],
       sources=SRC),
   num("p3-4-sum", 2, "A trader at Bonaberi market has a {a} kg bag of beans and a {b} g packet. Find the total mass in kilograms.", "a + b / 1000",
       ["Change to the same unit: {b} g = {b / 1000} kg.", "Total = {a} + {b / 1000} = {answer} kg."],
       vars={"a": {"int": [2, 50]}, "b": {"int": [100, 950], "step": 50}},
       misc=[("nounit", "a + b", "Grams and kilograms cannot be added directly: change {b} g to kg first.")],
       unit="kg", sources=SRC),
   num("p3-4-diff", 2, "An empty bottle has a mass of {e} g. Filled with water, its mass is {e + w} g. Find the mass of the water (g).", "w",
       ["Mass of water = (bottle + water) − bottle.", "= {e + w} − {e} = {answer} g."],
       vars={"e": {"int": [150, 400]}, "w": {"int": [200, 1000], "step": 10}},
       misc=[("add", "2 * e + w", "Subtract the empty bottle, do not add it.")],
       unit="g", sources=SRC),
   num("p3-4-zero", 3, "A balance has a zero error of +{z} g (it reads {z} g with nothing on it). A bag of salt reads {r} g. What is its true mass (g)?", "r - z",
       ["The balance reads {z} g too much.", "True mass = {r} − {z} = {answer} g."],
       vars={"z": {"int": [2, 15]}, "r": {"int": [150, 900]}},
       misc=[("add", "r + z", "The balance reads too much: subtract the zero error.")],
       unit="g", sources=SRC)],
  learn=learn(
    [("Balances",
      "In the laboratory, mass is measured with a balance. A beam balance compares the object with standard masses; an electronic (top-pan) balance shows the mass directly.\n"
      "Always check the reading is {0} before you start. If it shows, say, {3} g with nothing on it, the balance has a zero error: press 'tare' or subtract {3} g from every reading."),
     ("Units of mass",
      "• {1} tonne (t) = {1000} kg\n• {1} kg = {1000} g\n• {1} g = {1000} mg\n"
      "A lorry of cocoa might carry {10} t; a bag of rice {50} kg; a packet of seasoning {10} g.\n"
      "To add masses, first change them to the same unit: {2} kg + {500} g = {2.5} kg."),
     ("Mass by difference",
      "A liquid has to be weighed in a container. Weigh the empty container, then the container with the liquid, and subtract:\n"
      "mass of liquid = (container + liquid) − container.\n"
      "If an empty beaker is {85} g and with palm oil it is {233} g, the oil has a mass of {148} g.")],
    key_words=[("balance", "an instrument for measuring mass"), ("tare", "set the balance to zero"), ("zero error", "a reading when nothing is being measured")],
    examples=["{3500} g = {3.5} kg", "{0.25} t = {250} kg", "{750} mg = {0.75} g"],
    mistake=("{2} kg + {300} g = {302} kg", "{2} kg + {0.3} kg = {2.3} kg",
             "Change both to the same unit before adding.")))

# ---------------------------------------------------------------- 5. Measuring volume
SRC = ["measurement"]
L.lesson(D, S, 5, ("p3-5", "Measure the volume of liquids, regular and irregular solids"), [1],
  "Volume is the space an object occupies. SI unit: m³; also cm³ and litres (1 L = 1000 cm³ = 1 dm³; 1 mL = 1 cm³; 1 m³ = 1000 L).\n"
  "• Liquids: measuring cylinder, burette, pipette. Read at the bottom of the meniscus with the eye level with it.\n"
  "• Regular solids: calculate (cuboid: l × w × h; cylinder: πr²h).\n"
  "• Irregular solids: displacement. Volume = (reading with the object) − (reading without it), or use an overflow (eureka) can.",
  worked({"b": 42, "a": 58},
         "Water in a measuring cylinder reads {b} mL. A stone is lowered in and the level rises to {a} mL. Find the volume of the stone.",
         ["The stone pushes aside (displaces) its own volume of water.", "Volume = {a} − {b} = {a - b} mL = {a - b} cm³."],
         "{a - b} cm³", checks=["a - b == 16"], figure="displacement(b, a)"),
  [card("c3p5-1", "Read a measuring cylinder at the bottom of the meniscus, eye level with it.",
        ["Each small mark is {2} mL on a {100} mL cylinder."], "p3-5-read"),
   card("c3p5-2", "Volume of a cuboid = length × width × height.",
        ["{5} cm × {4} cm × {2} cm = {40} cm³"], "p3-5-box"),
   card("c3p5-3", "Volume of an irregular solid = rise in the water level.",
        ["{50} mL → {65} mL: the stone is {15} cm³."], "p3-5-disp")],
  [num("p3-5-read", 1, "How much water is in the measuring cylinder (mL)?", "2 * v",
       ["Each small mark is {2} mL.", "The bottom of the meniscus is at {answer} mL."],
       vars={"v": {"int": [6, 48]}},
       misc=[("top", "2 * v + 2", "Read at the bottom of the curved surface, not at the edges.")],
       unit="mL", figure="cylinder(2 * v)", sources=SRC),
   num("p3-5-box", 1, "A wooden block is {l} cm long, {w} cm wide and {h} cm high. Find its volume (cm³).", "l * w * h",
       ["V = l × w × h.", "V = {l} × {w} × {h} = {answer} cm³."],
       vars={"l": {"int": [3, 15]}, "w": {"int": [2, 10]}, "h": {"int": [2, 8]}},
       misc=[("add", "l + w + h", "Volume multiplies the three measurements."), ("area", "l * w", "That is the area of the base. Multiply by the height too.")],
       unit="cm³", sources=SRC),
   num("p3-5-disp", 2, "What is the volume of the stone (cm³)?", "2 * d",
       ["Volume of stone = rise in the water level.", "{2 * b + 2 * d} − {2 * b} = {answer} mL = {answer} cm³."],
       vars={"b": {"int": [15, 30]}, "d": {"int": [3, 15]}},
       misc=[("after", "2 * b + 2 * d", "That is the reading with the stone. Subtract the reading before.")],
       unit="cm³", figure="displacement(2 * b, 2 * b + 2 * d)", sources=SRC),
   num("p3-5-conv", 2, "Convert {v} {X.f} to {X.t}.", "convertUnit(v, X.f, X.t)",
       ["{1} {X.f} = {factor(X.f, X.t)} {X.t}.", "{v} {X.f} = {answer} {X.t}."],
       vars={"v": {"int": [2, 90]}, "X": {"pick": [{"f": "L", "t": "cm³"}, {"f": "cm³", "t": "L"}, {"f": "m³", "t": "L"}, {"f": "mL", "t": "L"}, {"f": "L", "t": "mL"}]}},
       misc=[("flip", "convertUnit(v, X.t, X.f)", "Check the direction: {1} {X.f} = {factor(X.f, X.t)} {X.t}.")],
       sources=SRC),
   num("p3-5-cyl", 3, "A cylindrical water tank has radius {r} m and height {h} m. Find its volume in litres (π = {3.14}).", "roundTo(3.14 * r * r * h * 1000, 1)",
       ["V = πr²h = {3.14} × {r}² × {h} = {roundTo(3.14 * r * r * h, 0.001)} m³.", "{1} m³ = {1000} L, so V = {answer} L."],
       vars={"r": {"pick": [0.5, 1, 1.5, 2]}, "h": {"int": [1, 3]}},
       misc=[("m3", "roundTo(3.14 * r * r * h, 0.001)", "That is in m³. Multiply by {1000} for litres."), ("nosq", "roundTo(3.14 * r * h * 1000, 1)", "Square the radius: r² = {r * r}.")],
       unit="L", sources=SRC)],
  learn=learn(
    [("Volume and its units",
      "Volume is the amount of space something takes up. The SI unit is the cubic metre (m³), but for small amounts we use cm³ and litres.\n"
      "• {1} L = {1000} cm³ = {1} dm³\n• {1} mL = {1} cm³\n• {1} m³ = {1000} L\n"
      "A water tank at home may hold {1000} L, which is {1} m³."),
     ("Reading a measuring cylinder",
      "Water in a narrow tube curves at the surface: this curve is the meniscus. Read the scale at the bottom of the meniscus, with your eye level with it.\n"
      "Looking from above or below gives a wrong reading (parallax error).\n"
      "First work out what each small mark is worth: on a {100} mL cylinder with ten small marks between labels, each mark is {1} mL or {2} mL.", "cylinder(46)"),
     ("Regular and irregular solids",
      "For a regular shape, measure and calculate: a cuboid is length × width × height.\n"
      "For an irregular shape like a stone, use displacement. Read the water level, lower the stone in gently on a thread, and read again. The rise in level is the volume of the stone.\n"
      "For a large stone use an overflow (eureka) can and measure the water that overflows.")],
    key_words=[("volume", "the space an object takes up"), ("meniscus", "the curved surface of a liquid in a tube"),
               ("displacement", "the liquid pushed aside by an object put into it"), ("parallax error", "a wrong reading from looking at a scale from the side")],
    examples=["{2.5} L = {2500} cm³", "Cuboid {10} cm × {5} cm × {4} cm = {200} cm³", "Water {40} mL → {52} mL: stone {12} cm³"],
    mistake=("Stone: water rises from {40} mL to {52} mL, so the stone is {52} cm³", "The stone is {52} − {40} = {12} cm³",
             "Only the rise in level is due to the stone.")))
