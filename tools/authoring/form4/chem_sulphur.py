"""Form 4 Chemistry, Term 1, rows 1-9: the chemistry of sulphur. Row 10 is an integration activity, not a lesson.
Run: python tools/authoring/form4/chem_sulphur.py
Equations are written with formula() so that subscripts are drawn, never typed (TEACHER-REVIEW TR-K4-1)."""
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

# ---------------------------------------------------------------- 1. Frasch process
FRASCH = [
    {"q": "Where is sulphur found as the free element?", "r": "In underground deposits, often near volcanoes and oil fields",
     "w": ["Only combined in sea water", "Only in the air", "Only in living plants"],
     "e": ["Sea water holds sulphates, which are combined sulphur, not the free element.",
           "Air holds only traces of sulphur compounds, not the free element.",
           "Plants hold sulphur in proteins, which is combined sulphur."],
     "y": "Free sulphur occurs in beds a few hundred metres down, and combined as sulphides and sulphates."},
    {"q": "How many concentric pipes are used in the Frasch process?", "r": "Three",
     "w": ["One", "Two", "Five"],
     "e": ["One pipe could not carry water down and sulphur up at the same time.",
           "A third pipe is needed for the compressed air that lifts the froth.",
           "Three are enough: water in, air in, froth out."],
     "y": "Superheated water goes down the outer pipe, hot compressed air down the inner one, and the froth rises up the middle one."},
    {"q": "What is sent down the outer pipe in the Frasch process, and why?", "r": "Superheated water at about {170} °C, to melt the sulphur underground",
     "w": ["Cold water, to cool the rock", "Hot compressed air, to blow the sulphur up", "Molten sulphur, to start the process"],
     "e": ["Cold water would not melt sulphur, which melts at about {115} °C.",
           "The compressed air goes down the INNER pipe; the water goes down the outer one.",
           "The sulphur is already in the ground; the water melts it there."],
     "y": "Sulphur melts at about {115} °C, so water above that temperature, kept liquid by pressure, melts it in place."},
    {"q": "Why is hot compressed air forced down the inner pipe?", "r": "It froths the molten sulphur so that the lighter froth is pushed up the middle pipe",
     "w": ["It burns the sulphur to sulphur dioxide", "It cools the molten sulphur so it sets", "It dissolves the sulphur in water"],
     "e": ["Burning would destroy the product; the air is there to lift it.",
           "Hot air does not set the sulphur; the froth must stay molten to rise.",
           "Sulphur is insoluble in water."],
     "y": "The froth of air and molten sulphur is less dense, so the pressure pushes it up the middle pipe."},
    {"q": "Why is sulphur from the Frasch process very pure?", "r": "Only the sulphur melts and is pushed up; the rock and sand stay behind",
     "w": ["It is purified later by distillation", "It is washed with acid at the surface", "It is crystallised from water"],
     "e": ["No further purification is needed; it comes up about {99} per cent pure.",
           "No acid washing is used in the process.",
           "Sulphur is insoluble in water, so it cannot be crystallised from it."],
     "y": "Melting separates the sulphur from the rock underground, so it arrives almost pure."},
]

PURE = [
    {"q": 'Why does the Frasch process give sulphur that needs no further purification?', "r": 'Only the sulphur melts at that temperature, so the rock and sand are left behind underground',
     "w": ['The sulphur is distilled as it rises', 'Acid is added to dissolve the impurities', 'The water washes all the impurities away'],
     "e": ['No distillation takes place; the separation happens by melting.', 'No acid is used in the Frasch process.', 'Sulphur is insoluble in water, and the impurities are not washed out by it.'],
     "y": 'Sulphur melts at about {115} °C but rock and sand do not, so only the sulphur is carried up.'},
    {"q": 'Why is the Frasch process used instead of digging the sulphur out?', "r": 'The beds lie under layers of loose, water-bearing rock that would collapse into a mine',
     "w": ['Sulphur is too valuable to dig', 'Digging would set the sulphur on fire', 'The sulphur lies only a few metres down'],
     "e": ['Value is not the reason; the ground above the beds is.', 'Sulphur does not catch fire by itself when dug.', 'The beds lie a few HUNDRED metres down.'],
     "y": 'Pumping melted sulphur up through pipes avoids sinking a shaft through unsafe ground.'},
    {"q": 'What happens to the molten sulphur when it reaches the surface?', "r": 'It runs into large tanks and solidifies as it cools',
     "w": ['It is burned at once to sulphur dioxide', 'It is dissolved in water for transport', 'It is distilled to separate the allotropes'],
     "e": ['Burning it would destroy the product; some is burned later, at the factory.', 'Sulphur is insoluble in water.', 'Allotropes are not separated by distillation; they are forms of the same element.'],
     "y": 'The froth is run into tanks, where the sulphur cools and sets as a solid ready for use.'},
    {"q": 'Roughly how pure is the sulphur brought up by the Frasch process?', "r": 'About {99} per cent pure',
     "w": ['About {50} per cent pure', 'About {75} per cent pure', 'Less than {10} per cent pure'],
     "e": ['Half of the mass would be impurity, which melting underground avoids.', 'The purity is much higher than that.', 'That would be an ore, not the free element.'],
     "y": 'Because only the sulphur melts, almost nothing else comes up with it.'},
]

