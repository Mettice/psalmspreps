"""Form 4 Chemistry, Term 1, rows 19-24: formulae, moles and equations (definitions, the mole, basic calculations,
finding formulae by experiment, percentage composition, empirical and molecular formulae).
Row 30 is an integration activity. Run: python tools/authoring/form4/chem_moles.py"""
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

COMMON = ["H2O", "CO2", "NaCl", "CaCO3", "H2SO4", "NH3", "MgO", "CuO", "Fe2O3", "NaOH", "KNO3", "ZnO"]

# ---------------------------------------------------------------- 19. Definitions
DEFS = [
    {"q": "What is the relative atomic mass of an element?", "r": "The average mass of its atoms compared with one twelfth of the mass of a carbon-12 atom",
     "w": ["The mass of one atom in grams", "The number of protons in an atom", "The mass of one mole in kilograms"],
     "e": ["The mass of a single atom in grams is far too small to be convenient; a RELATIVE mass is used.",
           "The number of protons is the atomic number, not the mass.",
           "The molar mass is in grams per mole, and relative atomic mass has no unit."],
     "y": "It is a ratio, so it has no unit: the relative atomic mass of carbon is {12} exactly."},
    {"q": "What is the relative molecular mass of a compound?", "r": "The sum of the relative atomic masses of all the atoms in its molecule",
     "w": ["The mass of one molecule in grams", "The number of atoms in the molecule",
           "The mass of one mole of its atoms"],
     "e": ["Again, a relative mass is used, not the tiny mass in grams.",
           "The number of atoms is a count, not a mass.",
           "That would be the molar mass of the element, not of the compound."],
     "y": "For {formula('H2O')}: {2} × {1} + {16} = {18}."},
    {"q": "Why is 'relative formula mass' used for sodium chloride rather than 'relative molecular mass'?",
     "r": "Sodium chloride is ionic, so it has no molecules, only a lattice of ions",
     "w": ["Its molecules are too large", "It has no mass", "The two terms mean exactly the same thing"],
     "e": ["Size is not the point; an ionic solid has no separate molecules at all.",
           "It certainly has mass; the point is what the formula stands for.",
           "'Molecular' is used where molecules exist; 'formula' covers ionic compounds too."],
     "y": "{formula('NaCl')} is the simplest ratio of ions in the lattice, so the mass found from it is a formula mass."},
    {"q": "What is molar mass?", "r": "The mass of one mole of a substance, in grams per mole",
     "w": ["The number of particles in one mole", "The volume of one mole of a gas",
           "The mass of one atom"],
     "e": ["The number of particles is the Avogadro constant.",
           "That is the molar volume, {22.4} dm³/mol at s.t.p.",
           "The mass of one atom is a tiny number of grams."],
     "y": "The molar mass in g/mol is the same number as the relative atomic or molecular mass."},
    {"q": "What is molar volume?", "r": "The volume occupied by one mole of any gas, {22.4} dm³ at s.t.p.",
     "w": ["The volume of one mole of any liquid", "The volume of one gram of a gas",
           "The volume of {6.02} × {10} to the power {23} atoms of a solid"],
     "e": ["Liquids and solids have very different molar volumes; the rule holds for gases.",
           "The molar volume is per MOLE, not per gram.",
           "The rule applies to gases, not to solids."],
     "y": "At the same temperature and pressure, equal volumes of gases hold equal numbers of molecules."},
]

