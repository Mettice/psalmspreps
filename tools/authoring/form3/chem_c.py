"""Form 3 Chemistry, Term 1, rows 15-26 (structure and bonding). Run: python tools/authoring/form3/chem_c.py
Chemical equations and formulae with digits are written as fixed text: {'2Na + Cl₂ → 2NaCl'}."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "chemistry", "chemistry"
SRC = ["bonding"]
IONIC_PAIRS = {"P": {"pick": ["Na", "K", "Mg", "Ca", "Al", "Li"]}, "N": {"pick": ["Cl", "F", "O", "S"]}}


VAL = {"Na": 1, "K": 1, "Li": 1, "Mg": 2, "Ca": 2, "Al": 3, "Cl": 1, "F": 1, "O": 2, "S": 2}


def _part(x, n):
    return x if n == 1 else f"{x}{n}"


def _pair(p, n):
    from math import gcd
    a, b = VAL[p], VAL[n]
    g = gcd(a, b)
    i, j = b // g, a // g
    return {"p": p, "n": n, "w": _part(p, j) + _part(n, i), "d": _part(p, 2 * i) + _part(n, 2 * j)}


PAIRS = [_pair(p, n) for p, n in [("Na", "O"), ("K", "O"), ("Li", "O"), ("Na", "S"), ("K", "S"), ("Mg", "Cl"), ("Ca", "Cl"), ("Mg", "F"), ("Ca", "F"),
                                  ("Al", "Cl"), ("Al", "F"), ("Al", "O"), ("Al", "S")]]


def E(s):
    """A chemical equation or formula as fixed text inside a card, Learn screen or example."""
    return "{'" + s + "'}"


# ---------------------------------------------------------------- 15. The octet rule
L.lesson(D, S, 15, ("k3-15", "The octet rule: noble gas configuration"), [11],
  "Noble gases (He, Ne, Ar) are very unreactive because their outer shell is full: 2 for helium, 8 for the others (an octet).\n"
  "Octet rule: atoms react by losing, gaining or sharing electrons so that they end up with a full outer shell like the nearest noble gas.\n"
  "• Metals with 1, 2 or 3 outer electrons lose them: Na (2,8,1) → Na⁺ (2,8), like neon.\n"
  "• Non-metals with 5, 6 or 7 outer electrons gain 3, 2 or 1: O (2,6) → O²⁻ (2,8), like neon.\n"
  "• Non-metals can also share electrons to complete their octets (covalent bonds).",
  worked({"z": 16},
         "Sulphur has atomic number {z}. How does it reach a noble gas configuration, and what ion forms?",
         ["Configuration: {shells(z)}: {outerElectrons(z)} outer electrons.", "Gaining {8 - outerElectrons(z)} is easier than losing {outerElectrons(z)}.",
          "It gains {8 - outerElectrons(z)} electrons: {shells(z + 8 - outerElectrons(z))}, like argon. The ion is S²⁻."],
         "It gains {8 - outerElectrons(z)} electrons to form S²⁻", checks=["8 - outerElectrons(z) == 2"]),
  [card("c3k15-1", "A full outer shell (an octet, or {2} for helium) is stable.",
        ["Neon {2}, {8} and argon {2}, {8}, {8} do not react."], "k3-15-why"),
   card("c3k15-2", "Metals lose their {1}, {2} or {3} outer electrons.",
        ["Mg ({2}, {8}, {2}) → Mg²⁺ ({2}, {8})"], "k3-15-lose"),
   card("c3k15-3", "Non-metals gain electrons to make {8}.",
        ["Cl ({2}, {8}, {7}) → Cl⁻ ({2}, {8}, {8})"], "k3-15-gain")],
  [bank("k3-15-why", 1, "{X.q}", [
     {"q": "Why are the noble gases unreactive?", "r": "Their outer shells are full", "w": ["They have no electrons", "They are too heavy to react", "They have only one shell"],
      "e": ["They have electrons in full shells.", "Mass does not decide reactivity.", "Argon has three shells."], "y": "A full outer shell is a stable arrangement."},
     {"q": "What does the octet rule say?", "r": "Atoms tend to gain, lose or share electrons to get eight in the outer shell", "w": ["Atoms always have eight electrons", "Every atom has eight shells", "Atoms always gain eight electrons"],
      "e": ["Most atoms do not have eight outer electrons to start with.", "Shells, not eight of them.", "They gain or lose only what they need."], "y": "Eight outer electrons, like a noble gas, is stable."},
     {"q": "Which ion has the same electron arrangement as neon (2, 8)?", "r": "Na⁺", "w": ["Na", "Cl⁻", "K⁺"],
      "e": ["The sodium atom is 2, 8, 1.", "Cl⁻ is 2, 8, 8 like argon.", "K⁺ is 2, 8, 8 like argon."], "y": "Na⁺ has 10 electrons: 2, 8."}], SRC),
   num("k3-15-lose", 1, "How many electrons does {nameOf(X)} (atomic number {z}) lose to reach a noble gas configuration?", "outerElectrons(z)",
       ["Configuration {shells(z)}: {outerElectrons(z)} outer electron(s).", "It loses all {answer} to leave a full shell."],
       vars={"X": {"pick": ["Li", "Na", "K", "Be", "Mg", "Ca", "Al"]}, "z": {"expr": "atomicNumber(X)"}},
       misc=[("gain", "8 - outerElectrons(z)", "Metals lose their few outer electrons rather than gaining many.")],
       sources=SRC),
   num("k3-15-gain", 2, "How many electrons does {nameOf(X)} (atomic number {z}) gain to reach a noble gas configuration?", "8 - outerElectrons(z)",
       ["Configuration {shells(z)}: {outerElectrons(z)} outer electrons.", "It needs {8} − {outerElectrons(z)} = {answer} more to complete the octet."],
       vars={"X": {"pick": ["N", "O", "F", "P", "S", "Cl"]}, "z": {"expr": "atomicNumber(X)"}},
       misc=[("lose", "outerElectrons(z)", "Non-metals with {outerElectrons(z)} outer electrons gain electrons rather than losing so many.")],
       sources=SRC, where=["8 - outerElectrons(z) != outerElectrons(z)"]),
   num("k3-15-charge", 3, "What is the charge of the ion formed by {nameOf(X)} (atomic number {z})? Give a signed number, e.g. −1.", "outerElectrons(z) <= 3 ? outerElectrons(z) : outerElectrons(z) - 8",
       ["Configuration {shells(z)}.", "{outerElectrons(z) <= 3 ? 'It loses ' + outerElectrons(z) + ' electron(s), so the ion is positive.' : 'It gains ' + (8 - outerElectrons(z)) + ' electron(s), so the ion is negative.'} Charge {answer}."],
       vars={"X": {"pick": ["Li", "Na", "K", "Mg", "Ca", "Al", "N", "O", "F", "S", "Cl"]}, "z": {"expr": "atomicNumber(X)"}},
       misc=[("sign", "outerElectrons(z) <= 3 ? 0 - outerElectrons(z) : 8 - outerElectrons(z)", "Losing electrons gives a positive ion; gaining gives a negative ion.")],
       sources=SRC, signed=True)],
  learn=learn(
    [("Why noble gases are special",
      "Helium, neon and argon hardly react at all. Their outer shells are full: {2} electrons for helium, {8} for neon and argon.\n"
      "A full outer shell is a very stable arrangement. Eight outer electrons is called an octet."),
     ("The octet rule",
      "Other atoms react in ways that give them a full outer shell, like the nearest noble gas.\n"
      "• Metals have {1}, {2} or {3} outer electrons. It is easiest to lose them: sodium ({2}, {8}, {1}) becomes Na⁺ ({2}, {8}).\n"
      "• Non-metals have {5}, {6} or {7}. It is easiest to gain the few that are missing: chlorine ({2}, {8}, {7}) becomes Cl⁻ ({2}, {8}, {8}).\n"
      "• Two non-metals can also share electrons so that both complete their octets."),
     ("Predicting the charge",
      "Losing electrons gives a positive ion; gaining gives a negative ion:\n"
      "• group I → +{1}; group II → +{2}; group III → +{3};\n• group V → −{3}; group VI → −{2}; group VII → −{1}.\n"
      "So aluminium forms Al³⁺ and oxygen forms O²⁻.")],
    key_words=[("octet", "eight electrons in the outer shell"), ("noble gas configuration", "a full outer shell like He, Ne or Ar"),
               ("stable", "unlikely to react")],
    examples=["K ({2},{8},{8},{1}) → K⁺ ({2},{8},{8})", "N ({2},{5}) gains {3} → N³⁻ ({2},{8})", "Ca loses {2} → Ca²⁺"],
    mistake=("Chlorine loses {7} electrons to empty its outer shell", "Chlorine gains {1} electron to complete its octet",
             "Gaining one electron is far easier than losing seven.")))

# ---------------------------------------------------------------- 16. Bond formation and the octet rule
L.lesson(D, S, 16, ("k3-16", "Chemical bonds and the octet rule: ionic, covalent and metallic"), [15],
  "A chemical bond holds atoms together. Atoms form bonds to reach a stable, full outer shell.\n"
  "• Ionic bond: a metal transfers electrons to a non-metal; the oppositely charged ions attract (NaCl).\n"
  "• Covalent bond: two non-metal atoms share a pair of electrons (H₂, H₂O, CH₄).\n"
  "• Metallic bond: metal atoms lose their outer electrons into a 'sea' of electrons shared by all the positive ions (copper, iron).\n"
  "Quick guide: metal + non-metal → ionic; non-metal + non-metal → covalent; metal alone → metallic.",
  worked({},
         "State the type of bonding in sodium chloride, water and copper.",
         ["Sodium chloride: metal + non-metal → ionic.", "Water: hydrogen and oxygen, both non-metals → covalent.", "Copper: a metal element → metallic."],
         "ionic, covalent, metallic"),
  [card("c3k16-1", "Metal + non-metal: electrons are transferred (ionic bond).",
        ["Sodium + chlorine → sodium chloride"], "k3-16-type"),
   card("c3k16-2", "Non-metal + non-metal: electrons are shared (covalent bond).",
        ["Hydrogen + oxygen → water"], "k3-16-pair"),
   card("c3k16-3", "In a metal, positive ions sit in a sea of shared electrons (metallic bond).",
        ["Iron, copper, aluminium"], "k3-16-metal")],
  [bank("k3-16-type", 1, "What type of bonding is in {X.q}?", [
     {"q": "sodium chloride, NaCl", "r": "ionic", "w": ["covalent", "metallic", "no bonding"],
      "e": ["Sodium is a metal and chlorine a non-metal: electrons are transferred.", "Only one of the elements is a metal.", "The atoms are bonded."], "y": "Metal + non-metal: ionic."},
     {"q": "water, H₂O", "r": "covalent", "w": ["ionic", "metallic", "no bonding"],
      "e": ["Hydrogen and oxygen are both non-metals: they share electrons.", "There is no metal.", "The atoms are bonded."], "y": "Non-metal + non-metal: covalent."},
     {"q": "a copper wire", "r": "metallic", "w": ["ionic", "covalent", "no bonding"],
      "e": ["There is no non-metal to accept electrons.", "Metals do not share pairs of electrons like non-metals.", "The atoms are bonded."], "y": "A metal element: metallic bonding."},
     {"q": "methane, CH₄", "r": "covalent", "w": ["ionic", "metallic", "no bonding"],
      "e": ["Carbon and hydrogen are both non-metals.", "There is no metal.", "The atoms are bonded."], "y": "Non-metals share electrons."},
     {"q": "magnesium oxide, MgO", "r": "ionic", "w": ["covalent", "metallic", "no bonding"],
      "e": ["Magnesium is a metal: it transfers electrons to oxygen.", "Oxygen is a non-metal.", "The atoms are bonded."], "y": "Metal + non-metal: ionic."}], SRC),
   bank("k3-16-pair", 1, "{X.q}", [
     {"q": "Which pair of elements will form an ionic compound?", "r": "potassium and fluorine", "w": ["carbon and oxygen", "nitrogen and hydrogen", "chlorine and chlorine"],
      "e": ["Both are non-metals: covalent.", "Both are non-metals: covalent.", "Two identical non-metals share electrons."], "y": "A metal and a non-metal: ionic."},
     {"q": "Which pair of elements will form a covalent compound?", "r": "hydrogen and chlorine", "w": ["sodium and chlorine", "calcium and oxygen", "magnesium and sulphur"],
      "e": ["Sodium is a metal: ionic.", "Calcium is a metal: ionic.", "Magnesium is a metal: ionic."], "y": "Two non-metals share electrons."},
     {"q": "In an ionic bond, what happens to the electrons?", "r": "They are transferred from the metal to the non-metal", "w": ["They are shared equally", "They are destroyed", "They move from the non-metal to the metal"],
      "e": ["Sharing is covalent bonding.", "Electrons are never destroyed.", "The metal loses electrons; the non-metal gains them."], "y": "The metal becomes a positive ion and the non-metal a negative ion."}], SRC),
   bank("k3-16-metal", 2, "{X.q}", [
     {"q": "What holds the atoms together in a piece of iron?", "r": "Attraction between positive ions and a sea of moving electrons", "w": ["Shared pairs of electrons between two atoms", "Attraction between positive and negative ions", "Nothing: the atoms are separate"],
      "e": ["That is a covalent bond.", "There are no negative ions in a pure metal.", "The atoms are held together strongly."], "y": "Metallic bonding: delocalised electrons around positive ions."},
     {"q": "Why do atoms form chemical bonds?", "r": "To reach a stable, full outer shell", "w": ["To lose their protons", "To become heavier", "To change into another element"],
      "e": ["Protons never change in a reaction.", "Mass is not the reason.", "The element does not change."], "y": "Losing, gaining or sharing electrons gives full outer shells."},
     {"q": "Which substance has metallic bonding?", "r": "aluminium foil", "w": ["table salt", "sugar", "carbon dioxide"],
      "e": ["Salt is ionic.", "Sugar is covalent.", "Carbon dioxide is covalent."], "y": "Aluminium is a metal."}], SRC),
   bank("k3-16-octet", 3, "{X.q}", [
     {"q": "In water, how does the oxygen atom complete its octet?", "r": "It shares one pair of electrons with each of two hydrogen atoms", "w": ["It gains two electrons from hydrogen ions", "It loses six electrons", "It shares electrons with another oxygen atom"],
      "e": ["Hydrogen and oxygen are both non-metals: they share.", "Losing six is far too hard.", "Water has one oxygen atom."], "y": "Two shared pairs give oxygen 8 and each hydrogen 2."},
     {"q": "How does magnesium oxide form?", "r": "Magnesium transfers two electrons to oxygen", "w": ["Magnesium and oxygen share two pairs of electrons", "Oxygen transfers two electrons to magnesium", "Magnesium and oxygen share a sea of electrons"],
      "e": ["A metal and a non-metal transfer electrons.", "The metal loses; the non-metal gains.", "That is metallic bonding."], "y": "Mg²⁺ and O²⁻ form, both with a full shell."},
     {"q": "Two chlorine atoms form a Cl₂ molecule. How?", "r": "They share one pair of electrons", "w": ["One gives an electron to the other", "They share a sea of electrons", "They do not bond"],
      "e": ["Identical atoms cannot easily transfer electrons.", "That is metallic bonding.", "Chlorine exists as Cl₂ molecules."], "y": "Each gets eight outer electrons by sharing one pair."}], SRC)],
  learn=learn(
    [("Why atoms bond",
      "Most atoms do not have a full outer shell, so they are not stable on their own. By bonding with other atoms they can reach a full shell, like a noble gas.\n"
      "There are three main ways: transferring electrons, sharing electrons, and pooling electrons."),
     ("Three types of bond",
      "• Ionic: between a metal and a non-metal. The metal gives its outer electrons to the non-metal; the positive and negative ions attract strongly. Example: sodium chloride (table salt).\n"
      "• Covalent: between non-metals. Atoms share pairs of electrons. Examples: water, methane, oxygen gas.\n"
      "• Metallic: in metals. Atoms release their outer electrons into a sea of electrons that moves through a lattice of positive ions. Examples: copper, iron, aluminium."),
     ("Telling them apart",
      "Look at the elements:\n• metal + non-metal → ionic;\n• non-metal + non-metal → covalent;\n• a metal element (or alloy) → metallic.\n"
      "The type of bond explains many properties, such as melting point and electrical conductivity, which you will meet in the next lessons.")],
    key_words=[("chemical bond", "a force holding atoms or ions together"), ("ionic bond", "attraction between oppositely charged ions"),
               ("covalent bond", "a shared pair of electrons"), ("metallic bond", "attraction between metal ions and a sea of electrons")],
    examples=["KCl: ionic", "NH₃: covalent", "Brass (an alloy): metallic"],
    mistake=("Water is ionic because it has two elements", "Water is covalent: hydrogen and oxygen are both non-metals",
             "It is the kind of element (metal or non-metal), not the number of elements, that decides.")))

# ---------------------------------------------------------------- 17. Ionic bonding
L.lesson(D, S, 17, ("k3-17", "Ionic bonding: formation and formulae of ionic compounds"), [16],
  "In ionic bonding, a metal atom transfers electrons to a non-metal atom:\n"
  "• Na (2,8,1) loses 1 → Na⁺ (2,8); Cl (2,8,7) gains 1 → Cl⁻ (2,8,8). The ions attract: NaCl.\n"
  "• Mg (2,8,2) loses 2 → Mg²⁺; O (2,6) gains 2 → O²⁻: MgO.\n"
  "Dot-and-cross diagrams show the outer electrons of each atom (dots for one, crosses for the other) and the charges of the ions.\n"
  "Formula: the total positive charge must equal the total negative charge. Mg²⁺ with Cl⁻ needs two Cl⁻: MgCl₂. Al³⁺ with O²⁻: Al₂O₃.",
  worked({},
         "Show how aluminium and oxygen form an ionic compound, and give its formula.",
         ["Al ({2},{8},{3}) loses {3} electrons → Al³⁺. O ({2},{6}) gains {2} → O²⁻.", "Charges must balance: the lowest common multiple of {3} and {2} is {6}.",
          "Two Al³⁺ give +{6}; three O²⁻ give −{6}."], E("Al₂O₃")),
  [card("c3k17-1", "The metal loses electrons and the non-metal gains them.",
        [E("Na → Na⁺ + e⁻") + ";  " + E("Cl + e⁻ → Cl⁻")], "k3-17-formula"),
   card("c3k17-2", "Balance the charges to get the formula.",
        [E("Ca²⁺") + " with " + E("Cl⁻") + ": " + E("CaCl₂")], "k3-17-ions"),
   card("c3k17-3", "The ions attract because they have opposite charges.",
        [E("Na⁺") + " and " + E("Cl⁻") + " pack together in a giant lattice."], "k3-17-e")],
  [mcq("k3-17-formula", 1, "What is the formula of {compoundName(X.p, X.n)}?", "{formula(compoundFormula(X.p, X.n))}",
       [("{formula(X.p + X.n)}", "one"), ("{formula(X.w)}", "swap"), ("{formula(X.d)}", "double")],
       ["{X.p} forms an ion of charge +{valency(X.p)}; {X.n} forms an ion of charge −{valency(X.n)}.", "The charges must balance: {answer}."],
       vars={"X": {"pick": PAIRS}},
       misc=[("one", "One of each does not balance +{valency(X.p)} and −{valency(X.n)}."),
             ("swap", "The numbers are the wrong way round: the number of {X.n} comes from the charge of {X.p}."),
             ("double", "Use the smallest whole numbers that balance the charges.")],
       sources=SRC),
   num("k3-17-e", 1, "How many electrons does each {nameOf(P)} atom transfer when it forms an ionic compound?", "valency(P)",
       ["{nameOf(P)} has {valency(P)} outer electron(s).", "It transfers all {answer} to the non-metal."],
       vars={"P": {"pick": ["Na", "K", "Li", "Mg", "Ca", "Al"]}},
       misc=[("gain", "8 - valency(P)", "Metals lose their few outer electrons; they do not gain.")],
       sources=SRC),
   bank("k3-17-ions", 2, "{X.q}", [
     {"q": "When magnesium reacts with oxygen, what ions form?", "r": "Mg²⁺ and O²⁻", "w": ["Mg⁺ and O⁻", "Mg²⁻ and O²⁺", "Mg²⁺ and O⁻"],
      "e": ["Magnesium loses two electrons and oxygen gains two.", "The metal becomes positive, the non-metal negative.", "Oxygen gains two electrons, not one."], "y": "Two electrons are transferred."},
     {"q": "In sodium chloride, what is the electron arrangement of the chloride ion?", "r": "2, 8, 8", "w": ["2, 8, 7", "2, 8", "2, 8, 8, 1"],
      "e": ["That is the chlorine atom.", "That is the sodium ion.", "Chloride gains one electron, giving 18 in all."], "y": "Cl⁻ has 18 electrons: 2, 8, 8."},
     {"q": "What holds the ions together in an ionic compound?", "r": "Strong attraction between opposite charges", "w": ["Shared pairs of electrons", "A sea of electrons", "Weak forces between molecules"],
      "e": ["That is covalent bonding.", "That is metallic bonding.", "Ionic bonds are strong."], "y": "Electrostatic attraction between + and − ions."}], SRC),
   num("k3-17-count", 2, "In the formula of {compoundName(P, N)}, how many {nameOf(N)} ions are there for each formula unit? (Give the number of {N} in the formula.)", "valency(P) / hcf(valency(P), valency(N))",
       ["Charges: {P} +{valency(P)}, {N} −{valency(N)}.", "Formula {formula(compoundFormula(P, N))}: there are {answer} {N} in it."],
       vars={"P": {"pick": ["Mg", "Ca", "Al", "Na", "K"]}, "N": {"pick": ["Cl", "F", "O", "S"]}},
       misc=[("swap", "valency(N) / hcf(valency(P), valency(N))", "The number of {N} comes from the metal's charge (+{valency(P)}).")],
       sources=SRC, where=["valency(P) / hcf(valency(P), valency(N)) != valency(N) / hcf(valency(P), valency(N))", "valency(P) / hcf(valency(P), valency(N)) != 1"]),
   order("k3-17-steps", 3, "Put the steps of forming sodium chloride in order.",
         ["The sodium atom (2, 8, 1) loses its outer electron.", "The chlorine atom (2, 8, 7) gains that electron.",
          "Na⁺ (2, 8) and Cl⁻ (2, 8, 8) are formed, each with a full outer shell.", "The oppositely charged ions attract to form an ionic lattice."],
         hint="Start with the metal losing its electron.", sources=SRC, review="authored")],
  learn=learn(
    [("Transferring electrons",
      "When a metal meets a non-metal, the metal atom gives its outer electrons to the non-metal atom.\n"
      "Sodium ({2},{8},{1}) gives its one outer electron to chlorine ({2},{8},{7}). Now sodium is Na⁺ ({2},{8}) and chlorine is Cl⁻ ({2},{8},{8}): both have full shells.\n"
      "The positive and negative ions attract each other strongly. This attraction is the ionic bond."),
     ("Dot-and-cross diagrams",
      "To show the transfer, draw the outer shells only: the metal's electrons as crosses (×) and the non-metal's as dots (•).\n"
      "After the transfer, draw each ion in square brackets with its charge outside, for example [Na]⁺ and [Cl]⁻ with eight electrons around chlorine.\n"
      "Remember: electrons move from the metal to the non-metal, never the other way."),
     ("Writing formulae",
      "An ionic compound has no overall charge, so the charges must balance.\n"
      "• Na⁺ and Cl⁻: one of each, NaCl.\n• Mg²⁺ and Cl⁻: two chlorides, MgCl₂.\n• Al³⁺ and O²⁻: lowest common multiple {6}, so two Al and three O: Al₂O₃.\n"
      "Use the smallest whole numbers that balance.")],
    key_words=[("ion", "a charged particle"), ("dot-and-cross diagram", "a drawing of outer electrons showing transfer or sharing"),
               ("ionic lattice", "a giant regular arrangement of positive and negative ions")],
    examples=[E("K⁺ + Br⁻ → KBr"), E("Ca²⁺ + O²⁻ → CaO"), E("2Na⁺ + O²⁻ → Na₂O")],
    mistake=("Chlorine gives an electron to sodium", "Sodium (the metal) gives an electron to chlorine",
             "Metals lose electrons; non-metals gain them.")))

# ---------------------------------------------------------------- 18. Properties of ionic compounds
L.lesson(D, S, 18, ("k3-18", "Properties of ionic compounds"), [17],
  "Ionic compounds form giant lattices of ions held by strong electrostatic forces. So they:\n"
  "• have high melting and boiling points (much energy is needed to separate the ions), e.g. NaCl melts at 801 °C;\n"
  "• are hard but brittle crystalline solids at room temperature;\n"
  "• are often soluble in water but insoluble in organic solvents (petrol, kerosene);\n"
  "• do not conduct electricity when solid (ions cannot move) but do conduct when molten or dissolved in water (ions free to move).",
  worked({},
         "Explain why solid salt does not conduct electricity but salt water does.",
         ["Electricity needs charged particles that can move.", "In solid salt the ions are held in fixed positions in the lattice.",
          "When salt dissolves, the ions separate and move freely, so the solution conducts."],
         "The ions can move only when dissolved (or molten)"),
  [card("c3k18-1", "Strong forces between ions: high melting points.",
        ["Salt melts at about {801} °C."], "k3-18-mp"),
   card("c3k18-2", "Ionic compounds conduct only when molten or dissolved.",
        ["The ions must be free to move."], "k3-18-cond"),
   card("c3k18-3", "Many ionic compounds dissolve in water, not in kerosene.",
        ["Salt dissolves in water; it does not dissolve in kerosene."], "k3-18-sol")],
  [bank("k3-18-mp", 1, "{X.q}", [
     {"q": "Why does sodium chloride have a high melting point?", "r": "Strong forces hold the ions together in a giant lattice", "w": ["Its molecules are very heavy", "It contains a metal that is hard to melt", "Weak forces between molecules"],
      "e": ["It has no separate molecules; it is a lattice of ions.", "It is the ionic bonding, not the metal, that matters.", "Weak forces would give a low melting point."], "y": "Much energy is needed to break the many strong ionic bonds."},
     {"q": "At room temperature, ionic compounds are usually…", "r": "crystalline solids", "w": ["gases", "liquids", "soft waxy solids"],
      "e": ["Strong bonds keep them solid.", "Their melting points are high.", "They are hard and brittle."], "y": "High melting points: solid at room temperature."},
     {"q": "Which has the highest melting point?", "r": "magnesium oxide (ionic)", "w": ["water (covalent)", "methane (covalent)", "oxygen (covalent)"],
      "e": ["Water melts at 0 °C.", "Methane is a gas.", "Oxygen is a gas."], "y": "Ionic lattices have high melting points."}], SRC),
   bank("k3-18-cond", 1, "{X.q}", [
     {"q": "When does an ionic compound conduct electricity?", "r": "when molten or dissolved in water", "w": ["when solid", "never", "only when frozen"],
      "e": ["In the solid the ions cannot move.", "It does conduct when the ions are free.", "Frozen means solid: no movement."], "y": "Moving ions carry the current."},
     {"q": "What carries the current in molten sodium chloride?", "r": "moving Na⁺ and Cl⁻ ions", "w": ["free electrons", "water molecules", "protons"],
      "e": ["Free electrons carry current in metals.", "There is no water in the melt.", "Protons stay in the nuclei."], "y": "In ionic liquids, ions carry the current."},
     {"q": "Why does solid potassium chloride not conduct electricity?", "r": "Its ions are fixed in place", "w": ["It has no ions", "It contains no metal", "Its electrons are free"],
      "e": ["It is made of ions.", "Potassium is a metal.", "Free electrons would make it conduct."], "y": "Charged particles must move to carry current."}], SRC),
   bank("k3-18-sol", 2, "{X.q}", [
     {"q": "Common salt is mixed with kerosene. What happens?", "r": "It does not dissolve", "w": ["It dissolves quickly", "It melts", "It burns"],
      "e": ["Ionic compounds dissolve in water, not organic solvents.", "Salt melts at 801 °C.", "Salt does not burn."], "y": "Ionic compounds are generally insoluble in organic solvents."},
     {"q": "Which property is typical of an ionic compound?", "r": "brittle: it shatters when hit", "w": ["bends easily", "low boiling point", "conducts when solid"],
      "e": ["Metals bend; ionic crystals break.", "Ionic compounds have high boiling points.", "Solid ionic compounds do not conduct."], "y": "Shifting the layers brings like charges together, so the crystal splits."},
     {"q": "Why do many ionic compounds dissolve in water?", "r": "Water molecules attract and separate the ions", "w": ["Water melts them", "They react to form gases", "Water contains free electrons"],
      "e": ["Dissolving is not melting.", "No gas is formed.", "Water has no free electrons."], "y": "The ions spread out among the water molecules."}], SRC),
   bank("k3-18-ident", 3, "{X.q}", [
     {"q": "A white solid melts at 770 °C, dissolves in water, and its solution conducts electricity. What type of substance is it?", "r": "ionic", "w": ["simple covalent", "metallic", "a noble gas"],
      "e": ["Simple covalent substances have low melting points and do not conduct.", "Metals conduct as solids and do not dissolve in water.", "Noble gases are gases."], "y": "High melting point, soluble, conducts in solution: ionic."},
     {"q": "Which result shows a substance is NOT ionic?", "r": "It melts at 45 °C", "w": ["It dissolves in water", "Its melt conducts electricity", "It is a hard crystal"],
      "e": ["Many ionic compounds dissolve in water.", "Molten ionic compounds conduct.", "Ionic compounds are hard crystals."], "y": "A low melting point means weak forces: not ionic."},
     {"q": "A compound conducts when molten but not when solid. Its bonding is…", "r": "ionic", "w": ["metallic", "covalent", "none"],
      "e": ["Metals conduct when solid too.", "Covalent compounds do not conduct when molten.", "It must be bonded."], "y": "Ions become free to move when it melts."}], SRC)],
  learn=learn(
    [("A giant lattice of ions",
      "An ionic compound is not made of separate molecules. Millions of positive and negative ions are packed in a regular three-dimensional pattern called a giant ionic lattice.\n"
      "Every ion is attracted strongly by the oppositely charged ions around it. These strong forces explain the properties."),
     ("High melting points, brittle crystals",
      "Melting means freeing the ions, which needs a lot of energy: salt melts at about {801} °C, magnesium oxide at about {2800} °C.\n"
      "Ionic compounds are hard crystals, but brittle: a sharp blow shifts the layers so that ions of the same charge meet, they repel, and the crystal shatters."),
     ("Dissolving and conducting",
      "Many ionic compounds dissolve in water, because water molecules attract the ions and pull them apart; they do not dissolve in kerosene or petrol.\n"
      "To conduct electricity, charged particles must move. In the solid the ions are fixed, so it does not conduct. Molten or dissolved, the ions move freely, so it conducts.")],
    key_words=[("giant ionic lattice", "a huge regular arrangement of ions"), ("brittle", "breaks into pieces when hit"), ("electrolyte", "a molten or dissolved ionic compound that conducts")],
    examples=["NaCl: m.p. {801} °C, soluble, conducts in solution", "MgO: very high m.p., used to line furnaces"],
    mistake=("Solid salt conducts because it contains ions", "Solid salt does not conduct: its ions cannot move",
             "Ions must be free to move to carry a current.")))