L.lesson(D, S, 1, ("k4-1", "Describe the occurrence of sulphur and its extraction by the Frasch process"), [],
  "Sulphur occurs free in underground beds, often near volcanoes and oil fields, and combined as sulphides "
  "(galena PbS, zinc blende ZnS, iron pyrites FeS2) and sulphates (gypsum CaSO4, barytes BaSO4).\n"
  "The Frasch process brings up free sulphur from deep beds using three concentric pipes:\n"
  "• Outer pipe: superheated water at about 170 °C, kept liquid under pressure, melts the sulphur (melting point about 115 °C).\n"
  "• Inner pipe: hot compressed air froths the molten sulphur.\n"
  "• Middle pipe: the froth, being less dense, is forced up to the surface.\n"
  "The rock and sand stay underground, so the sulphur comes up about 99 per cent pure. It is run into tanks and allowed to solidify.",
  worked({"mp": 115, "t": 170},
         "Explain why the water sent down the Frasch pump is at {t} °C and not at {100} °C.",
         ["Sulphur melts at about {mp} °C.",
          "Water at {100} °C is not hot enough to melt it.",
          "Water is kept liquid above {100} °C by the pressure in the pipe, so it can be superheated to {t} °C.",
          "At {t} °C the water is well above {mp} °C and melts the sulphur underground."],
         "because {mp} °C is needed to melt sulphur, which is above the normal boiling point of water",
         checks=["t > mp"]),
  [card("c4k1-1", "Sulphur occurs free underground and combined in sulphides and sulphates.",
        ["free in beds near oil fields; combined as {formula('PbS')}, {formula('ZnS')} and {formula('CaSO4')}"], "k4-1-frasch"),
   card("c4k1-2", "The Frasch pump has three concentric pipes: superheated water in, compressed air in, froth out.",
        ["water about {170} °C down the outer pipe; air down the inner; froth up the middle"], "k4-1-pipes"),
   card("c4k1-3", "Only the sulphur melts, so it comes up almost pure.",
        ["the rock and sand are left underground"], "k4-1-pure")],
  [bank("k4-1-frasch", 1, "{X.q}", FRASCH, SRC),
   mcq("k4-1-pipes", 1, "Which pipe of the Frasch pump carries {P.q}?",
       "{P.r}", [("{P.w1}", "w1"), ("{P.w2}", "w2"), ("{P.w3}", "w3")],
       ["{P.y}", "So the answer is: {answer}."],
       vars={"P": {"pick": [
           {"q": "the superheated water down to the sulphur bed", "r": "The outer pipe",
            "w1": "The inner pipe", "w2": "The middle pipe", "w3": "There is only one pipe",
            "y": "Water goes down the outer pipe, air down the inner pipe, and the froth comes up the middle one."},
           {"q": "the hot compressed air", "r": "The inner pipe",
            "w1": "The outer pipe", "w2": "The middle pipe", "w3": "A separate fourth pipe",
            "y": "The innermost pipe carries air, which froths the molten sulphur so it can rise."},
           {"q": "the froth of molten sulphur to the surface", "r": "The middle pipe",
            "w1": "The outer pipe", "w2": "The inner pipe", "w3": "The same pipe as the water",
            "y": "The froth rises between the water pipe and the air pipe, that is up the middle one."}]}},
       misc=[("w1", "{P.y}"), ("w2", "{P.y}"), ("w3", "{P.y}")],
       sources=SRC),
   match("k4-1-ores", 2, "Match each mineral to its formula.",
         [("Galena", "{formula('PbS')}"), ("Zinc blende", "{formula('ZnS')}"), ("Iron pyrites", "{formula('FeS2')}"),
          ("Gypsum", "{formula('CaSO4')}"), ("Barytes", "{formula('BaSO4')}")],
         pick=3, sources=SRC),
   bank("k4-1-pure", 2, "{X.q}", PURE, SRC),
   order("k4-1-steps", 3, "{A.q}",
         ["{A.s[0]}", "{A.s[1]}", "{A.s[2]}", "{A.s[3]}", "{A.s[4]}"],
         vars={"A": {"pick": [
             {"q": "Put the stages of the Frasch process in order.",
              "s": ["Three concentric pipes are sunk down to the sulphur bed",
                    "Superheated water at about {170} °C is forced down the outer pipe",
                    "The sulphur in the bed melts",
                    "Hot compressed air is forced down the inner pipe and froths the molten sulphur",
                    "The froth is pushed up the middle pipe and runs into tanks to solidify"]},
             {"q": "Put these stages of getting sulphur from the ground in order, starting with the deepest.",
              "s": ["Solid sulphur lies in a bed a few hundred metres down",
                    "Heat from the superheated water reaches the bed",
                    "The sulphur melts and collects at the foot of the pipes",
                    "Air bubbles make the molten sulphur into a light froth",
                    "The froth reaches the surface and is run off"]},
             {"q": "Put these stages of testing a sample from a Frasch well in order.",
              "s": ["A sample of the solid from the tank is taken",
                    "Its colour is noted: a brittle yellow solid",
                    "A little is shaken with water and does not dissolve",
                    "A little is shaken with carbon disulphide and dissolves",
                    "A little is heated in air and burns with a blue flame"]}]}},
         sources=SRC)],
  learn=learn(
    [goal("say where sulphur is found and describe each stage of the Frasch process and why it gives pure sulphur.",
          "Form Three elements, mixtures and the idea of melting point.",
          "Lesson {2} (the properties of sulphur) and the compounds made from it in the rest of the chapter."),
     ("Where sulphur is found",
      "Sulphur is found free (uncombined) in beds a few hundred metres underground, often near volcanoes and oil fields, "
      "notably in the United States, Mexico and Poland.\n"
      "It is also found combined:\n"
      "• as sulphides: galena {formula('PbS')}, zinc blende {formula('ZnS')}, iron pyrites {formula('FeS2')};\n"
      "• as sulphates: gypsum {formula('CaSO4')}, barytes {formula('BaSO4')}.\n"
      "Sulphur is also present in coal and crude oil, and in the proteins of living things."),
     ("The Frasch process",
      "Free sulphur deep underground is brought up by the Frasch pump, which has three concentric pipes.\n"
      "• Superheated water at about {170} °C is forced down the OUTER pipe. Pressure keeps it liquid above its normal "
      "boiling point, and it melts the sulphur, whose melting point is about {115} °C.\n"
      "• Hot compressed air is forced down the INNER pipe. It froths the molten sulphur.\n"
      "• The froth is less dense than water, so the pressure pushes it up the MIDDLE pipe to the surface, where it runs "
      "into tanks and solidifies.\n"
      "Because only the sulphur melts, the rock and sand stay underground and the sulphur comes up about {99} per cent pure.")],
    key_words=[("free element", "an element not joined to any other, as sulphur is in its beds"),
               ("superheated water", "water kept liquid above {100} °C by pressure"),
               ("Frasch process", "the method of mining underground sulphur with three concentric pipes"),
               ("froth", "a light mixture of gas bubbles and liquid")],
    examples=["galena {formula('PbS')}: a sulphide", "gypsum {formula('CaSO4')}: a sulphate", "water at {170} °C melts sulphur at {115} °C"],
    mistake=("the compressed air burns the sulphur so it can rise", "the air froths the molten sulphur so it is light enough to be pushed up",
             "Burning would destroy the sulphur. The air only makes a light froth.")))

