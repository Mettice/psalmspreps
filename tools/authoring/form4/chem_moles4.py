"""Form 4 Chemistry, Term 1, rows 27-29: percentage yield in practice, balancing equations by the mole concept,
and chemical equations with state symbols. Run: python tools/authoring/form4/chem_moles4.py"""
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

# ---------------------------------------------------------------- 27. Percentage yield in practice
YIELD = [
    {"q": "Why can a percentage yield never be more than {100} per cent?", "r": "No more product can be made than the equation allows from the reactants used",
     "w": ["Because the balance is not accurate enough", "Because some reactant is always left over",
           "It can be more than {100} per cent in a good experiment"],
     "e": ["A more accurate balance would not create extra product.",
           "Leftover reactant lowers the yield, it does not raise it.",
           "A figure above {100} per cent means the product is wet or impure."],
     "y": "Atoms are conserved: the theoretical yield already counts every atom available."},
    {"q": "A pupil calculates a percentage yield of {110} per cent. What is the most likely reason?",
     "r": "The product was weighed before it was dry, so the water counted as product",
     "w": ["The reaction was very efficient", "The balance was set to zero",
           "The theoretical yield was too large"],
     "e": ["No reaction can beat its theoretical yield.",
           "Zeroing the balance is correct practice and would not raise the mass.",
           "A theoretical yield that was too large would give a yield BELOW {100} per cent."],
     "y": "Water or unreacted material left in the product adds to the mass weighed."},
    {"q": "Which of these lowers the percentage yield?", "r": "Some of the product stays on the filter paper",
     "w": ["Using a cleaner balance", "Writing the equation correctly", "Using excess of the other reactant"],
     "e": ["A cleaner balance gives a more accurate reading, not a lower yield.",
           "A correct equation gives the right theoretical yield.",
           "Excess of the other reactant does not change what the limiting reagent can give."],
     "y": "Any product left behind in the apparatus is not weighed, so the actual yield falls."},
    {"q": "Why does industry care about percentage yield?", "r": "A low yield wastes raw material and money, so the process may not be worth running",
     "w": ["A low yield makes the product impure", "A low yield makes the reaction dangerous",
           "Yield has nothing to do with cost"],
     "e": ["Purity and yield are different measurements.",
           "A low yield is wasteful, not necessarily dangerous.",
           "Raw materials cost money, so the yield is central to the cost."],
     "y": "If only half the reactant becomes product, twice as much must be bought for the same output."},
    {"q": "Two methods make the same product. One has a yield of {85} per cent and the other {40} per cent. What else must be known before choosing?",
     "r": "The cost and availability of the reactants, the energy needed and how pure the product is",
     "w": ["Nothing: always choose the higher yield", "Only the colour of the product",
           "Only how long each method takes"],
     "e": ["A high yield from a very expensive reactant can still be the worse choice.",
           "Colour is not usually what decides a process.",
           "Time matters, but so do cost, energy and purity."],
     "y": "Yield is one factor among several in choosing an industrial process."},
]