L.lesson(D, S, 19, ("k4-19", "Define relative atomic mass, relative molecular mass, molar mass and molar volume"), [],
  "Relative atomic mass (Ar): the average mass of the atoms of an element compared with one twelfth of the mass of a "
  "carbon-12 atom. It is a ratio, so it has no unit. Ar(H) = 1, Ar(C) = 12, Ar(O) = 16, Ar(Cl) = 35.5.\n"
  "Relative molecular mass (Mr): the sum of the relative atomic masses of all the atoms in a molecule. "
  "Mr(H2O) = 2 × 1 + 16 = 18.\n"
  "For an ionic compound, which has no molecules, the same sum is called the relative formula mass. Mr(NaCl) = 23 + 35.5 = 58.5.\n"
  "Molar mass: the mass of one mole of a substance, in g/mol. Its number is the same as the relative atomic or molecular mass.\n"
  "Molar volume: the volume of one mole of ANY gas, 22.4 dm³ at s.t.p. (0 °C and one atmosphere).",
  worked({"F": "H2SO4"},
         "Find the relative molecular mass of {formula(F)} and state its molar mass.",
         ["Count the atoms: {totalAtoms(F)} in all.",
          "Add the relative atomic masses: H is {ram('H')}, S is {ram('S')} and O is {ram('O')}.",
          "{2} × {ram('H')} + {ram('S')} + {4} × {ram('O')} = {molarMass(F)}.",
          "The molar mass is the same number with the unit g/mol."],
         "relative molecular mass {molarMass(F)}; molar mass {molarMass(F)} g/mol",
         checks=["molarMass('H2SO4') == 98"]),
  [card("c4k19-1", "Relative atomic mass compares an atom with one twelfth of a carbon-{12} atom; it has no unit.",
        ["Ar(H) = {1}, Ar(C) = {12}, Ar(O) = {16}, Ar(Cl) = {35.5}"], "k4-19-define"),
   card("c4k19-2", "Relative molecular mass is the sum of the relative atomic masses in the formula.",
        ["{formula('H2O')}: {2} × {1} + {16} = {18}"], "k4-19-mr"),
   card("c4k19-3", "Molar mass is in g/mol; molar volume is {22.4} dm³/mol for any gas at s.t.p.",
        ["{1} mol of {formula('CO2')} is {44} g and fills {22.4} dm³ at s.t.p."], "k4-19-molar")],
  [bank("k4-19-define", 1, "{X.q}", DEFS, SRC),
   num("k4-19-mr", 1, "Find the relative molecular (or formula) mass of {formula(F)}.",
       "molarMass(F)",
       ["Add the relative atomic mass of every atom in the formula.",
        "{formula(F)} has {totalAtoms(F)} atoms from {elementCount(F)} elements.", "The answer is {answer}."],
       vars={"F": {"pick": COMMON}},
       misc=[("atoms", "totalAtoms(F)", "{totalAtoms(F)} is the NUMBER of atoms, not their total mass."),
             ("first", "ram(symbolsIn(F)[0])", "Include every atom, not just the first element.")],
       sources=SRC),
   num("k4-19-molar", 1, "What is the mass, in grams, of {1} mole of {formula(F)}?",
       "molarMass(F)",
       ["The molar mass in g/mol has the same number as the relative molecular mass.",
        "For {formula(F)} that is {molarMass(F)}.", "So {1} mole has a mass of {answer} g."],
       vars={"F": {"pick": COMMON}},
       misc=[("atoms", "totalAtoms(F)", "Add the masses of the atoms; do not count them."),
             ("vol", "22.4", "{22.4} dm³ is the molar VOLUME of a gas, not a mass.")],
       sources=SRC, unit="g"),
   num("k4-19-vol", 2, "What volume, in dm³ at s.t.p., is occupied by {n} mol of {formula(F)} gas?",
       "gasVolume(n)",
       ["At s.t.p. {1} mol of any gas fills {22.4} dm³.", "{n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 3]}, "F": {"pick": ["CO2", "NH3", "SO2", "H2S", "N2", "O2", "H2"]}},
       misc=[("mass", "massOf(n, F)", "The question asks for a VOLUME in dm³, not a mass in grams."),
             ("div", "volumeToMoles(n)", "Multiply by {22.4} dm³/mol; do not divide.")],
       sources=SRC, unit="dm³"),
   mcq("k4-19-equal", 3, "{E.q}",
       "{E.r}", [("{E.w1}", "w1"), ("{E.w2}", "w2"), ("{E.w3}", "w3")],
       ["{E.y}", "So the answer is: {answer}."],
       vars={"E": {"pick": [
           {"q": "Two flasks of the same size hold carbon dioxide and hydrogen at the same temperature and pressure. What is the same in both?",
            "r": "The number of molecules", "w1": "The mass of gas", "w2": "The density of the gas", "w3": "Nothing is the same",
            "y": "Equal volumes of gases at the same temperature and pressure hold equal numbers of molecules."},
           {"q": "Why does {1} mol of hydrogen fill the same volume as {1} mol of carbon dioxide at s.t.p., although it is much lighter?",
            "r": "The molar volume is the same for every gas: the molecules are far apart whatever their mass",
            "w1": "Hydrogen molecules are larger", "w2": "Carbon dioxide molecules are squashed together",
            "w3": "They do not fill the same volume",
            "y": "In a gas the molecules are so far apart that their own size and mass hardly affect the volume."},
           {"q": "Which holds more molecules at s.t.p.: {22.4} dm³ of oxygen or {22.4} dm³ of ammonia?",
            "r": "Neither: both hold one mole, that is the same number of molecules",
            "w1": "The oxygen, because it is denser", "w2": "The ammonia, because its molecules are smaller",
            "w3": "It cannot be worked out", "y": "Equal volumes at the same temperature and pressure hold equal numbers of molecules."}]}},
       misc=[("w1", "{E.y}"), ("w2", "{E.y}"), ("w3", "{E.y}")],
       sources=SRC)],
  learn=learn(
    [goal("define and use relative atomic mass, relative molecular mass, molar mass and molar volume.",
          "Form Three relative atomic mass and the mole of atoms.",
          "Lesson {20} (the mole and the Avogadro constant) and every calculation in this chapter."),
     ("Relative masses",
      "Atoms are far too light to weigh one at a time, so their masses are compared with a standard.\n"
      "RELATIVE ATOMIC MASS (Ar) is the average mass of the atoms of an element compared with one twelfth of the mass of a "
      "carbon-{12} atom. Being a ratio, it has no unit: Ar(H) = {1}, Ar(C) = {12}, Ar(O) = {16}, Ar(Cl) = {35.5}.\n"
      "RELATIVE MOLECULAR MASS (Mr) adds the relative atomic masses of all the atoms in a molecule:\n"
      "{formula('H2O')} = {2} × {1} + {16} = {18}; {formula('H2SO4')} = {2} + {32} + {64} = {98}.\n"
      "An ionic compound has no molecules, so the same sum is called the RELATIVE FORMULA MASS: "
      "{formula('NaCl')} = {23} + {35.5} = {58.5}."),
     ("Molar mass and molar volume",
      "MOLAR MASS is the mass of one mole, in grams per mole. Its number is the same as the relative atomic or molecular "
      "mass, so one mole of water is {18} g and one mole of carbon dioxide is {44} g.\n"
      "MOLAR VOLUME is the volume of one mole of any GAS: {22.4} dm³ at s.t.p., which means {0} °C and one atmosphere.\n"
      "That the same volume holds a mole of any gas follows from Avogadro's law: equal volumes of gases at the same "
      "temperature and pressure hold equal numbers of molecules. In a gas the molecules are so far apart that their own "
      "size and mass hardly matter.")],
    key_words=[("relative atomic mass (Ar)", "the mass of an atom compared with one twelfth of a carbon-{12} atom"),
               ("relative molecular mass (Mr)", "the sum of the relative atomic masses in a molecule"),
               ("molar mass", "the mass of one mole, in g/mol"),
               ("molar volume", "{22.4} dm³/mol, the volume of one mole of any gas at s.t.p."),
               ("s.t.p.", "standard temperature and pressure: {0} °C and one atmosphere")],
    examples=["Mr({formula('CO2')}) = {44}", "Mr({formula('NaCl')}) = {58.5}", "{1} mol of any gas = {22.4} dm³ at s.t.p."],
    mistake=("relative atomic mass is measured in grams", "it has no unit at all",
             "It is a RATIO of two masses, so the units cancel. The molar mass, in g/mol, is the one with a unit.")))

# ---------------------------------------------------------------- 20. The mole and the Avogadro constant
MOLE = [
    {"q": "What is a mole?", "r": "The amount of a substance that holds as many particles as there are atoms in {12} g of carbon-12",
     "w": ["A mass of {1} g of any substance", "A volume of {22.4} dm³ of any substance",
           "The mass of one molecule"],
     "e": ["The mass of a mole differs from substance to substance.",
           "{22.4} dm³ is the volume of a mole of a GAS, not of a solid or liquid.",
           "A mole holds a very large number of molecules, not one."],
     "y": "That number is the Avogadro constant, about {6.02} × {10} to the power {23}."},
    {"q": "What is the Avogadro constant?", "r": "About {6.02} × {10} to the power {23} particles per mole",
     "w": ["{22.4} dm³ per mole", "{12} g per mole", "{100} particles per mole"],
     "e": ["{22.4} dm³/mol is the molar volume of a gas.",
           "{12} g/mol is the molar mass of carbon.",
           "The number is enormously larger than {100}."],
     "y": "One mole of any substance holds that number of particles, whether atoms, molecules or ions."},
    {"q": "How many atoms are there in one mole of helium?", "r": "About {6.02} × {10} to the power {23}",
     "w": ["{4}", "{22.4}", "{12}"],
     "e": ["{4} is the relative atomic mass of helium, not a number of atoms.",
           "{22.4} dm³ is the volume a mole of helium fills at s.t.p.",
           "{12} g is the mass of a mole of carbon."],
     "y": "One mole of ANY substance holds the Avogadro number of particles."},
    {"q": "How many atoms are there in one mole of water molecules?", "r": "Three times the Avogadro number, because each molecule has {3} atoms",
     "w": ["The Avogadro number", "Twice the Avogadro number", "One third of the Avogadro number"],
     "e": ["That is the number of MOLECULES, not of atoms.",
           "There are {2} hydrogen atoms AND {1} oxygen atom: {3} in all.",
           "There are more atoms than molecules, not fewer."],
     "y": "{formula('H2O')} has {3} atoms per molecule, so a mole of molecules holds {3} moles of atoms."},
    {"q": "How many ions are there in one mole of sodium chloride, {formula('NaCl')}?", "r": "Two moles of ions: one of {formula('Na')} and one of {formula('Cl')}",
     "w": ["One mole of ions", "Three moles of ions", "There are no ions"],
     "e": ["Each formula unit gives TWO ions.",
           "{formula('NaCl')} holds only two ions per formula unit.",
           "Sodium chloride is ionic: it is made of ions."],
     "y": "{formula('NaCl')} → {formula('Na')} and {formula('Cl')} ions, so a mole of the salt gives {2} mol of ions."},
]

L.lesson(D, S, 20, ("k4-20", "Define the mole and the Avogadro constant and apply them to atoms, molecules and ions"), [19],
  "A mole is the amount of a substance that holds as many particles as there are atoms in 12 g of carbon-12. "
  "That number is the Avogadro constant, L = 6.02 × 10²³ per mole.\n"
  "One mole of any substance holds 6.02 × 10²³ particles, whether they are atoms, molecules or ions.\n"
  "• 1 mol of helium = 6.02 × 10²³ atoms.\n"
  "• 1 mol of water = 6.02 × 10²³ molecules, but 3 × 6.02 × 10²³ atoms, because each molecule has 3 atoms.\n"
  "• 1 mol of NaCl gives 2 mol of ions: one of Na⁺ and one of Cl⁻.\n"
  "Number of particles = moles × L.\n"
  "The mass of one mole is the molar mass in g/mol, and one mole of any gas fills 22.4 dm³ at s.t.p.",
  worked({"n": 0.5, "F": "H2O"},
         "How many molecules, and how many atoms, are there in {n} mol of {formula(F)}?",
         ["Number of molecules = moles × L = {n} × {6.02} × {10} to the power {23}.",
          "= {particles(n)} molecules.",
          "Each molecule of {formula(F)} holds {totalAtoms(F)} atoms.",
          "So the number of atoms is {totalAtoms(F)} × {particles(n)}."],
         "{particles(n)} molecules and {particles(n * totalAtoms(F))} atoms",
         checks=["totalAtoms('H2O') == 3"]),
  [card("c4k20-1", "One mole holds {6.02} × {10} to the power {23} particles: the Avogadro constant.",
        ["{1} mol of helium = {6.02} × {10} to the power {23} atoms"], "k4-20-define"),
   card("c4k20-2", "Number of particles = moles × L.",
        ["{2} mol of {formula('CO2')} = {1.2} × {10} to the power {24} molecules"], "k4-20-count"),
   card("c4k20-3", "A mole of molecules holds more than a mole of atoms: count the atoms in the formula.",
        ["{1} mol of {formula('H2O')} = {3} mol of atoms"], "k4-20-atoms")],
  [bank("k4-20-define", 1, "{X.q}", MOLE, SRC),
   num("k4-20-count", 1, "How many moles of atoms are there in {n} mol of {formula(F)} molecules?",
       "roundTo(n * totalAtoms(F), 0.001)",
       ["Each molecule of {formula(F)} holds {totalAtoms(F)} atoms.",
        "{n} × {totalAtoms(F)} = {answer} mol of atoms."],
       vars={"n": {"pick": [0.1, 0.25, 0.5, 1, 2, 3]}, "F": {"pick": ["H2O", "CO2", "NH3", "H2SO4", "SO2", "CH4"]}},
       misc=[("same", "n", "A molecule holds more than one atom: multiply by {totalAtoms(F)}."),
             ("elements", "roundTo(n * elementCount(F), 0.001)", "Count the ATOMS ({totalAtoms(F)}), not the different elements ({elementCount(F)}).")],
       sources=SRC, unit="mol"),
   num("k4-20-moles", 2, "How many moles are there in {m} g of {formula(F)}?",
       "roundTo(molesOf(m, F), 0.001)",
       ["Moles = mass ÷ molar mass.", "The molar mass of {formula(F)} is {molarMass(F)} g/mol.",
        "{m} ÷ {molarMass(F)} = {answer} mol."],
       vars={"F": {"pick": ["H2O", "CO2", "NaCl", "CaCO3", "H2SO4", "NaOH", "MgO"]},
             "k": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 4]}, "m": {"expr": "roundTo(k * molarMass(F), 0.01)"}},
       misc=[("mult", "roundTo(massOf(m, F), 0.01)", "Moles = mass ÷ molar mass: divide, do not multiply."),
             ("swap", "roundTo(molarMass(F) / m, 0.001)", "Divide the MASS by the molar mass, not the other way round.")],
       sources=SRC, unit="mol"),
   num("k4-20-mass", 2, "What is the mass, in grams, of {n} mol of {formula(F)}?",
       "massOf(n, F)",
       ["Mass = moles × molar mass.", "The molar mass of {formula(F)} is {molarMass(F)} g/mol.",
        "{n} × {molarMass(F)} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 3]}, "F": {"pick": COMMON}},
       misc=[("div", "roundTo(molesOf(n, F), 0.0001)", "Mass = moles × molar mass: multiply, do not divide."),
             ("molar", "molarMass(F)", "{molarMass(F)} g is the mass of ONE mole; here there are {n} mol.")],
       sources=SRC, unit="g"),
   num("k4-20-atoms", 3, "How many moles of {E} atoms are there in {n} mol of {formula(F)}?",
       "roundTo(n * atomCount(F, E), 0.001)",
       ["Each formula unit of {formula(F)} holds {atomCount(F, E)} atoms of {E}.",
        "{n} × {atomCount(F, E)} = {answer} mol of {E} atoms."],
       vars={"P": {"pick": [["H2SO4", "O"], ["H2SO4", "H"], ["CaCO3", "O"], ["Fe2O3", "Fe"], ["NH3", "H"], ["CO2", "O"], ["H2O", "H"]]},
             "F": {"expr": "P[0]"}, "E": {"expr": "P[1]"}, "n": {"pick": [0.1, 0.25, 0.5, 1, 2]}},
       misc=[("same", "n", "Each formula unit holds {atomCount(F, E)} atoms of {E}, not one."),
             ("all", "roundTo(n * totalAtoms(F), 0.001)", "Count only the {E} atoms ({atomCount(F, E)}), not all {totalAtoms(F)}.")],
       sources=SRC, unit="mol")],
  learn=learn(
    [goal("define the mole and the Avogadro constant, and count particles, atoms and ions in a given amount.",
          "Lesson {19} (relative masses) and Form Three the mole of atoms.",
          "Lesson {21}, where moles, mass and volume are used together in calculations."),
     ("The mole and the Avogadro constant",
      "Chemists work with huge numbers of atoms, so they count them in moles.\n"
      "A MOLE is the amount of a substance that holds as many particles as there are atoms in {12} g of carbon-{12}. "
      "That number is the AVOGADRO CONSTANT, L = {6.02} × {10} to the power {23} per mole.\n"
      "One mole of any substance holds that many particles:\n"
      "• {1} mol of helium: {6.02} × {10} to the power {23} atoms;\n"
      "• {1} mol of carbon dioxide: {6.02} × {10} to the power {23} molecules;\n"
      "• {1} mol of sodium chloride: {6.02} × {10} to the power {23} formula units, which is {2} mol of ions.\n"
      "Number of particles = moles × L."),
     ("Atoms, molecules and ions",
      "Be careful to say WHICH particle is being counted.\n"
      "One mole of water, {formula('H2O')}:\n"
      "• {1} mol of molecules;\n• {3} mol of atoms, because each molecule has {2} hydrogen and {1} oxygen;\n"
      "• {2} mol of hydrogen atoms and {1} mol of oxygen atoms.\n"
      "One mole of {formula('H2SO4')} holds {7} mol of atoms: {2} of hydrogen, {1} of sulphur and {4} of oxygen.\n"
      "One mole of {formula('CaCl2')} gives {3} mol of ions: {1} of calcium and {2} of chloride.\n"
      "Together with the molar mass from Lesson {19}, this links a mass you can weigh to a number of particles you cannot count.")],
    key_words=[("mole", "the amount of substance holding {6.02} × {10} to the power {23} particles"),
               ("Avogadro constant (L)", "{6.02} × {10} to the power {23} per mole"),
               ("formula unit", "the group of ions shown by the formula of an ionic compound"),
               ("amount of substance", "the quantity measured in moles")],
    examples=["{1} mol of {formula('CO2')}: {3} mol of atoms", "{2} mol of {formula('NaCl')}: {4} mol of ions", "particles = moles × L"],
    mistake=("one mole of water holds {6.02} × {10} to the power {23} atoms", "it holds that many MOLECULES, and three times as many atoms",
             "Each water molecule has {3} atoms, so a mole of molecules is {3} mol of atoms.")))