# ---------------------------------------------------------------- 2. Properties and allotropes
ALLO = [
    {"q": "What are allotropes?", "r": "Different forms of the same element in the same physical state",
     "w": ["Different elements with the same properties", "Compounds of one element with another",
           "Atoms of one element with different numbers of neutrons"],
     "e": ["Allotropes are forms of ONE element, not different elements.",
           "No other element is joined: an allotrope is still the pure element.",
           "Those are isotopes, which differ in the nucleus, not in the arrangement of the atoms."],
     "y": "Rhombic and monoclinic sulphur are both pure solid sulphur, with the atoms packed differently."},
    {"q": "Which allotrope of sulphur is stable below {96} °C?", "r": "Rhombic (alpha) sulphur",
     "w": ["Monoclinic (beta) sulphur", "Plastic sulphur", "Both are equally stable"],
     "e": ["Monoclinic sulphur is the stable form between about {96} °C and the melting point.",
           "Plastic sulphur is not stable at all: it slowly changes back to rhombic.",
           "Only one form is stable at a given temperature."],
     "y": "Below the transition temperature of about {96} °C, rhombic sulphur is the stable form."},
    {"q": "What shape are the crystals of monoclinic sulphur?", "r": "Long needle-shaped crystals",
     "w": ["Octahedral crystals", "Cubes", "It has no crystals at all"],
     "e": ["Octahedral crystals are the rhombic form.",
           "Neither allotrope of sulphur forms cubes.",
           "Monoclinic sulphur does form crystals; it is plastic sulphur that has none."],
     "y": "Monoclinic sulphur grows as needles, while rhombic sulphur grows as octahedral crystals."},
    {"q": "In which liquid does sulphur dissolve?", "r": "Carbon disulphide",
     "w": ["Water", "Dilute hydrochloric acid", "Ethanol, very readily"],
     "e": ["Sulphur is insoluble in water.",
           "Sulphur does not react with or dissolve in dilute acids.",
           "Sulphur is only very slightly soluble in ethanol."],
     "y": "Sulphur is insoluble in water but dissolves well in carbon disulphide, which is how rhombic crystals are grown."},
    {"q": "What is seen when sulphur burns in air?", "r": "A blue flame, giving a colourless gas with a choking smell",
     "w": ["A bright white flame, giving a white solid", "A yellow flame, giving a black solid",
           "No reaction takes place"],
     "e": ["A bright white flame with a white solid is burning magnesium.",
           "A black solid is not formed; the product is a gas.",
           "Sulphur burns readily when heated in air."],
     "y": "Sulphur burns with a blue flame to give sulphur dioxide: S + {formula('O2')} → {formula('SO2')}."},
    {"q": "How is plastic sulphur made?", "r": "By pouring boiling sulphur into cold water",
     "w": ["By cooling molten sulphur very slowly", "By dissolving sulphur in carbon disulphide and evaporating",
           "By heating sulphur gently to just above its melting point"],
     "e": ["Slow cooling gives crystals, not the plastic form.",
           "That method grows rhombic crystals.",
           "Gentle melting gives a runny amber liquid, which sets back to a crystalline form."],
     "y": "Sudden cooling traps long chains of sulphur atoms, giving a brown rubbery solid that is not crystalline."},
]

BURN = [
    {"q": 'Sulphur is heated in a deflagrating spoon and lowered into a gas jar of air. What is seen and formed?', "r": "A blue flame, forming sulphur dioxide, {formula('SO2')}",
     "w": ["A yellow flame, forming sulphur trioxide, {formula('SO3')}", 'A white flame, forming a white solid', 'Nothing happens'],
     "e": ["{formula('SO3')} is made in the Contact process with a catalyst, not by burning sulphur in air.", 'The product is a gas, not a solid.', 'Heated sulphur burns in air with a clearly visible flame.'],
     "y": "S + {formula('O2')} → {formula('SO2')}, with a blue flame and a choking smell."},
    {"q": 'Iron filings and sulphur are heated together. What is formed?', "r": "Iron(II) sulphide, {formula('FeS')}, a black solid",
     "w": ['A mixture of iron and sulphur, unchanged', "Iron(II) sulphate, {formula('FeSO4')}", 'Iron and sulphur dioxide'],
     "e": ['Heating makes them react; the product cannot be separated with a magnet.', 'No oxygen is present, so no sulphate can form.', "No oxygen is present, so no {formula('SO2')} can form."],
     "y": "Fe + S → {formula('FeS')}: sulphur combines with many metals when heated."},
    {"q": 'What does sulphur do with dilute hydrochloric acid?', "r": 'Nothing: sulphur does not react with dilute acids',
     "w": ['It gives off hydrogen', 'It gives off hydrogen sulphide', 'It dissolves to give a yellow solution'],
     "e": ['Only metals above hydrogen give off hydrogen with a dilute acid.', 'That happens with a metal SULPHIDE, not with sulphur itself.', 'Sulphur is insoluble and unreactive towards dilute acids.'],
     "y": 'Sulphur reacts with hot concentrated acids, but not with dilute ones.'},
    {"q": 'Why is a deflagrating spoon used to burn sulphur in a gas jar?', "r": 'It holds the burning sulphur safely in the jar while the gas collects',
     "w": ['It makes the sulphur burn more brightly', 'It stops the sulphur from melting', 'It dries the gas as it forms'],
     "e": ['The brightness depends on the sulphur and the air, not on the spoon.', 'The sulphur melts before it burns; the spoon holds the molten sulphur.', 'The spoon does not dry anything.'],
     "y": 'The long handle lets the burning sulphur be lowered into the jar and taken out safely.'},
]

WHYALLO = [
    {"q": 'Rhombic and monoclinic sulphur are both pure sulphur, yet their densities and crystal shapes differ. Why?', "r": 'The same atoms are packed in a different arrangement in each crystal',
     "w": ['They contain different numbers of neutrons', 'One of them contains a little oxygen', 'They are different elements'],
     "e": ['Different numbers of neutrons give isotopes, which have the same crystal forms.', 'Both allotropes are pure sulphur; neither contains oxygen.', 'Allotropes are forms of ONE element, not different elements.'],
     "y": 'Both are rings of {8} sulphur atoms, but the rings are stacked differently.'},
    {"q": 'Monoclinic sulphur is left at room temperature for several weeks. What happens?', "r": 'It slowly changes into rhombic sulphur, the stable form below {96} °C',
     "w": ['It stays monoclinic for ever', 'It changes into plastic sulphur', 'It melts'],
     "e": ['Below the transition temperature the monoclinic form is not stable.', 'Plastic sulphur comes from pouring boiling sulphur into cold water.', 'Sulphur melts at about {115} °C, far above room temperature.'],
     "y": 'An allotrope changes into whichever form is stable at that temperature, though slowly.'},
    {"q": 'How are crystals of rhombic sulphur grown in the laboratory?', "r": 'By dissolving sulphur in carbon disulphide and letting the liquid evaporate slowly',
     "w": ['By dissolving sulphur in hot water and cooling it', 'By pouring boiling sulphur into cold water', 'By heating sulphur until it glows'],
     "e": ['Sulphur is insoluble in water, so no solution can be made.', 'That gives plastic sulphur, which has no crystals.', 'Heating alone does not grow crystals.'],
     "y": 'As the solvent evaporates below {96} °C, octahedral rhombic crystals are left.'},
    {"q": 'Why does plastic sulphur slowly harden and turn yellow again?', "r": 'The long chains of atoms slowly rearrange into stable rhombic crystals',
     "w": ['It takes in oxygen from the air', 'It loses water', 'It reacts with the carbon dioxide in air'],
     "e": ['No oxygen is taken in; the element stays pure sulphur.', 'There is no water in plastic sulphur to lose.', 'Sulphur does not react with carbon dioxide.'],
     "y": 'Plastic sulphur is unstable, so its atoms return to the arrangement of the stable rhombic form.'},
]

