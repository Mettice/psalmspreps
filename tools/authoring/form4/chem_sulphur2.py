"""Form 4 Chemistry, Term 1, rows 5-9: hydrogen sulphide, the sulphides of sodium and iron, sulphuric acid and the
uses of sulphur. Run: python tools/authoring/form4/chem_sulphur2.py (rows 1-4 are in chem_sulphur.py)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order, match
from common import goal, bank

L.use_class("form-4", "Form 4")
D, S = "chemistry", "chemistry"
SRC = ["sulphur"]

# ---------------------------------------------------------------- 5. Lab preparation and physical properties of H2S
H2SPREP = [
    {"q": "Which reagents are used to prepare hydrogen sulphide in the laboratory?", "r": "Iron(II) sulphide and dilute hydrochloric acid",
     "w": ["Iron(II) sulphate and dilute hydrochloric acid", "Iron filings and dilute hydrochloric acid",
           "Iron(II) sulphide and concentrated nitric acid"],
     "e": ["A sulphate gives no {formula('H2S')} with a dilute acid; a sulphide does.",
           "Iron with a dilute acid gives hydrogen, not hydrogen sulphide.",
           "Concentrated nitric acid is an oxidising acid; it would oxidise the sulphide to sulphur."],
     "y": "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}."},
    {"q": "What does hydrogen sulphide smell like?", "r": "Rotten eggs",
     "w": ["A sharp choking smell", "Sweet and pleasant", "It has no smell"],
     "e": ["The sharp choking smell is sulphur dioxide.",
           "The smell is strongly unpleasant.",
           "Even a trace can be smelt, which is one way it is noticed."],
     "y": "{formula('H2S')} is a colourless, poisonous gas that smells of rotten eggs."},
    {"q": "How is hydrogen sulphide collected?", "r": "By downward delivery, because it is denser than air",
     "w": ["By upward delivery", "Over water in an open trough", "It cannot be collected"],
     "e": ["Its relative molecular mass is {34}, above the average for air, so it sinks.",
           "It is fairly soluble in water, so some would be lost.",
           "It is collected in the ordinary way, in a fume cupboard."],
     "y": "A gas denser than air and soluble in water is collected by downward delivery."},
    {"q": "Why is hydrogen sulphide dangerous to work with?", "r": "It is very poisonous, and it dulls the sense of smell so that it may not be noticed",
     "w": ["It explodes in contact with air", "It is only unpleasant, not harmful", "It burns the skin on contact"],
     "e": ["It burns in air, but it does not explode on contact.",
           "It is seriously poisonous and has killed people.",
           "The danger is from breathing it in, not from skin contact."],
     "y": "After a short time the smell can no longer be noticed, so the gas must always be used in a fume cupboard."},
    {"q": "How does hydrogen sulphide behave in water?", "r": "It dissolves fairly well, giving a weakly acidic solution",
     "w": ["It is insoluble", "It dissolves to give an alkaline solution", "It reacts violently with water"],
     "e": ["It is fairly soluble: a few volumes dissolve in one volume of water.",
           "The solution turns blue litmus red, so it is acidic.",
           "There is no violent reaction; it simply dissolves."],
     "y": "The solution is a weak acid, sometimes called hydrosulphuric acid."},
]

L.lesson(D, S, 5, ("k4-5", "Prepare hydrogen sulphide in the laboratory and state its physical properties"), [3],
  "Laboratory preparation: a metal sulphide and a dilute acid.\n"
  "FeS + 2HCl → FeCl2 + H2S\n"
  "Iron(II) sulphide is placed in a flask and dilute hydrochloric acid is run onto it. No heat is needed. "
  "The gas is collected by downward delivery, because it is denser than air.\n"
  "Dilute sulphuric acid may be used instead. Nitric acid must not be used: it is an oxidising acid and gives sulphur instead.\n"
  "Physical properties: a colourless, very poisonous gas smelling of rotten eggs; denser than air (relative molecular mass 34); "
  "fairly soluble in water, giving a weakly acidic solution. It dulls the sense of smell, so it must always be made in a fume cupboard.",
  worked({"z": 1},
         "Write the equation for the laboratory preparation of hydrogen sulphide and explain why nitric acid is not used.",
         ["A metal sulphide with a dilute acid gives a salt and hydrogen sulphide.",
          "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}.",
          "Nitric acid is an oxidising acid.",
          "It would oxidise the hydrogen sulphide to sulphur, so the gas would not be collected."],
         "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}; nitric acid would oxidise the gas to sulphur",
         checks=[]),
  [card("c4k5-1", "A metal sulphide with a dilute acid gives hydrogen sulphide.",
        ["{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}"], "k4-5-prep"),
   card("c4k5-2", "{formula('H2S')} is denser than air, so it is collected by downward delivery.",
        ["relative molecular mass {34}, above the average for air"], "k4-5-mass"),
   card("c4k5-3", "{formula('H2S')} is very poisonous and dulls the sense of smell: use a fume cupboard.",
        ["the rotten-egg smell fades even though the gas is still there"], "k4-5-safe")],
  [bank("k4-5-prep", 1, "{X.q}", H2SPREP, SRC),
   num("k4-5-mass", 1, "Find the relative molecular mass of {formula(F)}.",
       "molarMass(F)",
       ["Add the relative atomic mass of every atom in the formula.", "The relative molecular mass of {formula(F)} is {answer}."],
       vars={"F": {"pick": ["H2S", "FeS", "Na2S", "PbS", "ZnS", "FeCl2"]}},
       misc=[("atoms", "totalAtoms(F)", "{totalAtoms(F)} is the number of atoms, not the mass."),
             ("one", "ram(symbolsIn(F)[0])", "Include every atom in the formula, not just the first element.")],
       sources=SRC),
   mcq("k4-5-safe", 2, "Why must hydrogen sulphide always be prepared in a fume cupboard?",
       "{A.r}", [("{A.w1}", "w1"), ("{A.w2}", "w2"), ("{A.w3}", "w3")],
       ["{A.y}", "So the answer is: {answer}."],
       vars={"A": {"pick": [
           {"r": "It is very poisonous, and it soon dulls the sense of smell so that it is no longer noticed",
            "w1": "It smells unpleasant, but it is harmless", "w2": "It explodes when it meets air",
            "w3": "It burns the skin on contact", "y": "The fading smell is the real danger: a worker may keep breathing it without knowing."},
           {"r": "Breathing it damages the lungs and in larger amounts it can kill",
            "w1": "It stains the skin yellow", "w2": "It makes glassware crack", "w3": "It is harmless once it is dry",
            "y": "{formula('H2S')} is seriously poisonous, so the fumes must be drawn away."},
           {"r": "It is denser than air, so it gathers at low level where people work",
            "w1": "It rises and escapes through the roof", "w2": "It is destroyed by daylight",
            "w3": "It turns into harmless sulphur in air", "y": "With a relative molecular mass of {34}, {formula('H2S')} sinks instead of rising away."}]}},
       misc=[("w1", "{A.y}"), ("w2", "{A.y}"), ("w3", "{A.y}")],
       sources=SRC),
   num("k4-5-vol", 2, "What volume of hydrogen sulphide, in dm³ at s.t.p., is given off when {n} mol of iron(II) sulphide reacts completely with dilute hydrochloric acid?",
       "gasVolume(n)",
       ["{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}.",
        "{1} mol of {formula('FeS')} gives {1} mol of {formula('H2S')}.",
        "At s.t.p. {1} mol of any gas is {22.4} dm³, so the volume is {n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("double", "gasVolume(2 * n)", "The equation gives {1} mol of gas for each {1} mol of sulphide, not {2}."),
             ("div", "volumeToMoles(n)", "Multiply the moles by {22.4} dm³/mol.")],
       sources=SRC, unit="dm³"),
   num("k4-5-mols", 3, "What mass of iron(II) sulphide, in grams, is needed to make {n} mol of hydrogen sulphide?",
       "massOf(n, 'FeS')",
       ["{1} mol of {formula('FeS')} gives {1} mol of {formula('H2S')}, so {n} mol of {formula('FeS')} is needed.",
        "The relative formula mass of {formula('FeS')} is {molarMass('FeS')}.",
        "Mass = moles × molar mass = {n} × {molarMass('FeS')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("div", "roundTo(n / molarMass('FeS'), 0.0001)", "Mass = moles × molar mass: multiply, do not divide."),
             ("h2s", "massOf(n, 'H2S')", "The question asks for the mass of {formula('FeS')}, not of the gas.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("write the equation for preparing hydrogen sulphide, explain how it is collected and state its properties and dangers.",
          "Lesson {3} (preparing a gas and collecting it) and Form Three acids with salts.",
          "Lesson {6} (the chemical properties of {formula('H2S')}) and the sulphides of Lesson {7}."),
     ("Preparation",
      "A metal sulphide and a dilute acid give hydrogen sulphide:\n"
      "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}\n"
      "Lumps of iron(II) sulphide are placed in a flask and dilute hydrochloric acid is run onto them from a thistle funnel. "
      "No heating is needed.\n"
      "Dilute sulphuric acid works as well. Nitric acid must NOT be used: it is an oxidising acid and would oxidise the "
      "hydrogen sulphide to sulphur, leaving a yellow deposit instead of a gas."),
     ("Physical properties and safety",
      "Hydrogen sulphide is a colourless gas with the smell of rotten eggs.\n"
      "Its relative molecular mass is {2} × {1} + {32} = {34}, above the average for air, so it is denser than air and is "
      "collected by downward delivery.\n"
      "It is fairly soluble in water, giving a weakly acidic solution that turns blue litmus red.\n"
      "It is very poisonous. Worse, it quickly dulls the sense of smell, so a worker may stop noticing it while still "
      "breathing it in. It must always be prepared and used in a fume cupboard.")],
    key_words=[("sulphide", "a compound of a metal with sulphur, such as {formula('FeS')}"),
               ("oxidising acid", "an acid such as nitric acid that oxidises what it reacts with"),
               ("downward delivery", "collecting a dense gas at the bottom of a jar")],
    examples=["{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}", "RMM of {formula('H2S')} = {34}"],
    mistake=("hydrogen sulphide is prepared with dilute nitric acid", "a non-oxidising acid such as hydrochloric acid is used",
             "Nitric acid would oxidise the gas to sulphur, so none would be collected.")))

# ---------------------------------------------------------------- 6. Chemical properties of H2S
H2SCHEM = [
    {"q": "Hydrogen sulphide burns in plenty of air. What is formed?", "r": "Sulphur dioxide and water",
     "w": ["Sulphur and water only", "Hydrogen and sulphur", "Sulphur trioxide and hydrogen"],
     "e": ["Sulphur and water are formed when the air supply is LIMITED.",
           "Burning joins the gas with oxygen; it does not split it into its elements.",
           "{formula('SO3')} is not formed by simple burning, and the hydrogen is oxidised to water."],
     "y": "{2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}, with a blue flame."},
    {"q": "Hydrogen sulphide burns in a limited supply of air. What is seen?", "r": "A yellow deposit of sulphur forms",
     "w": ["A white solid forms", "The flame goes out at once", "A brown gas is given off"],
     "e": ["No white solid is formed in this reaction.",
           "It still burns; the limited air changes the product, not whether it burns.",
           "A brown gas is nitrogen dioxide, which is not formed here."],
     "y": "{2}{formula('H2S')} + {formula('O2')} → {2}S + {2}{formula('H2O')}: with too little oxygen the sulphur is not oxidised."},
    {"q": "Why is hydrogen sulphide described as a reducing agent?", "r": "It gives up its hydrogen or its electrons, and is itself oxidised to sulphur",
     "w": ["It adds oxygen to other substances", "It is an acid in water", "It is denser than air"],
     "e": ["Adding oxygen is what an OXIDISING agent does.",
           "Being an acid is a separate property; it has nothing to do with reduction.",
           "Density has nothing to do with being a reducing agent."],
     "y": "With most oxidising agents, {formula('H2S')} is oxidised and a pale yellow deposit of sulphur appears."},
    {"q": "Hydrogen sulphide is passed into lead(II) nitrate solution. What is seen?", "r": "A black precipitate of lead(II) sulphide",
     "w": ["A white precipitate", "A yellow solution", "No change"],
     "e": ["Lead(II) sulphide is black, not white.",
           "A precipitate forms rather than a coloured solution.",
           "The change is clear and is used as a test for the gas."],
     "y": "{formula('Pb(NO3)2')} + {formula('H2S')} → {formula('PbS')} + {2}{formula('HNO3')}: lead sulphide is black."},
    {"q": "Which test paper shows that a gas is hydrogen sulphide?", "r": "Filter paper moistened with lead(II) ethanoate, which turns black",
     "w": ["Damp red litmus paper, which turns blue", "Starch iodide paper, which turns blue",
           "Filter paper moistened with limewater, which turns milky"],
     "e": ["{formula('H2S')} is acidic, so it turns BLUE litmus red, and that is not a specific test.",
           "Starch iodide paper is used for chlorine and other oxidising gases.",
           "Limewater is the test for carbon dioxide."],
     "y": "Lead(II) ethanoate paper turning black shows the black lead sulphide."},
    {"q": "Hydrogen sulphide is bubbled into a solution of sulphur dioxide. What is seen, and which gas is oxidised?",
     "r": "A yellow deposit of sulphur; the hydrogen sulphide is oxidised",
     "w": ["A yellow deposit; the sulphur dioxide is oxidised", "A white precipitate; neither is oxidised",
           "No change; the two gases do not react"],
     "e": ["{formula('SO2')} is the oxidising agent here, so it is REDUCED, not oxidised.",
           "A yellow solid, not a white one, is formed, and a redox reaction does take place.",
           "The two react readily and the sulphur formed is easy to see."],
     "y": "{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}: {formula('H2S')} loses hydrogen, so it is oxidised."},
]

L.lesson(D, S, 6, ("k4-6", "Describe the chemical properties of hydrogen sulphide"), [5],
  "Hydrogen sulphide is a weak acid, a reducing agent and it burns in air.\n"
  "• Weak acid: its solution turns blue litmus red. With alkalis it gives sulphides: H2S + 2NaOH → Na2S + 2H2O.\n"
  "• Burning: in plenty of air, 2H2S + 3O2 → 2SO2 + 2H2O (blue flame). In a limited supply, 2H2S + O2 → 2S + 2H2O, "
  "leaving a yellow deposit.\n"
  "• Reducing agent: it is oxidised to sulphur by many oxidising agents. With acidified potassium manganate(VII) the purple "
  "colour goes and sulphur appears; with chlorine water the colour goes; with sulphur dioxide: SO2 + 2H2S → 3S + 2H2O.\n"
  "• With metal salts it gives coloured sulphide precipitates, used in analysis: lead(II) nitrate gives black PbS. "
  "Lead(II) ethanoate paper turning black is the test for the gas.",
  worked({"z": 1},
         "Explain, with equations, what happens when hydrogen sulphide burns in plenty of air and in a limited supply of air.",
         ["In plenty of air there is enough oxygen to oxidise both the hydrogen and the sulphur.",
          "{2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}, with a blue flame.",
          "In a limited supply there is only enough oxygen for the hydrogen.",
          "{2}{formula('H2S')} + {formula('O2')} → {2}S + {2}{formula('H2O')}, leaving a yellow deposit of sulphur."],
         "plenty of air gives {formula('SO2')} and water; limited air gives sulphur and water",
         checks=[]),
  [card("c4k6-1", "{formula('H2S')} burns: plenty of air gives {formula('SO2')}; limited air gives sulphur.",
        ["{2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}"], "k4-6-chem"),
   card("c4k6-2", "{formula('H2S')} is a reducing agent: it is oxidised to sulphur, seen as a yellow deposit.",
        ["{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}"], "k4-6-reduce"),
   card("c4k6-3", "With metal salts, {formula('H2S')} gives coloured sulphides; lead(II) ethanoate paper turns black.",
        ["{formula('Pb(NO3)2')} + {formula('H2S')} → {formula('PbS')} + {2}{formula('HNO3')}"], "k4-6-test")],
  [bank("k4-6-chem", 1, "{X.q}", H2SCHEM, SRC),
   mcq("k4-6-reduce", 2, "Hydrogen sulphide is bubbled through {T.n}. What is seen?",
       "{T.r}", [("{T.w1}", "w1"), ("{T.w2}", "w2"), ("{T.w3}", "w3")],
       ["{T.y}", "So the answer is: {answer}."],
       vars={"T": {"pick": [
           {"n": "acidified potassium manganate(VII) solution", "r": "The purple colour disappears and a yellow deposit of sulphur appears",
            "w1": "The solution turns a deeper purple", "w2": "A black precipitate forms", "w3": "Nothing is seen",
            "y": "{formula('H2S')} is a reducing agent: the manganate(VII) is reduced and the {formula('H2S')} is oxidised to sulphur."},
           {"n": "chlorine water", "r": "The colour of the chlorine water disappears and a yellow deposit forms",
            "w1": "The solution turns green", "w2": "A white precipitate forms", "w3": "The gas is unchanged",
            "y": "Chlorine oxidises the {formula('H2S')} to sulphur and is itself reduced to chloride ions."},
           {"n": "lead(II) nitrate solution", "r": "A black precipitate of lead(II) sulphide forms",
            "w1": "A white precipitate forms", "w2": "A yellow solution forms", "w3": "Bubbles of gas are given off",
            "y": "{formula('Pb(NO3)2')} + {formula('H2S')} → {formula('PbS')} + {2}{formula('HNO3')}, and {formula('PbS')} is black."},
           {"n": "a solution of sulphur dioxide", "r": "A pale yellow deposit of sulphur appears",
            "w1": "The mixture turns purple", "w2": "A black precipitate forms", "w3": "Nothing is seen",
            "y": "{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}: here {formula('SO2')} is the oxidising agent."}]}},
       misc=[("w1", "{T.y}"), ("w2", "{T.y}"), ("w3", "{T.y}")],
       sources=SRC),
   num("k4-6-sulphur", 2, "When {n} mol of sulphur dioxide reacts completely with hydrogen sulphide, how many moles of sulphur are formed?",
       "3 * n",
       ["{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}.",
        "{1} mol of {formula('SO2')} gives {3} mol of sulphur.", "{n} mol gives {3} × {n} = {answer} mol."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 1.5, 2]}},
       misc=[("same", "n", "Read the balanced equation: {1} mol of {formula('SO2')} gives {3} mol of sulphur."),
             ("two", "2 * n", "{2} is the coefficient of {formula('H2S')}, not of the sulphur.")],
       sources=SRC, unit="mol"),
   mcq("k4-6-test", 2, "Which observation shows that a gas is hydrogen sulphide?",
       "{A.r}", [("{A.w1}", "w1"), ("{A.w2}", "w2"), ("{A.w3}", "w3")],
       ["{A.y}", "So the answer is: {answer}."],
       vars={"A": {"pick": [
           {"r": "Damp lead(II) ethanoate paper turns black", "w1": "Damp red litmus paper turns blue",
            "w2": "Limewater turns milky", "w3": "A glowing splint relights",
            "y": "The black colour is lead(II) sulphide, formed from the gas."},
           {"r": "It smells of rotten eggs and turns damp blue litmus red", "w1": "It smells sweet and turns red litmus blue",
            "w2": "It has no smell and relights a splint", "w3": "It is brown and turns starch iodide paper blue",
            "y": "{formula('H2S')} is acidic in water as well as having its characteristic smell."},
           {"r": "Passed into lead(II) nitrate solution, it gives a black precipitate",
            "w1": "Passed into limewater, it gives a white precipitate", "w2": "Passed into silver nitrate, it gives no change",
            "w3": "Passed into water, it turns the water brown",
            "y": "Black {formula('PbS')} is the sign of hydrogen sulphide in the gas."}]}},
       misc=[("w1", "{A.y}"), ("w2", "{A.y}"), ("w3", "{A.y}")],
       sources=SRC),
   num("k4-6-mass", 3, "What mass of sulphur, in grams, is formed when {n} mol of hydrogen sulphide reacts completely with sulphur dioxide?",
       "roundTo(massOf(1.5 * n, 'S'), 0.01)",
       ["{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}.",
        "{2} mol of {formula('H2S')} gives {3} mol of S, so {n} mol gives {1.5} × {n} = {1.5 * n} mol.",
        "Mass = moles × {ram('S')} = {1.5 * n} × {ram('S')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.4, 0.5, 1, 2]}},
       misc=[("same", "massOf(n, 'S')", "The ratio is {3} mol of sulphur for every {2} mol of {formula('H2S')}."),
             ("three", "massOf(3 * n, 'S')", "{3} mol of sulphur comes from {2} mol of {formula('H2S')}, not from {1}.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("describe hydrogen sulphide as a weak acid, a reducing agent and a gas that burns, and give the test for it.",
          "Lesson {5} (preparing {formula('H2S')}) and Lesson {4} (redox reactions of {formula('SO2')}).",
          "Lesson {7} (the sulphides themselves) and the use of {formula('H2S')} in analysis."),
     ("Burning and acidity",
      "Hydrogen sulphide burns in air with a blue flame, and what it gives depends on how much oxygen it has.\n"
      "• Plenty of air: {2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}.\n"
      "• Limited air: {2}{formula('H2S')} + {formula('O2')} → {2}S + {2}{formula('H2O')}, leaving a yellow deposit.\n"
      "In water it is a weak acid: the solution turns blue litmus red, and with sodium hydroxide it gives a sulphide:\n"
      "{formula('H2S')} + {2}{formula('NaOH')} → {formula('Na2S')} + {2}{formula('H2O')}."),
     ("A reducing agent, and the test",
      "Hydrogen sulphide gives up hydrogen easily, so it is a good reducing agent. It is itself oxidised to sulphur, "
      "which appears as a pale yellow deposit:\n"
      "• acidified potassium manganate(VII): purple → colourless, with sulphur;\n"
      "• chlorine water: the colour goes, with sulphur;\n"
      "• sulphur dioxide: {formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}. Here {formula('SO2')} is the oxidising agent.\n"
      "With solutions of metal salts it gives sulphides of different colours, which is why it is used in analysis:\n"
      "{formula('Pb(NO3)2')} + {formula('H2S')} → {formula('PbS')} + {2}{formula('HNO3')}, a BLACK precipitate.\n"
      "The test for the gas is damp lead(II) ethanoate paper, which turns black.")],
    key_words=[("weak acid", "an acid only slightly split into ions in water"),
               ("reducing agent", "a substance that gives electrons or hydrogen to another"),
               ("precipitate", "an insoluble solid formed when two solutions are mixed"),
               ("lead(II) ethanoate paper", "test paper that turns black with hydrogen sulphide")],
    examples=["{2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}", "{formula('PbS')}: black", "sulphur: a pale yellow deposit"],
    mistake=("hydrogen sulphide burning in limited air gives sulphur dioxide", "it gives sulphur",
             "With too little oxygen, only the hydrogen is oxidised, leaving the sulphur behind.")))

# ---------------------------------------------------------------- 7. Sulphides of sodium and iron
SULPHIDES = [
    {"q": "How is iron(II) sulphide prepared in the laboratory?", "r": "By heating a mixture of iron filings and sulphur",
     "w": ["By adding iron filings to dilute sulphuric acid", "By burning iron in air",
           "By adding iron filings to water containing sulphur"],
     "e": ["Iron with dilute sulphuric acid gives iron(II) sulphate and hydrogen.",
           "Burning iron in air gives an oxide, not a sulphide.",
           "Sulphur is insoluble in water, and no reaction takes place in the cold."],
     "y": "Fe + S → {formula('FeS')}: once started, the mixture glows and keeps reacting by itself."},
    {"q": "What is seen when a mixture of iron filings and sulphur is heated strongly?", "r": "The mixture glows red and keeps reacting without more heating",
     "w": ["The mixture melts and runs like a liquid", "A brown gas is given off", "Nothing happens until acid is added"],
     "e": ["The product is a solid that does not melt at that temperature.",
           "No brown gas is formed; the product is a black solid.",
           "The reaction starts with heat alone."],
     "y": "The reaction gives out heat, so it continues on its own once it has started."},
    {"q": "How can iron(II) sulphide be told from a mixture of iron and sulphur?", "r": "A magnet picks iron out of the mixture but not out of the compound",
     "w": ["The compound is yellow and the mixture is black", "Both behave in exactly the same way",
           "Only the compound can be seen with a hand lens"],
     "e": ["It is the other way round in colour terms: the compound is black and the mixture shows yellow specks.",
           "A compound has properties of its own, different from those of its elements.",
           "Both can be seen; the difference is in their properties."],
     "y": "In a mixture the elements keep their own properties, so the iron is still magnetic."},
    {"q": "What happens when dilute hydrochloric acid is added to iron(II) sulphide?", "r": "Hydrogen sulphide is given off",
     "w": ["Hydrogen is given off", "Sulphur dioxide is given off", "Nothing happens"],
     "e": ["Hydrogen comes from a metal with an acid, not from a sulphide.",
           "Sulphur dioxide comes from a sulphite with an acid.",
           "The reaction is the standard way of making {formula('H2S')}."],
     "y": "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}."},
    {"q": "Which statement about sodium sulphide is correct?", "r": "It is soluble in water and its solution is alkaline",
     "w": ["It is insoluble in water", "Its solution is strongly acidic", "It is a yellow gas"],
     "e": ["Sodium compounds are generally soluble, and sodium sulphide is no exception.",
           "The solution of a salt of a strong base and a weak acid is alkaline, not acidic.",
           "It is a solid, not a gas."],
     "y": "{formula('Na2S')} dissolves and its solution is alkaline because the sulphide ion reacts with water."},
    {"q": "Why is iron(II) sulphide used, rather than sodium sulphide, to make hydrogen sulphide in the laboratory?",
     "r": "It is a solid that reacts steadily with dilute acid, so the flow of gas is easy to control",
     "w": ["Sodium sulphide gives a different gas", "Iron(II) sulphide is the only sulphide that exists",
           "Sodium sulphide does not react with acids"],
     "e": ["Both give hydrogen sulphide with an acid.",
           "Many metal sulphides exist, such as {formula('Na2S')}, {formula('ZnS')} and {formula('PbS')}.",
           "Sodium sulphide does react, and very readily."],
     "y": "Lumps of {formula('FeS')} react at a steady rate, while the very soluble {formula('Na2S')} would react too fast."},
]

L.lesson(D, S, 7, ("k4-7", "Prepare the sulphides of sodium and iron and describe their properties"), [6],
  "A sulphide is a compound of a metal with sulphur.\n"
  "Iron(II) sulphide: heat a mixture of iron filings and sulphur. Fe + S → FeS. The mixture glows and goes on reacting "
  "without more heating, because the reaction gives out heat. The product is a black solid.\n"
  "Sodium sulphide: made by heating sodium with sulphur, or by reducing sodium sulphate with carbon. It is a solid that "
  "dissolves easily in water to give an alkaline solution.\n"
  "A compound is not a mixture: a magnet picks iron out of a MIXTURE of iron and sulphur, but not out of FeS; "
  "the mixture shows yellow specks, while FeS is uniformly black.\n"
  "Both sulphides give hydrogen sulphide with a dilute acid: FeS + 2HCl → FeCl2 + H2S.",
  worked({"z": 1},
         "Give two ways of showing that the black solid made by heating iron and sulphur is a compound, not a mixture.",
         ["Hold a magnet near it: a mixture gives up its iron filings to the magnet, but the compound does not.",
          "Look at it closely: a mixture shows yellow specks of sulphur among grey iron, but the compound is uniformly black.",
          "Add dilute hydrochloric acid: the mixture gives hydrogen (odourless), the compound gives hydrogen sulphide (rotten eggs).",
          "In a compound the elements have lost their own properties."],
         "a magnet no longer picks out iron, and the solid is uniformly black",
         checks=[]),
  [card("c4k7-1", "Fe + S → {formula('FeS')}: heating starts the reaction, which then continues on its own.",
        ["the mixture glows red without more heating"], "k4-7-make"),
   card("c4k7-2", "A compound is not a mixture: {formula('FeS')} is not magnetic and is uniformly black.",
        ["a magnet picks iron out of the mixture only"], "k4-7-tell"),
   card("c4k7-3", "A sulphide with a dilute acid gives hydrogen sulphide.",
        ["{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}"], "k4-7-acid")],
  [bank("k4-7-make", 1, "{X.q}", SULPHIDES, SRC),
   mcq("k4-7-tell", 1, "How can you tell iron(II) sulphide from a mixture of iron and sulphur by {M.q}?",
       "{M.r}", [("{M.w1}", "w1"), ("{M.w2}", "w2"), ("{M.w3}", "w3")],
       ["{M.y}", "So the answer is: {answer}."],
       vars={"M": {"pick": [
           {"q": "using a magnet", "r": "A magnet picks iron out of the mixture, but takes nothing from the compound",
            "w1": "A magnet picks iron out of both", "w2": "A magnet picks iron out of the compound only",
            "w3": "A magnet has no effect on either", "y": "In a mixture each element keeps its own properties, so the iron is still magnetic."},
           {"q": "looking at them", "r": "The mixture shows yellow specks among grey, while the compound is uniformly black",
            "w1": "Both are uniformly black", "w2": "The compound shows yellow specks", "w3": "Both show yellow specks",
            "y": "The compound is a new substance with its own appearance."},
           {"q": "adding dilute hydrochloric acid", "r": "The mixture gives an odourless gas, the compound a gas smelling of rotten eggs",
            "w1": "Both give an odourless gas", "w2": "Both give a gas smelling of rotten eggs", "w3": "Neither reacts with the acid",
            "y": "The iron in a mixture gives hydrogen; the compound gives hydrogen sulphide."}]}},
       misc=[("w1", "{M.y}"), ("w2", "{M.y}"), ("w3", "{M.y}")],
       sources=SRC),
   num("k4-7-ratio", 2, "What mass of sulphur, in grams, combines exactly with {m} g of iron to make iron(II) sulphide?",
       "roundTo(m * ram('S') / ram('Fe'), 0.01)",
       ["Fe + S → {formula('FeS')}: {1} mol of iron needs {1} mol of sulphur.",
        "{m} g of iron is {m} ÷ {ram('Fe')} = {roundTo(m / ram('Fe'), 0.001)} mol.",
        "That needs the same number of moles of sulphur: {roundTo(m / ram('Fe'), 0.001)} × {ram('S')} = {answer} g."],
       vars={"m": {"pick": [5.6, 11.2, 14, 22.4, 28, 56]}},
       misc=[("same", "m", "Equal moles do not mean equal masses: iron and sulphur have different relative atomic masses."),
             ("swap", "roundTo(m * ram('Fe') / ram('S'), 0.01)", "Divide by the relative atomic mass of IRON and multiply by that of sulphur.")],
       sources=SRC, unit="g"),
   mcq("k4-7-acid", 2, "Dilute hydrochloric acid is added to {C.n}. What gas is given off?",
       "{C.r}", [("{C.w1}", "w1"), ("{C.w2}", "w2"), ("{C.w3}", "w3")],
       ["{C.y}", "So the answer is: {answer}."],
       vars={"C": {"pick": [
           {"n": "iron(II) sulphide", "r": "Hydrogen sulphide, which smells of rotten eggs",
            "w1": "Hydrogen", "w2": "Sulphur dioxide", "w3": "Carbon dioxide",
            "y": "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}."},
           {"n": "sodium sulphite", "r": "Sulphur dioxide, which has a sharp choking smell",
            "w1": "Hydrogen sulphide", "w2": "Hydrogen", "w3": "Oxygen",
            "y": "A sulphITE gives {formula('SO2')}; a sulphIDE gives {formula('H2S')}."},
           {"n": "iron filings", "r": "Hydrogen, which is odourless and pops with a lighted splint",
            "w1": "Hydrogen sulphide", "w2": "Sulphur dioxide", "w3": "No gas at all",
            "y": "A metal above hydrogen in the reactivity series gives hydrogen with a dilute acid."},
           {"n": "sodium carbonate", "r": "Carbon dioxide, which turns limewater milky",
            "w1": "Hydrogen sulphide", "w2": "Sulphur dioxide", "w3": "Hydrogen",
            "y": "A carbonate with an acid always gives carbon dioxide."}]}},
       misc=[("w1", "{C.y}"), ("w2", "{C.y}"), ("w3", "{C.y}")],
       sources=SRC),
   num("k4-7-mass", 3, "What mass of iron(II) sulphide, in grams, is made when {m} g of iron combines completely with sulphur?",
       "roundTo(m * molarMass('FeS') / ram('Fe'), 0.01)",
       ["{m} g of iron is {roundTo(m / ram('Fe'), 0.001)} mol.",
        "Fe + S → {formula('FeS')}, so the same number of moles of {formula('FeS')} is made.",
        "The relative formula mass of {formula('FeS')} is {molarMass('FeS')}, so the mass is {roundTo(m / ram('Fe'), 0.001)} × {molarMass('FeS')} = {answer} g."],
       vars={"m": {"pick": [5.6, 11.2, 14, 22.4, 28, 56]}},
       misc=[("same", "m", "The sulphur adds to the mass: the product is heavier than the iron alone."),
             ("sulphur", "roundTo(m * ram('S') / ram('Fe'), 0.01)", "That is the mass of SULPHUR needed; the question asks for the mass of {formula('FeS')}.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("prepare the sulphides of iron and sodium, tell a compound from a mixture, and work out the masses that combine.",
          "Lesson {6} (hydrogen sulphide) and Form One compounds and mixtures.",
          "Lesson {8} (sulphuric acid) and the mole calculations of the third chapter."),
     ("Making the sulphides",
      "Iron(II) sulphide: mix iron filings with powdered sulphur and heat one spot strongly. The mixture begins to glow "
      "red and goes on reacting without further heating, because the reaction gives out heat:\n"
      "Fe + S → {formula('FeS')}\n"
      "The product is a black solid.\n"
      "Sodium sulphide: made by heating sodium with sulphur, or in industry by reducing sodium sulphate with carbon. "
      "It is a solid that dissolves readily in water, giving an alkaline solution.\n"
      "Both sulphides give hydrogen sulphide with a dilute acid, which is how the gas is prepared."),
     ("Compound against mixture",
      "A mixture of iron and sulphur and the compound {formula('FeS')} look different and behave differently:\n"
      "• a magnet picks the iron out of the MIXTURE, but takes nothing from the compound;\n"
      "• the mixture shows yellow specks among grey, while the compound is uniformly black;\n"
      "• dilute acid gives odourless hydrogen from the mixture, but hydrogen sulphide from the compound;\n"
      "• a mixture can hold any proportions, but {formula('FeS')} always has {56} parts of iron to {32} of sulphur by mass.\n"
      "In a compound the elements have joined chemically and lost their own properties.")],
    key_words=[("sulphide", "a compound of a metal with sulphur"),
               ("mixture", "substances together but not chemically joined"),
               ("exothermic", "giving out heat, as the iron and sulphur reaction does"),
               ("fixed proportions", "the fixed ratio by mass in which elements combine in a compound")],
    examples=["Fe + S → {formula('FeS')}", "{formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}", "{56} g of Fe needs {32} g of S"],
    mistake=("a magnet separates iron from iron(II) sulphide", "a magnet separates iron from a MIXTURE of iron and sulphur only",
             "In the compound the iron is chemically joined and the solid is not magnetic.")))

# ---------------------------------------------------------------- 8. Chemical properties of sulphuric acid
H2SO4 = [
    {"q": "Dilute sulphuric acid is added to zinc. What is seen?", "r": "Bubbles of hydrogen, which pop with a lighted splint",
     "w": ["Bubbles of sulphur dioxide", "A yellow deposit of sulphur", "No reaction"],
     "e": ["Sulphur dioxide comes from the CONCENTRATED acid with copper, not from the dilute acid with zinc.",
           "Sulphur is not formed with the dilute acid.",
           "Zinc is above hydrogen in the reactivity series, so it does react."],
     "y": "Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}: the dilute acid behaves as an ordinary acid."},
    {"q": "Dilute sulphuric acid is added to sodium carbonate. What gas is given off?", "r": "Carbon dioxide",
     "w": ["Hydrogen", "Sulphur dioxide", "Hydrogen sulphide"],
     "e": ["Hydrogen comes from a metal with an acid, not from a carbonate.",
           "Sulphur dioxide comes from a sulphite, not from a carbonate.",
           "Hydrogen sulphide comes from a sulphide."],
     "y": "{formula('Na2CO3')} + {formula('H2SO4')} → {formula('Na2SO4')} + {formula('H2O')} + {formula('CO2')}."},
    {"q": "Concentrated sulphuric acid is poured onto sugar. What is seen?", "r": "The sugar turns black and a spongy mass of carbon rises out of the beaker",
     "w": ["The sugar dissolves to give a clear solution", "The sugar turns bright yellow",
           "Nothing happens until the mixture is heated"],
     "e": ["The sugar is not simply dissolved; it is chemically changed.",
           "The colour is black, from the carbon left behind.",
           "The change starts at once, and heat is given out."],
     "y": "The acid removes hydrogen and oxygen from the sugar as water, leaving carbon: it is a dehydrating agent."},
    {"q": "Copper is warmed with concentrated sulphuric acid. What gas is given off?", "r": "Sulphur dioxide",
     "w": ["Hydrogen", "Hydrogen sulphide", "Oxygen"],
     "e": ["Copper is below hydrogen in the reactivity series, so it cannot displace hydrogen.",
           "Hydrogen sulphide comes from a sulphide with a dilute acid.",
           "No oxygen is given off in this reaction."],
     "y": "Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}: here the acid is an oxidising agent."},
    {"q": "Concentrated sulphuric acid is warmed with sodium chloride. What is given off, and why?",
     "r": "Hydrogen chloride, because the acid is less volatile and displaces the more volatile acid",
     "w": ["Chlorine, because the acid is an oxidising agent", "Hydrogen, because sodium is a reactive metal",
           "Nothing: the two do not react"],
     "e": ["Chlorine needs a stronger oxidising agent, such as manganese(IV) oxide with concentrated hydrochloric acid.",
           "The sodium is already combined as a salt, so it cannot displace hydrogen.",
           "The reaction is the standard preparation of hydrogen chloride."],
     "y": "{formula('NaCl')} + {formula('H2SO4')} → {formula('NaHSO4')} + {formula('HCl')}: a less volatile acid drives out a more volatile one."},
    {"q": "Why must concentrated sulphuric acid be added to water, and never water to the acid?",
     "r": "Mixing gives out a great deal of heat, and water poured onto the acid can boil and spit acid out",
     "w": ["The acid would become too weak", "Water would react chemically with the acid to give hydrogen",
           "The order makes no difference"],
     "e": ["Diluting always lowers the concentration; that is not the danger.",
           "No hydrogen is given off; the danger is heat.",
           "The order matters a great deal for safety."],
     "y": "Adding acid slowly to a large volume of water lets the heat spread out safely."},
]

L.lesson(D, S, 8, ("k4-8", "Describe the chemical properties of sulphuric acid"), [4],
  "Dilute sulphuric acid behaves as a typical strong acid:\n"
  "• with a metal above hydrogen: Zn + H2SO4 → ZnSO4 + H2;\n"
  "• with a base or basic oxide: CuO + H2SO4 → CuSO4 + H2O;\n"
  "• with a carbonate: Na2CO3 + H2SO4 → Na2SO4 + H2O + CO2.\n"
  "Concentrated sulphuric acid has three further properties:\n"
  "• Dehydrating agent: it removes hydrogen and oxygen as water. Sugar turns to a black spongy mass of carbon; "
  "blue copper(II) sulphate crystals turn white.\n"
  "• Oxidising agent when hot: Cu + 2H2SO4 → CuSO4 + SO2 + 2H2O.\n"
  "• A less volatile acid: it displaces more volatile acids from their salts. NaCl + H2SO4 → NaHSO4 + HCl.\n"
  "Safety: always add the acid to water, never water to the acid, because a great deal of heat is given out.",
  worked({"z": 1},
         "Explain what is seen when concentrated sulphuric acid is poured onto blue copper(II) sulphate crystals, and name the property shown.",
         ["Blue copper(II) sulphate crystals contain water of crystallisation.",
          "Concentrated sulphuric acid takes up water very strongly.",
          "It removes the water from the crystals, and the solid turns white.",
          "Removing water from a substance is dehydration, so the acid is acting as a dehydrating agent."],
         "the blue crystals turn white; the acid is acting as a dehydrating agent",
         checks=[]),
  [card("c4k8-1", "Dilute sulphuric acid is a typical acid: metal → hydrogen, base → salt and water, carbonate → carbon dioxide.",
        ["Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}"], "k4-8-chem"),
   card("c4k8-2", "Concentrated sulphuric acid is a dehydrating agent: it removes water from other substances.",
        ["sugar turns to a black mass of carbon"], "k4-8-dehydrate"),
   card("c4k8-3", "Hot concentrated sulphuric acid is an oxidising agent, and it displaces more volatile acids.",
        ["Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}"], "k4-8-conc")],
  [bank("k4-8-chem", 1, "{X.q}", H2SO4, SRC),
   mcq("k4-8-dehydrate", 2, "Concentrated sulphuric acid is added to {D.n}. What is seen?",
       "{D.r}", [("{D.w1}", "w1"), ("{D.w2}", "w2"), ("{D.w3}", "w3")],
       ["{D.y}", "So the answer is: {answer}."],
       vars={"D": {"pick": [
           {"n": "sugar in a beaker", "r": "The sugar turns black and a spongy column of carbon rises",
            "w1": "The sugar dissolves to a clear solution", "w2": "The sugar turns bright yellow", "w3": "Nothing happens",
            "y": "The acid removes hydrogen and oxygen as water, leaving the carbon behind."},
           {"n": "blue copper(II) sulphate crystals", "r": "The blue crystals turn white",
            "w1": "The crystals turn black", "w2": "The crystals turn green", "w3": "The crystals dissolve to a blue solution",
            "y": "The acid takes the water of crystallisation out of the blue crystals, leaving the white anhydrous salt."},
           {"n": "a piece of wood or paper", "r": "It is charred and turns black",
            "w1": "It turns white", "w2": "It dissolves completely", "w3": "It is unchanged",
            "y": "Wood and paper contain hydrogen and oxygen, which the acid removes as water, leaving carbon."}]}},
       misc=[("w1", "{D.y}"), ("w2", "{D.y}"), ("w3", "{D.y}")],
       sources=SRC),
   num("k4-8-mass", 2, "What mass of {formula('H2SO4')}, in grams, is there in {n} mol of the acid?",
       "massOf(n, 'H2SO4')",
       ["The relative molecular mass of {formula('H2SO4')} is {molarMass('H2SO4')}.",
        "Mass = moles × molar mass = {n} × {molarMass('H2SO4')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 2.5]}},
       misc=[("div", "roundTo(n / molarMass('H2SO4'), 0.0001)", "Mass = moles × molar mass."),
             ("so3", "massOf(n, 'SO3')", "Use the formula {formula('H2SO4')}, which includes the {2} hydrogen atoms.")],
       sources=SRC, unit="g"),
   mcq("k4-8-conc", 2, "Which property of concentrated sulphuric acid is shown by {P.n}?",
       "{P.r}", [("{P.w1}", "w1"), ("{P.w2}", "w2"), ("{P.w3}", "w3")],
       ["{P.y}", "So the answer is: {answer}."],
       vars={"P": {"pick": [
           {"n": "sugar turning into a black spongy mass", "r": "It is a dehydrating agent",
            "w1": "It is an oxidising agent", "w2": "It is a reducing agent", "w3": "It is a volatile acid",
            "y": "Hydrogen and oxygen are removed from the sugar as water, leaving carbon."},
           {"n": "copper giving sulphur dioxide when warmed with the acid", "r": "It is an oxidising agent",
            "w1": "It is a dehydrating agent", "w2": "It is a reducing agent", "w3": "It is a drying agent",
            "y": "The copper is oxidised to copper(II) sulphate while the acid is reduced to {formula('SO2')}."},
           {"n": "hydrogen chloride given off when the acid is warmed with sodium chloride", "r": "It is a less volatile acid than hydrochloric acid",
            "w1": "It is an oxidising agent", "w2": "It is a dehydrating agent", "w3": "It is a weak acid",
            "y": "A less volatile acid drives a more volatile acid out of its salt on heating."},
           {"n": "a gas being dried by bubbling it through the acid", "r": "It is a drying agent",
            "w1": "It is an oxidising agent", "w2": "It is a reducing agent", "w3": "It is a weak acid",
            "y": "The acid takes up water vapour strongly without reacting with the gas."}]}},
       misc=[("w1", "{P.y}"), ("w2", "{P.y}"), ("w3", "{P.y}")],
       sources=SRC),
   num("k4-8-vol", 3, "What volume of hydrogen, in dm³ at s.t.p., is given off when {n} mol of zinc reacts completely with dilute sulphuric acid?",
       "gasVolume(n)",
       ["Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}.",
        "{1} mol of zinc gives {1} mol of hydrogen, so {n} mol gives {n} mol.",
        "At s.t.p. that is {n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 1.5, 2]}},
       misc=[("double", "gasVolume(2 * n)", "The equation gives {1} mol of hydrogen for each {1} mol of zinc."),
             ("mass", "massOf(n, 'H2')", "The question asks for a VOLUME in dm³, not a mass in grams.")],
       sources=SRC, unit="dm³")],
  learn=learn(
    [goal("describe dilute sulphuric acid as a typical acid and concentrated sulphuric acid as a dehydrating, oxidising and less volatile acid.",
          "Lesson {4} ({formula('SO2')} and the acid made from it) and Form Three acids, bases and salts.",
          "Lesson {9} (the uses of sulphur and its compounds) and salt preparations."),
     ("The dilute acid",
      "Dilute sulphuric acid behaves as a typical strong acid. It turns blue litmus red and reacts in the usual three ways:\n"
      "• with a metal above hydrogen: Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')};\n"
      "• with a base or a basic oxide: {formula('CuO')} + {formula('H2SO4')} → {formula('CuSO4')} + {formula('H2O')};\n"
      "• with a carbonate: {formula('Na2CO3')} + {formula('H2SO4')} → {formula('Na2SO4')} + {formula('H2O')} + {formula('CO2')}.\n"
      "Its salts are sulphates. Lead and barium sulphates are insoluble, which is why barium chloride solution with dilute "
      "hydrochloric acid is the test for a sulphate."),
     ("The concentrated acid",
      "Concentrated sulphuric acid has three extra properties:\n"
      "• DEHYDRATING agent: it removes hydrogen and oxygen as water. Sugar becomes a black spongy mass of carbon; "
      "blue copper(II) sulphate crystals turn white; paper and wood char. It also dries gases that do not react with it.\n"
      "• OXIDISING agent when hot: Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}. "
      "Copper is below hydrogen, so it could not react with the dilute acid at all.\n"
      "• LESS VOLATILE acid: on heating it drives more volatile acids out of their salts: "
      "{formula('NaCl')} + {formula('H2SO4')} → {formula('NaHSO4')} + {formula('HCl')}.\n"
      "Safety: always add the acid slowly to water with stirring, never water to the acid, because a great deal of heat is given out.")],
    key_words=[("dehydrating agent", "a substance that removes hydrogen and oxygen as water"),
               ("oxidising agent", "a substance that gives oxygen to, or takes electrons from, another"),
               ("volatile", "easily turned into a vapour"),
               ("water of crystallisation", "water joined into a crystal, as in blue {formula('CuSO4')} crystals")],
    examples=["Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}", "sugar → black carbon", "Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}"],
    mistake=("copper reacts with dilute sulphuric acid to give hydrogen", "copper does not react with the dilute acid at all",
             "Copper is below hydrogen in the reactivity series. Only the hot CONCENTRATED acid attacks it, giving {formula('SO2')}.")))

# ---------------------------------------------------------------- 9. Uses of sulphur and its compounds
USES = [
    {"q": "What is the largest single use of sulphur?", "r": "Making sulphuric acid",
     "w": ["Making matches", "Vulcanising rubber", "Making fungicides"],
     "e": ["Matches use only a small amount of sulphur.",
           "Vulcanising is important but uses far less sulphur than the acid industry.",
           "Fungicides use a small amount compared with the acid industry."],
     "y": "Most mined sulphur is burned to {formula('SO2')} and turned into sulphuric acid by the Contact process."},
    {"q": "Why is sulphur added to rubber?", "r": "To vulcanise it, making it harder and more elastic",
     "w": ["To make it burn more easily", "To colour it yellow", "To make it dissolve in water"],
     "e": ["Rubber is not treated with sulphur in order to burn it.",
           "Vulcanised rubber is not yellow; the change is in its strength, not its colour.",
           "Rubber does not dissolve in water either before or after."],
     "y": "Sulphur links the rubber chains together, so the rubber keeps its shape and wears better in tyres."},
    {"q": "Which use depends on sulphur dioxide being a preservative?", "r": "Treating dried fruit and fruit juice so that they keep",
     "w": ["Filling a car battery", "Making fertiliser", "Vulcanising rubber"],
     "e": ["A car battery uses sulphuric ACID, not the gas as a preservative.",
           "Fertiliser is made with sulphuric acid, not with the gas as a preservative.",
           "Vulcanising uses the element sulphur."],
     "y": "{formula('SO2')} kills bacteria and moulds, so it is used in small amounts to preserve food and drink."},
    {"q": "Which of these is made using sulphuric acid?", "r": "Ammonium sulphate fertiliser",
     "w": ["Common salt from sea water", "Limestone for building", "Charcoal from wood"],
     "e": ["Salt is obtained by evaporating sea water; no acid is needed.",
           "Limestone is quarried, not made with acid.",
           "Charcoal is made by heating wood out of contact with air."],
     "y": "Ammonia is neutralised with sulphuric acid to give {formula('(NH4)2SO4')}, a widely used fertiliser."},
    {"q": "Why is sulphuric acid used in a car battery?", "r": "It is the electrolyte that lets the battery give a current",
     "w": ["It stops the battery from rusting", "It cools the battery", "It cleans the metal plates"],
     "e": ["Rusting is not what the acid is there to prevent.",
           "Cooling is not its purpose; batteries are cooled by air.",
           "The acid does not act as a cleaner; it carries the current as ions."],
     "y": "A lead-acid battery uses dilute sulphuric acid as its electrolyte."},
    {"q": "Which use of sulphur depends on its killing fungi?", "r": "Dusting crops to control mildew and other fungal diseases",
     "w": ["Making gunpowder", "Making matches", "Making sulphuric acid"],
     "e": ["Gunpowder uses sulphur because it burns, not because it kills fungi.",
           "Matches use sulphur because it catches fire easily.",
           "Making the acid depends on burning the sulphur."],
     "y": "Sulphur dust and lime-sulphur sprays are used as fungicides on crops."},
]

L.lesson(D, S, 9, ("k4-9", "State the uses of sulphur and its compounds"), [8],
  "Sulphur itself is used to:\n"
  "• make sulphuric acid, by far its largest use (the Contact process);\n"
  "• vulcanise rubber, linking the chains so that tyres are harder, stronger and more elastic;\n"
  "• make matches, gunpowder and fireworks, because it catches fire easily;\n"
  "• make fungicides, dusted or sprayed on crops;\n"
  "• make drugs and ointments for skin diseases.\n"
  "Sulphur dioxide is used to bleach wool, silk, straw and paper, to preserve dried fruit and fruit juice, and to make sulphuric acid.\n"
  "Sulphuric acid is used in fertilisers (ammonium sulphate), detergents, paints, dyes, plastics, car batteries, "
  "pickling steel before plating, and in refining petroleum. Because so many industries depend on it, the amount a country "
  "uses is a measure of how industrial it is.",
  worked({"z": 1},
         "Give three uses of sulphuric acid, with the industry for each.",
         ["Fertiliser: ammonia is neutralised with the acid to give ammonium sulphate.",
          "Batteries: dilute sulphuric acid is the electrolyte of a lead-acid car battery.",
          "Metals: the acid pickles steel, cleaning the surface before it is plated.",
          "Others include detergents, paints, dyes, plastics and refining petroleum."],
         "fertilisers, car batteries and pickling steel (among many others)",
         checks=[]),
  [card("c4k9-1", "The largest use of sulphur is making sulphuric acid.",
        ["sulphur → {formula('SO2')} → {formula('SO3')} → {formula('H2SO4')} in the Contact process"], "k4-9-uses"),
   card("c4k9-2", "Sulphur vulcanises rubber, making tyres harder and more elastic.",
        ["the sulphur links the rubber chains together"], "k4-9-match"),
   card("c4k9-3", "{formula('SO2')} preserves food and bleaches delicate materials.",
        ["dried fruit and fruit juice are treated with it"], "k4-9-which")],
  [bank("k4-9-uses", 1, "{X.q}", USES, SRC),
   match("k4-9-match", 2, "Match each substance to a use.",
         [("Sulphur", "Vulcanising rubber"), ("Sulphur dioxide", "Preserving dried fruit"),
          ("Sulphuric acid", "The electrolyte of a car battery"), ("Ammonium sulphate", "A nitrogen fertiliser"),
          ("Lime-sulphur spray", "Controlling fungal disease on crops")],
         pick=3, sources=SRC),
   mcq("k4-9-which", 2, "Which substance is used {U.q}?",
       "{U.r}", [("{U.w1}", "w1"), ("{U.w2}", "w2"), ("{U.w3}", "w3")],
       ["{U.y}", "So the answer is: {answer}."],
       vars={"U": {"pick": [
           {"q": "to preserve fruit juice", "r": "Sulphur dioxide", "w1": "Sulphuric acid", "w2": "Hydrogen sulphide",
            "w3": "Iron(II) sulphide", "y": "A little {formula('SO2')} kills the bacteria and moulds that spoil the juice."},
           {"q": "as the liquid inside a car battery", "r": "Dilute sulphuric acid", "w1": "Concentrated sulphuric acid",
            "w2": "Sulphur dioxide", "w3": "Sodium sulphide", "y": "A lead-acid battery uses dilute sulphuric acid as its electrolyte."},
           {"q": "to make tyres harder and more elastic", "r": "Sulphur", "w1": "Sulphur dioxide", "w2": "Sulphuric acid",
            "w3": "Hydrogen sulphide", "y": "Heating rubber with sulphur links its chains: this is vulcanising."},
           {"q": "to make the fertiliser ammonium sulphate", "r": "Sulphuric acid", "w1": "Hydrogen sulphide",
            "w2": "Sulphur dioxide", "w3": "Sodium sulphide", "y": "Ammonia is neutralised with sulphuric acid to give {formula('(NH4)2SO4')}."}]}},
       misc=[("w1", "{U.y}"), ("w2", "{U.y}"), ("w3", "{U.y}")],
       sources=SRC),
   num("k4-9-fert", 2, "What mass of sulphuric acid, in grams, is needed to make {n} mol of ammonium sulphate, {formula('(NH4)2SO4')}?",
       "massOf(n, 'H2SO4')",
       ["{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}: {1} mol of acid gives {1} mol of the fertiliser.",
        "The relative molecular mass of {formula('H2SO4')} is {molarMass('H2SO4')}.",
        "Mass = {n} × {molarMass('H2SO4')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.5, 1, 2, 2.5]}},
       misc=[("salt", "massOf(n, '(NH4)2SO4')", "The question asks for the mass of the ACID, not of the fertiliser."),
             ("double", "massOf(2 * n, 'H2SO4')", "{1} mol of acid is needed for {1} mol of ammonium sulphate, not {2}.")],
       sources=SRC, unit="g"),
   mcq("k4-9-why", 3, "Why is the amount of sulphuric acid a country uses taken as a measure of how industrial it is?",
       "{W.r}", [("{W.w1}", "w1"), ("{W.w2}", "w2"), ("{W.w3}", "w3")],
       ["{W.y}", "So the answer is: {answer}."],
       vars={"W": {"pick": [
           {"r": "It is used at some stage in a very wide range of industries, from fertilisers to metals and plastics",
            "w1": "It is the most expensive chemical made", "w2": "It is used only in the making of fertilisers",
            "w3": "It is the only acid that can be made in a factory",
            "y": "Because so many different industries need it, its use rises with industry as a whole."},
           {"r": "Fertilisers, detergents, paints, dyes, plastics, batteries and metal treatment all need it",
            "w1": "It is used only in car batteries", "w2": "It is the cheapest chemical to transport",
            "w3": "It cannot be imported, so every country must make its own",
            "y": "A long list of industries depend on it, so its use follows the size of the whole industrial base."},
           {"r": "Its use grows with the number of factories, not with the size of the population",
            "w1": "Its use grows with the population only", "w2": "Its use is fixed by law in every country",
            "w3": "It is used mainly in homes rather than in factories",
            "y": "It is an industrial chemical, so its use measures industry rather than the number of people."}]}},
       misc=[("w1", "{W.y}"), ("w2", "{W.y}"), ("w3", "{W.y}")],
       sources=SRC)],
  learn=learn(
    [goal("list the main uses of sulphur, sulphur dioxide and sulphuric acid, and say which property each use depends on.",
          "Lessons {2} to {8}, which give the properties behind each use.",
          "the nitrogen chapter, where fertilisers made with sulphuric acid appear again."),
     ("Sulphur and sulphur dioxide",
      "Sulphur itself is used to:\n"
      "• make sulphuric acid, by far its largest use;\n"
      "• vulcanise rubber: heating rubber with sulphur links its chains, so tyres are harder, stronger and more elastic;\n"
      "• make matches, gunpowder and fireworks, because it catches fire easily;\n"
      "• make fungicides, as dust or as a lime-sulphur spray on crops;\n"
      "• make ointments and drugs for skin diseases.\n"
      "Sulphur dioxide bleaches wool, silk, straw and paper, which chlorine would damage. It also preserves dried fruit "
      "and fruit juice, because it kills bacteria and moulds."),
     ("Sulphuric acid",
      "Sulphuric acid is one of the most important chemicals made. It is used:\n"
      "• to make fertilisers, especially ammonium sulphate from ammonia;\n"
      "• to make detergents, paints, dyes, plastics and fibres;\n"
      "• as the electrolyte in lead-acid car batteries;\n"
      "• to pickle steel, cleaning the surface before it is plated;\n"
      "• in refining petroleum.\n"
      "Because so many industries depend on it, the amount a country uses is often taken as a measure of how industrial it is. "
      "Care is still needed: the acid is corrosive, and sulphur dioxide escaping from factories causes acid rain.")],
    key_words=[("vulcanising", "heating rubber with sulphur to link its chains"),
               ("fungicide", "a substance that kills fungi such as mildew"),
               ("electrolyte", "a liquid that conducts electricity by its ions"),
               ("pickling", "cleaning a metal surface with acid before plating")],
    examples=["sulphur → sulphuric acid: the largest use", "{formula('SO2')}: preserving fruit juice", "{formula('H2SO4')}: car batteries"],
    mistake=("sulphur dioxide is used in car batteries", "dilute sulphuric acid is used in car batteries",
             "The battery needs an electrolyte, which is the acid, not the gas.")))
