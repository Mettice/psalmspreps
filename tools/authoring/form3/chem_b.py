"""Form 3 Chemistry, Term 1, rows 9-13 (electrons, configuration, Periodic Table, group families).
Run: python tools/authoring/form3/chem_b.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "chemistry", "chemistry"
SYMS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
EL = {"X": {"pick": SYMS}, "z": {"expr": "atomicNumber(X)"}}
EL3 = {"X": {"pick": SYMS[2:]}, "z": {"expr": "atomicNumber(X)"}}  # from lithium: at least two shells
SRC = ["electrons"]

# ---------------------------------------------------------------- 9. Nucleus and electrons
L.lesson(D, S, 9, ("k3-9", "Structure of the atom: the nucleus and electron shells"), [1],
  "Electrons are arranged in shells (energy levels) around the nucleus.\n"
  "• The first shell, nearest the nucleus, holds at most 2 electrons; the second at most 8; for the first 20 elements the third holds 8 before the fourth starts.\n"
  "• Shells fill from the inside out: inner shells first.\n"
  "• Electrons in shells further out have more energy and are held less strongly.\n"
  "A Bohr (shell) diagram shows the nucleus and each shell with its electrons as dots or crosses.",
  worked({"z": 12},
         "Draw the shells of a magnesium atom (atomic number {z}) and state how many electrons are in each.",
         ["{z} electrons to place.", "First shell: {2}; second shell: {8}; that makes {10}.", "The remaining {z - 10} go into the third shell."],
         "{shells(z)}", checks=["shells(z) == '2, 8, 2'"], figure="bohr(z)"),
  [card("c3k9-1", "Shell capacities for the first {20} elements: {2}, then {8}, then {8}.",
        ["Sodium ({11}): {2}, {8}, {1}"], "k3-9-cap"),
   card("c3k9-2", "Fill the inner shells first.",
        ["Oxygen ({8}): {2}, {6}"], "k3-9-count"),
   card("c3k9-3", "Outer electrons are further from the nucleus and held less tightly.",
        ["Potassium's outer electron is easy to remove."], "k3-9-fig")],
  [num("k3-9-cap", 1, "What is the greatest number of electrons the {X.n} shell can hold (for the first {20} elements)?", "X.c",
       ["Shell capacities: first {2}, second {8}, third {8} (before the fourth starts).", "So the {X.n} shell holds {answer}."],
       vars={"X": {"pick": [{"n": "first", "c": 2}, {"n": "second", "c": 8}, {"n": "third", "c": 8}]}},
       misc=[("eighteen", "18", "For the first {20} elements, the third shell takes {8} before the fourth starts.")],
       review="authored", sources=SRC),
   num("k3-9-count", 1, "How many shells contain electrons in an atom of {nameOf(X)} (atomic number {z})?", "periodOf(z)",
       ["Arrangement: {shells(z)}.", "That is {answer} shell(s)."],
       vars=EL, misc=[("outer", "outerElectrons(z)", "That is the number of electrons in the outer shell. Count the shells.")],
       sources=SRC, where=["outerElectrons(z) != periodOf(z)"]),
   num("k3-9-fig", 2, "The diagram shows the shells of an atom. What is its atomic number?", "z",
       ["Count all the electrons: {shells(z)}.", "Total = {answer}, so the atomic number is {answer}."],
       vars=EL3, misc=[("outer", "outerElectrons(z)", "Count the electrons in every shell, not only the outer one.")],
       figure="bohr(z)", sources=SRC, where=["outerElectrons(z) != z"]),
   bank("k3-9-energy", 2, "{X.q}", [
     {"q": "Which electrons are held most strongly by the nucleus?", "r": "those in the first (innermost) shell", "w": ["those in the outer shell", "all electrons equally", "those furthest away"],
      "e": ["Outer electrons are further away and held less strongly.", "Distance makes a difference.", "Further electrons are held less strongly."], "y": "The closer to the nucleus, the stronger the attraction."},
     {"q": "Why does the third shell of argon hold 8 electrons and potassium's 19th electron go into a fourth shell?", "r": "For the first 20 elements the third shell is full with 8 before the fourth starts", "w": ["The third shell can never hold more than 2", "Potassium has no third shell", "The fourth shell fills first"],
      "e": ["The third shell holds 8 here.", "Potassium's third shell has 8 electrons.", "Inner shells fill first."], "y": "Arrangement 2, 8, 8, 1 for potassium."},
     {"q": "In which order do shells fill?", "r": "from the nucleus outwards", "w": ["from the outside inwards", "all at the same time", "at random"],
      "e": ["Inner shells fill first.", "One shell fills before the next.", "There is a fixed order."], "y": "Electrons occupy the lowest energy levels first."}], SRC),
   num("k3-9-left", 3, "An atom has {z} electrons. How many electrons are in its outer shell?", "outerElectrons(z)",
       ["Fill the shells: {shells(z)}.", "The outer shell has {answer}."],
       vars={"z": {"int": [3, 20]}},
       misc=[("mod", "z - 2", "Fill the second shell (up to {8}) before the third."), ("all", "z", "Only the outermost shell counts.")],
       sources=SRC, where=["z - 2 != outerElectrons(z)"])],
  learn=learn(
    [("Electrons live in shells",
      "Electrons do not move anywhere they like around the nucleus. They are found in shells (energy levels) at different distances from it.\n"
      "The first shell is closest to the nucleus. Electrons there have the least energy and are held most strongly.\n"
      "A shell diagram (Bohr diagram) shows the nucleus as a small circle and each shell as a ring with its electrons.", "bohr(11)"),
     ("How many in each shell?",
      "For the first {20} elements:\n• first shell: at most {2};\n• second shell: at most {8};\n• third shell: {8} before the fourth shell starts.\n"
      "Fill from the inside out. Sodium has {11} electrons: {2} in the first shell, {8} in the second, {1} in the third: written {2}, {8}, {1}."),
     ("Outer electrons matter",
      "The electrons in the outer shell are furthest from the nucleus and held least strongly. They take part in chemical reactions.\n"
      "That is why the next lessons count outer electrons so carefully: they explain the Periodic Table and how atoms bond.")],
    key_words=[("shell (energy level)", "a region around the nucleus where electrons are found"), ("Bohr diagram", "a drawing of the nucleus and electron shells"),
               ("outer shell", "the last shell that contains electrons")],
    examples=["Carbon ({6}): {2}, {4}", "Chlorine ({17}): {2}, {8}, {7}", "Calcium ({20}): {2}, {8}, {8}, {2}"],
    mistake=("Sodium ({11}): {2}, {9}", "Sodium: {2}, {8}, {1}",
             "The second shell is full at {8}; the next electron starts the third shell.")))

# ---------------------------------------------------------------- 10. Electronic configuration
L.lesson(D, S, 10, ("k3-10", "Electronic configuration of the first 20 elements"), [9],
  "The electronic configuration lists the electrons in each shell, inner to outer: 2, 8, 1 for sodium.\n"
  "Rule for the first 20: fill 2, then 8, then 8, then the rest.\n"
  "• H 1 · He 2 · Li 2,1 · Be 2,2 · B 2,3 · C 2,4 · N 2,5 · O 2,6 · F 2,7 · Ne 2,8\n"
  "• Na 2,8,1 · Mg 2,8,2 · Al 2,8,3 · Si 2,8,4 · P 2,8,5 · S 2,8,6 · Cl 2,8,7 · Ar 2,8,8 · K 2,8,8,1 · Ca 2,8,8,2\n"
  "The total of the numbers equals the atomic number.",
  worked({"z": 17},
         "Write the electronic configuration of chlorine (atomic number {z}).",
         ["First shell: {2} (leaves {z - 2}).", "Second shell: {8} (leaves {z - 10}).", "Third shell: the remaining {z - 10}."],
         "{shells(z)}", checks=["shells(z) == '2, 8, 7'"], figure="bohr(z)"),
  [card("c3k10-1", "Write the electrons shell by shell: {2}, then {8}, then {8}.",
        ["Aluminium ({13}): {2}, {8}, {3}"], "k3-10-write"),
   card("c3k10-2", "The numbers in a configuration add up to the atomic number.",
        ["{2} + {8} + {6} = {16}: sulphur"], "k3-10-which"),
   card("c3k10-3", "Potassium and calcium start a fourth shell.",
        ["K: {2}, {8}, {8}, {1}"], "k3-10-k")],
  [mcq("k3-10-write", 1, "What is the electronic configuration of {nameOf(X)} (atomic number {z})?", "{shells(z)}",
       [("{shells(z - 1)}", "minus"), ("{shells(z + 1)}", "plus"), ("{z <= 10 ? (z > 2 ? '2, 8, ' + (z - 2) : '2, ' + z) : '2, ' + (z - 2)}", "fill")],
       ["Fill {2}, then {8}, then {8}.", "{z} electrons: {answer}."],
       vars=EL3, misc=[("minus", "Count again: those numbers add up to {z - 1}, not {z}."), ("plus", "Count again: those numbers add up to {z + 1}, not {z}."),
                       ("fill", "The second shell holds at most {8}: {z > 10 ? 'go on to the next shell' : 'there are not enough electrons to fill it'}.")],
       sources=SRC, where=["X != 'Ca'", "(z <= 10 ? (z > 2 ? '2, 8, ' + (z - 2) : '2, ' + z) : '2, ' + (z - 2)) != shells(z)"]),
   num("k3-10-which", 1, "An atom has the configuration {shells(z)}. What is its atomic number?", "z",
       ["Add the electrons: {shells(z)}.", "Total = {answer}."],
       vars=EL3, misc=[("outer", "outerElectrons(z)", "Add all the shells, not just the last."), ("shells", "periodOf(z)", "That is the number of shells. Add the electrons.")],
       sources=SRC, where=["outerElectrons(z) != z", "periodOf(z) != outerElectrons(z)"]),
   bank("k3-10-k", 2, "{X.q}", [
     {"q": "What is the electronic configuration of potassium (atomic number 19)?", "r": "2, 8, 8, 1", "w": ["2, 8, 9", "2, 9, 8", "2, 8, 1, 8"],
      "e": ["The third shell takes 8, then the fourth starts.", "The second shell holds at most 8.", "Shells fill from the inside out."], "y": "2 + 8 + 8 = 18, then 1 in the fourth shell."},
     {"q": "What is the electronic configuration of calcium (atomic number 20)?", "r": "2, 8, 8, 2", "w": ["2, 8, 10", "2, 10, 8", "2, 8, 2, 8"],
      "e": ["The third shell takes 8, then the fourth starts.", "The second shell holds at most 8.", "Shells fill from the inside out."], "y": "2, 8, 8, then 2 in the fourth shell."},
     {"q": "Which element has the configuration 2, 8, 8?", "r": "argon (18)", "w": ["calcium (20)", "neon (10)", "chlorine (17)"],
      "e": ["Calcium is 2, 8, 8, 2.", "Neon is 2, 8.", "Chlorine is 2, 8, 7."], "y": "2 + 8 + 8 = 18: argon."}], SRC),
   num("k3-10-ion", 2, "Write the configuration of the ion {X.s}. How many electrons are in its outer shell?", "8",
       ["{X.s} has {atomicNumber(X.e) - X.q} electrons.", "Configuration: {shells(atomicNumber(X.e) - X.q)}: outer shell {answer}."],
       vars={"X": {"pick": [{"s": "Na⁺", "e": "Na", "q": 1}, {"s": "Mg²⁺", "e": "Mg", "q": 2}, {"s": "Cl⁻", "e": "Cl", "q": -1}, {"s": "O²⁻", "e": "O", "q": -2},
                            {"s": "Al³⁺", "e": "Al", "q": 3}, {"s": "S²⁻", "e": "S", "q": -2}, {"s": "K⁺", "e": "K", "q": 1}, {"s": "F⁻", "e": "F", "q": -1}]}},
       misc=[("atom", "outerElectrons(atomicNumber(X.e))", "That is the neutral atom. The ion has {X.q > 0 ? 'lost' : 'gained'} electrons.")],
       sources=SRC),
   mcq("k3-10-pick", 3, "Which configuration belongs to an element with {o} electrons in its outer shell and {p} shells?", "{shells(z)}",
       [("{shells(z + 1)}", "w1"), ("{shells(z - 1)}", "w2"), ("{shells(z <= 10 ? z + 8 : z - 8)}", "w3")],
       ["{p} shells, with {o} in the last: {answer}.", "That is element number {z}."],
       vars={"z": {"int": [3, 18]}, "o": {"expr": "outerElectrons(z)"}, "p": {"expr": "periodOf(z)"}},
       misc=[("w1", "That has {outerElectrons(z + 1)} outer electron(s) and {periodOf(z + 1)} shell(s)."), ("w2", "That has {outerElectrons(z - 1)} outer electron(s) and {periodOf(z - 1)} shell(s)."),
             ("w3", "That has {periodOf(z <= 10 ? z + 8 : z - 8)} shells, not {p}.")],
       sources=SRC, where=["z != 10 && z != 11 && z != 18", "z != 3"])],
  learn=learn(
    [("Writing configurations",
      "The electronic configuration lists the number of electrons in each shell from the nucleus outwards, separated by commas.\n"
      "Method: start with the atomic number, put {2} in the first shell, up to {8} in the second, up to {8} in the third, and the rest in the fourth.\n"
      "Phosphorus ({15}): {2}, {8}, {5}. Check: {2} + {8} + {5} = {15}."),
     ("The first twenty",
      "• H {1} · He {2}\n• Li {2},{1} · Be {2},{2} · B {2},{3} · C {2},{4} · N {2},{5} · O {2},{6} · F {2},{7} · Ne {2},{8}\n"
      "• Na {2},{8},{1} · Mg {2},{8},{2} · Al {2},{8},{3} · Si {2},{8},{4} · P {2},{8},{5} · S {2},{8},{6} · Cl {2},{8},{7} · Ar {2},{8},{8}\n"
      "• K {2},{8},{8},{1} · Ca {2},{8},{8},{2}\nNotice the pattern repeating in each row."),
     ("Configurations of ions",
      "When an atom becomes an ion, only the electrons change.\n"
      "• Na ({2},{8},{1}) loses {1} → Na⁺ {2},{8}.\n• Cl ({2},{8},{7}) gains {1} → Cl⁻ {2},{8},{8}.\n"
      "Both ions end up with a full outer shell, like a noble gas. This is the key to chemical bonding.")],
    key_words=[("electronic configuration", "the number of electrons in each shell, e.g. {2}, {8}, {1}"),
               ("noble gas configuration", "a full outer shell, like He, Ne or Ar")],
    examples=["Nitrogen ({7}): {2}, {5}", "Silicon ({14}): {2}, {8}, {4}", "Mg²⁺: {2}, {8}"],
    mistake=("Potassium ({19}): {2}, {8}, {9}", "Potassium: {2}, {8}, {8}, {1}",
             "For the first {20} elements the third shell holds {8} before the fourth starts.")))

# ---------------------------------------------------------------- 11. Valence electrons and the Periodic Table
L.lesson(D, S, 11, ("k3-11", "Valence electrons and the Periodic Table"), [10],
  "Valence electrons are the electrons in the outer shell.\n"
  "In the Periodic Table:\n"
  "• the group number = the number of valence electrons (groups I to VII; group VIII or 0 = noble gases, with a full outer shell);\n"
  "• the period number = the number of shells containing electrons.\n"
  "Elements in the same group have the same number of valence electrons, so they have similar chemical properties.\n"
  "Families: group I alkali metals, group II alkaline earth metals, group VII halogens, group VIII (0) noble gases.",
  worked({"z": 16},
         "Sulphur has atomic number {z}. Find its group and period.",
         ["Configuration: {shells(z)}.", "Valence electrons: {outerElectrons(z)}, so group {groupOf(z)}.", "Shells: {periodOf(z)}, so period {periodOf(z)}."],
         "Group {groupOf(z)}, period {periodOf(z)}", checks=["groupOf(z) == 6"]),
  [card("c3k11-1", "Group = number of outer (valence) electrons.",
        ["Chlorine {2}, {8}, {7}: group {7}"], "k3-11-group"),
   card("c3k11-2", "Period = number of shells.",
        ["Chlorine has {3} shells: period {3}"], "k3-11-period"),
   card("c3k11-3", "Same group, same number of valence electrons, similar chemistry.",
        ["Li, Na and K are all in group {1}: alkali metals."], "k3-11-family")],
  [num("k3-11-group", 1, "{nameOf(X)} has atomic number {z}. Which group is it in?", "groupOf(z)",
       ["Configuration: {shells(z)}.", "{z == 2 ? 'Helium has a full outer shell: it is a noble gas, group 8 (0).' : 'Valence electrons: ' + outerElectrons(z) + '.'} Group {answer}."],
       vars=EL3, misc=[("period", "periodOf(z)", "That is the period (number of shells). The group is the number of outer electrons.")],
       sources=SRC, where=["groupOf(z) != periodOf(z)"]),
   num("k3-11-period", 1, "{nameOf(X)} has atomic number {z}. Which period is it in?", "periodOf(z)",
       ["Configuration: {shells(z)}.", "Number of shells: {answer}, so period {answer}."],
       vars=EL3, misc=[("group", "groupOf(z)", "That is the group. The period is the number of shells.")],
       sources=SRC, where=["groupOf(z) != periodOf(z)"]),
   mcq("k3-11-family", 2, "{nameOf(X)} (atomic number {z}) belongs to which family?", "{familyOf(z)}",
       [("{familyOf(z) == 'alkali metals' ? 'halogens' : 'alkali metals'}", "f1"), ("{familyOf(z) == 'noble gases' ? 'halogens' : 'noble gases'}", "f2"),
        ("{familyOf(z) == 'alkaline earth metals' ? 'halogens' : 'alkaline earth metals'}", "f3")],
       ["Configuration {shells(z)}: group {groupOf(z)}.", "Group {groupOf(z)} is the {answer}."],
       vars={"X": {"pick": ["Li", "Na", "K", "Be", "Mg", "Ca", "F", "Cl", "He", "Ne", "Ar"]}, "z": {"expr": "atomicNumber(X)"}},
       misc=[("f1", "Group {groupOf(z)}: {familyOf(z)}. Alkali metals are group {1}, halogens group {7}."), ("f2", "Group {groupOf(z)}: {familyOf(z)}. Noble gases have a full outer shell."),
             ("f3", "Group {groupOf(z)}: {familyOf(z)}. {familyOf(z) == 'alkaline earth metals' ? 'Halogens are group ' + 7 + '.' : 'Alkaline earth metals are group ' + 2 + '.'}")],
       sources=SRC),
   num("k3-11-z", 2, "An element is in group {g} and period {p}. What is its atomic number?", "z",
       ["Period {p}: {p} shells; group {g}: {g} electron(s) in the outer shell.", "Configuration {shells(z)}, so the atomic number is {answer}."],
       vars={"z": {"int": [3, 20]}, "g": {"expr": "groupOf(z)"}, "p": {"expr": "periodOf(z)"}},
       misc=[("add", "g + p", "Build the configuration and add all the electrons, not just the group and period numbers.")],
       sources=SRC, where=["g + p != z", "g != 8"]),
   bank("k3-11-same", 3, "{X.q}", [
     {"q": "Why do sodium and potassium react in a similar way?", "r": "Both have one electron in the outer shell", "w": ["Both have the same number of shells", "Both have the same atomic number", "Both are gases"],
      "e": ["Sodium has 3 shells, potassium 4.", "Their atomic numbers are 11 and 19.", "Both are solid metals."], "y": "Same group: same number of valence electrons."},
     {"q": "Which pair of elements are in the same period?", "r": "sodium and chlorine", "w": ["sodium and potassium", "fluorine and chlorine", "helium and neon"],
      "e": ["Same group (I), different periods.", "Same group (VII), different periods.", "Both noble gases, different periods."], "y": "Na (2,8,1) and Cl (2,8,7) both have 3 shells."},
     {"q": "Why are the noble gases very unreactive?", "r": "Their outer shells are full", "w": ["They have no electrons", "They are very heavy", "They have one outer electron"],
      "e": ["They have electrons; their outer shell is full.", "Mass does not explain it.", "That describes group I."], "y": "A full outer shell is a stable arrangement."}], SRC)],
  learn=learn(
    [("Outer electrons decide the group",
      "The electrons in the outer shell are called valence electrons. They are the ones used in reactions.\n"
      "In the Periodic Table, the group (column) number tells you the number of valence electrons: group I has {1}, group II has {2}, … group VII has {7}.\n"
      "Group VIII (also called group {0}) holds the noble gases, whose outer shells are full."),
     ("Shells decide the period",
      "The period (row) number tells you how many shells contain electrons. Lithium ({2}, {1}) has {2} shells, so it is in period {2}; sodium ({2}, {8}, {1}) is in period {3}.\n"
      "So from the configuration you can place any of the first {20} elements: chlorine ({2}, {8}, {7}) is group VII, period {3}."),
     ("Families with similar chemistry",
      "Elements in the same group have the same number of valence electrons, so they react in similar ways:\n"
      "• group I: alkali metals (Li, Na, K);\n• group II: alkaline earth metals (Be, Mg, Ca);\n• group VII: halogens (F, Cl, Br, I);\n• group VIII ({0}): noble gases (He, Ne, Ar).\n"
      "Going down a group, the number of shells increases.")],
    key_words=[("valence electrons", "electrons in the outer shell"), ("group", "a column of the Periodic Table: same number of valence electrons"),
               ("period", "a row of the Periodic Table: same number of shells")],
    examples=["Magnesium {2},{8},{2}: group II, period {3}", "Oxygen {2},{6}: group VI, period {2}", "Potassium {2},{8},{8},{1}: group I, period {4}"],
    mistake=("Chlorine ({2}, {8}, {7}) is in group {3}", "Chlorine is in group VII (seven outer electrons) and period {3}",
             "The group counts outer electrons; the period counts shells.")))

# ---------------------------------------------------------------- 12. Alkali metals and halogens
SRC = ["groups"]
L.lesson(D, S, 12, ("k3-12", "Electronic configuration and chemical properties: alkali metals and halogens"), [11],
  "Alkali metals (group I: Li, Na, K) have 1 valence electron, which they lose easily to form +1 ions.\n"
  "• Soft, shiny when cut, stored under oil; react vigorously with water to give an alkaline hydroxide and hydrogen: 2Na + 2H₂O → 2NaOH + H₂.\n"
  "• Reactivity increases down the group (the outer electron is further from the nucleus and lost more easily): K > Na > Li.\n"
  "Halogens (group VII: F, Cl, Br, I) have 7 valence electrons and gain 1 to form −1 ions (halide ions).\n"
  "• Coloured, poisonous non-metals; diatomic molecules (Cl₂). Reactivity decreases down the group: F > Cl > Br > I.\n"
  "• They react with alkali metals to form salts: 2Na + Cl₂ → 2NaCl.",
  worked({},
         "Explain why potassium reacts more vigorously with water than sodium.",
         ["Both have {1} valence electron and react by losing it.", "Potassium has more shells ({2}, {8}, {8}, {1}), so its outer electron is further from the nucleus.",
          "It is held less strongly and lost more easily, so potassium is more reactive."],
         "Its outer electron is further from the nucleus and is lost more easily"),
  [card("c3k12-1", "Alkali metals lose {1} electron to form +{1} ions; reactivity increases down the group.",
        ["Na → Na⁺ + e⁻"], "k3-12-alk"),
   card("c3k12-2", "Halogens gain {1} electron to form −{1} ions; reactivity decreases down the group.",
        ["Cl + e⁻ → Cl⁻"], "k3-12-hal"),
   card("c3k12-3", "Alkali metal + water → alkaline hydroxide + hydrogen.",
        ["{'2Na + 2H₂O → 2NaOH + H₂'}"], "k3-12-water")],
  [bank("k3-12-alk", 1, "{X.q}", [
     {"q": "Why are sodium and potassium stored under oil?", "r": "They react quickly with air and water", "w": ["They are poisonous gases", "They dissolve in oil", "They are too heavy"],
      "e": ["They are solid metals.", "The oil keeps air and water away; they do not dissolve in it.", "They are light metals."], "y": "Oil keeps out the air and moisture."},
     {"q": "Which alkali metal is the most reactive?", "r": "potassium", "w": ["lithium", "sodium", "they are all equally reactive"],
      "e": ["Lithium is the least reactive of the three.", "Sodium is less reactive than potassium.", "Reactivity increases down the group."], "y": "Potassium's outer electron is furthest from the nucleus."},
     {"q": "What ion does an alkali metal form?", "r": "a +1 ion", "w": ["a −1 ion", "a +2 ion", "no ion"],
      "e": ["Metals lose electrons, making positive ions.", "Group I has one electron to lose.", "They readily form ions."], "y": "Losing the single outer electron gives +1."}], SRC),
   bank("k3-12-hal", 1, "{X.q}", [
     {"q": "Which halogen is the most reactive?", "r": "fluorine", "w": ["iodine", "bromine", "chlorine"],
      "e": ["Iodine is the least reactive.", "Bromine is below chlorine.", "Chlorine is below fluorine."], "y": "Reactivity of halogens decreases down the group."},
     {"q": "What ion does a halogen form?", "r": "a −1 ion (halide)", "w": ["a +1 ion", "a −7 ion", "a +7 ion"],
      "e": ["Non-metals gain electrons.", "It gains only one electron to fill its shell.", "It gains, not loses, electrons."], "y": "Seven outer electrons: gaining one fills the shell."},
     {"q": "How does chlorine exist at room temperature?", "r": "as a green-yellow gas of Cl₂ molecules", "w": ["as a shiny metal", "as single Cl atoms", "as a purple solid"],
      "e": ["Chlorine is a non-metal.", "Chlorine atoms pair up into Cl₂.", "That describes iodine."], "y": "Halogens are diatomic: Cl₂."}], SRC),
   bank("k3-12-water", 2, "{X.q}", [
     {"q": "Sodium is added to water. What are the products?", "r": "sodium hydroxide and hydrogen", "w": ["sodium oxide and oxygen", "sodium chloride and water", "sodium and hydrogen chloride"],
      "e": ["The gas given off is hydrogen.", "No chlorine is present.", "Sodium reacts, so it is not left as sodium."], "y": "2Na + 2H₂O → 2NaOH + H₂."},
     {"q": "After potassium reacts with water, the solution turns universal indicator purple. Why?", "r": "Potassium hydroxide is a strong alkali", "w": ["The solution is acidic", "Hydrogen colours the indicator", "Potassium is purple"],
      "e": ["Purple means alkaline.", "Hydrogen gas escapes; it does not colour the solution.", "Potassium is a silvery metal."], "y": "Alkali metals form alkaline hydroxides."},
     {"q": "What forms when sodium burns in chlorine?", "r": "sodium chloride (common salt)", "w": ["sodium hydroxide", "chlorine oxide", "hydrogen chloride"],
      "e": ["No water is involved.", "Oxygen is not involved.", "No hydrogen is involved."], "y": "2Na + Cl₂ → 2NaCl."}], SRC),
   num("k3-12-e", 2, "How many electrons must {X.n} {X.v} to reach a full outer shell?", "X.k",
       ["Configuration of {X.n}: {shells(atomicNumber(X.s))}.", "It is easier to {X.v} {answer} electron(s) than to {X.v == 'lose' ? 'gain' : 'lose'} {8 - X.k}."],
       vars={"X": {"pick": [{"n": "sodium", "s": "Na", "v": "lose", "k": 1}, {"n": "potassium", "s": "K", "v": "lose", "k": 1}, {"n": "lithium", "s": "Li", "v": "lose", "k": 1},
                            {"n": "chlorine", "s": "Cl", "v": "gain", "k": 1}, {"n": "fluorine", "s": "F", "v": "gain", "k": 1}]}},
       misc=[("seven", "7", "{X.v == 'lose' ? 'Losing seven would be much harder than losing one.' : 'It already has seven: it needs only one more.'}")],
       review="authored", sources=SRC),
   bank("k3-12-trend", 3, "{X.q}", [
     {"q": "Why does reactivity INCREASE down group I but DECREASE down group VII?", "r": "Group I loses an electron (easier when far from the nucleus); group VII gains one (harder when far from the nucleus)", "w": ["Both groups gain electrons", "Atoms get smaller down both groups", "Group VII metals lose electrons"],
      "e": ["Group I metals lose electrons.", "Atoms get larger down a group.", "Halogens are non-metals that gain electrons."], "y": "Distance from the nucleus helps losing but hinders gaining."},
     {"q": "Chlorine water is added to potassium bromide solution and the solution turns orange. Why?", "r": "Chlorine is more reactive and displaces bromine", "w": ["Bromine displaces chlorine", "Potassium turns orange", "No reaction happens"],
      "e": ["The less reactive halogen cannot displace a more reactive one.", "Potassium ions are colourless.", "The orange colour shows bromine has formed."], "y": "Cl₂ + 2KBr → 2KCl + Br₂."},
     {"q": "Rubidium is below potassium in group I. Predict its reaction with water.", "r": "even more violent than potassium", "w": ["slower than lithium", "no reaction", "it forms an acid"],
      "e": ["It is lower in the group, so more reactive.", "All alkali metals react with water.", "It forms an alkaline hydroxide."], "y": "Reactivity increases down group I."}], SRC)],
  learn=learn(
    [("Group I: the alkali metals",
      "Lithium, sodium and potassium have {1} electron in the outer shell. They react by losing it to form ions with a +{1} charge: Na → Na⁺ + e⁻.\n"
      "They are soft (they can be cut with a knife), shiny when freshly cut, and so reactive that they are stored under oil.\n"
      "With water they fizz, giving hydrogen gas and an alkaline solution of the hydroxide: {'2Na + 2H₂O → 2NaOH + H₂'}. That is why they are called alkali metals."),
     ("Reactivity down group I",
      "Going down the group, atoms have more shells, so the outer electron is further from the nucleus and more shielded. It is held less strongly and lost more easily.\n"
      "So reactivity increases: lithium fizzes steadily, sodium melts into a ball and races around, potassium bursts into a lilac flame."),
     ("Group VII: the halogens",
      "Fluorine, chlorine, bromine and iodine have {7} outer electrons. They react by gaining {1} electron to form −{1} ions (fluoride, chloride, bromide, iodide).\n"
      "They are coloured, poisonous non-metals made of pairs of atoms (Cl₂). Going down the group, the extra electron is attracted less strongly, so reactivity decreases: fluorine is the most reactive.\n"
      "A more reactive halogen displaces a less reactive one from its salts.")],
    key_words=[("alkali metals", "group I: Li, Na, K…"), ("halogens", "group VII: F, Cl, Br, I"), ("halide", "a −{1} ion of a halogen"),
               ("displacement", "a more reactive element pushing a less reactive one out of a compound")],
    examples=["{'2K + 2H₂O → 2KOH + H₂'}", "{'2Na + Cl₂ → 2NaCl'}", "{'Cl₂ + 2KI → 2KCl + I₂'}"],
    mistake=("Halogens get more reactive down the group, like alkali metals", "Halogen reactivity decreases down the group",
             "Halogens gain an electron, and that is harder when the outer shell is further from the nucleus.")))

# ---------------------------------------------------------------- 13. Alkaline earth metals and halogens
SRC = ["groups"]
L.lesson(D, S, 13, ("k3-13", "Electronic configuration and chemical properties: alkaline earth metals and halogens"), [12],
  "Alkaline earth metals (group II: Be, Mg, Ca) have 2 valence electrons and lose both to form +2 ions (Mg²⁺, Ca²⁺).\n"
  "• Harder and less reactive than group I. Reactivity increases down the group: Ca > Mg > Be.\n"
  "• Calcium reacts steadily with cold water: Ca + 2H₂O → Ca(OH)₂ + H₂. Magnesium reacts very slowly with cold water but burns in steam and with a bright white flame in air: 2Mg + O₂ → 2MgO.\n"
  "With halogens they form halides with formula MX₂: Mg + Cl₂ → MgCl₂ (one Mg²⁺ for two Cl⁻).\n"
  "Their oxides and hydroxides are basic; calcium hydroxide solution is limewater.",
  worked({},
         "Write the formula of calcium chloride and explain it.",
         ["Calcium is in group II: it loses {2} electrons, forming Ca²⁺.", "Chlorine is in group VII: each atom gains {1} electron, forming Cl⁻.", "Two Cl⁻ balance one Ca²⁺."],
         "CaCl₂"),
  [card("c3k13-1", "Group II metals lose {2} electrons to form +{2} ions.",
        ["{'Mg → Mg²⁺ + 2e⁻'}"], "k3-13-ion"),
   card("c3k13-2", "Reactivity increases down group II but is less than group I.",
        ["Calcium reacts with cold water; magnesium hardly."], "k3-13-react"),
   card("c3k13-3", "Group II halides have formula MX₂.",
        ["{'Mg²⁺ + 2Cl⁻ → MgCl₂'}"], "k3-13-formula")],
  [bank("k3-13-ion", 1, "{X.q}", [
     {"q": "What ion does magnesium form?", "r": "Mg²⁺", "w": ["Mg⁺", "Mg²⁻", "Mg⁻"],
      "e": ["It has two outer electrons to lose.", "Metals lose electrons: positive ions.", "Metals form positive ions."], "y": "Losing two electrons gives +2."},
     {"q": "How many valence electrons does calcium have?", "r": "2", "w": ["1", "8", "20"],
      "e": ["That is group I.", "That is a full shell.", "20 is the atomic number."], "y": "Ca: 2, 8, 8, 2 — group II."},
     {"q": "What is the configuration of the calcium ion Ca²⁺?", "r": "2, 8, 8", "w": ["2, 8, 8, 2", "2, 8, 8, 4", "2, 8"],
      "e": ["That is the atom; the ion has lost two electrons.", "It loses electrons, not gains.", "It loses only 2 electrons, not 10."], "y": "20 − 2 = 18 electrons: 2, 8, 8."}], SRC),
   bank("k3-13-react", 1, "{X.q}", [
     {"q": "Which reacts fastest with cold water?", "r": "calcium", "w": ["magnesium", "beryllium", "they react equally"],
      "e": ["Magnesium reacts very slowly with cold water.", "Beryllium hardly reacts.", "Reactivity increases down group II."], "y": "Calcium is lowest of the three in group II."},
     {"q": "How does magnesium burn in air?", "r": "with a very bright white flame, forming magnesium oxide", "w": ["with a lilac flame", "it does not burn", "with a green flame forming magnesium chloride"],
      "e": ["Lilac is potassium.", "Magnesium ribbon burns brightly.", "No chlorine is in air."], "y": "2Mg + O₂ → 2MgO."},
     {"q": "Compared with sodium, magnesium is…", "r": "less reactive", "w": ["more reactive", "equally reactive", "unreactive like a noble gas"],
      "e": ["Losing two electrons takes more energy than losing one.", "Group II is less reactive than group I in the same period.", "It does react."], "y": "Group II metals are less reactive than group I."}], SRC),
   mcq("k3-13-formula", 2, "What is the formula of {compoundName(M, X)}?", "{formula(compoundFormula(M, X))}",
       [("{formula(M + X)}", "one"), ("{formula(M + '2' + X)}", "swap"), ("{formula(M + X + '3')}", "three")],
       ["{M} forms {M}²⁺; {X} forms {X}⁻.", "Two {X}⁻ balance one {M}²⁺: {answer}."],
       vars={"M": {"pick": ["Mg", "Ca"]}, "X": {"pick": ["Cl", "F", "I"]}},
       misc=[("one", "One {X}⁻ cannot balance a +{2} charge."), ("swap", "The metal has the +{2} charge; you need two halide ions, not two metal atoms."),
             ("three", "+{2} is balanced by two −{1} ions, not three.")],
       sources=SRC),
   bank("k3-13-water", 2, "{X.q}", [
     {"q": "Calcium reacts with water. What are the products?", "r": "calcium hydroxide and hydrogen", "w": ["calcium oxide and oxygen", "calcium chloride and hydrogen", "calcium carbonate and water"],
      "e": ["The gas is hydrogen; the hydroxide forms in water.", "There is no chlorine.", "There is no carbon."], "y": "Ca + 2H₂O → Ca(OH)₂ + H₂."},
     {"q": "What is limewater?", "r": "a solution of calcium hydroxide", "w": ["a solution of lemon juice", "calcium carbonate", "sodium hydroxide solution"],
      "e": ["It is alkaline, not acidic.", "Calcium carbonate is chalk; it is insoluble.", "Limewater contains calcium, not sodium."], "y": "Ca(OH)₂ in water; it turns milky with carbon dioxide."},
     {"q": "Are the oxides of group II metals acidic or basic?", "r": "basic", "w": ["acidic", "neutral", "they do not form oxides"],
      "e": ["Metal oxides are basic.", "They react with acids, so they are not neutral.", "They burn to form oxides."], "y": "MgO and CaO are bases; they neutralise acids."}], SRC),
   bank("k3-13-compare", 3, "{X.q}", [
     {"q": "Why is calcium less reactive than potassium, although both are in period 4?", "r": "Calcium must lose two electrons, which needs more energy than losing one", "w": ["Calcium has fewer shells", "Calcium is a non-metal", "Potassium has more protons"],
      "e": ["Both have 4 shells.", "Calcium is a metal.", "Calcium has more protons (20) than potassium (19)."], "y": "Removing two electrons is harder, and calcium's nucleus holds them more strongly."},
     {"q": "Strontium is below calcium in group II. How does it react with water?", "r": "faster than calcium", "w": ["slower than magnesium", "not at all", "it forms an acid"],
      "e": ["It is lower in the group, so more reactive.", "Group II metals react with water.", "It forms an alkaline hydroxide."], "y": "Reactivity increases down group II."},
     {"q": "Magnesium burns in chlorine. What is the formula of the product?", "r": "MgCl₂", "w": ["MgCl", "Mg₂Cl", "MgCl₇"],
      "e": ["Mg²⁺ needs two Cl⁻.", "One Mg²⁺ and two Cl⁻, not two Mg.", "Each chloride ion is −1, so only two are needed."], "y": "Mg + Cl₂ → MgCl₂."}], SRC)],
  learn=learn(
    [("Group II: the alkaline earth metals",
      "Beryllium, magnesium and calcium have {2} outer electrons. They react by losing both to form ions with a +{2} charge: Mg → Mg²⁺ + {2}e⁻.\n"
      "Losing two electrons takes more energy than losing one, so they are less reactive than the alkali metals next to them. They are also harder and denser."),
     ("How they react",
      "• With water: calcium fizzes steadily in cold water, giving calcium hydroxide and hydrogen; magnesium reacts only very slowly with cold water but quickly with steam.\n"
      "• With air: magnesium ribbon burns with a dazzling white flame, forming white magnesium oxide.\n"
      "• Reactivity increases down the group: beryllium < magnesium < calcium.\n"
      "Calcium hydroxide solution is limewater, used to test for carbon dioxide."),
     ("With halogens",
      "Group II metals react with halogens to form salts. One M²⁺ ion needs two halide ions (each −{1}) to balance its charge, so the formula is MX₂: MgCl₂, CaF₂, CaCl₂.\n"
      "The halogens behave as in the last lesson: they gain one electron each, and fluorine is the most reactive.")],
    key_words=[("alkaline earth metals", "group II: Be, Mg, Ca…"), ("limewater", "calcium hydroxide solution"), ("basic oxide", "a metal oxide that neutralises acids")],
    examples=["{'Ca + 2H₂O → Ca(OH)₂ + H₂'}", "{'2Mg + O₂ → 2MgO'}", "{'Mg + Cl₂ → MgCl₂'}"],
    mistake=("Magnesium chloride is MgCl", "Magnesium chloride is MgCl₂",
             "Mg²⁺ carries two positive charges, so it needs two Cl⁻ ions.")))