L.lesson(D, S, 2, ("k4-2", "Describe the physical and chemical properties of sulphur and its allotropes"), [1],
  "Sulphur is a brittle yellow solid, insoluble in water, soluble in carbon disulphide, and a poor conductor of heat and electricity.\n"
  "Allotropes are different forms of the same element in the same physical state. Sulphur has two crystalline allotropes:\n"
  "• Rhombic (alpha) sulphur: octahedral crystals, stable below about 96 °C, density 2.07 g/cm³.\n"
  "• Monoclinic (beta) sulphur: needle-shaped crystals, stable between about 96 °C and the melting point, density 1.98 g/cm³.\n"
  "96 °C is the transition temperature. Plastic sulphur, a brown rubbery form made by pouring boiling sulphur into cold water, "
  "is not crystalline and slowly changes back to rhombic sulphur.\n"
  "Chemically, sulphur burns in air with a blue flame to sulphur dioxide, and combines with many metals on heating to form sulphides.",
  worked({"t": 96},
         "A sample of sulphur is kept at {t - 20} °C for several days and then at {t + 10} °C for several days. Name the stable form in each case.",
         ["The transition temperature is about {t} °C.",
          "Below {t} °C the stable form is rhombic (alpha) sulphur, with octahedral crystals.",
          "Between {t} °C and the melting point the stable form is monoclinic (beta) sulphur, with needle-shaped crystals.",
          "{t - 20} °C is below {t} °C, and {t + 10} °C is above it."],
         "rhombic at {t - 20} °C and monoclinic at {t + 10} °C",
         checks=["t == 96"]),
  [card("c4k2-1", "Allotropes are different forms of the same element in the same state.",
        ["rhombic and monoclinic sulphur are both pure solid sulphur"], "k4-2-allo"),
   card("c4k2-2", "Rhombic sulphur is stable below about {96} °C; monoclinic above it.",
        ["{96} °C is the transition temperature"], "k4-2-stable"),
   card("c4k2-3", "Sulphur burns in air with a blue flame to give sulphur dioxide.",
        ["S + {formula('O2')} → {formula('SO2')}"], "k4-2-burn")],
  [bank("k4-2-allo", 1, "{X.q}", ALLO, SRC),
   mcq("k4-2-stable", 1, "Which form of sulphur is stable at {t} °C?",
       "{t < 96 ? 'Rhombic (alpha) sulphur' : 'Monoclinic (beta) sulphur'}",
       [("{t < 96 ? 'Monoclinic (beta) sulphur' : 'Rhombic (alpha) sulphur'}", "swap"),
        ("Plastic sulphur", "plastic"), ("Neither: sulphur is liquid at that temperature", "liquid")],
       ["The transition temperature is about {96} °C.",
        "{t} °C is {t < 96 ? 'below' : 'above'} it, and the melting point is about {115} °C.", "So the answer is: {answer}."],
       vars={"t": {"pick": [20, 25, 40, 60, 80, 90, 100, 105, 110, 112]}},
       misc=[("swap", "Rhombic is stable BELOW about {96} °C and monoclinic above it, up to the melting point."),
             ("plastic", "Plastic sulphur is never the stable form: it slowly changes back to rhombic."),
             ("liquid", "Sulphur melts at about {115} °C, so at {t} °C it is still solid.")],
       sources=SRC),
   match("k4-2-match", 2, "Match each quantity to its value for sulphur.",
         [("Shape of rhombic crystals", "Octahedral"), ("Shape of monoclinic crystals", "Needles"),
          ("Density of rhombic sulphur", "{2.07} g/cm³"), ("Density of monoclinic sulphur", "{1.98} g/cm³"),
          ("Transition temperature", "About {96} °C"), ("Melting point", "About {115} °C")],
         pick=3, sources=SRC),
   bank("k4-2-burn", 2, "{X.q}", BURN, SRC),
   bank("k4-2-why", 3, "{X.q}", WHYALLO, SRC)],
  learn=learn(
    [goal("describe the properties of sulphur and tell its allotropes apart by crystal shape, stability and density.",
          "Lesson {1} (where sulphur comes from) and Form Three structure and bonding.",
          "Lessons {3} to {8}, which deal with the compounds sulphur forms."),
     ("Physical properties and allotropes",
      "Sulphur is a brittle yellow solid. It is insoluble in water, dissolves in carbon disulphide, does not conduct "
      "electricity, and melts at about {115} °C.\n"
      "Allotropes are different forms of the same element in the same physical state. Sulphur has two crystalline forms:\n"
      "• Rhombic (alpha): octahedral crystals, density {2.07} g/cm³, stable below about {96} °C. Grown by letting carbon "
      "disulphide evaporate from a solution of sulphur.\n"
      "• Monoclinic (beta): needle-shaped crystals, density {1.98} g/cm³, stable between about {96} °C and the melting point. "
      "Grown by letting molten sulphur cool slowly and pouring off the liquid left.\n"
      "About {96} °C is the transition temperature, where one form changes into the other."),
     ("Plastic sulphur and chemical properties",
      "If boiling sulphur is poured into cold water it sets as plastic sulphur: a brown rubbery solid with no crystals. "
      "It is unstable and slowly turns back into rhombic sulphur.\n"
      "Chemically, sulphur:\n"
      "• burns in air with a blue flame to sulphur dioxide: S + {formula('O2')} → {formula('SO2')};\n"
      "• combines with many metals on heating to give sulphides: Fe + S → {formula('FeS')};\n"
      "• is oxidised by hot concentrated sulphuric acid and by hot concentrated nitric acid.\n"
      "It does not react with water or with dilute acids.")],
    key_words=[("allotropes", "different forms of the same element in the same physical state"),
               ("rhombic sulphur", "the octahedral form, stable below about {96} °C"),
               ("monoclinic sulphur", "the needle-shaped form, stable above about {96} °C"),
               ("transition temperature", "the temperature at which one allotrope changes into the other")],
    examples=["rhombic: octahedral, {2.07} g/cm³", "monoclinic: needles, {1.98} g/cm³", "S + {formula('O2')} → {formula('SO2')}"],
    mistake=("rhombic and monoclinic sulphur are isotopes of sulphur", "they are allotropes",
             "Isotopes differ in the nucleus. Allotropes differ in how the same atoms are arranged.")))

