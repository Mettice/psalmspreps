"""Form 4 Chemistry, Term 1, rows 13-17: nitric acid, the effect of heat on nitrates, the oxides of nitrogen,
the nitrogen cycle and the uses of nitrogen compounds. Run: python tools/authoring/form4/chem_nitrogen2.py"""
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

# ---------------------------------------------------------------- 13. Nitric acid
HNO3 = [
    {"q": "How is nitric acid prepared in the laboratory?", "r": "By heating a nitrate with concentrated sulphuric acid and distilling off the nitric acid",
     "w": ["By dissolving nitrogen in water", "By heating a nitrate alone", "By adding water to ammonia"],
     "e": ["Nitrogen is almost insoluble in water and does not give an acid.",
           "Heating a nitrate alone gives oxygen and oxides of nitrogen, not the acid.",
           "Ammonia in water gives an ALKALINE solution."],
     "y": "{formula('KNO3')} + {formula('H2SO4')} → {formula('KHSO4')} + {formula('HNO3')}: the less volatile acid drives out the more volatile one."},
    {"q": "Why must an all-glass apparatus be used when nitric acid is distilled?", "r": "The hot acid attacks cork, rubber and most metals",
     "w": ["Glass is cheaper", "The acid would dissolve in rubber harmlessly", "Any apparatus will do"],
     "e": ["Cost is not the reason; glass resists the acid.",
           "The acid attacks and destroys rubber rather than dissolving in it.",
           "Cork or rubber joints would be charred and would spoil the product."],
     "y": "Nitric acid is both a strong acid and a strong oxidising agent, so only glass stands up to it when hot."},
    {"q": "Pure nitric acid turns yellow on standing in the light. Why?", "r": "It decomposes a little, and the nitrogen dioxide formed dissolves in it",
     "w": ["It absorbs water from the air", "It reacts with the glass", "It takes in carbon dioxide"],
     "e": ["Taking in water would dilute it, not colour it.",
           "The acid does not attack glass.",
           "Carbon dioxide does not react with nitric acid."],
     "y": "{4}{formula('HNO3')} → {4}{formula('NO2')} + {2}{formula('H2O')} + {formula('O2')}: the brown {formula('NO2')} colours the acid yellow."},
    {"q": "Dilute nitric acid is added to copper. What gas is given off?", "r": "Nitrogen oxide, {formula('NO')}, which turns brown at the mouth of the tube",
     "w": ["Hydrogen", "Nitrogen dioxide only", "No gas at all"],
     "e": ["Copper is below hydrogen in the reactivity series, and nitric acid is an oxidising acid: no hydrogen is given off.",
           "{formula('NO2')} is given off with the CONCENTRATED acid; the dilute acid gives {formula('NO')}.",
           "The reaction does take place, and a blue solution of copper(II) nitrate forms."],
     "y": "The colourless {formula('NO')} meets the air and is oxidised at once to brown {formula('NO2')}."},
    {"q": "Why does nitric acid give no hydrogen with most metals?", "r": "It is a strong oxidising agent, so it oxidises any hydrogen formed to water",
     "w": ["It is too weak an acid", "Metals do not react with it at all", "It contains no hydrogen"],
     "e": ["Nitric acid is a strong acid; that is not the reason.",
           "Most metals do react with it, giving a nitrate and an oxide of nitrogen.",
           "Its formula {formula('HNO3')} shows that it does contain hydrogen."],
     "y": "Being an oxidising acid, it gives oxides of nitrogen instead of hydrogen; very dilute acid with magnesium is the exception."},
    {"q": "Dilute nitric acid is added to sodium carbonate. What happens?", "r": "Carbon dioxide is given off and sodium nitrate is formed",
     "w": ["Nitrogen dioxide is given off", "Hydrogen is given off", "Nothing happens"],
     "e": ["Nitrogen dioxide comes from the concentrated acid with a metal, not from a carbonate.",
           "Hydrogen comes from a metal with a non-oxidising acid.",
           "Any acid reacts with a carbonate."],
     "y": "{formula('Na2CO3')} + {2}{formula('HNO3')} → {2}{formula('NaNO3')} + {formula('H2O')} + {formula('CO2')}: here it behaves as an ordinary acid."},
]

