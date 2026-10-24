"""Form 4 Chemistry, Term 1, rows 24-29: empirical and molecular formulae, masses and volumes from equations,
limiting reagents and yield, percentage yield, balancing by the mole concept, and state symbols.
Run: python tools/authoring/form4/chem_moles3.py"""
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

# ---------------------------------------------------------------- 24. Empirical and molecular formulae
EMP = [
    {"q": "What is an empirical formula?", "r": "The simplest whole-number ratio of the atoms in a compound",
     "w": ["The actual number of atoms in one molecule", "The formula of the simplest compound of two elements",
           "A formula found only by experiment"],
     "e": ["That is the MOLECULAR formula.",
           "'Empirical' describes the ratio, not how simple the compound is.",
           "It can be worked out from a molecular formula on paper as well."],
     "y": "{formula('C6H12O6')} has the empirical formula {formula('CH2O')}: the ratio {1} : {2} : {1}."},
    {"q": "What is a molecular formula?", "r": "The actual number of atoms of each element in one molecule",
     "w": ["The simplest ratio of the atoms", "The formula of an ionic compound",
           "The formula written with state symbols"],
     "e": ["That is the EMPIRICAL formula.",
           "Ionic compounds have formula units, not molecules.",
           "State symbols are added to an equation; they are not part of the formula."],
     "y": "Glucose has the molecular formula {formula('C6H12O6')}, which is {6} times its empirical formula {formula('CH2O')}."},
    {"q": "A compound has the empirical formula {formula('CH2')} and a relative molecular mass of {42}. What is its molecular formula?",
     "r": "{formula('C3H6')}", "w": ["{formula('CH2')}", "{formula('C2H4')}", "{formula('C4H8')}"],
     "e": ["{formula('CH2')} has a mass of only {14}, not {42}.",
           "{formula('C2H4')} has a mass of {28}.",
           "{formula('C4H8')} has a mass of {56}, which is too much."],
     "y": "{42} ÷ {14} = {3}, so the molecular formula is {3} times the empirical one."},
    {"q": "Why do ionic compounds have only an empirical formula?", "r": "They are lattices of ions, with no separate molecules",
     "w": ["Their molecules are too large to write", "They have no fixed composition",
           "Their molecular formula is always the same as the empirical one by chance"],
     "e": ["Size is not the reason; there are no molecules at all.",
           "An ionic compound does have a fixed composition.",
           "There is no molecule for a molecular formula to describe."],
     "y": "{formula('NaCl')} shows the ratio of ions in the lattice; there is no {formula('NaCl')} molecule."},
    {"q": "In finding an empirical formula from percentages, what is the first step?", "r": "Divide each percentage by the relative atomic mass of that element",
     "w": ["Add the percentages together", "Multiply each percentage by the relative atomic mass",
           "Divide each percentage by {100}"],
     "e": ["The percentages add to {100}, which is a check but not a step.",
           "Dividing, not multiplying, turns a mass into a number of moles.",
           "Dividing by {100} changes nothing about the ratio."],
     "y": "Percentage by mass behaves like a mass in grams, so dividing by Ar gives the moles."},
]

