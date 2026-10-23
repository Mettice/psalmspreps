"""Form 3 Chemistry, Term 1, rows 1-7 (atoms, diffusion, subatomic particles, isotopes, RAM, the mole).
Run: python tools/authoring/form3/chem_a.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "chemistry", "chemistry"
EL = {"X": {"pick": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]}}

# ---------------------------------------------------------------- 1. Structure of the atom (review)
SRC = ["atoms"]
L.lesson(D, S, 1, ("k3-1", "Review: the simple structure of the atom"), [],
  "All matter is made of tiny particles called atoms. An atom has:\n"
  "• a very small, dense nucleus at the centre, containing protons (positive) and neutrons (no charge);\n"
  "• electrons (negative) moving around the nucleus in shells (energy levels).\n"
  "An atom is electrically neutral: number of protons = number of electrons.\n"
  "The number of protons is the atomic number (Z); protons + neutrons is the mass number (A). Neutrons = A − Z.",
  worked({"X": "Na"},
         "A sodium atom has atomic number {atomicNumber(X)} and mass number {massNumber(X)}. How many protons, electrons and neutrons does it have?",
         ["Protons = atomic number = {atomicNumber(X)}.", "The atom is neutral, so electrons = protons = {atomicNumber(X)}.",
          "Neutrons = mass number − atomic number = {massNumber(X)} − {atomicNumber(X)} = {neutrons(X)}."],
         "{atomicNumber(X)} protons, {atomicNumber(X)} electrons, {neutrons(X)} neutrons", checks=["neutrons(X) == 12"]),
  [card("c3k1-1", "Protons and neutrons are in the nucleus; electrons move around it in shells.",
        ["Hydrogen has {1} proton and {1} electron and no neutron."], "k3-1-where"),
   card("c3k1-2", "In a neutral atom, the number of electrons equals the number of protons.",
        ["Oxygen: {8} protons, so {8} electrons."], "k3-1-e"),
   card("c3k1-3", "Neutrons = mass number − atomic number.",
        ["Carbon: {12} − {6} = {6} neutrons."], "k3-1-n")],
  [bank("k3-1-where", 1, "{X.q}", [
     {"q": "Where are the protons in an atom?", "r": "in the nucleus", "w": ["in the shells around the nucleus", "spread evenly through the atom", "outside the atom"],
      "e": ["Electrons are in the shells.", "The nucleus is a tiny dense centre.", "All particles of an atom are inside it."], "y": "Protons and neutrons make up the nucleus."},
     {"q": "Which particle moves around the nucleus?", "r": "the electron", "w": ["the proton", "the neutron", "the nucleus"],
      "e": ["Protons stay in the nucleus.", "Neutrons stay in the nucleus.", "The nucleus is the centre itself."], "y": "Electrons move in shells around the nucleus."},
     {"q": "Why is an atom electrically neutral?", "r": "It has equal numbers of protons and electrons", "w": ["It has no particles with charge", "It has equal numbers of protons and neutrons", "Its neutrons cancel the charges"],
      "e": ["Protons and electrons are charged.", "Neutrons have no charge, so they do not balance anything.", "Neutrons have no charge."], "y": "Each proton's + charge is balanced by an electron's − charge."}], SRC),
   num("k3-1-e", 1, "An atom of {nameOf(X)} has atomic number {atomicNumber(X)}. How many electrons does it have?", "atomicNumber(X)",
       ["The atom is neutral: electrons = protons = atomic number.", "So it has {answer} electrons."],
       vars=EL, misc=[("mass", "massNumber(X)", "The mass number counts protons and neutrons. Electrons = atomic number.")],
       sources=SRC, where=["massNumber(X) != atomicNumber(X)"]),
   num("k3-1-n", 2, "An atom of {nameOf(X)} has atomic number {atomicNumber(X)} and mass number {massNumber(X)}. How many neutrons does it have?", "neutrons(X)",
       ["Neutrons = mass number − atomic number.", "= {massNumber(X)} − {atomicNumber(X)} = {answer}."],
       vars=EL, misc=[("sum", "massNumber(X) + atomicNumber(X)", "Subtract the atomic number from the mass number."), ("z", "atomicNumber(X)", "That is the number of protons.")],
       sources=SRC, where=["X != 'H'", "neutrons(X) != atomicNumber(X)"]),
   num("k3-1-a", 2, "An atom has {p} protons and {n} neutrons. What is its mass number?", "p + n",
       ["Mass number = protons + neutrons.", "= {p} + {n} = {answer}."],
       vars={"p": {"int": [3, 20]}, "n": {"int": [3, 22]}},
       misc=[("diff", "abs(n - p)", "Add protons and neutrons: both are in the nucleus.")],
       sources=SRC, where=["n != p"]),
   bank("k3-1-model", 3, "{X.q}", [
     {"q": "Most of the mass of an atom is in…", "r": "the nucleus", "w": ["the electrons", "the empty space", "the outer shell"],
      "e": ["Electrons are very light (about 1/1840 of a proton).", "Space has no mass.", "The outer shell holds only light electrons."], "y": "Protons and neutrons are much heavier than electrons."},
     {"q": "Most of the volume of an atom is…", "r": "empty space around the nucleus", "w": ["filled by the nucleus", "filled with neutrons", "filled with protons"],
      "e": ["The nucleus is tiny compared with the atom.", "Neutrons are in the tiny nucleus.", "Protons are in the tiny nucleus."], "y": "Electrons move in a large space around a tiny nucleus."},
     {"q": "Which statement about the nucleus is correct?", "r": "It is positively charged", "w": ["It is negatively charged", "It has no charge", "It contains the electrons"],
      "e": ["It holds protons (positive) and neutrons (none).", "The protons give it a positive charge.", "Electrons are outside it."], "y": "Protons give the nucleus its positive charge."}], SRC)],
  learn=learn(
    [("Inside an atom",
      "Everything around you, the air, water, the wood of your desk, is made of atoms. They are far too small to see: millions of them would fit across the full stop at the end of this sentence.\n"
      "An atom has a tiny, heavy centre called the nucleus. Around it, much lighter particles called electrons move in shells (energy levels).", "bohr(6)"),
     ("Three particles",
      "• Protons: in the nucleus, positive charge.\n• Neutrons: in the nucleus, no charge.\n• Electrons: in the shells, negative charge, very light.\n"
      "An atom has the same number of electrons as protons, so the charges cancel: the atom is neutral.\n"
      "Almost all the mass of an atom is in the nucleus, but almost all its volume is the space where the electrons move."),
     ("Atomic number and mass number",
      "The atomic number (Z) is the number of protons. It decides which element the atom is: every atom with {6} protons is carbon.\n"
      "The mass number (A) is the number of protons plus neutrons.\n"
      "So neutrons = A − Z. A sodium atom (Z = {11}, A = {23}) has {11} protons, {11} electrons and {12} neutrons.")],
    key_words=[("nucleus", "the small, dense centre of an atom"), ("proton", "positive particle in the nucleus"),
               ("neutron", "neutral particle in the nucleus"), ("electron", "negative particle moving around the nucleus")],
    examples=["Hydrogen: {1} proton, {1} electron, no neutron", "Oxygen (Z = {8}, A = {16}): {8} neutrons", "Calcium (Z = {20}): {20} electrons"],
    mistake=("Electrons = mass number", "Electrons = protons = atomic number (in a neutral atom)",
             "The mass number counts protons and neutrons together.")))

# ---------------------------------------------------------------- 2. Diffusion and Brownian motion
SRC = ["atoms"]
L.lesson(D, S, 2, ("k3-2", "Diffusion and Brownian motion: evidence for moving particles"), [1],
  "Diffusion is the spreading of particles from a region of high concentration to a region of low concentration until they are evenly mixed.\n"
  "• Smell of food spreading through a house; a crystal of potassium permanganate colouring still water.\n"
  "• Ammonia and hydrogen chloride from the two ends of a tube meet and form a white ring of ammonium chloride nearer the hydrogen chloride end: lighter particles (ammonia) diffuse faster.\n"
  "• Gases diffuse faster than liquids; diffusion is faster when hot.\n"
  "Brownian motion: under a microscope, smoke or pollen particles move in a jerky, random way because invisible air or water particles keep hitting them.",
  worked({},
         "Cotton wool soaked in ammonia is put at one end of a long glass tube and cotton wool soaked in hydrochloric acid at the other. A white ring forms nearer the acid end. Explain.",
         ["Both gases diffuse along the tube; where they meet they react to make white ammonium chloride.",
          "The ring is nearer the acid, so the ammonia travelled further in the same time.", "Ammonia particles are lighter, so they diffuse faster."],
         "Ammonia is lighter and diffuses faster"),
  [card("c3k2-1", "Diffusion: particles spread from high to low concentration.",
        ["The smell of ndolé cooking spreads through the house."], "k3-2-def"),
   card("c3k2-2", "Lighter particles diffuse faster; heat speeds diffusion.",
        ["Ammonia diffuses faster than hydrogen chloride."], "k3-2-ring"),
   card("c3k2-3", "Brownian motion: tiny visible particles jiggle because invisible particles hit them.",
        ["Smoke particles seen under a microscope move randomly."], "k3-2-brown")],
  [bank("k3-2-def", 1, "{X.q}", [
     {"q": "What is diffusion?", "r": "The spreading of particles from high to low concentration", "w": ["The melting of a solid", "The movement of particles from low to high concentration", "The dissolving of a gas in a liquid only"],
      "e": ["Melting is a change of state.", "Particles spread from where there are many to where there are few.", "Diffusion happens in gases and liquids generally."], "y": "Random motion spreads particles out evenly."},
     {"q": "A crystal of potassium permanganate is dropped into still water. After some hours…", "r": "the purple colour spreads through all the water", "w": ["the colour stays around the crystal", "the water turns solid", "the colour moves to the top only"],
      "e": ["The particles move and spread out.", "Nothing freezes.", "They spread in all directions."], "y": "The coloured particles diffuse until evenly spread."},
     {"q": "Which shows diffusion?", "r": "The smell of perfume spreading across a room", "w": ["Water freezing in a fridge", "A stone sinking in water", "Ice melting in the sun"],
      "e": ["That is freezing.", "That is sinking (density).", "That is melting."], "y": "Perfume particles spread through the air."}], SRC),
   bank("k3-2-ring", 2, "{X.q}", [
     {"q": "In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end?", "r": "Ammonia particles are lighter and diffuse faster", "w": ["Hydrogen chloride is lighter", "Ammonia was put in first", "The ring always forms in the middle"],
      "e": ["Hydrogen chloride (36.5) is heavier than ammonia (17).", "Both are put in at the same time.", "Then the ring would be in the middle."], "y": "The faster gas travels further before they meet."},
     {"q": "Which gas diffuses fastest?", "r": "hydrogen (the lightest gas)", "w": ["carbon dioxide", "chlorine", "oxygen"],
      "e": ["Carbon dioxide is heavier.", "Chlorine is very heavy.", "Oxygen is heavier than hydrogen."], "y": "Lighter particles move faster."},
     {"q": "How does temperature affect diffusion?", "r": "Diffusion is faster at higher temperature", "w": ["Diffusion is slower at higher temperature", "Temperature has no effect", "Diffusion stops above 50 °C"],
      "e": ["Heat makes particles move faster.", "Faster particles spread faster.", "It does not stop."], "y": "Particles have more energy when hot."}], SRC),
   bank("k3-2-brown", 2, "{X.q}", [
     {"q": "What is seen in Brownian motion?", "r": "Small particles such as smoke moving in a jerky, random way", "w": ["Atoms seen directly under a microscope", "Particles moving in straight lines only", "Particles standing still"],
      "e": ["Atoms are far too small to see; we see the smoke specks they hit.", "The motion is zig-zag.", "They keep moving."], "y": "Invisible air particles knock the visible specks about."},
     {"q": "What causes Brownian motion of pollen grains in water?", "r": "Water molecules hitting the grains unevenly", "w": ["The grains are alive and swimming", "Light pushing the grains", "Magnetism"],
      "e": ["Dead pollen and dust move too.", "Light is not the cause.", "There is no magnet."], "y": "Uneven bombardment by moving water molecules."},
     {"q": "Brownian motion is evidence that…", "r": "the particles of liquids and gases are always moving", "w": ["solids do not contain particles", "particles are larger than smoke specks", "air has no mass"],
      "e": ["It says nothing about solids.", "The particles are much smaller.", "Air particles have mass; that is why they can push."], "y": "Only moving particles could keep jostling the specks."}], SRC),
   order("k3-2-order", 3, "Put the explanation of the white ring in the ammonia / hydrogen chloride tube in order.",
         ["Ammonia and hydrogen chloride particles move along the tube by diffusion.", "Ammonia particles are lighter, so they move faster.",
          "The two gases meet nearer the hydrogen chloride end.", "They react to form a white ring of solid ammonium chloride."], hint="Start with the particles moving.", sources=SRC, review="authored")],
  learn=learn(
    [("Particles on the move",
      "When someone cooks ndolé, you can smell it in another room. Particles of the smell travel through the air, spreading from where there are many of them to where there are few.\n"
      "This spreading is diffusion: movement from high concentration to low concentration until the particles are evenly mixed. It happens because particles move all the time, at random."),
     ("Fast and slow diffusion",
      "• Gases diffuse faster than liquids; solids hardly at all.\n• Heat makes particles move faster, so diffusion speeds up.\n• Lighter particles diffuse faster than heavier ones.\n"
      "In a long tube with ammonia at one end and hydrogen chloride at the other, a white ring of ammonium chloride forms nearer the hydrogen chloride: ammonia (lighter) travelled further."),
     ("Brownian motion",
      "Look at smoke in a small glass cell under a microscope: the bright specks dance about in a jerky, random way. The same happens to pollen grains in water.\n"
      "The specks are being hit by air (or water) molecules, which are far too small to see. Because the hits are uneven, the specks are pushed one way, then another.\n"
      "This is strong evidence that matter is made of tiny, constantly moving particles.")],
    key_words=[("diffusion", "spreading of particles from high to low concentration"), ("concentration", "how many particles are in a given space"),
               ("Brownian motion", "the random movement of small visible particles caused by invisible moving molecules")],
    examples=["Perfume spreading across a classroom", "Purple colour spreading from a permanganate crystal", "Smoke specks jiggling under a microscope"],
    mistake=("Heavier gases diffuse faster", "Lighter gases diffuse faster",
             "Lighter particles move faster at the same temperature.")))

# ---------------------------------------------------------------- 3. Subatomic particles
SRC = ["atoms"]
L.lesson(D, S, 3, ("k3-3", "Characteristics of protons, neutrons and electrons"), [1],
  "Particle — relative mass — relative charge — where:\n"
  "• proton — 1 — +1 — nucleus\n• neutron — 1 — 0 — nucleus\n• electron — 1/1840 (almost 0) — −1 — shells\n"
  "Ions: an atom that loses electrons becomes a positive ion (Na → Na⁺); one that gains electrons becomes a negative ion (Cl → Cl⁻).\n"
  "Electrons in an ion = protons − charge: Na⁺ has 11 − 1 = 10 electrons; Cl⁻ has 17 + 1 = 18.",
  worked({"X": "Mg", "q": 2},
         "How many protons and electrons are in a magnesium ion, Mg²⁺ (atomic number {atomicNumber(X)})?",
         ["Protons = atomic number = {atomicNumber(X)} (the nucleus does not change).", "The ion has lost {q} electrons: {atomicNumber(X)} − {q} = {atomicNumber(X) - q} electrons."],
         "{atomicNumber(X)} protons, {atomicNumber(X) - q} electrons", checks=["atomicNumber(X) - q == 10"]),
  [card("c3k3-1", "Proton: mass {1}, charge +{1}. Neutron: mass {1}, charge {0}. Electron: mass almost {0}, charge −{1}.",
        ["The electron is about {1840} times lighter than a proton."], "k3-3-table"),
   card("c3k3-2", "A positive ion has lost electrons; a negative ion has gained them.",
        ["Na⁺: {11} protons, {10} electrons"], "k3-3-ion"),
   card("c3k3-3", "The number of protons never changes when an ion forms.",
        ["Cl⁻ still has {17} protons."], "k3-3-p")],
  [bank("k3-3-table", 1, "{X.q}", [
     {"q": "What is the relative charge of a neutron?", "r": "0", "w": ["+1", "−1", "+2"],
      "e": ["+1 is the proton.", "−1 is the electron.", "No subatomic particle has +2."], "y": "Neutrons are neutral."},
     {"q": "Which particle has a relative mass of about 1/1840?", "r": "the electron", "w": ["the proton", "the neutron", "the nucleus"],
      "e": ["A proton has relative mass 1.", "A neutron has relative mass 1.", "The nucleus is the heaviest part."], "y": "Electrons are about 1840 times lighter than protons."},
     {"q": "What is the relative charge of a proton?", "r": "+1", "w": ["−1", "0", "+1840"],
      "e": ["−1 is the electron.", "0 is the neutron.", "1840 compares masses, not charges."], "y": "Protons carry one positive charge each."}], SRC),
   num("k3-3-ion", 1, "How many electrons are in the ion {X.s} (atomic number {atomicNumber(X.e)})?", "atomicNumber(X.e) - X.q",
       ["Protons = {atomicNumber(X.e)}.", "{X.q > 0 ? 'Lost ' + X.q : 'Gained ' + (0 - X.q)} electron(s): {atomicNumber(X.e)} {X.q > 0 ? '−' : '+'} {abs(X.q)} = {answer}."],
       vars={"X": {"pick": [{"s": "Na⁺", "e": "Na", "q": 1}, {"s": "Mg²⁺", "e": "Mg", "q": 2}, {"s": "Al³⁺", "e": "Al", "q": 3}, {"s": "Cl⁻", "e": "Cl", "q": -1},
                            {"s": "O²⁻", "e": "O", "q": -2}, {"s": "K⁺", "e": "K", "q": 1}, {"s": "Ca²⁺", "e": "Ca", "q": 2}, {"s": "F⁻", "e": "F", "q": -1}, {"s": "S²⁻", "e": "S", "q": -2}]}},
       misc=[("atom", "atomicNumber(X.e)", "That is the neutral atom. The ion has {X.q > 0 ? 'lost' : 'gained'} {abs(X.q)} electron(s)."),
             ("sign", "atomicNumber(X.e) + X.q", "{X.q > 0 ? 'A positive ion has fewer electrons than protons.' : 'A negative ion has more electrons than protons.'}")],
       sources=SRC),
   num("k3-3-p", 2, "How many protons are in the ion {X.s}? (atomic number {atomicNumber(X.e)})", "atomicNumber(X.e)",
       ["Forming an ion changes only the electrons.", "Protons = atomic number = {answer}."],
       vars={"X": {"pick": [{"s": "Na⁺", "e": "Na", "q": 1}, {"s": "Mg²⁺", "e": "Mg", "q": 2}, {"s": "Cl⁻", "e": "Cl", "q": -1}, {"s": "O²⁻", "e": "O", "q": -2}, {"s": "Al³⁺", "e": "Al", "q": 3}]}},
       misc=[("e", "atomicNumber(X.e) - X.q", "That is the number of electrons. Protons do not change.")],
       sources=SRC),
   bank("k3-3-charge", 3, "{X.q}", [
     {"q": "An atom loses two electrons. What is the charge of the ion?", "r": "2+", "w": ["2−", "0", "1+"],
      "e": ["Losing negative electrons leaves extra positive charge.", "It now has more protons than electrons.", "It lost two, not one."], "y": "Two more protons than electrons: 2+."},
     {"q": "An ion has 17 protons and 18 electrons. What is its charge?", "r": "1−", "w": ["1+", "0", "35−"],
      "e": ["It has more electrons than protons.", "The numbers are not equal.", "Charge = protons − electrons = −1."], "y": "One extra electron: 1−."},
     {"q": "An ion has 12 protons and 10 electrons. What is its charge?", "r": "2+", "w": ["2−", "22+", "0"],
      "e": ["It has fewer electrons than protons.", "Charge is the difference, not the sum.", "The numbers are not equal."], "y": "12 − 10 = 2 more protons: 2+."}], SRC)],
  learn=learn(
    [("Comparing the particles",
      "• Proton: relative mass {1}, charge +{1}, in the nucleus.\n• Neutron: relative mass {1}, charge {0}, in the nucleus.\n• Electron: relative mass about {1} ÷ {1840}, charge −{1}, in the shells.\n"
      "Because electrons are so light, the mass of an atom is practically the mass of its protons and neutrons."),
     ("Ions",
      "Atoms can lose or gain electrons in chemical reactions, but never protons. Then the charges no longer balance and the particle is an ion.\n"
      "• Lose electrons → more protons than electrons → positive ion. Sodium loses {1}: Na⁺.\n"
      "• Gain electrons → more electrons than protons → negative ion. Chlorine gains {1}: Cl⁻.\n"
      "Metals usually form positive ions; non-metals form negative ions."),
     ("Counting electrons in an ion",
      "Electrons = protons − charge.\n• Na⁺: {11} − {1} = {10} electrons.\n• Mg²⁺: {12} − {2} = {10}.\n• O²⁻: {8} + {2} = {10}.\n"
      "Interesting: these ions all have {10} electrons, like the noble gas neon. You will see why in the lessons on bonding.")],
    key_words=[("relative mass", "mass compared with a proton (proton = {1})"), ("ion", "a charged particle formed when an atom loses or gains electrons"),
               ("cation", "a positive ion"), ("anion", "a negative ion")],
    examples=["K⁺: {19} protons, {18} electrons", "F⁻: {9} protons, {10} electrons", "Al³⁺: {13} protons, {10} electrons"],
    mistake=("Na⁺ has {12} electrons because it is positive", "Na⁺ has {10} electrons: it lost one",
             "A positive charge means electrons were lost, so there are fewer of them.")))

# ---------------------------------------------------------------- 4. Atomic number and mass number
SRC = ["atoms"]
L.lesson(D, S, 4, ("k3-4", "Atomic number, mass number and nuclide notation"), [1, 3],
  "Atomic number Z = number of protons (also the number of electrons in a neutral atom). It identifies the element.\n"
  "Mass number A = number of protons + number of neutrons.\n"
  "Nuclide notation: the mass number is written at the top left and the atomic number at the bottom left of the symbol, e.g. ²³₁₁Na.\n"
  "So: protons = Z, electrons = Z (neutral atom), neutrons = A − Z.\n"
  "Elements are arranged in the Periodic Table in order of atomic number.",
  worked({"X": "Al"},
         "For ²⁷₁₃Al, give the number of protons, neutrons and electrons.",
         ["Bottom number (Z) = {atomicNumber(X)}: {atomicNumber(X)} protons and {atomicNumber(X)} electrons.", "Top number (A) = {massNumber(X)}: neutrons = {massNumber(X)} − {atomicNumber(X)} = {neutrons(X)}."],
         "{atomicNumber(X)} protons, {neutrons(X)} neutrons, {atomicNumber(X)} electrons", checks=["neutrons(X) == 14"]),
  [card("c3k4-1", "Z (bottom) = protons; A (top) = protons + neutrons.",
        ["¹⁶₈O: {8} protons, {8} neutrons"], "k3-4-read"),
   card("c3k4-2", "The atomic number identifies the element.",
        ["Every atom with {6} protons is carbon."], "k3-4-which"),
   card("c3k4-3", "Neutrons = A − Z.",
        ["³⁹₁₉K: {39} − {19} = {20} neutrons"], "k3-4-n")],
  [num("k3-4-read", 1, "In the notation {sup(massNumber(X))}{sub(atomicNumber(X))}{X}, how many protons are there?", "atomicNumber(X)",
       ["The bottom number is the atomic number = number of protons.", "So there are {answer} protons."],
       vars=EL, misc=[("top", "massNumber(X)", "The top number is the mass number (protons + neutrons). Protons = the bottom number.")],
       sources=SRC, where=["X != 'H'"]),
   num("k3-4-which", 1, "An atom has {atomicNumber(X)} protons. Which element is it? Give its atomic number.", "atomicNumber(X)",
       ["The number of protons is the atomic number: {answer}.", "Atomic number {answer} is {nameOf(X)} ({X})."],
       vars=EL, misc=[("mass", "massNumber(X)", "The number of protons is the atomic number, not the mass number.")],
       sources=SRC, where=["X != 'H'"]),
   num("k3-4-n", 2, "How many neutrons are in {sup(massNumber(X))}{sub(atomicNumber(X))}{X}?", "neutrons(X)",
       ["Neutrons = A − Z = {massNumber(X)} − {atomicNumber(X)}.", "= {answer}."],
       vars=EL, misc=[("a", "massNumber(X)", "Subtract the atomic number from the mass number."), ("sum", "massNumber(X) + atomicNumber(X)", "Neutrons = A − Z: subtract.")],
       sources=SRC, where=["X != 'H'", "neutrons(X) != atomicNumber(X)"]),
   mcq("k3-4-write", 2, "An atom of {nameOf(X)} has {atomicNumber(X)} protons and {neutrons(X)} neutrons. How is it written in nuclide notation?",
       "{sup(massNumber(X)) + sub(atomicNumber(X)) + X}",
       [("{sup(atomicNumber(X)) + sub(massNumber(X)) + X}", "swap"), ("{sup(neutrons(X)) + sub(atomicNumber(X)) + X}", "neut"), ("{sup(massNumber(X) + atomicNumber(X)) + sub(atomicNumber(X)) + X}", "add")],
       ["Mass number = {atomicNumber(X)} + {neutrons(X)} = {massNumber(X)} (top).", "Atomic number = {atomicNumber(X)} (bottom). So: {answer}."],
       vars=EL, misc=[("swap", "The mass number (bigger) goes on top; the atomic number at the bottom."), ("neut", "The top number is protons + neutrons, not neutrons alone."),
                      ("add", "The mass number is protons + neutrons = {massNumber(X)}.")],
       sources=SRC, where=["X != 'H'", "neutrons(X) != atomicNumber(X)", "neutrons(X) != massNumber(X)"]),
   num("k3-4-a", 3, "An atom has {e} electrons and {n} neutrons. What is its mass number?", "e + n",
       ["Neutral atom: protons = electrons = {e}.", "Mass number = protons + neutrons = {e} + {n} = {answer}."],
       vars={"e": {"int": [3, 20]}, "d": {"int": [0, 2]}, "n": {"expr": "e + d"}},
       misc=[("e", "e + e + n", "Electrons do not count in the mass number: A = protons + neutrons.")],
       sources=SRC)],
  learn=learn(
    [("Two numbers describe a nucleus",
      "The atomic number Z is the number of protons. It is the identity of the element: {1} proton is hydrogen, {6} is carbon, {8} is oxygen, {11} is sodium.\n"
      "The mass number A is the total number of protons and neutrons, the heavy particles in the nucleus.\n"
      "In a neutral atom the number of electrons equals Z."),
     ("Nuclide notation",
      "We write the mass number at the top left and the atomic number at the bottom left of the symbol: {sup(23)}{sub(11)}Na.\n"
      "From this you can read everything:\n• protons = {11}\n• electrons = {11}\n• neutrons = {23} − {11} = {12}\n"
      "The bigger number is always the mass number."),
     ("Order in the Periodic Table",
      "The Periodic Table lists the elements in order of increasing atomic number: H ({1}), He ({2}), Li ({3}), … Ca ({20}).\n"
      "Knowing the first {20} elements and their atomic numbers will help you in every chemistry lesson this year.")],
    key_words=[("atomic number (Z)", "the number of protons"), ("mass number (A)", "protons + neutrons"), ("nuclide notation", "ᴬ_Z X: A on top, Z below")],
    examples=["{sup(35)}{sub(17)}Cl: {17} p, {18} n, {17} e", "{sup(40)}{sub(20)}Ca: {20} p, {20} n, {20} e", "{sup(4)}{sub(2)}He: {2} p, {2} n, {2} e"],
    mistake=("{sup(23)}{sub(11)}Na has {23} neutrons", "{23} − {11} = {12} neutrons",
             "The top number counts protons and neutrons together.")))

# ---------------------------------------------------------------- 5. Isotopes and relative atomic mass
SRC = ["isotopes"]
L.lesson(D, S, 5, ("k3-5", "Isotopes and calculating relative atomic mass"), [4],
  "Isotopes are atoms of the same element (same number of protons) with different numbers of neutrons, so different mass numbers: ³⁵Cl and ³⁷Cl; ¹²C and ¹⁴C.\n"
  "Isotopes of an element have the same chemical properties (same electrons) but slightly different physical properties (mass, density).\n"
  "Relative atomic mass (RAM, Ar) is the average mass of the atoms of an element compared with 1/12 of the mass of a carbon-12 atom. It takes account of the abundance (percentage) of each isotope:\n"
  "RAM = (mass₁ × %₁ + mass₂ × %₂) ÷ 100. For chlorine: (35 × 75 + 37 × 25) ÷ 100 = 35.5.",
  worked({"m1": 35, "p1": 75, "m2": 37},
         "Chlorine is {p1}% ³⁵Cl and {100 - p1}% ³⁷Cl. Calculate its relative atomic mass.",
         ["RAM = (mass × % for each isotope, added) ÷ {100}.", "= ({m1} × {p1} + {m2} × {100 - p1}) ÷ {100} = ({m1 * p1} + {m2 * (100 - p1)}) ÷ {100}.",
          "= {(m1 * p1 + m2 * (100 - p1)) / 100}."], "{(m1 * p1 + m2 * (100 - p1)) / 100}", checks=["(m1 * p1 + m2 * (100 - p1)) / 100 == 35.5"]),
  [card("c3k5-1", "Isotopes: same protons, different neutrons.",
        ["¹²C and ¹⁴C both have {6} protons; ¹⁴C has {2} more neutrons."], "k3-5-def"),
   card("c3k5-2", "RAM is the average of the isotope masses, weighted by abundance.",
        ["({35} × {75} + {37} × {25}) ÷ {100} = {35.5}"], "k3-5-ram"),
   card("c3k5-3", "Isotopes react in the same way because they have the same electrons.",
        ["³⁵Cl and ³⁷Cl both form Cl⁻."], "k3-5-prop")],
  [bank("k3-5-def", 1, "{X.q}", [
     {"q": "What are isotopes?", "r": "Atoms of the same element with different numbers of neutrons", "w": ["Atoms of different elements with the same mass number", "Atoms with different numbers of protons", "Atoms with different numbers of electrons only"],
      "e": ["Different elements have different numbers of protons.", "Changing the protons changes the element.", "That describes ions."], "y": "Same Z, different A."},
     {"q": "¹²₆C and ¹⁴₆C are isotopes. How do they differ?", "r": "¹⁴C has two more neutrons", "w": ["¹⁴C has two more protons", "¹⁴C has two more electrons", "They are different elements"],
      "e": ["Both have 6 protons.", "Both neutral atoms have 6 electrons.", "Both are carbon (Z = 6)."], "y": "Mass numbers differ by 2, protons are equal, so neutrons differ by 2."},
     {"q": "Which pair are isotopes?", "r": "³⁵₁₇Cl and ³⁷₁₇Cl", "w": ["⁴⁰₁₈Ar and ⁴⁰₂₀Ca", "²³₁₁Na and ²⁴₁₂Mg", "¹⁶₈O and ¹⁴₇N"],
      "e": ["Same mass number but different elements (different Z).", "Different elements.", "Different elements."], "y": "Same atomic number (17), different mass numbers."}], SRC),
   num("k3-5-ram", 2, "An element has two isotopes: mass {m} ({p}%) and mass {m + 2} ({100 - p}%). Calculate its relative atomic mass.", "(m * p + (m + 2) * (100 - p)) / 100",
       ["RAM = ({m} × {p} + {m + 2} × {100 - p}) ÷ {100}.", "= ({m * p} + {(m + 2) * (100 - p)}) ÷ {100} = {answer}."],
       vars={"m": {"int": [6, 79]}, "p": {"int": [10, 90], "step": 5}},
       misc=[("plain", "m + 1", "That is the simple average. Use the percentages: the commoner isotope counts more."),
             ("swap", "(m * (100 - p) + (m + 2) * p) / 100", "Each mass goes with its own percentage: {m} with {p}%.")],
       sources=SRC, where=["p != 50"]),
   num("k3-5-real", 1, "{X.n}: {X.a}. Calculate the relative atomic mass of {X.n} to {1} decimal place.", "roundTo(X.v, 0.1)",
       ["{X.s}", "≈ {answer}."],
       vars={"X": {"pick": [
         {"n": "Chlorine", "a": "75% ³⁵Cl and 25% ³⁷Cl", "s": "(35 × 75 + 37 × 25) ÷ 100 = 35.5", "v": 35.5},
         {"n": "Copper", "a": "69% ⁶³Cu and 31% ⁶⁵Cu", "s": "(63 × 69 + 65 × 31) ÷ 100 = 63.62", "v": 63.62},
         {"n": "Boron", "a": "20% ¹⁰B and 80% ¹¹B", "s": "(10 × 20 + 11 × 80) ÷ 100 = 10.8", "v": 10.8},
         {"n": "Neon", "a": "90% ²⁰Ne and 10% ²²Ne", "s": "(20 × 90 + 22 × 10) ÷ 100 = 20.2", "v": 20.2},
         {"n": "Bromine", "a": "50% ⁷⁹Br and 50% ⁸¹Br", "s": "(79 × 50 + 81 × 50) ÷ 100 = 80", "v": 80}]}},
       review="authored", sources=SRC),
   bank("k3-5-prop", 2, "{X.q}", [
     {"q": "Why do ³⁵Cl and ³⁷Cl have the same chemical properties?", "r": "They have the same number of electrons", "w": ["They have the same mass number", "They have the same number of neutrons", "They are different elements"],
      "e": ["Their mass numbers differ.", "Their neutrons differ.", "Both are chlorine."], "y": "Chemical reactions involve electrons, which are the same."},
     {"q": "Which property differs between two isotopes of the same element?", "r": "their mass", "w": ["their number of protons", "their chemical reactions", "their atomic number"],
      "e": ["Protons are the same.", "Reactions are the same.", "The atomic number is the same."], "y": "Different numbers of neutrons give different masses."},
     {"q": "Why is the RAM of chlorine 35.5 and not a whole number?", "r": "It is an average of isotopes of mass 35 and 37", "w": ["A chlorine atom has half a neutron", "It has 35.5 protons", "It was measured wrongly"],
      "e": ["Particles are not split.", "Chlorine has 17 protons.", "It is an exact average."], "y": "The weighted average of 35 (75%) and 37 (25%) is 35.5."}], SRC),
   num("k3-5-pct", 3, "An element has RAM {R} and two isotopes of mass {m} and {m + 2}. What percentage is the isotope of mass {m}?", "100 - (R - m) * 50",
       ["Let x% be mass {m}: ({m}x + {m + 2}({100} − x)) ÷ {100} = {R}.", "{m}x + {(m + 2) * 100} − {m + 2}x = {R * 100}, so {2}x = {(m + 2) * 100 - R * 100}, x = {answer}%."],
       vars={"m": {"int": [10, 60]}, "q": {"int": [1, 9]}, "R": {"expr": "m + q / 5"}},
       misc=[("other", "(R - m) * 50", "That is the percentage of the heavier isotope."), ("half", "50", "Work it out from the RAM; it is not always half.")],
       unit="%", sources=SRC, where=["q != 5"])],
  learn=learn(
    [("Same element, different masses",
      "All chlorine atoms have {17} protons, but not all have the same number of neutrons. About three in four have {18} neutrons (mass {35}); about one in four has {20} neutrons (mass {37}).\n"
      "Atoms of the same element with different numbers of neutrons are isotopes. They are written ³⁵Cl and ³⁷Cl, or chlorine-{35} and chlorine-{37}.\n"
      "Carbon has ¹²C (common) and ¹⁴C (rare, used to date old objects)."),
     ("Same chemistry",
      "Chemical reactions depend on electrons. Isotopes of an element have the same number of protons and therefore the same number of electrons, so they react in exactly the same way.\n"
      "They differ only in mass, which slightly changes physical properties such as density."),
     ("Relative atomic mass",
      "A sample of an element contains a mixture of its isotopes, so its average atomic mass is not a whole number. We compare it with {1}/{12} of the mass of a carbon-{12} atom.\n"
      "RAM = (mass × percentage for each isotope, added up) ÷ {100}.\n"
      "Chlorine: ({35} × {75} + {37} × {25}) ÷ {100} = ({2625} + {925}) ÷ {100} = {35.5}.")],
    key_words=[("isotopes", "atoms with the same atomic number but different mass numbers"), ("abundance", "the percentage of each isotope in the element"),
               ("relative atomic mass (Ar)", "the average mass of an element's atoms compared with {1}/{12} of carbon-{12}")],
    examples=["Boron: {20}% ¹⁰B, {80}% ¹¹B → RAM {10.8}", "Hydrogen isotopes: ¹H, ²H (deuterium), ³H (tritium)"],
    mistake=("RAM of chlorine = ({35} + {37}) ÷ {2} = {36}", "RAM = ({35} × {75} + {37} × {25}) ÷ {100} = {35.5}",
             "The commoner isotope counts more: use the percentages, not a simple average.")))

# ---------------------------------------------------------------- 6. RAM and the mole of atoms
SRC = ["mole"]
RAMS = [{"s": "C", "n": "carbon", "r": 12}, {"s": "O", "n": "oxygen", "r": 16}, {"s": "Na", "n": "sodium", "r": 23}, {"s": "Mg", "n": "magnesium", "r": 24},
        {"s": "Al", "n": "aluminium", "r": 27}, {"s": "S", "n": "sulphur", "r": 32}, {"s": "Ca", "n": "calcium", "r": 40}, {"s": "Fe", "n": "iron", "r": 56},
        {"s": "Cu", "n": "copper", "r": 64}, {"s": "Zn", "n": "zinc", "r": 65}, {"s": "N", "n": "nitrogen", "r": 14}]
L.lesson(D, S, 6, ("k3-6", "Relative atomic mass and the mole of atoms"), [5],
  "Chemists count atoms by weighing them. A mole (mol) of atoms of an element is its relative atomic mass in grams:\n"
  "• 1 mol of carbon (C = 12) has a mass of 12 g; 1 mol of magnesium (Mg = 24) has a mass of 24 g.\n"
  "• This mass per mole is the molar mass, in g/mol.\n"
  "Formulas: number of moles = mass ÷ molar mass; mass = moles × molar mass.\n"
  "Example: 48 g of magnesium = 48 ÷ 24 = 2 mol.",
  worked({"r": 24, "m": 60},
         "How many moles of magnesium atoms are in {m} g of magnesium? (Mg = {r})",
         ["Molar mass of Mg = {r} g/mol.", "Moles = mass ÷ molar mass = {m} ÷ {r} = {m / r} mol."],
         "{m / r} mol", checks=["m / r == 2.5"]),
  [card("c3k6-1", "One mole of an element has a mass equal to its RAM in grams.",
        ["C = {12}: {1} mol of carbon is {12} g."], "k3-6-molar"),
   card("c3k6-2", "Moles = mass ÷ molar mass.",
        ["{48} g of Mg (Mg = {24}): {2} mol"], "k3-6-n"),
   card("c3k6-3", "Mass = moles × molar mass.",
        ["{3} mol of O atoms (O = {16}): {48} g"], "k3-6-m")],
  [num("k3-6-molar", 1, "What is the mass of {1} mole of {X.n} atoms (g)? ({X.s} = {X.r})", "X.r",
       ["The mass of {1} mol is the RAM in grams.", "{1} mol of {X.n} = {answer} g."],
       vars={"X": {"pick": RAMS}},
       misc=[("one", "1", "A mole is not {1} g: it is the RAM in grams.")],
       unit="g", sources=SRC),
   num("k3-6-n", 1, "How many moles of atoms are in {X.r * k} g of {X.n}? ({X.s} = {X.r})", "k",
       ["Moles = mass ÷ molar mass = {X.r * k} ÷ {X.r}.", "= {answer} mol."],
       vars={"X": {"pick": RAMS}, "k": {"int": [2, 8]}},
       misc=[("times", "X.r * k * X.r", "Divide the mass by the molar mass."), ("flip", "roundTo(1 / k, 0.0001)", "Moles = mass ÷ molar mass, not molar mass ÷ mass.")],
       unit="mol", sources=SRC),
   num("k3-6-m", 2, "Find the mass of {n} mol of {X.n} atoms (g). ({X.s} = {X.r})", "roundTo(n * X.r, 0.01)",
       ["Mass = moles × molar mass = {n} × {X.r}.", "= {answer} g."],
       vars={"X": {"pick": RAMS}, "k": {"int": [1, 12]}, "n": {"expr": "k / 4"}},
       misc=[("div", "roundTo(X.r / n, 0.01)", "Mass = moles × molar mass: multiply.")],
       unit="g", sources=SRC, where=["k != 4"]),
   num("k3-6-frac", 2, "How many moles of atoms are in {m} g of {X.n}? ({X.s} = {X.r}) Give the answer to {2} decimal places.", "roundTo(m / X.r, 0.01)",
       ["Moles = {m} ÷ {X.r}.", "= {answer} mol."],
       vars={"X": {"pick": RAMS}, "m": {"int": [2, 30]}},
       misc=[("times", "m * X.r", "Divide the mass by the molar mass.")],
       unit="mol", sources=SRC, where=["m % X.r != 0"]),
   num("k3-6-compare", 3, "Which contains more atoms: {a} g of {X.n} ({X.s} = {X.r}) or {b} g of {Y.n} ({Y.s} = {Y.r})? Give the number of moles of atoms in the one with more, to {2} decimal places.", "roundTo(max(a / X.r, b / Y.r), 0.01)",
       ["{X.n}: {a} ÷ {X.r} = {roundTo(a / X.r, 0.01)} mol.", "{Y.n}: {b} ÷ {Y.r} = {roundTo(b / Y.r, 0.01)} mol.", "More moles means more atoms: {answer} mol."],
       vars={"X": {"pick": RAMS[:5]}, "Y": {"pick": RAMS[5:]}, "a": {"int": [10, 60], "step": 2}, "b": {"int": [10, 60], "step": 2}},
       misc=[("mass", "max(a, b)", "More grams does not mean more atoms: compare moles."), ("min", "roundTo(min(a / X.r, b / Y.r), 0.01)", "That is the one with fewer atoms.")],
       unit="mol", sources=SRC, where=["roundTo(a / X.r, 0.01) != roundTo(b / Y.r, 0.01)", "(a > b) != (a / X.r > b / Y.r)"])],
  learn=learn(
    [("Counting by weighing",
      "Atoms are far too small to count one by one. Market traders in Mokolo sell rice by the cup or the bag, not grain by grain; chemists count atoms by weighing them.\n"
      "The unit chemists use for 'a certain number of particles' is the mole (mol)."),
     ("What a mole of atoms weighs",
      "One mole of atoms of an element has a mass equal to its relative atomic mass in grams.\n"
      "• C = {12}: {1} mol of carbon atoms is {12} g.\n• Mg = {24}: {1} mol is {24} g.\n• Fe = {56}: {1} mol is {56} g.\n"
      "This mass per mole is the molar mass (g/mol). One mole of any element contains the same number of atoms."),
     ("Two formulas",
      "• moles = mass ÷ molar mass: {48} g of magnesium is {48} ÷ {24} = {2} mol.\n"
      "• mass = moles × molar mass: {0.5} mol of iron is {0.5} × {56} = {28} g.\n"
      "To compare numbers of atoms in two samples, compare their moles, not their masses: {12} g of carbon has more atoms than {32} g of sulphur? Both are {1} mol, so they have the same number.")],
    key_words=[("mole (mol)", "the chemist's unit for an amount of particles"), ("molar mass", "the mass of {1} mol, in g/mol: the RAM in grams")],
    examples=["{36} g of carbon = {3} mol", "{0.25} mol of calcium = {10} g", "{56} g of iron and {12} g of carbon: both {1} mol"],
    mistake=("{48} g of Mg = {48} × {24} mol", "{48} g of Mg = {48} ÷ {24} = {2} mol",
             "Divide the mass by the molar mass to get moles.")))

# ---------------------------------------------------------------- 7. The mole and Avogadro's constant
SRC = ["mole"]
L.lesson(D, S, 7, ("k3-7", "A mole of atoms and the Avogadro constant"), [6],
  "One mole of any substance contains 6.02 × 10²³ particles (atoms, molecules or ions). This number is the Avogadro constant, L or Nₐ.\n"
  "• Number of particles = moles × 6.02 × 10²³.\n• Moles = number of particles ÷ 6.02 × 10²³.\n"
  "• 12 g of carbon (1 mol) and 24 g of magnesium (1 mol) contain the same number of atoms: 6.02 × 10²³.\n"
  "Combine with mass: atoms = (mass ÷ molar mass) × 6.02 × 10²³.",
  worked({"n": 2},
         "How many atoms are in {n} mol of copper? Give the answer in standard form.",
         ["Atoms = moles × {6.02} × {10}{sup(23)}.", "= {n} × {6.02} × {10}{sup(23)} = {n * 6.02} × {10}{sup(23)}.", "In standard form: {n * 0.602} × {10}{sup(24)}."],
         "{n * 0.602} × {10}{sup(24)} atoms", checks=["n * 0.602 == 1.204"]),
  [card("c3k7-1", "One mole contains {6.02} × {10}{sup(23)} particles: the Avogadro constant.",
        ["{1} mol of carbon atoms: {6.02} × {10}{sup(23)} atoms"], "k3-7-L"),
   card("c3k7-2", "Particles = moles × {6.02} × {10}{sup(23)}.",
        ["{0.5} mol: {3.01} × {10}{sup(23)} atoms"], "k3-7-count"),
   card("c3k7-3", "Moles = particles ÷ {6.02} × {10}{sup(23)}.",
        ["{12.04} × {10}{sup(23)} atoms = {2} mol"], "k3-7-back")],
  [bank("k3-7-L", 1, "{X.q}", [
     {"q": "What is the Avogadro constant?", "r": "6.02 × 10²³ particles per mole", "w": ["6.02 × 10²³ grams", "12 g of carbon", "1840"],
      "e": ["It is a number of particles, not a mass.", "12 g of carbon is one mole; it contains 6.02 × 10²³ atoms.", "1840 compares the masses of a proton and an electron."], "y": "The number of particles in one mole."},
     {"q": "Which contains 6.02 × 10²³ atoms?", "r": "24 g of magnesium (Mg = 24)", "w": ["1 g of magnesium", "12 g of magnesium", "6.02 g of magnesium"],
      "e": ["1 g is 1/24 mol.", "12 g is 0.5 mol.", "The number 6.02 is not a mass."], "y": "24 g of magnesium is 1 mol."},
     {"q": "12 g of carbon and 32 g of sulphur (C = 12, S = 32). Which has more atoms?", "r": "They have the same number", "w": ["The sulphur", "The carbon", "It cannot be told"],
      "e": ["32 g of S is only 1 mol.", "12 g of C is only 1 mol.", "Both are 1 mol, so the numbers can be compared."], "y": "1 mol of each: 6.02 × 10²³ atoms."}], SRC),
   num("k3-7-count", 1, "How many atoms are in {n} mol of an element? Write the answer as a × {10}{sup(23)}; give a.", "roundTo(n * 6.02, 0.001)",
       ["Atoms = moles × {6.02} × {10}{sup(23)}.", "= {n} × {6.02} × {10}{sup(23)} = {answer} × {10}{sup(23)}."],
       vars={"k": {"int": [1, 8]}, "n": {"expr": "k / 4"}},
       misc=[("div", "roundTo(6.02 / n, 0.01)", "Multiply the moles by the Avogadro constant.")],
       sources=SRC, where=["k != 4"]),
   num("k3-7-back", 2, "A sample contains {a} × {10}{sup(23)} atoms. How many moles is that?", "roundTo(a / 6.02, 0.01)",
       ["Moles = atoms ÷ {6.02} × {10}{sup(23)}.", "= {a} ÷ {6.02} = {answer} mol."],
       vars={"k": {"int": [1, 10]}, "a": {"expr": "roundTo(k * 6.02 / 2, 0.01)"}},
       misc=[("times", "roundTo(a * 6.02, 0.01)", "Divide the number of atoms by the Avogadro constant.")],
       unit="mol", sources=SRC),
   num("k3-7-mass", 2, "How many atoms are in {X.r * k} g of {X.n} ({X.s} = {X.r})? Write the answer as a × {10}{sup(23)}; give a.", "roundTo(k * 6.02, 0.01)",
       ["Moles = {X.r * k} ÷ {X.r} = {k} mol.", "Atoms = {k} × {6.02} × {10}{sup(23)} = {answer} × {10}{sup(23)}."],
       vars={"X": {"pick": RAMS}, "k": {"int": [2, 5]}},
       misc=[("mass", "roundTo(X.r * k * 6.02, 0.01)", "Change the mass to moles first (÷ {X.r})."), ("one", "6.02", "That is for {1} mol; there are {k} mol.")],
       sources=SRC),
   num("k3-7-std", 3, "How many atoms are in {m} g of {X.n} ({X.s} = {X.r})? Write the answer in standard form a × {10}ⁿ; give a to {2} decimal places.", "roundTo(m / X.r * 6.02 / (m / X.r * 6.02 >= 10 ? 10 : 1), 0.01)",
       ["Moles = {m} ÷ {X.r} = {roundTo(m / X.r, 0.0001)} mol.", "Atoms = {roundTo(m / X.r, 0.0001)} × {6.02} × {10}{sup(23)} = {roundTo(m / X.r * 6.02, 0.01)} × {10}{sup(23)}.",
        "In standard form a = {answer}."],
       vars={"X": {"pick": RAMS}, "m": {"int": [3, 100]}},
       misc=[("nostd", "roundTo(m / X.r * 6.02, 0.01)", "That number is not between {1} and {10}: move the decimal point.")],
       sources=SRC, where=["m / X.r * 6.02 >= 10", "m / X.r * 6.02 < 100"])],
  learn=learn(
    [("How many in a mole?",
      "A dozen means {12}; a ream of paper means {500} sheets. A mole means {6.02} × {10}{sup(23)} particles.\n"
      "This huge number is the Avogadro constant (L). It was chosen so that {12} g of carbon-{12} contains exactly one mole of atoms.\n"
      "{6.02} × {10}{sup(23)} is {602000} million million million: if you counted one atom every second, it would take far longer than the age of the universe."),
     ("Particles and moles",
      "• particles = moles × {6.02} × {10}{sup(23)}\n• moles = particles ÷ ({6.02} × {10}{sup(23)})\n"
      "{2} mol of copper contains {2} × {6.02} × {10}{sup(23)} = {12.04} × {10}{sup(23)} = {1.204} × {10}{sup(24)} atoms.\n"
      "{3.01} × {10}{sup(23)} atoms is half a mole."),
     ("From grams to atoms",
      "Go through moles:\n• grams → moles: divide by the molar mass;\n• moles → atoms: multiply by {6.02} × {10}{sup(23)}.\n"
      "{46} g of sodium (Na = {23}) is {2} mol, which is {12.04} × {10}{sup(23)} atoms. Equal numbers of moles always contain equal numbers of particles.")],
    key_words=[("Avogadro constant", "{6.02} × {10}{sup(23)} particles per mole"), ("particle", "an atom, molecule or ion"), ("standard form", "a × {10}ⁿ with {1} ≤ a < {10}")],
    examples=["{0.5} mol = {3.01} × {10}{sup(23)} atoms", "{3} mol = {1.806} × {10}{sup(24)} atoms", "{64} g of copper (Cu = {64}) = {6.02} × {10}{sup(23)} atoms"],
    mistake=("{2} mol = {6.02} × {10}{sup(23)} atoms", "{2} mol = {2} × {6.02} × {10}{sup(23)} = {1.204} × {10}{sup(24)} atoms",
             "Each mole contains {6.02} × {10}{sup(23)} particles; multiply by the number of moles.")))