L.lesson(D, S, 13, ("k4-13", "Prepare nitric acid and describe its properties"), [12],
  "Laboratory preparation: heat potassium or sodium nitrate with concentrated sulphuric acid in an all-glass apparatus "
  "and distil off the nitric acid.\n"
  "KNO3 + H2SO4 → KHSO4 + HNO3\n"
  "The less volatile sulphuric acid drives out the more volatile nitric acid. Glass is used because the hot acid attacks "
  "cork, rubber and metals.\n"
  "Industrially it is made by oxidising ammonia (the Ostwald process).\n"
  "Properties:\n"
  "• As an acid: with bases, basic oxides and carbonates it gives nitrates. Na2CO3 + 2HNO3 → 2NaNO3 + H2O + CO2.\n"
  "• As an oxidising agent: with metals it gives a nitrate and an oxide of nitrogen, not hydrogen. "
  "Dilute acid with copper gives NO; concentrated acid gives NO2.\n"
  "• It decomposes in light: 4HNO3 → 4NO2 + 2H2O + O2, so pure acid slowly turns yellow and is kept in dark bottles.",
  worked({"z": 1},
         "Explain why copper gives no hydrogen with nitric acid, although zinc gives hydrogen with dilute hydrochloric acid.",
         ["Copper is below hydrogen in the reactivity series, so it cannot displace hydrogen from any acid.",
          "Zinc is above hydrogen, so with hydrochloric acid it does displace it.",
          "Nitric acid is also a strong oxidising agent.",
          "It oxidises copper to copper(II) nitrate and is itself reduced to an oxide of nitrogen: {formula('NO')} with the dilute acid, {formula('NO2')} with the concentrated acid."],
         "copper is below hydrogen, and nitric acid oxidises instead, giving an oxide of nitrogen",
         checks=[]),
  [card("c4k13-1", "A nitrate with concentrated sulphuric acid gives nitric acid, distilled in all-glass apparatus.",
        ["{formula('KNO3')} + {formula('H2SO4')} → {formula('KHSO4')} + {formula('HNO3')}"], "k4-13-prep"),
   card("c4k13-2", "Nitric acid is an oxidising acid: with metals it gives an oxide of nitrogen, not hydrogen.",
        ["dilute acid with copper gives {formula('NO')}; concentrated acid gives {formula('NO2')}"], "k4-13-metal"),
   card("c4k13-3", "With bases and carbonates it behaves as an ordinary acid, giving nitrates.",
        ["{formula('Na2CO3')} + {2}{formula('HNO3')} → {2}{formula('NaNO3')} + {formula('H2O')} + {formula('CO2')}"], "k4-13-salt")],
  [bank("k4-13-prep", 1, "{X.q}", HNO3, SRC),
   mcq("k4-13-metal", 2, "{M.q}",
       "{M.r}", [("{M.w1}", "w1"), ("{M.w2}", "w2"), ("{M.w3}", "w3")],
       ["{M.y}", "So the answer is: {answer}."],
       vars={"M": {"pick": [
           {"q": "Copper is warmed with dilute nitric acid. What gas is given off?",
            "r": "Nitrogen oxide, {formula('NO')}, colourless but turning brown in air",
            "w1": "Hydrogen", "w2": "Nitrogen dioxide, brown from the start", "w3": "Carbon dioxide",
            "y": "The dilute acid is reduced to {formula('NO')}, which is oxidised to brown {formula('NO2')} when it meets the air."},
           {"q": "Copper is warmed with concentrated nitric acid. What gas is given off?",
            "r": "Nitrogen dioxide, {formula('NO2')}, a brown gas",
            "w1": "Hydrogen", "w2": "Nitrogen oxide, which stays colourless", "w3": "Oxygen",
            "y": "The concentrated acid is reduced only as far as {formula('NO2')}, which is brown."},
           {"q": "Very dilute nitric acid is added to magnesium. What gas is given off?",
            "r": "Hydrogen, the one case where nitric acid behaves as an ordinary acid with a metal",
            "w1": "Nitrogen dioxide", "w2": "Nitrogen oxide", "w3": "No gas at all",
            "y": "Magnesium is reactive enough, and the acid is too dilute to act as an oxidising agent."},
           {"q": "Why is no hydrogen given off when copper reacts with nitric acid?",
            "r": "Copper is below hydrogen in the reactivity series, and the acid oxidises instead",
            "w1": "Copper is above hydrogen in the reactivity series", "w2": "Nitric acid contains no hydrogen",
            "w3": "Copper does not react with nitric acid at all",
            "y": "An oxidising acid gives an oxide of nitrogen rather than hydrogen."}]}},
       misc=[("w1", "{M.y}"), ("w2", "{M.y}"), ("w3", "{M.y}")],
       sources=SRC),
   num("k4-13-mass", 2, "What mass of nitric acid, in grams, is there in {n} mol of the acid?",
       "massOf(n, 'HNO3')",
       ["The relative molecular mass of {formula('HNO3')} is {molarMass('HNO3')}.",
        "Mass = moles × molar mass = {n} × {molarMass('HNO3')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("div", "roundTo(n / molarMass('HNO3'), 0.0001)", "Mass = moles × molar mass."),
             ("no3", "massOf(n, 'NO3')", "Include the hydrogen atom: the formula is {formula('HNO3')}.")],
       sources=SRC, unit="g"),
   mcq("k4-13-salt", 2, "Dilute nitric acid is added to {R.n}. What is formed?",
       "{R.r}", [("{R.w1}", "w1"), ("{R.w2}", "w2"), ("{R.w3}", "w3")],
       ["{R.y}", "So the answer is: {answer}."],
       vars={"R": {"pick": [
           {"n": "sodium carbonate", "r": "Sodium nitrate, water and carbon dioxide",
            "w1": "Sodium nitrate and hydrogen", "w2": "Sodium nitrate and nitrogen dioxide", "w3": "No reaction",
            "y": "{formula('Na2CO3')} + {2}{formula('HNO3')} → {2}{formula('NaNO3')} + {formula('H2O')} + {formula('CO2')}."},
           {"n": "copper(II) oxide", "r": "Copper(II) nitrate and water, giving a blue solution",
            "w1": "Copper(II) nitrate and hydrogen", "w2": "Copper and water", "w3": "No reaction",
            "y": "{formula('CuO')} + {2}{formula('HNO3')} → {formula('Cu(NO3)2')} + {formula('H2O')}: a base with an acid gives a salt and water."},
           {"n": "sodium hydroxide solution", "r": "Sodium nitrate and water",
            "w1": "Sodium nitrate and hydrogen", "w2": "Ammonia and water", "w3": "No reaction",
            "y": "{formula('NaOH')} + {formula('HNO3')} → {formula('NaNO3')} + {formula('H2O')}: an ordinary neutralisation."}]}},
       misc=[("w1", "{R.y}"), ("w2", "{R.y}"), ("w3", "{R.y}")],
       sources=SRC),
   num("k4-13-salt-mass", 3, "What mass of sodium nitrate, in grams, is made when {n} mol of sodium hydroxide is neutralised by dilute nitric acid?",
       "massOf(n, 'NaNO3')",
       ["{formula('NaOH')} + {formula('HNO3')} → {formula('NaNO3')} + {formula('H2O')}: {1} mol gives {1} mol.",
        "The relative formula mass of {formula('NaNO3')} is {molarMass('NaNO3')}.",
        "Mass = {n} × {molarMass('NaNO3')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("acid", "massOf(n, 'HNO3')", "The question asks for the mass of the SALT, not of the acid."),
             ("base", "massOf(n, 'NaOH')", "The question asks for the mass of sodium nitrate.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("prepare nitric acid, explain why glass is used, and describe it as both an acid and an oxidising agent.",
          "Lesson {8} (sulphuric acid as a less volatile acid) and Lesson {12} (ammonia).",
          "Lesson {14} (what heat does to nitrates) and Lesson {15} (the oxides of nitrogen)."),
     ("Preparation",
      "Heat potassium or sodium nitrate with concentrated sulphuric acid and distil:\n"
      "{formula('KNO3')} + {formula('H2SO4')} → {formula('KHSO4')} + {formula('HNO3')}\n"
      "Sulphuric acid is less volatile, so on heating it drives the more volatile nitric acid out of its salt, and the "
      "nitric acid distils over.\n"
      "The whole apparatus must be glass, because the hot acid attacks cork, rubber and most metals. The receiver is kept "
      "cool so that the acid condenses.\n"
      "Pure nitric acid is colourless, but it slowly decomposes in the light:\n"
      "{4}{formula('HNO3')} → {4}{formula('NO2')} + {2}{formula('H2O')} + {formula('O2')}, and the brown {formula('NO2')} "
      "dissolving in it turns it yellow. It is kept in dark bottles.\n"
      "In industry it is made by oxidising ammonia in the Ostwald process."),
     ("An acid and an oxidising agent",
      "As an ACID, dilute nitric acid behaves normally with bases, basic oxides and carbonates, giving nitrates:\n"
      "• {formula('NaOH')} + {formula('HNO3')} → {formula('NaNO3')} + {formula('H2O')};\n"
      "• {formula('Na2CO3')} + {2}{formula('HNO3')} → {2}{formula('NaNO3')} + {formula('H2O')} + {formula('CO2')}.\n"
      "With METALS it behaves differently, because it is a strong oxidising agent. Instead of hydrogen it gives an oxide of nitrogen:\n"
      "• dilute acid with copper: colourless {formula('NO')}, which turns brown in the air;\n"
      "• concentrated acid with copper: brown {formula('NO2')}.\n"
      "The one common exception is very dilute acid with magnesium, which does give hydrogen.")],
    key_words=[("volatile", "easily turned into a vapour"),
               ("oxidising acid", "an acid that oxidises what it reacts with, giving no hydrogen with most metals"),
               ("distil", "boil a liquid and condense the vapour to collect it"),
               ("nitrate", "a salt of nitric acid, such as {formula('NaNO3')}")],
    examples=["{formula('KNO3')} + {formula('H2SO4')} → {formula('KHSO4')} + {formula('HNO3')}", "dilute acid + Cu → {formula('NO')}", "concentrated acid + Cu → {formula('NO2')}"],
    mistake=("copper and dilute nitric acid give hydrogen", "they give nitrogen oxide, {formula('NO')}",
             "Nitric acid is an oxidising acid, and copper is below hydrogen in the reactivity series.")))

# ---------------------------------------------------------------- 14. Effect of heat on nitrates
NITRATES = [
    {"q": "What is formed when sodium nitrate is heated?", "r": "Sodium nitrite and oxygen",
     "w": ["Sodium oxide, nitrogen dioxide and oxygen", "Sodium, nitrogen dioxide and oxygen", "It does not decompose"],
     "e": ["That is what happens to the nitrates of most other metals, but not to those of sodium and potassium.",
           "Only the nitrates of silver and mercury leave the metal itself.",
           "It does decompose, giving off oxygen."],
     "y": "{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}: a very reactive metal keeps its nitrogen as a nitrite."},
    {"q": "What is formed when lead(II) nitrate is heated?", "r": "Lead(II) oxide, nitrogen dioxide and oxygen",
     "w": ["Lead(II) nitrite and oxygen", "Lead, nitrogen dioxide and oxygen", "Lead(II) oxide only"],
     "e": ["Only the nitrates of sodium and potassium give nitrites.",
           "Only silver and mercury nitrates leave the metal itself.",
           "A brown gas and oxygen are given off as well."],
     "y": "{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}, with crackling and a brown gas."},
    {"q": "What is formed when silver nitrate is heated?", "r": "Silver, nitrogen dioxide and oxygen",
     "w": ["Silver oxide, nitrogen dioxide and oxygen", "Silver nitrite and oxygen", "It does not decompose"],
     "e": ["Silver oxide is itself unstable to heat and breaks down to the metal.",
           "Only the very reactive metals give nitrites.",
           "It decomposes readily on heating."],
     "y": "{2}{formula('AgNO3')} → {2}Ag + {2}{formula('NO2')} + {formula('O2')}: an unreactive metal is left as the metal."},
    {"q": "What is formed when ammonium nitrate is heated gently?", "r": "Dinitrogen oxide and water",
     "w": ["Ammonia and nitric acid", "Nitrogen and water", "Nitrogen dioxide and water"],
     "e": ["The salt does not simply split back into its acid and base on gentle heating.",
           "Nitrogen and water come from ammonium NITRITE, not nitrate.",
           "Nitrogen dioxide comes from the nitrates of metals."],
     "y": "{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}: this is how laughing gas is prepared."},
    {"q": "Which observation shows that a brown gas given off on heating a nitrate is nitrogen dioxide?",
     "r": "It is brown, it turns damp blue litmus red, and it is the only common brown gas here",
     "w": ["It is brown and turns limewater milky", "It is brown and relights a glowing splint",
           "It is brown and smells of rotten eggs"],
     "e": ["Limewater is the test for carbon dioxide, which is colourless.",
           "Oxygen relights a splint, but oxygen is colourless.",
           "Rotten eggs is hydrogen sulphide, which is colourless."],
     "y": "{formula('NO2')} is brown and acidic; the oxygen given off with it is what relights a splint."},
    {"q": "Why do the nitrates of sodium and potassium behave differently from the rest?",
     "r": "They are the nitrates of very reactive metals, so they decompose only as far as the nitrite",
     "w": ["They are not really nitrates", "They contain no oxygen", "They melt instead of decomposing"],
     "e": ["They are nitrates, with the same {formula('NO3')} ion.",
           "Every nitrate contains oxygen.",
           "They do melt, but they also decompose, giving off oxygen."],
     "y": "The more reactive the metal, the more stable its compounds are to heat."},
]

HEATTEST = [
    {"q": "Two nitrates are heated. One gives off only a colourless gas; the other gives off a brown gas as well. What does this show?",
     "r": "The first is the nitrate of a very reactive metal such as sodium or potassium",
     "w": ["The first is the nitrate of a very unreactive metal", "The second has not been heated strongly enough",
           "The two are the same compound"],
     "e": ["An unreactive metal such as silver gives the metal, brown {formula('NO2')} AND oxygen.",
           "Stronger heating would not change which products form.",
           "The same compound would give the same products."],
     "y": "Only sodium and potassium nitrates decompose as far as the nitrite, giving off oxygen alone."},
    {"q": "A nitrate is heated and a shiny solid is left in the tube. Which metal is it likely to be?", "r": "Silver",
     "w": ["Sodium", "Copper", "Zinc"],
     "e": ["Sodium nitrate leaves a white nitrite, not a shiny metal.",
           "Copper(II) nitrate leaves black copper(II) oxide.",
           "Zinc nitrate leaves zinc oxide, yellow while hot and white when cold."],
     "y": "Only the very unreactive metals, silver and mercury, are left as the metal itself."},
    {"q": "A nitrate is heated and leaves a solid that is yellow while hot and white when cold. Which oxide is it?",
     "r": "Zinc oxide", "w": ["Lead(II) oxide", "Copper(II) oxide", "Sodium oxide"],
     "e": ["Lead(II) oxide is orange while hot and yellow when cold.",
           "Copper(II) oxide is black both hot and cold.",
           "Sodium nitrate leaves a nitrite, not an oxide."],
     "y": "Zinc oxide is the one that changes from yellow to white as it cools."},
    {"q": "Which gas given off when a nitrate is heated would relight a glowing splint?", "r": "Oxygen",
     "w": ["Nitrogen dioxide", "Nitrogen", "Carbon dioxide"],
     "e": ["Nitrogen dioxide is brown and would not relight a splint.",
           "Nitrogen puts a splint out.",
           "No carbon dioxide is given off by a nitrate."],
     "y": "Every nitrate gives off oxygen on heating, and oxygen relights a glowing splint."},
]

L.lesson(D, S, 14, ("k4-14", "Describe the effect of heat on nitrates"), [13],
  "All nitrates decompose on heating, but what is left depends on the metal.\n"
  "• Sodium and potassium nitrates (very reactive metals) give the nitrite and oxygen:\n"
  "2NaNO3 → 2NaNO2 + O2.\n"
  "• Most other metal nitrates give the metal oxide, brown nitrogen dioxide and oxygen:\n"
  "2Pb(NO3)2 → 2PbO + 4NO2 + O2. Lead(II) nitrate crackles as it decomposes.\n"
  "• Silver and mercury nitrates (very unreactive metals) give the metal itself, nitrogen dioxide and oxygen:\n"
  "2AgNO3 → 2Ag + 2NO2 + O2.\n"
  "• Ammonium nitrate is not a metal nitrate: it gives dinitrogen oxide and water, NH4NO3 → N2O + 2H2O.\n"
  "The more reactive the metal, the more stable its nitrate is to heat.",
  worked({"z": 1},
         "Lead(II) nitrate and sodium nitrate are each heated strongly. State what is seen and write the equations.",
         ["Lead(II) nitrate crackles, gives off a brown gas and leaves a yellow solid.",
          "{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}.",
          "Sodium nitrate melts and gives off a colourless gas that relights a glowing splint; the solid left is white.",
          "{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}."],
         "lead nitrate gives {formula('PbO')}, {formula('NO2')} and {formula('O2')}; sodium nitrate gives {formula('NaNO2')} and {formula('O2')}",
         checks=[]),
  [card("c4k14-1", "Sodium and potassium nitrates give the nitrite and oxygen only.",
        ["{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}"], "k4-14-which"),
   card("c4k14-2", "Most other metal nitrates give the oxide, brown {formula('NO2')} and oxygen.",
        ["{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}"], "k4-14-product"),
   card("c4k14-3", "Silver and mercury nitrates leave the metal itself.",
        ["{2}{formula('AgNO3')} → {2}Ag + {2}{formula('NO2')} + {formula('O2')}"], "k4-14-group")],
  [bank("k4-14-which", 1, "{X.q}", NITRATES, SRC),
   mcq("k4-14-product", 1, "{N} is heated strongly. What solid is left?",
       "{P.r}", [("{P.w1}", "w1"), ("{P.w2}", "w2"), ("{P.w3}", "w3")],
       ["{P.y}", "So the answer is: {answer}."],
       vars={"P": {"pick": [
           {"n": "Potassium nitrate", "r": "Potassium nitrite", "w1": "Potassium oxide", "w2": "Potassium metal", "w3": "Nothing at all",
            "y": "Potassium is very reactive, so its nitrate decomposes only as far as the nitrite."},
           {"n": "Copper(II) nitrate", "r": "Black copper(II) oxide", "w1": "Copper(II) nitrite", "w2": "Copper metal", "w3": "Nothing at all",
            "y": "A metal of middling reactivity leaves its oxide, with brown {formula('NO2')} and oxygen given off."},
           {"n": "Silver nitrate", "r": "Silver metal", "w1": "Silver oxide", "w2": "Silver nitrite", "w3": "Nothing at all",
            "y": "Silver is very unreactive, so even its oxide is unstable and the metal is left."},
           {"n": "Zinc nitrate", "r": "Zinc oxide", "w1": "Zinc nitrite", "w2": "Zinc metal", "w3": "Nothing at all",
            "y": "Zinc is in the middle of the reactivity series, so its nitrate gives the oxide."}]},
             "N": {"expr": "P.n"}},
       misc=[("w1", "{P.y}"), ("w2", "{P.y}"), ("w3", "{P.y}")],
       sources=SRC),
   bank("k4-14-group", 2, "{X.q}", HEATTEST, SRC),
   num("k4-14-vol", 2, "What volume of oxygen, in dm³ at s.t.p., is given off when {n} mol of sodium nitrate decomposes completely?",
       "gasVolume(n / 2)",
       ["{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}.",
        "{2} mol of the nitrate gives {1} mol of oxygen, so {n} mol gives {n} ÷ {2} = {n / 2} mol.",
        "At s.t.p. that is {n / 2} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.2, 0.4, 0.5, 1, 2, 4]}},
       misc=[("same", "gasVolume(n)", "The equation gives {1} mol of oxygen for every {2} mol of nitrate."),
             ("double", "gasVolume(2 * n)", "Read the coefficients: {2} nitrate to {1} oxygen.")],
       sources=SRC, unit="dm³"),
   num("k4-14-mass", 3, "What mass of lead(II) oxide, in grams, is left when {n} mol of lead(II) nitrate decomposes completely?",
       "massOf(n, 'PbO')",
       ["{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}: {1} mol gives {1} mol of {formula('PbO')}.",
        "The relative formula mass of {formula('PbO')} is {molarMass('PbO')}.",
        "Mass = {n} × {molarMass('PbO')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1]}},
       misc=[("nitrate", "massOf(n, 'Pb(NO3)2')", "The question asks for the mass of the OXIDE left, not of the nitrate."),
             ("half", "massOf(n / 2, 'PbO')", "The ratio is {2} to {2}, that is {1} mol of oxide for each {1} mol of nitrate.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("predict and write equations for what heat does to the nitrate of any metal, and link it to the reactivity series.",
          "Lesson {13} (nitrates as the salts of nitric acid) and Form Three the reactivity series.",
          "Lesson {15} (the oxides of nitrogen given off) and testing for nitrates."),
     ("Three patterns",
      "Every nitrate decomposes on heating, but the products depend on how reactive the metal is.\n"
      "• VERY REACTIVE metals (sodium, potassium): the nitrite and oxygen only.\n"
      "{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}\n"
      "• MOST metals (calcium, magnesium, zinc, iron, lead, copper): the oxide, brown nitrogen dioxide and oxygen.\n"
      "{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}\n"
      "Lead(II) nitrate crackles loudly as it decomposes, and the yellow {formula('PbO')} left is orange while hot.\n"
      "• VERY UNREACTIVE metals (silver, mercury): the metal itself, nitrogen dioxide and oxygen.\n"
      "{2}{formula('AgNO3')} → {2}Ag + {2}{formula('NO2')} + {formula('O2')}"),
     ("Ammonium nitrate, and what you see",
      "Ammonium nitrate is not a metal nitrate, and it behaves differently again:\n"
      "{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}\n"
      "This gentle heating is how dinitrogen oxide, 'laughing gas', is prepared. Strong heating of ammonium nitrate is "
      "dangerous, because it can explode.\n"
      "What to look for when a nitrate is heated:\n"
      "• a colourless gas that relights a glowing splint: oxygen;\n"
      "• a brown gas that turns damp blue litmus red: nitrogen dioxide;\n"
      "• the colour of the solid left: white for a nitrite, yellow or black for an oxide, shiny for a metal.\n"
      "The rule to remember: the more reactive the metal, the more stable its nitrate.")],
    key_words=[("decompose", "break down into simpler substances"),
               ("nitrite", "a salt containing the {formula('NO2')} ion with a {1}− charge, such as {formula('NaNO2')}"),
               ("thermal stability", "how well a compound stands up to heat"),
               ("reactivity series", "metals in order of how readily they react")],
    examples=["{2}{formula('NaNO3')} → {2}{formula('NaNO2')} + {formula('O2')}", "{2}{formula('Pb(NO3)2')} → {2}{formula('PbO')} + {4}{formula('NO2')} + {formula('O2')}", "{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}"],
    mistake=("heating sodium nitrate gives sodium oxide and nitrogen dioxide", "it gives sodium nitrite and oxygen",
             "Sodium is very reactive, so its nitrate decomposes only as far as the nitrite.")))

# ---------------------------------------------------------------- 15. Oxides of nitrogen
OXIDES = [
    {"q": "How is dinitrogen oxide, {formula('N2O')}, prepared?", "r": "By gently heating ammonium nitrate",
     "w": ["By heating a metal nitrate", "By burning nitrogen in air", "By adding water to a nitride"],
     "e": ["A metal nitrate gives {formula('NO2')} and oxygen, not {formula('N2O')}.",
           "Nitrogen does not burn in air.",
           "A nitride with water gives ammonia."],
     "y": "{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}, gently heated."},
    {"q": "What is unusual about dinitrogen oxide in a test for gases?", "r": "It relights a glowing splint, like oxygen",
     "w": ["It turns limewater milky", "It smells of rotten eggs", "It is brown"],
     "e": ["Limewater is the test for carbon dioxide.",
           "That smell belongs to hydrogen sulphide.",
           "{formula('N2O')} is colourless; {formula('NO2')} is the brown one."],
     "y": "It decomposes on the hot splint to give oxygen, so it relights it; but it is not oxygen, and it has a faint sweet smell."},
    {"q": "Nitrogen oxide, {formula('NO')}, is let out into the air. What is seen?", "r": "It turns brown at once",
     "w": ["It stays colourless", "It turns blue", "It disappears"],
     "e": ["It reacts with the oxygen of the air immediately.",
           "No blue colour is formed.",
           "It does not disappear; it becomes a visible brown gas."],
     "y": "{2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}: the brown colour is a test for {formula('NO')}."},
    {"q": "Which oxide of nitrogen is brown?", "r": "Nitrogen dioxide, {formula('NO2')}",
     "w": ["Nitrogen oxide, {formula('NO')}", "Dinitrogen oxide, {formula('N2O')}", "All three are brown"],
     "e": ["{formula('NO')} is colourless until it meets air.",
           "{formula('N2O')} is colourless.",
           "Only {formula('NO2')} is coloured."],
     "y": "{formula('NO2')} is a brown, poisonous, acidic gas."},
    {"q": "Nitrogen dioxide is dissolved in water. What is formed?", "r": "A mixture of nitric acid and nitrous acid",
     "w": ["Ammonia solution", "A neutral solution", "Nitrogen and oxygen"],
     "e": ["Ammonia is alkaline and is not formed from {formula('NO2')} and water.",
           "The solution turns blue litmus red, so it is acidic.",
           "The gas dissolves and reacts; it does not split into its elements."],
     "y": "{2}{formula('NO2')} + {formula('H2O')} → {formula('HNO3')} + {formula('HNO2')}: an acidic oxide."},
    {"q": "Which oxide of nitrogen is used as an anaesthetic?", "r": "Dinitrogen oxide, {formula('N2O')}",
     "w": ["Nitrogen oxide, {formula('NO')}", "Nitrogen dioxide, {formula('NO2')}", "None of them"],
     "e": ["{formula('NO')} is poisonous and is not used as an anaesthetic.",
           "{formula('NO2')} is poisonous and damages the lungs.",
           "{formula('N2O')} has been used in dentistry for many years."],
     "y": "Dinitrogen oxide, 'laughing gas', is used with oxygen as a mild anaesthetic."},
]

L.lesson(D, S, 15, ("k4-15", "Prepare and describe the oxides of nitrogen"), [14],
  "Three oxides of nitrogen are studied.\n"
  "• Dinitrogen oxide, N2O ('laughing gas'): made by gently heating ammonium nitrate, NH4NO3 → N2O + 2H2O. "
  "Colourless, faintly sweet, fairly soluble, neutral. It relights a glowing splint, like oxygen, because it decomposes on "
  "the hot splint. Used with oxygen as a mild anaesthetic.\n"
  "• Nitrogen oxide, NO: made by warming copper with dilute nitric acid. Colourless and neutral, almost insoluble in water, "
  "but it turns brown at once in air: 2NO + O2 → 2NO2. That is the test for it.\n"
  "• Nitrogen dioxide, NO2: made by heating lead(II) nitrate, or by copper with concentrated nitric acid. "
  "A brown, poisonous, acidic gas, denser than air, very soluble: 2NO2 + H2O → HNO3 + HNO2.\n"
  "Nitrogen oxides from car engines and lightning take part in acid rain.",
  worked({"z": 1},
         "A colourless gas relights a glowing splint. Give two gases it could be, and a test that tells them apart.",
         ["Oxygen relights a glowing splint.",
          "Dinitrogen oxide also relights one, because it decomposes on the hot splint to give oxygen.",
          "To tell them apart, mix the gas with nitrogen oxide, {formula('NO')}.",
          "With oxygen the mixture turns brown at once, because {2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}; with {formula('N2O')} it does not."],
         "oxygen or dinitrogen oxide; mixing with {formula('NO')} turns brown only with oxygen",
         checks=[]),
  [card("c4k15-1", "{formula('N2O')} comes from gently heating ammonium nitrate and relights a glowing splint.",
        ["{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}"], "k4-15-which"),
   card("c4k15-2", "{formula('NO')} is colourless but turns brown at once in air.",
        ["{2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}"], "k4-15-no"),
   card("c4k15-3", "{formula('NO2')} is brown and acidic: with water it gives nitric and nitrous acids.",
        ["{2}{formula('NO2')} + {formula('H2O')} → {formula('HNO3')} + {formula('HNO2')}"], "k4-15-match")],
  [bank("k4-15-which", 1, "{X.q}", OXIDES, SRC),
   match("k4-15-match", 1, "Match each oxide of nitrogen to a property.",
         [("{formula('N2O')}", "Colourless; relights a glowing splint"), ("{formula('NO')}", "Colourless; turns brown in air"),
          ("{formula('NO2')}", "Brown and acidic"), ("{formula('N2')}", "Makes up most of the air"),
          ("{formula('NH3')}", "Alkaline, with a pungent smell")],
         pick=3, sources=SRC),
   mcq("k4-15-no", 1, "{Q.q}",
       "{Q.r}", [("{Q.w1}", "w1"), ("{Q.w2}", "w2"), ("{Q.w3}", "w3")],
       ["{Q.y}", "So the answer is: {answer}."],
       vars={"Q": {"pick": [
           {"q": "How can nitrogen oxide be told from dinitrogen oxide?", "r": "Nitrogen oxide turns brown when it meets air; dinitrogen oxide does not",
            "w1": "Dinitrogen oxide turns brown in air", "w2": "Both turn brown in air", "w3": "Neither can be told from the other",
            "y": "{2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}, and {formula('NO2')} is brown."},
           {"q": "How is nitrogen oxide prepared in the laboratory?", "r": "By warming copper with dilute nitric acid",
            "w1": "By warming copper with concentrated nitric acid", "w2": "By heating ammonium nitrate", "w3": "By burning ammonia in air",
            "y": "The dilute acid is reduced as far as {formula('NO')}; the concentrated acid gives {formula('NO2')}."},
           {"q": "Why is nitrogen oxide collected over water?", "r": "It is almost insoluble in water, and water keeps the air away from it",
            "w1": "It is very soluble in water", "w2": "It is less dense than air", "w3": "It reacts with water to give an acid",
            "y": "Collecting it over water stops it meeting air and turning brown."}]}},
       misc=[("w1", "{Q.y}"), ("w2", "{Q.y}"), ("w3", "{Q.y}")],
       sources=SRC),
   num("k4-15-vol", 2, "What volume of dinitrogen oxide, in dm³ at s.t.p., is given off when {n} mol of ammonium nitrate is gently heated?",
       "gasVolume(n)",
       ["{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}: {1} mol gives {1} mol of gas.",
        "At s.t.p. that is {n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("double", "gasVolume(2 * n)", "{2} is the coefficient of the WATER, not of the gas collected."),
             ("mass", "massOf(n, 'N2O')", "The question asks for a volume in dm³, not a mass in grams.")],
       sources=SRC, unit="dm³"),
   num("k4-15-mass", 3, "What mass of ammonium nitrate, in grams, is needed to make {n} mol of dinitrogen oxide?",
       "massOf(n, 'NH4NO3')",
       ["{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}: {1} mol of the salt gives {1} mol of gas.",
        "The relative formula mass of {formula('NH4NO3')} is {molarMass('NH4NO3')}.",
        "Mass = {n} × {molarMass('NH4NO3')} = {answer} g."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 2]}},
       misc=[("gas", "massOf(n, 'N2O')", "The question asks for the mass of the SALT, not of the gas."),
             ("div", "roundTo(n / molarMass('NH4NO3'), 0.0001)", "Mass = moles × molar mass.")],
       sources=SRC, unit="g")],
  learn=learn(
    [goal("prepare and recognise the three oxides of nitrogen and tell them apart by colour and by simple tests.",
          "Lesson {14} (nitrates give oxides of nitrogen on heating) and Lesson {13} (nitric acid with copper).",
          "Lesson {16} (the nitrogen cycle) and the part these oxides play in acid rain."),
     ("Dinitrogen oxide and nitrogen oxide",
      "DINITROGEN OXIDE, {formula('N2O')}, 'laughing gas':\n"
      "• made by gently heating ammonium nitrate: {formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')};\n"
      "• colourless, faintly sweet, fairly soluble, neutral;\n"
      "• it RELIGHTS a glowing splint, because it decomposes on the hot splint and gives oxygen. So this test alone cannot "
      "tell it from oxygen;\n"
      "• used with oxygen as a mild anaesthetic.\n"
      "NITROGEN OXIDE, {formula('NO')}:\n"
      "• made by warming copper with DILUTE nitric acid;\n"
      "• colourless, neutral, almost insoluble, so it is collected over water;\n"
      "• it turns brown at once in air: {2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}. This is its test."),
     ("Nitrogen dioxide",
      "NITROGEN DIOXIDE, {formula('NO2')}:\n"
      "• made by heating lead(II) nitrate, or by warming copper with CONCENTRATED nitric acid;\n"
      "• a BROWN, poisonous gas, denser than air and very soluble;\n"
      "• acidic: {2}{formula('NO2')} + {formula('H2O')} → {formula('HNO3')} + {formula('HNO2')}, so it turns damp blue litmus red.\n"
      "Telling the three apart: only {formula('NO2')} is brown to start with; {formula('NO')} turns brown when air reaches it; "
      "{formula('N2O')} stays colourless and relights a splint.\n"
      "Nitrogen oxides are made in car engines and by lightning, and they help to cause acid rain and photochemical smog.")],
    key_words=[("anaesthetic", "a substance that takes away the feeling of pain"),
               ("acidic oxide", "an oxide that gives an acid with water"),
               ("smog", "a haze formed when sunlight acts on pollutants in the air")],
    examples=["{formula('NH4NO3')} → {formula('N2O')} + {2}{formula('H2O')}", "{2}{formula('NO')} + {formula('O2')} → {2}{formula('NO2')}", "{2}{formula('NO2')} + {formula('H2O')} → {formula('HNO3')} + {formula('HNO2')}"],
    mistake=("a gas that relights a glowing splint must be oxygen", "it could also be dinitrogen oxide",
             "{formula('N2O')} decomposes on the hot splint and gives oxygen, so it relights it too.")))