# ---------------------------------------------------------------- 3. Lab preparation and physical properties of SO2
SO2PREP = [
    {"q": "Which reagents are used to prepare sulphur dioxide in the laboratory?", "r": "Sodium sulphite and dilute hydrochloric acid",
     "w": ["Sodium sulphate and dilute hydrochloric acid", "Sodium sulphide and dilute hydrochloric acid",
           "Sodium carbonate and dilute hydrochloric acid"],
     "e": ["A sulphate does not give off {formula('SO2')} with a dilute acid; a sulphite does.",
           "A sulphide gives hydrogen sulphide, {formula('H2S')}, not {formula('SO2')}.",
           "A carbonate gives carbon dioxide."],
     "y": "{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}."},
    {"q": "How is sulphur dioxide collected?", "r": "By downward delivery, because it is denser than air",
     "w": ["By downward displacement of water", "Over water", "By upward delivery, because it is less dense than air"],
     "e": ["{formula('SO2')} is very soluble in water, so it cannot be collected over or through water.",
           "It would dissolve in the water.",
           "Its relative molecular mass is {64}, well above the average for air, so it is denser."],
     "y": "A dense, very soluble gas is collected by downward delivery into a dry gas jar."},
    {"q": "Which drying agent is used for sulphur dioxide?", "r": "Concentrated sulphuric acid",
     "w": ["Quicklime, {formula('CaO')}", "Sodium hydroxide pellets", "Water"],
     "e": ["Quicklime is basic and would react with the acidic gas.",
           "Sodium hydroxide is a base and would absorb the gas.",
           "Water dissolves the gas instead of drying it."],
     "y": "An acidic gas is dried with concentrated sulphuric acid, which does not react with it."},
    {"q": "What is the smell and colour of sulphur dioxide?", "r": "Colourless, with a sharp choking smell",
     "w": ["Brown, with a choking smell", "Colourless, with a smell of rotten eggs", "Yellow and odourless"],
     "e": ["Brown is the colour of nitrogen dioxide.",
           "Rotten eggs is the smell of hydrogen sulphide.",
           "Sulphur dioxide is colourless and certainly not odourless."],
     "y": "{formula('SO2')} is a colourless, poisonous gas with a sharp choking smell."},
    {"q": "Why must sulphur dioxide be prepared in a fume cupboard?", "r": "It is poisonous and irritates the eyes and lungs",
     "w": ["It catches fire easily", "It explodes on contact with air", "It is only a nuisance because of its colour"],
     "e": ["Sulphur dioxide does not burn; it is itself a product of burning.",
           "It does not explode in air.",
           "The gas is colourless; the danger is that it is poisonous."],
     "y": "Breathing it in damages the lungs, so it must be used where the fumes can be drawn away."},
]

DRYING = [
    {"q": "Why is quicklime, {formula('CaO')}, not used to dry sulphur dioxide?", "r": 'Quicklime is basic and reacts with the acidic gas',
     "w": ['Quicklime is not a drying agent at all', 'Quicklime would make the gas wetter', 'Quicklime dissolves the gas in water'],
     "e": ['Quicklime IS a drying agent; it is used for ammonia. The problem here is that it reacts.', 'A drying agent removes water; quicklime does not add any.', 'Quicklime reacts with the gas; it does not dissolve it in water.'],
     "y": 'An acidic gas must be dried with an acidic drying agent, such as concentrated sulphuric acid.'},
    {"q": 'Which drying agent is used for ammonia, and why?', "r": 'Quicklime, because ammonia is alkaline and would react with an acidic drying agent',
     "w": ['Concentrated sulphuric acid, because it dries every gas', 'Water, because ammonia dissolves in it', 'No drying agent can be used with ammonia'],
     "e": ['Concentrated sulphuric acid reacts with ammonia to give ammonium sulphate.', 'Water dissolves ammonia instead of drying it.', 'Quicklime dries it well.'],
     "y": 'A drying agent must not react with the gas: a basic gas needs a basic drying agent.'},
    {"q": 'A gas is passed through a wash bottle of concentrated sulphuric acid. What is this for?', "r": 'To remove water vapour from the gas',
     "w": ['To cool the gas', 'To make the gas more soluble', 'To change the gas into an acid'],
     "e": ['Cooling is not the purpose, and the acid does not cool the gas.', 'Drying does not change how soluble the gas is.', 'The acid does not react with a gas it is used to dry.'],
     "y": 'Concentrated sulphuric acid takes up water strongly, which is why it is a drying agent.'},
    {"q": 'Why must the gas jar be dry when sulphur dioxide is collected?', "r": 'The gas is very soluble, so any water in the jar would dissolve some of it',
     "w": ['Water would make the gas explode', 'A wet jar would crack', 'Water would turn the gas brown'],
     "e": ['Sulphur dioxide does not explode with water; it dissolves.', 'The jar does not crack; the problem is loss of the gas.', 'Sulphur dioxide stays colourless in water; it forms sulphurous acid.'],
     "y": "{formula('SO2')} is very soluble in water, so a wet jar would hold less gas."},
]

