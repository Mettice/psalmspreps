"""Form 3 Physics, Term 1, rows 6-9 (temperature and time, density). Run: python tools/authoring/form3/physics_a2.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "physics", "physics"

# ---------------------------------------------------------------- 6. Temperature and time
SRC = ["measurement"]
L.lesson(D, S, 6, ("p3-6", "Measure temperature and time"), [1],
  "Temperature tells how hot or cold a body is. It is measured with a thermometer, in degrees Celsius (°C) or in kelvin (K).\n"
  "• T(K) = T(°C) + 273. Water freezes at 0 °C (273 K) and boils at 100 °C (373 K) at normal pressure.\n"
  "• Laboratory thermometers use mercury or coloured alcohol; a clinical thermometer reads body temperature (about 37 °C).\n"
  "Time is measured with clocks and stopwatches. SI unit: the second. 1 min = 60 s, 1 h = 3600 s.\n"
  "To time something short (a swing of a pendulum), time many swings and divide: period = total time ÷ number of swings.",
  worked({"n": 20, "t": 32},
         "A pendulum makes {n} complete swings in {t} s. Find its period.",
         ["Period = time for one swing = total time ÷ number of swings.", "= {t} ÷ {n} = {t / n} s."],
         "{t / n} s", checks=["t / n == 1.6"]),
  [card("c3p6-1", "Read a thermometer where the liquid ends, eye level with the scale.",
        ["Each small mark on a {0}–{50} °C scale is {1} °C."], "p3-6-read"),
   card("c3p6-2", "Kelvin = degrees Celsius + {273}.",
        ["{27} °C = {300} K"], "p3-6-k"),
   card("c3p6-3", "Time many swings and divide to find one swing.",
        ["{10} swings in {15} s: one swing takes {1.5} s."], "p3-6-period")],
  [num("p3-6-read", 1, "What temperature does the thermometer show (°C)?", "t",
       ["Each small mark is {1} °C.", "The liquid ends at {answer} °C."],
       vars={"t": {"int": [12, 46]}},
       misc=[("next", "t + 1", "Read where the liquid ends, not the next mark.")],
       unit="°C", figure="thermometer(t)", sources=SRC),
   num("p3-6-k", 1, "Convert {c} °C to kelvin.", "toKelvin(c)",
       ["T(K) = T(°C) + {273}.", "{c} + {273} = {answer} K."],
       vars={"c": {"int": [-20, 100]}},
       misc=[("sub", "c - 273", "Add {273} to change °C to kelvin.")],
       unit="K", sources=SRC),
   num("p3-6-c", 2, "Convert {k} K to degrees Celsius.", "toCelsius(k)",
       ["T(°C) = T(K) − {273}.", "{k} − {273} = {answer} °C."],
       vars={"k": {"int": [250, 400]}},
       misc=[("add", "k + 273", "Subtract {273} to change kelvin to °C.")],
       unit="°C", sources=SRC, signed=True),
   num("p3-6-time", 2, "A race lasted {m} min {s} s. How many seconds is that?", "60 * m + s",
       ["{1} min = {60} s, so {m} min = {60 * m} s.", "{60 * m} + {s} = {answer} s."],
       vars={"m": {"int": [1, 12]}, "s": {"int": [5, 55]}},
       misc=[("hundred", "100 * m + s", "A minute is {60} s, not {100} s.")],
       unit="s", sources=SRC),
   num("p3-6-period", 3, "Bih times {n} swings of a pendulum three times: {t1} s, {t2} s and {t3} s. Find the period, using the mean time (s).", "roundTo((t1 + t2 + t3) / 3 / n, 0.01)",
       ["Mean time = ({t1} + {t2} + {t3}) ÷ {3} = {roundTo((t1 + t2 + t3) / 3, 0.01)} s.", "Period = mean ÷ {n} = {answer} s."],
       vars={"n": {"pick": [10, 20]}, "base": {"int": [12, 30]}, "t1": {"expr": "base + 0.2"}, "t2": {"expr": "base + 0.4"}, "t3": {"expr": "base"}},
       misc=[("mean", "roundTo((t1 + t2 + t3) / 3, 0.01)", "That is the time for {n} swings. Divide by {n} for one swing."),
             ("sum", "roundTo((t1 + t2 + t3) / n, 0.01)", "Find the mean of the three timings first (divide by {3}).")],
       unit="s", sources=SRC)],
  learn=learn(
    [("Thermometers",
      "A liquid-in-glass thermometer has a bulb of mercury or coloured alcohol. When it warms, the liquid expands up the narrow tube; the scale shows the temperature.\n"
      "Read it where the liquid ends, with your eye level with that point. Wait until the level stops moving.\n"
      "A clinical thermometer has a narrow kink so the reading stays after you take it out of the mouth; it reads about {35} °C to {42} °C.", "thermometer(28)"),
     ("Celsius and kelvin",
      "Two temperature scales are used:\n• Celsius: water freezes at {0} °C and boils at {100} °C.\n• Kelvin (SI): T(K) = T(°C) + {273}.\n"
      "So {0} °C = {273} K and {100} °C = {373} K. A hot day in Garoua at {40} °C is {313} K. There are no negative temperatures on the kelvin scale."),
     ("Measuring time",
      "Time is measured with clocks, watches and stopwatches; the SI unit is the second. {1} min = {60} s and {1} h = {3600} s.\n"
      "Your reaction time when starting and stopping a stopwatch adds an error. To reduce it, time many events and divide.\n"
      "For a pendulum, time {20} swings and divide by {20}; repeat three times and take the mean.")],
    key_words=[("temperature", "how hot or cold something is"), ("kelvin", "the SI unit of temperature: K = °C + {273}"),
               ("period", "the time for one complete swing")],
    examples=["{37} °C = {310} K", "{2} min {15} s = {135} s", "{20} swings in {30} s: period {1.5} s"],
    mistake=("{300} K = {300} + {273} = {573} °C", "{300} K = {300} − {273} = {27} °C",
             "To go from kelvin to Celsius, subtract {273}.")))

# ---------------------------------------------------------------- 7. Density
SRC = ["density"]
L.lesson(D, S, 7, ("p3-7", "Density: definition, calculation, units; density of a liquid"), [4, 5],
  "Density is mass per unit volume: ρ = m ÷ V.\n"
  "• Units: kg/m³ (SI) or g/cm³. 1 g/cm³ = 1000 kg/m³. Water: 1 g/cm³ = 1000 kg/m³.\n"
  "• Rearranged: m = ρV and V = m ÷ ρ.\n"
  "• A solid floats in a liquid if its density is less than that of the liquid.\n"
  "Density of a liquid: measure a volume in a measuring cylinder, find its mass by difference on a balance, then divide.",
  worked({"m": 540, "V": 200},
         "A block of aluminium has a mass of {m} g and a volume of {V} cm³. Find its density in g/cm³ and in kg/m³.",
         ["ρ = m ÷ V = {m} ÷ {V} = {m / V} g/cm³.", "{1} g/cm³ = {1000} kg/m³, so ρ = {m / V * 1000} kg/m³."],
         "{m / V} g/cm³ = {m / V * 1000} kg/m³", checks=["m / V == 2.7"]),
  [card("c3p7-1", "Density = mass ÷ volume.",
        ["{60} g in {20} cm³: ρ = {3} g/cm³"], "p3-7-rho"),
   card("c3p7-2", "Mass = density × volume.",
        ["ρ = {8} g/cm³, V = {10} cm³: m = {80} g"], "p3-7-m"),
   card("c3p7-3", "{1} g/cm³ = {1000} kg/m³.",
        ["Water: {1} g/cm³ = {1000} kg/m³"], "p3-7-conv")],
  [num("p3-7-rho", 1, "A stone has mass {m} g and volume {V} cm³. Find its density (g/cm³).", "density(m, V)",
       ["ρ = m ÷ V = {m} ÷ {V}.", "ρ = {answer} g/cm³."],
       vars={"V": {"int": [5, 40]}, "k": {"int": [12, 90]}, "m": {"expr": "V * k / 10"}},
       misc=[("flip", "density(V, m)", "Density is mass ÷ volume, not volume ÷ mass."), ("times", "m * V", "Divide mass by volume.")],
       unit="g/cm³", sources=SRC),
   num("p3-7-m", 1, "Cooking oil has a density of {r} g/cm³. Find the mass of {V} cm³ of it (g).", "roundTo(r * V, 0.01)",
       ["m = ρ × V = {r} × {V}.", "m = {answer} g."],
       vars={"r": {"pick": [0.8, 0.9, 0.92]}, "V": {"int": [50, 500], "step": 50}},
       misc=[("div", "roundTo(V / r, 0.01)", "Mass = density × volume: multiply.")],
       unit="g", sources=SRC),
   num("p3-7-conv", 2, "Convert a density of {r} g/cm³ to kg/m³.", "r * 1000",
       ["{1} g/cm³ = {1000} kg/m³.", "{r} × {1000} = {answer} kg/m³."],
       vars={"k": {"int": [5, 200]}, "r": {"expr": "k / 10"}},
       misc=[("div", "r / 1000", "kg/m³ numbers are larger: multiply by {1000}.")],
       unit="kg/m³", sources=SRC),
   num("p3-7-liquid", 2, "An empty measuring cylinder has mass {e} g. With {V} cm³ of a liquid it has mass {e + m} g. Find the density of the liquid (g/cm³).", "density(m, V)",
       ["Mass of liquid = {e + m} − {e} = {m} g.", "ρ = {m} ÷ {V} = {answer} g/cm³."],
       vars={"e": {"int": [80, 200]}, "V": {"pick": [50, 100, 200]}, "k": {"int": [7, 14]}, "m": {"expr": "V * k / 10"}},
       misc=[("total", "density(e + m, V)", "Subtract the empty cylinder first: only the liquid's mass counts.")],
       unit="g/cm³", sources=SRC),
   mcq("p3-7-float", 3, "A solid has mass {m} g and volume {V} cm³. Will it float or sink in water (density {1} g/cm³)?",
       "{m / V < 1 ? 'Float: its density is ' + fmt(density(m, V)) + ' g/cm³, less than water' : 'Sink: its density is ' + fmt(density(m, V)) + ' g/cm³, more than water'}",
       [("{m / V < 1 ? 'Sink: its density is ' + fmt(density(m, V)) + ' g/cm³, more than water' : 'Float: its density is ' + fmt(density(m, V)) + ' g/cm³, less than water'}", "flip"),
        ("{m > 100 ? 'Sink: it is heavy' : 'Float: it is light'}", "heavy"), ("{'Float: all solids float in water'}", "all")],
       ["ρ = {m} ÷ {V} = {density(m, V)} g/cm³.", "Compare with water ({1} g/cm³): {answer}."],
       vars={"V": {"int": [20, 200], "step": 10}, "k": {"pick": [4, 6, 7, 8, 9, 12, 15, 19, 27]}, "m": {"expr": "V * k / 10"}},
       misc=[("flip", "Compare carefully: {density(m, V)} is {m / V < 1 ? 'less' : 'more'} than {1}."),
             ("heavy", "Floating depends on density, not on mass alone: a heavy log of wood floats."), ("all", "A solid denser than water (like a stone) sinks.")],
       sources=SRC, where=["(m > 100) == (m / V < 1)"])],
  learn=learn(
    [("Heavy for its size",
      "A small iron nail sinks but a large log floats. The log has more mass, but it is less dense: each cubic centimetre of wood has less mass than a cubic centimetre of iron.\n"
      "Density is mass per unit volume: ρ = m ÷ V (ρ is the Greek letter rho)."),
     ("Units and rearranging",
      "Units: g/cm³ or, in SI, kg/m³. Since {1} g/cm³ = {1000} kg/m³, water has density {1} g/cm³ = {1000} kg/m³.\n"
      "• m = ρV: {200} cm³ of oil of density {0.9} g/cm³ has a mass of {180} g.\n• V = m ÷ ρ.\n"
      "Typical densities (g/cm³): cork {0.25}, wood {0.6}, palm oil {0.9}, water {1}, aluminium {2.7}, iron {7.9}, mercury {13.6}."),
     ("Density of a liquid",
      "• Find the mass of an empty measuring cylinder.\n• Pour in some liquid and read its volume.\n• Find the new mass; subtract to get the mass of the liquid.\n"
      "• Divide: ρ = m ÷ V.\n"
      "Objects float in a liquid if they are less dense than it: that is why oil floats on water.")],
    key_words=[("density", "mass per unit volume, ρ = m ÷ V"), ("kg/m³", "the SI unit of density"), ("float", "stay on the surface: less dense than the liquid")],
    examples=["{60} g in {20} cm³: {3} g/cm³", "{2.7} g/cm³ = {2700} kg/m³", "Cork ({0.25} g/cm³) floats on water"],
    mistake=("ρ = V ÷ m", "ρ = m ÷ V",
             "Density is mass per unit volume: mass on top, volume underneath.")))

# ---------------------------------------------------------------- 8. Density experiments
SRC = ["density"]
L.lesson(D, S, 8, ("p3-8", "Measure the density of regular and irregular solids"), [7],
  "Regular solid: measure its sides with a ruler (or vernier calipers), calculate the volume, find its mass on a balance, then ρ = m ÷ V.\n"
  "Irregular solid: find its mass on a balance; find its volume by displacement (measuring cylinder or overflow can); then ρ = m ÷ V.\n"
  "Sources of error: air bubbles on the stone, splashing, reading the meniscus from the side, water clinging to the stone if weighed after.\n"
  "Weigh the solid before putting it in water.",
  worked({"m": 78, "b": 50, "a": 60},
         "A stone has mass {m} g. Water in a measuring cylinder rises from {b} mL to {a} mL when the stone is put in. Find the density of the stone.",
         ["Volume = {a} − {b} = {a - b} cm³.", "ρ = m ÷ V = {m} ÷ {a - b} = {m / (a - b)} g/cm³."],
         "{m / (a - b)} g/cm³", checks=["m / (a - b) == 7.8"], figure="displacement(b, a)"),
  [card("c3p8-1", "Regular solid: volume from its measurements, mass from a balance.",
        ["{4} cm × {3} cm × {2} cm = {24} cm³; {48} g → {2} g/cm³"], "p3-8-reg"),
   card("c3p8-2", "Irregular solid: volume by displacement.",
        ["{50} mL → {60} mL: V = {10} cm³"], "p3-8-irr"),
   card("c3p8-3", "Do the steps in a sensible order: weigh first, then put it in water.",
        ["A wet stone gives a wrong mass."], "p3-8-order")],
  [num("p3-8-reg", 1, "A rectangular block is {l} cm × {w} cm × {h} cm and has mass {l * w * h * k / 10} g. Find its density (g/cm³).", "k / 10",
       ["V = {l} × {w} × {h} = {l * w * h} cm³.", "ρ = {l * w * h * k / 10} ÷ {l * w * h} = {answer} g/cm³."],
       vars={"l": {"int": [2, 8]}, "w": {"int": [2, 6]}, "h": {"int": [2, 5]}, "k": {"int": [5, 90]}},
       misc=[("nov", "l * w * h * k / 10", "That is the mass. Divide it by the volume."), ("area", "roundTo(l * w * h * k / 10 / (l * w), 0.01)", "Use the volume (l × w × h), not the area of one face.")],
       unit="g/cm³", sources=SRC),
   num("p3-8-irr", 2, "A stone of mass {m} g is lowered into the cylinder shown. Find its density (g/cm³).", "roundTo(m / (2 * d), 0.01)",
       ["Volume = {2 * b + 2 * d} − {2 * b} = {2 * d} cm³.", "ρ = {m} ÷ {2 * d} = {answer} g/cm³."],
       vars={"b": {"int": [15, 30]}, "d": {"int": [4, 12]}, "k": {"int": [20, 40]}, "m": {"expr": "2 * d * k / 10"}},
       misc=[("level", "roundTo(m / (2 * b + 2 * d), 0.01)", "Use the rise in level, not the final reading, as the volume.")],
       unit="g/cm³", figure="displacement(2 * b, 2 * b + 2 * d)", sources=SRC),
   num("p3-8-vol", 2, "A brass key has a density of {r} g/cm³ and a mass of {r * V} g. What volume of water will it displace (cm³)?", "V",
       ["V = m ÷ ρ.", "V = {r * V} ÷ {r} = {answer} cm³."],
       vars={"r": {"pick": [8, 8.5]}, "V": {"int": [2, 12]}},
       misc=[("times", "r * r * V", "Volume = mass ÷ density: divide.")],
       unit="cm³", sources=SRC),
   order("p3-8-order", 1, "Put the steps for finding the density of a stone in order.",
         ["Find the mass of the dry stone on a balance.", "Pour water into a measuring cylinder and read the volume.",
          "Lower the stone in gently on a thread and read the new volume.", "Subtract the readings to get the volume of the stone.", "Divide the mass by the volume."],
         hint="Weigh the stone while it is still dry.", sources=SRC, review="authored"),
   num("p3-8-eureka", 3, "A stone of mass {m} g is lowered into a full overflow can. The water that overflows has mass {v} g. Find the density of the stone (g/cm³).", "roundTo(m / v, 0.01)",
       ["The overflow water has the same volume as the stone. Water has {1} g in each cm³, so V = {v} cm³.", "ρ = {m} ÷ {v} = {answer} g/cm³."],
       vars={"v": {"int": [20, 80]}, "k": {"int": [20, 35]}, "m": {"expr": "roundTo(v * k / 10, 1)"}},
       misc=[("flip", "roundTo(v / m, 0.01)", "Density is the stone's mass divided by its volume.")],
       unit="g/cm³", sources=SRC)],
  learn=learn(
    [("Regular solids",
      "For a block, cube or cylinder, find the volume by measuring and calculating, then weigh it.\n"
      "A block {4} cm × {3} cm × {2} cm has V = {24} cm³. If its mass is {48} g, ρ = {48} ÷ {24} = {2} g/cm³.\n"
      "Measure each side carefully: a small error in a length makes a bigger error in the volume."),
     ("Irregular solids",
      "A stone has no simple shape, so find its volume by displacement:\n• weigh the dry stone first;\n• read the water level in a measuring cylinder;\n"
      "• lower the stone in on a thread and read the new level;\n• the rise is the stone's volume.\n"
      "For a large stone, use an overflow (eureka) can and collect the water that comes out.", "displacement(50, 60)"),
     ("Good practice",
      "• Weigh before wetting the stone.\n• Lower it gently so water does not splash out.\n• Shake off air bubbles: they add to the volume.\n"
      "• Read the meniscus at eye level.\nRepeat and take the mean to reduce errors.")],
    key_words=[("regular solid", "a solid with a simple shape whose volume can be calculated"), ("irregular solid", "a solid with no simple shape"),
               ("overflow (eureka) can", "a can with a spout to collect the water an object displaces")],
    examples=["Brass key {85} g, {10} cm³: {8.5} g/cm³", "Stone {78} g raises water {50} → {60} mL: {7.8} g/cm³"],
    mistake=("Volume of the stone = final reading {60} mL", "Volume = {60} − {50} = {10} cm³",
             "The water was already there; only the rise is due to the stone.")))

# ---------------------------------------------------------------- 9. Applications of density
SRC = ["density"]
L.lesson(D, S, 9, ("p3-9", "Applications of density in engineering and daily life"), [7, 8],
  "Engineers choose materials partly by density:\n"
  "• Aircraft and bicycles: aluminium alloys (low density, strong).\n• Ships: steel hulls are hollow, so the ship's average density is less than water's and it floats.\n"
  "• Hot-air balloons rise because hot air is less dense than cold air.\n• Life jackets use low-density foam.\n"
  "• Builders estimate loads: mass = density × volume (concrete ≈ 2400 kg/m³).\n• Oil spills float on the sea because oil is less dense than water.",
  worked({"l": 3, "w": 2, "h": 0.15, "r": 2400},
         "A concrete slab for a house in Bafoussam is {l} m × {w} m × {h} m. Concrete has density {r} kg/m³. Find its mass.",
         ["V = {l} × {w} × {h} = {roundTo(l * w * h, 0.001)} m³.", "m = ρV = {r} × {roundTo(l * w * h, 0.001)} = {roundTo(r * l * w * h, 1)} kg."],
         "{roundTo(r * l * w * h, 1)} kg", checks=["roundTo(r * l * w * h, 1) == 2160"]),
  [card("c3p9-1", "A ship floats because its average density (steel + air inside) is less than water's.",
        ["A solid steel bar sinks; a hollow steel hull floats."], "p3-9-ship"),
   card("c3p9-2", "Low-density materials keep vehicles light: aluminium for aircraft.",
        ["Aluminium {2.7} g/cm³; steel {7.9} g/cm³"], "p3-9-choose"),
   card("c3p9-3", "Builders use m = ρV to estimate loads.",
        ["{1} m³ of concrete ≈ {2400} kg"], "p3-9-load")],
  [bank("p3-9-ship", 1, "{X.q}", [
     {"q": "Why does a large steel ship float when a steel nail sinks?", "r": "The hollow hull makes the ship's average density less than water's", "w": ["Steel is less dense than water", "The ship is lighter than the nail", "Sea water has no density"],
      "e": ["Steel (7.9 g/cm³) is much denser than water.", "The ship is far heavier than the nail.", "Sea water is slightly denser than fresh water."], "y": "The air inside the hull lowers the average density."},
     {"q": "Why does a hot-air balloon rise?", "r": "Hot air is less dense than the cold air around it", "w": ["Hot air has no mass", "The basket is lighter than air", "Fire pushes the balloon up"],
      "e": ["Hot air still has mass, just less per cubic metre.", "The basket is denser than air; the hot air carries it.", "The flame heats the air; it does not push the balloon."], "y": "Less dense air rises through denser air."},
     {"q": "After an oil spill, the oil spreads on top of the sea. Why?", "r": "Oil is less dense than sea water", "w": ["Oil is denser than sea water", "Oil is a gas", "The wind pushes it up"],
      "e": ["Denser oil would sink.", "Oil is a liquid.", "It floats because of density, even on a calm day."], "y": "Less dense liquids float on denser ones."}], SRC),
   bank("p3-9-choose", 1, "{X.q}", [
     {"q": "Why is aluminium used to make aircraft bodies?", "r": "It is strong and has a low density", "w": ["It is the densest metal", "It is magnetic", "It melts easily"],
      "e": ["A dense metal would make the aircraft too heavy.", "Magnetism is not why it is chosen.", "A low melting point would be a problem, not an advantage."], "y": "Strength with low density keeps the aircraft light."},
     {"q": "Which material is best for a life jacket?", "r": "Foam of very low density", "w": ["Iron", "Concrete", "Lead"],
      "e": ["Iron is very dense: it sinks.", "Concrete sinks.", "Lead is very dense: it sinks."], "y": "A low-density material floats and helps you float."},
     {"q": "Fishermen in Limbe tie lead weights to their nets. Why lead?", "r": "Lead is very dense, so a small piece pulls the net down", "w": ["Lead floats", "Lead is light", "Lead dissolves in water"],
      "e": ["Lead sinks: it is denser than water.", "Lead is very dense.", "Lead does not dissolve; it is chosen for its density."], "y": "High density: a small volume has a large mass."}], SRC),
   num("p3-9-load", 2, "A concrete pillar has a volume of {V} m³. Concrete has a density of {2400} kg/m³. Find its mass (kg).", "roundTo(2400 * V, 1)",
       ["m = ρV = {2400} × {V}.", "m = {answer} kg."],
       vars={"k": {"int": [2, 30]}, "V": {"expr": "k / 10"}},
       misc=[("div", "roundTo(2400 / V, 0.01)", "Mass = density × volume: multiply.")],
       unit="kg", sources=SRC),
   num("p3-9-avg", 2, "A closed hollow tin can has mass {m} g and volume {V} cm³. Find its average density (g/cm³).", "roundTo(m / V, 0.01)",
       ["Average density = total mass ÷ total volume.", "= {m} ÷ {V} = {answer} g/cm³, {m / V < 1 ? 'less than water, so it floats' : 'more than water, so it sinks'}."],
       vars={"V": {"int": [300, 900], "step": 50}, "m": {"int": [60, 400], "step": 20}},
       misc=[("flip", "roundTo(V / m, 0.01)", "Density is mass ÷ volume.")],
       unit="g/cm³", sources=SRC, where=["m < V"]),
   num("p3-9-tank", 3, "A water tank on a roof holds {L} litres. Water has density {1000} kg/m³. What extra mass does the full tank put on the roof (kg)?", "L",
       ["{L} L = {L / 1000} m³.", "m = {1000} × {L / 1000} = {answer} kg (each litre of water has a mass of about {1} kg)."],
       vars={"L": {"int": [500, 3000], "step": 250}},
       misc=[("m3", "L / 1000", "That is the volume in m³. Multiply by the density {1000} kg/m³."), ("big", "L * 1000", "Change litres to m³ first: divide by {1000}.")],
       unit="kg", sources=SRC)],
  learn=learn(
    [("Floating and sinking",
      "An object floats if its average density is less than that of the liquid. A solid steel bar sinks, but a steel ship is mostly air inside, so its average density is less than water's.\n"
      "Hot air is less dense than cold air, so a hot-air balloon rises. Oil is less dense than water, so an oil spill floats on the sea and can be scooped off."),
     ("Choosing materials",
      "• Aircraft, bicycles and car parts: aluminium alloys, strong but light ({2.7} g/cm³ against {7.9} g/cm³ for steel).\n"
      "• Life jackets and floats: foams of very low density.\n• Fishing weights and sinkers: lead, very dense, so a small piece is heavy.\n"
      "• Boats are built so that they float even when loaded."),
     ("Estimating loads",
      "Builders and engineers use m = ρV to know how heavy a structure will be.\n"
      "A concrete slab {3} m × {2} m × {0.15} m has V = {0.9} m³; at {2400} kg/m³ its mass is {2160} kg.\n"
      "A {1000} L water tank on a roof adds about {1000} kg: the roof must be designed for that load.")],
    key_words=[("average density", "total mass ÷ total volume of an object made of several materials"), ("alloy", "a mixture of metals, such as aluminium alloy"),
               ("load", "the weight a structure must support")],
    examples=["Ship: hollow hull floats", "Life jacket: low-density foam", "{2} m³ of concrete ≈ {4800} kg"],
    mistake=("A ship floats because steel is light", "A ship floats because its average density, with the air inside, is less than water's",
             "Steel is much denser than water. The shape of the hull, full of air, makes the difference.")))
