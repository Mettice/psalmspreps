"""Form 4 Chemistry, Term 1, rows 21-25: basic mole calculations, finding formulae by experiment, percentage
composition, empirical and molecular formulae, masses and volumes from equations.
Run: python tools/authoring/form4/chem_moles2.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order, match
from common import goal, bank

L.use_class("form-4", "Form 4")
D, S = "chemistry", "chemistry"
SRC = ["moles"]

COMMON = ["H2O", "CO2", "NaCl", "CaCO3", "H2SO4", "NH3", "MgO", "CuO", "NaOH", "KNO3", "ZnO"]

# ---------------------------------------------------------------- 21. Basic calculations on the mole concept
L.lesson(D, S, 21, ("k4-21", "Carry out basic calculations with moles, mass, particles and gas volume"), [20],
  "Three relations link a mole to things that can be measured.\n"
  "• moles = mass ÷ molar mass, so mass = moles × molar mass.\n"
  "• number of particles = moles × 6.02 × 10²³.\n"
  "• volume of a gas at s.t.p. = moles × 22.4 dm³, so moles = volume ÷ 22.4.\n"
  "Always write down what is given, change it to moles, and then change the moles to what is asked for.\n"
  "Example: 11 g of carbon dioxide. Molar mass 44 g/mol, so moles = 11 ÷ 44 = 0.25 mol; "
  "volume at s.t.p. = 0.25 × 22.4 = 5.6 dm³; molecules = 0.25 × 6.02 × 10²³.",
  worked({"m": 11, "F": "CO2"},
         "Find the number of moles in {m} g of {formula(F)}, and the volume it would fill at s.t.p.",
         ["The molar mass of {formula(F)} is {molarMass(F)} g/mol.",
          "moles = mass ÷ molar mass = {m} ÷ {molarMass(F)} = {molesOf(m, F)} mol.",
          "At s.t.p. {1} mol fills {22.4} dm³.",
          "Volume = {molesOf(m, F)} × {22.4} = {gasVolume(molesOf(m, F))} dm³."],
         "{molesOf(m, F)} mol, filling {gasVolume(molesOf(m, F))} dm³",
         checks=["molesOf(11, 'CO2') == 0.25"]),
  [card("c4k21-1", "moles = mass ÷ molar mass.",
        ["{44} g of {formula('CO2')} ÷ {44} g/mol = {1} mol"], "k4-21-moles"),
   card("c4k21-2", "mass = moles × molar mass.",
        ["{0.5} mol of {formula('H2O')} × {18} g/mol = {9} g"], "k4-21-mass"),
   card("c4k21-3", "At s.t.p., volume = moles × {22.4} dm³.",
        ["{0.25} mol of a gas fills {5.6} dm³"], "k4-21-vol")],
  [num("k4-21-moles", 1, "How many moles are there in {m} g of {formula(F)}?",
       "roundTo(molesOf(m, F), 0.001)",
       ["Molar mass of {formula(F)} = {molarMass(F)} g/mol.", "moles = {m} ÷ {molarMass(F)} = {answer} mol."],
       vars={"F": {"pick": COMMON}, "k": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 5]}, "m": {"expr": "roundTo(k * molarMass(F), 0.01)"}},
       misc=[("mult", "roundTo(massOf(m, F), 0.01)", "Divide the mass by the molar mass."),
             ("swap", "roundTo(molarMass(F) / m, 0.001)", "moles = mass ÷ molar mass, not molar mass ÷ mass.")],
       sources=SRC, unit="mol"),
   num("k4-21-mass", 1, "What is the mass, in grams, of {n} mol of {formula(F)}?",
       "massOf(n, F)",
       ["Molar mass of {formula(F)} = {molarMass(F)} g/mol.", "mass = {n} × {molarMass(F)} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 3]}, "F": {"pick": COMMON}},
       misc=[("div", "roundTo(molesOf(n, F), 0.0001)", "mass = moles × molar mass."),
             ("one", "molarMass(F)", "{molarMass(F)} g is one mole; here there are {n} mol.")],
       sources=SRC, unit="g"),
   num("k4-21-vol", 2, "What volume, in dm³ at s.t.p., is filled by {m} g of {formula(F)} gas?",
       "roundTo(gasVolume(molesOf(m, F)), 0.01)",
       ["moles = {m} ÷ {molarMass(F)} = {roundTo(molesOf(m, F), 0.001)} mol.",
        "volume = moles × {22.4} = {answer} dm³."],
       vars={"F": {"pick": ["CO2", "NH3", "SO2", "H2S", "N2", "O2", "H2", "CH4"]},
             "k": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}, "m": {"expr": "roundTo(k * molarMass(F), 0.01)"}},
       misc=[("nomole", "roundTo(gasVolume(m), 0.01)", "Change the mass to MOLES first, then multiply by {22.4}."),
             ("div", "roundTo(volumeToMoles(m), 0.001)", "Multiply the moles by {22.4} dm³/mol.")],
       sources=SRC, unit="dm³"),
   num("k4-21-back", 2, "What mass, in grams, of {formula(F)} gas fills {v} dm³ at s.t.p.?",
       "roundTo(massOf(volumeToMoles(v), F), 0.01)",
       ["moles = volume ÷ {22.4} = {v} ÷ {22.4} = {roundTo(volumeToMoles(v), 0.001)} mol.",
        "mass = moles × {molarMass(F)} = {answer} g."],
       vars={"F": {"pick": ["CO2", "NH3", "SO2", "N2", "O2", "H2", "CH4"]}, "v": {"pick": [2.24, 4.48, 5.6, 11.2, 22.4, 44.8]}},
       misc=[("novol", "roundTo(massOf(v, F), 0.01)", "Change the volume to MOLES first: divide by {22.4}."),
             ("mult", "roundTo(massOf(gasVolume(v), F), 0.01)", "Divide the volume by {22.4}; do not multiply.")],
       sources=SRC, unit="g"),
   num("k4-21-count", 3, "How many moles of {formula(F)} hold {p} times the Avogadro number of molecules?",
       "p",
       ["The Avogadro number of molecules is {1} mol.", "{p} times that number is {p} mol."],
       vars={"p": {"pick": [0.1, 0.25, 0.5, 1.5, 2, 3]}, "F": {"pick": ["CO2", "H2O", "NH3", "O2"]}},
       misc=[("avog", "roundTo(p * 6.02, 0.01)", "The Avogadro number IS one mole: no further multiplying is needed."),
             ("div", "roundTo(1 / p, 0.001)", "{p} times the number of particles is {p} times the number of moles.")],
       sources=SRC, unit="mol")],
  learn=learn(
    [goal("change between mass, moles, number of particles and gas volume in any direction.",
          "Lesson {20} (the mole and the Avogadro constant) and Lesson {19} (molar mass and molar volume).",
          "Lessons {22} to {27}, where these steps are used inside larger calculations."),
     ("The three links",
      "Everything in this chapter uses three relations, with MOLES always in the middle.\n"
      "• mass: moles = mass ÷ molar mass, and mass = moles × molar mass;\n"
      "• particles: number = moles × L, where L = {6.02} × {10} to the power {23};\n"
      "• gas volume at s.t.p.: volume = moles × {22.4} dm³, and moles = volume ÷ {22.4}.\n"
      "A question that gives one of these and asks for another is solved in two steps: change what is given into moles, "
      "then change the moles into what is asked for."),
     ("Worked examples",
      "{11} g of carbon dioxide:\n"
      "• molar mass {44} g/mol, so moles = {11} ÷ {44} = {0.25} mol;\n"
      "• volume at s.t.p. = {0.25} × {22.4} = {5.6} dm³;\n"
      "• molecules = {0.25} × {6.02} × {10} to the power {23}.\n"
      "{5.6} dm³ of oxygen at s.t.p.:\n"
      "• moles = {5.6} ÷ {22.4} = {0.25} mol;\n• mass = {0.25} × {32} = {8} g.\n"
      "Always write the unit with the answer: mol, g or dm³. If the answer looks far too large or small, check whether "
      "you multiplied where you should have divided.")],
    key_words=[("molar mass", "the mass of one mole, in g/mol"),
               ("s.t.p.", "standard temperature and pressure: {0} °C and one atmosphere"),
               ("dm³", "a cubic decimetre, the same as a litre")],
    examples=["{9} g of {formula('H2O')} = {0.5} mol", "{0.5} mol of gas = {11.2} dm³ at s.t.p.", "{2} mol = {1.204} × {10} to the power {24} particles"],
    mistake=("moles = molar mass ÷ mass", "moles = mass ÷ molar mass",
             "Check with a simple case: {44} g of {formula('CO2')} must be {1} mol, and {44} ÷ {44} = {1}.")))

# ---------------------------------------------------------------- 22. Determining formulae by experiment
EXPT = [
    {"q": "In finding the formula of magnesium oxide, why is the crucible lid lifted from time to time?",
     "r": "To let air in so the magnesium can go on burning, while keeping the white smoke in",
     "w": ["To let the magnesium oxide escape", "To cool the crucible", "To let water in"],
     "e": ["Letting the oxide escape would make the mass found too small; the lid keeps it in.",
           "Cooling would stop the reaction, which is the opposite of what is wanted.",
           "Water must be kept out; it would react with the product."],
     "y": "Oxygen is needed for the reaction, but the white smoke of magnesium oxide must not be lost."},
    {"q": "Why is the crucible heated, cooled and weighed again, more than once?", "r": "To make sure the reaction is complete, shown by a constant mass",
     "w": ["To make the crucible lighter", "To take the average of the readings", "To dry the crucible"],
     "e": ["The mass does not fall; it rises as oxygen is taken in.",
           "The readings are not averaged; the aim is a mass that stops changing.",
           "Drying is not the purpose, though the crucible must be dry at the start."],
     "y": "Heating to CONSTANT MASS shows that all the magnesium has reacted."},
    {"q": "In finding the formula of copper oxide, why is the hydrogen allowed to flow for a while before it is lit?",
     "r": "To sweep all the air out of the tube, so the hydrogen does not explode",
     "w": ["To warm the copper oxide", "To dry the copper oxide", "To measure the volume of hydrogen"],
     "e": ["The flame does the heating, not the gas flow.",
           "The gas is dried before it reaches the tube, not by waiting.",
           "No volume is measured in this experiment."],
     "y": "A mixture of hydrogen and air explodes when lit, so the air must be swept out first."},
    {"q": "In the copper oxide experiment, the mass falls as the reaction goes on. Why?",
     "r": "Oxygen is removed from the oxide and leaves as water vapour",
     "w": ["Copper evaporates", "Hydrogen is added to the copper", "The crucible burns away"],
     "e": ["Copper does not evaporate at the temperature used.",
           "The hydrogen leaves with the oxygen as water; it does not stay behind.",
           "The apparatus does not burn."],
     "y": "{formula('CuO')} + {formula('H2')} → Cu + {formula('H2O')}: the oxygen leaves the solid."},
    {"q": "Which masses must be measured to find the formula of magnesium oxide?",
     "r": "The crucible empty, the crucible with magnesium, and the crucible with the product",
     "w": ["Only the magnesium at the start", "Only the product at the end", "The crucible and the lid separately"],
     "e": ["The mass of oxygen taken in can only be found by weighing the product as well.",
           "Without the starting mass of magnesium, the ratio cannot be found.",
           "The lid is weighed with the crucible throughout, so it cancels out."],
     "y": "Mass of magnesium and mass of oxygen are both needed, and the oxygen is the difference between the last two."},
]

L.lesson(D, S, 22, ("k4-22", "Find the formulae of magnesium oxide and copper oxide by experiment"), [21],
  "Magnesium oxide, by combination:\n"
  "Weigh a crucible and lid; add magnesium ribbon and weigh again. Heat strongly, lifting the lid from time to time to "
  "let air in without letting the white smoke escape. Heat, cool and weigh until the mass is constant.\n"
  "mass of Mg = (crucible + Mg) − crucible; mass of O = (crucible + product) − (crucible + Mg).\n"
  "Divide each mass by its relative atomic mass and take the simplest ratio: 1 : 1, so the formula is MgO.\n"
  "Copper oxide, by reduction:\n"
  "Weigh a dry tube holding copper(II) oxide. Pass dry hydrogen over it, letting the gas flow before lighting it, so that "
  "no air is left to explode. Heat; the black solid turns pink-brown. Cool in hydrogen and weigh.\n"
  "mass of O is the loss in mass. The ratio again gives CuO.",
  worked({"mg": 2.4, "mo": 4.0},
         "In an experiment, {mg} g of magnesium gave {mo} g of magnesium oxide. Find the formula.",
         ["Mass of oxygen = {mo} − {mg} = {roundTo(mo - mg, 0.01)} g.",
          "Moles of Mg = {mg} ÷ {ram('Mg')} = {roundTo(mg / ram('Mg'), 0.001)}.",
          "Moles of O = {roundTo(mo - mg, 0.01)} ÷ {ram('O')} = {roundTo((mo - mg) / ram('O'), 0.001)}.",
          "Divide both by the smaller: the ratio is {1} : {1}."],
         "{formula('MgO')}",
         checks=["empiricalOf(['Mg', 'O'], [2.4, 1.6]) == 'MgO'"]),
  [card("c4k22-1", "Heat, cool and weigh until the mass is constant: that shows the reaction is complete.",
        ["the mass rises as oxygen is taken in, then stops changing"], "k4-22-method"),
   card("c4k22-2", "Divide each mass by its relative atomic mass, then take the simplest ratio.",
        ["{2.4} ÷ {24} = {0.1} and {1.6} ÷ {16} = {0.1}: a ratio of {1} : {1}"], "k4-22-formula"),
   card("c4k22-3", "Copper oxide is reduced by hydrogen: the mass falls as oxygen leaves.",
        ["{formula('CuO')} + {formula('H2')} → Cu + {formula('H2O')}"], "k4-22-copper")],
  [bank("k4-22-method", 1, "{X.q}", EXPT, SRC),
   num("k4-22-oxygen", 1, "A crucible holds {mg} g of magnesium. After burning, the product has a mass of {mo} g. What mass of oxygen, in grams, has combined?",
       "roundTo(mo - mg, 0.01)",
       ["The gain in mass is the oxygen taken in.", "{mo} − {mg} = {answer} g."],
       vars={"k": {"pick": [0.05, 0.1, 0.15, 0.2, 0.25]}, "mg": {"expr": "roundTo(k * 24, 0.01)"}, "mo": {"expr": "roundTo(k * 40, 0.01)"}},
       misc=[("sum", "roundTo(mo + mg, 0.01)", "The oxygen is the INCREASE in mass: subtract."),
             ("whole", "mo", "{mo} g is the mass of the whole product, magnesium and oxygen together.")],
       sources=SRC, unit="g"),
   mcq("k4-22-formula", 2, "{mg} g of magnesium combines with {mo} g of oxygen. What is the formula of the oxide?",
       "{empiricalOf(['Mg', 'O'], [mg, mo])}",
       [("{formula('Mg2O')}", "w1"), ("{formula('MgO2')}", "w2"), ("{formula('Mg2O3')}", "w3")],
       ["Moles of Mg = {mg} ÷ {ram('Mg')} = {roundTo(mg / ram('Mg'), 0.001)}; moles of O = {mo} ÷ {ram('O')} = {roundTo(mo / ram('O'), 0.001)}.",
        "Divide both by the smaller to get the simplest ratio.", "So the formula is {answer}."],
       vars={"k": {"pick": [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]}, "mg": {"expr": "roundTo(k * 24, 0.01)"}, "mo": {"expr": "roundTo(k * 16, 0.01)"}},
       misc=[("w1", "That would need twice as many moles of magnesium as of oxygen; here they are equal."),
             ("w2", "That would need twice as many moles of oxygen as of magnesium; here they are equal."),
             ("w3", "The moles come out equal, so the ratio is {1} : {1}.")],
       sources=SRC),
   num("k4-22-copper", 2, "{mo} g of copper(II) oxide is reduced by hydrogen and leaves {mc} g of copper. What mass of oxygen, in grams, was in the oxide?",
       "roundTo(mo - mc, 0.01)",
       ["The loss in mass is the oxygen removed.", "{mo} − {mc} = {answer} g."],
       vars={"k": {"pick": [0.05, 0.1, 0.2, 0.25, 0.5]}, "mo": {"expr": "roundTo(k * 80, 0.01)"}, "mc": {"expr": "roundTo(k * 64, 0.01)"}},
       misc=[("sum", "roundTo(mo + mc, 0.01)", "The oxygen is the LOSS in mass: subtract."),
             ("copper", "mc", "{mc} g is the copper left behind.")],
       sources=SRC, unit="g"),
   num("k4-22-check", 3, "In the copper oxide experiment, {mo} g of copper(II) oxide gave {mc} g of copper. How many moles of oxygen atoms were removed?",
       "roundTo((mo - mc) / ram('O'), 0.001)",
       ["Mass of oxygen = {mo} − {mc} = {roundTo(mo - mc, 0.01)} g.",
        "Moles of oxygen atoms = {roundTo(mo - mc, 0.01)} ÷ {ram('O')} = {answer} mol."],
       vars={"k": {"pick": [0.1, 0.2, 0.25, 0.5, 1]}, "mo": {"expr": "roundTo(k * 80, 0.01)"}, "mc": {"expr": "roundTo(k * 64, 0.01)"}},
       misc=[("mass", "roundTo(mo - mc, 0.01)", "That is the MASS of oxygen; divide it by {ram('O')} for the moles."),
             ("copper", "roundTo(mc / ram('Cu'), 0.001)", "That is the moles of copper; the question asks for oxygen.")],
       sources=SRC, unit="mol")],
  learn=learn(
    [goal("describe both experiments and use the masses to work out the formula of the oxide.",
          "Lesson {21} (moles from mass) and Form Three oxidation and reduction.",
          "Lesson {24} (empirical formulae from any data) and practical work in the laboratory."),
     ("Magnesium oxide, by combination",
      "• Weigh a clean, dry crucible with its lid.\n• Add a coil of cleaned magnesium ribbon and weigh again.\n"
      "• Heat strongly, lifting the lid from time to time. Air must get in for the reaction, but the white smoke must not "
      "get out, or the mass of the product will be too small.\n"
      "• When all the magnesium has burned, cool and weigh. Heat, cool and weigh again until the mass is CONSTANT, "
      "which shows that the reaction is complete.\n"
      "mass of magnesium = (crucible + Mg) − crucible;\nmass of oxygen = (crucible + product) − (crucible + Mg).\n"
      "Divide each by its relative atomic mass: {2.4} ÷ {24} = {0.1} and {1.6} ÷ {16} = {0.1}. The ratio is {1} : {1}, so the formula is {formula('MgO')}."),
     ("Copper oxide, by reduction",
      "• Weigh a dry reduction tube holding copper(II) oxide.\n"
      "• Pass DRY hydrogen over it. Let the gas flow for a while BEFORE lighting it at the jet, so that all the air is "
      "swept out: a mixture of hydrogen and air explodes.\n"
      "• Heat the oxide. The black solid turns pink-brown as copper forms, and water collects in the cool part of the tube.\n"
      "• Cool in a stream of hydrogen, so that the hot copper cannot be oxidised again by air, then weigh.\n"
      "{formula('CuO')} + {formula('H2')} → Cu + {formula('H2O')}\n"
      "mass of copper = final − tube; mass of oxygen = the loss in mass. "
      "{6.4} ÷ {64} = {0.1} and {1.6} ÷ {16} = {0.1}: the ratio is {1} : {1}, so the formula is {formula('CuO')}.")],
    key_words=[("constant mass", "a mass that no longer changes on further heating, showing the reaction is complete"),
               ("crucible", "a small dish that stands strong heating"),
               ("reduction", "removal of oxygen from a compound"),
               ("simplest ratio", "the smallest whole-number ratio of the moles")],
    examples=["{2.4} g Mg + {1.6} g O → {formula('MgO')}", "{8} g {formula('CuO')} → {6.4} g Cu + {1.6} g O"],
    mistake=("the mass of oxygen in the magnesium oxide experiment is the mass of the product", "it is the product minus the magnesium",
             "The product holds both the magnesium and the oxygen; subtract to find the oxygen alone.")))

# ---------------------------------------------------------------- 23. Percentage composition by mass
PCCHECK = [
    {"q": "The percentages by mass of all the elements in a compound are added. What should the total be?", "r": "{100} per cent",
     "w": ["It depends on the compound", "More than {100} per cent for a large molecule", "Less than {100} per cent"],
     "e": ["The whole is always the sum of its parts, whatever the compound.",
           "The parts cannot add to more than the whole.",
           "Nothing is left out: every atom belongs to one of the elements."],
     "y": "Every atom belongs to one element, so the masses add up to the whole formula mass."},
    {"q": "A pupil finds that a compound is {40} per cent carbon and {70} per cent oxygen. What does this show?",
     "r": "A mistake has been made, because the total is more than {100} per cent",
     "w": ["The compound holds another element as well", "The compound is a mixture", "Nothing is wrong"],
     "e": ["Another element would make the total even larger, not smaller.",
           "Even a mixture's percentages must add to {100}.",
           "A total above {100} per cent is impossible."],
     "y": "The percentages of the parts can never add to more than the whole."},
    {"q": "Which fertiliser carries the most nitrogen for each kilogram bought?",
     "r": "Urea, {formula('CO(NH2)2')}, at about {47} per cent nitrogen",
     "w": ["Ammonium sulphate, at about {21} per cent", "Ammonium nitrate, at about {35} per cent",
           "Sodium nitrate, at about {16} per cent"],
     "e": ["Ammonium sulphate carries a heavy sulphate group, so its nitrogen percentage is low.",
           "Ammonium nitrate is good, but urea is better still.",
           "Sodium nitrate carries a heavy sodium atom for each nitrogen."],
     "y": "The smaller the rest of the formula, the larger the share of the mass that is nitrogen."},
    {"q": "Why does a mining company care about the percentage of metal in an ore?",
     "r": "It tells them how much metal each tonne of rock will give, and so whether mining is worth the cost",
     "w": ["It tells them how deep the ore lies", "It tells them the colour of the metal",
           "It tells them how hard the rock is"],
     "e": ["Depth is found by surveying, not from the formula.",
           "The colour has nothing to do with the percentage by mass.",
           "Hardness is a physical property of the rock."],
     "y": "Haematite, {formula('Fe2O3')}, is {70} per cent iron, so {100} tonnes of pure ore would give {70} tonnes of iron."},
]

L.lesson(D, S, 23, ("k4-23", "Calculate percentage composition by mass"), [21],
  "The percentage by mass of an element in a compound is:\n"
  "(mass of that element in one formula unit ÷ relative formula mass) × 100 per cent.\n"
  "Steps: work out the relative formula mass; multiply the relative atomic mass of the element by how many atoms of it "
  "there are; divide and multiply by 100.\n"
  "Example: water, H2O, Mr = 18. Hydrogen: 2 × 1 = 2, so 2/18 × 100 = 11.1 per cent. Oxygen: 16/18 × 100 = 88.9 per cent. "
  "The percentages add up to 100.\n"
  "The same idea tells a farmer which fertiliser carries the most nitrogen per bag, and tells a miner how much metal an ore holds.",
  worked({"F": "CaCO3", "E": "Ca"},
         "Find the percentage by mass of {E} in {formula(F)}.",
         ["Relative formula mass of {formula(F)} = {molarMass(F)}.",
          "There {atomCount(F, E) == 1 ? 'is' : 'are'} {atomCount(F, E)} atom of {E}, of mass {atomCount(F, E) * ram(E)}.",
          "Percentage = {atomCount(F, E) * ram(E)} ÷ {molarMass(F)} × {100}."],
         "{roundTo(percentMass(F, E), 0.1)} per cent",
         checks=["molarMass('CaCO3') == 100"]),
  [card("c4k23-1", "Percentage = (mass of the element ÷ relative formula mass) × {100}.",
        ["{formula('H2O')}: hydrogen is {2} ÷ {18} × {100} = {11.1} per cent"], "k4-23-pc"),
   card("c4k23-2", "Count every atom of the element in the formula.",
        ["{formula('H2SO4')}: oxygen is {4} × {16} = {64} out of {98}"], "k4-23-count"),
   card("c4k23-3", "The percentages of all the elements add up to {100}.",
        ["{formula('H2O')}: {11.1} + {88.9} = {100}"], "k4-23-sum")],
  [num("k4-23-pc", 1, "Find the percentage by mass of {E} in {formula(F)}. Give your answer to {1} decimal place.",
       "roundTo(percentMass(F, E), 0.1)",
       ["Relative formula mass of {formula(F)} = {molarMass(F)}.",
        "{E}: {atomCount(F, E)} × {ram(E)} = {atomCount(F, E) * ram(E)}.",
        "Percentage = {atomCount(F, E) * ram(E)} ÷ {molarMass(F)} × {100} = {answer} per cent."],
       vars={"P": {"pick": [["H2O", "O"], ["CO2", "C"], ["CaCO3", "Ca"], ["MgO", "Mg"], ["NaCl", "Na"],
                            ["H2SO4", "S"], ["CuO", "Cu"], ["Fe2O3", "Fe"], ["NH3", "N"], ["ZnO", "Zn"]]},
             "F": {"expr": "P[0]"}, "E": {"expr": "P[1]"}},
       misc=[("swap", "roundTo(molarMass(F) / (atomCount(F, E) * ram(E)) * 100, 0.1)", "Divide the mass of the ELEMENT by the whole formula mass."),
             ("noatoms", "roundTo(ram(E) / molarMass(F) * 100, 0.1)", "Count every atom of {E}: there are {atomCount(F, E)}.", "atomCount(F, E) > 1")],
       sources=SRC, unit="%"),
   num("k4-23-count", 1, "What is the total mass of {E} in one formula unit of {formula(F)}?",
       "atomCount(F, E) * ram(E)",
       ["{formula(F)} holds {atomCount(F, E)} atoms of {E}.",
        "{atomCount(F, E)} × {ram(E)} = {answer}."],
       vars={"P": {"pick": [["H2SO4", "O"], ["CaCO3", "O"], ["Fe2O3", "O"], ["NH3", "H"], ["H2O", "H"], ["CO2", "O"], ["Al2O3", "O"]]},
             "F": {"expr": "P[0]"}, "E": {"expr": "P[1]"}},
       misc=[("one", "ram(E)", "There are {atomCount(F, E)} atoms of {E}, not one."),
             ("whole", "molarMass(F)", "{molarMass(F)} is the mass of the WHOLE formula unit.")],
       sources=SRC),
   num("k4-23-mass", 2, "What mass of {E}, in grams, is there in {m} g of {formula(F)}? Give your answer to {1} decimal place.",
       "roundTo(m * percentMass(F, E) / 100, 0.1)",
       ["{E} is {roundTo(percentMass(F, E), 0.1)} per cent of {formula(F)} by mass.",
        "{roundTo(percentMass(F, E), 0.1)} per cent of {m} g = {answer} g."],
       vars={"P": {"pick": [["CaCO3", "Ca"], ["MgO", "Mg"], ["CuO", "Cu"], ["Fe2O3", "Fe"], ["ZnO", "Zn"], ["H2O", "O"]]},
             "F": {"expr": "P[0]"}, "E": {"expr": "P[1]"}, "m": {"pick": [20, 25, 40, 50, 100, 200]}},
       misc=[("pc", "roundTo(percentMass(F, E), 0.1)", "That is the PERCENTAGE; apply it to the {m} g given."),
             ("whole", "m", "Only part of the {m} g is {E}.")],
       sources=SRC, unit="g"),
   bank("k4-23-sum", 2, "{X.q}", PCCHECK, SRC),
   num("k4-23-fert", 3, "A farmer compares two fertilisers. What is the percentage by mass of nitrogen in {formula(F)}? Give your answer to {1} decimal place.",
       "roundTo(percentMass(F, 'N'), 0.1)",
       ["Relative formula mass of {formula(F)} = {molarMass(F)}.",
        "Nitrogen: {atomCount(F, 'N')} × {ram('N')} = {atomCount(F, 'N') * ram('N')}.",
        "Percentage = {atomCount(F, 'N') * ram('N')} ÷ {molarMass(F)} × {100} = {answer} per cent."],
       vars={"F": {"pick": ["NH4NO3", "(NH4)2SO4", "NaNO3", "KNO3", "CO(NH2)2", "NH3"]}},
       misc=[("one", "roundTo(ram('N') / molarMass(F) * 100, 0.1)", "Count every nitrogen atom: there are {atomCount(F, 'N')}.", "atomCount(F, 'N') > 1"),
             ("swap", "roundTo(molarMass(F) / (atomCount(F, 'N') * ram('N')) * 100, 0.1)", "Divide the nitrogen mass by the whole formula mass.")],
       sources=SRC, unit="%")],
  learn=learn(
    [goal("work out the percentage by mass of any element in a compound, and use it to compare fertilisers or ores.",
          "Lesson {19} (relative formula mass) and Lesson {21} (mole calculations).",
          "Lesson {24}, which runs this calculation backwards to find a formula from percentages."),
     ("The calculation",
      "Percentage by mass of an element = (mass of that element in one formula unit ÷ relative formula mass) × {100}.\n"
      "Water, {formula('H2O')}, Mr = {18}:\n"
      "• hydrogen: {2} × {1} = {2}, so {2} ÷ {18} × {100} = {11.1} per cent;\n"
      "• oxygen: {16} ÷ {18} × {100} = {88.9} per cent.\n"
      "The two add up to {100}, which is a useful check.\n"
      "Count EVERY atom of the element. In {formula('H2SO4')} (Mr = {98}) the oxygen is {4} × {16} = {64}, "
      "so {64} ÷ {98} × {100} = {65.3} per cent."),
     ("Why it matters",
      "A farmer buying fertiliser wants the most nitrogen for the money, so the percentage of nitrogen matters more than the "
      "mass of the bag:\n"
      "• ammonium nitrate {formula('NH4NO3')} (Mr {80}): nitrogen {28} ÷ {80} × {100} = {35} per cent;\n"
      "• ammonium sulphate {formula('(NH4)2SO4')} (Mr {132}): nitrogen {28} ÷ {132} × {100} = {21.2} per cent;\n"
      "• urea {formula('CO(NH2)2')} (Mr {60}): nitrogen {28} ÷ {60} × {100} = {46.7} per cent.\n"
      "In the same way, a miner works out how much metal an ore carries: haematite {formula('Fe2O3')} is {70} per cent iron, "
      "so {100} tonnes of pure ore would give {70} tonnes of iron.")],
    key_words=[("percentage composition", "the percentage by mass of each element in a compound"),
               ("relative formula mass", "the sum of the relative atomic masses in the formula"),
               ("ore", "a rock from which a metal can be taken")],
    examples=["{formula('H2O')}: {11.1} per cent H", "{formula('CaCO3')}: {40} per cent Ca", "urea: {46.7} per cent N"],
    mistake=("the percentage of oxygen in {formula('H2SO4')} is {16} ÷ {98} × {100}", "it is {4} × {16} ÷ {98} × {100}",
             "There are {4} oxygen atoms in the formula, so their total mass is {64}.")))
