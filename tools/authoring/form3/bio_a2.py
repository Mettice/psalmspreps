"""Form 3 Biology, Term 1, rows 6-9 (diffusion, active transport, osmosis, practical, classification).
Run: python tools/authoring/form3/bio_a2.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "biology", "biology"

# ---------------------------------------------------------------- 6. Diffusion and active transport
SRC = ["transport"]
L.lesson(D, S, 6, ("b3-6", "Diffusion and active transport across cell membranes"), [2],
  "Diffusion: the net movement of particles from a region of higher concentration to a region of lower concentration, down a concentration gradient. It needs no energy from the cell.\n"
  "Examples: oxygen into blood in the lungs; carbon dioxide into a leaf; digested food into blood in the small intestine.\n"
  "Faster with: a steeper concentration gradient, higher temperature, larger surface area, shorter distance (thin surfaces).\n"
  "Small organisms have a large surface area to volume ratio, so diffusion alone can supply them.\n"
  "Active transport: movement of particles against a concentration gradient (low to high), using energy from respiration and carrier proteins. Examples: root hairs taking in mineral ions from dilute soil water; glucose absorption in the gut.",
  worked({"l": 2},
         "Find the surface area to volume ratio of a cube of side {l} cm.",
         ["Surface area = {6} × {l}² = {6 * l * l} cm².", "Volume = {l}³ = {l * l * l} cm³.", "Ratio = {6 * l * l} ÷ {l * l * l} = {6 / l} : {1}."],
         "{6 / l} : {1}", checks=["6 / l == 3"]),
  [card("c3b6-1", "Diffusion: from high to low concentration, with no energy needed.",
        ["Oxygen diffuses from the air sacs into the blood."], "b3-6-def"),
   card("c3b6-2", "Active transport: from low to high concentration, using energy.",
        ["Root hairs take in nitrate ions from dilute soil water."], "b3-6-active"),
   card("c3b6-3", "Smaller objects have a larger surface area to volume ratio.",
        ["Cube of side {1} cm: {6} : {1}; side {3} cm: {2} : {1}"], "b3-6-ratio")],
  [bank("b3-6-def", 1, "{X.q}", [
     {"q": "What is diffusion?", "r": "Net movement of particles from high to low concentration", "w": ["Movement of water only, through a membrane", "Movement from low to high concentration using energy", "Movement of particles that stops at once"],
      "e": ["That describes osmosis.", "That is active transport.", "Particles keep moving."], "y": "Particles spread down the concentration gradient."},
     {"q": "Which is an example of diffusion?", "r": "Oxygen moving from the air sacs into the blood", "w": ["A root hair taking up ions from dilute soil water", "Food moving down the gut by muscle contraction", "Blood pumped by the heart"],
      "e": ["That is against the gradient: active transport.", "That is peristalsis.", "That is pumping (mass flow)."], "y": "Oxygen is more concentrated in the air sacs than in the blood arriving."},
     {"q": "Does diffusion need energy from respiration?", "r": "No: particles move by their own random motion", "w": ["Yes, always", "Only in plants", "Only in animals"],
      "e": ["It is passive.", "It is passive in all organisms.", "It is passive in all organisms."], "y": "Diffusion is a passive process."}], SRC),
   bank("b3-6-active", 1, "{X.q}", [
     {"q": "Why do root hair cells need active transport to take in mineral ions?", "r": "The ions are more concentrated inside the cell than in the soil water", "w": ["Ions cannot dissolve in water", "Soil has no ions", "Diffusion is faster"],
      "e": ["Ions are dissolved in soil water.", "Soil water contains dilute ions.", "Diffusion would carry ions out, not in."], "y": "Moving against the gradient needs energy."},
     {"q": "Where does the energy for active transport come from?", "r": "respiration in the cell's mitochondria", "w": ["the sun directly", "diffusion", "the cell wall"],
      "e": ["Sunlight is used in photosynthesis.", "Diffusion releases no usable energy.", "The cell wall does not supply energy."], "y": "Respiration releases the energy carriers use."},
     {"q": "A poison stops respiration in root cells. What happens to the uptake of mineral ions?", "r": "It falls, because active transport stops", "w": ["It rises", "It stays the same", "Only water uptake stops"],
      "e": ["Without energy, carriers cannot work.", "It needs energy.", "Mineral uptake is the process that needs energy."], "y": "No respiration, no energy for active transport."}], SRC),
   num("b3-6-ratio", 2, "Find the surface area to volume ratio of a cube of side {l} cm. Give the first number of the ratio n : {1}.", "roundTo(6 / l, 0.01)",
       ["Surface area = {6} × {l}² = {6 * l * l} cm²; volume = {l}³ = {l * l * l} cm³.", "Ratio = {6 * l * l} ÷ {l * l * l} = {answer} : {1}."],
       vars={"l": {"int": [1, 6]}},
       misc=[("flip", "roundTo(l / 6, 0.01)", "Surface area ÷ volume, not volume ÷ surface area."), ("area", "6 * l * l", "Divide by the volume as well.")],
       sources=SRC, where=["l != 6"]),
   bank("b3-6-rate", 3, "{X.q}", [
     {"q": "Which change makes diffusion of oxygen into the blood faster?", "r": "a thinner wall between air and blood", "w": ["a thicker wall", "a smaller surface area", "a lower concentration of oxygen in the air sacs"],
      "e": ["A thicker wall is a longer distance.", "Less surface means less diffusion.", "That reduces the gradient."], "y": "A shorter distance speeds diffusion."},
     {"q": "Why can an amoeba rely on diffusion alone for its oxygen, but a cow cannot?", "r": "The amoeba is tiny, with a large surface area to volume ratio", "w": ["The amoeba does not respire", "The cow lives in water", "The cow has no surface"],
      "e": ["Amoeba respires.", "The cow lives on land.", "Its body surface is small compared with its volume."], "y": "Large animals need lungs and blood to deliver oxygen."},
     {"q": "Why do villi in the small intestine speed up absorption?", "r": "They greatly increase the surface area", "w": ["They make the wall thicker", "They slow the blood", "They stop active transport"],
      "e": ["Villi have thin walls.", "Blood flow keeps the gradient steep.", "They also use active transport."], "y": "More surface, more diffusion."}], SRC)],
  learn=learn(
    [("Down the gradient",
      "Particles in liquids and gases move about at random. Where there are many of them (high concentration) more move away than come in, so overall they spread to where there are few. This net movement is diffusion.\n"
      "The difference in concentration is the concentration gradient; diffusion goes 'down' it. It needs no energy from the cell.\n"
      "Oxygen diffuses from the air in the lungs into the blood; carbon dioxide diffuses into a leaf from the air."),
     ("Speeding up diffusion",
      "Diffusion is faster when:\n• the concentration gradient is steeper;\n• the temperature is higher;\n• the surface area is larger;\n• the distance is shorter (thin walls).\n"
      "Small organisms have a large surface area compared with their volume (a {1} cm cube has {6} cm² for {1} cm³; a {3} cm cube only {2} cm² per cm³), so diffusion can supply them. Big animals need lungs, gills and blood."),
     ("Against the gradient: active transport",
      "Sometimes a cell must take in a substance that is already more concentrated inside it, for example a root hair taking in nitrate ions from very dilute soil water.\n"
      "It uses carrier proteins in the membrane and energy from respiration. This is active transport: from low to high concentration, using energy.\n"
      "If respiration stops (no oxygen, poison), active transport stops.")],
    key_words=[("diffusion", "net movement from high to low concentration"), ("concentration gradient", "a difference in concentration between two regions"),
               ("active transport", "movement against a concentration gradient using energy")],
    examples=["CO₂ into a leaf: diffusion", "Mineral ions into root hairs: active transport", "Cube side {2} cm: ratio {3} : {1}"],
    mistake=("Active transport moves substances from high to low concentration", "Active transport moves them from low to high, using energy",
             "Moving down the gradient needs no energy; that is diffusion.")))

# ---------------------------------------------------------------- 7. Osmosis
SRC = ["transport"]
L.lesson(D, S, 7, ("b3-7", "Osmosis: meaning, experiments and importance"), [6],
  "Osmosis is the net movement of water molecules from a region of higher water concentration (dilute solution) to a region of lower water concentration (concentrated solution) through a partially permeable membrane.\n"
  "• Plant cell in pure water or a dilute solution: water enters, the cell becomes turgid (firm). In a concentrated solution: water leaves, the cell becomes flaccid, then plasmolysed (membrane pulls away from the wall).\n"
  "• Animal cell (red blood cell) in water: swells and bursts (no wall). In a concentrated solution: shrinks (crenated).\n"
  "Importance: water uptake by root hairs; support (turgor); opening of stomata. Salting fish and adding sugar to jam preserve food by drawing water out of microbes.",
  worked({"a": 5.0, "b": 5.6},
         "A potato cylinder of mass {a} g is left in pure water. Its mass becomes {b} g. Find the percentage change in mass and explain it.",
         ["Change = {b} − {a} = {roundTo(b - a, 0.01)} g.", "Percentage change = {roundTo(b - a, 0.01)} ÷ {a} × {100} = {roundTo((b - a) / a * 100, 0.1)}%.",
          "Water moved into the potato cells by osmosis because pure water has a higher water concentration than the cell sap."],
         "+{roundTo((b - a) / a * 100, 0.1)}%: water entered by osmosis", checks=["roundTo((b - a) / a * 100, 0.1) == 12"]),
  [card("c3b7-1", "Osmosis: water moves from dilute to concentrated through a partially permeable membrane.",
        ["Raisins swell when soaked in water."], "b3-7-def"),
   card("c3b7-2", "Plant cells become turgid in water and plasmolysed in strong solutions.",
        ["Wilted vegetables recover in fresh water."], "b3-7-plant"),
   card("c3b7-3", "Percentage change = change ÷ starting mass × {100}.",
        ["{4}.{0} g → {4}.{4} g: +{10}%"], "b3-7-pct")],
  [bank("b3-7-def", 1, "{X.q}", [
     {"q": "What is osmosis?", "r": "Movement of water from a dilute to a concentrated solution through a partially permeable membrane", "w": ["Movement of salt from a concentrated to a dilute solution", "Movement of any particle down a gradient", "Movement of water using energy"],
      "e": ["Osmosis is about water, not salt.", "That is diffusion in general.", "Osmosis is passive."], "y": "It is a special case of diffusion: water through a membrane."},
     {"q": "Which way does water move by osmosis?", "r": "from a dilute solution to a concentrated solution", "w": ["from a concentrated solution to a dilute solution", "always into cells", "always out of cells"],
      "e": ["Water moves to where there is less water.", "It depends on the solutions.", "It depends on the solutions."], "y": "A dilute solution has more water molecules."},
     {"q": "Why must the membrane be partially permeable for osmosis?", "r": "Water molecules pass through but larger solute molecules cannot", "w": ["Nothing must pass through", "Everything must pass through", "Only salt must pass through"],
      "e": ["Water passes.", "If solutes passed, they would just diffuse.", "Salt is held back."], "y": "Only water can cross, so water moves."}], SRC),
   bank("b3-7-plant", 1, "{X.q}", [
     {"q": "A plant cell is placed in pure water. It becomes…", "r": "turgid", "w": ["plasmolysed", "burst", "crenated"],
      "e": ["That happens in strong solutions.", "The cell wall stops it bursting.", "Crenation is for animal cells in strong solutions."], "y": "Water enters, the vacuole swells, the cell becomes firm."},
     {"q": "A red blood cell is placed in pure water. What happens?", "r": "It swells and bursts", "w": ["It becomes turgid and safe", "It shrinks", "Nothing happens"],
      "e": ["Animal cells have no wall to stop bursting.", "It gains water, not loses.", "Water moves in by osmosis."], "y": "No cell wall, so it bursts (haemolysis)."},
     {"q": "Salt is sprinkled on fresh fish to preserve it. Why does it work?", "r": "Water leaves bacteria by osmosis, so they cannot grow", "w": ["Salt feeds the bacteria", "Salt adds water", "Salt kills fish cells by heat"],
      "e": ["Salt does not feed them.", "It draws water out.", "There is no heating."], "y": "The concentrated salt draws water out of microbes."}], SRC),
   num("b3-7-pct", 2, "A potato cylinder of mass {a} g is left in a sugar solution. Its mass becomes {b} g. Find the percentage change in mass (use − for a loss).", "roundTo((b - a) / a * 100, 0.1)",
       ["Change = {b} − {a} = {roundTo(b - a, 0.01)} g.", "Percentage change = {roundTo(b - a, 0.01)} ÷ {a} × {100} = {answer}%."],
       vars={"a": {"pick": [4, 5, 8, 10]}, "q": {"int": [-20, 20]}, "b": {"expr": "roundTo(a * (1 + q / 100), 0.01)"}},
       misc=[("final", "roundTo((b - a) / b * 100, 0.1)", "Divide the change by the starting mass {a} g, not the final mass."), ("abs", "roundTo(abs(b - a), 0.01)", "That is the change in grams. Divide by {a} and multiply by {100}.")],
       unit="%", sources=SRC, where=["q != 0"], signed=True),
   bank("b3-7-why", 3, "{X.q}", [
     {"q": "Leaves of a plant wilt on a hot afternoon. Why?", "r": "The cells lose more water than they take in and become flaccid", "w": ["The cells gain too much water", "The leaves are too heavy", "The sun melts the cells"],
      "e": ["They lose water.", "Weight is not the cause.", "Cells do not melt."], "y": "Flaccid cells cannot support the leaf."},
     {"q": "A farmer adds too much fertiliser near seedlings and they die. Why?", "r": "The soil water becomes more concentrated than root sap, so water leaves the roots", "w": ["Fertiliser is too heavy", "The roots get too much water", "Fertiliser blocks the sun"],
      "e": ["Weight is not the reason.", "The roots lose water.", "Fertiliser does not block light."], "y": "Water moves out of the roots by osmosis."},
     {"q": "How do root hairs take in water from the soil?", "r": "By osmosis, because the cell sap is more concentrated than soil water", "w": ["By active transport of water", "By the root pulling water in", "By photosynthesis"],
      "e": ["Water enters by osmosis; ions use active transport.", "There is no pulling.", "Photosynthesis happens in leaves."], "y": "Water moves from the dilute soil water to the concentrated sap."}], SRC)],
  learn=learn(
    [("A special kind of diffusion",
      "Osmosis is the diffusion of water through a partially permeable membrane, which lets water molecules through but holds back larger dissolved particles such as sugar.\n"
      "Water moves from where it is more concentrated (a dilute solution) to where it is less concentrated (a concentrated solution).\n"
      "Remember: a dilute solution has a lot of water; a concentrated solution has less."),
     ("Plant and animal cells",
      "• Plant cell in water: water enters, the vacuole swells and the cell presses on its wall: turgid. The wall stops it bursting.\n"
      "• Plant cell in a strong solution: water leaves, the cell becomes flaccid, and the membrane may pull away from the wall: plasmolysis.\n"
      "• Red blood cell in water: it swells and bursts, because it has no wall. In a strong solution it shrinks and becomes crenated."),
     ("Measuring osmosis and using it",
      "Put equal potato cylinders into solutions of different concentration, weigh them before and after, and work out the percentage change in mass:\n"
      "change ÷ starting mass × {100}. A gain means water went in; a loss means water came out.\n"
      "Osmosis lets roots absorb water and keeps plants upright; salting fish and making jam preserve food by drawing water out of microbes.")],
    key_words=[("osmosis", "movement of water through a partially permeable membrane from dilute to concentrated solution"),
               ("turgid", "firm, full of water"), ("plasmolysis", "membrane pulling away from the cell wall after water loss"), ("flaccid", "soft, having lost water")],
    examples=["Soaked raisins swell", "Salted fish keeps", "Potato {5} g → {5.6} g: +{12}%"],
    mistake=("Water moves from the concentrated to the dilute solution", "Water moves from the dilute to the concentrated solution",
             "Think of water: it moves from where there is more water to where there is less.")))

# ---------------------------------------------------------------- 8. Practical: diffusion and osmosis
SRC = ["practicals"]
L.lesson(D, S, 8, ("b3-8", "Practical: diffusion and osmosis"), [6, 7],
  "Diffusion: drop a crystal of potassium permanganate into still water in a beaker and watch the purple colour spread; repeat in warm water: it spreads faster.\n"
  "Osmosis with potato: cut equal cylinders with a cork borer, blot and weigh each, place them in sugar (or salt) solutions of different concentrations for 30 minutes, blot and weigh again.\n"
  "Calculate the percentage change in mass for each, plot it against concentration, and read where the line crosses zero: there the solution has the same water concentration as the potato cells.\n"
  "Osmosis with Visking tubing: tie sugar solution inside, stand it in water; the tubing swells and the liquid rises in an attached capillary.\n"
  "Control variables: same size of cylinder, same time, same temperature, blot the same way.",
  worked({"q1": 8, "q2": -6},
         "Potato cylinders gained {q1}% of their mass in {0.2} M sugar solution and lost {abs(q2)}% in {0.4} M. Between which concentrations is the potato's own sap concentration?",
         ["A gain means water entered: the solution was more dilute than the sap.", "A loss means water left: the solution was more concentrated than the sap.",
          "So the sap concentration lies between the two."], "Between the two solutions ({0.2} M and {0.4} M)"),
  [card("c3b8-1", "Keep everything the same except the concentration (control variables).",
        ["Same size, same time, same temperature."], "b3-8-fair"),
   card("c3b8-2", "Percentage change in mass shows the direction of osmosis.",
        ["Gain: water in. Loss: water out."], "b3-8-calc"),
   card("c3b8-3", "Where there is no change, the solution matches the cell sap.",
        ["Read the concentration where the graph crosses {0}%."], "b3-8-zero")],
  [bank("b3-8-fair", 1, "{X.q}", [
     {"q": "Why are all the potato cylinders cut to the same size?", "r": "To make it a fair test: only the concentration should differ", "w": ["To make them look nice", "To make them heavier", "Because small cylinders do not take in water"],
      "e": ["Appearance does not matter.", "Mass is measured, not chosen.", "All sizes take in water; size changes the rate."], "y": "Controlled variables must be kept the same."},
     {"q": "Why are the cylinders blotted dry before weighing?", "r": "To remove surface liquid that would add to the mass", "w": ["To kill the cells", "To add water", "To make them float"],
      "e": ["Blotting does not kill them.", "It removes water.", "Floating does not matter."], "y": "Only water inside the cells should be measured."},
     {"q": "In the permanganate experiment, why does the colour spread faster in warm water?", "r": "Particles move faster at higher temperature", "w": ["Warm water is purple", "The crystal is bigger in warm water", "Cold water stops diffusion completely"],
      "e": ["The colour comes from the crystal.", "The crystal is the same.", "Diffusion still happens in cold water, more slowly."], "y": "More kinetic energy, faster diffusion."}], SRC),
   num("b3-8-calc", 2, "A potato cylinder had mass {a} g before and {b} g after 30 minutes in a solution. Find the percentage change in mass (use − for a loss).", "roundTo((b - a) / a * 100, 0.1)",
       ["Change = {b} − {a} = {roundTo(b - a, 0.01)} g.", "Percentage change = {roundTo(b - a, 0.01)} ÷ {a} × {100} = {answer}%."],
       vars={"a": {"pick": [2, 2.5, 4, 5]}, "q": {"int": [-25, 25], "step": 5}, "b": {"expr": "roundTo(a * (1 + q / 100), 0.01)"}},
       misc=[("final", "roundTo((b - a) / b * 100, 0.1)", "Divide by the starting mass {a} g.")],
       unit="%", sources=SRC, where=["q != 0"], signed=True),
   order("b3-8-steps", 1, "Put the potato osmosis method in order.",
         ["Cut equal potato cylinders with a cork borer.", "Blot and weigh each cylinder.", "Place each in a different sugar solution for 30 minutes.",
          "Remove, blot and weigh again.", "Calculate the percentage change in mass."], hint="Weigh before and after.", sources=SRC, review="authored"),
   num("b3-8-zero", 3, "The percentage change in mass is +{u}% in {c1} M sugar and −{v}% in {c2} M. Assuming a straight line between them, at what concentration (M) is there no change? Give 2 decimal places.", "roundTo(c1 + (c2 - c1) * u / (u + v), 0.01)",
       ["Zero lies {u} ÷ ({u} + {v}) of the way from {c1} to {c2}.", "c = {c1} + ({c2} − {c1}) × {u} ÷ {u + v} = {answer} M."],
       vars={"c1": {"pick": [0.2, 0.3]}, "c2": {"pick": [0.4, 0.5]}, "u": {"int": [2, 12]}, "v": {"int": [2, 12]}},
       misc=[("mid", "roundTo((c1 + c2) / 2, 0.01)", "The zero is not always half-way: it is nearer the solution with the smaller change.")],
       unit="M", sources=SRC, where=["u != v"])],
  learn=learn(
    [("Seeing diffusion",
      "Drop a crystal of potassium permanganate into a beaker of still water. Over time, purple colour spreads through all the water: the particles diffuse from where they are concentrated to where they are not.\n"
      "Repeat in warm water: the colour spreads faster, because particles move faster when warmer."),
     ("Osmosis with potato cylinders",
      "• Cut equal cylinders of potato with a cork borer; blot and weigh each.\n• Put each into a sugar solution of a different concentration (including pure water) for the same time.\n"
      "• Blot and weigh again; work out the percentage change in mass.\n"
      "Gains show water entered (the solution was more dilute than the sap); losses show water left (it was more concentrated)."),
     ("Finding the sap concentration",
      "Plot percentage change in mass against concentration. The line crosses {0}% where the solution has the same water concentration as the potato cells: no net osmosis.\n"
      "Keep the test fair: same size of cylinder, same time, same temperature, and blot each the same way.\n"
      "Visking tubing (an artificial partially permeable membrane) filled with sugar solution and placed in water swells as water enters by osmosis.")],
    key_words=[("cork borer", "a metal tube for cutting equal cylinders"), ("control variable", "something kept the same so the test is fair"),
               ("Visking tubing", "an artificial partially permeable membrane")],
    examples=["Cylinder {4} g → {4.4} g: +{10}%", "Cylinder {5} g → {4.5} g: −{10}%", "No change between {0.2} M and {0.4} M solutions"],
    mistake=("A mass loss means water went into the potato", "A mass loss means water left the potato by osmosis",
             "The potato gets lighter when water moves out.")))

# ---------------------------------------------------------------- 9. Classification
SRC = ["classification"]
L.lesson(D, S, 9, ("b3-9", "Classification: reasons and the five-kingdom system"), [1],
  "Classification is sorting living things into groups by their shared features. It makes the huge variety of life easier to study, name and identify, and shows relationships.\n"
  "The five kingdoms: Prokaryotae (Monera: bacteria), Protoctista (Amoeba, Spirogyra, Plasmodium), Fungi (moulds, mushrooms, yeast), Plantae (plants), Animalia (animals).\n"
  "Levels (largest to smallest): kingdom, phylum, class, order, family, genus, species.\n"
  "Binomial system (Linnaeus): every species has two Latin names, genus then species, e.g. Homo sapiens (human), Zea mays (maize). The genus starts with a capital letter; both names are written in italics or underlined.",
  worked({},
         "Write the scientific name of maize correctly and say what each part means.",
         ["The genus is Zea and the species is mays.", "The genus starts with a capital, the species with a small letter, both italic (underlined when handwritten)."],
         "Zea mays: genus Zea, species mays"),
  [card("c3b9-1", "Classification groups organisms by shared features.",
        ["Animals with backbones are vertebrates."], "b3-9-why"),
   card("c3b9-2", "Five kingdoms: Prokaryotae, Protoctista, Fungi, Plantae, Animalia.",
        ["Mushrooms are in kingdom Fungi."], "b3-9-kingdom"),
   card("c3b9-3", "A scientific name is genus + species: Homo sapiens.",
        ["Genus with a capital letter; species small."], "b3-9-name")],
  [bank("b3-9-why", 1, "{X.q}", [
     {"q": "Why do biologists classify living things?", "r": "To make the variety of life easier to study and identify", "w": ["To make organisms grow faster", "To change their features", "To reduce the number of species"],
      "e": ["Classification does not affect growth.", "It describes features; it does not change them.", "It does not change how many species there are."], "y": "Grouping shows similarities and relationships."},
     {"q": "Organisms are put in the same group because they…", "r": "share important features", "w": ["live in the same place", "are the same colour", "are the same size"],
      "e": ["A fish and a frog may share a pond but are in different classes.", "Colour is not a reliable feature.", "Size is not used."], "y": "Shared body features show relationships."},
     {"q": "Which is the smallest group in classification?", "r": "species", "w": ["kingdom", "family", "genus"],
      "e": ["Kingdom is the largest.", "A family contains several genera.", "A genus contains several species."], "y": "Members of a species can breed together to give fertile young."}], SRC),
   bank("b3-9-kingdom", 1, "To which kingdom does this belong? {X.q}", [
     {"q": "A mushroom", "r": "Fungi", "w": ["Plantae", "Protoctista", "Prokaryotae"],
      "e": ["Mushrooms have no chlorophyll and do not photosynthesise.", "Protoctists are mostly single-celled.", "Prokaryotes have no nucleus."], "y": "Fungi feed by absorbing food; their walls are made of chitin."},
     {"q": "Amoeba", "r": "Protoctista", "w": ["Animalia", "Fungi", "Prokaryotae"],
      "e": ["Animals are multicellular.", "Amoeba is not a fungus.", "Amoeba has a nucleus."], "y": "A single eukaryotic cell: protoctist."},
     {"q": "A bacterium causing cholera", "r": "Prokaryotae", "w": ["Protoctista", "Fungi", "Animalia"],
      "e": ["Protoctists have a nucleus.", "Bacteria are not fungi.", "Bacteria are not animals."], "y": "No true nucleus: prokaryote."},
     {"q": "A mango tree", "r": "Plantae", "w": ["Fungi", "Protoctista", "Animalia"],
      "e": ["Fungi do not photosynthesise.", "Protoctists are simple, mostly single-celled.", "Animals do not photosynthesise."], "y": "Multicellular, photosynthesises, cellulose walls: plant."}], SRC),
   order("b3-9-levels", 2, "Put the levels of classification in order from largest to smallest.",
         ["kingdom", "phylum", "class", "order", "family", "genus", "species"], hint="'King Philip Came Over For Good Soup'.", sources=SRC, review="authored"),
   bank("b3-9-name", 3, "{X.q}", [
     {"q": "Which is the correct way to write the scientific name of humans?", "r": "Homo sapiens", "w": ["homo Sapiens", "Homo Sapiens", "HOMO SAPIENS"],
      "e": ["The genus takes the capital, not the species.", "The species name starts with a small letter.", "Only the first letter of the genus is capital."], "y": "Genus with a capital, species small, in italics."},
     {"q": "Two organisms are called Panthera leo and Panthera pardus. What does this tell you?", "r": "They belong to the same genus", "w": ["They are the same species", "They are in different kingdoms", "They are unrelated"],
      "e": ["Their species names differ.", "Same genus means same kingdom.", "Same genus shows a close relationship."], "y": "Lion and leopard share the genus Panthera."},
     {"q": "In Zea mays (maize), what is 'mays'?", "r": "the species name", "w": ["the genus name", "the family name", "the kingdom name"],
      "e": ["Zea is the genus.", "Families are not part of the binomial name.", "Kingdoms are not part of the name."], "y": "The second name is the species."}], SRC)],
  learn=learn(
    [("Why classify?",
      "There are millions of kinds of living things. Sorting them into groups by the features they share makes them easier to study, to name and to identify, and shows which organisms are related.\n"
      "For example, all animals with a backbone (fish, frogs, lizards, birds, mammals) are grouped as vertebrates."),
     ("Five kingdoms",
      "• Prokaryotae (Monera): bacteria; no true nucleus.\n• Protoctista: mostly single-celled eukaryotes such as Amoeba, Spirogyra and Plasmodium.\n"
      "• Fungi: moulds, mushrooms and yeast; no chlorophyll, feed by absorbing food.\n• Plantae: multicellular, photosynthesise, cellulose cell walls.\n• Animalia: multicellular, feed on other organisms, no cell walls.\n"
      "Each kingdom is divided again: phylum, class, order, family, genus and species."),
     ("Two-part names",
      "Common names change from place to place (maize, corn, 'kon'). Scientists use the binomial system invented by Linnaeus: every species has a two-part Latin name, genus then species.\n"
      "• Human: Homo sapiens. • Maize: Zea mays. • Lion: Panthera leo.\n"
      "The genus starts with a capital letter, the species with a small one, and the name is printed in italics (underlined when handwritten).")],
    key_words=[("classification", "sorting organisms into groups by shared features"), ("kingdom", "the largest group"),
               ("species", "organisms that can breed together to give fertile offspring"), ("binomial name", "genus + species, e.g. Homo sapiens")],
    examples=["Kingdom Fungi: yeast", "Kingdom Protoctista: Plasmodium", "Panthera leo and Panthera pardus: same genus"],
    mistake=("Homo Sapiens", "Homo sapiens",
             "Only the genus name begins with a capital letter.")))
