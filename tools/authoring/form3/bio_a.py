"""Form 3 Biology, Term 1, rows 1-9 (cells, water, diffusion, osmosis, classification). Run: python tools/authoring/form3/bio_a.py
Practicals (rows 3 and 8) are taught as guided preparation: method, observations and calculations."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "biology", "biology"

# ---------------------------------------------------------------- 1. Cells, types, cell theory
SRC = ["cells"]
L.lesson(D, S, 1, ("b3-1", "Cells: prokaryotic and eukaryotic cells; the cell theory"), [],
  "The cell is the basic unit of structure and function of all living things.\n"
  "Cell theory: (1) all living things are made of one or more cells; (2) the cell is the basic unit of life; (3) all cells come from pre-existing cells.\n"
  "Two types of cell:\n"
  "• Prokaryotic (bacteria): small (about 1–10 µm), no true nucleus (DNA lies free in the cytoplasm), no membrane-bound organelles, small ribosomes.\n"
  "• Eukaryotic (plants, animals, fungi, protoctists): larger (10–100 µm), a true nucleus with a nuclear membrane, membrane-bound organelles such as mitochondria.\n"
  "Sizes: 1 mm = 1000 µm. Real size = image size ÷ magnification.",
  worked({"img": 50, "mag": 400},
         "A drawing of a cheek cell is {img} mm long at a magnification of ×{mag}. Find the real length of the cell in µm.",
         ["Real size = image size ÷ magnification = {img} ÷ {mag} = {realSize(img, mag)} mm.", "{1} mm = {1000} µm, so the cell is {realSize(img, mag) * 1000} µm long."],
         "{realSize(img, mag) * 1000} µm", checks=["realSize(img, mag) * 1000 == 125"]),
  [card("c3b1-1", "All living things are made of cells, and cells come from other cells.",
        ["A new skin cell forms when an old one divides."], "b3-1-theory"),
   card("c3b1-2", "Prokaryotic cells have no true nucleus; eukaryotic cells do.",
        ["Bacteria are prokaryotes; you are made of eukaryotic cells."], "b3-1-type"),
   card("c3b1-3", "Real size = image size ÷ magnification.",
        ["Image {20} mm at ×{100}: real size {0.2} mm = {200} µm"], "b3-1-size")],
  [bank("b3-1-theory", 1, "{X.q}", [
     {"q": "Which is a statement of the cell theory?", "r": "All cells come from pre-existing cells", "w": ["Cells can form from non-living matter", "Only animals are made of cells", "Viruses are the smallest cells"],
      "e": ["The theory says new cells come only from dividing cells.", "Plants, fungi and bacteria are made of cells too.", "Viruses are not cells."], "y": "Cells arise only from other cells by division."},
     {"q": "What is the basic unit of structure and function in living things?", "r": "the cell", "w": ["the organ", "the tissue", "the atom"],
      "e": ["Organs are made of many cells.", "Tissues are groups of cells.", "Atoms are not alive."], "y": "Every living thing is made of one or more cells."},
     {"q": "Who first named 'cells' after looking at cork?", "r": "Robert Hooke", "w": ["Charles Darwin", "Louis Pasteur", "Isaac Newton"],
      "e": ["Darwin is known for evolution.", "Pasteur worked on germs and vaccines.", "Newton worked on forces and light."], "y": "Hooke looked at cork in 1665."}], SRC),
   bank("b3-1-type", 1, "{X.q}", [
     {"q": "Which feature is found only in eukaryotic cells?", "r": "a nucleus with a nuclear membrane", "w": ["a cell membrane", "cytoplasm", "ribosomes"],
      "e": ["All cells have a cell membrane.", "All cells have cytoplasm.", "Prokaryotes have (smaller) ribosomes too."], "y": "Prokaryotes have DNA free in the cytoplasm, not in a nucleus."},
     {"q": "Which organism is made of prokaryotic cells?", "r": "a bacterium", "w": ["a maize plant", "a mushroom", "an amoeba"],
      "e": ["Plants are eukaryotes.", "Fungi are eukaryotes.", "Protoctists like Amoeba are eukaryotes."], "y": "Bacteria are the prokaryotes."},
     {"q": "Which statement about prokaryotic cells is true?", "r": "They have no membrane-bound organelles such as mitochondria", "w": ["They are larger than eukaryotic cells", "They have a true nucleus", "They are found only in animals"],
      "e": ["They are usually much smaller.", "They have no true nucleus.", "Bacteria are not animals."], "y": "Prokaryotes lack a nucleus and membrane-bound organelles."}], SRC),
   num("b3-1-size", 2, "A cell's image is {img} mm long at magnification ×{mag}. What is its real length in micrometres (µm)?", "realSize(img, mag) * 1000",
       ["Real size = {img} ÷ {mag} = {realSize(img, mag)} mm.", "× {1000} for µm: {answer} µm."],
       vars={"mag": {"pick": [40, 100, 400]}, "k": {"int": [2, 20]}, "img": {"expr": "k * mag / 200"}},
       misc=[("mm", "realSize(img, mag)", "That is in millimetres. {1} mm = {1000} µm."), ("times", "img * mag", "Divide by the magnification: the real cell is smaller than the drawing.")],
       unit="µm", sources=SRC),
   num("b3-1-mag", 3, "A bacterium {r} µm long is drawn {d} mm long. What is the magnification of the drawing?", "d * 1000 / r",
       ["Same units: {d} mm = {d * 1000} µm.", "Magnification = image ÷ real = {d * 1000} ÷ {r} = ×{answer}."],
       vars={"r": {"pick": [1, 2, 4, 5]}, "d": {"int": [10, 40], "step": 2}},
       misc=[("units", "d / r", "Change the image size to µm first (× {1000})."), ("flip", "r / (d * 1000)", "Magnification = image size ÷ real size.")],
       sources=SRC)],
  learn=learn(
    [("The unit of life",
      "Every living thing, from a bacterium to a mango tree to you, is made of cells. Some organisms, like bacteria and Amoeba, are a single cell; you are made of millions of millions.\n"
      "The cell theory sums this up:\n• all living things are made of cells;\n• the cell is the basic unit of structure and function;\n• all cells come from pre-existing cells by division."),
     ("Two kinds of cell",
      "• Prokaryotic cells (bacteria) are small. Their DNA lies free in the cytoplasm: there is no true nucleus. They have no membrane-bound organelles.\n"
      "• Eukaryotic cells (plants, animals, fungi, protoctists) are larger. Their DNA is inside a nucleus surrounded by a nuclear membrane, and they contain organelles such as mitochondria.\n"
      "'Pro' means before and 'karyon' means nucleus: prokaryotes came before the nucleus."),
     ("How big are cells?",
      "Cells are measured in micrometres: {1} mm = {1000} µm. Most bacteria are {1}–{10} µm long; most plant and animal cells {10}–{100} µm.\n"
      "In a drawing or photograph: real size = image size ÷ magnification. A cell drawn {50} mm long at ×{400} is really {0.125} mm = {125} µm long.")],
    key_words=[("cell", "the basic unit of life"), ("prokaryote", "an organism whose cells have no true nucleus (bacteria)"),
               ("eukaryote", "an organism whose cells have a nucleus"), ("micrometre (µm)", "one thousandth of a millimetre")],
    examples=["Bacterium: prokaryote, about {2} µm", "Onion epidermis cell: eukaryote, about {100} µm", "Real size = {20} mm ÷ {100} = {0.2} mm"],
    mistake=("Real size = image size × magnification", "Real size = image size ÷ magnification",
             "The drawing is magnified, so the real cell is smaller: divide.")))

# ---------------------------------------------------------------- 2. Ultrastructure of plant and animal cells
SRC = ["cells"]
ORG = [{"o": "nucleus", "f": "controls the cell's activities and contains the DNA (genetic material)"},
       {"o": "mitochondrion", "f": "carries out aerobic respiration, releasing energy"},
       {"o": "ribosome", "f": "makes proteins"},
       {"o": "chloroplast", "f": "carries out photosynthesis"},
       {"o": "cell membrane", "f": "controls what enters and leaves the cell"},
       {"o": "cell wall", "f": "gives the plant cell shape and support"},
       {"o": "vacuole", "f": "stores cell sap and keeps the plant cell firm (turgid)"},
       {"o": "rough endoplasmic reticulum", "f": "transports proteins made by its ribosomes"},
       {"o": "Golgi body", "f": "packages and sends out substances made by the cell"}]
L.lesson(D, S, 2, ("b3-2", "Ultrastructure of plant and animal cells"), [1],
  "Under the electron microscope cells show many organelles:\n"
  "• Nucleus: contains DNA, controls the cell. • Mitochondria: aerobic respiration, release energy. • Ribosomes: make proteins.\n"
  "• Endoplasmic reticulum (ER): transport channels; rough ER has ribosomes. • Golgi body: packages and secretes substances.\n"
  "• Cell membrane: partially permeable, controls entry and exit. • Cytoplasm: where most reactions happen.\n"
  "Only in plant cells: cellulose cell wall (support), chloroplasts (photosynthesis), large permanent vacuole with cell sap.\n"
  "Animal cells have small temporary vacuoles and centrioles (used in cell division).",
  worked({},
         "Give three differences between a palisade cell of a leaf and a cell from the lining of your cheek.",
         ["The leaf cell has a cellulose cell wall; the cheek cell has only a cell membrane.", "The leaf cell has chloroplasts; the cheek cell has none.",
          "The leaf cell has a large permanent vacuole; the cheek cell has only small temporary vacuoles."],
         "Cell wall, chloroplasts and a large vacuole in the plant cell only"),
  [card("c3b2-1", "Each organelle has a job.",
        ["Mitochondria release energy by respiration."], "b3-2-func"),
   card("c3b2-2", "Plant cells have a cell wall, chloroplasts and a large vacuole.",
        ["Animal cells have none of these."], "b3-2-plant"),
   card("c3b2-3", "Use the lettered drawing to name parts.",
        ["Find the green discs: the chloroplasts."], "b3-2-letter")],
  [mcq("b3-2-func", 1, "What is the function of the {X.o}?", "{X.f}",
       [("{Y.f}", "y"), ("{Z.f}", "z"), ("{W.f}", "w")],
       ["The {X.o} {X.f}.", "So the answer is: {answer}."],
       vars={"X": {"pick": ORG}, "Y": {"pick": ORG}, "Z": {"pick": ORG}, "W": {"pick": ORG}},
       misc=[("y", "That is the job of the {Y.o}."), ("z", "That is the job of the {Z.o}."), ("w", "That is the job of the {W.o}.")],
       review="authored", sources=SRC, where=["X.o != Y.o && X.o != Z.o && X.o != W.o && Y.o != Z.o && Y.o != W.o && Z.o != W.o"]),
   bank("b3-2-plant", 1, "{X.q}", [
     {"q": "Which structure is found in plant cells but not in animal cells?", "r": "cell wall", "w": ["cell membrane", "nucleus", "mitochondrion"],
      "e": ["Both have a cell membrane.", "Both have a nucleus.", "Both have mitochondria."], "y": "Only plant cells have a cellulose cell wall."},
     {"q": "Which structure is found in both plant and animal cells?", "r": "mitochondrion", "w": ["chloroplast", "cellulose cell wall", "large permanent vacuole"],
      "e": ["Only plant cells have chloroplasts.", "Only plant cells have a cell wall.", "Animal cells have only small vacuoles."], "y": "Both kinds of cell respire."},
     {"q": "Which structure is found in animal cells but not in most plant cells?", "r": "centrioles", "w": ["chloroplasts", "cell wall", "cell membrane"],
      "e": ["Chloroplasts are plant structures.", "The cell wall is a plant structure.", "Both have a membrane."], "y": "Centrioles help animal cells divide."}], SRC),
   mcq("b3-2-letter", 2, "In the drawing of a plant cell, which letter labels the {plantPart(i)}?", "{bioLetter(k, 6, i)}",
       [("{bioLetter(k, 6, (i + 1) % 6)}", "a"), ("{bioLetter(k, 6, (i + 2) % 6)}", "b"), ("{bioLetter(k, 6, (i + 3) % 6)}", "c")],
       ["The {plantPart(i)} is labelled {answer}."],
       vars={"k": {"int": [0, 719]}, "i": {"int": [0, 5]}},
       misc=[("a", "That is the {plantPart((i + 1) % 6)}."), ("b", "That is the {plantPart((i + 2) % 6)}."), ("c", "That is the {plantPart((i + 3) % 6)}.")],
       figure="plantCell(k)", sources=SRC),
   bank("b3-2-which", 2, "{X.q}", [
     {"q": "Which cells would have the most mitochondria?", "r": "muscle cells, which need a lot of energy", "w": ["fat storage cells", "dead xylem cells", "red blood cells of mammals"],
      "e": ["Fat cells mostly store fat.", "Dead cells have no organelles.", "Mature red blood cells have no mitochondria."], "y": "Active cells need much respiration."},
     {"q": "A cell makes and sends out many enzymes (proteins). Which organelles will it have many of?", "r": "ribosomes, rough ER and Golgi bodies", "w": ["chloroplasts", "large vacuoles", "cell walls"],
      "e": ["Chloroplasts make sugar, not enzymes.", "Vacuoles store sap.", "Cell walls give support."], "y": "Proteins are made on ribosomes, moved by rough ER and packaged by Golgi."},
     {"q": "Root hair cells have no chloroplasts. Why?", "r": "They are underground, where there is no light for photosynthesis", "w": ["They are animal cells", "They make proteins only", "They have no nucleus"],
      "e": ["They are plant cells.", "That is not the reason.", "They have a nucleus."], "y": "Chloroplasts would be useless in the dark."}], SRC),
   bank("b3-2-compare", 3, "{X.q}", [
     {"q": "A cell has a nucleus, mitochondria, a cellulose wall and chloroplasts. It is…", "r": "a plant cell", "w": ["an animal cell", "a bacterium", "a virus"],
      "e": ["Animal cells have no cell wall or chloroplasts.", "Bacteria have no nucleus.", "A virus is not a cell."], "y": "Wall and chloroplasts: plant."},
     {"q": "A cell has DNA free in the cytoplasm, a cell wall and no mitochondria. It is…", "r": "a bacterium", "w": ["a plant cell", "an animal cell", "a yeast cell"],
      "e": ["Plant cells have a nucleus and mitochondria.", "Animal cells have a nucleus and no wall.", "Yeast is a eukaryote with a nucleus."], "y": "No nucleus and no mitochondria: prokaryote."},
     {"q": "Why is the cell membrane described as partially permeable?", "r": "It lets some substances through but not others", "w": ["It lets everything through", "It lets nothing through", "It is only partly made"],
      "e": ["Then it could not control entry.", "Then the cell could not take in food or oxygen.", "It is complete."], "y": "It controls which substances enter and leave."}], SRC)],
  learn=learn(
    [("Seeing more detail",
      "With a light microscope you see the cell wall, membrane, cytoplasm, nucleus, vacuole and chloroplasts. An electron microscope magnifies much more and shows the ultrastructure: many tiny organelles, each with a job.\n"
      "• Nucleus: holds the DNA and controls the cell.\n• Mitochondria: aerobic respiration releases energy.\n• Ribosomes: make proteins.\n"
      "• Endoplasmic reticulum: a network of channels; rough ER is covered in ribosomes.\n• Golgi body: packages substances for export."),
     ("Plant cells",
      "Plant cells have, in addition:\n• a cellulose cell wall, which gives shape and support;\n• chloroplasts, where photosynthesis happens;\n• a large permanent vacuole full of cell sap, which keeps the cell firm.\n"
      "Inside the wall is the cell membrane, which is partially permeable: it controls what enters and leaves.", "plantCell(0)"),
     ("Animal cells",
      "Animal cells have a membrane, cytoplasm, nucleus, mitochondria, ribosomes, ER and Golgi, but no cell wall, no chloroplasts and only small temporary vacuoles. They have centrioles, which help in cell division.\n"
      "Cells that do a lot of work have more of certain organelles: muscle cells are packed with mitochondria; gland cells with ribosomes and Golgi bodies.", "animalCell(0)")],
    key_words=[("organelle", "a structure with a particular job inside a cell"), ("mitochondrion", "organelle of aerobic respiration (plural: mitochondria)"),
               ("ribosome", "tiny organelle that makes proteins"), ("partially permeable", "letting some substances through but not others")],
    examples=["Nucleus: control", "Chloroplast: photosynthesis", "Golgi body: packaging and secretion"],
    mistake=("Plant cells do not have mitochondria because they have chloroplasts", "Plant cells have both: they photosynthesise and also respire",
             "All living cells respire, day and night, so plant cells need mitochondria too.")))

# ---------------------------------------------------------------- 3. Practical: observing cells
SRC = ["practicals"]
L.lesson(D, S, 3, ("b3-3", "Practical: observing plant and animal cells under the microscope"), [1, 2],
  "Onion epidermis (plant cells): peel a thin layer from the inside of an onion scale, lay it flat in a drop of water or iodine solution on a slide, lower a cover slip at an angle to avoid air bubbles, observe at low then high power.\n"
  "Cheek cells (animal cells): gently scrape the inside of your cheek with a clean spatula, smear on a slide, add a drop of methylene blue, cover and observe.\n"
  "Stains make parts visible: iodine stains the nucleus and starch; methylene blue stains the nucleus.\n"
  "Biological drawings: pencil, clear single lines, no shading, label lines ruled and not crossing, state the magnification.\n"
  "Total magnification = eyepiece × objective.",
  worked({"e": 10, "o": 40},
         "A student uses a ×{e} eyepiece and a ×{o} objective lens. What is the total magnification?",
         ["Total magnification = eyepiece × objective.", "= {e} × {o} = ×{magnification(e, o)}."], "×{magnification(e, o)}", checks=["magnification(e, o) == 400"]),
  [card("c3b3-1", "Total magnification = eyepiece × objective.",
        ["×{10} eyepiece and ×{10} objective: ×{100}"], "b3-3-mag"),
   card("c3b3-2", "Stains make cell parts easier to see.",
        ["Iodine for onion cells; methylene blue for cheek cells."], "b3-3-stain"),
   card("c3b3-3", "Lower the cover slip at an angle to avoid air bubbles.",
        ["Air bubbles look like black-edged circles."], "b3-3-steps")],
  [num("b3-3-mag", 1, "What is the total magnification with a ×{e} eyepiece and a ×{o} objective?", "magnification(e, o)",
       ["Total = eyepiece × objective = {e} × {o}.", "= ×{answer}."],
       vars={"e": {"pick": [5, 10, 15]}, "o": {"pick": [4, 10, 40, 100]}},
       misc=[("add", "e + o", "Multiply the two magnifications, do not add them.")],
       sources=SRC),
   bank("b3-3-stain", 1, "{X.q}", [
     {"q": "Which stain is used for onion epidermis cells?", "r": "iodine solution", "w": ["methylene blue only", "ink", "salt solution"],
      "e": ["Methylene blue is usually used for cheek cells.", "Ink is not a laboratory stain.", "Salt solution does not stain."], "y": "Iodine stains the nucleus and any starch."},
     {"q": "Why is a stain added to cheek cells?", "r": "To make the nucleus and other parts visible", "w": ["To kill bacteria", "To make the cells larger", "To dissolve the membrane"],
      "e": ["That is not its purpose.", "Stains do not change size.", "The membrane stays."], "y": "Cells are almost transparent without stain."},
     {"q": "Which structure can be seen in onion cells but not in cheek cells?", "r": "a cell wall", "w": ["a nucleus", "cytoplasm", "a cell membrane"],
      "e": ["Both have a nucleus.", "Both have cytoplasm.", "Both have a membrane."], "y": "Plant cells have a cellulose wall."}], SRC),
   order("b3-3-steps", 2, "Put the steps for preparing an onion slide in order.",
         ["Peel a thin layer of epidermis from an onion scale.", "Lay it flat in a drop of iodine solution on a clean slide.",
          "Lower a cover slip at an angle with a mounted needle.", "Observe first under low power, then under high power."],
         hint="Prepare the specimen before covering and viewing it.", sources=SRC, review="authored"),
   bank("b3-3-draw", 2, "{X.q}", [
     {"q": "Which is a rule for biological drawings?", "r": "Use a sharp pencil and clear single lines without shading", "w": ["Use a pen and colour the drawing", "Draw label lines with arrow heads that cross", "Shade the nucleus darkly"],
      "e": ["Pencil, not pen; no colour.", "Label lines are ruled, without arrows, and must not cross.", "No shading."], "y": "Clear, accurate pencil outlines are easiest to read."},
     {"q": "A drawing should also include…", "r": "a title and the magnification", "w": ["the student's favourite colour", "a background picture", "shading to show depth"],
      "e": ["That is not needed.", "Only the specimen is drawn.", "Shading is not used."], "y": "The title and magnification tell the reader what and how big."},
     {"q": "You see black-edged circles on your slide. What are they most likely to be?", "r": "air bubbles", "w": ["nuclei", "chloroplasts", "bacteria"],
      "e": ["Nuclei are inside cells and stain.", "Onion epidermis has no chloroplasts.", "Bacteria are far smaller."], "y": "Lowering the cover slip carelessly traps air."}], SRC),
   num("b3-3-real", 3, "Under ×{m} total magnification, an onion cell appears {img} mm long in your drawing. What is its real length (µm)?", "realSize(img, m) * 1000",
       ["Real = image ÷ magnification = {img} ÷ {m} = {realSize(img, m)} mm.", "= {answer} µm."],
       vars={"m": {"pick": [40, 100]}, "k": {"int": [4, 30]}, "img": {"expr": "k * m / 400"}},
       misc=[("mm", "realSize(img, m)", "That is in mm; × {1000} for µm.")],
       unit="µm", sources=SRC)],
  learn=learn(
    [("Preparing an onion slide",
      "• Peel a thin, almost transparent layer (epidermis) from the inside of an onion scale with forceps.\n• Lay it flat in a drop of iodine solution on a clean slide.\n"
      "• Lower a cover slip at an angle, using a mounted needle, so no air bubbles are trapped.\n• Observe under low power first, then high power.\n"
      "You will see a brick-like pattern of cells, each with a cell wall and a dark nucleus."),
     ("Preparing cheek cells",
      "• Gently scrape the inside of your cheek with a clean spatula (or the flat end of a clean toothpick).\n• Smear the scrapings on a slide, add a drop of methylene blue and cover.\n"
      "• Throw used spatulas into disinfectant.\nThe cells are irregular in shape, with a blue nucleus and no cell wall."),
     ("Microscope and drawings",
      "Total magnification = eyepiece × objective: ×{10} and ×{40} give ×{400}.\n"
      "Draw what you see, not what you expect: sharp pencil, clear single lines, no shading, ruled label lines that do not cross, a title and the magnification.\n"
      "Then you can work out real sizes: real size = drawing size ÷ magnification.")],
    key_words=[("epidermis", "a thin outer layer of cells"), ("stain", "a dye that makes cell parts visible"), ("cover slip", "a thin square of glass placed over the specimen")],
    examples=["×{10} × ×{40} = ×{400}", "Onion: iodine stain, cell wall visible", "Cheek: methylene blue, no cell wall"],
    mistake=("Total magnification = {10} + {40} = {50}", "Total magnification = {10} × {40} = {400}",
             "The two lenses multiply the magnification.")))

# ---------------------------------------------------------------- 4. Water and its importance
SRC = ["water"]
L.lesson(D, S, 4, ("b3-4", "Water and its importance to living organisms"), [1],
  "Water makes up about 60–70% of the human body and up to 90% of some plants and jellyfish.\n"
  "Importance:\n• Solvent: many substances dissolve in it, so reactions can happen in cells.\n• Transport: blood plasma, xylem and phloem carry dissolved substances.\n"
  "• Temperature control: sweating and transpiration cool organisms.\n• Raw material for photosynthesis; product of respiration.\n"
  "• Support: water keeps plant cells turgid; it also forms a habitat for aquatic organisms.\n• Lubrication (tears, joints) and removal of wastes (urine).",
  worked({"m": 50, "p": 65},
         "About {p}% of Ayuk's body mass is water. His mass is {m} kg. What mass of water is in his body?",
         ["Mass of water = {p}% of {m} kg.", "= {p} ÷ {100} × {m} = {p * m / 100} kg."], "{p * m / 100} kg", checks=["p * m / 100 == 32.5"]),
  [card("c3b4-1", "Water is a solvent: reactions in cells happen in solution.",
        ["Sugar and salts dissolve in the cytoplasm."], "b3-4-role"),
   card("c3b4-2", "Water carries substances: in blood plasma and in xylem.",
        ["Glucose travels dissolved in plasma."], "b3-4-transport"),
   card("c3b4-3", "Evaporation of water (sweat) cools the body.",
        ["You sweat on a hot afternoon in Garoua."], "b3-4-pct")],
  [bank("b3-4-role", 1, "{X.q}", [
     {"q": "Why is water called a good solvent?", "r": "Many substances dissolve in it", "w": ["It is colourless", "It boils at 100 °C", "It is found in rivers"],
      "e": ["Colour does not make a solvent.", "Boiling point is a different property.", "Where it is found does not matter."], "y": "Reactions in cells happen in water solutions."},
     {"q": "How does water help plants stay upright?", "r": "It keeps cells firm (turgid)", "w": ["It makes the stem heavier", "It dissolves the cell walls", "It produces oxygen"],
      "e": ["Weight does not support a plant.", "Cell walls do not dissolve.", "Oxygen production is photosynthesis."], "y": "Turgid cells press against each other and support soft parts."},
     {"q": "In which process is water a raw material?", "r": "photosynthesis", "w": ["respiration", "excretion of urea", "digestion of fats only"],
      "e": ["Water is a product of aerobic respiration.", "Urea removal uses water but it is not a raw material.", "Water is used in all digestion (hydrolysis), not fats only."], "y": "Carbon dioxide + water → glucose + oxygen."}], SRC),
   bank("b3-4-transport", 1, "{X.q}", [
     {"q": "Which part of the blood carries dissolved food and wastes?", "r": "plasma (mostly water)", "w": ["red blood cells", "platelets", "white blood cells"],
      "e": ["Red cells carry oxygen.", "Platelets help clotting.", "White cells fight infection."], "y": "Plasma is about 90% water."},
     {"q": "Which plant tissue carries water from the roots to the leaves?", "r": "xylem", "w": ["phloem", "epidermis", "cambium"],
      "e": ["Phloem carries food (sugars).", "Epidermis is a covering layer.", "Cambium makes new cells."], "y": "Xylem vessels carry water and minerals upwards."},
     {"q": "How does sweating cool the body?", "r": "Heat is taken from the skin to evaporate the sweat", "w": ["Sweat is cold", "Sweat blocks the sun", "Sweat contains ice"],
      "e": ["Sweat is at body temperature.", "It does not block sunlight.", "Sweat is liquid."], "y": "Evaporation uses heat energy from the skin."}], SRC),
   num("b3-4-pct", 2, "A person of mass {m} kg is about {p}% water. Find the mass of water in the body (kg).", "p * m / 100",
       ["Mass of water = {p} ÷ {100} × {m}.", "= {answer} kg."],
       vars={"m": {"int": [30, 80]}, "p": {"pick": [60, 65, 70]}},
       misc=[("other", "(100 - p) * m / 100", "That is the mass of everything else. Water is {p}%."), ("noper", "p * m", "Divide by {100}: {p}% means {p} out of {100}.")],
       unit="kg", sources=SRC),
   num("b3-4-dry", 3, "A {f} g piece of pawpaw is dried in an oven until its mass stops changing at {d} g. What percentage of the fresh mass was water?", "roundTo((f - d) / f * 100, 0.1)",
       ["Water lost = {f} − {d} = {f - d} g.", "Percentage = {f - d} ÷ {f} × {100} = {answer}%."],
       vars={"f": {"pick": [50, 80, 100, 120, 200]}, "q": {"int": [5, 15]}, "d": {"expr": "f * q / 100"}},
       misc=[("dry", "roundTo(d / f * 100, 0.1)", "That is the dry matter. Water = fresh mass − dry mass."), ("ofdry", "roundTo((f - d) / d * 100, 0.1)", "Divide by the fresh mass, not the dry mass.")],
       unit="%", sources=SRC)],
  learn=learn(
    [("Life depends on water",
      "Water is the most common substance in living things: about {60}–{70}% of your body, about {90}% of a ripe pawpaw or a leaf of lettuce, even more in a jellyfish.\n"
      "All the chemical reactions of life happen in water solutions inside cells."),
     ("Jobs that water does",
      "• Solvent: salts, sugars and gases dissolve in it.\n• Transport: blood plasma, lymph, xylem and phloem are mostly water.\n"
      "• Reactant: photosynthesis uses water; digestion splits food using water.\n• Cooling: sweating and transpiration take heat away as water evaporates.\n"
      "• Support: water keeps plant cells firm and stems upright.\n• Lubrication and removal of wastes: tears, mucus, joint fluid, urine."),
     ("Measuring water content",
      "Weigh a fresh sample, dry it slowly in an oven until the mass stops changing, and weigh it again.\n"
      "Water lost = fresh mass − dry mass, and percentage of water = water lost ÷ fresh mass × {100}.\n"
      "A {100} g piece of pawpaw that dries to {10} g was {90}% water.")],
    key_words=[("solvent", "a liquid that dissolves other substances"), ("turgid", "swollen and firm because full of water"),
               ("plasma", "the liquid part of the blood")],
    examples=["Water in a {50} kg person at {65}%: {32.5} kg", "Transpiration cools leaves", "Water is a product of respiration"],
    mistake=("Percentage of water = dry mass ÷ fresh mass × {100}", "Percentage of water = (fresh − dry) ÷ fresh × {100}",
             "The water is the mass that was lost on drying.")))

# ---------------------------------------------------------------- 5. The water cycle
SRC = ["water"]
L.lesson(D, S, 5, ("b3-5", "The water cycle"), [4],
  "Water moves continuously between the sea, the air, the land and living things: the water cycle.\n"
  "• Evaporation: the sun heats seas, rivers and lakes; water vapour rises.\n• Transpiration: plants lose water vapour from their leaves; with evaporation from soil it is evapotranspiration.\n"
  "• Condensation: rising vapour cools and forms tiny droplets: clouds.\n• Precipitation: droplets join and fall as rain (or hail).\n"
  "• Infiltration (into the soil), runoff (into streams and rivers) and groundwater flow return water to the sea.\n"
  "Animals take in water by drinking and in food, and return it by breathing out, sweating and excreting.",
  worked({},
         "Describe the path of a drop of water from the Atlantic Ocean at Kribi to a farm near Ebolowa and back.",
         ["The sun heats the sea: water evaporates.", "The vapour rises, cools and condenses into clouds, which the wind carries inland.",
          "Rain falls on the farm; some soaks into the soil and is taken up by plants, then transpired; some runs off into rivers that flow back to the ocean."],
         "Evaporation → condensation → precipitation → infiltration/runoff (and transpiration) → back to the sea"),
  [card("c3b5-1", "Evaporation: liquid water becomes vapour when heated.",
        ["Puddles dry after the rain."], "b3-5-proc"),
   card("c3b5-2", "Condensation: vapour cools and becomes droplets (clouds).",
        ["Mist on Mount Cameroon in the morning"], "b3-5-step"),
   card("c3b5-3", "Plants return water to the air by transpiration.",
        ["Forests make the air humid."], "b3-5-living")],
  [bank("b3-5-proc", 1, "Which process is this? {X.q}", [
     {"q": "Water vapour cools high in the sky and forms clouds.", "r": "condensation", "w": ["evaporation", "transpiration", "infiltration"],
      "e": ["Evaporation turns liquid into vapour.", "Transpiration is water loss from leaves.", "Infiltration is water soaking into soil."], "y": "Vapour → droplets is condensation."},
     {"q": "Water is lost as vapour from the leaves of a cocoa tree.", "r": "transpiration", "w": ["precipitation", "condensation", "runoff"],
      "e": ["Precipitation is rain falling.", "Condensation forms droplets.", "Runoff is water flowing over land."], "y": "Water loss from leaves is transpiration."},
     {"q": "Rain falls on the ground.", "r": "precipitation", "w": ["evaporation", "transpiration", "condensation"],
      "e": ["Evaporation sends water up.", "Transpiration is from leaves.", "Condensation forms clouds."], "y": "Water falling from clouds is precipitation."},
     {"q": "Rain water soaks into the soil.", "r": "infiltration", "w": ["runoff", "evaporation", "condensation"],
      "e": ["Runoff flows over the surface.", "Evaporation sends water into the air.", "Condensation happens in the air."], "y": "Water entering the soil is infiltration."}], SRC),
   order("b3-5-step", 2, "Put these stages of the water cycle in order, starting at the sea.",
         ["Water evaporates from the sea.", "Water vapour rises and cools.", "It condenses into clouds.", "Rain falls on the land.", "Rivers carry the water back to the sea."],
         hint="Evaporation starts it; rivers finish it.", sources=SRC, review="authored"),
   bank("b3-5-living", 2, "{X.q}", [
     {"q": "How do animals return water to the water cycle?", "r": "By breathing out, sweating and excreting urine", "w": ["Only by drinking", "By photosynthesis", "They do not return water"],
      "e": ["Drinking takes water in.", "Animals do not photosynthesise.", "They lose water in several ways."], "y": "Water leaves animals as vapour and liquid."},
     {"q": "Why does cutting down large forests reduce rainfall in an area?", "r": "Less transpiration puts less water vapour into the air", "w": ["Trees make clouds directly", "Forests cool the sea", "Trees store all the rain"],
      "e": ["Trees release vapour; clouds form by condensation.", "Forests do not cool the sea.", "Most water passes through trees, not stays."], "y": "Transpiration is a big source of vapour over land."},
     {"q": "What energy source drives the water cycle?", "r": "the sun", "w": ["the wind only", "the moon", "volcanoes"],
      "e": ["Wind moves clouds but the sun causes evaporation.", "The moon causes tides, not evaporation.", "Volcanoes are not the main driver."], "y": "Solar heat evaporates water."}], SRC),
   bank("b3-5-why", 3, "{X.q}", [
     {"q": "Why is the water cycle important to living things?", "r": "It returns fresh water to the land again and again", "w": ["It makes the sea salty", "It removes all water from the land", "It stops plants transpiring"],
      "e": ["Salt is not the purpose.", "It brings water back.", "Transpiration is part of the cycle."], "y": "Evaporation leaves salt behind, so rain is fresh water."},
     {"q": "Why is rain water fresh even though much of it comes from the sea?", "r": "Salt does not evaporate; only water does", "w": ["Clouds filter the salt", "The wind removes salt", "Sea water is fresh"],
      "e": ["There is no filter.", "Salt stays in the sea.", "Sea water is salty."], "y": "Evaporation leaves dissolved salts behind."},
     {"q": "Paving large areas of a town with concrete increases flooding. Why?", "r": "Less water infiltrates, so more runs off", "w": ["Concrete makes more rain", "Concrete increases transpiration", "Concrete evaporates water"],
      "e": ["Concrete does not change rainfall.", "Concrete has no leaves.", "It mainly stops infiltration."], "y": "Water that cannot soak in flows over the surface."}], SRC)],
  learn=learn(
    [("Water on the move",
      "The same water has been used again and again for millions of years. It moves round and round between the sea, the air and the land: the water cycle.\n"
      "The sun provides the energy: it heats seas, lakes and rivers, and water evaporates."),
     ("The main stages",
      "• Evaporation: liquid water becomes vapour.\n• Transpiration: plants release water vapour from their leaves.\n• Condensation: vapour rises, cools and forms droplets: clouds and mist.\n"
      "• Precipitation: droplets join and fall as rain.\n• Infiltration and runoff: rain soaks into the soil or flows into streams, rivers and back to the sea.\n"
      "Salt does not evaporate, so rain is fresh water."),
     ("Living things in the cycle",
      "Plants take water from the soil and transpire it; animals drink and eat water and return it by breathing out, sweating and excreting.\n"
      "Forests put a lot of water vapour into the air, so cutting them down can reduce local rainfall. Concrete and bare soil reduce infiltration and increase floods.")],
    key_words=[("evaporation", "liquid water becoming vapour"), ("condensation", "vapour cooling into droplets"),
               ("precipitation", "rain, hail or snow falling"), ("transpiration", "loss of water vapour from leaves")],
    examples=["Morning mist: condensation", "Drying clothes: evaporation", "Flooded streets after a storm: runoff"],
    mistake=("Clouds are made of water vapour", "Clouds are made of tiny droplets of liquid water",
             "Water vapour is invisible; clouds form when it condenses.")))