L.lesson(D, S, 3, ("k4-3", "Prepare sulphur dioxide in the laboratory and state its physical properties"), [2],
  "Laboratory preparation: a sulphite and a dilute acid.\n"
  "Na2SO3 + 2HCl → 2NaCl + H2O + SO2\n"
  "The acid is added to sodium sulphite in a flask; the gas is dried by passing it through concentrated sulphuric acid, "
  "and collected by downward delivery into a dry gas jar, because it is denser than air and very soluble in water.\n"
  "Sulphur dioxide can also be made by burning sulphur in air, or by heating copper with concentrated sulphuric acid.\n"
  "Physical properties: a colourless, poisonous gas with a sharp choking smell; denser than air (relative molecular mass 64); "
  "very soluble in water, giving an acidic solution; easily liquefied. It must be made in a fume cupboard.",
  worked({"m": 12.6},
         "Write the equation for the laboratory preparation of sulphur dioxide from sodium sulphite and dilute hydrochloric acid, and name the drying agent.",
         ["A sulphite and a dilute acid give a salt, water and sulphur dioxide.",
          "{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}.",
          "Sulphur dioxide is an acidic gas, so it is dried with concentrated sulphuric acid, which does not react with it."],
         "{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}; dried with concentrated {formula('H2SO4')}",
         checks=[]),
  [card("c4k3-1", "A sulphite with a dilute acid gives sulphur dioxide.",
        ["{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}"], "k4-3-prep"),
   card("c4k3-2", "{formula('SO2')} is denser than air and very soluble, so it is collected by downward delivery.",
        ["relative molecular mass {64}, well above the average for air"], "k4-3-collect"),
   card("c4k3-3", "An acidic gas is dried with concentrated sulphuric acid, never with a base.",
        ["quicklime would react with {formula('SO2')}"], "k4-3-dry")],
  [bank("k4-3-prep", 1, "{X.q}", SO2PREP, SRC),
   num("k4-3-mass", 2, "Find the relative molecular mass of {formula(F)}.",
       "molarMass(F)",
       ["Add the relative atomic mass of every atom in the formula.",
        "{formula(F)} has {totalAtoms(F)} atoms in all.", "The relative molecular mass is {answer}."],
       vars={"F": {"pick": ["SO2", "SO3", "H2S", "H2SO4", "H2SO3", "Na2SO3", "CaSO4", "FeS"]}},
       misc=[("atoms", "totalAtoms(F)", "{totalAtoms(F)} is the NUMBER of atoms; the mass adds their relative atomic masses."),
             ("elements", "elementCount(F)", "Count the mass of every atom, not the number of different elements.")],
       sources=SRC),
   mcq("k4-3-collect", 1, "How should the gas {G.f} be collected?",
       "{G.r}", [("{G.w1}", "w1"), ("{G.w2}", "w2"), ("{G.w3}", "w3")],
       ["{G.y}", "So the answer is: {answer}."],
       vars={"G": {"pick": [
           {"f": "sulphur dioxide", "r": "By downward delivery, because it is denser than air and very soluble in water",
            "w1": "Over water", "w2": "By upward delivery", "w3": "In a balloon held over the flask",
            "y": "{formula('SO2')} has a relative molecular mass of {64} and dissolves readily in water."},
           {"f": "hydrogen sulphide", "r": "By downward delivery, because it is denser than air",
            "w1": "By upward delivery", "w2": "Over water in an open trough", "w3": "It cannot be collected at all",
            "y": "{formula('H2S')} has a relative molecular mass of {34}, greater than the average for air."},
           {"f": "ammonia", "r": "By upward delivery, because it is less dense than air and very soluble in water",
            "w1": "By downward delivery", "w2": "Over water", "w3": "Over mercury only",
            "y": "{formula('NH3')} has a relative molecular mass of {17}, well below the average for air."}]}},
       misc=[("w1", "{G.y}"), ("w2", "{G.y}"), ("w3", "{G.y}")],
       sources=SRC),
   bank("k4-3-dry", 2, "{X.q}", DRYING, SRC),
   order("k4-3-steps", 3, "{A.q}",
         ["{A.s[0]}", "{A.s[1]}", "{A.s[2]}", "{A.s[3]}", "{A.s[4]}"],
         vars={"A": {"pick": [
             {"q": "Put the steps of preparing a dry jar of sulphur dioxide in order.",
              "s": ["Place sodium sulphite in the flask and set up the apparatus in a fume cupboard",
                    "Add dilute hydrochloric acid from the thistle funnel",
                    "Pass the gas given off through concentrated sulphuric acid to dry it",
                    "Lead the dry gas to the bottom of a dry gas jar by downward delivery",
                    "Cover the full jar with a greased glass plate"]},
             {"q": "Put the path of the gas through the apparatus in order, from where it is made.",
              "s": ["The gas is given off in the reaction flask",
                    "It passes along the delivery tube",
                    "It bubbles through the concentrated sulphuric acid in the wash bottle",
                    "It leaves the wash bottle dry",
                    "It sinks to the bottom of the gas jar"]},
             {"q": "Put the steps of testing a jar of sulphur dioxide in order.",
              "s": ["Lift the glass plate a little and smell the gas carefully by wafting",
                    "Note the sharp choking smell",
                    "Lower in a piece of damp blue litmus paper",
                    "Note that the litmus turns red",
                    "Note that the red colour is then bleached away"]}]}},
         sources=SRC)],
  learn=learn(
    [goal("write the equation for preparing sulphur dioxide, explain how it is dried and collected, and state its physical properties.",
          "Lesson {2} (sulphur burns to {formula('SO2')}) and Form Three gas collection.",
          "Lesson {4} (the chemical properties of {formula('SO2')}) and the Contact process."),
     ("Preparation",
      "In the laboratory, sulphur dioxide is made from a sulphite and a dilute acid:\n"
      "{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}\n"
      "The dilute acid is run onto sodium sulphite in a flask. The gas is led through a wash bottle of concentrated "
      "sulphuric acid, which dries it without reacting, and then down into a dry gas jar.\n"
      "It can also be made by burning sulphur in air, or by heating copper with concentrated sulphuric acid:\n"
      "Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}."),
     ("Physical properties and collection",
      "Sulphur dioxide is a colourless gas with a sharp choking smell. It is poisonous, so it must be prepared in a fume cupboard.\n"
      "Its relative molecular mass is {32} + {2} × {16} = {64}, well above the average for air, so it is denser than air.\n"
      "It is very soluble in water, giving an acidic solution of sulphurous acid.\n"
      "Being dense and very soluble, it is collected by downward delivery into a dry gas jar: not over water, which would "
      "dissolve it.\n"
      "It is easily turned to a liquid by pressure, which is how it is stored and transported.")],
    key_words=[("sulphite", "a salt containing the {formula('SO3')} ion with a {2}− charge, such as {formula('Na2SO3')}"),
               ("downward delivery", "collecting a dense gas by leading it to the bottom of a jar"),
               ("drying agent", "a substance that removes water from a gas without reacting with it"),
               ("fume cupboard", "a cabinet that draws harmful fumes away")],
    examples=["{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}", "RMM of {formula('SO2')} = {64}"],
    mistake=("sulphur dioxide is collected over water", "it is collected by downward delivery",
             "{formula('SO2')} is very soluble in water, so collecting it over water would lose the gas.")))

