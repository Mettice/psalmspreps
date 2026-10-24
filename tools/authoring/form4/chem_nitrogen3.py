"""Form 4 Chemistry, Term 1, rows 16-17: the nitrogen cycle and the uses of nitrogen compounds.
Run: python tools/authoring/form4/chem_nitrogen3.py"""
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

# ---------------------------------------------------------------- 16. The nitrogen cycle
CYCLE = [
    {"q": "What is nitrogen fixation?", "r": "Changing nitrogen from the air into a compound that plants can use",
     "w": ["Taking nitrates out of the soil", "Changing nitrates back into nitrogen gas",
           "Holding nitrogen in the air so it cannot escape"],
     "e": ["Taking nitrates out of the soil is what plants do when they absorb them.",
           "That is denitrification, the opposite process.",
           "Nitrogen does not need to be held in; the problem is that plants cannot use it as a gas."],
     "y": "Plants cannot use nitrogen gas, so it must first be fixed into ammonia or nitrates."},
    {"q": "Which bacteria live in the root nodules of leguminous plants such as beans and groundnuts?", "r": "Nitrogen-fixing bacteria",
     "w": ["Denitrifying bacteria", "Nitrifying bacteria", "Bacteria of decay"],
     "e": ["Denitrifying bacteria live in waterlogged soil and give nitrogen back to the air.",
           "Nitrifying bacteria live free in the soil and change ammonium compounds into nitrates.",
           "Bacteria of decay break down dead matter; they do not live in root nodules."],
     "y": "Rhizobium in the nodules fixes nitrogen from the air, which is why legumes enrich the soil."},
    {"q": "What do nitrifying bacteria do?", "r": "They change ammonium compounds into nitrites and then into nitrates",
     "w": ["They change nitrates into nitrogen gas", "They fix nitrogen from the air",
           "They break down protein in dead plants"],
     "e": ["That is denitrification.",
           "That is nitrogen fixation, done by different bacteria.",
           "That is done by the bacteria of decay, which give ammonium compounds."],
     "y": "Nitrosomonas gives nitrites and Nitrobacter gives nitrates, which the plant roots can absorb."},
    {"q": "What happens during denitrification?", "r": "Nitrates in the soil are changed back into nitrogen gas",
     "w": ["Nitrogen gas is changed into nitrates", "Protein is changed into ammonia",
           "Ammonia is changed into nitrates"],
     "e": ["That is nitrogen fixation.",
           "That is decay, carried out by bacteria of decay.",
           "That is nitrification."],
     "y": "Denitrifying bacteria work in waterlogged soil with little air, and the soil loses nitrogen to the atmosphere."},
    {"q": "How does lightning take part in the nitrogen cycle?", "r": "Its very high temperature makes nitrogen and oxygen combine, and the oxides dissolve in rain as nitric acid",
     "w": ["It splits nitrates in the soil", "It kills nitrifying bacteria", "It has no part in the cycle"],
     "e": ["Lightning acts on the air, not on the soil.",
           "Its effect is to add fixed nitrogen, not to remove bacteria.",
           "It is one of the natural ways nitrogen is fixed."],
     "y": "{formula('N2')} + {formula('O2')} → {2}{formula('NO')} in the flash; the acid formed reaches the soil as nitrate."},
    {"q": "Why do farmers often grow beans or groundnuts between crops of maize?", "r": "The bacteria in their root nodules put fixed nitrogen back into the soil",
     "w": ["They take nitrates out of the soil faster", "They keep insects away from the maize",
           "They use less water than maize"],
     "e": ["Legumes add nitrogen to the soil rather than stripping it.",
           "Keeping insects away is not the reason for this rotation.",
           "Water use is not what makes this rotation useful."],
     "y": "Legumes carry nitrogen-fixing bacteria, so the soil is richer in nitrogen for the next crop."},
]

