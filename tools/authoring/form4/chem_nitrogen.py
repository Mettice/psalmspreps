"""Form 4 Chemistry, Term 1, rows 11-17: the chemistry of nitrogen. Row 18 is an integration activity, not a lesson.
The sheet's lesson numbers (10-16) differ from the row order; the app numbers by place in the year (TR-K4-2).
Run: python tools/authoring/form4/chem_nitrogen.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order, match
from common import goal, bank

L.use_class("form-4", "Form 4")
D, S = "chemistry", "chemistry"
SRC = ["nitrogen"]

# ---------------------------------------------------------------- 11. Occurrence and properties of nitrogen
NITRO = [
    {"q": "About what fraction of the air is nitrogen by volume?", "r": "About {78} per cent",
     "w": ["About {21} per cent", "About {50} per cent", "Less than {1} per cent"],
     "e": ["{21} per cent is the proportion of oxygen.",
           "Nitrogen is far more than half of the air.",
           "Less than {1} per cent covers argon, carbon dioxide and the rest together."],
     "y": "Air is about {78} per cent nitrogen, {21} per cent oxygen and {1} per cent other gases by volume."},
    {"q": "Why is nitrogen so unreactive?", "r": "Its two atoms are held by a strong triple bond that is hard to break",
     "w": ["Its atoms have a full outer shell already", "It is a noble gas", "Its molecules are very large"],
     "e": ["A nitrogen atom has {5} outer electrons, so it is not full; the molecule is stable because of the bond.",
           "Nitrogen is in group {5}, not group {0}; it is not a noble gas.",
           "The molecule is small; it is the strength of the bond that matters."],
     "y": "A great deal of energy is needed to break the N≡N triple bond, so nitrogen reacts only in hard conditions."},
    {"q": "How can nitrogen be obtained from air in the laboratory?", "r": "By passing air over heated copper to remove the oxygen, after removing carbon dioxide and water",
     "w": ["By burning the air", "By cooling air until the nitrogen freezes out",
           "By bubbling air through sodium hydroxide only"],
     "e": ["Air cannot be burned; something must be burned IN it.",
           "That is the industrial method (fractional distillation of liquid air), not the laboratory one.",
           "Sodium hydroxide removes carbon dioxide only, leaving the oxygen behind."],
     "y": "Heated copper takes the oxygen as copper(II) oxide, leaving nitrogen with a little argon."},
    {"q": "Nitrogen prepared from air is slightly denser than pure nitrogen. Why?", "r": "It still contains the noble gases, mainly argon, which are denser",
     "w": ["It contains some oxygen", "It contains water vapour", "Nitrogen from air has heavier atoms"],
     "e": ["The oxygen has been removed by the heated copper.",
           "The air is dried before the oxygen is removed.",
           "Atoms of nitrogen from air are the same as any other nitrogen atoms."],
     "y": "Argon and the other noble gases are not removed, and argon has a relative atomic mass of {40}."},
    {"q": "Magnesium burns in nitrogen. What is formed?", "r": "Magnesium nitride, {formula('Mg3N2')}",
     "w": ["Magnesium oxide", "Magnesium and nitrogen do not react", "Ammonia"],
     "e": ["Magnesium oxide needs oxygen, which is not present here.",
           "Magnesium is reactive enough to combine with nitrogen when it is burning.",
           "Ammonia needs hydrogen as well; it is not formed directly here."],
     "y": "{3}Mg + {formula('N2')} → {formula('Mg3N2')}: one of the few reactions of nitrogen at ordinary pressure."},
    {"q": "How is nitrogen obtained in industry?", "r": "By the fractional distillation of liquid air",
     "w": ["By heating nitrates", "From natural gas", "By passing air over heated copper"],
     "e": ["Heating nitrates gives oxygen and oxides of nitrogen, not pure nitrogen.",
           "Natural gas is mainly methane; it is a source of hydrogen, not nitrogen.",
           "That is the laboratory method and is far too slow for industry."],
     "y": "Air is liquefied and then distilled; nitrogen boils off first at −{196} °C, before oxygen at −{183} °C."},
]

L.lesson(D, S, 11, ("k4-11", "Describe the occurrence and properties of nitrogen"), [],
  "Nitrogen makes up about 78 per cent of the air by volume. It is also combined in proteins, in nitrates in the soil, "
  "and in ammonia.\n"
  "Laboratory preparation from air: remove carbon dioxide with sodium hydroxide, dry the air, then pass it over heated "
  "copper, which takes the oxygen. What is left is nitrogen with a little argon, so it is slightly denser than pure nitrogen.\n"
  "Pure nitrogen is made by heating ammonium nitrite: NH4NO2 → N2 + 2H2O.\n"
  "In industry it comes from the fractional distillation of liquid air.\n"
  "Properties: a colourless, odourless gas, almost insoluble in water, slightly less dense than air, and very unreactive "
  "because of the strong triple bond N≡N. It does not burn and does not support burning. "
  "It combines with magnesium (3Mg + N2 → Mg3N2), with hydrogen in the Haber process, and with oxygen in a lightning flash.",
  worked({"z": 1},
         "Explain why nitrogen obtained by removing oxygen from air is slightly denser than nitrogen made from ammonium nitrite.",
         ["Removing carbon dioxide, water and oxygen from air leaves nitrogen and the noble gases.",
          "The noble gases, mainly argon, are not removed by heated copper.",
          "Argon has a relative atomic mass of {40}, well above the {28} of a nitrogen molecule.",
          "So the mixture is a little denser than pure nitrogen."],
         "because it still contains argon, which is denser than nitrogen",
         checks=[]),
  [card("c4k11-1", "Air is about {78} per cent nitrogen by volume.",
        ["with about {21} per cent oxygen and {1} per cent other gases"], "k4-11-which"),
   card("c4k11-2", "Nitrogen is unreactive because of its strong triple bond.",
        ["N≡N needs a great deal of energy to break"], "k4-11-unreactive"),
   card("c4k11-3", "Heated copper removes oxygen from air, leaving nitrogen and argon.",
        ["{2}Cu + {formula('O2')} → {2}{formula('CuO')}"], "k4-11-prep")],
  [bank("k4-11-which", 1, "{X.q}", NITRO, SRC),
   num("k4-11-mass", 1, "Find the relative molecular mass of {formula(F)}.",
       "molarMass(F)",
       ["Add the relative atomic mass of every atom in the formula.", "The relative molecular mass of {formula(F)} is {answer}."],
       vars={"F": {"pick": ["N2", "NH3", "HNO3", "NO", "NO2", "N2O", "NH4NO3", "Mg3N2"]}},
       misc=[("atoms", "totalAtoms(F)", "{totalAtoms(F)} is the number of atoms, not the mass."),
             ("one", "ram(symbolsIn(F)[0])", "Include every atom in the formula.")],
       sources=SRC),
   mcq("k4-11-prep", 2, "In preparing nitrogen from air, what is the purpose of {P.n}?",
       "{P.r}", [("{P.w1}", "w1"), ("{P.w2}", "w2"), ("{P.w3}", "w3")],
       ["{P.y}", "So the answer is: {answer}."],
       vars={"P": {"pick": [
           {"n": "the sodium hydroxide solution", "r": "To remove the carbon dioxide from the air",
            "w1": "To remove the oxygen", "w2": "To dry the air", "w3": "To remove the argon",
            "y": "An alkali absorbs the acidic carbon dioxide."},
           {"n": "the concentrated sulphuric acid", "r": "To dry the air by removing water vapour",
            "w1": "To remove the oxygen", "w2": "To remove the carbon dioxide", "w3": "To react with the nitrogen",
            "y": "Concentrated sulphuric acid is a drying agent and does not react with nitrogen."},
           {"n": "the heated copper", "r": "To remove the oxygen, forming copper(II) oxide",
            "w1": "To remove the carbon dioxide", "w2": "To dry the gas", "w3": "To remove the argon",
            "y": "{2}Cu + {formula('O2')} → {2}{formula('CuO')}: the copper turns from pink-brown to black."},
           {"n": "heating ammonium nitrite instead", "r": "To obtain pure nitrogen, free of the noble gases",
            "w1": "To obtain oxygen", "w2": "To obtain ammonia", "w3": "To dry the nitrogen",
            "y": "{formula('NH4NO2')} → {formula('N2')} + {2}{formula('H2O')} gives nitrogen with no argon in it."}]}},
       misc=[("w1", "{P.y}"), ("w2", "{P.y}"), ("w3", "{P.y}")],
       sources=SRC),
   num("k4-11-vol", 2, "What volume of nitrogen, in dm³, is there in {v} dm³ of air? Take air as {78} per cent nitrogen by volume.",
       "roundTo(v * 78 / 100, 0.01)",
       ["{78} per cent of the air is nitrogen.", "{78} ÷ {100} × {v} = {answer} dm³."],
       vars={"v": {"pick": [50, 100, 200, 250, 400, 500, 1000]}},
       misc=[("oxygen", "roundTo(v * 21 / 100, 0.01)", "{21} per cent is the OXYGEN; nitrogen is {78} per cent."),
             ("whole", "v", "Only part of the air is nitrogen, not all of it.")],
       sources=SRC, unit="dm³"),
   mcq("k4-11-unreactive", 3, "Nitrogen is used to fill packets of crisps and to flush oil tanks. Which property does this use?",
       "{U.r}", [("{U.w1}", "w1"), ("{U.w2}", "w2"), ("{U.w3}", "w3")],
       ["{U.y}", "So the answer is: {answer}."],
       vars={"U": {"pick": [
           {"r": "It is unreactive, so it keeps oxygen away without attacking the contents",
            "w1": "It is poisonous, so it kills bacteria", "w2": "It is very soluble in fat", "w3": "It burns readily",
            "y": "The strong triple bond makes nitrogen almost inert at ordinary temperatures."},
           {"r": "It does not support burning, so a tank filled with it cannot catch fire",
            "w1": "It puts out fires by cooling them", "w2": "It reacts with petrol to make it safe", "w3": "It is denser than air, so it smothers a fire",
            "y": "Nitrogen neither burns nor lets anything else burn, so flushing a tank removes the danger."},
           {"r": "It is unreactive, so food does not go stale by being oxidised",
            "w1": "It dissolves the fat in food", "w2": "It freezes the food", "w3": "It makes the packet stronger",
            "y": "Replacing the air with nitrogen takes away the oxygen that makes fat go rancid."}]}},
       misc=[("w1", "{U.y}"), ("w2", "{U.y}"), ("w3", "{U.y}")],
       sources=SRC)],
  learn=learn(
    [goal("say where nitrogen is found, prepare it from air, and explain its properties from its triple bond.",
          "Form One the composition of air, and Form Three bonding.",
          "Lesson {12} (ammonia) and Lesson {16}, the nitrogen cycle."),
     ("Where nitrogen is found, and how it is obtained",
      "Nitrogen makes up about {78} per cent of the air by volume. It is also combined in the proteins of living things, "
      "in nitrates in the soil, and in ammonia.\n"
      "From air in the laboratory: pass air through sodium hydroxide solution to take out carbon dioxide, then through "
      "concentrated sulphuric acid to dry it, then over heated copper, which takes the oxygen:\n"
      "{2}Cu + {formula('O2')} → {2}{formula('CuO')}\n"
      "What is left is nitrogen with a little argon, so it is slightly DENSER than pure nitrogen.\n"
      "Pure nitrogen: heat ammonium nitrite, {formula('NH4NO2')} → {formula('N2')} + {2}{formula('H2O')}.\n"
      "In industry: fractional distillation of liquid air, where nitrogen boils off first."),
     ("Properties",
      "Nitrogen is a colourless, odourless gas, almost insoluble in water, and very slightly less dense than air "
      "(relative molecular mass {28} against about {29} for air).\n"
      "It is very unreactive. Its two atoms are joined by a TRIPLE bond, N≡N, which needs a great deal of energy to break. "
      "It does not burn and does not support burning.\n"
      "It does react in hard conditions:\n"
      "• with burning magnesium: {3}Mg + {formula('N2')} → {formula('Mg3N2')};\n"
      "• with hydrogen under pressure and a catalyst (the Haber process): {formula('N2')} + {3}{formula('H2')} → {2}{formula('NH3')};\n"
      "• with oxygen in a lightning flash or a hot engine: {formula('N2')} + {formula('O2')} → {2}{formula('NO')}.\n"
      "Being unreactive makes it useful: packets of food and oil tanks are filled with it to keep oxygen out.")],
    key_words=[("triple bond", "three shared pairs of electrons between two atoms"),
               ("inert", "very unreactive"),
               ("fractional distillation", "separating liquids by their different boiling points"),
               ("nitride", "a compound of a metal with nitrogen, such as {formula('Mg3N2')}")],
    examples=["air: about {78} per cent nitrogen", "{2}Cu + {formula('O2')} → {2}{formula('CuO')}", "{3}Mg + {formula('N2')} → {formula('Mg3N2')}"],
    mistake=("nitrogen is unreactive because its atoms have full outer shells", "it is unreactive because of the strong triple bond",
             "A nitrogen ATOM has {5} outer electrons. It is the N≡N bond in the molecule that is hard to break.")))

# ---------------------------------------------------------------- 12. Ammonia
AMM = [
    {"q": "Which reagents are used to prepare ammonia in the laboratory?", "r": "An ammonium salt and an alkali, heated: ammonium chloride with calcium hydroxide",
     "w": ["Ammonium chloride and dilute hydrochloric acid", "Nitrogen and water", "A nitrate and a dilute acid"],
     "e": ["An acid would give no ammonia; an ALKALI drives it out of an ammonium salt.",
           "Nitrogen and water do not react; the Haber process uses hydrogen, not water.",
           "A nitrate with a dilute acid gives no ammonia."],
     "y": "{2}{formula('NH4Cl')} + {formula('Ca(OH)2')} → {formula('CaCl2')} + {2}{formula('NH3')} + {2}{formula('H2O')}."},
    {"q": "How is ammonia collected?", "r": "By upward delivery, because it is less dense than air",
     "w": ["By downward delivery", "Over water", "Over mercury only"],
     "e": ["Its relative molecular mass is {17}, well below the average for air, so it rises.",
           "It is extremely soluble in water, so none would be collected.",
           "There is no need for mercury; an inverted jar works."],
     "y": "A gas less dense than air and very soluble is collected by upward delivery into an inverted jar."},
    {"q": "Which drying agent is used for ammonia?", "r": "Quicklime, {formula('CaO')}",
     "w": ["Concentrated sulphuric acid", "Phosphorus(V) oxide", "Anhydrous calcium chloride"],
     "e": ["Concentrated sulphuric acid is acidic and reacts with ammonia to give ammonium sulphate.",
           "Phosphorus(V) oxide is acidic and also reacts with ammonia.",
           "Anhydrous calcium chloride forms a compound with ammonia, so it cannot be used."],
     "y": "An alkaline gas must be dried with a basic drying agent, and quicklime is the usual choice."},
    {"q": "What is seen in the fountain experiment with ammonia?", "r": "Water rushes up into the flask as a fountain, turning red if litmus is present",
     "w": ["The water stays where it is", "The flask cracks", "The gas bubbles out through the water"],
     "e": ["The gas dissolves so fast that the pressure in the flask falls at once.",
           "No crack is needed; the pressure difference drives the fountain.",
           "The gas is taken INTO the water, not pushed out."],
     "y": "Ammonia is extremely soluble, so a drop of water lowers the pressure in the flask and the rest is pushed in."},
    {"q": "Ammonia gas meets hydrogen chloride gas. What is seen?", "r": "Dense white fumes of ammonium chloride",
     "w": ["A brown gas", "A yellow solid", "Nothing is seen"],
     "e": ["A brown gas is nitrogen dioxide, which is not formed here.",
           "The solid formed is white, not yellow.",
           "The white fumes are easy to see and are used as a test."],
     "y": "{formula('NH3')} + {formula('HCl')} → {formula('NH4Cl')}: the two gases meet and form a white smoke of fine solid."},
    {"q": "Ammonia is passed over heated copper(II) oxide. What is seen, and what does it show?",
     "r": "The black solid turns pink-brown; ammonia is acting as a reducing agent",
     "w": ["The black solid turns white; ammonia is acting as an acid",
           "The solid is unchanged; ammonia is unreactive", "A yellow solid forms; ammonia is acting as an oxidising agent"],
     "e": ["No white solid is formed, and ammonia is alkaline, not acidic.",
           "The reaction is clear, and the copper(II) oxide is reduced to copper.",
           "The ammonia is oxidised here, so it is the reducing agent."],
     "y": "{3}{formula('CuO')} + {2}{formula('NH3')} → {3}Cu + {formula('N2')} + {3}{formula('H2O')}: the copper oxide is reduced to copper."},
]

AMMRED = [
    {"q": "Ammonia is passed over heated copper(II) oxide. Which statement is correct?",
     "r": "The copper(II) oxide is reduced to copper, and the ammonia is oxidised to nitrogen",
     "w": ["The copper(II) oxide is oxidised and the ammonia reduced", "Neither is changed", "Both are reduced"],
     "e": ["Losing oxygen is reduction, so it is the copper(II) oxide that is reduced.",
           "The colour change from black to pink-brown shows a clear reaction.",
           "In any redox reaction one substance is oxidised while the other is reduced."],
     "y": "{3}{formula('CuO')} + {2}{formula('NH3')} → {3}Cu + {formula('N2')} + {3}{formula('H2O')}."},
    {"q": "What colour change is seen when ammonia reduces heated copper(II) oxide?", "r": "Black to pink-brown",
     "w": ["Pink-brown to black", "Black to white", "Blue to white"],
     "e": ["That is what happens when copper is heated in air: the opposite change.",
           "No white solid is formed; copper metal is pink-brown.",
           "Blue to white is what happens to copper(II) sulphate crystals when they are dehydrated."],
     "y": "The black copper(II) oxide becomes pink-brown copper as the oxygen is taken away."},
    {"q": "Which gas is formed from the ammonia when it reduces copper(II) oxide?", "r": "Nitrogen",
     "w": ["Hydrogen", "Oxygen", "Nitrogen dioxide"],
     "e": ["The hydrogen of the ammonia ends up in the water that is formed.",
           "The oxygen comes FROM the copper oxide and also ends up in the water.",
           "Nitrogen dioxide needs more oxygen; the product here is nitrogen itself."],
     "y": "The nitrogen of the ammonia is set free as {formula('N2')}, and its hydrogen becomes water."},
    {"q": "Why does ammonia burn in pure oxygen but not in air?", "r": "Air holds too little oxygen to keep the flame going",
     "w": ["Ammonia is not flammable at all", "The nitrogen in air puts the flame out by reacting", "Air is too cold"],
     "e": ["It does burn, as the experiment in pure oxygen shows.",
           "Nitrogen does not react; it simply dilutes the oxygen.",
           "Temperature is not the difference; the proportion of oxygen is."],
     "y": "In pure oxygen ammonia burns with a greenish-yellow flame; in air, with only {21} per cent oxygen, it will not."},
]

L.lesson(D, S, 12, ("k4-12", "Prepare ammonia and describe its properties"), [11],
  "Laboratory preparation: heat an ammonium salt with an alkali.\n"
  "2NH4Cl + Ca(OH)2 → CaCl2 + 2NH3 + 2H2O\n"
  "The gas is dried with quicklime (not concentrated sulphuric acid, which would react with it) and collected by upward "
  "delivery, because it is less dense than air and extremely soluble in water.\n"
  "Physical properties: a colourless gas with a sharp, pungent smell; less dense than air (relative molecular mass 17); "
  "extremely soluble in water, as the fountain experiment shows; easily liquefied.\n"
  "Chemical properties:\n"
  "• Alkaline: its solution turns damp red litmus blue, the only common alkaline gas.\n"
  "• With acids it gives ammonium salts: NH3 + HCl → NH4Cl, seen as dense white fumes.\n"
  "• A reducing agent: it reduces heated copper(II) oxide, 3CuO + 2NH3 → 3Cu + N2 + 3H2O.\n"
  "• It burns in oxygen, but not in air.",
  worked({"z": 1},
         "Explain why ammonia is dried with quicklime and not with concentrated sulphuric acid.",
         ["A drying agent must remove water without reacting with the gas.",
          "Ammonia is an alkaline gas.",
          "Concentrated sulphuric acid is an acid, so it would react with the ammonia to give ammonium sulphate.",
          "Quicklime, {formula('CaO')}, is a basic oxide, so it dries the gas without reacting with it."],
         "because sulphuric acid would react with the alkaline gas, while quicklime does not",
         checks=[]),
  [card("c4k12-1", "An ammonium salt heated with an alkali gives ammonia.",
        ["{2}{formula('NH4Cl')} + {formula('Ca(OH)2')} → {formula('CaCl2')} + {2}{formula('NH3')} + {2}{formula('H2O')}"], "k4-12-prep"),
   card("c4k12-2", "Ammonia is the only common alkaline gas: it turns damp red litmus blue.",
        ["with {formula('HCl')} it gives dense white fumes of {formula('NH4Cl')}"], "k4-12-test"),
   card("c4k12-3", "Ammonia is a reducing agent: it reduces heated copper(II) oxide to copper.",
        ["{3}{formula('CuO')} + {2}{formula('NH3')} → {3}Cu + {formula('N2')} + {3}{formula('H2O')}"], "k4-12-reduce")],
  [bank("k4-12-prep", 1, "{X.q}", AMM, SRC),
   mcq("k4-12-test", 1, "How would you show that a colourless gas is ammonia?",
       "{T.r}", [("{T.w1}", "w1"), ("{T.w2}", "w2"), ("{T.w3}", "w3")],
       ["{T.y}", "So the answer is: {answer}."],
       vars={"T": {"pick": [
           {"r": "Damp red litmus paper turns blue", "w1": "Damp blue litmus paper turns red",
            "w2": "Limewater turns milky", "w3": "A glowing splint relights",
            "y": "Ammonia is the only common alkaline gas, so it turns RED litmus blue."},
           {"r": "A rod dipped in concentrated hydrochloric acid gives dense white fumes",
            "w1": "A rod dipped in acid gives a brown gas", "w2": "A lighted splint burns more brightly",
            "w3": "The gas turns lead(II) ethanoate paper black",
            "y": "{formula('NH3')} + {formula('HCl')} → {formula('NH4Cl')}, a white solid that appears as a smoke."},
           {"r": "It has a sharp pungent smell and turns damp red litmus blue",
            "w1": "It smells of rotten eggs", "w2": "It has no smell at all", "w3": "It smells sweet and turns limewater milky",
            "y": "The smell with the litmus test together identify ammonia."}]}},
       misc=[("w1", "{T.y}"), ("w2", "{T.y}"), ("w3", "{T.y}")],
       sources=SRC),
   bank("k4-12-reduce", 2, "{X.q}", AMMRED, SRC),
   num("k4-12-mass", 2, "What mass of ammonia, in grams, is there in {n} mol of the gas?",
       "massOf(n, 'NH3')",
       ["The relative molecular mass of {formula('NH3')} is {molarMass('NH3')}.",
        "Mass = moles × molar mass = {n} × {molarMass('NH3')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2, 3]}},
       misc=[("div", "roundTo(n / molarMass('NH3'), 0.0001)", "Mass = moles × molar mass."),
             ("n2", "massOf(n, 'N2')", "Use the formula {formula('NH3')}, which includes the {3} hydrogen atoms.")],
       sources=SRC, unit="g"),
   num("k4-12-vol", 3, "What volume of ammonia, in dm³ at s.t.p., is given off when {n} mol of ammonium chloride is heated with excess calcium hydroxide?",
       "gasVolume(n)",
       ["{2}{formula('NH4Cl')} + {formula('Ca(OH)2')} → {formula('CaCl2')} + {2}{formula('NH3')} + {2}{formula('H2O')}.",
        "{2} mol of {formula('NH4Cl')} gives {2} mol of {formula('NH3')}, so {n} mol gives {n} mol.",
        "At s.t.p. that is {n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("half", "gasVolume(n / 2)", "The ratio is {2} to {2}, that is {1} mol of gas for each {1} mol of the salt."),
             ("mass", "massOf(n, 'NH3')", "The question asks for a volume in dm³, not a mass in grams.")],
       sources=SRC, unit="dm³")],
  learn=learn(
    [goal("prepare ammonia, explain how it is dried and collected, and describe it as an alkaline gas and a reducing agent.",
          "Lesson {11} (nitrogen) and Form Three acids, bases and salts.",
          "Lesson {17} (fertilisers made from ammonia) and the Haber process."),
     ("Preparation and collection",
      "Heat an ammonium salt with an alkali:\n"
      "{2}{formula('NH4Cl')} + {formula('Ca(OH)2')} → {formula('CaCl2')} + {2}{formula('NH3')} + {2}{formula('H2O')}\n"
      "The mixture is heated in a slanting tube, so that the water that condenses runs away from the hot glass.\n"
      "Drying: with QUICKLIME, {formula('CaO')}. Concentrated sulphuric acid cannot be used, because the acid would react "
      "with the alkaline gas; anhydrous calcium chloride also forms a compound with it.\n"
      "Collection: by upward delivery into an inverted jar, because ammonia is less dense than air "
      "(relative molecular mass {17}) and far too soluble to collect over water."),
     ("Properties",
      "Ammonia is a colourless gas with a sharp, pungent smell. It is extremely soluble in water: in the fountain experiment, "
      "a few drops of water in a flask of the gas lower the pressure so much that water rushes in as a fountain.\n"
      "• ALKALINE: it is the only common alkaline gas, and turns damp red litmus blue.\n"
      "• With acids it gives ammonium salts: {formula('NH3')} + {formula('HCl')} → {formula('NH4Cl')}, seen as dense white fumes. "
      "This is the test for the gas.\n"
      "• REDUCING agent: {3}{formula('CuO')} + {2}{formula('NH3')} → {3}Cu + {formula('N2')} + {3}{formula('H2O')}. "
      "The black solid turns pink-brown.\n"
      "• It burns in pure oxygen but not in air.")],
    key_words=[("alkaline gas", "a gas whose solution is an alkali; ammonia is the only common one"),
               ("quicklime", "calcium oxide, {formula('CaO')}, a basic drying agent"),
               ("upward delivery", "collecting a gas less dense than air in an inverted jar"),
               ("fountain experiment", "a demonstration of how soluble ammonia is")],
    examples=["{2}{formula('NH4Cl')} + {formula('Ca(OH)2')} → {formula('CaCl2')} + {2}{formula('NH3')} + {2}{formula('H2O')}", "{formula('NH3')} + {formula('HCl')} → {formula('NH4Cl')}: white fumes"],
    mistake=("ammonia is dried with concentrated sulphuric acid", "it is dried with quicklime",
             "The acid reacts with the alkaline gas to give ammonium sulphate, so the gas would be lost.")))