L.lesson(D, S, 24, ("k4-24", "Find empirical and molecular formulae"), [23],
  "The empirical formula is the simplest whole-number ratio of the atoms in a compound. "
  "The molecular formula is the actual number of atoms in one molecule.\n"
  "To find an empirical formula from masses or percentages:\n"
  "1. Write the mass (or percentage) of each element.\n"
  "2. Divide each by its relative atomic mass: this gives the moles.\n"
  "3. Divide every answer by the smallest of them.\n"
  "4. If the numbers are not whole, multiply them all until they are.\n"
  "To go from the empirical formula to the molecular formula, divide the relative molecular mass by the mass of the "
  "empirical formula; the answer is how many times to multiply.\n"
  "Example: 85.7 per cent carbon and 14.3 per cent hydrogen gives CH2. If Mr = 42, then 42 ÷ 14 = 3, so the molecular "
  "formula is C3H6. Ionic compounds have only an empirical formula.",
  worked({"pc": 85.7, "ph": 14.3, "M": 42},
         "A hydrocarbon is {pc} per cent carbon and {ph} per cent hydrogen, and its relative molecular mass is {M}. Find its molecular formula.",
         ["Divide each percentage by the relative atomic mass: C {pc} ÷ {ram('C')}, H {ph} ÷ {ram('H')}.",
          "That gives about {roundTo(pc / ram('C'), 0.01)} and {roundTo(ph / ram('H'), 0.01)} moles.",
          "Divide both by the smaller: the ratio is about {1} : {2}, so the empirical formula is {formula('CH2')}.",
          "The empirical formula mass is {molarMass('CH2')}, and {M} ÷ {molarMass('CH2')} = {formulaTimes('CH2', M)}."],
         "{formula('C3H6')}",
         checks=["formulaTimes('CH2', 42) == 3"]),
  [card("c4k24-1", "Empirical formula: the simplest ratio. Molecular formula: the actual atoms in a molecule.",
        ["{formula('C6H12O6')} has the empirical formula {formula('CH2O')}"], "k4-24-define"),
   card("c4k24-2", "Divide each mass or percentage by its relative atomic mass, then by the smallest answer.",
        ["{2.4} ÷ {24} = {0.1}; {1.6} ÷ {16} = {0.1}; the ratio is {1} : {1}"], "k4-24-emp"),
   card("c4k24-3", "Molecular formula = empirical formula × (Mr ÷ empirical formula mass).",
        ["{formula('CH2')} with Mr {42}: {42} ÷ {14} = {3}, so {formula('C3H6')}"], "k4-24-mol")],
  [bank("k4-24-define", 1, "{X.q}", EMP, SRC),
   mcq("k4-24-emp", 2, "A compound holds {m1} g of {E1} and {m2} g of {E2}. What is its empirical formula?",
       "{formula(empiricalOf([E1, E2], [m1, m2]))}",
       [("{formula(E1 + '2' + E2)}", "w1"), ("{formula(E1 + E2 + '2')}", "w2"), ("{formula(E1 + '2' + E2 + '3')}", "w3")],
       ["Moles of {E1} = {m1} ÷ {ram(E1)} = {roundTo(m1 / ram(E1), 0.001)}; moles of {E2} = {m2} ÷ {ram(E2)} = {roundTo(m2 / ram(E2), 0.001)}.",
        "Divide both by the smaller to get the simplest ratio.", "So the empirical formula is {answer}."],
       vars={"P": {"pick": [["Mg", "O", 2.4, 1.6], ["Cu", "O", 6.4, 1.6], ["Fe", "O", 11.2, 4.8], ["Ca", "O", 4, 1.6],
                            ["Zn", "O", 6.5, 1.6], ["Na", "Cl", 4.6, 7.1], ["Al", "O", 5.4, 4.8]]},
             "E1": {"expr": "P[0]"}, "E2": {"expr": "P[1]"}, "m1": {"expr": "P[2]"}, "m2": {"expr": "P[3]"}},
       misc=[("w1", "Work out the moles: {roundTo(m1 / ram(E1), 0.001)} of {E1} and {roundTo(m2 / ram(E2), 0.001)} of {E2}."),
             ("w2", "Divide each mass by its own relative atomic mass before comparing."),
             ("w3", "The simplest ratio of the moles gives {formula(empiricalOf([E1, E2], [m1, m2]))}.")],
       sources=SRC),
   num("k4-24-mol", 2, "A compound has the empirical formula {formula(F)} and a relative molecular mass of {M}. How many times does the empirical formula fit into the molecular formula?",
       "formulaTimes(F, M)",
       ["The empirical formula mass of {formula(F)} is {molarMass(F)}.",
        "{M} ÷ {molarMass(F)} = {answer}."],
       vars={"P": {"pick": [["CH2", 42], ["CH2", 56], ["CH2O", 180], ["CH", 78], ["NO2", 92], ["CH2O", 60], ["HO", 34]]},
             "F": {"expr": "P[0]"}, "M": {"expr": "P[1]"}},
       misc=[("mult", "roundTo(M * molarMass(F), 0.01)", "Divide the relative molecular mass by the empirical formula mass."),
             ("swap", "roundTo(molarMass(F) / M, 0.001)", "Divide the LARGER mass by the smaller one.")],
       sources=SRC),
   num("k4-24-pc", 2, "A compound is {p1} per cent {E1} and the rest {E2}. How many moles of {E1} are there in {100} g of it?",
       "roundTo(p1 / ram(E1), 0.001)",
       ["In {100} g there are {p1} g of {E1}.", "Moles = {p1} ÷ {ram(E1)} = {answer} mol."],
       vars={"P": {"pick": [["Mg", "O", 60], ["Ca", "O", 40], ["Na", "Cl", 39.3], ["C", "O", 27.3], ["Fe", "O", 70], ["H", "O", 11.1]]},
             "E1": {"expr": "P[0]"}, "E2": {"expr": "P[1]"}, "p1": {"expr": "P[2]"}},
       misc=[("mult", "roundTo(p1 * ram(E1), 0.01)", "Divide the mass by the relative atomic mass to get moles."),
             ("other", "roundTo((100 - p1) / ram(E2), 0.001)", "That is the moles of {E2}; the question asks for {E1}.")],
       sources=SRC, unit="mol"),
   mcq("k4-24-full", 3, "A compound is {p1} per cent {E1} and {p2} per cent {E2}, with a relative molecular mass of {M}. What is its molecular formula?",
       "{formula(MOL)}",
       [("{formula(EMPF)}", "emp"), ("{formula(E1 + E2)}", "simple"), ("{formula(E1 + '2' + E2 + '2')}", "guess")],
       ["Moles in {100} g: {E1} {roundTo(p1 / ram(E1), 0.01)}, {E2} {roundTo(p2 / ram(E2), 0.01)}.",
        "The simplest ratio gives the empirical formula {formula(EMPF)}, of mass {molarMass(EMPF)}.",
        "{M} ÷ {molarMass(EMPF)} = {formulaTimes(EMPF, M)}, so multiply every subscript by {formulaTimes(EMPF, M)}.",
        "So the molecular formula is {answer}."],
       vars={"P": {"pick": [["C", "H", 85.7, 14.3, 42, "CH2", "C3H6"], ["C", "H", 85.7, 14.3, 56, "CH2", "C4H8"],
                            ["C", "H", 92.3, 7.7, 78, "CH", "C6H6"], ["N", "O", 30.4, 69.6, 92, "NO2", "N2O4"]]},
             "E1": {"expr": "P[0]"}, "E2": {"expr": "P[1]"}, "p1": {"expr": "P[2]"}, "p2": {"expr": "P[3]"},
             "M": {"expr": "P[4]"}, "EMPF": {"expr": "P[5]"}, "MOL": {"expr": "P[6]"}},
       misc=[("emp", "That is the EMPIRICAL formula, of mass {molarMass(EMPF)}; the molecule is {formulaTimes(EMPF, M)} times as heavy."),
             ("simple", "Work out the moles first: the ratio is not {1} : {1}."),
             ("guess", "Find the empirical formula from the moles, then scale it up by {formulaTimes(EMPF, M)}.")],
       sources=SRC)],
  learn=learn(
    [goal("find an empirical formula from masses or percentages, and turn it into a molecular formula using the relative molecular mass.",
          "Lesson {23} (percentage composition) and Lesson {22} (formulae by experiment).",
          "Lesson {25}, where a balanced equation is used to find masses and volumes."),
     ("Finding the empirical formula",
      "The EMPIRICAL formula is the simplest whole-number ratio of the atoms. The MOLECULAR formula is the actual number "
      "in one molecule. Glucose is {formula('C6H12O6')}, whose empirical formula is {formula('CH2O')}.\n"
      "From masses or percentages:\n"
      "{1}. Write the mass of each element (a percentage behaves like a mass in {100} g).\n"
      "{2}. Divide each by its relative atomic mass: that gives the moles.\n"
      "{3}. Divide every answer by the smallest.\n"
      "{4}. If the answers are not whole numbers, multiply them all by {2} or {3} until they are.\n"
      "Example: {85.7} per cent C and {14.3} per cent H. {85.7} ÷ {12} = {7.14}; {14.3} ÷ {1} = {14.3}. "
      "Dividing by {7.14}: {1} and {2}. The empirical formula is {formula('CH2')}."),
     ("From empirical to molecular",
      "The molecular formula is always a whole-number multiple of the empirical formula.\n"
      "Divide the relative molecular mass by the mass of the empirical formula:\n"
      "• {formula('CH2')} has a mass of {14}. If Mr = {42}, then {42} ÷ {14} = {3}, so the molecular formula is {formula('C3H6')}.\n"
      "• If Mr = {56}, then {56} ÷ {14} = {4}, giving {formula('C4H8')}.\n"
      "Ionic compounds, such as {formula('NaCl')} and {formula('CaCO3')}, have no molecules, so their formulae are always "
      "empirical: they show the ratio of ions in the lattice.")],
    key_words=[("empirical formula", "the simplest whole-number ratio of the atoms"),
               ("molecular formula", "the actual number of atoms in one molecule"),
               ("lattice", "the regular arrangement of ions in an ionic solid"),
               ("simplest ratio", "the ratio after dividing by the smallest value")],
    examples=["{formula('C6H12O6')} → {formula('CH2O')}", "{formula('CH2')} with Mr {42} → {formula('C3H6')}", "{2.4} g Mg + {1.6} g O → {formula('MgO')}"],
    mistake=("the empirical formula of {formula('C6H12O6')} is {formula('C6H12O6')}", "it is {formula('CH2O')}",
             "Divide every subscript by their highest common factor, which is {6}.")))