L.lesson(D, S, 16, ("k4-16", "Describe the nitrogen cycle"), [15],
  "The nitrogen cycle is how nitrogen passes between the air, the soil and living things.\n"
  "• Fixation: nitrogen from the air is turned into compounds plants can use. By nitrogen-fixing bacteria (Rhizobium) in "
  "the root nodules of legumes such as beans and groundnuts; by lightning, which makes nitrogen oxides that reach the soil "
  "in rain; and by industry, in the Haber process.\n"
  "• Absorption: plant roots take in nitrates and build them into proteins. Animals get their protein by eating plants.\n"
  "• Decay: bacteria of decay break down dead plants, animals and waste into ammonium compounds.\n"
  "• Nitrification: nitrifying bacteria change ammonium compounds into nitrites (Nitrosomonas) and then nitrates (Nitrobacter).\n"
  "• Denitrification: in waterlogged soil, denitrifying bacteria change nitrates back into nitrogen gas, which returns to the air.\n"
  "Farmers keep the soil rich by rotating crops with legumes and by adding fertilisers.",
  worked({"z": 1},
         "Explain why planting beans in a field helps the maize grown there the following year.",
         ["Beans are legumes, and their roots carry nodules holding nitrogen-fixing bacteria.",
          "These bacteria change nitrogen from the air into compounds the plant can use.",
          "When the bean plants die and decay, that fixed nitrogen is left in the soil as ammonium compounds.",
          "Nitrifying bacteria change these into nitrates, which the maize roots can take in."],
         "the bacteria in the bean root nodules leave fixed nitrogen in the soil",
         checks=[]),
  [card("c4k16-1", "Fixation turns nitrogen gas into compounds plants can use.",
        ["by bacteria in root nodules, by lightning, and in the Haber process"], "k4-16-which"),
   card("c4k16-2", "Nitrifying bacteria turn ammonium compounds into nitrites and then nitrates.",
        ["decay gives ammonium compounds; nitrification gives nitrates"], "k4-16-stage"),
   card("c4k16-3", "Denitrifying bacteria return nitrogen to the air from waterlogged soil.",
        ["which is why waterlogged fields lose their fertility"], "k4-16-match")],
  [bank("k4-16-which", 1, "{X.q}", CYCLE, SRC),
   match("k4-16-match", 1, "Match each stage of the nitrogen cycle to what happens.",
         [("Nitrogen fixation", "Nitrogen gas becomes a compound plants can use"),
          ("Decay", "Dead matter becomes ammonium compounds"),
          ("Nitrification", "Ammonium compounds become nitrates"),
          ("Denitrification", "Nitrates become nitrogen gas again"),
          ("Absorption", "Plant roots take in nitrates from the soil")],
         pick=3, sources=SRC),
   mcq("k4-16-stage", 2, "{G.q}",
       "{G.r}", [("{G.w1}", "w1"), ("{G.w2}", "w2"), ("{G.w3}", "w3")],
       ["{G.y}", "So the answer is: {answer}."],
       vars={"G": {"pick": [
           {"q": "Which stage comes immediately after the decay of a dead plant?",
            "r": "Nitrification: the ammonium compounds become nitrites and then nitrates",
            "w1": "Denitrification", "w2": "Nitrogen fixation", "w3": "Absorption by the roots",
            "y": "Decay gives ammonium compounds, which nitrifying bacteria change into nitrates."},
           {"q": "A field is waterlogged for several weeks. What is likely to happen to its nitrates?",
            "r": "Denitrifying bacteria change them into nitrogen gas, which escapes",
            "w1": "They are fixed into protein", "w2": "They turn into ammonia and stay in the soil",
            "w3": "Nothing happens to them", "y": "Denitrifying bacteria work where there is little air, so waterlogged soil loses nitrogen."},
           {"q": "How does nitrogen from the air reach the protein of a cow?",
            "r": "Fixation to nitrates, absorption by a plant, then the cow eats the plant",
            "w1": "The cow breathes in nitrogen and uses it directly", "w2": "The cow absorbs nitrates through its skin",
            "w3": "Lightning puts nitrogen straight into the cow's food",
            "y": "Animals cannot use nitrogen gas: it must pass through fixation and then through plants."}]}},
       misc=[("w1", "{G.y}"), ("w2", "{G.y}"), ("w3", "{G.y}")],
       sources=SRC),
   order("k4-16-order", 2, "{A.q}",
         ["{A.s[0]}", "{A.s[1]}", "{A.s[2]}", "{A.s[3]}", "{A.s[4]}"],
         vars={"A": {"pick": [
             {"q": "Put the stages of the nitrogen cycle in order, starting from nitrogen in the air.",
              "s": ["Nitrogen in the air is fixed by bacteria or by lightning",
                    "Nitrates form in the soil",
                    "Plant roots absorb the nitrates and build proteins",
                    "Animals eat the plants, and both die and decay",
                    "Denitrifying bacteria return nitrogen gas to the air"]},
             {"q": "Put these stages of decay and nitrification in order.",
              "s": ["A plant dies and falls on the soil",
                    "Bacteria of decay break down its protein",
                    "Ammonium compounds are left in the soil",
                    "Nitrosomonas changes them into nitrites",
                    "Nitrobacter changes the nitrites into nitrates"]},
             {"q": "Put the stages by which lightning adds nitrogen to the soil in order.",
              "s": ["A lightning flash heats the air to a very high temperature",
                    "Nitrogen and oxygen combine to give nitrogen oxide",
                    "The nitrogen oxide is oxidised to nitrogen dioxide in the air",
                    "The nitrogen dioxide dissolves in rain to give an acid",
                    "The acid reaches the soil, where it forms nitrates"]}]}},
         sources=SRC),
   mcq("k4-16-farm", 3, "{F.q}",
       "{F.r}", [("{F.w1}", "w1"), ("{F.w2}", "w2"), ("{F.w3}", "w3")],
       ["{F.y}", "So the answer is: {answer}."],
       vars={"F": {"pick": [
           {"q": "Why does a farmer plough and drain a waterlogged field?",
            "r": "To let air into the soil, so that denitrifying bacteria do not take the nitrates away",
            "w1": "To kill the nitrifying bacteria", "w2": "To add nitrates directly", "w3": "To stop lightning fixing nitrogen",
            "y": "Denitrifying bacteria work where there is little air, so draining the soil protects its nitrates."},
           {"q": "Why does burning crop residues instead of ploughing them in waste nitrogen?",
            "r": "The nitrogen in the plants escapes into the air instead of decaying into the soil",
            "w1": "Burning makes the soil too hot for roots", "w2": "Ash contains no minerals at all",
            "w3": "Burning kills the plants, which were still growing",
            "y": "Ploughing the residues in lets bacteria of decay return their nitrogen to the soil."},
           {"q": "A farmer grows maize in the same field every year without fertiliser. What happens to the yield?",
            "r": "It falls, because each crop removes nitrates that are not replaced",
            "w1": "It rises, because the soil gets used to maize", "w2": "It stays the same for ever",
            "w3": "It falls, because lightning stops fixing nitrogen",
            "y": "Harvesting takes the nitrogen away in the grain, so the soil must be replenished."}]}},
       misc=[("w1", "{F.y}"), ("w2", "{F.y}"), ("w3", "{F.y}")],
       sources=SRC)],
  learn=learn(
    [goal("name and explain each stage of the nitrogen cycle and say how farming practices affect it.",
          "Lesson {11} (nitrogen is unreactive) and Form Three food chains.",
          "Lesson {17} (fertilisers) and the study of soil fertility in Biology and Agriculture."),
     ("Getting nitrogen into living things",
      "Nitrogen gas is {78} per cent of the air, but it is so unreactive that plants cannot use it. It must first be FIXED "
      "into a compound:\n"
      "• nitrogen-fixing bacteria (Rhizobium) in the root nodules of legumes such as beans, groundnuts and soya;\n"
      "• lightning: the flash is hot enough to make {formula('N2')} and {formula('O2')} combine, and the oxides dissolve in rain;\n"
      "• industry: the Haber process makes ammonia, which is turned into fertiliser.\n"
      "Plant roots absorb NITRATES from the soil and build them into proteins. Animals get their protein by eating plants."),
     ("Returning nitrogen to the soil and the air",
      "• DECAY: when plants and animals die, and in their waste, bacteria of decay break the protein down into ammonium compounds.\n"
      "• NITRIFICATION: nitrifying bacteria change these into nitrites (Nitrosomonas) and then into nitrates (Nitrobacter), "
      "which plants can use again.\n"
      "• DENITRIFICATION: in waterlogged soil, where there is little air, denitrifying bacteria change nitrates back into "
      "nitrogen gas, and the soil loses nitrogen to the air.\n"
      "Farmers work with the cycle: they rotate crops with legumes, plough crop residues back in, drain waterlogged land, "
      "and add fertilisers to replace the nitrogen taken away in the harvest.")],
    key_words=[("nitrogen fixation", "changing nitrogen gas into a usable compound"),
               ("legume", "a plant such as a bean or groundnut with nitrogen-fixing root nodules"),
               ("nitrification", "the change of ammonium compounds into nitrates by bacteria"),
               ("denitrification", "the change of nitrates back into nitrogen gas")],
    examples=["Rhizobium in bean roots: fixation", "decay → ammonium compounds", "waterlogged soil: denitrification"],
    mistake=("plants take nitrogen straight from the air", "they take nitrates from the soil",
             "Only certain bacteria can use nitrogen gas; plants need it already fixed.")))

