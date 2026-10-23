"""Form 3 Physics, Term 1, rows 10-17 (pressure, elasticity, energy). Run: python tools/authoring/form3/physics_b.py
g = 10 N/kg throughout (TR-P03)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "physics", "physics"

# ---------------------------------------------------------------- 10. Pressure in solids
SRC = ["pressure"]
L.lesson(D, S, 10, ("p3-10", "Pressure: definition, calculation and units; pressure in solids"), [3],
  "Pressure is the force acting normally (at right angles) on unit area: P = F ÷ A.\n"
  "• Unit: the pascal, 1 Pa = 1 N/m². Also N/cm² and kPa (1 kPa = 1000 Pa).\n"
  "• The same force on a smaller area gives a larger pressure; on a larger area, a smaller pressure.\n"
  "• Applications: knives and needles are sharp (small area, high pressure); lorries have many wide tyres, tractors have wide tracks, and building foundations are wide (large area, low pressure).\n"
  "• Change cm² to m² by dividing by 10 000.",
  worked({"F": 600, "A": 0.04},
         "A man weighing {F} N stands on both feet. The total area of his soles is {A} m². Find the pressure on the floor.",
         ["P = F ÷ A.", "P = {F} ÷ {A} = {pressure(F, A)} Pa."], "{pressure(F, A)} Pa", checks=["pressure(F, A) == 15000"]),
  [card("c3p10-1", "Pressure = force ÷ area, in pascals (N/m²).",
        ["{100} N on {2} m²: P = {50} Pa"], "p3-10-p"),
   card("c3p10-2", "A smaller area gives a bigger pressure for the same force.",
        ["A sharp knife cuts because its edge has a tiny area."], "p3-10-app"),
   card("c3p10-3", "Change cm² to m²: divide by {10000}.",
        ["{200} cm² = {0.02} m²"], "p3-10-cm")],
  [num("p3-10-p", 1, "A force of {F} N acts on an area of {A} m². Find the pressure (Pa).", "pressure(F, A)",
       ["P = F ÷ A = {F} ÷ {A}.", "P = {answer} Pa."],
       vars={"A": {"pick": [0.5, 2, 4, 5, 10, 20]}, "k": {"int": [5, 90]}, "F": {"expr": "A * k * 10"}},
       misc=[("mult", "F * A", "Pressure is force divided by area."), ("flip", "pressure(A, F)", "Force on top, area underneath: P = F ÷ A.")],
       unit="Pa", sources=SRC),
   bank("p3-10-app", 1, "{X.q}", [
     {"q": "Why is a kitchen knife sharpened?", "r": "A thin edge has a small area, so the pressure is large", "w": ["A thin edge has a large area", "Sharpening makes the knife heavier", "Sharpening reduces the force needed to lift it"],
      "e": ["A thin edge has a small area.", "Sharpening removes metal; it is lighter.", "Lifting has nothing to do with cutting."], "y": "The same push over a smaller area gives a bigger pressure."},
     {"q": "Why do heavy lorries have many wide tyres?", "r": "To spread the weight over a large area and reduce the pressure on the road", "w": ["To increase the pressure on the road", "To make the lorry go faster", "To reduce the weight of the lorry"],
      "e": ["Large pressure would damage the road and sink into soft ground.", "Tyre width is about pressure, not speed.", "The weight stays the same."], "y": "A large area reduces the pressure."},
     {"q": "Why are the foundations of a building made wide?", "r": "To reduce the pressure on the ground so the building does not sink", "w": ["To increase the pressure on the ground", "To make the walls stronger", "To make the building lighter"],
      "e": ["High pressure would make the building sink.", "Width of the foundation is about pressure on the soil.", "The weight is not reduced."], "y": "A wide base spreads the weight over a large area."}], SRC),
   num("p3-10-f", 2, "A pressure of {P} Pa acts on an area of {A} m². Find the force (N).", "P * A",
       ["F = P × A.", "F = {P} × {A} = {answer} N."],
       vars={"P": {"int": [200, 5000], "step": 100}, "A": {"pick": [0.2, 0.5, 2, 3, 4]}},
       misc=[("div", "roundTo(P / A, 0.01)", "F = P × A: multiply.")],
       unit="N", sources=SRC),
   num("p3-10-cm", 2, "A woman of weight {W} N stands on one heel of area {a} cm². Find the pressure on the floor (Pa).", "W / (a / 10000)",
       ["Area = {a} cm² = {a / 10000} m².", "P = {W} ÷ {a / 10000} = {answer} Pa."],
       vars={"W": {"int": [500, 700], "step": 50}, "a": {"pick": [1, 2, 4, 5]}},
       misc=[("nocm", "W / a", "That is in N/cm². Change cm² to m² first (÷ {10000})."), ("mult", "W * a / 10000", "Divide the force by the area.")],
       unit="Pa", sources=SRC),
   num("p3-10-brick", 3, "A brick of weight {W} N measures {l} m × {w} m × {h} m. What is the greatest pressure it can exert when standing on a table (Pa)?", "roundTo(W / (w * h), 1)",
       ["The greatest pressure is on the smallest face: {w} m × {h} m = {roundTo(w * h, 0.0001)} m².", "P = {W} ÷ {roundTo(w * h, 0.0001)} = {answer} Pa."],
       vars={"W": {"int": [20, 40]}, "l": {"pick": [0.2, 0.25]}, "w": {"pick": [0.1, 0.12]}, "h": {"pick": [0.05, 0.06]}},
       misc=[("big", "roundTo(W / (l * w), 1)", "That is the pressure on the largest face, the smallest pressure. Use the smallest area for the greatest pressure.")],
       unit="Pa", sources=SRC)],
  learn=learn(
    [("Force and area",
      "Push a drawing pin into a board: the sharp point goes in easily, but the flat head would not. The force is the same; what changes is the area.\n"
      "Pressure measures how concentrated a force is: P = F ÷ A, where F is the force acting at right angles to the surface and A is the area.\n"
      "The unit is the pascal: {1} Pa = {1} N/m². Pressures are often large, so kPa ({1000} Pa) is also used."),
     ("Small area, large pressure",
      "• Knives, axes, needles and nails have thin edges or points: tiny area, huge pressure, so they cut or pierce easily.\n"
      "• Football boots have studs to grip the ground.\n"
      "• A woman's narrow heel can damage a soft floor because her weight acts on a tiny area."),
     ("Large area, small pressure",
      "• Lorries have many wide tyres; tractors and bulldozers have wide tracks, so they do not sink into mud.\n"
      "• Buildings stand on wide foundations so the soil is not overloaded.\n"
      "• Carrying a load on a flat pad on the head is more comfortable than on a narrow strap.\n"
      "Remember to change cm² to m² (divide by {10000}) before working out pascals.")],
    key_words=[("pressure", "force per unit area, P = F ÷ A"), ("pascal (Pa)", "{1} newton per square metre"), ("normal force", "a force at right angles to a surface")],
    examples=["{600} N on {0.04} m² gives {15000} Pa", "{50} N on {1} cm² ({0.0001} m²) gives {500000} Pa"],
    mistake=("P = {600} N ÷ {200} cm² = {3} Pa", "{200} cm² = {0.02} m², so P = {30000} Pa",
             "The pascal is N per square metre: change cm² to m² first.")))

# ---------------------------------------------------------------- 11. Pressure in liquids
SRC = ["pressure"]
L.lesson(D, S, 11, ("p3-11", "Pressure in liquids"), [10],
  "Pressure in a liquid:\n"
  "• increases with depth;\n• increases with the density of the liquid;\n• acts equally in all directions at a given depth;\n"
  "• does not depend on the shape or width of the container.\n"
  "Formula: p = ρgh (ρ in kg/m³, g = 10 N/kg, h = depth in m, p in Pa).\n"
  "Applications: dams are thicker at the bottom; water tanks are placed high so taps have good pressure; divers feel more pressure deeper down.",
  worked({"r": 1000, "h": 12},
         "Find the pressure due to the water at the bottom of a well {h} m deep (density of water {r} kg/m³, g = {10} N/kg).",
         ["p = ρgh.", "p = {r} × {10} × {h} = {liquidPressure(r, h)} Pa."], "{liquidPressure(r, h)} Pa", checks=["liquidPressure(r, h) == 120000"]),
  [card("c3p11-1", "Liquid pressure p = ρgh.",
        ["Water {5} m deep: p = {1000} × {10} × {5} = {50000} Pa"], "p3-11-p"),
   card("c3p11-2", "Pressure increases with depth and acts in all directions.",
        ["Water squirts furthest from the lowest hole in a can."], "p3-11-char"),
   card("c3p11-3", "The shape of the container does not matter, only the depth.",
        ["A wide and a narrow tank of the same depth have the same pressure at the bottom."], "p3-11-h")],
  [num("p3-11-p", 1, "Find the pressure due to water at a depth of {h} m (density {1000} kg/m³, g = {10} N/kg).", "liquidPressure(1000, h)",
       ["p = ρgh = {1000} × {10} × {h}.", "p = {answer} Pa."],
       vars={"h": {"int": [2, 40]}},
       misc=[("nog", "1000 * h", "Include g = {10} N/kg: p = ρgh."), ("noh", "10000", "Multiply by the depth h = {h} m too.")],
       unit="Pa", sources=SRC),
   bank("p3-11-char", 1, "{X.q}", [
     {"q": "A tin has three holes at different heights and is filled with water. Water squirts furthest from…", "r": "the lowest hole", "w": ["the highest hole", "the middle hole", "all holes equally"],
      "e": ["Near the top the depth, and so the pressure, is small.", "The lowest hole is deepest.", "Pressure increases with depth, so the jets differ."], "y": "The deepest point has the greatest pressure."},
     {"q": "Why is a dam built thicker at the bottom than at the top?", "r": "Water pressure increases with depth", "w": ["Water is denser at the top", "The top must hold more water", "Pressure is greatest at the surface"],
      "e": ["The density is the same throughout.", "The deeper water pushes harder.", "Pressure is smallest at the surface."], "y": "The wall must resist the large pressure near the bottom."},
     {"q": "At the same depth in a liquid, the pressure acts…", "r": "equally in all directions", "w": ["only downwards", "only sideways", "only upwards"],
      "e": ["Liquid pressure also pushes sideways and upwards.", "It also pushes down and up.", "It also pushes down and sideways."], "y": "Liquid pressure at a point is the same in every direction."}], SRC),
   num("p3-11-h", 2, "The pressure due to sea water (density {1030} kg/m³) on a diver is {p} Pa. How deep is the diver (m)?", "d",
       ["h = p ÷ (ρg) = {p} ÷ ({1030} × {10}).", "h = {answer} m."],
       vars={"d": {"int": [2, 30]}, "p": {"expr": "1030 * 10 * d"}},
       misc=[("nog", "d * 10", "Divide by both ρ and g: ρg = {10300}.")],
       unit="m", sources=SRC),
   num("p3-11-diff", 2, "A water tank in Bamenda is {H} m above a tap. Find the extra pressure at the tap due to the water (kPa).", "liquidPressure(1000, H) / 1000",
       ["p = ρgh = {1000} × {10} × {H} = {liquidPressure(1000, H)} Pa.", "In kPa: {liquidPressure(1000, H)} ÷ {1000} = {answer} kPa."],
       vars={"H": {"int": [3, 25]}},
       misc=[("pa", "liquidPressure(1000, H)", "That is in Pa. Divide by {1000} for kPa.")],
       unit="kPa", sources=SRC),
   num("p3-11-total", 3, "Atmospheric pressure is {100000} Pa. Find the total pressure on a fish {h} m below the surface of a lake (Pa).", "100000 + liquidPressure(1000, h)",
       ["Water pressure = ρgh = {1000} × {10} × {h} = {liquidPressure(1000, h)} Pa.", "Total = {100000} + {liquidPressure(1000, h)} = {answer} Pa."],
       vars={"h": {"int": [2, 30]}},
       misc=[("water", "liquidPressure(1000, h)", "Add the atmospheric pressure pressing on the surface too."), ("air", "100000", "The water adds ρgh to the atmospheric pressure.")],
       unit="Pa", sources=SRC)],
  learn=learn(
    [("Deeper means more pressure",
      "Water has weight. The deeper you go, the more water there is above you pressing down, so the pressure increases with depth.\n"
      "Fill a tin with water and make three holes at different heights: the jet from the lowest hole goes furthest.\n"
      "Divers feel the pressure on their ears a few metres down; at the bottom of a deep lake it is very large."),
     ("Three more facts",
      "• At a given depth the pressure acts equally in all directions: up, down and sideways.\n"
      "• A denser liquid gives a larger pressure at the same depth (sea water more than fresh water).\n"
      "• The shape of the container does not matter. A narrow pipe and a wide tank filled to the same depth have the same pressure at the bottom.\n"
      "That is why dams, like those at Edéa and Song Loulou, are thickest at the bottom."),
     ("Calculating it",
      "p = ρgh, with ρ the density in kg/m³, g = {10} N/kg and h the depth in metres.\n"
      "At {5} m in water: p = {1000} × {10} × {5} = {50000} Pa.\n"
      "This is the pressure due to the liquid. The air also presses on the surface, so the total pressure is atmospheric pressure + ρgh.")],
    key_words=[("depth", "distance below the surface of the liquid"), ("ρgh", "pressure due to a liquid column"), ("dam", "a wall that holds back water")],
    examples=["{10} m of water: {100000} Pa", "Mercury ({13600} kg/m³), {0.76} m: about {103360} Pa"],
    mistake=("A wide tank has more pressure at the bottom than a narrow one of the same depth", "The pressures are equal: only depth (and density) matter",
             "p = ρgh has no area in it, so the width of the container does not matter.")))

# ---------------------------------------------------------------- 12. Atmospheric pressure
SRC = ["pressure"]
L.lesson(D, S, 12, ("p3-12", "Atmospheric pressure and the simple barometer"), [11],
  "The atmosphere is a layer of air around the Earth; its weight presses on everything: this is atmospheric pressure, about 100 000 Pa (100 kPa) at sea level.\n"
  "Demonstrations: a can crushes when the air inside is removed (by steam then cooling); a card stays on an upturned glass of water; a straw works because the air pushes the drink up.\n"
  "The simple mercury barometer: a tube full of mercury is upturned in a dish; the mercury falls until about 760 mm (0.76 m) is left. The air pressure holds up that column: p = ρgh.\n"
  "Mercury is used because it is very dense (13 600 kg/m³), so the tube can be short; a water barometer would need about 10 m.",
  worked({"h": 0.76, "r": 13600},
         "A mercury barometer reads {h * 1000} mm. Find the atmospheric pressure (density of mercury {r} kg/m³, g = {10} N/kg).",
         ["h = {h * 1000} mm = {h} m.", "p = ρgh = {r} × {10} × {h} = {liquidPressure(r, h)} Pa."], "{liquidPressure(r, h)} Pa", checks=["liquidPressure(r, h) == 103360"]),
  [card("c3p12-1", "The weight of the air above us causes atmospheric pressure, about {100} kPa.",
        ["A can crushes when the air inside is removed."], "p3-12-demo"),
   card("c3p12-2", "A barometer's mercury column is held up by air pressure: p = ρgh.",
        ["{760} mm of mercury ≈ {103360} Pa"], "p3-12-hg"),
   card("c3p12-3", "Mercury is used because it is dense: the column is short.",
        ["Water would need a tube about {10} m tall."], "p3-12-why")],
  [bank("p3-12-demo", 1, "{X.q}", [
     {"q": "Steam fills a can, the lid is closed and the can is cooled. It collapses. Why?", "r": "The steam condenses, the pressure inside falls, and the air outside crushes the can", "w": ["Cold water shrinks the metal", "The steam pulls the walls in", "The can becomes heavier"],
      "e": ["Cooling the metal this little does not crush it.", "Steam does not pull; the outside air pushes.", "Its weight barely changes."], "y": "Atmospheric pressure outside is much larger than the pressure left inside."},
     {"q": "How does a drinking straw work?", "r": "You lower the pressure in the straw; atmospheric pressure pushes the drink up", "w": ["Your mouth pulls the drink up by suction force", "The drink is lighter than air", "The straw squeezes the drink"],
      "e": ["Suction is not a force: the outside air does the pushing.", "Drinks are much denser than air.", "The straw does not squeeze anything."], "y": "Air pressure on the surface of the drink pushes it up the straw."},
     {"q": "A card covers a full glass of water turned upside down, and the water does not fall. Why?", "r": "Atmospheric pressure on the card is greater than the water pressure on it", "w": ["The card is glued by the water", "Water has no weight", "The glass is magnetic"],
      "e": ["Water does not glue strongly enough to hold the weight.", "Water has weight.", "Glass is not magnetic."], "y": "The air pushes up on the card with about {100000} Pa."}], SRC),
   num("p3-12-hg", 1, "A mercury barometer reads {mm} mm. Find the atmospheric pressure (Pa). Density of mercury = {13600} kg/m³, g = {10} N/kg.", "liquidPressure(13600, mm / 1000)",
       ["h = {mm} mm = {mm / 1000} m.", "p = {13600} × {10} × {mm / 1000} = {answer} Pa."],
       vars={"mm": {"int": [680, 770], "step": 10}},
       misc=[("mm", "13600 * 10 * mm", "Change mm to metres first (÷ {1000})."), ("nog", "liquidPressure(13600, mm / 1000) / 10", "Include g = {10} N/kg.")],
       unit="Pa", sources=SRC),
   num("p3-12-water", 2, "Atmospheric pressure is {p} Pa. How tall would the column be in a water barometer (m)? Density of water {1000} kg/m³.", "p / 10000",
       ["h = p ÷ (ρg) = {p} ÷ ({1000} × {10}).", "h = {answer} m."],
       vars={"p": {"int": [95000, 104000], "step": 1000}},
       misc=[("nog", "p / 1000", "Divide by ρg = {10000}, not just by ρ.")],
       unit="m", sources=SRC),
   bank("p3-12-why", 2, "{X.q}", [
     {"q": "Why is mercury used in a barometer rather than water?", "r": "Mercury is very dense, so the column is short (about 76 cm)", "w": ["Mercury is cheaper than water", "Water evaporates too fast to read", "Mercury is lighter than water"],
      "e": ["Mercury is expensive.", "The main reason is the height: water would need about 10 m.", "Mercury is about 13.6 times denser than water."], "y": "p = ρgh: a large ρ gives a small h."},
     {"q": "What is in the space above the mercury in a barometer tube?", "r": "A vacuum (almost nothing)", "w": ["Air", "Water vapour", "Mercury gas at high pressure"],
      "e": ["Air would push the mercury down and spoil the reading.", "No water is in the tube.", "There is only a tiny amount of mercury vapour."], "y": "The tube was full of mercury before it was turned over; nothing replaced the mercury that fell."},
     {"q": "If the barometer tube is tilted, what happens to the vertical height of the mercury column?", "r": "It stays the same", "w": ["It increases", "It decreases", "It becomes zero"],
      "e": ["The mercury fills more of the tube, but the vertical height is fixed by air pressure.", "Air pressure has not changed.", "Air pressure still holds the mercury up."], "y": "Only the vertical height depends on the air pressure."}], SRC),
   num("p3-12-alt", 3, "At sea level in Limbe a barometer reads {760} mm of mercury; at the top of a hill it reads {r} mm. Find the difference in atmospheric pressure (Pa).", "liquidPressure(13600, (760 - r) / 1000)",
       ["Difference in height = {760} − {r} = {760 - r} mm = {(760 - r) / 1000} m.", "Δp = {13600} × {10} × {(760 - r) / 1000} = {answer} Pa."],
       vars={"r": {"int": [700, 750], "step": 5}},
       misc=[("top", "liquidPressure(13600, r / 1000)", "That is the pressure at the top. The question asks for the difference."), ("mm", "13600 * 10 * (760 - r)", "Change mm to metres.")],
       unit="Pa", sources=SRC)],
  learn=learn(
    [("An ocean of air",
      "We live at the bottom of an ocean of air many kilometres deep. That air has weight, and it presses on everything: this is atmospheric pressure, about {100000} Pa at sea level.\n"
      "We do not feel it because the fluids in our body push outwards just as hard."),
     ("Seeing it work",
      "• Boil a little water in a can, close it and cool it: the steam turns back to water, the pressure inside drops, and the outside air crushes the can.\n"
      "• A straw: you lower the pressure inside; the air pushes the drink up.\n"
      "• A full glass with a card on top can be turned over without spilling: the air holds up the card."),
     ("The mercury barometer",
      "Fill a long glass tube with mercury, close the end and turn it upside down into a dish of mercury. The mercury falls until the column is about {760} mm high, leaving a vacuum at the top.\n"
      "The air pressure on the dish holds up the column, so p = ρgh = {13600} × {10} × {0.76} ≈ {103360} Pa.\n"
      "Mercury is used because it is so dense; with water the tube would need to be about {10} m tall.")],
    key_words=[("atmospheric pressure", "the pressure caused by the weight of the air"), ("barometer", "an instrument that measures atmospheric pressure"),
               ("vacuum", "a space with no air")],
    examples=["{760} mm of mercury ≈ {103} kPa", "A water barometer needs about {10} m of water"],
    mistake=("A straw sucks the drink up", "The air pushes the drink up when the pressure in the straw is lowered",
             "Suction is not a pulling force: atmospheric pressure does the work.")))

# ---------------------------------------------------------------- 13. Effects of atmospheric pressure
SRC = ["pressure"]
L.lesson(D, S, 13, ("p3-13", "Effects of atmospheric pressure on boiling points and on health"), [12],
  "Atmospheric pressure decreases with altitude: there is less air above you.\n"
  "Boiling point depends on pressure: a liquid boils when its vapour pressure equals the pressure above it.\n"
  "• Lower pressure (high places such as Mount Cameroon) → water boils below 100 °C, so food takes longer to cook.\n"
  "• Higher pressure (pressure cooker) → water boils above 100 °C, so food cooks faster.\n"
  "Health: at high altitude there is less oxygen per breath (altitude sickness, headaches, breathlessness); ears 'pop' when pressure changes quickly; divers who rise too fast suffer the bends. Aircraft cabins are pressurised.",
  worked({},
         "Why do climbers on Mount Cameroon find that rice cooks slowly near the summit?",
         ["The air pressure is lower high up.", "Lower pressure lowers the boiling point of water below {100} °C.", "The water boils at a lower temperature, so the rice cooks more slowly."],
         "Lower pressure, lower boiling point, slower cooking"),
  [card("c3p13-1", "Higher altitude → lower air pressure → lower boiling point.",
        ["High on a mountain, water may boil at about {90} °C."], "p3-13-boil"),
   card("c3p13-2", "A pressure cooker raises the pressure, so water boils above {100} °C.",
        ["Beans cook faster in a pressure cooker."], "p3-13-cooker"),
   card("c3p13-3", "Low pressure at altitude means less oxygen per breath.",
        ["Climbers may feel dizzy and breathless."], "p3-13-health")],
  [bank("p3-13-boil", 1, "{X.q}", [
     {"q": "How does the boiling point of water change as you climb a mountain?", "r": "It goes down", "w": ["It goes up", "It stays at 100 °C", "Water cannot boil there"],
      "e": ["Higher up the pressure is lower, which lowers the boiling point.", "100 °C is the boiling point only at normal sea-level pressure.", "It boils, but at a lower temperature."], "y": "Lower air pressure, lower boiling point."},
     {"q": "Why does food take longer to cook at high altitude?", "r": "Water boils at a lower temperature there", "w": ["Water boils at a higher temperature there", "Fire burns hotter there", "Food is heavier there"],
      "e": ["Lower pressure means a lower boiling point.", "Less oxygen makes fires burn less well, not hotter.", "The weight of food has nothing to do with cooking time."], "y": "Boiling water is cooler, so cooking is slower."},
     {"q": "What happens to atmospheric pressure as altitude increases?", "r": "It decreases", "w": ["It increases", "It stays the same", "It becomes zero at once"],
      "e": ["There is less air above you higher up.", "There is less air above you higher up.", "It falls gradually."], "y": "Less air above, less weight, lower pressure."}], SRC),
   bank("p3-13-cooker", 1, "{X.q}", [
     {"q": "How does a pressure cooker cook food faster?", "r": "It raises the pressure, so water boils above 100 °C", "w": ["It lowers the boiling point", "It removes the air so food cooks in a vacuum", "It makes the flame hotter"],
      "e": ["It raises the boiling point.", "It traps steam, raising the pressure.", "The flame is the same."], "y": "Hotter boiling water cooks food faster."},
     {"q": "Why must a pressure cooker have a safety valve?", "r": "To let steam out if the pressure gets dangerously high", "w": ["To let air in", "To make the food taste better", "To measure the temperature"],
      "e": ["The valve releases pressure, it does not let air in.", "Taste has nothing to do with it.", "It does not measure temperature."], "y": "Too much pressure could burst the cooker."},
     {"q": "Water in a sealed pressure cooker boils at about…", "r": "120 °C", "w": ["80 °C", "100 °C exactly", "0 °C"],
      "e": ["Higher pressure raises the boiling point above 100 °C.", "100 °C is the boiling point at normal pressure.", "0 °C is the freezing point."], "y": "The higher pressure raises the boiling point to about 120 °C."}], SRC),
   bank("p3-13-health", 2, "{X.q}", [
     {"q": "Why do some climbers feel dizzy near the summit of a high mountain?", "r": "The low air pressure means less oxygen in each breath", "w": ["The air contains more oxygen", "Their blood becomes heavier", "The sun is closer"],
      "e": ["There is less oxygen per breath.", "Blood density does not change.", "Distance to the sun is not the cause."], "y": "Altitude sickness comes from low pressure and less oxygen."},
     {"q": "Why do your ears 'pop' when a plane takes off?", "r": "The outside pressure changes quickly and the pressure in the middle ear adjusts", "w": ["The engine noise is too loud", "The ears freeze", "Oxygen fills the ears"],
      "e": ["Noise does not cause popping.", "Cabins are warm.", "It is about pressure, not oxygen."], "y": "Swallowing lets air in or out to balance the pressure on the eardrum."},
     {"q": "Why are aircraft cabins pressurised?", "r": "At cruising height the air pressure is too low for people to breathe comfortably", "w": ["To make the plane heavier", "To keep the plane warm", "To make the engines work"],
      "e": ["Pressurising does not add useful weight.", "Heating is a separate system.", "Engines take in outside air."], "y": "High up, the outside pressure is too low for healthy breathing."}], SRC),
   order("p3-13-chain", 3, "Put the explanation in order: why does rice cook slowly near the top of Mount Cameroon?",
         ["The climber is very high up.", "There is less air above, so the air pressure is lower.", "Water boils at a temperature below 100 °C.",
          "The boiling water is not as hot, so the rice cooks more slowly."], hint="Start from the height and end with the cooking.", sources=SRC, review="authored")],
  learn=learn(
    [("Less air higher up",
      "The higher you go, the less air there is above you, so the atmospheric pressure is lower. At the top of Mount Cameroon (about {4000} m) it is roughly two-thirds of the pressure in Douala.\n"
      "Pressure changes affect boiling, breathing and our ears."),
     ("Boiling and pressure",
      "Water boils when its vapour can push back against the pressure of the air above it. With less air pressure, this happens at a lower temperature.\n"
      "So on a high mountain water may boil at about {90} °C, and food takes longer to cook.\n"
      "A pressure cooker does the opposite: it traps steam, raises the pressure and makes water boil at about {120} °C, so beans and meat cook much faster. Its safety valve releases steam if the pressure gets too high."),
     ("Pressure and health",
      "• At high altitude each breath holds less oxygen: climbers can get headaches, dizziness and breathlessness (altitude sickness).\n"
      "• Quick changes of pressure, in a plane or a car going down a hill, make your ears 'pop'; swallowing helps.\n"
      "• Divers who come up too fast can get the bends. Aircraft cabins are pressurised so passengers breathe comfortably.")],
    key_words=[("altitude", "height above sea level"), ("boiling point", "the temperature at which a liquid boils; it depends on pressure"),
               ("pressure cooker", "a sealed pan that raises the pressure and the boiling point")],
    examples=["Mountain top: water boils below {100} °C", "Pressure cooker: water boils at about {120} °C"],
    mistake=("Water always boils at {100} °C", "{100} °C is the boiling point only at normal sea-level pressure",
             "Lower pressure lowers the boiling point; higher pressure raises it.")))

# ---------------------------------------------------------------- 14. Elasticity and Hooke's law
SRC = ["elasticity"]
L.lesson(D, S, 14, ("p3-14", "Elasticity and Hooke's law"), [2],
  "A material is elastic if it returns to its original shape when the force is removed (rubber, a steel spring). Plastic materials keep the new shape (clay, plasticine).\n"
  "Extension = stretched length − original length.\n"
  "Hooke's law: the extension of a spring is directly proportional to the load (force), provided the elastic limit is not exceeded: F = ke, where k is the spring constant (N/m or N/cm).\n"
  "Beyond the elastic limit, the spring is permanently stretched and the law no longer holds.\n"
  "To verify: hang loads on a spring, measure the extension for each, and plot force against extension: a straight line through the origin.",
  worked({"o": 12, "n": 18, "F": 3},
         "A spring is {o} cm long. With a load of {F} N it is {n} cm long. Find the extension and the spring constant (N/cm).",
         ["Extension e = {n} − {o} = {n - o} cm.", "k = F ÷ e = {F} ÷ {n - o} = {F / (n - o)} N/cm."],
         "e = {n - o} cm, k = {F / (n - o)} N/cm", checks=["F / (n - o) == 0.5"]),
  [card("c3p14-1", "Extension = stretched length − original length.",
        ["{15} cm − {10} cm = {5} cm"], "p3-14-ext"),
   card("c3p14-2", "Hooke's law: F = ke, as long as the elastic limit is not passed.",
        ["k = {2} N/cm, e = {3} cm: F = {6} N"], "p3-14-f"),
   card("c3p14-3", "Beyond the elastic limit the spring does not go back to its length.",
        ["A spring overloaded in a game stays longer."], "p3-14-limit")],
  [num("p3-14-ext", 1, "A spring is {o} cm long. With a load it is {o + e} cm long. Find the extension (cm).", "e",
       ["Extension = stretched length − original length.", "= {o + e} − {o} = {answer} cm."],
       vars={"o": {"int": [8, 25]}, "e": {"int": [1, 12]}},
       misc=[("new", "o + e", "That is the new length. Extension is the increase."), ("add", "2 * o + e", "Subtract the original length.")],
       unit="cm", sources=SRC),
   num("p3-14-f", 1, "A spring has spring constant {k} N/cm. What load gives an extension of {e} cm (N)?", "k * e",
       ["F = ke.", "F = {k} × {e} = {answer} N."],
       vars={"k": {"int": [2, 9]}, "e": {"int": [2, 10]}},
       misc=[("div", "roundTo(e / k, 0.01)", "F = k × e: multiply.")],
       unit="N", sources=SRC, where=["k != e"]),
   num("p3-14-prop", 2, "A load of {F1} N stretches a spring by {e1} cm. What extension will a load of {F2} N give (cm), within the elastic limit?", "e1 * F2 / F1",
       ["Extension is proportional to load.", "e = {e1} × {F2} ÷ {F1} = {answer} cm."],
       vars={"F1": {"int": [2, 6]}, "e1": {"int": [2, 6]}, "F2": {"int": [3, 12]}},
       misc=[("add", "e1 + F2 - F1", "Hooke's law is about proportion: multiply by {F2} ÷ {F1}.")],
       unit="cm", sources=SRC, where=["F1 != F2", "(e1 * F2) % F1 == 0", "e1 + F2 - F1 != e1 * F2 / F1"]),
   num("p3-14-k", 2, "A load of {F} N stretches a spring by {c} cm. Find the spring constant in N/m.", "F / (c / 100)",
       ["e = {c} cm = {c / 100} m.", "k = F ÷ e = {F} ÷ {c / 100} = {answer} N/m."],
       vars={"F": {"int": [2, 20]}, "c": {"pick": [2, 4, 5, 20]}},
       misc=[("cm", "F / c", "That is in N/cm. Change cm to m first."), ("mult", "F * c / 100", "k = F ÷ e: divide.")],
       unit="N/m", sources=SRC),
   bank("p3-14-limit", 3, "{X.q}", [
     {"q": "A spring is loaded beyond its elastic limit, then the load is removed. What happens?", "r": "It stays longer than its original length", "w": ["It returns exactly to its original length", "It becomes shorter than before", "Its extension doubles"],
      "e": ["Only within the elastic limit does it return.", "It is permanently stretched, not shortened.", "There is no such rule."], "y": "Beyond the elastic limit the deformation is permanent."},
     {"q": "Which material is plastic rather than elastic?", "r": "modelling clay", "w": ["a rubber band", "a steel spring", "a tennis ball"],
      "e": ["A rubber band springs back.", "A steel spring springs back within its limit.", "A tennis ball regains its shape."], "y": "Clay keeps the new shape."},
     {"q": "Hooke's law says the extension is proportional to the load…", "r": "provided the elastic limit is not exceeded", "w": ["for any load", "only for rubber", "only when the spring is horizontal"],
      "e": ["Beyond the limit the graph curves.", "It applies to springs and wires too.", "Direction does not matter."], "y": "The law holds only up to the limit of proportionality."}], SRC)],
  learn=learn(
    [("Elastic and plastic",
      "Stretch a rubber band and let go: it returns to its original shape. Materials that do this are elastic: rubber, steel springs, the strings of a guitar.\n"
      "Squeeze modelling clay: it keeps its new shape. Such materials are plastic.\n"
      "Even an elastic material has a limit. Pull a spring too hard and it stays longer: you have passed its elastic limit."),
     ("Hooke's law",
      "Robert Hooke found that, for a spring, the extension e is directly proportional to the stretching force F: double the load, double the extension.\n"
      "F = ke, where k is the spring constant (stiffness), in N/m or N/cm.\n"
      "Extension means the increase in length: stretched length − original length. A spring {10} cm long that stretches to {15} cm has an extension of {5} cm."),
     ("Checking it in the laboratory",
      "• Hang the spring from a clamp next to a metre rule and read its length.\n• Add loads one at a time and read the length each time.\n"
      "• Work out each extension and plot load (N) against extension (cm).\n"
      "Up to the limit the points lie on a straight line through the origin; after it, the line curves.")],
    key_words=[("elastic", "returns to its original shape when the force is removed"), ("extension", "the increase in length"),
               ("spring constant k", "force per unit extension"), ("elastic limit", "the largest load after which the spring still returns to its length")],
    examples=["{4} N stretches a spring {2} cm: k = {2} N/cm", "{6} N then stretches it {3} cm"],
    mistake=("Extension = the stretched length, {15} cm", "Extension = {15} − {10} = {5} cm",
             "Hooke's law is about the increase in length, not the total length.")))

# ---------------------------------------------------------------- 15. Force-extension graph, applications
SRC = ["elasticity"]
L.lesson(D, S, 15, ("p3-15", "Force-extension graphs and uses of elastic materials"), [14],
  "A force-extension graph for a spring is a straight line through the origin up to the limit of proportionality; then it curves.\n"
  "• The gradient (force ÷ extension) is the spring constant k.\n• From the graph you can read the extension for any load, or the load for any extension.\n"
  "Uses of elastic materials: spring balances, car and motorbike suspension, mattresses and chairs, catapults, bows, rubber bands, trampolines, shock absorbers.",
  worked({"k": 2},
         "The graph shows load against extension for a spring. Use it to find the spring constant.",
         ["Pick a point on the line: {6} N gives {6 / k} cm.", "k = gradient = {6} ÷ {6 / k} = {k} N/cm."],
         "{k} N/cm", checks=["k == 2"], figure="lineGraph([0, 1, 2, 3, 4], [0, k, 2 * k, 3 * k, 4 * k], 'extension (cm)', 'load (N)')"),
  [card("c3p15-1", "The gradient of the load-extension line is the spring constant.",
        ["{8} N for {4} cm: k = {2} N/cm"], "p3-15-k"),
   card("c3p15-2", "Read values straight from the line.",
        ["Go across from the load, then down to the extension."], "p3-15-read"),
   card("c3p15-3", "Springs are used where a force must be measured or a shock absorbed.",
        ["Spring balance, car suspension, mattress"], "p3-15-use")],
  [num("p3-15-k", 1, "Use the graph to find the spring constant (N/cm).", "k",
       ["Take a point on the line: {4 * k} N at {4} cm.", "k = {4 * k} ÷ {4} = {answer} N/cm."],
       vars={"k": {"int": [2, 6]}},
       misc=[("flip", "1 / k", "k = load ÷ extension, not extension ÷ load.")],
       unit="N/cm", figure="lineGraph([0, 1, 2, 3, 4], [0, k, 2 * k, 3 * k, 4 * k], 'extension (cm)', 'load (N)')", sources=SRC),
   num("p3-15-read", 2, "Use the graph: what extension does a load of {k * x} N give (cm)?", "x",
       ["The line rises {k} N for every {1} cm.", "{k * x} N ÷ {k} N/cm = {answer} cm."],
       vars={"k": {"int": [2, 6]}, "x": {"int": [1, 4]}},
       misc=[("load", "k * x", "{k * x} is the load; read across to the extension.")],
       unit="cm", figure="lineGraph([0, 1, 2, 3, 4], [0, k, 2 * k, 3 * k, 4 * k], 'extension (cm)', 'load (N)')", sources=SRC, where=["k * x != x"]),
   bank("p3-15-use", 1, "{X.q}", [
     {"q": "Which device uses a spring to measure force?", "r": "a spring balance (newton meter)", "w": ["a beam balance", "a thermometer", "a measuring cylinder"],
      "e": ["A beam balance compares masses without a spring.", "A thermometer measures temperature.", "A measuring cylinder measures volume."], "y": "The extension of the spring shows the force."},
     {"q": "Why do cars and motorbikes have springs in their suspension?", "r": "To absorb shocks from bumps in the road", "w": ["To make the vehicle faster", "To measure the speed", "To make the vehicle heavier"],
      "e": ["Springs do not increase speed.", "A speedometer measures speed.", "That is not their purpose."], "y": "The springs stretch and compress, giving a smoother ride."},
     {"q": "Which of these does NOT use an elastic material for its job?", "r": "a brick wall", "w": ["a catapult", "a trampoline", "a mattress"],
      "e": ["A catapult stores energy in stretched rubber.", "A trampoline bounces back.", "A mattress springs back."], "y": "A wall must stay rigid; it does not use elasticity."}], SRC),
   bank("p3-15-shape", 2, "{X.q}", [
     {"q": "On a load-extension graph for a spring, what does a straight line through the origin show?", "r": "Extension is proportional to load (Hooke's law)", "w": ["The spring has broken", "The load is constant", "The spring is plastic"],
      "e": ["A broken spring gives no line.", "The load changes along the axis.", "A plastic material does not give a straight line through the origin."], "y": "Straight line through the origin: direct proportion."},
     {"q": "After a certain load the graph starts to curve. This point is…", "r": "the limit of proportionality", "w": ["the origin", "the spring constant", "the zero error"],
      "e": ["The origin is where the line starts.", "The spring constant is the gradient.", "A zero error is a wrong starting reading."], "y": "Beyond it, extension is no longer proportional to load."},
     {"q": "Spring A has a steeper load-extension line than spring B. Which is stiffer?", "r": "A", "w": ["B", "They are equally stiff", "It depends on their colour"],
      "e": ["B stretches more for the same load.", "Different gradients mean different stiffness.", "Colour does not matter."], "y": "A steeper line means more load for each centimetre: a larger k."}], SRC),
   num("p3-15-weigh", 3, "A spring has constant {k} N/cm. An unknown bunch of plantains stretches it by {e} cm. Find the weight (N) and the mass (kg) of the plantains. Give the mass.", "k * e / 10",
       ["Weight F = ke = {k} × {e} = {k * e} N.", "Mass = W ÷ g = {k * e} ÷ {10} = {answer} kg."],
       vars={"k": {"int": [5, 20]}, "e": {"int": [2, 12]}},
       misc=[("weight", "k * e", "That is the weight in newtons. Divide by g = {10} N/kg for the mass.")],
       unit="kg", sources=SRC)],
  learn=learn(
    [("Reading the graph",
      "Plot load (N) up the side and extension (cm) along the bottom. For a spring obeying Hooke's law you get a straight line through the origin.\n"
      "The gradient (rise ÷ run) is the spring constant: if {8} N gives {4} cm, k = {2} N/cm.\n"
      "To find the extension for a load, go across from the load to the line, then down.", "lineGraph([0, 1, 2, 3, 4], [0, 2, 4, 6, 8], 'extension (cm)', 'load (N)')"),
     ("Beyond the limit",
      "If you keep adding loads, the line eventually bends: this is the limit of proportionality. Soon after comes the elastic limit; beyond it the spring stays stretched.\n"
      "A steeper line means a stiffer spring (bigger k): it needs more force to stretch the same amount."),
     ("Elastic materials at work",
      "• Spring balances measure force by extension.\n• Suspension springs and shock absorbers in cars, motorbikes and bicycles smooth out bumps.\n"
      "• Mattresses and chairs use springs or foam for comfort.\n• Catapults, bows and trampolines store energy when stretched and release it.\n"
      "• Rubber bands hold things together because they pull back.")],
    key_words=[("gradient", "rise ÷ run of a line; here load ÷ extension = k"), ("limit of proportionality", "where the graph stops being straight"),
               ("stiff", "hard to stretch: large spring constant")],
    examples=["Line through ({4} cm, {12} N): k = {3} N/cm", "k = {5} N/cm, e = {4} cm: weight {20} N, mass {2} kg"],
    mistake=("k = extension ÷ load", "k = load ÷ extension",
             "The spring constant is the force needed for each unit of extension.")))

# ---------------------------------------------------------------- 16. Energy: forms and sources
SRC = ["energy"]
L.lesson(D, S, 16, ("p3-16", "Energy: forms and sources, renewable and non-renewable"), [],
  "Energy is the ability to do work. Unit: the joule (J); 1 kJ = 1000 J.\n"
  "Forms: kinetic (movement), potential (gravitational: height; elastic: stretched spring), chemical (food, fuel, batteries), thermal (heat), electrical, light, sound, nuclear.\n"
  "Sources:\n• Renewable (will not run out): solar, wind, hydroelectric (Edéa, Song Loulou, Lagdo dams), biomass (wood, crop waste), geothermal, tides.\n"
  "• Non-renewable (will run out): petroleum, natural gas, coal, nuclear fuel (uranium).\n"
  "Fossil fuels release carbon dioxide and pollute; renewables are cleaner but some depend on weather.",
  worked({},
         "Classify these sources of energy used in Cameroon: firewood, the Lagdo dam, kerosene, solar panels in Maroua.",
         ["Firewood: biomass, renewable if trees are replanted.", "Lagdo dam: hydroelectricity, renewable.", "Kerosene: from petroleum, non-renewable.", "Solar panels: solar energy, renewable."],
         "Renewable: firewood (if replanted), Lagdo dam, solar; non-renewable: kerosene"),
  [card("c3p16-1", "Energy has many forms; the unit is the joule.",
        ["A moving bus has kinetic energy; a battery stores chemical energy."], "p3-16-form"),
   card("c3p16-2", "Renewable sources do not run out: sun, wind, flowing water.",
        ["Edéa and Song Loulou dams make hydroelectricity."], "p3-16-src"),
   card("c3p16-3", "Fossil fuels are non-renewable and release carbon dioxide.",
        ["Petrol, diesel, kerosene, natural gas, coal"], "p3-16-adv")],
  [bank("p3-16-form", 1, "{X.q}", [
     {"q": "What form of energy does a stretched catapult rubber store?", "r": "elastic potential energy", "w": ["kinetic energy", "chemical energy", "sound energy"],
      "e": ["It is not moving yet.", "Chemical energy is stored in food and fuels.", "It makes little sound."], "y": "Stretched or squeezed objects store elastic potential energy."},
     {"q": "What form of energy is stored in a plate of rice and beans?", "r": "chemical energy", "w": ["kinetic energy", "nuclear energy", "light energy"],
      "e": ["The food is not moving.", "Nuclear energy is in the nucleus of atoms such as uranium.", "Food does not shine."], "y": "Food stores chemical energy that the body releases."},
     {"q": "A mango hanging high on a tree has…", "r": "gravitational potential energy", "w": ["kinetic energy", "electrical energy", "sound energy"],
      "e": ["It is not moving.", "It carries no current.", "It makes no sound."], "y": "Its height gives it gravitational potential energy."},
     {"q": "What is the SI unit of energy?", "r": "joule (J)", "w": ["watt (W)", "newton (N)", "pascal (Pa)"],
      "e": ["The watt is the unit of power.", "The newton is the unit of force.", "The pascal is the unit of pressure."], "y": "Energy is measured in joules."}], SRC),
   bank("p3-16-src", 1, "{X.q}", [
     {"q": "Which source of energy is renewable?", "r": "hydroelectricity from a dam", "w": ["petrol", "natural gas", "coal"],
      "e": ["Petrol comes from crude oil, which will run out.", "Natural gas is a fossil fuel.", "Coal is a fossil fuel."], "y": "Rain refills the river behind the dam."},
     {"q": "Which source of energy is non-renewable?", "r": "kerosene", "w": ["solar energy", "wind energy", "firewood from replanted forests"],
      "e": ["The sun keeps shining.", "Wind keeps blowing.", "Replanted trees grow again."], "y": "Kerosene comes from petroleum, which forms over millions of years."},
     {"q": "Why is wood called renewable only if trees are replanted?", "r": "Cutting trees faster than they grow uses up the forest", "w": ["Wood is a fossil fuel", "Wood never burns completely", "Trees grow back in one day"],
      "e": ["Wood is biomass, not a fossil fuel.", "Burning has nothing to do with it.", "Trees take years to grow."], "y": "Biomass is renewable only when it is replaced."}], SRC),
   num("p3-16-kj", 2, "A battery stores {E} kJ of energy. How many joules is that?", "E * 1000",
       ["{1} kJ = {1000} J.", "{E} × {1000} = {answer} J."],
       vars={"E": {"int": [2, 90]}},
       misc=[("div", "E / 1000", "Joules are smaller units: the number gets bigger.")],
       unit="J", sources=SRC),
   bank("p3-16-adv", 2, "{X.q}", [
     {"q": "What is one disadvantage of solar panels?", "r": "They produce little at night or on cloudy days", "w": ["They release a lot of carbon dioxide", "Sunlight will soon run out", "They need petrol to work"],
      "e": ["They release no carbon dioxide when working.", "The sun will shine for billions of years.", "They need only sunlight."], "y": "Solar power depends on the weather and time of day."},
     {"q": "What is one disadvantage of burning fossil fuels?", "r": "They release carbon dioxide and pollute the air", "w": ["They are renewable", "They cannot be burned", "They give no heat"],
      "e": ["Fossil fuels are non-renewable.", "They burn easily.", "They give a lot of heat."], "y": "Carbon dioxide contributes to climate change."},
     {"q": "What is one advantage of hydroelectricity for Cameroon?", "r": "It uses rivers that are renewed by rain and releases little pollution", "w": ["It works without water", "It can be built anywhere", "It is non-renewable"],
      "e": ["It needs flowing water.", "It needs a suitable river and valley.", "It is renewable."], "y": "Rivers such as the Sanaga provide renewable energy."}], SRC),
   bank("p3-16-change", 3, "{X.q}", [
     {"q": "A girl climbs to the top of a slide, then slides down. Which energy change happens as she slides?", "r": "gravitational potential energy → kinetic energy (and some heat)", "w": ["kinetic energy → chemical energy", "electrical energy → sound energy", "chemical energy → nuclear energy"],
      "e": ["She is not storing energy chemically as she slides.", "No electricity is involved.", "No nuclear change happens."], "y": "She loses height and gains speed; friction makes some heat."},
     {"q": "A battery-powered torch is switched on. What is the main energy change in the battery?", "r": "chemical → electrical", "w": ["electrical → chemical", "light → electrical", "kinetic → chemical"],
      "e": ["That happens when charging.", "That happens in a solar cell.", "The battery is not moving."], "y": "Chemicals in the battery react to give electrical energy."},
     {"q": "In a hydroelectric power station, what is the order of energy changes?", "r": "potential (stored water) → kinetic (falling water) → electrical", "w": ["electrical → kinetic → potential", "chemical → heat → electrical", "nuclear → heat → electrical"],
      "e": ["That is backwards.", "That describes a fuel-burning station.", "That describes a nuclear station."], "y": "Water high behind the dam falls, turns turbines and generators."}], SRC)],
  learn=learn(
    [("What energy is",
      "Energy is what makes things happen: it lets us move, heat, light and make sounds. We measure it in joules (J); a kilojoule (kJ) is {1000} J.\n"
      "Forms of energy:\n• kinetic (anything moving);\n• potential: gravitational (high up) and elastic (stretched or squeezed);\n"
      "• chemical (food, fuels, batteries);\n• thermal (heat), electrical, light, sound and nuclear."),
     ("Renewable sources",
      "Renewable sources are replaced naturally and will not run out:\n• solar (sunshine, strong in the North);\n• wind;\n"
      "• hydroelectric: Cameroon gets much of its electricity from dams such as Edéa, Song Loulou, Lagdo and Lom Pangar;\n"
      "• biomass: firewood, charcoal and crop waste, renewable only if trees and crops are replanted;\n• geothermal and tidal energy."),
     ("Non-renewable sources",
      "Non-renewable sources took millions of years to form and will run out: petroleum (petrol, diesel, kerosene), natural gas, coal and nuclear fuel.\n"
      "Burning fossil fuels gives carbon dioxide and other pollutants, which harm health and change the climate.\n"
      "Renewables are cleaner, though some depend on the weather (no solar power at night).")],
    key_words=[("energy", "the ability to do work, measured in joules"), ("renewable", "replaced naturally; will not run out"),
               ("non-renewable", "will run out; cannot be replaced in a human lifetime"), ("fossil fuel", "fuel formed from ancient living things: oil, gas, coal")],
    examples=["Kinetic: a moving okada", "Chemical: a bag of groundnuts", "Renewable: Song Loulou dam", "Non-renewable: diesel"],
    mistake=("Firewood is always renewable", "Firewood is renewable only if trees are replanted as fast as they are cut",
             "Cutting forests faster than they grow uses them up.")))

# ---------------------------------------------------------------- 17. Conservation of energy, transducers, calculations
SRC = ["energy"]
L.lesson(D, S, 17, ("p3-17", "Conservation of energy, transducers, energy flow and simple calculations"), [16],
  "Law of conservation of energy: energy cannot be created or destroyed; it only changes from one form to another. The total stays the same.\n"
  "A transducer changes one form of energy into another: microphone (sound → electrical), loudspeaker (electrical → sound), solar cell (light → electrical), dynamo (kinetic → electrical), electric motor (electrical → kinetic), bulb (electrical → light + heat).\n"
  "Energy flow (Sankey) diagrams show input = useful output + wasted output.\n"
  "Calculations: gravitational potential energy PE = mgh; kinetic energy KE = ½mv²; efficiency = useful output ÷ total input × 100%.",
  worked({"m": 2, "h": 5},
         "A {m} kg coconut falls from a height of {h} m. Find its potential energy at the top and its speed just before it hits the ground (ignore air resistance).",
         ["PE = mgh = {m} × {10} × {h} = {m * 10 * h} J.", "All of it becomes kinetic energy: ½mv² = {m * 10 * h}, so v² = {2 * 10 * h}.",
          "v = √{2 * 10 * h} = {sqrt(2 * 10 * h)} m/s."], "PE = {m * 10 * h} J, v = {sqrt(2 * 10 * h)} m/s", checks=["sqrt(2 * 10 * h) == 10"]),
  [card("c3p17-1", "Energy is never lost: it changes form, and the total stays the same.",
        ["A bulb: electrical in = light out + heat out"], "p3-17-trans"),
   card("c3p17-2", "Potential energy PE = mgh; kinetic energy KE = ½mv².",
        ["{2} kg at {5} m: PE = {100} J"], "p3-17-pe"),
   card("c3p17-3", "Efficiency = useful output ÷ total input × {100}%.",
        ["{100} J in, {20} J of light out: {20}%"], "p3-17-eff")],
  [bank("p3-17-trans", 1, "{X.q}", [
     {"q": "What energy change happens in a microphone?", "r": "sound → electrical", "w": ["electrical → sound", "light → electrical", "kinetic → light"],
      "e": ["That is a loudspeaker.", "That is a solar cell.", "No light is produced."], "y": "A microphone turns sound waves into electrical signals."},
     {"q": "What energy change happens in a solar cell?", "r": "light → electrical", "w": ["electrical → light", "chemical → electrical", "heat → sound"],
      "e": ["That is a lamp.", "That is a battery.", "That is not what a solar cell does."], "y": "Sunlight falling on the cell produces electricity."},
     {"q": "Which device changes electrical energy into kinetic energy?", "r": "an electric motor", "w": ["a dynamo", "a microphone", "a solar cell"],
      "e": ["A dynamo does the opposite (kinetic → electrical).", "A microphone gives electrical energy from sound.", "A solar cell gives electrical energy from light."], "y": "A motor turns electricity into motion, as in a fan."},
     {"q": "A bicycle dynamo lights a lamp. What is the energy change in the dynamo?", "r": "kinetic → electrical", "w": ["electrical → kinetic", "chemical → light", "sound → electrical"],
      "e": ["That is a motor.", "The dynamo uses motion, not chemicals.", "That is a microphone."], "y": "The turning wheel drives the dynamo, which produces electricity."}], SRC),
   num("p3-17-pe", 1, "A {m} kg bag of cement is lifted {h} m onto a lorry. Find the gain in potential energy (J). (g = {10} N/kg)", "m * 10 * h",
       ["PE = mgh = {m} × {10} × {h}.", "PE = {answer} J."],
       vars={"m": {"int": [5, 50], "step": 5}, "h": {"int": [1, 3]}},
       misc=[("nog", "m * h", "Include g = {10} N/kg: PE = mgh.")],
       unit="J", sources=SRC),
   num("p3-17-ke", 2, "A motorbike of mass {m} kg moves at {v} m/s. Find its kinetic energy (J).", "m * v * v / 2",
       ["KE = ½mv² = ½ × {m} × {v}².", "= ½ × {m} × {v * v} = {answer} J."],
       vars={"m": {"int": [100, 300], "step": 20}, "v": {"int": [4, 20]}},
       misc=[("nosq", "m * v / 2", "Square the speed: v² = {v * v}."), ("nohalf", "m * v * v", "KE has a half: ½mv².")],
       unit="J", sources=SRC),
   num("p3-17-eff", 2, "A bulb uses {E} J of electrical energy and gives out {U} J of light. Find its efficiency (%).", "U / E * 100",
       ["Efficiency = useful ÷ total × {100}%.", "= {U} ÷ {E} × {100} = {answer}%."],
       vars={"E": {"pick": [100, 200, 400, 500, 1000]}, "U": {"int": [5, 90], "step": 5}},
       misc=[("waste", "100 - U / E * 100", "That is the percentage wasted as heat. Efficiency uses the useful output."), ("noper", "U / E", "Multiply by {100} to get a percentage.")],
       unit="%", sources=SRC, where=["U < E"]),
   num("p3-17-fall", 3, "A stone falls from a height of {h} m. Ignoring air resistance, find its speed just before it reaches the ground (m/s). (g = {10} N/kg)", "sqrt(20 * h)",
       ["PE at the top = KE at the bottom: mgh = ½mv², so v² = {2}gh.", "v² = {2} × {10} × {h} = {20 * h}, so v = {answer} m/s."],
       vars={"h": {"pick": [5, 20, 45, 80, 125, 180]}},
       misc=[("nosqrt", "20 * h", "That is v². Take the square root."), ("noh2", "10 * h", "v² = {2}gh: remember the {2}.")],
       unit="m/s", sources=SRC)],
  learn=learn(
    [("Energy is conserved",
      "The law of conservation of energy: energy cannot be created or destroyed, only changed from one form to another.\n"
      "When a coconut falls, its gravitational potential energy changes into kinetic energy; when it hits the ground, into sound and heat. The total amount of energy stays the same.\n"
      "When we say energy is 'wasted', we mean it has gone into a form we did not want, usually heat."),
     ("Transducers and energy flow",
      "Devices that change energy from one form to another are transducers:\n"
      "• microphone: sound → electrical; loudspeaker: electrical → sound;\n• solar cell: light → electrical; bulb: electrical → light and heat;\n"
      "• dynamo: kinetic → electrical; motor: electrical → kinetic; battery: chemical → electrical.\n"
      "An energy flow (Sankey) diagram shows the input split into useful and wasted outputs; the arrows add up to the input."),
     ("Working it out",
      "• Gravitational potential energy: PE = mgh. A {50} kg bag lifted {2} m gains {50} × {10} × {2} = {1000} J.\n"
      "• Kinetic energy: KE = ½mv². A {100} kg motorbike at {10} m/s has {5000} J.\n"
      "• Efficiency = useful output ÷ total input × {100}%. A bulb giving {20} J of light from {100} J is {20}% efficient; the other {80} J become heat.")],
    key_words=[("conservation of energy", "energy is not created or destroyed, only changed"), ("transducer", "a device that changes energy from one form to another"),
               ("efficiency", "useful output ÷ total input × {100}%"), ("Sankey diagram", "a diagram showing how energy input divides into outputs")],
    examples=["Loudspeaker: electrical → sound", "PE of {3} kg at {4} m: {120} J", "KE of {2} kg at {3} m/s: {9} J"],
    mistake=("Energy is used up when a bulb is switched on", "Electrical energy is changed into light and heat; the total is the same",
             "Energy is never destroyed; it only changes form.")))