# ---------------------------------------------------------------- 25. Masses and volumes from equations
L.lesson(D, S, 25, ("k4-25", "Calculate masses and volumes of gases from balanced equations"), [24],
  "A balanced equation gives the ratio of moles. That ratio is the key to every calculation.\n"
  "Steps:\n"
  "1. Write the balanced equation.\n"
  "2. Change what is given into moles (mass ÷ molar mass, or volume ÷ 22.4).\n"
  "3. Use the ratio in the equation to find the moles of what is wanted.\n"
  "4. Change those moles into a mass or a volume.\n"
  "Example: CaCO3 → CaO + CO2. 10 g of CaCO3 is 10 ÷ 100 = 0.1 mol, which gives 0.1 mol of CO2, "
  "that is 0.1 × 44 = 4.4 g, or 0.1 × 22.4 = 2.24 dm³ at s.t.p.\n"
  "For gases alone, the mole ratio is also the ratio of the volumes at the same temperature and pressure.",
  worked({"m": 10},
         "What mass of calcium oxide, and what volume of carbon dioxide at s.t.p., are made when {m} g of calcium carbonate decomposes completely?",
         ["{formula('CaCO3')} → {formula('CaO')} + {formula('CO2')}.",
          "Moles of {formula('CaCO3')} = {m} ÷ {molarMass('CaCO3')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} mol.",
          "The ratio is {1} : {1} : {1}, so the same number of moles of each product is made.",
          "Mass of {formula('CaO')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} × {molarMass('CaO')}; volume of {formula('CO2')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} × {22.4}."],
         "{roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)} g of {formula('CaO')} and {roundTo(gasVolume(molesOf(m, 'CaCO3')), 0.01)} dm³ of {formula('CO2')}",
         checks=["molarMass('CaCO3') == 100"]),
  [card("c4k25-1", "A balanced equation gives the ratio of MOLES, not of masses.",
        ["{formula('CaCO3')} → {formula('CaO')} + {formula('CO2')} is {1} : {1} : {1} by moles"], "k4-25-ratio"),
   card("c4k25-2", "Change to moles, use the ratio, then change back.",
        ["{10} g {formula('CaCO3')} → {0.1} mol → {0.1} mol {formula('CO2')} → {4.4} g"], "k4-25-mass"),
   card("c4k25-3", "For gases, the mole ratio is also the volume ratio.",
        ["{formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}: {1} : {3} : {2} by volume"], "k4-25-vol")],
  [num("k4-25-ratio", 1, "In the equation {2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')}, how many moles of water are made from {n} mol of oxygen?",
       "2 * n",
       ["The ratio of {formula('O2')} to {formula('H2O')} is {1} : {2}.", "{n} × {2} = {answer} mol."],
       vars={"n": {"pick": [0.1, 0.25, 0.5, 1, 1.5, 2, 3]}},
       misc=[("same", "n", "Read the coefficients: {1} mol of oxygen gives {2} mol of water."),
             ("half", "roundTo(n / 2, 0.001)", "{2} is the coefficient of the water, so multiply by {2}.")],
       sources=SRC, unit="mol"),
   num("k4-25-mass", 2, "What mass of calcium oxide, in grams, is made when {m} g of calcium carbonate decomposes completely?",
       "roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)",
       ["{formula('CaCO3')} → {formula('CaO')} + {formula('CO2')}, a ratio of {1} : {1}.",
        "Moles of {formula('CaCO3')} = {m} ÷ {molarMass('CaCO3')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} mol.",
        "Mass of {formula('CaO')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} × {molarMass('CaO')} = {answer} g."],
       vars={"m": {"pick": [5, 10, 20, 25, 50, 100]}},
       misc=[("same", "m", "Some mass leaves as carbon dioxide, so the oxide is lighter than the carbonate."),
             ("co2", "roundTo(massOf(molesOf(m, 'CaCO3'), 'CO2'), 0.01)", "That is the mass of carbon dioxide given off.")],
       sources=SRC, unit="g"),
   num("k4-25-vol", 2, "What volume of carbon dioxide, in dm³ at s.t.p., is given off when {m} g of calcium carbonate decomposes completely?",
       "roundTo(gasVolume(molesOf(m, 'CaCO3')), 0.01)",
       ["Moles of {formula('CaCO3')} = {m} ÷ {molarMass('CaCO3')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} mol.",
        "{1} mol gives {1} mol of {formula('CO2')}.",
        "Volume = {roundTo(molesOf(m, 'CaCO3'), 0.001)} × {22.4} = {answer} dm³."],
       vars={"m": {"pick": [5, 10, 20, 25, 50, 100]}},
       misc=[("mass", "roundTo(massOf(molesOf(m, 'CaCO3'), 'CO2'), 0.01)", "That is the MASS in grams; the question asks for a volume."),
             ("nomole", "roundTo(gasVolume(m), 0.01)", "Change the mass to moles first.")],
       sources=SRC, unit="dm³"),
   num("k4-25-gas", 3, "In the Haber process, {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}. What volume of ammonia, in dm³, is made from {v} dm³ of nitrogen, all volumes measured at the same temperature and pressure?",
       "2 * v",
       ["For gases, the mole ratio is also the volume ratio.",
        "The ratio of {formula('N2')} to {formula('NH3')} is {1} : {2}.", "{v} × {2} = {answer} dm³."],
       vars={"v": {"pick": [5, 10, 20, 25, 50, 100]}},
       misc=[("three", "3 * v", "{3} is the coefficient of the HYDROGEN, not of the ammonia."),
             ("same", "v", "{1} volume of nitrogen gives {2} volumes of ammonia.")],
       sources=SRC, unit="dm³"),
   num("k4-25-zinc", 3, "What mass of zinc, in grams, is needed to make {v} dm³ of hydrogen at s.t.p. with excess dilute sulphuric acid?",
       "roundTo(massOf(volumeToMoles(v), 'Zn'), 0.01)",
       ["Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}, a ratio of {1} : {1}.",
        "Moles of hydrogen = {v} ÷ {22.4} = {roundTo(volumeToMoles(v), 0.001)} mol, so the same moles of zinc are needed.",
        "Mass = {roundTo(volumeToMoles(v), 0.001)} × {ram('Zn')} = {answer} g."],
       vars={"v": {"pick": [2.24, 4.48, 5.6, 11.2, 22.4]}},
       misc=[("novol", "roundTo(massOf(v, 'Zn'), 0.01)", "Change the volume to moles first: divide by {22.4}."),
             ("h2", "roundTo(massOf(volumeToMoles(v), 'H2'), 0.01)", "That is the mass of the hydrogen, not of the zinc.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("use a balanced equation to find the mass or volume of any substance in a reaction.",
          "Lesson {21} (mass, moles and volume) and Form Three balanced equations.",
          "Lesson {26} (when one reactant runs out first) and every quantitative experiment."),
     ("Moles are the bridge",
      "A balanced equation gives the ratio of MOLES, not of masses. In\n"
      "{formula('CaCO3')} → {formula('CaO')} + {formula('CO2')}\n"
      "one mole of the carbonate gives one mole of each product, but their masses are {100} g, {56} g and {44} g.\n"
      "Every calculation has the same four steps:\n"
      "{1}. write the balanced equation;\n{2}. change what is given into moles;\n"
      "{3}. use the ratio to get the moles of what is wanted;\n{4}. change those moles into a mass or a volume.\n"
      "For {10} g of {formula('CaCO3')}: moles = {10} ÷ {100} = {0.1}; so {0.1} mol of {formula('CO2')}; "
      "that is {0.1} × {44} = {4.4} g, or {0.1} × {22.4} = {2.24} dm³ at s.t.p."),
     ("Volumes of gases",
      "When every substance in the ratio is a gas, and all are measured at the same temperature and pressure, the mole "
      "ratio is also the VOLUME ratio. This follows from Avogadro's law.\n"
      "{formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}\n"
      "So {1} dm³ of nitrogen needs {3} dm³ of hydrogen and gives {2} dm³ of ammonia; {10} dm³ of nitrogen gives {20} dm³ "
      "of ammonia, with no need to work out any moles at all.\n"
      "Be careful: this shortcut works only for gases. For a solid or a liquid in the equation, go through the moles.")],
    key_words=[("mole ratio", "the ratio of the coefficients in a balanced equation"),
               ("excess", "more than enough, so that the other reactant decides the amount made"),
               ("Avogadro's law", "equal volumes of gases at the same temperature and pressure hold equal numbers of molecules")],
    examples=["{10} g {formula('CaCO3')} → {4.4} g {formula('CO2')}", "{1} dm³ {formula('N2')} → {2} dm³ {formula('NH3')}"],
    mistake=("{100} g of {formula('CaCO3')} gives {100} g of {formula('CaO')}", "it gives {56} g, because {44} g leaves as {formula('CO2')}",
             "The equation balances MOLES, not masses; always change to moles first.")))

# ---------------------------------------------------------------- 26. Limiting reagents, theoretical and percentage yield
LIMIT = [
    {"q": "What is a limiting reagent?", "r": "The reactant that is used up first and so decides how much product is made",
     "w": ["The reactant there is most of", "The reactant with the largest molar mass",
           "The product made in the smallest amount"],
     "e": ["The one in excess is left over; it is not what limits the reaction.",
           "Molar mass does not decide which runs out first.",
           "A limiting reagent is a reactant, not a product."],
     "y": "Once the limiting reagent is gone the reaction stops, however much of the other reactant is left."},
    {"q": "How is the limiting reagent found?", "r": "Divide the moles of each reactant by its coefficient, and take the smallest",
     "w": ["Take the reactant with the smaller mass", "Take the reactant with the smaller molar mass",
           "Take the reactant with the larger number of moles"],
     "e": ["A small mass may still be many moles if the molar mass is small.",
           "Molar mass alone does not decide it.",
           "More moles does not help if the equation needs even more of it."],
     "y": "The coefficient says how many moles the reaction uses for each unit of reaction, so divide by it before comparing."},
    {"q": "What is the theoretical yield?", "r": "The mass of product that the equation says should be made, if nothing is lost",
     "w": ["The mass of product actually collected", "The mass of the reactants used",
           "The percentage of product that is pure"],
     "e": ["That is the ACTUAL yield.",
           "The reactants are what you start with, not the yield.",
           "Purity is a different idea."],
     "y": "It is worked out from the limiting reagent and the mole ratio in the equation."},
    {"q": "Why is the actual yield usually less than the theoretical yield?", "r": "Some product is lost in transferring and purifying, and the reaction may not go to completion",
     "w": ["The equation is wrong", "Atoms are destroyed in the reaction",
           "The theoretical yield is always a guess"],
     "e": ["The equation is right; the losses happen in the laboratory.",
           "Atoms are never destroyed; they are simply left behind in the apparatus or in side products.",
           "The theoretical yield is calculated exactly from the equation."],
     "y": "Product sticks to filter papers and beakers, some stays dissolved, and side reactions use up reactant."},
    {"q": "A reaction has a percentage yield of {100} per cent. What does this mean?",
     "r": "All the limiting reagent was turned into product and none was lost",
     "w": ["The product is {100} per cent pure", "The reaction was very fast",
           "Twice as much product was made as expected"],
     "e": ["Purity and yield are different measurements.",
           "Speed has nothing to do with yield.",
           "A yield can never be more than {100} per cent."],
     "y": "Percentage yield = actual ÷ theoretical × {100}, so {100} per cent means actual = theoretical."},
]

L.lesson(D, S, 26, ("k4-26", "Use limiting reagents, theoretical yield and percentage yield"), [25],
  "When two reactants are mixed, one is usually used up first. That one is the limiting reagent, and it decides how much "
  "product can be made. The other is said to be in excess.\n"
  "To find it: work out the moles of each reactant, divide each by its coefficient in the equation, and take the smallest.\n"
  "Theoretical yield: the mass of product the equation says should be made from the limiting reagent, if nothing is lost.\n"
  "Actual yield: the mass actually collected. It is almost always less, because product is lost in transferring, filtering "
  "and purifying, because reactions may not go to completion, and because side reactions use up reactant.\n"
  "Percentage yield = (actual yield ÷ theoretical yield) × 100 per cent. It can never be more than 100 per cent.",
  worked({"a": 0.3, "b": 0.4},
         "{a} mol of nitrogen is mixed with {b} mol of hydrogen: {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}. Which is the limiting reagent, and how many moles of ammonia can be made?",
         ["Divide each by its coefficient: nitrogen {a} ÷ {1} = {a}; hydrogen {b} ÷ {3} = {roundTo(b / 3, 0.001)}.",
          "The smaller is the hydrogen, so hydrogen is the limiting reagent.",
          "The ratio of {formula('H2')} to {formula('NH3')} is {3} : {2}.",
          "Moles of ammonia = {b} × {2} ÷ {3} = {roundTo(b * 2 / 3, 0.001)} mol."],
         "hydrogen is limiting; {roundTo(b * 2 / 3, 0.001)} mol of ammonia",
         checks=["0.4 / 3 < 0.3"]),
  [card("c4k26-1", "The limiting reagent runs out first and decides how much product is made.",
        ["the other reactant is in excess and is left over"], "k4-26-define"),
   card("c4k26-2", "Divide the moles of each reactant by its coefficient; the smallest is limiting.",
        ["{0.3} ÷ {1} = {0.3} against {0.4} ÷ {3} = {0.133}: the second is limiting"], "k4-26-find"),
   card("c4k26-3", "Percentage yield = actual ÷ theoretical × {100}.",
        ["{8} g made out of a possible {10} g is {80} per cent"], "k4-26-yield")],
  [bank("k4-26-define", 1, "{X.q}", LIMIT, SRC),
   mcq("k4-26-find", 2, "{a} mol of {formula('N2')} is mixed with {b} mol of {formula('H2')}: {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}. Which is the limiting reagent?",
       "{b / 3 < a ? 'Hydrogen' : 'Nitrogen'}",
       [("{b / 3 < a ? 'Nitrogen' : 'Hydrogen'}", "swap"), ("Neither: they are exactly matched", "exact"),
        ("The one with the larger number of moles", "more")],
       ["Divide each by its coefficient: nitrogen {a} ÷ {1} = {a}; hydrogen {b} ÷ {3} = {roundTo(b / 3, 0.001)}.",
        "The smaller value belongs to the limiting reagent.", "So the answer is: {answer}."],
       vars={"a": {"pick": [0.1, 0.2, 0.3, 0.5, 1]}, "b": {"pick": [0.3, 0.4, 0.6, 0.9, 1.2, 2]}},
       misc=[("swap", "Compare {a} with {roundTo(b / 3, 0.001)}: the SMALLER one runs out first."),
             ("exact", "{a} and {roundTo(b / 3, 0.001)} are not equal, so one runs out before the other."),
             ("more", "Having more moles does not help if the equation needs {3} times as many.")],
       sources=SRC, where=["abs(b / 3 - a) > 0.02"]),
   num("k4-26-yield", 2, "A reaction should give {t} g of product, but only {y} g is collected. What is the percentage yield?",
       "percentYield(y, t)",
       ["Percentage yield = actual ÷ theoretical × {100}.", "{y} ÷ {t} × {100} = {answer} per cent."],
       vars={"t": {"pick": [10, 20, 25, 40, 50, 80, 100]}, "f": {"pick": [0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95]},
             "y": {"expr": "roundTo(t * f, 0.01)"}},
       misc=[("swap", "percentYield(t, y)", "Divide the ACTUAL yield by the theoretical one."),
             ("diff", "roundTo(t - y, 0.01)", "That is the mass lost, not the percentage yield.")],
       sources=SRC, unit="%"),
   num("k4-26-actual", 2, "A reaction has a theoretical yield of {t} g and a percentage yield of {p} per cent. What mass of product, in grams, is actually collected?",
       "roundTo(t * p / 100, 0.01)",
       ["Actual = theoretical × percentage ÷ {100}.", "{t} × {p} ÷ {100} = {answer} g."],
       vars={"t": {"pick": [10, 20, 25, 40, 50, 80]}, "p": {"pick": [40, 50, 60, 75, 80, 90]}},
       misc=[("div", "roundTo(t * 100 / p, 0.01)", "The actual yield is LESS than the theoretical one."),
             ("same", "t", "Only {p} per cent of the possible yield was collected.")],
       sources=SRC, unit="g"),
   num("k4-26-full", 3, "{m} g of calcium carbonate is heated and {y} g of calcium oxide is collected. What is the percentage yield?",
       "percentYield(y, massOf(molesOf(m, 'CaCO3'), 'CaO'))",
       ["Moles of {formula('CaCO3')} = {m} ÷ {molarMass('CaCO3')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} mol.",
        "The ratio is {1} : {1}, so the theoretical mass of {formula('CaO')} is {roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)} g.",
        "Percentage yield = {y} ÷ {roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)} × {100} = {answer} per cent."],
       vars={"m": {"pick": [10, 20, 25, 50, 100]}, "f": {"pick": [0.5, 0.6, 0.75, 0.8, 0.9]},
             "y": {"expr": "roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO') * f, 0.01)"}},
       misc=[("carbonate", "percentYield(y, m)", "Compare the yield with the theoretical mass of {formula('CaO')}, not with the mass of carbonate."),
             ("swap", "percentYield(massOf(molesOf(m, 'CaCO3'), 'CaO'), y)", "Divide the actual yield by the theoretical one.")],
       sources=SRC, unit="%")],
  learn=learn(
    [goal("find the limiting reagent, work out a theoretical yield, and calculate a percentage yield.",
          "Lesson {25} (masses from equations) and Lesson {21} (mole calculations).",
          "Lesson {27} (percentage yield in practice) and the costing of industrial processes."),
     ("The limiting reagent",
      "Mix {2} slices of bread with {10} slices of cheese and you can still make only {1} sandwich: the bread limits it. "
      "Chemistry works the same way.\n"
      "The LIMITING REAGENT is the reactant used up first; it decides how much product can be made. The other reactant is "
      "in EXCESS and is left over.\n"
      "To find it:\n"
      "{1}. work out the moles of each reactant;\n{2}. divide each by its coefficient in the balanced equation;\n"
      "{3}. the smallest answer belongs to the limiting reagent.\n"
      "For {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')} with {0.3} mol of {formula('N2')} and {0.4} mol of "
      "{formula('H2')}: {0.3} ÷ {1} = {0.3}, and {0.4} ÷ {3} = {0.133}. The hydrogen is limiting."),
     ("Theoretical, actual and percentage yield",
      "The THEORETICAL yield is what the equation says should be made from the limiting reagent, with nothing lost.\n"
      "The ACTUAL yield is what is really collected. It is almost always smaller, because:\n"
      "• some product sticks to the filter paper or the beaker;\n• some stays dissolved in the solvent;\n"
      "• the reaction may not go to completion;\n• side reactions use up some reactant.\n"
      "PERCENTAGE YIELD = (actual ÷ theoretical) × {100} per cent.\n"
      "If {10} g was expected and {8} g collected, the yield is {80} per cent. A yield above {100} per cent is impossible; "
      "if one is calculated, the product is probably still wet or impure.")],
    key_words=[("limiting reagent", "the reactant used up first, which decides the amount of product"),
               ("excess", "more than enough of a reactant"),
               ("theoretical yield", "the mass of product the equation predicts"),
               ("percentage yield", "actual ÷ theoretical × {100}")],
    examples=["{0.4} mol {formula('H2')} with {0.3} mol {formula('N2')}: hydrogen limits", "{8} g of a possible {10} g: {80} per cent"],
    mistake=("the reactant with the smaller mass is always limiting", "divide the moles by the coefficient and compare",
             "A small mass of a light substance can still be many moles.")))