# ---------------------------------------------------------------- 17. Uses of nitrogen compounds
NUSES = [
    {"q": "Which compound of nitrogen is the starting point for most nitrogen fertilisers?", "r": "Ammonia",
     "w": ["Nitrogen dioxide", "Dinitrogen oxide", "Hydrogen sulphide"],
     "e": ["Nitrogen dioxide is a poisonous pollutant, not a feedstock for fertiliser.",
           "Dinitrogen oxide is used as an anaesthetic, not for fertiliser.",
           "Hydrogen sulphide contains no nitrogen at all."],
     "y": "Ammonia from the Haber process is neutralised by acids to give ammonium salts, or oxidised to nitric acid."},
    {"q": "Ammonia is neutralised by sulphuric acid. Which fertiliser is formed?", "r": "Ammonium sulphate",
     "w": ["Ammonium nitrate", "Sodium nitrate", "Urea"],
     "e": ["Ammonium nitrate comes from ammonia and NITRIC acid.",
           "Sodium nitrate contains no ammonium; it is mined or made from sodium compounds.",
           "Urea is made from ammonia and carbon dioxide."],
     "y": "{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}."},
    {"q": "Why is liquid nitrogen used to freeze food and to store medical samples?", "r": "It is very cold and unreactive, so it freezes quickly without damaging the material",
     "w": ["It is hot enough to kill bacteria", "It dissolves the water in the food", "It burns away any oxygen"],
     "e": ["Liquid nitrogen is extremely cold, not hot.",
           "It does not dissolve anything; it freezes it.",
           "It does not burn; it simply keeps oxygen away by being unreactive."],
     "y": "Liquid nitrogen boils at −{196} °C, so it freezes quickly, and being inert it does not react with the sample."},
    {"q": "Which use depends on a nitrogen compound exploding?", "r": "Making TNT and other explosives for quarrying",
     "w": ["Making ammonium sulphate fertiliser", "Filling packets of food", "Making nitric acid"],
     "e": ["A fertiliser must not explode in the field; it is used for its nitrogen.",
           "Food packets are filled with nitrogen GAS, which is unreactive.",
           "Nitric acid is a reagent, not an explosive itself."],
     "y": "Nitro compounds made from nitric acid release a great deal of gas very suddenly."},
    {"q": "Why is ammonia used in some refrigerators?", "r": "It is easily liquefied and takes in a great deal of heat when it evaporates",
     "w": ["It is poisonous to bacteria", "It is lighter than air", "It freezes at a very high temperature"],
     "e": ["Keeping food cold, not killing bacteria directly, is the purpose of a refrigerator.",
           "Being lighter than air has nothing to do with cooling.",
           "A refrigerant must evaporate easily, not freeze easily."],
     "y": "The latent heat taken in as the liquid ammonia evaporates is what cools the cabinet."},
    {"q": "Which statement about nitrogen fertilisers and the environment is correct?",
     "r": "Fertiliser washed into rivers makes water plants grow too fast, and the water loses its oxygen",
     "w": ["Fertilisers cannot reach rivers", "Extra nitrates in a river are always harmless",
           "Nitrogen fertilisers cause acid rain directly"],
     "e": ["Rain washes soluble nitrates off fields into streams and rivers.",
           "Too much nitrate causes eutrophication, which kills fish.",
           "Acid rain comes mainly from sulphur dioxide and nitrogen oxides in smoke, not from fertiliser in the soil."],
     "y": "Eutrophication: the plants grow, then die and decay, and the decay uses up the oxygen in the water."},
]