L.lesson(D, S, 27, ("k4-27", "Calculate the percentage yield of a reaction"), [26],
  "Percentage yield = (actual yield ÷ theoretical yield) × 100 per cent.\n"
  "To work one out:\n"
  "1. Find the moles of the limiting reagent.\n"
  "2. Use the equation to find the moles of product expected.\n"
  "3. Change that to a mass: this is the theoretical yield.\n"
  "4. Divide the actual yield by it and multiply by 100.\n"
  "A yield above 100 per cent is impossible; if one is calculated, the product is probably still wet or impure.\n"
  "Yields matter in industry: a low yield wastes raw material, so the cost of the reactants, the energy used and the "
  "purity of the product are all weighed up together when a process is chosen.",
  worked({"m": 10, "y": 4.4},
         "{m} g of calcium carbonate is heated and {y} g of calcium oxide is collected. Find the percentage yield.",
         ["{formula('CaCO3')} → {formula('CaO')} + {formula('CO2')}.",
          "Moles of {formula('CaCO3')} = {m} ÷ {molarMass('CaCO3')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} mol.",
          "Theoretical mass of {formula('CaO')} = {roundTo(molesOf(m, 'CaCO3'), 0.001)} × {molarMass('CaO')} = {roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)} g.",
          "Percentage yield = {y} ÷ {roundTo(massOf(molesOf(m, 'CaCO3'), 'CaO'), 0.01)} × {100}."],
         "{percentYield(y, massOf(molesOf(m, 'CaCO3'), 'CaO'))} per cent",
         checks=["molarMass('CaO') == 56"]),
  [card("c4k27-1", "Percentage yield = actual ÷ theoretical × {100}.",
        ["{8} g collected out of a possible {10} g is {80} per cent"], "k4-27-why"),
   card("c4k27-2", "Work out the theoretical yield from the equation first.",
        ["{10} g {formula('CaCO3')} should give {5.6} g {formula('CaO')}"], "k4-27-theory"),
   card("c4k27-3", "A yield above {100} per cent means the product is wet or impure.",
        ["dry the product to constant mass before weighing it"], "k4-27-over")],
  [bank("k4-27-why", 1, "{X.q}", YIELD, SRC),
   num("k4-27-pc", 1, "A reaction should give {t} g of product and {y} g is collected. What is the percentage yield?",
       "percentYield(y, t)",
       ["Percentage yield = actual ÷ theoretical × {100}.", "{y} ÷ {t} × {100} = {answer} per cent."],
       vars={"t": {"pick": [8, 10, 16, 20, 25, 40, 50]}, "f": {"pick": [0.4, 0.5, 0.6, 0.75, 0.8, 0.9]},
             "y": {"expr": "roundTo(t * f, 0.01)"}},
       misc=[("swap", "percentYield(t, y)", "Divide the ACTUAL yield by the theoretical one."),
             ("diff", "roundTo(t - y, 0.01)", "That is the mass lost, not a percentage.")],
       sources=SRC, unit="%"),
   num("k4-27-theory", 2, "What is the theoretical mass, in grams, of magnesium oxide from burning {m} g of magnesium completely?",
       "roundTo(massOf(molesOf(m, 'Mg'), 'MgO'), 0.01)",
       ["{2}Mg + {formula('O2')} → {2}{formula('MgO')}: {1} mol of Mg gives {1} mol of {formula('MgO')}.",
        "Moles of Mg = {m} ÷ {ram('Mg')} = {roundTo(molesOf(m, 'Mg'), 0.001)} mol.",
        "Mass of {formula('MgO')} = {roundTo(molesOf(m, 'Mg'), 0.001)} × {molarMass('MgO')} = {answer} g."],
       vars={"m": {"pick": [2.4, 4.8, 7.2, 12, 24, 48]}},
       misc=[("same", "m", "Oxygen adds to the mass, so the oxide is heavier than the magnesium."),
             ("half", "roundTo(massOf(molesOf(m, 'Mg') / 2, 'MgO'), 0.01)", "The ratio is {2} : {2}, that is {1} mol of oxide for each {1} mol of magnesium.")],
       sources=SRC, unit="g"),
   num("k4-27-full", 2, "{m} g of magnesium is burned and {y} g of magnesium oxide is collected. What is the percentage yield?",
       "percentYield(y, massOf(molesOf(m, 'Mg'), 'MgO'))",
       ["Theoretical mass of {formula('MgO')} = {roundTo(massOf(molesOf(m, 'Mg'), 'MgO'), 0.01)} g.",
        "Percentage yield = {y} ÷ {roundTo(massOf(molesOf(m, 'Mg'), 'MgO'), 0.01)} × {100} = {answer} per cent."],
       vars={"m": {"pick": [2.4, 4.8, 12, 24]}, "f": {"pick": [0.5, 0.6, 0.75, 0.8, 0.9]},
             "y": {"expr": "roundTo(massOf(molesOf(m, 'Mg'), 'MgO') * f, 0.01)"}},
       misc=[("mg", "percentYield(y, m)", "Compare the yield with the theoretical mass of the OXIDE, not of the magnesium."),
             ("swap", "percentYield(massOf(molesOf(m, 'Mg'), 'MgO'), y)", "Divide the actual yield by the theoretical one.")],
       sources=SRC, unit="%"),
   num("k4-27-over", 3, "A reaction has a theoretical yield of {t} g. A pupil weighs the product and finds {y} g. By what mass, in grams, must the product be wet or impure?",
       "roundTo(y - t, 0.01)",
       ["No reaction can give more than its theoretical yield of {t} g.",
        "The extra mass must be water or impurity: {y} − {t} = {answer} g."],
       vars={"t": {"pick": [10, 20, 25, 40, 50]}, "e": {"pick": [0.5, 1, 1.5, 2, 3]}, "y": {"expr": "roundTo(t + e, 0.01)"}},
       misc=[("sum", "roundTo(y + t, 0.01)", "Find the DIFFERENCE between what was weighed and what was possible."),
             ("pc", "percentYield(y, t)", "That is the percentage yield; the question asks for a mass in grams.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("calculate a percentage yield from experimental masses and explain why yields fall short.",
          "Lesson {26} (theoretical yield and limiting reagents) and Lesson {25} (masses from equations).",
          "Lesson {28} (balancing by the mole concept) and the costing of industrial processes."),
     ("Working out a percentage yield",
      "Percentage yield = (actual ÷ theoretical) × {100} per cent.\n"
      "The four steps:\n"
      "{1}. find the moles of the limiting reagent;\n{2}. use the equation to find the moles of product expected;\n"
      "{3}. change that to a mass: the theoretical yield;\n{4}. divide the actual yield by it and multiply by {100}.\n"
      "Example: {10} g of {formula('CaCO3')} is heated and {4.4} g of {formula('CaO')} is collected.\n"
      "Moles of carbonate = {10} ÷ {100} = {0.1}; so {0.1} mol of {formula('CaO')}, which is {0.1} × {56} = {5.6} g.\n"
      "Percentage yield = {4.4} ÷ {5.6} × {100} = {78.6} per cent."),
     ("Why yields fall short, and why it matters",
      "Common reasons:\n"
      "• product left on the filter paper, the beaker or the stirring rod;\n• product that stays dissolved in the solvent;\n"
      "• a reaction that does not go to completion, or that reverses;\n• side reactions making something else.\n"
      "A yield above {100} per cent is impossible, because atoms are conserved. If one is calculated, the product was "
      "probably weighed before it was dry, so water was counted as product. The cure is to dry to constant mass.\n"
      "In industry a low yield means buying more raw material for the same output, so it costs more. A process is chosen "
      "by weighing up yield, the cost of the reactants, the energy needed, the time taken and the purity of the product.")],
    key_words=[("actual yield", "the mass of product really collected"),
               ("theoretical yield", "the mass the equation predicts"),
               ("percentage yield", "actual ÷ theoretical × {100}"),
               ("constant mass", "the mass once no more water can be driven off")],
    examples=["{4.4} g of a possible {5.6} g: {78.6} per cent", "{8} g of a possible {10} g: {80} per cent"],
    mistake=("a yield of {110} per cent shows an unusually good reaction", "it shows the product was wet or impure",
             "Atoms are conserved, so no reaction can beat its theoretical yield.")))

# ---------------------------------------------------------------- 28. Balancing equations by the mole concept
BAL = [
    {"q": "Why must a chemical equation be balanced?", "r": "Atoms are neither made nor destroyed, so each element must have the same number of atoms on both sides",
     "w": ["To make the equation look tidy", "So that the masses of the reactants are equal",
           "So that there is the same number of molecules on both sides"],
     "e": ["Balancing is not about appearance; it states a law of nature.",
           "The two reactants may have very different masses; it is the atoms that must match.",
           "The number of MOLECULES often changes; it is the atoms that are conserved."],
     "y": "Balancing states the conservation of matter: the same atoms are simply rearranged."},
    {"q": "What may be changed when balancing an equation?", "r": "Only the coefficients, the numbers in front of the formulae",
     "w": ["The subscripts inside the formulae", "Both the subscripts and the coefficients", "Nothing at all"],
     "e": ["Changing a subscript changes the substance: {formula('H2O')} is water, but {formula('H2O2')} is not.",
           "Subscripts must never be changed; they belong to the formula.",
           "The coefficients are exactly what is adjusted."],
     "y": "A coefficient says how many units react; a subscript says what the substance IS."},
    {"q": "What does the equation {2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')} tell us?",
     "r": "{2} mol of hydrogen react with {1} mol of oxygen to give {2} mol of water",
     "w": ["{2} g of hydrogen react with {1} g of oxygen", "{2} molecules make {1} molecule",
           "Hydrogen and oxygen react in equal masses"],
     "e": ["The coefficients are moles (or molecules), not grams.",
           "It is {2} molecules of hydrogen with {1} of oxygen giving {2} of water.",
           "{4} g of hydrogen react with {32} g of oxygen: not equal masses."],
     "y": "The coefficients give the ratio of moles, which is also the ratio of molecules."},
    {"q": "In {formula('Fe2O3')} + {3}{formula('CO')} → {2}Fe + {3}{formula('CO2')}, how many moles of carbon monoxide react with {1} mol of iron(III) oxide?",
     "r": "{3} mol", "w": ["{1} mol", "{2} mol", "{6} mol"],
     "e": ["The coefficient of {formula('CO')} is {3}, not {1}.",
           "{2} is the coefficient of the iron.",
           "{6} is twice the coefficient of the carbon monoxide."],
     "y": "Read the coefficient in front of {formula('CO')}: it is {3}."},
    {"q": "A pupil balances an equation by changing {formula('H2O')} into {formula('H2O2')}. What is wrong?",
     "r": "{formula('H2O2')} is hydrogen peroxide, a different substance from water",
     "w": ["Nothing: it balances the equation", "{formula('H2O2')} does not exist",
           "The coefficient should have been changed to {2} as well"],
     "e": ["Balancing must not change which substances take part.",
           "Hydrogen peroxide does exist, but it is not water.",
           "No change of coefficient can make up for changing the formula."],
     "y": "Subscripts belong to the formula of the substance and must never be changed to balance."},
]

L.lesson(D, S, 28, ("k4-28", "Balance chemical equations using the mole concept"), [25],
  "A balanced equation has the same number of atoms of each element on both sides, because atoms are neither made nor "
  "destroyed. The numbers put in front of the formulae are the coefficients; they give the ratio of moles.\n"
  "Rules:\n"
  "• Change only the coefficients. Never change a subscript: that would change the substance.\n"
  "• Balance the element that appears in fewest places first, and leave hydrogen and oxygen to the end.\n"
  "• Count again at the end, element by element.\n"
  "Example: balance Fe2O3 + CO → Fe + CO2.\n"
  "Iron: 2 on the left, so put 2 in front of Fe. Oxygen: 3 + 1 = 4 on the left against 2 on the right; "
  "trying 3CO and 3CO2 gives 3 + 3 = 6 on each side. The balanced equation is Fe2O3 + 3CO → 2Fe + 3CO2.",
  worked({"z": 1},
         "Balance {formula('Fe2O3')} + {formula('CO')} → Fe + {formula('CO2')}.",
         ["Iron appears in fewest places: {2} on the left, so write {2}Fe on the right.",
          "Carbon: {1} on each side so far; oxygen: {3} + {1} = {4} on the left and {2} on the right.",
          "Try {3}{formula('CO')} and {3}{formula('CO2')}: oxygen becomes {3} + {3} = {6} on the left and {6} on the right.",
          "Count again: Fe {2} and {2}; C {3} and {3}; O {6} and {6}."],
         "{formula('Fe2O3')} + {3}{formula('CO')} → {2}Fe + {3}{formula('CO2')}",
         checks=[]),
  [card("c4k28-1", "Balance by changing coefficients only; never change a subscript.",
        ["{formula('H2O')} must stay {formula('H2O')}, not become {formula('H2O2')}"], "k4-28-rules"),
   card("c4k28-2", "The coefficients give the ratio of moles.",
        ["{2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')} is {2} : {1} : {2} by moles"], "k4-28-coef"),
   card("c4k28-3", "Count every element again at the end.",
        ["{formula('Fe2O3')} + {3}{formula('CO')} → {2}Fe + {3}{formula('CO2')}: O is {6} on each side"], "k4-28-count")],
  [bank("k4-28-rules", 1, "{X.q}", BAL, SRC),
   num("k4-28-coef", 1, "In the equation {E.eq}, what is the coefficient of {E.t}?",
       "E.c",
       ["Read the number written in front of {E.t}.", "It is {answer}. (A formula with no number in front has a coefficient of {1}.)"],
       vars={"E": {"pick": [
           {"eq": "{2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')}", "t": "{formula('O2')}", "c": 1},
           {"eq": "{2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')}", "t": "{formula('H2O')}", "c": 2},
           {"eq": "{formula('Fe2O3')} + {3}{formula('CO')} → {2}Fe + {3}{formula('CO2')}", "t": "{formula('CO')}", "c": 3},
           {"eq": "{formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}", "t": "{formula('H2')}", "c": 3},
           {"eq": "{formula('CH4')} + {2}{formula('O2')} → {formula('CO2')} + {2}{formula('H2O')}", "t": "{formula('O2')}", "c": 2},
           {"eq": "{2}{formula('Mg')} + {formula('O2')} → {2}{formula('MgO')}", "t": "{formula('MgO')}", "c": 2}]}},
       misc=[("one", "1", "A number is written in front of {E.t} in this equation: read it again."),
             ("sub", "2", "Read the number in FRONT of the formula, not a subscript inside it.")],
       sources=SRC),
   mcq("k4-28-count", 2, "Which equation is correctly balanced?",
       "{B.r}", [("{B.w1}", "w1"), ("{B.w2}", "w2"), ("{B.w3}", "w3")],
       ["{B.y}", "So the answer is: {answer}."],
       vars={"B": {"pick": [
           {"r": "{2}{formula('Mg')} + {formula('O2')} → {2}{formula('MgO')}",
            "w1": "{formula('Mg')} + {formula('O2')} → {formula('MgO')}",
            "w2": "{formula('Mg')} + {formula('O2')} → {formula('MgO2')}",
            "w3": "{2}{formula('Mg')} + {formula('O2')} → {formula('MgO')}",
            "y": "Count the atoms: Mg {2} and {2}; O {2} and {2}. The others leave oxygen unbalanced or change the formula."},
           {"r": "{formula('CH4')} + {2}{formula('O2')} → {formula('CO2')} + {2}{formula('H2O')}",
            "w1": "{formula('CH4')} + {formula('O2')} → {formula('CO2')} + {formula('H2O')}",
            "w2": "{formula('CH4')} + {2}{formula('O2')} → {formula('CO2')} + {formula('H2O')}",
            "w3": "{formula('CH4')} + {3}{formula('O2')} → {formula('CO2')} + {2}{formula('H2O')}",
            "y": "Count: C {1} and {1}; H {4} and {4}; O {4} and {4}."},
           {"r": "{formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}",
            "w1": "{formula('N2')} + {formula('H2')} → {formula('NH3')}",
            "w2": "{formula('N2')} + {2}{formula('H2')} → {2}{formula('NH3')}",
            "w3": "{formula('N2')} + {3}{formula('H2')} → {formula('NH3')}",
            "y": "Count: N {2} and {2}; H {6} and {6}."},
           {"r": "{2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')}",
            "w1": "{formula('H2')} + {formula('O2')} → {formula('H2O')}",
            "w2": "{formula('H2')} + {formula('O2')} → {formula('H2O2')}",
            "w3": "{2}{formula('H2')} + {2}{formula('O2')} → {2}{formula('H2O')}",
            "y": "Count: H {4} and {4}; O {2} and {2}."}]}},
       misc=[("w1", "{B.y}"), ("w2", "{B.y}"), ("w3", "{B.y}"), ],
       sources=SRC),
   num("k4-28-moles", 2, "In {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')}, how many moles of hydrogen are needed for {n} mol of nitrogen?",
       "3 * n",
       ["The ratio of {formula('N2')} to {formula('H2')} is {1} : {3}.", "{n} × {3} = {answer} mol."],
       vars={"n": {"pick": [0.1, 0.25, 0.5, 1, 2, 2.5]}},
       misc=[("two", "2 * n", "{2} is the coefficient of the ammonia, not of the hydrogen."),
             ("same", "n", "Each mole of nitrogen needs {3} mol of hydrogen.")],
       sources=SRC, unit="mol"),
   num("k4-28-mass", 3, "In {2}{formula('Mg')} + {formula('O2')} → {2}{formula('MgO')}, what mass of oxygen, in grams, reacts with {m} g of magnesium?",
       "roundTo(massOf(molesOf(m, 'Mg') / 2, 'O2'), 0.01)",
       ["Moles of Mg = {m} ÷ {ram('Mg')} = {roundTo(molesOf(m, 'Mg'), 0.001)} mol.",
        "The ratio of Mg to {formula('O2')} is {2} : {1}, so moles of {formula('O2')} = {roundTo(molesOf(m, 'Mg') / 2, 0.001)} mol.",
        "Mass = {roundTo(molesOf(m, 'Mg') / 2, 0.001)} × {molarMass('O2')} = {answer} g."],
       vars={"m": {"pick": [2.4, 4.8, 12, 24, 48]}},
       misc=[("noratio", "roundTo(massOf(molesOf(m, 'Mg'), 'O2'), 0.01)", "The ratio is {2} mol of Mg to {1} mol of {formula('O2')}: halve it."),
             ("atom", "roundTo(massOf(molesOf(m, 'Mg') / 2, 'O'), 0.01)", "Oxygen gas is {formula('O2')}, of molar mass {molarMass('O2')}.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("balance an equation by changing only the coefficients, and read the mole ratio from it.",
          "Form Three balancing simple equations and Lesson {25} (using the ratio).",
          "Lesson {29} (adding state symbols) and every calculation that starts from an equation."),
     ("Why and how to balance",
      "In a chemical reaction atoms are neither made nor destroyed; they are only rearranged. So an equation must have the "
      "same number of atoms of each element on both sides.\n"
      "The numbers written IN FRONT of the formulae are the coefficients. They may be changed freely. "
      "The small numbers INSIDE a formula are subscripts; they must never be changed, because they say what the substance is. "
      "Changing {formula('H2O')} to {formula('H2O2')} turns water into hydrogen peroxide.\n"
      "A useful order:\n"
      "{1}. balance the element that appears in the fewest places;\n{2}. leave hydrogen and oxygen until last;\n"
      "{3}. count every element again at the end."),
     ("A worked example and the mole ratio",
      "Balance {formula('Fe2O3')} + {formula('CO')} → Fe + {formula('CO2')}.\n"
      "• Iron: {2} on the left, so write {2}Fe.\n"
      "• Oxygen: {3} + {1} = {4} on the left, {2} on the right. Try {3}{formula('CO')} and {3}{formula('CO2')}: "
      "{3} + {3} = {6} on the left and {6} on the right.\n"
      "• Carbon: {3} and {3}. Balanced: {formula('Fe2O3')} + {3}{formula('CO')} → {2}Fe + {3}{formula('CO2')}.\n"
      "Once balanced, the coefficients give the MOLE RATIO, which is what every calculation uses: {1} mol of "
      "{formula('Fe2O3')} needs {3} mol of {formula('CO')} and gives {2} mol of iron.")],
    key_words=[("coefficient", "the number written in front of a formula"),
               ("subscript", "the small number inside a formula, which must not be changed"),
               ("conservation of matter", "atoms are neither made nor destroyed in a reaction"),
               ("mole ratio", "the ratio given by the coefficients")],
    examples=["{2}{formula('Mg')} + {formula('O2')} → {2}{formula('MgO')}", "{formula('CH4')} + {2}{formula('O2')} → {formula('CO2')} + {2}{formula('H2O')}"],
    mistake=("balance {formula('H2')} + {formula('O2')} → {formula('H2O')} by writing {formula('H2O2')}", "write {2}{formula('H2')} + {formula('O2')} → {2}{formula('H2O')}",
             "Changing the subscript changes the substance. Only coefficients may be changed.")))

# ---------------------------------------------------------------- 29. State symbols
STATES = [
    {"q": "What does the state symbol (aq) mean?", "r": "Dissolved in water: an aqueous solution",
     "w": ["A pure liquid", "A gas", "A solid"],
     "e": ["A pure liquid is shown by (l), such as water itself.",
           "A gas is shown by (g).",
           "A solid is shown by (s)."],
     "y": "(aq) shows that the substance is dissolved in water, as in {formula('NaCl')}(aq)."},
    {"q": "Which state symbol is used for water formed in a neutralisation at room temperature?", "r": "(l)",
     "w": ["(aq)", "(g)", "(s)"],
     "e": ["(aq) is for a substance DISSOLVED in water, not for water itself.",
           "Water is a gas only above {100} °C.",
           "Water is a solid only below {0} °C."],
     "y": "Water at room temperature is a pure liquid, so it takes (l)."},
    {"q": "Why are state symbols useful in an equation?", "r": "They show what would be seen: a precipitate, a gas given off, or a clear solution",
     "w": ["They make the equation balance", "They give the mass of each substance",
           "They show how fast the reaction goes"],
     "e": ["Balancing is done with coefficients; state symbols do not affect it.",
           "Masses come from the moles and the molar masses.",
           "Speed is not shown by an equation at all."],
     "y": "A (s) among (aq) substances means a precipitate; a (g) means bubbles."},
    {"q": "In {formula('Zn')}(s) + {formula('H2SO4')}(aq) → {formula('ZnSO4')}(aq) + {formula('H2')}(g), what would be seen?",
     "r": "The zinc dissolves and bubbles of gas are given off",
     "w": ["A precipitate forms", "Nothing changes", "The solution turns solid"],
     "e": ["No (s) appears among the products, so there is no precipitate.",
           "A gas is given off, which is easy to see.",
           "The products are a solution and a gas."],
     "y": "The (g) tells you to expect bubbles, and the zinc (s) disappears into the solution."},
    {"q": "In {formula('Pb(NO3)2')}(aq) + {2}{formula('KI')}(aq) → {formula('PbI2')}(s) + {2}{formula('KNO3')}(aq), what would be seen?",
     "r": "A precipitate forms", "w": ["Bubbles of gas", "The mixture boils", "Nothing at all"],
     "e": ["There is no (g) in the equation, so no gas is given off.",
           "Nothing in the equation suggests boiling.",
           "The (s) among the products is a clear change."],
     "y": "An (s) formed from two (aq) solutions is a precipitate: here the yellow lead(II) iodide."},
]

L.lesson(D, S, 29, ("k4-29", "Write chemical equations including state symbols"), [28],
  "State symbols are written after each formula to show the physical state:\n"
  "• (s) solid  • (l) pure liquid  • (g) gas  • (aq) dissolved in water (aqueous)\n"
  "Examples:\n"
  "Zn(s) + H2SO4(aq) → ZnSO4(aq) + H2(g)\n"
  "NaOH(aq) + HCl(aq) → NaCl(aq) + H2O(l)\n"
  "Pb(NO3)2(aq) + 2KI(aq) → PbI2(s) + 2KNO3(aq)\n"
  "They are useful because they tell you what would be seen: an (s) formed from (aq) solutions is a precipitate, "
  "a (g) means bubbles, and water formed in a neutralisation is (l), not (aq).\n"
  "A full equation is balanced first, then the state symbols are added.",
  worked({"z": 1},
         "Write the equation, with state symbols, for adding dilute hydrochloric acid to solid calcium carbonate.",
         ["The reactants are solid calcium carbonate and hydrochloric acid solution.",
          "A carbonate with an acid gives a salt, water and carbon dioxide.",
          "Balance first: {formula('CaCO3')} + {2}{formula('HCl')} → {formula('CaCl2')} + {formula('H2O')} + {formula('CO2')}.",
          "Then add the states: the carbonate is (s), the acid and the salt are (aq), the water is (l) and the carbon dioxide is (g)."],
         "{formula('CaCO3')}(s) + {2}{formula('HCl')}(aq) → {formula('CaCl2')}(aq) + {formula('H2O')}(l) + {formula('CO2')}(g)",
         checks=[]),
  [card("c4k29-1", "(s) solid, (l) pure liquid, (g) gas, (aq) dissolved in water.",
        ["{formula('NaCl')}(aq) is salt solution; {formula('H2O')}(l) is water itself"], "k4-29-which"),
   card("c4k29-2", "An (s) made from (aq) solutions is a precipitate.",
        ["{formula('PbI2')}(s) from two solutions: a yellow precipitate"], "k4-29-see"),
   card("c4k29-3", "Balance the equation first, then add the state symbols.",
        ["{formula('CaCO3')}(s) + {2}{formula('HCl')}(aq) → {formula('CaCl2')}(aq) + {formula('H2O')}(l) + {formula('CO2')}(g)"], "k4-29-write")],
  [bank("k4-29-which", 1, "{X.q}", STATES, SRC),
   match("k4-29-match", 1, "Match each state symbol to its meaning.",
         [("(s)", "Solid"), ("(l)", "Pure liquid"), ("(g)", "Gas"), ("(aq)", "Dissolved in water")],
         pick=3, sources=SRC),
   mcq("k4-29-see", 2, "What would be seen in the reaction {R.eq}?",
       "{R.r}", [("{R.w1}", "w1"), ("{R.w2}", "w2"), ("{R.w3}", "w3")],
       ["{R.y}", "So the answer is: {answer}."],
       vars={"R": {"pick": [
           {"eq": "{formula('Zn')}(s) + {formula('H2SO4')}(aq) → {formula('ZnSO4')}(aq) + {formula('H2')}(g)",
            "r": "The zinc dissolves and bubbles of gas are given off",
            "w1": "A precipitate forms", "w2": "Nothing changes", "w3": "The solution turns solid",
            "y": "The (g) means a gas is given off, and the solid zinc passes into solution."},
           {"eq": "{formula('Pb(NO3)2')}(aq) + {2}{formula('KI')}(aq) → {formula('PbI2')}(s) + {2}{formula('KNO3')}(aq)",
            "r": "A precipitate forms from two clear solutions",
            "w1": "Bubbles of gas are given off", "w2": "The mixture boils", "w3": "Nothing at all",
            "y": "An (s) formed from (aq) solutions is a precipitate: yellow lead(II) iodide."},
           {"eq": "{formula('NaOH')}(aq) + {formula('HCl')}(aq) → {formula('NaCl')}(aq) + {formula('H2O')}(l)",
            "r": "No visible change, though the mixture warms up",
            "w1": "A precipitate forms", "w2": "Bubbles of gas are given off", "w3": "The solution turns blue",
            "y": "Every product is (aq) or (l), so nothing can be seen; only an indicator or a thermometer shows the change."},
           {"eq": "{formula('CaCO3')}(s) + {2}{formula('HCl')}(aq) → {formula('CaCl2')}(aq) + {formula('H2O')}(l) + {formula('CO2')}(g)",
            "r": "The solid disappears and bubbles of gas are given off",
            "w1": "A precipitate forms", "w2": "Nothing changes", "w3": "The liquid turns into a solid",
            "y": "The (s) reactant is used up and the (g) product bubbles away."}]}},
       misc=[("w1", "{R.y}"), ("w2", "{R.y}"), ("w3", "{R.y}")],
       sources=SRC),
   mcq("k4-29-write", 2, "Which state symbol belongs to {W.n} in an equation at room temperature?",
       "{W.r}", [("{W.w1}", "w1"), ("{W.w2}", "w2"), ("{W.w3}", "w3")],
       ["{W.y}", "So the answer is: {answer}."],
       vars={"W": {"pick": [
           {"n": "the water made in a neutralisation", "r": "(l)", "w1": "(aq)", "w2": "(g)", "w3": "(s)",
            "y": "Water at room temperature is a pure liquid; (aq) is for things dissolved IN water."},
           {"n": "dilute hydrochloric acid", "r": "(aq)", "w1": "(l)", "w2": "(g)", "w3": "(s)",
            "y": "A dilute acid is hydrogen chloride dissolved in water, so it is aqueous."},
           {"n": "the carbon dioxide given off by a carbonate", "r": "(g)", "w1": "(aq)", "w2": "(l)", "w3": "(s)",
            "y": "Carbon dioxide bubbles away as a gas."},
           {"n": "the marble chips added to an acid", "r": "(s)", "w1": "(aq)", "w2": "(l)", "w3": "(g)",
            "y": "Marble is solid calcium carbonate."},
           {"n": "the copper(II) sulphate solution in a beaker", "r": "(aq)", "w1": "(s)", "w2": "(l)", "w3": "(g)",
            "y": "The salt is dissolved in water, so it is aqueous."}]}},
       misc=[("w1", "{W.y}"), ("w2", "{W.y}"), ("w3", "{W.y}")],
       sources=SRC),
   order("k4-29-steps", 3, "{A.q}",
         ["{A.s[0]}", "{A.s[1]}", "{A.s[2]}", "{A.s[3]}", "{A.s[4]}"],
         vars={"A": {"pick": [
             {"q": "Put the steps of writing a full chemical equation in order.",
              "s": ["Name the reactants and the products",
                    "Write the correct formula for each one",
                    "Balance the equation by changing the coefficients only",
                    "Count every element again to check",
                    "Add the state symbols after each formula"]},
             {"q": "Put these steps of predicting what will be seen in order.",
              "s": ["Write the balanced equation with state symbols",
                    "Look for an (s) among the products of (aq) reactants",
                    "If there is one, expect a precipitate",
                    "Look for a (g) among the products",
                    "If there is one, expect bubbles of gas"]},
             {"q": "Put the steps of working out a mass from an equation in order.",
              "s": ["Write the balanced equation",
                    "Change the mass given into moles",
                    "Use the mole ratio from the equation",
                    "Change the moles of the product into a mass",
                    "Write the answer with its unit"]}]}},
         sources=SRC)],
  learn=learn(
    [goal("add state symbols to a balanced equation and use them to say what would be seen.",
          "Lesson {28} (balancing) and Form Three states of matter.",
          "writing the full equations required in examinations, and ionic equations in Form Five."),
     ("The four symbols",
      "A state symbol is written just after each formula:\n"
      "• (s) solid  • (l) pure liquid  • (g) gas  • (aq) aqueous, that is dissolved in water.\n"
      "Take care with (l) and (aq). Water made in a neutralisation is {formula('H2O')}(l), because it is water itself. "
      "Salt dissolved in water is {formula('NaCl')}(aq), because it is dissolved IN water.\n"
      "Write the equation and balance it first; the state symbols are added last, and never change the balancing."),
     ("Reading what would be seen",
      "State symbols turn an equation into a description of the experiment.\n"
      "• {formula('Zn')}(s) + {formula('H2SO4')}(aq) → {formula('ZnSO4')}(aq) + {formula('H2')}(g): "
      "the solid disappears and bubbles are given off.\n"
      "• {formula('Pb(NO3)2')}(aq) + {2}{formula('KI')}(aq) → {formula('PbI2')}(s) + {2}{formula('KNO3')}(aq): "
      "two clear solutions give a yellow precipitate.\n"
      "• {formula('NaOH')}(aq) + {formula('HCl')}(aq) → {formula('NaCl')}(aq) + {formula('H2O')}(l): "
      "nothing is seen at all, though the mixture warms up.\n"
      "So an (s) among (aq) substances means a precipitate, and a (g) means bubbles.")],
    key_words=[("state symbol", "(s), (l), (g) or (aq), showing the physical state"),
               ("aqueous", "dissolved in water"),
               ("precipitate", "an insoluble solid formed when two solutions are mixed"),
               ("neutralisation", "the reaction of an acid with a base to give a salt and water")],
    examples=["{formula('Zn')}(s) + {formula('H2SO4')}(aq) → {formula('ZnSO4')}(aq) + {formula('H2')}(g)",
              "{formula('NaOH')}(aq) + {formula('HCl')}(aq) → {formula('NaCl')}(aq) + {formula('H2O')}(l)"],
    mistake=("the water made in a neutralisation is written {formula('H2O')}(aq)", "it is {formula('H2O')}(l)",
             "(aq) means dissolved in water; water cannot be dissolved in itself.")))
