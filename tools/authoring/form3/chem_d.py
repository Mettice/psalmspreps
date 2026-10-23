"""Form 3 Chemistry, Term 1, rows 19-26 (covalent and metallic bonding, shapes, crystals, diamond and graphite).
Run: python tools/authoring/form3/chem_d.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "chemistry", "chemistry"
SRC = ["bonding"]


def E(s):
    """A formula or equation as fixed text inside a card, Learn screen or example."""
    return "{'" + s + "'}"


MOLS = [{"f": "H₂", "n": "hydrogen", "p": 1, "b": "single"}, {"f": "Cl₂", "n": "chlorine", "p": 1, "b": "single"},
        {"f": "O₂", "n": "oxygen", "p": 2, "b": "double"}, {"f": "N₂", "n": "nitrogen", "p": 3, "b": "triple"},
        {"f": "HCl", "n": "hydrogen chloride", "p": 1, "b": "single"}, {"f": "H₂O", "n": "water", "p": 2, "b": "two single"},
        {"f": "NH₃", "n": "ammonia", "p": 3, "b": "three single"}, {"f": "CH₄", "n": "methane", "p": 4, "b": "four single"},
        {"f": "CO₂", "n": "carbon dioxide", "p": 4, "b": "two double"}]

# ---------------------------------------------------------------- 19. Covalent bonding
L.lesson(D, S, 19, ("k3-19", "Covalent bonding: formation"), [16],
  "A covalent bond is a shared pair of electrons between two non-metal atoms. Each atom puts in one electron and both atoms count the pair, so both complete their outer shells.\n"
  "• Single bond: one shared pair (H–H, Cl–Cl). Double bond: two pairs (O=O). Triple bond: three pairs (N≡N).\n"
  "• Number of bonds an atom forms = electrons it needs to complete its shell: H 1, Cl 1, O 2, N 3, C 4.\n"
  "• Covalent substances are made of molecules: H₂, O₂, H₂O, NH₃, CH₄, CO₂.\n"
  "Dot-and-cross diagrams show the shared pairs in the overlap of the two atoms' outer shells.",
  worked({},
         "Show how a molecule of methane, CH₄, is held together.",
         ["Carbon ({2}, {4}) needs {4} more electrons; each hydrogen needs {1}.", "Carbon shares one pair with each of {4} hydrogen atoms.",
          "Carbon now has {8} outer electrons and each hydrogen has {2}: all shells are full."],
         "Four single covalent bonds (four shared pairs)"),
  [card("c3k19-1", "A covalent bond is a shared pair of electrons.",
        ["H–H: each hydrogen gives one electron to the pair."], "k3-19-pairs"),
   card("c3k19-2", "An atom forms as many bonds as the electrons it needs.",
        ["Oxygen needs {2}: it forms {2} bonds."], "k3-19-bonds"),
   card("c3k19-3", "Two pairs make a double bond; three pairs a triple bond.",
        [E("O=O") + " (double), " + E("N≡N") + " (triple)"], "k3-19-type")],
  [num("k3-19-pairs", 1, "How many pairs of electrons are shared in a molecule of {X.n}, {X.f}?", "X.p",
       ["Count the shared pairs: {X.n} has {X.b} bond(s).", "That is {answer} shared pair(s)."],
       vars={"X": {"pick": MOLS}},
       misc=[("atoms", "X.p * 2", "Count pairs of electrons, not single electrons.")],
       review="authored", sources=SRC),
   num("k3-19-bonds", 1, "How many covalent bonds does a {X.n} atom usually form? ({X.n}: {X.c})", "X.k",
       ["It needs {X.k} more electron(s) to complete its outer shell.", "So it forms {answer} bond(s)."],
       vars={"X": {"pick": [{"n": "hydrogen", "c": "1", "k": 1}, {"n": "chlorine", "c": "2, 8, 7", "k": 1}, {"n": "oxygen", "c": "2, 6", "k": 2},
                            {"n": "nitrogen", "c": "2, 5", "k": 3}, {"n": "carbon", "c": "2, 4", "k": 4}, {"n": "sulphur", "c": "2, 8, 6", "k": 2}]}},
       misc=[("outer", "8 - X.k", "That is the number of outer electrons it already has. Count those it still needs.")],
       review="authored", sources=SRC, where=["8 - X.k != X.k"]),
   bank("k3-19-type", 2, "{X.q}", [
     {"q": "What type of bond holds the two atoms in an oxygen molecule, O₂?", "r": "a double covalent bond", "w": ["a single covalent bond", "an ionic bond", "a triple covalent bond"],
      "e": ["Each oxygen needs two electrons, so two pairs are shared.", "Oxygen atoms are both non-metals: they share.", "That is nitrogen, N₂."], "y": "Two shared pairs: O=O."},
     {"q": "Which molecule contains a triple bond?", "r": "N₂", "w": ["H₂", "Cl₂", "O₂"],
      "e": ["H–H is single.", "Cl–Cl is single.", "O=O is double."], "y": "Each nitrogen needs three electrons: N≡N."},
     {"q": "In a covalent bond, the shared electrons come from…", "r": "both atoms, one electron each", "w": ["the metal atom only", "the nucleus", "a third atom"],
      "e": ["There is no metal in a covalent bond.", "Electrons are outside the nucleus.", "Only the two bonded atoms are involved."], "y": "Each atom gives one electron to the shared pair."}], SRC),
   bank("k3-19-dot", 3, "{X.q}", [
     {"q": "In a dot-and-cross diagram of water, how many electrons are in the outer shell of oxygen?", "r": "8 (two shared pairs and two lone pairs)", "w": ["6", "2", "10"],
      "e": ["Count the shared electrons too.", "That is hydrogen's shell.", "Oxygen's second shell holds at most 8."], "y": "The shared pairs complete oxygen's octet."},
     {"q": "How many lone (non-bonding) pairs are on the nitrogen atom in ammonia, NH₃?", "r": "one", "w": ["none", "two", "three"],
      "e": ["Nitrogen has 5 outer electrons; 3 are used in bonds.", "Only 2 electrons are left over: one pair.", "Three electrons are used in bonding."], "y": "5 − 3 = 2 electrons left: one lone pair."},
     {"q": "Why does hydrogen form only one covalent bond?", "r": "Its only shell is full with two electrons", "w": ["It has no electrons", "It needs eight electrons", "It always loses its electron"],
      "e": ["Hydrogen has one electron.", "Its first shell holds only two.", "In covalent bonds it shares, not loses."], "y": "One shared pair gives hydrogen two electrons, like helium."}], SRC)],
  learn=learn(
    [("Sharing instead of transferring",
      "Two non-metal atoms both want to gain electrons, so neither will give electrons away. Instead they share.\n"
      "Each atom puts one electron into a pair that sits between the two nuclei. The shared pair is attracted by both nuclei: that is the covalent bond.\n"
      "Both atoms count the shared electrons as their own, so both complete their outer shells."),
     ("How many bonds?",
      "An atom forms as many covalent bonds as the electrons it is missing:\n• H ({1}) and Cl ({7}): one bond;\n• O ({6}): two;\n• N ({5}): three;\n• C ({4}): four.\n"
      "So water is H–O–H, ammonia has three N–H bonds, and methane has four C–H bonds.\n"
      "Sometimes two atoms share two pairs (a double bond, O=O, as in CO₂: O=C=O) or three pairs (a triple bond, N≡N)."),
     ("Dot-and-cross diagrams",
      "Draw the outer shells of the atoms overlapping. Put the shared pairs in the overlap: one electron as a dot (from one atom) and one as a cross (from the other).\n"
      "Electrons that are not shared are lone pairs. In water, oxygen has two shared pairs and two lone pairs: {8} electrons in all.")],
    key_words=[("covalent bond", "a pair of electrons shared between two atoms"), ("molecule", "a group of atoms joined by covalent bonds"),
               ("double bond", "two shared pairs"), ("lone pair", "a pair of outer electrons not used in bonding")],
    examples=[E("H–Cl") + ": one shared pair", E("O=C=O") + ": two double bonds", E("NH₃") + ": three single bonds, one lone pair"],
    mistake=("In a covalent bond one atom gives an electron to the other", "In a covalent bond the atoms share a pair of electrons",
             "Transferring electrons is ionic bonding, between a metal and a non-metal.")))

# ---------------------------------------------------------------- 20. Properties of covalent compounds
L.lesson(D, S, 20, ("k3-20", "Properties of covalent (molecular) compounds"), [19],
  "Simple covalent substances are made of small molecules. The bonds inside each molecule are strong, but the forces between molecules are weak. So they:\n"
  "• have low melting and boiling points; many are gases or liquids at room temperature (O₂, CO₂, H₂O, ethanol);\n"
  "• do not conduct electricity in any state (no ions or free electrons);\n"
  "• are often insoluble in water but soluble in organic solvents (kerosene, ethanol), though some (sugar, ethanol, ammonia) dissolve in water;\n"
  "• solids are soft (iodine, wax, sugar).\n"
  "Exception: giant covalent structures (diamond, graphite, sand) have very high melting points.",
  worked({},
         "Explain why water boils at {100} °C while sodium chloride boils at about {1400} °C.",
         ["Boiling water only separates the molecules from one another; the forces between molecules are weak.",
          "Boiling salt means separating ions held by strong ionic bonds throughout the lattice.", "Much less energy is needed for water."],
         "Weak forces between water molecules; strong ionic bonds in salt"),
  [card("c3k20-1", "Weak forces between molecules: low melting and boiling points.",
        ["Carbon dioxide is a gas at room temperature."], "k3-20-mp"),
   card("c3k20-2", "Molecular substances do not conduct: there are no free charged particles.",
        ["Pure water and sugar solution conduct very poorly."], "k3-20-cond"),
   card("c3k20-3", "Many dissolve in organic solvents rather than water.",
        ["Candle wax dissolves in kerosene, not in water."], "k3-20-sol")],
  [bank("k3-20-mp", 1, "{X.q}", [
     {"q": "Why does carbon dioxide have a low boiling point?", "r": "The forces between its molecules are weak", "w": ["The bonds inside the molecule are weak", "It is an ionic compound", "It contains a metal"],
      "e": ["The covalent bonds inside are strong; they do not break when it boils.", "It is covalent.", "Carbon and oxygen are non-metals."], "y": "Boiling separates molecules, which are weakly attracted."},
     {"q": "Which is most likely a simple covalent substance?", "r": "a liquid that boils at 78 °C", "w": ["a solid that melts at 801 °C", "a shiny solid that conducts", "a solid that conducts when molten"],
      "e": ["That is typical of an ionic compound.", "That is a metal.", "That is ionic."], "y": "Low boiling point: weak forces between molecules (ethanol)."},
     {"q": "When ice melts, what is broken?", "r": "the weak forces between water molecules", "w": ["the O–H covalent bonds", "ionic bonds", "the nuclei of the atoms"],
      "e": ["The molecules stay whole: still H₂O.", "Water is not ionic.", "Nuclei are never broken in melting."], "y": "Melting separates molecules, not atoms."}], SRC),
   bank("k3-20-cond", 1, "{X.q}", [
     {"q": "Why does sugar solution not conduct electricity?", "r": "Sugar is made of molecules with no charge", "w": ["Sugar is ionic", "Water blocks the current", "Sugar contains free electrons"],
      "e": ["Sugar is covalent.", "Salt water conducts, so water is not the problem.", "Free electrons would make it conduct."], "y": "No ions are formed when sugar dissolves."},
     {"q": "Which substance does not conduct electricity when molten?", "r": "wax (covalent)", "w": ["sodium chloride", "copper", "potassium bromide"],
      "e": ["Molten NaCl conducts (ions).", "Copper conducts (free electrons).", "Molten KBr conducts (ions)."], "y": "Wax has neither ions nor free electrons."},
     {"q": "Pure water conducts very poorly. Why?", "r": "It is made of covalent molecules with almost no ions", "w": ["It is a metal", "It is ionic", "It is a gas"],
      "e": ["Water is not a metal.", "Water is covalent.", "Water is a liquid at room temperature."], "y": "Without moving ions there is almost no current."}], SRC),
   bank("k3-20-sol", 2, "{X.q}", [
     {"q": "Candle wax is put in kerosene and in water. Where does it dissolve?", "r": "in kerosene", "w": ["in water", "in both", "in neither"],
      "e": ["Wax is covalent and insoluble in water.", "It does not dissolve in water.", "It dissolves in kerosene."], "y": "Covalent substances often dissolve in organic solvents."},
     {"q": "Which covalent substance dissolves well in water?", "r": "sugar", "w": ["wax", "iodine", "petrol"],
      "e": ["Wax is insoluble in water.", "Iodine hardly dissolves in water.", "Petrol floats on water."], "y": "Some covalent molecules, such as sugar and ethanol, dissolve in water."},
     {"q": "Iodine crystals are soft and turn into vapour on gentle heating. This shows that…", "r": "the forces between iodine molecules are weak", "w": ["iodine is ionic", "iodine is a metal", "the I–I bond is weak"],
      "e": ["Ionic solids are hard with high melting points.", "Iodine is a non-metal.", "The molecules stay as I₂; it is the forces between them that are weak."], "y": "Little energy is needed to separate the molecules."}], SRC),
   bank("k3-20-compare", 3, "{X.q}", [
     {"q": "Substance A melts at 801 °C and conducts when molten. Substance B melts at 0 °C and does not conduct. Which is covalent?", "r": "B", "w": ["A", "both", "neither"],
      "e": ["A is ionic.", "A conducts when molten, so it is ionic.", "B has the properties of a molecular substance."], "y": "Low melting point and no conduction: covalent molecules."},
     {"q": "Sand (silicon dioxide) is covalent but melts at about 1700 °C. Why?", "r": "It is a giant covalent structure: many strong bonds must break", "w": ["It is ionic", "It is made of small molecules", "It contains a metal"],
      "e": ["Silicon and oxygen are non-metals.", "Small molecules would melt easily.", "Silicon is a non-metal (metalloid)."], "y": "Giant covalent lattices have very high melting points."},
     {"q": "Which statement about simple covalent substances is FALSE?", "r": "They conduct electricity when molten", "w": ["They have low melting points", "Many are gases or liquids", "Their molecules contain strong bonds"],
      "e": ["True: weak forces between molecules.", "True: oxygen, water, ethanol.", "True: the covalent bonds themselves are strong."], "y": "They have no ions or free electrons, so they do not conduct."}], SRC)],
  learn=learn(
    [("Strong inside, weak outside",
      "In a simple covalent substance, each molecule is held together by strong covalent bonds. But the molecules attract one another only weakly.\n"
      "When the substance melts or boils, only these weak forces between molecules are overcome; the molecules themselves stay whole.\n"
      "So little energy is needed: oxygen, carbon dioxide and methane are gases; water and ethanol are liquids; wax, sugar and iodine are soft solids."),
     ("No conduction",
      "To conduct, a substance needs charged particles that can move. Molecular substances have neither ions nor free electrons, so they do not conduct when solid, liquid or dissolved.\n"
      "That is why plastics, which are covalent, are used to insulate electric wires."),
     ("Solubility, and an important exception",
      "Many covalent substances do not dissolve in water but do dissolve in organic solvents such as kerosene, petrol or ethanol (grease on hands is removed with kerosene). Some, like sugar and ethanol, dissolve in water.\n"
      "Not all covalent substances are molecular: diamond, graphite and sand (silicon dioxide) are giant covalent structures with very high melting points. You will meet them in a later lesson.")],
    key_words=[("molecular (simple covalent) substance", "made of separate small molecules"), ("intermolecular forces", "the weak forces between molecules"),
               ("organic solvent", "a carbon-based liquid such as kerosene or ethanol")],
    examples=["Water: b.p. {100} °C, does not conduct", "Iodine: soft, turns to vapour easily", "Sugar: dissolves in water, solution does not conduct"],
    mistake=("When water boils, the O–H bonds break", "When water boils, the molecules separate; the O–H bonds stay",
             "Steam is still H₂O: only the weak forces between molecules are overcome.")))

# ---------------------------------------------------------------- 21. Shapes of covalent molecules
SHAPES = [{"f": "CH₄", "n": "methane", "s": "tetrahedral", "a": 109.5, "bp": 4, "lp": 0},
          {"f": "NH₃", "n": "ammonia", "s": "pyramidal", "a": 107, "bp": 3, "lp": 1},
          {"f": "H₂O", "n": "water", "s": "bent (V-shaped)", "a": 104.5, "bp": 2, "lp": 2},
          {"f": "CO₂", "n": "carbon dioxide", "s": "linear", "a": 180, "bp": 2, "lp": 0},
          {"f": "BF₃", "n": "boron trifluoride", "s": "trigonal planar", "a": 120, "bp": 3, "lp": 0},
          {"f": "BeCl₂", "n": "beryllium chloride", "s": "linear", "a": 180, "bp": 2, "lp": 0}]
L.lesson(D, S, 21, ("k3-21", "Shapes of simple covalent molecules (VSEPR)"), [19],
  "VSEPR (valence shell electron pair repulsion): pairs of electrons around the central atom repel each other and get as far apart as possible.\n"
  "• 2 bonding groups: linear, 180° (CO₂, BeCl₂).\n• 3 bonding pairs: trigonal planar, 120° (BF₃).\n• 4 bonding pairs: tetrahedral, 109.5° (CH₄).\n"
  "• Lone pairs repel more than bonding pairs, squeezing the bonds closer:\n  NH₃ (3 bonding, 1 lone pair): pyramidal, about 107°; H₂O (2 bonding, 2 lone pairs): bent, about 104.5°.",
  worked({},
         "Predict the shape and bond angle of methane, CH₄.",
         ["Carbon has {4} bonding pairs and no lone pairs.", "Four pairs get furthest apart pointing to the corners of a tetrahedron.", "The bond angle is {109.5}°."],
         "Tetrahedral, {109.5}°"),
  [card("c3k21-1", "Electron pairs around a central atom repel and spread out as far as possible.",
        ["Four pairs → tetrahedral, {109.5}°"], "k3-21-shape"),
   card("c3k21-2", "Lone pairs repel more strongly than bonding pairs.",
        ["NH₃: {107}°; H₂O: {104.5}°"], "k3-21-angle"),
   card("c3k21-3", "Two bonding groups with no lone pairs give a straight (linear) molecule.",
        [E("O=C=O") + ": {180}°"], "k3-21-pairs")],
  [mcq("k3-21-shape", 1, "What is the shape of a molecule of {X.n}, {X.f}?", "{X.s}",
       [("{X.s == 'tetrahedral' ? 'trigonal planar' : 'tetrahedral'}", "w1"), ("{X.s == 'linear' ? 'bent (V-shaped)' : 'linear'}", "w2"), ("{X.s == 'pyramidal' ? 'bent (V-shaped)' : 'pyramidal'}", "w3")],
       ["The central atom has {X.bp} bonding group(s) and {X.lp} lone pair(s).", "So the shape is {answer}."],
       vars={"X": {"pick": SHAPES}},
       misc=[("w1", "Count the electron pairs round the centre: {X.bp} bonding and {X.lp} lone."), ("w2", "Count the pairs: {X.bp} bonding and {X.lp} lone pair(s)."),
             ("w3", "Count the pairs: {X.bp} bonding and {X.lp} lone pair(s).")],
       review="authored", sources=SRC),
   num("k3-21-angle", 2, "What is the bond angle in a molecule of {X.n}, {X.f} (degrees)?", "X.a",
       ["Shape: {X.s} ({X.bp} bonding pair(s), {X.lp} lone pair(s)).", "Bond angle: {answer}°."],
       vars={"X": {"pick": SHAPES[:5]}},
       misc=[("tet", "109.5", "That is the tetrahedral angle. Lone pairs or fewer pairs change it.")],
       unit="°", review="authored", sources=SRC, where=["X.a != 109.5"]),
   num("k3-21-pairs", 1, "How many lone pairs are on the central atom of {X.n}, {X.f}?", "X.lp",
       ["Central atom: {X.bp} bonding pair(s).", "Lone pairs: {answer}."],
       vars={"X": {"pick": SHAPES[:4]}},
       misc=[("bp", "X.bp", "That is the number of bonding pairs. Lone pairs are not used in bonds.")],
       review="authored", sources=SRC, where=["X.bp != X.lp"]),
   bank("k3-21-why", 3, "{X.q}", [
     {"q": "Why is the bond angle in water (104.5°) smaller than in methane (109.5°)?", "r": "Water's two lone pairs repel the bonding pairs more strongly", "w": ["Water has more bonds than methane", "Oxygen is smaller than hydrogen", "Water is ionic"],
      "e": ["Water has two bonds; methane has four.", "Size is not the reason here.", "Water is covalent."], "y": "Lone pairs push the O–H bonds closer together."},
     {"q": "Why is carbon dioxide linear?", "r": "The two double bonds repel each other and get as far apart as possible: 180°", "w": ["Carbon has two lone pairs", "Oxygen atoms attract each other", "It has four bonds in a square"],
      "e": ["Carbon has no lone pairs in CO₂.", "Like electron groups repel; that makes it straight.", "The two groups point opposite ways."], "y": "Two groups of electrons, no lone pairs: linear."},
     {"q": "BF₃ is trigonal planar but NH₃ is pyramidal. Why?", "r": "Nitrogen has a lone pair; boron has none", "w": ["Boron has a lone pair", "NH₃ has four bonds", "Fluorine is larger than hydrogen"],
      "e": ["Boron has no lone pair in BF₃.", "NH₃ has three bonds.", "Atom size does not explain the shape."], "y": "The lone pair on nitrogen pushes the three bonds down into a pyramid."}], SRC)],
  learn=learn(
    [("Electron pairs push apart",
      "Electron pairs are all negatively charged, so they repel. Around a central atom they arrange themselves to be as far apart as possible.\n"
      "This idea is VSEPR: valence shell electron pair repulsion. It lets us predict the shape of a molecule from the number of electron pairs around the centre."),
     ("The basic shapes",
      "• Two groups (CO₂, BeCl₂): opposite sides, linear, {180}°.\n• Three pairs (BF₃): flat triangle, trigonal planar, {120}°.\n"
      "• Four pairs (CH₄): pointing to the corners of a tetrahedron, {109.5}°. A tetrahedron is a pyramid with a triangular base: the molecule is three-dimensional.\n"
      "A double bond counts as one group when predicting shape."),
     ("Lone pairs squeeze the angle",
      "Lone pairs repel more strongly than bonding pairs.\n"
      "• Ammonia, NH₃: three bonding pairs and one lone pair → pyramidal, about {107}°.\n"
      "• Water, H₂O: two bonding pairs and two lone pairs → bent (V-shaped), about {104.5}°.\n"
      "The shape of water molecules explains many of its special properties.")],
    key_words=[("VSEPR", "electron pairs repel and spread as far apart as possible"), ("bond angle", "the angle between two bonds at the central atom"),
               ("tetrahedral", "four pairs pointing to the corners of a tetrahedron"), ("lone pair", "a non-bonding pair that still takes up space")],
    examples=["CH₄: tetrahedral, {109.5}°", "NH₃: pyramidal, {107}°", "H₂O: bent, {104.5}°", "CO₂: linear, {180}°"],
    mistake=("Water is linear like carbon dioxide", "Water is bent (about {104.5}°) because of its two lone pairs",
             "The lone pairs on oxygen push the two O–H bonds together.")))

# ---------------------------------------------------------------- 22. Metallic bonding
L.lesson(D, S, 22, ("k3-22", "The metallic bond: formation"), [16],
  "In a metal, each atom releases its outer (valence) electrons. The atoms become positive ions arranged in a regular lattice, and the released electrons move freely among them: a 'sea' of delocalised electrons.\n"
  "The metallic bond is the attraction between the positive ions and the sea of electrons.\n"
  "• Sodium gives 1 electron per atom, magnesium 2, aluminium 3: more delocalised electrons and higher ion charge give a stronger bond (aluminium melts higher than sodium).\n"
  "• The bond is not between particular pairs of atoms: it holds the whole lattice together.",
  worked({"z": 12},
         "Describe the bonding in magnesium (atomic number {z}).",
         ["Magnesium ({shells(z)}) releases its {outerElectrons(z)} outer electrons.", "It becomes Mg²⁺ ions in a regular lattice.",
          "The released electrons move freely between the ions; the ions are held by attraction to this sea of electrons."],
         "Mg²⁺ ions in a sea of delocalised electrons", checks=["outerElectrons(z) == 2"]),
  [card("c3k22-1", "Metal atoms release their outer electrons into a shared sea.",
        ["Each sodium atom gives {1} electron."], "k3-22-e"),
   card("c3k22-2", "The metallic bond: positive ions attracted to delocalised electrons.",
        ["The electrons are not attached to any one ion."], "k3-22-what"),
   card("c3k22-3", "More delocalised electrons per atom: a stronger metallic bond.",
        ["Aluminium ({3}) melts higher than sodium ({1})."], "k3-22-strong")],
  [num("k3-22-e", 1, "How many electrons does each {nameOf(X)} atom (atomic number {atomicNumber(X)}) give to the sea of electrons?", "outerElectrons(atomicNumber(X))",
       ["Configuration: {shells(atomicNumber(X))}.", "It releases its {answer} outer electron(s)."],
       vars={"X": {"pick": ["Li", "Na", "K", "Be", "Mg", "Ca", "Al"]}},
       misc=[("all", "atomicNumber(X)", "Only the outer electrons are released; inner electrons stay with the ion.")],
       sources=SRC),
   bank("k3-22-what", 1, "{X.q}", [
     {"q": "What is a metallic bond?", "r": "The attraction between positive metal ions and a sea of delocalised electrons", "w": ["A shared pair of electrons between two atoms", "The attraction between positive and negative ions", "A weak force between molecules"],
      "e": ["That is a covalent bond.", "That is an ionic bond; there are no negative ions in a metal.", "Metallic bonds are strong."], "y": "Delocalised electrons hold the ions together."},
     {"q": "In a lump of sodium, what particles make up the lattice?", "r": "Na⁺ ions surrounded by free electrons", "w": ["Na atoms sharing pairs of electrons", "Na⁺ and Cl⁻ ions", "Na₂ molecules"],
      "e": ["Metals do not form shared pairs between atoms.", "There is no chlorine.", "Sodium is not made of molecules."], "y": "Each atom gives up its outer electron to the sea."},
     {"q": "What does 'delocalised' mean for the electrons in a metal?", "r": "They are free to move through the whole lattice", "w": ["They are fixed to one atom", "They are lost from the metal", "They are in the nucleus"],
      "e": ["Those would be localised.", "They stay in the metal.", "Electrons are never in the nucleus."], "y": "They belong to the whole lattice, not one ion."}], SRC),
   num("k3-22-charge", 2, "What is the charge on the ions in the lattice of {nameOf(X)}? (atomic number {atomicNumber(X)})", "outerElectrons(atomicNumber(X))",
       ["{nameOf(X)} releases {outerElectrons(atomicNumber(X))} electron(s) per atom.", "So the ions are +{answer}."],
       vars={"X": {"pick": ["Na", "K", "Mg", "Ca", "Al"]}},
       misc=[("neg", "0 - outerElectrons(atomicNumber(X))", "Losing electrons makes positive ions.")],
       sources=SRC, signed=True),
   bank("k3-22-strong", 3, "{X.q}", [
     {"q": "Aluminium (660 °C) melts at a higher temperature than sodium (98 °C). Why?", "r": "Each Al atom gives 3 electrons and forms Al³⁺, so the attraction is stronger", "w": ["Aluminium is ionic", "Sodium has more delocalised electrons", "Aluminium is made of molecules"],
      "e": ["Aluminium is a metal: metallic bonding.", "Sodium gives only 1 electron per atom.", "Metals are not molecular."], "y": "More electrons in the sea and higher charge on the ions: stronger metallic bonding."},
     {"q": "Which metal would you expect to have the strongest metallic bonding?", "r": "aluminium", "w": ["sodium", "potassium", "lithium"],
      "e": ["Sodium gives 1 electron per atom.", "Potassium gives 1 and has larger ions.", "Lithium gives 1 electron per atom."], "y": "Aluminium gives 3 electrons per atom."},
     {"q": "Why are metal ions not pushed apart, even though they are all positive?", "r": "The sea of electrons between them holds them together", "w": ["They are neutral", "They share pairs of electrons", "They are held by negative ions"],
      "e": ["They are positive ions.", "The electrons are not in fixed pairs.", "There are no negative ions in a pure metal."], "y": "The negative electron sea attracts all the ions."}], SRC)],
  learn=learn(
    [("Atoms that give up electrons",
      "Metal atoms have only {1}, {2} or {3} outer electrons, held loosely. In a piece of metal, every atom lets its outer electrons go.\n"
      "The atoms become positive ions, packed tightly in a regular pattern (a lattice). The released electrons are free to move anywhere in the metal: they are delocalised."),
     ("The sea of electrons",
      "Picture rows of positive ions sitting in a 'sea' of moving electrons. The ions are attracted to the negative sea all around them.\n"
      "This attraction is the metallic bond. It does not join particular pairs of atoms; it holds the whole lattice together, which is why metals are strong."),
     ("Stronger and weaker metallic bonds",
      "The more electrons each atom puts into the sea, and the higher the charge on the ions, the stronger the bonding.\n"
      "• Sodium (Na⁺, {1} electron each) is soft and melts at {98} °C.\n• Magnesium (Mg²⁺, {2} each) melts at {650} °C.\n• Aluminium (Al³⁺, {3} each) melts at {660} °C.")],
    key_words=[("metallic bond", "attraction between metal ions and delocalised electrons"), ("delocalised electrons", "electrons free to move through the whole metal"),
               ("lattice", "a regular repeating arrangement of particles")],
    examples=["Potassium: K⁺ ions, {1} free electron per atom", "Calcium: Ca²⁺ ions, {2} free electrons per atom"],
    mistake=("A metal is held together by negative ions", "A metal has positive ions held by a sea of free electrons",
             "Metal atoms lose electrons; there are no negative ions in a pure metal.")))

# ---------------------------------------------------------------- 23. Properties of metals
L.lesson(D, S, 23, ("k3-23", "Properties of metals explained by metallic bonding"), [22],
  "Metallic bonding explains the properties of metals:\n"
  "• Good conductors of electricity: delocalised electrons move through the metal and carry the current.\n"
  "• Good conductors of heat: free electrons and vibrating ions pass on energy.\n"
  "• Malleable (can be hammered into shape) and ductile (can be drawn into wires): layers of ions can slide over each other without breaking the bond, because the electron sea moves with them.\n"
  "• Usually high melting points and high density; shiny (lustrous) when freshly cut; sonorous (ring when struck).\n"
  "Uses: copper for wires, aluminium for cooking pots and power cables, iron (steel) for building.",
  worked({},
         "Explain why copper is used for electric wires.",
         ["Copper has metallic bonding with many delocalised electrons.", "These electrons can move through the metal, carrying an electric current.",
          "Copper is also ductile, so it can be drawn into thin wires."], "It conducts well (free electrons) and is ductile"),
  [card("c3k23-1", "Free electrons carry electric current through a metal.",
        ["Copper and aluminium cables"], "k3-23-cond"),
   card("c3k23-2", "Layers of ions slide without breaking the bond: malleable and ductile.",
        ["Gold can be beaten into very thin sheets."], "k3-23-mall"),
   card("c3k23-3", "Each property suits a use.",
        ["Aluminium pots conduct heat well and do not rust."], "k3-23-use")],
  [bank("k3-23-cond", 1, "{X.q}", [
     {"q": "Why do metals conduct electricity when solid?", "r": "Their delocalised electrons can move", "w": ["Their ions can move", "They contain water", "Their atoms share pairs of electrons"],
      "e": ["In a solid metal the ions stay in place.", "Metals conduct when dry.", "Shared pairs are fixed; they cannot carry current."], "y": "Moving free electrons carry the current."},
     {"q": "Why do metals conduct heat well?", "r": "Free electrons and vibrating ions pass on energy quickly", "w": ["Metals are always hot", "Metals contain air", "Metals have no electrons"],
      "e": ["Metals are not always hot.", "Metals are dense, not airy.", "Metals have many free electrons."], "y": "That is why cooking pots are made of metal."},
     {"q": "Which material is best for an electric cable?", "r": "copper", "w": ["glass", "plastic", "rubber"],
      "e": ["Glass is an insulator.", "Plastic is used to insulate the cable.", "Rubber is an insulator."], "y": "Copper has many free electrons."}], SRC),
   bank("k3-23-mall", 1, "{X.q}", [
     {"q": "What does 'malleable' mean?", "r": "can be hammered into shape without breaking", "w": ["can be drawn into wires", "breaks easily", "conducts heat"],
      "e": ["That is ductile.", "That is brittle.", "That is thermal conductivity."], "y": "Blacksmiths hammer iron into tools."},
     {"q": "Why can metals be bent without breaking?", "r": "Layers of ions slide over each other and the electron sea keeps them bonded", "w": ["Metals have no bonds", "Metals are made of molecules", "The ions repel when moved"],
      "e": ["Metals have strong bonds.", "Metals are not molecular.", "The sea of electrons stops the ions repelling apart."], "y": "The bonding is not fixed between particular atoms."},
     {"q": "What does 'ductile' mean?", "r": "can be drawn out into a wire", "w": ["can be hammered flat", "is shiny", "rings when struck"],
      "e": ["That is malleable.", "That is lustrous.", "That is sonorous."], "y": "Copper is drawn into thin wires."}], SRC),
   bank("k3-23-use", 2, "Which property of the metal explains this use? {X.q}", [
     {"q": "Aluminium is used to make cooking pots.", "r": "good conductor of heat", "w": ["high density", "magnetic", "low melting point"],
      "e": ["Aluminium is light, not dense.", "Aluminium is not magnetic.", "Its melting point is high enough for cooking."], "y": "Heat passes quickly from the fire to the food."},
     {"q": "Iron sheets are used for roofing in Bamenda.", "r": "strong and malleable (can be pressed into corrugated sheets)", "w": ["good conductor of electricity", "low density", "shiny when cut"],
      "e": ["Conductivity is not why it is used for roofs.", "Iron is fairly dense.", "Roofing is painted or galvanised, not chosen for shine."], "y": "It can be shaped and is strong."},
     {"q": "Gold is used in jewellery.", "r": "shiny (lustrous) and does not corrode", "w": ["good conductor of heat", "high density", "brittle"],
      "e": ["Conductivity is not why jewellery is gold.", "Density is not the reason.", "Gold is malleable, not brittle."], "y": "It stays bright and attractive."}], SRC),
   bank("k3-23-compare", 3, "{X.q}", [
     {"q": "A sheet of metal is hammered and bends; a crystal of salt is hammered and shatters. Why the difference?", "r": "In salt, shifting layers brings like charges together; in a metal the electron sea keeps the ions bonded", "w": ["Salt is a metal", "Metals have no bonds", "Salt has free electrons"],
      "e": ["Salt is ionic.", "Metals have strong metallic bonds.", "Salt has no free electrons."], "y": "Ionic lattices are brittle; metallic lattices are malleable."},
     {"q": "Which property of metals is NOT explained by free electrons?", "r": "high density", "w": ["electrical conductivity", "thermal conductivity", "shininess"],
      "e": ["Free electrons carry current.", "Free electrons carry heat.", "Free electrons reflect light, making metals shiny."], "y": "Density depends on how heavy the ions are and how closely they pack."},
     {"q": "Why is aluminium, not copper, used for overhead power cables?", "r": "It conducts well and is much less dense, so the cables are lighter", "w": ["It conducts better than copper", "It is more dense", "It is an insulator"],
      "e": ["Copper conducts slightly better.", "It is less dense.", "Aluminium is a conductor."], "y": "Light cables need fewer, cheaper pylons."}], SRC)],
  learn=learn(
    [("Conducting electricity and heat",
      "The delocalised electrons in a metal are free to move. When a battery is connected, they drift through the metal: that is an electric current. So metals conduct electricity even when solid.\n"
      "They also carry heat energy quickly from hot parts to cold parts, together with the vibrating ions. That is why a metal spoon in hot tea soon feels hot."),
     ("Bending without breaking",
      "When a metal is hammered, the layers of ions slide over each other. The sea of electrons moves with them, so the bonding is not broken.\n"
      "So metals are malleable (can be hammered into sheets, such as roofing sheets) and ductile (can be drawn into wires, such as copper wire).\n"
      "Compare an ionic crystal: when its layers shift, like charges meet, repel, and it shatters."),
     ("Other properties and uses",
      "• Shiny when freshly cut (lustrous) and ringing when struck (sonorous).\n• Usually high melting points and high densities (but sodium and potassium are soft, light and low-melting).\n"
      "Uses follow from properties: copper wires (conducts, ductile), aluminium pots and cables (conducts heat and electricity, light), iron and steel for building (strong).")],
    key_words=[("malleable", "can be hammered into shape"), ("ductile", "can be drawn into wires"), ("lustrous", "shiny"),
               ("conductor", "a material that lets electricity or heat pass through easily")],
    examples=["Copper: electric wires", "Aluminium: pots and overhead cables", "Steel: bridges and roofing"],
    mistake=("Metals conduct because their ions move", "Metals conduct because their delocalised electrons move",
             "In a solid metal the ions stay in place; only the electrons move freely.")))

# ---------------------------------------------------------------- 24. Crystals
L.lesson(D, S, 24, ("k3-24", "Crystals: definition and types of crystal structure"), [18, 20, 22],
  "A crystal is a solid whose particles are arranged in a regular, repeating pattern (a lattice). Crystals have flat faces, straight edges and sharp angles.\n"
  "Types of crystal structure, by the particles and bonds:\n"
  "• Ionic: positive and negative ions (NaCl, cubic crystals).\n• Giant covalent (macromolecular): atoms joined by covalent bonds throughout (diamond, graphite, quartz).\n"
  "• Simple molecular: molecules held by weak forces (ice, iodine, sugar).\n• Metallic: positive ions in a sea of electrons (copper, iron).\n"
  "Crystals can be grown by slowly cooling or evaporating a saturated solution (e.g. copper(II) sulphate).",
  worked({},
         "Classify the crystals of common salt, ice, diamond and copper.",
         ["Salt: Na⁺ and Cl⁻ ions → ionic.", "Ice: H₂O molecules → simple molecular.", "Diamond: carbon atoms all covalently bonded → giant covalent.", "Copper: Cu²⁺ ions in a sea of electrons → metallic."],
         "ionic, simple molecular, giant covalent, metallic"),
  [card("c3k24-1", "A crystal has a regular, repeating arrangement of particles.",
        ["Salt crystals are tiny cubes."], "k3-24-def"),
   card("c3k24-2", "Four types: ionic, giant covalent, simple molecular, metallic.",
        ["Quartz (sand) is giant covalent."], "k3-24-type"),
   card("c3k24-3", "Grow crystals by slowly cooling or evaporating a saturated solution.",
        ["Slow cooling gives larger crystals."], "k3-24-grow")],
  [bank("k3-24-def", 1, "{X.q}", [
     {"q": "What is a crystal?", "r": "a solid with its particles in a regular, repeating pattern", "w": ["any shiny solid", "a liquid that has frozen quickly", "a mixture of solids"],
      "e": ["Shininess is not the definition.", "Quick freezing can give no crystals at all.", "A crystal is one substance in a regular pattern."], "y": "The regular lattice gives flat faces and sharp edges."},
     {"q": "Which feature shows that a solid is crystalline?", "r": "flat faces and sharp, regular angles", "w": ["a rough, irregular surface", "it is soft", "it is coloured"],
      "e": ["Irregular surfaces suggest no regular pattern.", "Hardness does not decide it.", "Colour does not decide it."], "y": "The outer shape reflects the regular arrangement inside."},
     {"q": "What shape are common salt crystals?", "r": "cubes", "w": ["needles", "spheres", "hexagonal plates"],
      "e": ["Salt crystals are not needle-shaped.", "Crystals have flat faces.", "Salt's lattice is cubic."], "y": "Na⁺ and Cl⁻ pack in a cubic lattice."}], SRC),
   bank("k3-24-type", 1, "What type of crystal structure has {X.q}?", [
     {"q": "sodium chloride", "r": "ionic", "w": ["metallic", "simple molecular", "giant covalent"],
      "e": ["There is no free electron sea.", "It is made of ions, not molecules.", "It has ions, not a network of covalent bonds."], "y": "A lattice of Na⁺ and Cl⁻ ions."},
     {"q": "ice", "r": "simple molecular", "w": ["ionic", "giant covalent", "metallic"],
      "e": ["Water is covalent.", "Ice melts at 0 °C: weak forces between molecules.", "Water is not a metal."], "y": "H₂O molecules held by weak forces."},
     {"q": "quartz (silicon dioxide)", "r": "giant covalent", "w": ["simple molecular", "ionic", "metallic"],
      "e": ["Quartz melts at about 1700 °C: not small molecules.", "Silicon and oxygen are non-metals.", "It has no free electrons."], "y": "Every atom is covalently bonded to its neighbours throughout."},
     {"q": "iron", "r": "metallic", "w": ["ionic", "giant covalent", "simple molecular"],
      "e": ["Iron alone has no negative ions.", "Iron atoms are not joined by shared pairs.", "Iron is not molecular."], "y": "Fe ions in a sea of delocalised electrons."}], SRC),
   bank("k3-24-grow", 2, "{X.q}", [
     {"q": "How can large crystals of copper(II) sulphate be grown?", "r": "Let a hot saturated solution cool slowly", "w": ["Boil the solution to dryness quickly", "Add more water", "Freeze it quickly"],
      "e": ["Fast evaporation gives tiny crystals.", "Adding water dissolves crystals.", "Fast cooling gives small crystals."], "y": "Slow cooling lets particles join the lattice in order."},
     {"q": "Why do slowly cooled solutions give larger crystals?", "r": "Particles have time to join the lattice in a regular way", "w": ["The particles get bigger", "Slow cooling adds more solute", "The solvent becomes solid"],
      "e": ["The particles themselves do not grow.", "No solute is added.", "The water stays liquid."], "y": "Fewer, larger crystals grow when particles are added gradually."},
     {"q": "What is a saturated solution?", "r": "one that cannot dissolve any more solute at that temperature", "w": ["one with no solute", "one that has boiled", "any coloured solution"],
      "e": ["That is pure solvent.", "Boiling does not define it.", "Colour does not define it."], "y": "Cooling a saturated solution makes crystals form."}], SRC),
   bank("k3-24-link", 3, "{X.q}", [
     {"q": "A crystal melts at 1600 °C, does not conduct when molten, and is very hard. Its structure is…", "r": "giant covalent", "w": ["ionic", "metallic", "simple molecular"],
      "e": ["A molten ionic compound conducts.", "Metals conduct.", "Simple molecular substances melt easily."], "y": "Very high melting point and no conduction: giant covalent."},
     {"q": "A crystal melts at 115 °C and does not conduct. Its structure is…", "r": "simple molecular", "w": ["ionic", "giant covalent", "metallic"],
      "e": ["Ionic crystals melt much higher.", "Giant covalent crystals melt much higher.", "Metals conduct."], "y": "Low melting point: weak forces between molecules (sulphur)."},
     {"q": "A crystal conducts electricity as a solid and is malleable. Its structure is…", "r": "metallic", "w": ["ionic", "giant covalent", "simple molecular"],
      "e": ["Solid ionic crystals do not conduct.", "Most giant covalent crystals do not conduct and are brittle.", "Molecular crystals do not conduct."], "y": "Free electrons: metallic."}], SRC)],
  learn=learn(
    [("Order inside, shape outside",
      "In a crystal, the particles (atoms, ions or molecules) are arranged in a regular pattern that repeats in every direction: a lattice.\n"
      "Because of this inner order, crystals have flat faces, straight edges and fixed angles. Salt grains seen under a hand lens are little cubes."),
     ("Four kinds of crystal",
      "Crystals are grouped by what the particles are and how they are bonded:\n"
      "• Ionic: positive and negative ions (salt, magnesium oxide).\n• Giant covalent: a network of covalently bonded atoms (diamond, graphite, quartz in sand).\n"
      "• Simple molecular: separate molecules held by weak forces (ice, iodine, sugar).\n• Metallic: metal ions in a sea of electrons (copper, iron, gold).\n"
      "The type of crystal tells you a lot about its properties."),
     ("Growing crystals",
      "Dissolve as much copper(II) sulphate as possible in hot water to make a saturated solution, filter it, and leave it to cool slowly or evaporate slowly.\n"
      "Blue crystals form as the water can no longer hold all the solute. Slow cooling gives large, well-shaped crystals; fast cooling gives many tiny ones.")],
    key_words=[("crystal", "a solid with a regular, repeating arrangement of particles"), ("lattice", "the repeating pattern of particles"),
               ("saturated solution", "a solution that can dissolve no more solute at that temperature")],
    examples=["Salt: ionic cubes", "Sugar: simple molecular crystals", "Diamond: giant covalent", "Copper: metallic"],
    mistake=("All crystals are made of ions", "Crystals can be made of ions, atoms, molecules or metal ions",
             "Ice and sugar crystals contain molecules; diamond contains atoms.")))

# ---------------------------------------------------------------- 25. Properties related to bond type and structure
L.lesson(D, S, 25, ("k3-25", "Properties of substances related to bond type and structure"), [24],
  "Bond type and structure decide physical properties:\n"
  "• Ionic lattice: high m.p.; conducts when molten or dissolved; often soluble in water; brittle.\n"
  "• Simple molecular: low m.p./b.p.; does not conduct; often insoluble in water, soluble in organic solvents.\n"
  "• Giant covalent: very high m.p.; hard (diamond) or slippery (graphite); does not conduct (except graphite); insoluble.\n"
  "• Metallic: high m.p. (usually); conducts when solid and liquid; malleable and ductile; insoluble.\n"
  "Use test results (melting point, conductivity, solubility) to identify the structure of an unknown substance.",
  worked({},
         "Substance X melts at {1083} °C, conducts electricity as a solid and is ductile. Identify its structure.",
         ["Conducts as a solid: only metals (and graphite) do this.", "Ductile: metals can be drawn into wires.", "So X is metallic (it is copper)."],
         "Metallic"),
  [card("c3k25-1", "Conducts when solid: metallic (or graphite).",
        ["Copper and graphite conduct as solids."], "k3-25-cond"),
   card("c3k25-2", "Conducts only when molten or dissolved: ionic.",
        ["Molten salt conducts; solid salt does not."], "k3-25-ionic"),
   card("c3k25-3", "Low melting point and no conduction: simple molecular.",
        ["Wax, sugar, iodine"], "k3-25-mol")],
  [bank("k3-25-cond", 1, "{X.q}", [
     {"q": "Which substance conducts electricity when solid?", "r": "copper", "w": ["sodium chloride", "sugar", "diamond"],
      "e": ["Solid salt has fixed ions.", "Sugar is molecular.", "Diamond has no free electrons."], "y": "Metals have delocalised electrons."},
     {"q": "Which non-metal conducts electricity?", "r": "graphite", "w": ["diamond", "sulphur", "iodine"],
      "e": ["All of diamond's electrons are in bonds.", "Sulphur is a molecular insulator.", "Iodine is a molecular insulator."], "y": "Graphite has one free electron per carbon atom."},
     {"q": "A substance conducts both when solid and when molten. It is most likely…", "r": "a metal", "w": ["an ionic compound", "a molecular compound", "diamond"],
      "e": ["Solid ionic compounds do not conduct.", "Molecular compounds never conduct.", "Diamond does not conduct."], "y": "Free electrons conduct in both states."}], SRC),
   bank("k3-25-ionic", 1, "{X.q}", [
     {"q": "Which result shows that a substance is ionic?", "r": "It conducts when molten but not when solid", "w": ["It conducts when solid", "It never conducts", "It melts below 100 °C"],
      "e": ["That suggests a metal.", "That suggests a covalent substance.", "Ionic compounds melt at high temperatures."], "y": "Ions are free to move only in the melt or solution."},
     {"q": "Potassium iodide dissolves in water and the solution conducts. KI is…", "r": "ionic", "w": ["metallic", "simple molecular", "giant covalent"],
      "e": ["It is a compound of a metal and a non-metal; it dissolves, unlike metals.", "Its solution conducts, so it has ions.", "Giant covalent substances are insoluble."], "y": "A metal + non-metal compound that conducts in solution."},
     {"q": "Why is magnesium oxide used to line furnaces?", "r": "Its ionic lattice gives a very high melting point", "w": ["It conducts electricity", "It is a gas", "It is soft"],
      "e": ["Conductivity is not the reason.", "It is a solid.", "Hardness and high melting point are needed."], "y": "Strong ionic bonds withstand the heat."}], SRC),
   bank("k3-25-mol", 2, "{X.q}", [
     {"q": "A white solid melts at 186 °C, does not conduct and dissolves in water. It is most likely…", "r": "simple molecular (sugar)", "w": ["ionic", "metallic", "giant covalent"],
      "e": ["An ionic solution would conduct.", "Metals conduct.", "Giant covalent substances melt much higher and are insoluble."], "y": "Low melting point and no conduction: molecular."},
     {"q": "Which substance has the lowest melting point?", "r": "methane (simple molecular)", "w": ["sodium chloride (ionic)", "iron (metallic)", "diamond (giant covalent)"],
      "e": ["Ionic bonds are strong.", "Metallic bonds are strong.", "Diamond has very strong covalent bonds throughout."], "y": "Only weak forces hold methane molecules together."},
     {"q": "Why does sulphur not conduct electricity, even when molten?", "r": "It is made of molecules with no ions or free electrons", "w": ["It is a metal", "Its ions are fixed", "It is a gas"],
      "e": ["Sulphur is a non-metal.", "Sulphur has no ions.", "It is a solid at room temperature."], "y": "No charged particles can move."}], SRC),
   bank("k3-25-table", 3, "{X.q}", [
     {"q": "Which set of properties fits an ionic compound?", "r": "high m.p., soluble in water, conducts in solution", "w": ["low m.p., insoluble, no conduction", "high m.p., conducts as a solid, malleable", "very high m.p., insoluble, never conducts"],
      "e": ["That fits a simple molecular substance.", "That fits a metal.", "That fits a giant covalent substance such as diamond."], "y": "Ionic: strong bonds, ions free in solution."},
     {"q": "Which set of properties fits a giant covalent substance like sand?", "r": "very high m.p., insoluble, does not conduct", "w": ["low m.p., soluble in kerosene", "conducts as a solid, malleable", "conducts when molten only"],
      "e": ["That is molecular.", "That is metallic.", "That is ionic."], "y": "Many strong covalent bonds and no free charges."},
     {"q": "Which set of properties fits a metal?", "r": "conducts as a solid, malleable, usually high m.p.", "w": ["brittle, conducts when molten only", "low m.p., does not conduct", "very hard, does not conduct"],
      "e": ["That is ionic.", "That is molecular.", "That is diamond-like."], "y": "Free electrons and sliding layers."}], SRC)],
  learn=learn(
    [("Structure explains properties",
      "Every property you test in the laboratory comes back to the particles and the forces between them.\n"
      "• Strong forces throughout a giant structure → high melting point.\n• Weak forces between small molecules → low melting point.\n"
      "• Charged particles that can move → electrical conductivity."),
     ("The four patterns",
      "• Ionic: high m.p.; conducts only when molten or dissolved; often soluble in water; brittle.\n"
      "• Simple molecular: low m.p.; never conducts; often insoluble in water but soluble in organic solvents.\n"
      "• Giant covalent: very high m.p.; insoluble; does not conduct (graphite is the exception).\n"
      "• Metallic: usually high m.p.; conducts as solid and liquid; malleable and ductile; insoluble."),
     ("Identifying an unknown",
      "Test three things: melting point, conductivity (solid, molten, in solution) and solubility.\n"
      "Conducts when solid → metallic (or graphite). Conducts only when molten or dissolved → ionic. Low melting point and never conducts → simple molecular. Very high melting point, insoluble, does not conduct → giant covalent.")],
    key_words=[("melting point", "the temperature at which a solid becomes a liquid"), ("conductivity", "how well a substance lets electricity through"),
               ("solubility", "how well a substance dissolves")],
    examples=["Salt: ionic", "Candle wax: molecular", "Sand: giant covalent", "Iron: metallic"],
    mistake=("All substances with high melting points are ionic", "Giant covalent and metallic substances also have high melting points",
             "Use conductivity too: it separates ionic, metallic and giant covalent substances.")))

# ---------------------------------------------------------------- 26. Diamond and graphite
L.lesson(D, S, 26, ("k3-26", "Giant covalent structures: diamond and graphite"), [24, 25],
  "Diamond and graphite are both pure carbon (allotropes) but have different structures.\n"
  "• Diamond: each carbon is covalently bonded to 4 others in a rigid 3-D tetrahedral network. Very hard, very high m.p., does not conduct (no free electrons). Uses: cutting and drilling tools, jewellery.\n"
  "• Graphite: each carbon bonded to 3 others in flat hexagonal layers; the fourth electron is delocalised. Layers are held by weak forces and slide over each other. Soft and slippery, conducts electricity, high m.p. Uses: pencil 'lead', lubricant, electrodes.",
  worked({},
         "Explain why graphite conducts electricity but diamond does not.",
         ["In diamond, all four outer electrons of each carbon are used in covalent bonds: none are free.",
          "In graphite, each carbon uses only {3} electrons in bonds; the {4}th is delocalised along the layers.", "These free electrons carry the current."],
         "Graphite has one free electron per carbon atom; diamond has none"),
  [card("c3k26-1", "Diamond: each carbon bonded to {4} others in a rigid network.",
        ["The hardest natural substance"], "k3-26-bonds"),
   card("c3k26-2", "Graphite: layers of carbon (each bonded to {3}) that slide over each other.",
        ["Pencil marks are layers of graphite left on paper."], "k3-26-prop"),
   card("c3k26-3", "Graphite conducts because each carbon has {1} free electron.",
        ["Graphite electrodes are used in electrolysis."], "k3-26-use")],
  [num("k3-26-bonds", 1, "In {X.n}, to how many other carbon atoms is each carbon atom covalently bonded?", "X.k",
       ["{X.s}", "So each carbon is bonded to {answer} others."],
       vars={"X": {"pick": [{"n": "diamond", "k": 4, "s": "In diamond all four outer electrons form bonds in a 3-D network."},
                            {"n": "graphite", "k": 3, "s": "In graphite three electrons form bonds in a flat layer; the fourth is free."}]}},
       misc=[("other", "7 - X.k", "{X.n == 'diamond' ? 'That is graphite. In diamond all four outer electrons bond.' : 'That is diamond. In graphite one electron per carbon is free.'}")],
       review="authored", sources=SRC),
   bank("k3-26-prop", 1, "{X.q}", [
     {"q": "Why is diamond very hard?", "r": "Each carbon is held by four strong covalent bonds in a rigid 3-D network", "w": ["It has free electrons", "Its layers slide easily", "It is ionic"],
      "e": ["Diamond has no free electrons.", "That describes graphite.", "Diamond is covalent."], "y": "Breaking it means breaking many strong bonds."},
     {"q": "Why is graphite soft and slippery?", "r": "Its layers are held only by weak forces and slide over each other", "w": ["It has no covalent bonds", "It is a metal", "Its atoms are not bonded"],
      "e": ["The bonds within each layer are strong covalent bonds.", "Graphite is a non-metal.", "Atoms within a layer are strongly bonded."], "y": "Weak forces between layers."},
     {"q": "What are diamond and graphite?", "r": "two forms (allotropes) of pure carbon", "w": ["two compounds of carbon and oxygen", "a metal and a non-metal", "two different elements"],
      "e": ["Both are pure carbon.", "Both are forms of the non-metal carbon.", "Both are the element carbon."], "y": "Same element, different structures."}], SRC),
   bank("k3-26-use", 2, "Which property explains this use? {X.q}", [
     {"q": "Diamond is used on the tips of drills for drilling wells.", "r": "it is extremely hard", "w": ["it conducts electricity", "it is slippery", "it is shiny"],
      "e": ["Diamond does not conduct.", "Diamond is not slippery.", "Shine is not why it is used for drilling."], "y": "Only something very hard can cut through rock."},
     {"q": "Graphite is used as a lubricant in machines.", "r": "its layers slide over each other easily", "w": ["it is very hard", "it is transparent", "it dissolves in oil"],
      "e": ["Graphite is soft.", "Graphite is black.", "It is insoluble; it works because it is slippery."], "y": "Sliding layers reduce friction."},
     {"q": "Graphite is used for electrodes in electrolysis.", "r": "it conducts electricity and has a high melting point", "w": ["it is very hard", "it is a good insulator", "it dissolves in water"],
      "e": ["Hardness is not needed for an electrode.", "An electrode must conduct.", "Graphite is insoluble."], "y": "Free electrons carry current; the high m.p. resists heat."}], SRC),
   bank("k3-26-explain", 3, "{X.q}", [
     {"q": "Both diamond and graphite have very high melting points. Why?", "r": "Both are giant structures with many strong covalent bonds to break", "w": ["Both have free electrons", "Both are ionic", "Both are made of small molecules"],
      "e": ["Only graphite has free electrons.", "Both are covalent.", "Small molecules would melt easily."], "y": "Melting means breaking strong covalent bonds throughout."},
     {"q": "Pencil 'lead' leaves a mark on paper. Why?", "r": "Layers of graphite slide off onto the paper", "w": ["Lead metal rubs off", "Diamond scratches the paper", "The carbon melts"],
      "e": ["Pencils contain graphite, not lead metal.", "Pencils contain graphite.", "Graphite does not melt at room temperature."], "y": "Weak forces between layers let them flake off."},
     {"q": "Why does diamond not conduct electricity although it is carbon like graphite?", "r": "All its outer electrons are used in bonds, so none are free", "w": ["It is a metal", "Its ions are fixed", "It contains water"],
      "e": ["Diamond is a non-metal.", "Diamond has no ions.", "Diamond is dry."], "y": "Conduction needs free electrons; diamond has none."}], SRC)],
  learn=learn(
    [("Same element, two structures",
      "Diamond and graphite are both made only of carbon atoms. Different forms of the same element are called allotropes.\n"
      "Their properties are very different because their atoms are joined in different ways. Both are giant covalent structures: no small molecules, just huge networks of bonded atoms."),
     ("Diamond",
      "Each carbon atom forms {4} covalent bonds to four other carbon atoms, arranged as a tetrahedron. This makes a rigid three-dimensional network.\n"
      "• Extremely hard: used on drill tips and cutting tools.\n• Very high melting point.\n• Does not conduct: all outer electrons are in bonds.\n• Sparkles when cut: used in jewellery."),
     ("Graphite",
      "Each carbon atom bonds to only {3} others, forming flat layers of hexagons. The fourth outer electron of each atom is delocalised, free to move along the layer.\n"
      "• Layers held by weak forces slide easily: soft and slippery, used in pencils and as a lubricant.\n"
      "• Conducts electricity: used for electrodes and in batteries.\n• High melting point, like diamond.")],
    key_words=[("allotropes", "different forms of the same element"), ("giant covalent structure", "a huge network of atoms joined by covalent bonds"),
               ("delocalised electron", "an electron free to move, not tied to one bond")],
    examples=["Diamond: drill tips, jewellery", "Graphite: pencils, lubricants, electrodes"],
    mistake=("Graphite is soft because its covalent bonds are weak", "Graphite is soft because the forces between its layers are weak",
             "The bonds within each layer are strong; it is the layers that slide.")))