# ---------------------------------------------------------------- 4. Chemical properties of SO2
SO2CHEM = [
    {"q": "What does sulphur dioxide form when it dissolves in water?", "r": "Sulphurous acid, {formula('H2SO3')}",
     "w": ["Sulphuric acid, {formula('H2SO4')}", "Hydrogen sulphide, {formula('H2S')}", "A neutral solution"],
     "e": ["Sulphuric acid comes from sulphur TRIoxide dissolving in water.",
           "Hydrogen sulphide is a different compound, made from a sulphide and an acid.",
           "The solution turns blue litmus red, so it is acidic."],
     "y": "{formula('SO2')} + {formula('H2O')} → {formula('H2SO3')}: an acidic oxide gives an acid."},
    {"q": "What happens when sulphur dioxide is bubbled into acidified potassium manganate(VII) solution?",
     "r": "The purple colour disappears, because the {formula('SO2')} reduces it",
     "w": ["The solution turns a deeper purple", "The solution turns brown", "Nothing happens"],
     "e": ["Reduction removes the purple colour; it does not deepen it.",
           "Brown is what happens with bromine water, not with manganate(VII).",
           "The colour change is clear and is used as a test."],
     "y": "{formula('SO2')} is a reducing agent: it is itself oxidised to a sulphate while the purple ion is reduced."},
    {"q": "Why is the bleaching by sulphur dioxide called temporary?", "r": "The colour slowly returns as air oxidises the bleached material",
     "w": ["The bleaching only works in the dark", "The material is destroyed rather than bleached",
           "It only works on cotton"],
     "e": ["Light is not what undoes it; oxygen from the air is.",
           "The material is not destroyed; its colour is removed and then returns.",
           "It works on wool, silk, straw and paper as well."],
     "y": "{formula('SO2')} bleaches by reduction, and oxygen in the air slowly reverses the change."},
    {"q": "How does bleaching by sulphur dioxide differ from bleaching by chlorine?", "r": "Sulphur dioxide bleaches by reduction; chlorine bleaches by oxidation",
     "w": ["Both bleach by oxidation", "Both bleach by reduction", "Sulphur dioxide bleaches by oxidation and chlorine by reduction"],
     "e": ["Chlorine bleaches by oxidation, but sulphur dioxide does not.",
           "Chlorine is an oxidising bleach, not a reducing one.",
           "It is the other way round."],
     "y": "That is why the bleaching by {formula('SO2')} is temporary and that by chlorine is permanent."},
    {"q": "Sulphur dioxide is bubbled through hydrogen sulphide. What is seen?", "r": "A yellow deposit of sulphur forms",
     "w": ["A white precipitate forms", "The mixture turns blue", "No change is seen"],
     "e": ["No white precipitate is formed in this reaction.",
           "No blue colour appears.",
           "A pale yellow solid appears clearly."],
     "y": "{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}: here {formula('SO2')} acts as the oxidising agent."},
    {"q": "Which gas is mainly responsible for acid rain from burning coal?", "r": "Sulphur dioxide",
     "w": ["Carbon dioxide", "Nitrogen", "Oxygen"],
     "e": ["Carbon dioxide makes rain only very slightly acidic; it is not the main cause of acid rain.",
           "Nitrogen in the air is unreactive and does not itself cause acid rain.",
           "Oxygen is neutral."],
     "y": "{formula('SO2')} from the sulphur in coal dissolves in rain and is oxidised to sulphuric acid."},
]

BLEACH = [
    {"q": 'A red flower is held in moist sulphur dioxide and loses its colour. It is then left in the air for some days. What happens?', "r": "The colour slowly returns, because the bleaching by {formula('SO2')} is temporary",
     "w": ['The flower stays white for ever', 'The flower turns black', 'The colour returns at once'],
     "e": ['Permanent bleaching is what chlorine does, by oxidation.', 'Blackening is what concentrated sulphuric acid does to sugar, by dehydration.', 'The change back takes days, because oxidation by air is slow.'],
     "y": "{formula('SO2')} bleaches by reduction, and oxygen in the air slowly reverses it."},
    {"q": 'Why must the material be moist for sulphur dioxide to bleach it?', "r": 'The gas must dissolve in the water to act on the colouring matter',
     "w": ['Water is what does the bleaching', 'Dry material would catch fire', 'The water washes the colour away'],
     "e": ['Water alone does not remove the colour of a flower.', 'Nothing catches fire in this test.', 'Washing is not the effect: the colour is removed chemically, and later returns.'],
     "y": 'Moisture lets the gas form sulphurous acid at the surface, and that is the reducing agent.'},
    {"q": 'Which bleach is used for cotton cloth, and why not sulphur dioxide?', "r": 'Chlorine or a chlorine compound, because its bleaching is permanent',
     "w": ['Sulphur dioxide, because it is cheaper', 'Neither: cotton cannot be bleached', 'Sulphur dioxide, because it is permanent'],
     "e": ['Cheapness does not help if the colour returns.', 'Cotton is bleached in large amounts in industry.', "Bleaching by {formula('SO2')} is temporary, not permanent."],
     "y": 'Chlorine bleaches by oxidation, which the air cannot reverse; sulphur dioxide bleaches by reduction.'},
    {"q": 'Why is sulphur dioxide still used to bleach straw, wool and paper?', "r": 'Chlorine would attack and weaken those materials, while sulphur dioxide does not',
     "w": ['It is the only bleach that works on them', 'It makes them stronger', "Its bleaching lasts longer than chlorine's"],
     "e": ['Other bleaches exist, but they damage these materials.', 'Bleaching does not strengthen a material.', 'Its bleaching lasts a shorter time, not longer.'],
     "y": 'A gentle reducing bleach is chosen where an oxidising bleach would damage the fibres.'},
]