L.lesson(D, S, 17, ("k4-17", "State the uses of nitrogen and its compounds"), [16],
  "Nitrogen gas: filling packets of food and flushing oil tanks, because it is unreactive; as liquid nitrogen at −196 °C "
  "for quick-freezing food and storing medical samples.\n"
  "Ammonia: made in the Haber process and used to make fertilisers (ammonium sulphate, ammonium nitrate, urea), "
  "nitric acid (the Ostwald process), cleaning liquids, and as a refrigerant.\n"
  "Nitric acid: making fertilisers, explosives (TNT, nitroglycerine), dyes, drugs and plastics.\n"
  "Fertilisers replace the nitrogen taken out of the soil by crops, so yields stay high. Too much, however, is washed into "
  "rivers, where it makes water plants grow too fast; when these die and decay the water loses its oxygen and fish die. "
  "This is eutrophication.",
  worked({"n": 2},
         "What mass of ammonium sulphate, {formula('(NH4)2SO4')}, is made from {n} mol of ammonia?",
         ["{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}.",
          "{2} mol of ammonia gives {1} mol of the fertiliser, so {n} mol gives {n} ÷ {2} = {n / 2} mol.",
          "The relative formula mass of {formula('(NH4)2SO4')} is {molarMass('(NH4)2SO4')}.",
          "Mass = {n / 2} × {molarMass('(NH4)2SO4')}."],
         "{massOf(n / 2, '(NH4)2SO4')} g",
         checks=["molarMass('(NH4)2SO4') == 132"]),
  [card("c4k17-1", "Ammonia from the Haber process is the starting point for fertilisers and nitric acid.",
        ["{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}"], "k4-17-uses"),
   card("c4k17-2", "Nitrogen gas is used where an unreactive atmosphere is needed.",
        ["packets of food, oil tanks, and liquid nitrogen for quick-freezing"], "k4-17-which"),
   card("c4k17-3", "Too much fertiliser washed into rivers causes eutrophication.",
        ["water plants grow fast, die, and their decay uses up the oxygen"], "k4-17-match")],
  [bank("k4-17-uses", 1, "{X.q}", NUSES, SRC),
   match("k4-17-match", 1, "Match each substance to a use.",
         [("Liquid nitrogen", "Quick-freezing food"), ("Ammonia", "Making fertiliser in the Haber process route"),
          ("Nitric acid", "Making explosives"), ("Ammonium sulphate", "Feeding a maize crop"),
          ("Dinitrogen oxide", "A mild anaesthetic")],
         pick=3, sources=SRC),
   mcq("k4-17-which", 2, "Which substance would be used {U.q}?",
       "{U.r}", [("{U.w1}", "w1"), ("{U.w2}", "w2"), ("{U.w3}", "w3")],
       ["{U.y}", "So the answer is: {answer}."],
       vars={"U": {"pick": [
           {"q": "to stop crisps going stale in a sealed packet", "r": "Nitrogen gas",
            "w1": "Ammonia", "w2": "Nitrogen dioxide", "w3": "Nitric acid",
            "y": "Nitrogen is unreactive, so it keeps oxygen away without affecting the food."},
           {"q": "to add nitrogen to a field of maize", "r": "Ammonium sulphate",
            "w1": "Liquid nitrogen", "w2": "Nitrogen dioxide", "w3": "Dinitrogen oxide",
            "y": "A soluble ammonium salt gives the plants nitrogen in a form their roots can take up."},
           {"q": "to freeze a medical sample quickly", "r": "Liquid nitrogen",
            "w1": "Ammonium nitrate", "w2": "Nitric acid", "w3": "Nitrogen dioxide",
            "y": "Liquid nitrogen boils at −{196} °C and is unreactive, so it freezes the sample without harming it."},
           {"q": "to make dyes and explosives in a factory", "r": "Nitric acid",
            "w1": "Liquid nitrogen", "w2": "Nitrogen gas", "w3": "Dinitrogen oxide",
            "y": "Nitric acid puts nitro groups into organic compounds, which is how dyes and explosives are made."}]}},
       misc=[("w1", "{U.y}"), ("w2", "{U.y}"), ("w3", "{U.y}")],
       sources=SRC),
   num("k4-17-fert", 2, "What mass of ammonium sulphate, in grams, is made from {n} mol of ammonia?",
       "massOf(n / 2, '(NH4)2SO4')",
       ["{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}: {2} mol of ammonia gives {1} mol of the salt.",
        "{n} mol of ammonia gives {n / 2} mol.",
        "Mass = {n / 2} × {molarMass('(NH4)2SO4')} = {answer} g."],
       vars={"n": {"pick": [0.2, 0.4, 0.5, 1, 2, 4]}},
       misc=[("nohalf", "massOf(n, '(NH4)2SO4')", "{2} mol of ammonia are needed for each {1} mol of the salt."),
             ("ammonia", "massOf(n, 'NH3')", "The question asks for the mass of the FERTILISER, not of the ammonia.")],
       sources=SRC, unit="g"),
   num("k4-17-percent", 3, "What is the percentage by mass of nitrogen in {formula(F)}? Give your answer to {1} decimal place.",
       "roundTo(percentMass(F, 'N'), 0.1)",
       ["The relative formula mass of {formula(F)} is {molarMass(F)}.",
        "It holds {atomCount(F, 'N')} nitrogen atoms, of mass {atomCount(F, 'N')} × {ram('N')} = {atomCount(F, 'N') * ram('N')}.",
        "Percentage = {atomCount(F, 'N') * ram('N')} ÷ {molarMass(F)} × {100} = {answer} per cent."],
       vars={"F": {"pick": ["NH3", "NH4NO3", "(NH4)2SO4", "NaNO3", "KNO3", "CO(NH2)2"]}},
       misc=[("swap", "roundTo(molarMass(F) / (atomCount(F, 'N') * ram('N')) * 100, 0.1)", "Divide the mass of nitrogen by the WHOLE formula mass."),
             ("one", "roundTo(ram('N') / molarMass(F) * 100, 0.1)", "Count every nitrogen atom: there are {atomCount(F, 'N')}.", "atomCount(F, 'N') > 1")],
       sources=SRC, unit="%")],
  learn=learn(
    [goal("give the uses of nitrogen, ammonia and nitric acid, and explain how too much fertiliser harms rivers.",
          "Lessons {11} to {16}, which give the properties behind each use.",
          "the mole calculations of the next chapter, used to work out how much fertiliser a crop needs."),
     ("Uses",
      "NITROGEN GAS is used where an unreactive atmosphere is needed: filling packets of crisps and other food so the fat "
      "does not go rancid, and flushing out oil tanks so that they cannot catch fire. As LIQUID nitrogen at −{196} °C it "
      "quick-freezes food and stores blood and other medical samples.\n"
      "AMMONIA, made in the Haber process, is the starting point for:\n"
      "• fertilisers: ammonium sulphate, ammonium nitrate and urea;\n"
      "• nitric acid, by the Ostwald process;\n"
      "• cleaning liquids, and refrigeration, because it takes in much heat as it evaporates.\n"
      "NITRIC ACID is used for fertilisers, explosives such as TNT, dyes, drugs and plastics.\n"
      "DINITROGEN OXIDE is used with oxygen as a mild anaesthetic."),
     ("Fertilisers and the environment",
      "Every harvest takes nitrogen off the land in the grain or the leaves. Fertilisers put it back, so yields stay high "
      "and the same field can be used year after year.\n"
      "A fertiliser is judged partly by its percentage of nitrogen by mass: in {formula('NH4NO3')} the nitrogen is "
      "{28} out of {80}, which is {35} per cent.\n"
      "But nitrates are soluble, so rain washes them into streams. There they make water plants grow very fast; when these "
      "die, the bacteria that decay them use up the oxygen and the fish suffocate. This is eutrophication.\n"
      "Careful farmers use only what the crop needs and leave strips of grass beside streams.")],
    key_words=[("fertiliser", "a substance added to soil to supply the elements plants need"),
               ("Haber process", "making ammonia from nitrogen and hydrogen"),
               ("eutrophication", "the loss of oxygen in water caused by too many nutrients"),
               ("urea", "{formula('CO(NH2)2')}, a nitrogen fertiliser made from ammonia and carbon dioxide")],
    examples=["{2}{formula('NH3')} + {formula('H2SO4')} → {formula('(NH4)2SO4')}", "{formula('NH4NO3')}: {35} per cent nitrogen", "liquid nitrogen at −{196} °C"],
    mistake=("more fertiliser always means a better harvest", "too much is washed into rivers and causes eutrophication",
             "Beyond what the crop can take up, the extra nitrate runs off and kills fish.")))