L.lesson(D, S, 4, ("k4-4", "Describe the chemical properties of sulphur dioxide"), [3],
  "Sulphur dioxide is an acidic oxide, a reducing agent and a bleaching agent.\n"
  "• Acidic oxide: SO2 + H2O → H2SO3 (sulphurous acid), which turns blue litmus red. With alkalis it gives sulphites: "
  "SO2 + 2NaOH → Na2SO3 + H2O.\n"
  "• Reducing agent: it decolourises acidified potassium manganate(VII) (purple to colourless) and turns acidified potassium "
  "dichromate(VI) from orange to green. It also decolourises bromine water.\n"
  "• Bleaching agent: it bleaches by reduction, so the bleaching is temporary; the colour slowly returns as air oxidises the material. "
  "Chlorine bleaches by oxidation and is permanent.\n"
  "• As an oxidising agent with a stronger reducing agent: SO2 + 2H2S → 3S + 2H2O, giving a yellow deposit of sulphur.\n"
  "In the air, SO2 is oxidised to SO3 and dissolves in rain as sulphuric acid: this is acid rain.",
  worked({"z": 1},
         "Explain, with an equation, what is seen when sulphur dioxide is bubbled through acidified potassium manganate(VII) solution.",
         ["Acidified potassium manganate(VII) solution is purple.",
          "Sulphur dioxide is a reducing agent, so it reduces the manganate(VII) ion.",
          "The purple colour disappears and the solution becomes colourless.",
          "The {formula('SO2')} is itself oxidised to sulphate: it gains oxygen from the oxidising agent."],
         "the purple colour disappears, because {formula('SO2')} reduces the manganate(VII)",
         checks=[]),
  [card("c4k4-1", "{formula('SO2')} is an acidic oxide: with water it gives sulphurous acid, with alkalis sulphites.",
        ["{formula('SO2')} + {formula('H2O')} → {formula('H2SO3')}"], "k4-4-chem"),
   card("c4k4-2", "{formula('SO2')} is a reducing agent: purple manganate(VII) goes colourless, orange dichromate(VI) goes green.",
        ["it is itself oxidised to a sulphate"], "k4-4-reduce"),
   card("c4k4-3", "{formula('SO2')} bleaches by reduction, so the bleaching is temporary.",
        ["the colour returns as air oxidises the material again"], "k4-4-bleach")],
  [bank("k4-4-chem", 1, "{X.q}", SO2CHEM, SRC),
   mcq("k4-4-reduce", 2, "What is seen when sulphur dioxide is bubbled through {T.n}?",
       "{T.r}", [("{T.w1}", "w1"), ("{T.w2}", "w2"), ("{T.w3}", "w3")],
       ["{T.y}", "So the answer is: {answer}."],
       vars={"T": {"pick": [
           {"n": "acidified potassium manganate(VII) solution", "r": "The purple colour disappears",
            "w1": "The solution turns purple from colourless", "w2": "A yellow solid appears", "w3": "The solution turns green",
            "y": "{formula('SO2')} reduces the purple manganate(VII) ion to a colourless one."},
           {"n": "acidified potassium dichromate(VI) solution", "r": "The orange colour changes to green",
            "w1": "The orange colour changes to purple", "w2": "The solution stays orange", "w3": "A white precipitate forms",
            "y": "{formula('SO2')} reduces the orange dichromate(VI) ion to the green chromium(III) ion."},
           {"n": "bromine water", "r": "The brown colour of the bromine water disappears",
            "w1": "The solution turns brown from colourless", "w2": "A yellow solid appears", "w3": "The solution turns blue",
            "y": "{formula('SO2')} reduces the bromine to colourless bromide ions."},
           {"n": "hydrogen sulphide", "r": "A yellow deposit of sulphur forms",
            "w1": "The mixture turns purple", "w2": "A white precipitate forms", "w3": "Nothing is seen",
            "y": "Here {formula('SO2')} is the OXIDISING agent: {formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}."}]}},
       misc=[("w1", "{T.y}"), ("w2", "{T.y}"), ("w3", "{T.y}")],
       sources=SRC),
   bank("k4-4-bleach", 2, "{X.q}", BLEACH, SRC),
   num("k4-4-vol", 2, "What volume of sulphur dioxide, in dm³ at s.t.p., is given off when {n} mol of sodium sulphite reacts completely with dilute hydrochloric acid?",
       "gasVolume(n)",
       ["{formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}.",
        "{1} mol of sulphite gives {1} mol of {formula('SO2')}, so {n} mol gives {n} mol.",
        "At s.t.p. {1} mol of any gas is {22.4} dm³, so the volume is {n} × {22.4} = {answer} dm³."],
       vars={"n": {"pick": [0.1, 0.2, 0.25, 0.5, 1, 1.5, 2]}},
       misc=[("double", "gasVolume(2 * n)", "The equation gives {1} mol of {formula('SO2')} for each {1} mol of sulphite, not {2}."),
             ("div", "volumeToMoles(n)", "Multiply the moles by {22.4} dm³/mol; do not divide.")],
       sources=SRC, unit="dm³"),
   match("k4-4-match", 3, "Match each observation to what is formed or seen.",
         [("{formula('SO2')} dissolved in water", "Sulphurous acid, {formula('H2SO3')}"),
          ("{formula('SO2')} passed into sodium hydroxide solution", "Sodium sulphite, {formula('Na2SO3')}"),
          ("{formula('SO2')} bubbled into acidified manganate(VII)", "The purple colour disappears"),
          ("{formula('SO2')} bubbled into acidified dichromate(VI)", "Orange changes to green"),
          ("{formula('SO2')} mixed with {formula('H2S')}", "A yellow deposit of sulphur")],
         pick=3, sources=SRC)],
  learn=learn(
    [goal("describe sulphur dioxide as an acidic oxide, a reducing agent, a bleach and sometimes an oxidising agent.",
          "Lesson {3} (preparing {formula('SO2')}) and Form Three acids, bases and redox.",
          "Lesson {8} (sulphuric acid) and the problem of acid rain."),
     ("An acidic oxide and a reducing agent",
      "Sulphur dioxide is the oxide of a non-metal, so it is acidic.\n"
      "• With water: {formula('SO2')} + {formula('H2O')} → {formula('H2SO3')}, sulphurous acid, which turns blue litmus red.\n"
      "• With an alkali: {formula('SO2')} + {2}{formula('NaOH')} → {formula('Na2SO3')} + {formula('H2O')}, giving a sulphite.\n"
      "It is also a good reducing agent, and the colour changes are used as tests:\n"
      "• acidified potassium manganate(VII): purple → colourless;\n"
      "• acidified potassium dichromate(VI): orange → green;\n"
      "• bromine water: brown → colourless.\n"
      "In each case the {formula('SO2')} is itself oxidised to a sulphate."),
     ("Bleaching, oxidising and acid rain",
      "Sulphur dioxide bleaches moist coloured materials such as flowers, straw, wool and paper. It does so by REDUCTION, "
      "so oxygen in the air slowly turns the colour back: the bleaching is temporary. Chlorine bleaches by oxidation, "
      "and that bleaching is permanent.\n"
      "With a stronger reducing agent, {formula('SO2')} is itself the oxidising agent:\n"
      "{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}, seen as a pale yellow deposit of sulphur.\n"
      "In the air, sulphur dioxide from burning coal and oil is oxidised and dissolves in rain as sulphuric acid. "
      "This acid rain damages buildings, kills fish in lakes and harms crops.")],
    key_words=[("acidic oxide", "an oxide that gives an acid with water and a salt with an alkali"),
               ("reducing agent", "a substance that removes oxygen from, or gives electrons to, another"),
               ("temporary bleach", "a bleach whose effect is slowly reversed by air"),
               ("acid rain", "rain made acidic by dissolved oxides of sulphur and nitrogen")],
    examples=["{formula('SO2')} + {formula('H2O')} → {formula('H2SO3')}", "purple → colourless with manganate(VII)", "{formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}"],
    mistake=("sulphur dioxide dissolves in water to give sulphuric acid", "it gives sulphurous acid, {formula('H2SO3')}",
             "Sulphuric acid, {formula('H2SO4')}, comes from sulphur TRIoxide, {formula('SO3')}.")))
