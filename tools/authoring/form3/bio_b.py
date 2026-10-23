"""Form 3 Biology, Term 1, rows 13-21 (viruses, bacteria, protoctists, fungi, plants, bony fish). Run: python tools/authoring/form3/bio_b.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "biology", "biology"
SRC = ["classification"]

# ---------------------------------------------------------------- 13. Viruses
L.lesson(D, S, 13, ("b3-13", "Viruses: characteristics, the T2 virus and how viruses replicate"), [9],
  "Viruses are extremely small particles (20–300 nm), seen only with an electron microscope. They are not cells.\n"
  "• They have a protein coat (capsid) around genetic material (DNA or RNA); no cytoplasm, no organelles, no respiration or nutrition of their own.\n"
  "• They can reproduce only inside a living host cell (they are obligate parasites); outside a host some can be crystallised.\n"
  "T2 bacteriophage (infects bacteria): head (protein capsid with DNA), tail (hollow sheath), tail fibres and base plate.\n"
  "Replication: attach to host → inject DNA → host makes new virus DNA and protein coats → new viruses assemble → host cell bursts, releasing them.\n"
  "Diseases: HIV/AIDS, measles, polio, influenza, COVID-19, yellow fever. Antibiotics do not work against viruses; vaccines prevent many viral diseases.",
  worked({},
         "Give two reasons why many biologists say viruses are not living organisms.",
         ["They are not made of cells: just genetic material inside a protein coat.", "They cannot feed, respire or reproduce on their own; they reproduce only inside living host cells."],
         "Not cells; cannot carry out life processes outside a host"),
  [card("c3b13-1", "A virus is genetic material in a protein coat; it is not a cell.",
        ["No cytoplasm, no nucleus, no ribosomes"], "b3-13-char"),
   card("c3b13-2", "Viruses reproduce only inside living host cells.",
        ["HIV reproduces inside white blood cells."], "b3-13-rep"),
   card("c3b13-3", "Antibiotics do not kill viruses; vaccines help prevent viral diseases.",
        ["The measles vaccine protects children."], "b3-13-disease")],
  [bank("b3-13-char", 1, "{X.q}", [
     {"q": "What is a virus made of?", "r": "genetic material (DNA or RNA) inside a protein coat", "w": ["a cell with a nucleus", "cytoplasm and a cell wall", "a single bacterium"],
      "e": ["Viruses are not cells.", "They have no cytoplasm or wall.", "A bacterium is a cell; a virus is not."], "y": "Just a capsid around nucleic acid."},
     {"q": "Which is true of viruses?", "r": "They can reproduce only inside a living host cell", "w": ["They can be seen with a school light microscope", "They respire like bacteria", "They are killed by antibiotics"],
      "e": ["They are far too small; an electron microscope is needed.", "They do not respire.", "Antibiotics act on bacteria, not viruses."], "y": "They are obligate parasites."},
     {"q": "How big are viruses compared with bacteria?", "r": "much smaller", "w": ["much larger", "the same size", "larger than human cells"],
      "e": ["Bacteria are about 1–10 µm; viruses about 0.02–0.3 µm.", "They are far smaller.", "Human cells are far larger."], "y": "Viruses are measured in nanometres."}], SRC),
   order("b3-13-rep", 2, "Put the stages of replication of a T2 virus in order.",
         ["The virus attaches to the bacterium with its tail fibres.", "It injects its DNA into the bacterium.", "The bacterium makes new virus DNA and protein coats.",
          "New viruses are assembled inside the cell.", "The bacterium bursts and releases the new viruses."], hint="Attach, inject, copy, assemble, burst.", sources=SRC, review="authored"),
   bank("b3-13-part", 1, "{X.q}", [
     {"q": "Which part of a T2 virus contains its DNA?", "r": "the head (capsid)", "w": ["the tail fibres", "the base plate", "the tail sheath only"],
      "e": ["Tail fibres attach to the host.", "The base plate anchors the virus.", "The tail injects the DNA but does not store it."], "y": "The DNA is packed in the head."},
     {"q": "What is the job of the tail fibres of a T2 virus?", "r": "to attach the virus to the host bacterium", "w": ["to store DNA", "to make proteins", "to digest the host"],
      "e": ["DNA is in the head.", "The virus cannot make proteins itself.", "Viruses do not digest."], "y": "They grip special sites on the bacterium."},
     {"q": "What does a T2 bacteriophage infect?", "r": "bacteria", "w": ["humans", "plants", "fungi"],
      "e": ["It infects bacteria only.", "It infects bacteria only.", "It infects bacteria only."], "y": "'Bacteriophage' means 'bacteria eater'."}], SRC),
   bank("b3-13-disease", 3, "{X.q}", [
     {"q": "Which disease is caused by a virus?", "r": "measles", "w": ["cholera", "malaria", "tuberculosis"],
      "e": ["Cholera is caused by a bacterium.", "Malaria is caused by a protoctist (Plasmodium).", "TB is caused by a bacterium."], "y": "Measles, HIV, polio and influenza are viral."},
     {"q": "Why are antibiotics not given to cure a common cold?", "r": "Colds are caused by viruses, and antibiotics do not affect viruses", "w": ["Colds are caused by bacteria", "Antibiotics are too expensive", "Colds are not diseases"],
      "e": ["Colds are viral.", "Cost is not the reason.", "A cold is an infection."], "y": "Antibiotics act on bacterial structures that viruses lack."},
     {"q": "How can the spread of HIV be reduced?", "r": "Avoiding contact with infected blood and practising safe sex", "w": ["Taking antibiotics", "Sleeping under a net", "Drinking boiled water only"],
      "e": ["Antibiotics do not kill HIV.", "Nets stop mosquitoes; HIV is not carried by mosquitoes.", "HIV is not spread by water."], "y": "HIV spreads through blood and sexual fluids."}], SRC)],
  learn=learn(
    [("Particles on the edge of life",
      "Viruses are far smaller than bacteria and can be seen only with an electron microscope. A virus is not a cell: it is a protein coat (capsid) wrapped round a little genetic material, DNA or RNA.\n"
      "It has no cytoplasm, no ribosomes, does not feed or respire, and cannot reproduce on its own. Outside a living cell it is inactive; some viruses can even be crystallised like salt."),
     ("The {'T2'} bacteriophage",
      "{'T2'} infects bacteria. It has a head (a protein capsid holding DNA), a hollow tail, a base plate and tail fibres.\n"
      "• It attaches to a bacterium with its tail fibres.\n• It injects its DNA through the tail.\n• The bacterium's machinery is taken over and makes new virus DNA and coats.\n"
      "• New viruses assemble, the bacterium bursts, and they are released to infect more cells."),
     ("Viruses and health",
      "Viruses cause HIV/AIDS, measles, polio, influenza, yellow fever and {'COVID-19'}. They also attack crops (cassava mosaic) and livestock.\n"
      "Antibiotics do not work on viruses. Vaccines (measles, polio, yellow fever) help the body resist them, and hygiene and safe behaviour stop their spread.")],
    key_words=[("virus", "a particle of genetic material in a protein coat that reproduces only inside host cells"), ("capsid", "the protein coat of a virus"),
               ("host", "the living organism a parasite lives in"), ("bacteriophage", "a virus that infects bacteria")],
    examples=["HIV: infects white blood cells", "Measles: prevented by vaccine", "{'T2'}: infects bacteria"],
    mistake=("Antibiotics cure viral infections", "Antibiotics act on bacteria, not viruses",
             "Viruses have none of the structures antibiotics attack.")))

# ---------------------------------------------------------------- 14. Bacteria
L.lesson(D, S, 14, ("b3-14", "Prokaryotae: bacteria"), [13],
  "Bacteria are single-celled prokaryotes (no true nucleus), about 1–10 µm long.\n"
  "Structure: cell wall, cell membrane, cytoplasm, circular DNA (nucleoid), plasmids, ribosomes; some have a slime capsule and flagella.\n"
  "Shapes: cocci (spheres), bacilli (rods), spirilla (spirals), vibrios (commas).\n"
  "Reproduction: binary fission (one cell splits into two); in good conditions every 20–30 minutes, so numbers double quickly. Some form resistant spores.\n"
  "Importance: decomposers (recycling nutrients), nitrogen fixation in legume roots, making yoghurt and cheese, sewage treatment; but some cause disease (cholera, typhoid, tuberculosis, tetanus) and spoil food.",
  worked({"n0": 10, "g": 20, "t": 120},
         "A bacterium divides every {g} minutes. Starting with {n0} bacteria, how many will there be after {t} minutes?",
         ["Number of divisions = {t} ÷ {g} = {t / g}.", "Each division doubles the number: {n0} × {2}{sup(t / g)} = {n0} × {2 ^ (t / g)} = {n0 * 2 ^ (t / g)}."],
         "{n0 * 2 ^ (t / g)} bacteria", checks=["n0 * 2 ^ (t / g) == 640"]),
  [card("c3b14-1", "Bacteria are prokaryotes: no true nucleus, DNA free in the cytoplasm.",
        ["They also have a cell wall and ribosomes."], "b3-14-struct"),
   card("c3b14-2", "Shapes: cocci (round), bacilli (rods), spirilla (spirals).",
        ["Cholera bacteria are comma-shaped (vibrios)."], "b3-14-shape"),
   card("c3b14-3", "Binary fission doubles the number at each generation.",
        ["{3} generations: × {8}"], "b3-14-grow")],
  [bank("b3-14-struct", 1, "{X.q}", [
     {"q": "Which structure does a bacterium NOT have?", "r": "a true nucleus", "w": ["a cell wall", "ribosomes", "a cell membrane"],
      "e": ["Bacteria have a cell wall.", "They have (small) ribosomes.", "They have a cell membrane."], "y": "Their DNA lies free in the cytoplasm."},
     {"q": "What is the function of a bacterium's flagellum?", "r": "movement", "w": ["photosynthesis", "storing DNA", "making proteins"],
      "e": ["Most bacteria do not photosynthesise.", "DNA is in the cytoplasm.", "Ribosomes make proteins."], "y": "The whip-like flagellum spins to move the cell."},
     {"q": "What are plasmids?", "r": "small extra rings of DNA in bacteria", "w": ["food stores", "cell walls", "flagella"],
      "e": ["They are genetic material.", "The wall surrounds the cell.", "Flagella are for movement."], "y": "Plasmids often carry genes such as antibiotic resistance."}], SRC),
   bank("b3-14-shape", 1, "{X.q}", [
     {"q": "Rod-shaped bacteria are called…", "r": "bacilli", "w": ["cocci", "spirilla", "vibrios"],
      "e": ["Cocci are spheres.", "Spirilla are spirals.", "Vibrios are comma-shaped."], "y": "Bacillus means little rod."},
     {"q": "Spherical bacteria are called…", "r": "cocci", "w": ["bacilli", "spirilla", "vibrios"],
      "e": ["Bacilli are rods.", "Spirilla are spirals.", "Vibrios are commas."], "y": "Coccus means berry."},
     {"q": "The cholera bacterium is comma-shaped. It is a…", "r": "vibrio", "w": ["coccus", "bacillus", "spirillum"],
      "e": ["Cocci are round.", "Bacilli are straight rods.", "Spirilla are spirals."], "y": "Vibrio cholerae is comma-shaped."}], SRC),
   num("b3-14-grow", 2, "A bacterium divides every {g} minutes. Starting with {n0} bacteria, how many will there be after {t} minutes?", "n0 * 2 ^ (t / g)",
       ["Divisions = {t} ÷ {g} = {t / g}.", "Number = {n0} × {2}{sup(t / g)} = {answer}."],
       vars={"n0": {"pick": [1, 2, 5, 10]}, "g": {"pick": [20, 30]}, "k": {"int": [2, 8]}, "t": {"expr": "g * k"}},
       misc=[("add", "n0 + 2 * (t / g)", "Each division doubles the number; do not add {2} each time."), ("mult", "n0 * 2 * (t / g)", "Doubling repeatedly means a power of {2}, not × {2} × the number of divisions.")],
       sources=SRC, where=["n0 * 2 ^ (t / g) <= 10000"]),
   bank("b3-14-use", 2, "{X.q}", [
     {"q": "How do bacteria in the root nodules of beans help farmers?", "r": "They fix nitrogen from the air into compounds the plant can use", "w": ["They kill pests", "They make the roots hard", "They produce sugar from sunlight"],
      "e": ["They do not kill pests.", "That is not their role.", "They do not photosynthesise."], "y": "Nitrogen fixation enriches the soil."},
     {"q": "Which is a useful activity of bacteria?", "r": "turning milk into yoghurt", "w": ["causing cholera", "spoiling food", "causing tetanus"],
      "e": ["That is harmful.", "That is harmful.", "That is harmful."], "y": "Lactobacillus turns milk sugar into lactic acid."},
     {"q": "Why are bacteria important in nature as decomposers?", "r": "They break down dead matter and return nutrients to the soil", "w": ["They make dead matter last forever", "They photosynthesise", "They produce oxygen for animals"],
      "e": ["They break it down.", "Decomposers do not photosynthesise.", "Decomposition uses oxygen."], "y": "Recycling keeps soils fertile."}], SRC),
   bank("b3-14-harm", 3, "{X.q}", [
     {"q": "Cholera spreads through dirty drinking water. Which measure best prevents it?", "r": "Boiling or treating drinking water and using clean latrines", "w": ["Sleeping under a mosquito net", "Taking a vaccine against measles", "Eating more sugar"],
      "e": ["Nets stop mosquitoes, not cholera.", "The measles vaccine does not protect against cholera.", "Diet does not stop the bacteria."], "y": "Cholera bacteria come from faeces in water."},
     {"q": "Why is tetanus a risk after a cut with a rusty nail in the soil?", "r": "Tetanus bacteria (spores) in soil can enter the wound", "w": ["Rust is a virus", "Iron causes tetanus", "The nail is too sharp"],
      "e": ["Rust is iron oxide.", "Iron is not the cause.", "Sharpness is not the cause."], "y": "Clean the wound and keep tetanus vaccination up to date."},
     {"q": "Bacteria divide every 20 minutes. Why does food left out on a hot day spoil quickly?", "r": "Warmth lets bacteria divide fast, so their numbers grow very rapidly", "w": ["Heat makes food grow", "Bacteria die in heat", "Food turns into bacteria"],
      "e": ["Food does not grow.", "Moderate warmth speeds them up.", "Bacteria come from outside."], "y": "Doubling every 20 minutes gives millions in hours."}], SRC)],
  learn=learn(
    [("Simple but successful",
      "Bacteria are tiny single cells, about {1}–{10} µm long. They are prokaryotes: their DNA is a loop lying free in the cytoplasm, not inside a nucleus.\n"
      "A typical bacterium has a cell wall, cell membrane, cytoplasm with ribosomes, a DNA loop and often small rings of DNA called plasmids. Some have a slimy capsule and whip-like flagella for movement."),
     ("Shapes and growth",
      "Bacteria are named by shape: cocci (spheres), bacilli (rods), spirilla (spirals) and vibrios (commas).\n"
      "They reproduce by binary fission: one cell splits into two. In warm, moist conditions with food this can happen every {20}–{30} minutes, so one bacterium can become {64} in two hours ({6} doublings).\n"
      "Some form tough spores that survive heat and drought."),
     ("Friends and enemies",
      "Useful: decomposers recycle nutrients; nitrogen-fixing bacteria in bean and groundnut nodules enrich soil; bacteria make yoghurt and cheese and clean sewage.\n"
      "Harmful: cholera, typhoid, tuberculosis and tetanus are bacterial diseases; bacteria also spoil food. Antibiotics can kill bacteria, but must be used properly to avoid resistance.")],
    key_words=[("binary fission", "splitting of one cell into two"), ("plasmid", "a small ring of extra DNA in a bacterium"),
               ("decomposer", "an organism that breaks down dead matter"), ("nitrogen fixation", "turning nitrogen gas into compounds plants can use")],
    examples=["Bacilli: tuberculosis", "Vibrio: cholera", "{1} bacterium, {5} doublings: {32}"],
    mistake=("All bacteria cause disease", "Most bacteria are harmless or useful",
             "Only some bacteria are pathogens; many recycle nutrients or make food.")))

# ---------------------------------------------------------------- 15. Protoctista and Amoeba
L.lesson(D, S, 15, ("b3-15", "Kingdom Protoctista; Amoeba: structure and mode of life"), [9],
  "Protoctista are mostly single-celled eukaryotes (they have a nucleus). Some are animal-like (Amoeba, Plasmodium), some plant-like with chloroplasts (Spirogyra, Chlamydomonas).\n"
  "Amoeba lives in fresh water and mud. Structure: cell membrane, granular cytoplasm, nucleus, food vacuoles, contractile vacuole, pseudopodia ('false feet').\n"
  "Mode of life:\n• Movement: by pushing out pseudopodia.\n• Feeding: surrounds food with pseudopodia (phagocytosis), forming a food vacuole where it is digested.\n"
  "• Gas exchange and excretion: by diffusion through the membrane.\n• Osmoregulation: the contractile vacuole collects excess water and pumps it out.\n• Reproduction: binary fission.",
  worked({},
         "Explain why an amoeba in fresh water needs a contractile vacuole.",
         ["Pond water is more dilute than the amoeba's cytoplasm.", "Water keeps entering the amoeba by osmosis.", "The contractile vacuole collects the extra water and expels it, so the amoeba does not burst."],
         "To remove water that enters by osmosis, so it does not burst"),
  [card("c3b15-1", "Protoctists are mostly single-celled organisms with a nucleus.",
        ["Amoeba, Spirogyra, Plasmodium"], "b3-15-king"),
   card("c3b15-2", "Amoeba moves and feeds using pseudopodia.",
        ["Food is enclosed in a food vacuole and digested."], "b3-15-part"),
   card("c3b15-3", "The contractile vacuole removes excess water.",
        ["It fills and empties every few seconds."], "b3-15-life")],
  [bank("b3-15-king", 1, "{X.q}", [
     {"q": "Which feature do all protoctists have?", "r": "cells with a true nucleus", "w": ["chloroplasts", "many cells", "a cell wall of chitin"],
      "e": ["Only plant-like protoctists have chloroplasts.", "Most are single-celled.", "Chitin walls are typical of fungi."], "y": "Protoctists are eukaryotes."},
     {"q": "Which organism is a protoctist?", "r": "Amoeba", "w": ["a mushroom", "a bacterium", "a mosquito"],
      "e": ["Mushrooms are fungi.", "Bacteria are prokaryotes.", "Mosquitoes are animals."], "y": "Amoeba is a single eukaryotic cell."},
     {"q": "Spirogyra is placed in Protoctista, not Plantae. Why?", "r": "It is a simple filament of similar cells, not a plant with organs", "w": ["It has no chloroplasts", "It has no nucleus", "It is an animal"],
      "e": ["Spirogyra has spiral chloroplasts.", "It has a nucleus.", "It photosynthesises."], "y": "Simple eukaryotes are protoctists."}], SRC),
   bank("b3-15-part", 1, "What is the function of this part of an amoeba? {X.q}", [
     {"q": "Pseudopodium", "r": "movement and capturing food", "w": ["removing excess water", "controlling the cell", "digesting food"],
      "e": ["That is the contractile vacuole.", "That is the nucleus.", "That happens in the food vacuole."], "y": "'False foot': cytoplasm flows into it."},
     {"q": "Contractile vacuole", "r": "removing excess water", "w": ["digesting food", "movement", "reproduction"],
      "e": ["That is the food vacuole.", "That is the pseudopodia.", "Reproduction is binary fission controlled by the nucleus."], "y": "It pumps out water that enters by osmosis."},
     {"q": "Food vacuole", "r": "digesting food", "w": ["removing water", "movement", "gas exchange"],
      "e": ["That is the contractile vacuole.", "That is the pseudopodia.", "Gases diffuse through the membrane."], "y": "Enzymes digest the captured food inside it."},
     {"q": "Nucleus", "r": "controlling the cell's activities and division", "w": ["movement", "digesting food", "removing water"],
      "e": ["That is the pseudopodia.", "That is the food vacuole.", "That is the contractile vacuole."], "y": "The nucleus holds the DNA."}], SRC),
   order("b3-15-feed", 2, "Put the steps of feeding in Amoeba in order.",
         ["Amoeba senses a food particle.", "Pseudopodia flow round the particle.", "The food is enclosed in a food vacuole.",
          "Enzymes digest the food.", "Digested food diffuses into the cytoplasm; waste is left behind."], hint="Surround, enclose, digest, absorb.", sources=SRC, review="authored"),
   bank("b3-15-life", 3, "{X.q}", [
     {"q": "How does an amoeba obtain oxygen?", "r": "By diffusion through its cell membrane", "w": ["Through lungs", "Through gills", "Through the contractile vacuole"],
      "e": ["It is a single cell.", "It is a single cell.", "That removes water."], "y": "Its large surface area to volume ratio makes diffusion enough."},
     {"q": "An amoeba is moved into sea water (more concentrated than its cytoplasm). What happens to its contractile vacuole?", "r": "It works less often, because less water enters", "w": ["It works faster", "It bursts", "It turns into a food vacuole"],
      "e": ["Less water enters in a concentrated solution.", "Vacuoles do not burst from this.", "They have different jobs."], "y": "Osmosis brings in less water."},
     {"q": "How does an amoeba reproduce?", "r": "By binary fission: the nucleus divides, then the cytoplasm", "w": ["By laying eggs", "By spores only", "By budding from a flower"],
      "e": ["Amoeba does not lay eggs.", "It mainly uses binary fission.", "It has no flowers."], "y": "One cell becomes two identical cells."}], SRC)],
  learn=learn(
    [("A kingdom of simple eukaryotes",
      "Protoctista is a mixed kingdom of mostly single-celled organisms that have a nucleus. Some behave like tiny animals (Amoeba, Paramecium, Plasmodium), others like tiny plants with chloroplasts (Chlamydomonas, Spirogyra).\n"
      "They live in water, damp soil or inside other organisms."),
     ("Amoeba: one cell doing everything",
      "Amoeba lives in ponds and mud. It is a single cell with a flexible membrane, granular cytoplasm and a nucleus.\n"
      "• It moves by pushing out pseudopodia ('false feet') and flowing into them.\n• It feeds by surrounding food with pseudopodia, trapping it in a food vacuole, digesting it with enzymes and absorbing the products.\n"
      "• Oxygen and carbon dioxide diffuse through the membrane."),
     ("Keeping water balance",
      "Fresh water is more dilute than the amoeba's cytoplasm, so water constantly enters by osmosis. A contractile vacuole collects the extra water and squeezes it out, so the amoeba does not swell and burst.\n"
      "When conditions are good, the amoeba reproduces by binary fission: the nucleus divides, then the cytoplasm.")],
    key_words=[("pseudopodium", "a temporary 'false foot' of cytoplasm"), ("food vacuole", "a vacuole where captured food is digested"),
               ("contractile vacuole", "a vacuole that collects and expels excess water"), ("phagocytosis", "engulfing food particles")],
    examples=["Amoeba: animal-like protoctist", "Chlamydomonas: plant-like protoctist", "Contractile vacuole: osmoregulation"],
    mistake=("The contractile vacuole digests food", "The contractile vacuole removes excess water; food is digested in food vacuoles",
             "Each vacuole has its own job.")))

# ---------------------------------------------------------------- 16. Spirogyra and Plasmodium
L.lesson(D, S, 16, ("b3-16", "Spirogyra; Plasmodium and the control of malaria"), [15],
  "Spirogyra: a green alga of ponds and slow streams. Unbranched filaments of cylindrical cells, each with a cellulose wall, a large vacuole, a central nucleus and one or more spiral (ribbon-shaped) chloroplasts with pyrenoids (starch stores). It photosynthesises, and reproduces by fragmentation and by conjugation.\n"
  "Plasmodium: the protoctist that causes malaria. It lives in two hosts: the female Anopheles mosquito and humans.\n"
  "Simplified cycle: an infected mosquito bites and injects sporozoites → they multiply in the liver → they invade red blood cells, multiply and burst them (fever every 48–72 hours) → some form gametocytes → a mosquito biting the person takes them up and the cycle continues in the mosquito.\n"
  "Control: sleep under insecticide-treated nets; drain stagnant water and clear bushes; spray insecticides; take antimalarial drugs; quick testing and treatment.",
  worked({},
         "Explain how sleeping under an insecticide-treated net reduces malaria.",
         ["Female Anopheles mosquitoes bite mostly at night.", "The net stops them biting, so Plasmodium is not injected.", "The insecticide also kills mosquitoes that land on it, reducing their numbers."],
         "It stops infected mosquitoes biting, and kills them"),
  [card("c3b16-1", "Spirogyra: green filaments with spiral chloroplasts.",
        ["Common in still ponds"], "b3-16-spiro"),
   card("c3b16-2", "Plasmodium is carried by the female Anopheles mosquito.",
        ["Only the female sucks blood."], "b3-16-cycle"),
   card("c3b16-3", "Control malaria by breaking the cycle: nets, draining water, drugs.",
        ["No stagnant water, fewer mosquito larvae."], "b3-16-control")],
  [bank("b3-16-spiro", 1, "{X.q}", [
     {"q": "What shape are the chloroplasts of Spirogyra?", "r": "spiral ribbons", "w": ["small round discs", "star shapes", "it has none"],
      "e": ["That describes most plant cells.", "Star-shaped chloroplasts belong to other algae.", "Spirogyra photosynthesises, so it has chloroplasts."], "y": "Its name comes from the spiral chloroplasts."},
     {"q": "What are pyrenoids in Spirogyra?", "r": "starch stores on the chloroplasts", "w": ["the nucleus", "the cell wall", "pores in the membrane"],
      "e": ["The nucleus is in the centre of the cell.", "The wall is outside.", "They are not pores."], "y": "Starch from photosynthesis is stored round them."},
     {"q": "How does Spirogyra feed?", "r": "by photosynthesis", "w": ["by engulfing food", "by absorbing digested food from a host", "by sucking blood"],
      "e": ["That is Amoeba.", "That is a parasite like Plasmodium.", "That is a mosquito."], "y": "It has chloroplasts and makes its own food."}], SRC),
   order("b3-16-cycle", 2, "Put the stages of the life cycle of Plasmodium in order, starting with the bite.",
         ["An infected female Anopheles mosquito bites a person and injects sporozoites.", "The parasites multiply in the liver.",
          "They invade red blood cells, multiply and burst them, causing fever.", "Some form gametocytes in the blood.", "A mosquito biting the person takes up the gametocytes."],
         hint="Bite, liver, blood, gametocytes, mosquito.", sources=SRC, review="authored"),
   bank("b3-16-control", 1, "{X.q}", [
     {"q": "Which measure kills the larvae of mosquitoes?", "r": "draining or covering stagnant water", "w": ["sleeping under a net", "taking antimalarial drugs", "wearing light clothes"],
      "e": ["Nets protect people from adults.", "Drugs treat people.", "Clothes protect from bites only."], "y": "Larvae develop in still water."},
     {"q": "Which organism causes malaria?", "r": "Plasmodium (a protoctist)", "w": ["the Anopheles mosquito itself", "a virus", "a bacterium"],
      "e": ["The mosquito carries the parasite (it is the vector).", "Malaria is not viral.", "Malaria is not bacterial."], "y": "The mosquito is the vector; Plasmodium is the cause."},
     {"q": "Why does a malaria patient have fever every two or three days?", "r": "Parasites burst out of red blood cells at regular intervals", "w": ["The mosquito bites every two days", "The liver stops working", "The patient drinks dirty water"],
      "e": ["The fever comes from inside the body.", "Liver stage causes no fever.", "Water does not spread malaria."], "y": "Each burst releases parasites and toxins."}], SRC),
   bank("b3-16-why", 3, "{X.q}", [
     {"q": "Why is the female Anopheles called the vector of malaria?", "r": "It carries Plasmodium from one person to another", "w": ["It causes the disease itself", "It cures malaria", "It lives in red blood cells"],
      "e": ["Plasmodium causes the disease.", "It spreads the disease.", "Plasmodium lives in red blood cells."], "y": "A vector transmits a pathogen without being the pathogen."},
     {"q": "Clearing bushes around houses helps reduce malaria. Why?", "r": "Adult mosquitoes rest in bushes during the day", "w": ["Bushes produce Plasmodium", "Bushes make the air hot", "It removes the liver stage"],
      "e": ["Plasmodium needs a host, not bushes.", "Temperature is not the main reason.", "The liver stage is in people."], "y": "Fewer resting places, fewer mosquitoes."},
     {"q": "A person living in Douala has fever, chills and headache every two days. What should be done first?", "r": "Go to a health centre for a malaria test and correct treatment", "w": ["Take any antibiotic at home", "Wait for it to pass", "Drink salty water"],
      "e": ["Antibiotics do not cure malaria.", "Untreated malaria can kill.", "Salt water does not treat malaria."], "y": "Quick testing and proper antimalarials save lives."}], SRC)],
  learn=learn(
    [("Spirogyra: a green filament",
      "Spirogyra forms slimy green threads in ponds and slow streams. Each thread is a row of cylindrical cells joined end to end.\n"
      "Each cell has a cellulose wall, a large vacuole, a nucleus held in the centre, and one or more ribbon-shaped chloroplasts coiled in a spiral, with pyrenoids that store starch.\n"
      "It makes its own food by photosynthesis and reproduces by breaking into pieces (fragmentation) and by conjugation between two filaments."),
     ("Plasmodium: the malaria parasite",
      "Malaria is caused by Plasmodium, a protoctist, and carried by female Anopheles mosquitoes (the vector).\n"
      "• An infected mosquito bites and injects sporozoites.\n• They multiply in the liver.\n• They enter red blood cells, multiply and burst them: every {48} to {72} hours the patient has fever, chills and sweating.\n"
      "• Some parasites become gametocytes; a mosquito drinking the blood takes them up, and they develop inside it."),
     ("Breaking the cycle",
      "Malaria can be controlled at every stage:\n• sleep under insecticide-treated nets; use repellents and window screens;\n• drain, cover or treat stagnant water and clear bushes near homes;\n"
      "• spray insecticides indoors;\n• get tested quickly and take the full course of antimalarial drugs; pregnant women and young children may get preventive treatment.")],
    key_words=[("filament", "a thread of cells joined end to end"), ("pyrenoid", "a starch-storing body on a chloroplast"),
               ("vector", "an organism that carries a pathogen between hosts"), ("sporozoite", "the stage of Plasmodium injected by the mosquito")],
    examples=["Spirogyra: spiral chloroplasts", "Plasmodium: two hosts, human and mosquito", "Treated nets: protect while sleeping"],
    mistake=("The mosquito causes malaria", "Plasmodium causes malaria; the mosquito carries it",
             "The mosquito is the vector, not the pathogen.")))

# ---------------------------------------------------------------- 17. Fungi: general characteristics, mould
L.lesson(D, S, 17, ("b3-17", "Kingdom Fungi: characteristics; mould: structure and mode of life"), [9],
  "Fungi are eukaryotes with no chlorophyll, so they cannot photosynthesise. Most are made of thread-like hyphae forming a network (mycelium); yeast is single-celled. Their cell walls contain chitin.\n"
  "Nutrition: saprophytic (feeding on dead matter by releasing enzymes and absorbing the products) or parasitic.\n"
  "Reproduction: mainly by spores, carried by air or water.\n"
  "Bread mould (Mucor / Rhizopus): white hyphae spreading over damp bread; vertical hyphae carry black sporangia full of spores; rhizoids anchor it. It grows best where it is warm, damp and dark, with food.",
  worked({},
         "Explain how bread mould feeds.",
         ["The hyphae grow over and into the bread.", "They release digestive enzymes that break down starch into sugars outside the mould.", "The hyphae absorb the dissolved products."],
         "Saprophytic: external digestion by enzymes, then absorption"),
  [card("c3b17-1", "Fungi have no chlorophyll and feed by absorbing food.",
        ["Mushrooms do not need light."], "b3-17-char"),
   card("c3b17-2", "Most fungi are made of hyphae forming a mycelium.",
        ["White threads of mould on old bread"], "b3-17-part"),
   card("c3b17-3", "Fungi reproduce by spores.",
        ["The black dots on mould are sporangia full of spores."], "b3-17-cond")],
  [bank("b3-17-char", 1, "{X.q}", [
     {"q": "Why can fungi not make their own food?", "r": "They have no chlorophyll", "w": ["They have no cells", "They live in the dark", "They have no nucleus"],
      "e": ["They are made of cells.", "Some grow in light; the reason is chlorophyll.", "They have nuclei."], "y": "Without chlorophyll there is no photosynthesis."},
     {"q": "What are fungal cell walls made of?", "r": "chitin", "w": ["cellulose", "protein only", "no wall at all"],
      "e": ["Cellulose is in plant walls.", "Chitin is a carbohydrate.", "Fungi do have walls."], "y": "Chitin is also found in insect skeletons."},
     {"q": "What is saprophytic nutrition?", "r": "Feeding on dead organic matter by digesting it outside the body and absorbing the products", "w": ["Making food by photosynthesis", "Swallowing food whole", "Living inside a living host"],
      "e": ["That is plant nutrition.", "Fungi do not swallow.", "That is parasitism."], "y": "Saprophytes are decomposers."}], SRC),
   bank("b3-17-part", 1, "{X.q}", [
     {"q": "What is a hypha?", "r": "one thread of a fungus", "w": ["a spore case", "a root of a plant", "a single bacterium"],
      "e": ["That is a sporangium.", "Fungi have no roots; they have rhizoids.", "Bacteria are a different kingdom."], "y": "Many hyphae make a mycelium."},
     {"q": "What is the job of the sporangium of bread mould?", "r": "to produce and release spores", "w": ["to anchor the mould", "to digest the bread", "to photosynthesise"],
      "e": ["Rhizoids anchor it.", "Hyphae release enzymes.", "Moulds cannot photosynthesise."], "y": "The black dots release thousands of spores."},
     {"q": "What anchors bread mould to the bread?", "r": "rhizoids", "w": ["sporangia", "chloroplasts", "flagella"],
      "e": ["Sporangia make spores.", "Moulds have none.", "Moulds do not swim."], "y": "Rhizoids are root-like hyphae."}], SRC),
   bank("b3-17-cond", 2, "{X.q}", [
     {"q": "Under which conditions does bread mould grow fastest?", "r": "warm, damp and dark", "w": ["cold and dry", "in a hot oven", "in a fridge"],
      "e": ["Cold and dry slow it.", "Very high heat kills it.", "Cold slows it."], "y": "Warmth and moisture help enzymes and growth."},
     {"q": "Why does keeping bread dry help stop mould?", "r": "Mould needs moisture to grow and digest food", "w": ["Dry bread has no food", "Spores cannot fly in dry air", "Dry bread is too hard to see"],
      "e": ["Dry bread still contains starch.", "Spores travel well in dry air.", "That is not a reason."], "y": "No water, little growth."},
     {"q": "How do mould spores reach new bread?", "r": "They are carried by air currents", "w": ["The mould walks there", "They grow from the flour", "They are made by the bread"],
      "e": ["Moulds do not move.", "Spores come from outside.", "Bread does not make spores."], "y": "Light spores float in the air everywhere."}], SRC),
   order("b3-17-grow", 3, "Put the growth of mould on bread in order.",
         ["A spore lands on damp bread.", "It germinates and a hypha grows.", "Hyphae branch to form a mycelium and digest the bread.",
          "Upright hyphae form sporangia.", "Sporangia burst and release new spores."], hint="Spore, hypha, mycelium, sporangia, spores.", sources=SRC, review="authored")],
  learn=learn(
    [("A kingdom of absorbers",
      "Fungi include moulds, mushrooms, toadstools and yeast. They have nuclei but no chlorophyll, so they cannot make food. Their cell walls are made of chitin, not cellulose.\n"
      "Most are built from fine threads called hyphae, which branch into a network called a mycelium. Yeast is an exception: it is single-celled."),
     ("How fungi feed",
      "Most fungi are saprophytes: they feed on dead plants and animals, rotting fruit, leaves and bread. Their hyphae release enzymes that digest the food outside the fungus; the dissolved products are then absorbed.\n"
      "Some are parasites, living on living hosts: ringworm on skin, black pod disease on cocoa."),
     ("Bread mould",
      "Leave damp bread in a warm, dark place and white fluffy threads appear: the hyphae of Mucor or Rhizopus. Rhizoids anchor it; upright hyphae carry black round sporangia.\n"
      "Each sporangium releases thousands of tiny spores into the air. When a spore lands on suitable food, it grows a new hypha. Keeping food cool, dry and covered slows mould.")],
    key_words=[("hypha", "a thread of a fungus (plural hyphae)"), ("mycelium", "a network of hyphae"), ("sporangium", "a structure that makes spores"),
               ("saprophyte", "an organism that feeds on dead organic matter")],
    examples=["Bread mould: Mucor, Rhizopus", "Black pod of cocoa: parasitic fungus", "Mushrooms: saprophytes"],
    mistake=("Fungi are plants", "Fungi are a separate kingdom",
             "They have no chlorophyll and their walls are made of chitin, not cellulose.")))

# ---------------------------------------------------------------- 18. Mushroom, yeast and importance of fungi
L.lesson(D, S, 18, ("b3-18", "Mushroom and yeast: structure, mode of life and importance of fungi"), [17],
  "Mushroom: the part above ground is the fruiting body: a stalk (stipe) and a cap (pileus) with gills underneath, where spores are made. Most of the mushroom is an underground mycelium feeding saprophytically on dead matter.\n"
  "Yeast: single oval cells; reproduces by budding. It respires anaerobically in sugar solution (fermentation): glucose → ethanol (alcohol) + carbon dioxide + energy.\n"
  "Importance of fungi:\n• Useful: food (mushrooms), yeast in bread (CO₂ makes dough rise) and in brewing; antibiotics (penicillin from Penicillium); decomposers that recycle nutrients.\n"
  "• Harmful: diseases of people (ringworm, athlete's foot, thrush), of crops (black pod of cocoa, maize smut), food spoilage, and poisonous mushrooms.",
  worked({},
         "Explain why yeast makes bread dough rise.",
         ["Yeast respires the sugar in the dough.", "It produces carbon dioxide gas.", "The gas bubbles are trapped in the dough, so it swells; baking kills the yeast and sets the bread."],
         "Carbon dioxide from yeast respiration is trapped in the dough"),
  [card("c3b18-1", "A mushroom is the fruiting body; spores form on the gills.",
        ["Cap, gills and stalk above ground; mycelium below"], "b3-18-part"),
   card("c3b18-2", "Yeast ferments sugar to alcohol and carbon dioxide.",
        ["Used in bread and in palm wine fermentation"], "b3-18-yeast"),
   card("c3b18-3", "Fungi can be useful or harmful.",
        ["Penicillin (useful); black pod of cocoa (harmful)"], "b3-18-imp")],
  [bank("b3-18-part", 1, "{X.q}", [
     {"q": "Where are the spores of a mushroom produced?", "r": "on the gills under the cap", "w": ["in the stalk", "in the soil only", "in the leaves"],
      "e": ["The stalk holds the cap up.", "Spores form above ground on the gills.", "Mushrooms have no leaves."], "y": "Gills release spores into the air."},
     {"q": "Most of a mushroom's body is…", "r": "an underground mycelium", "w": ["the cap", "the gills", "the roots"],
      "e": ["The cap is only the fruiting body.", "Gills are only part of the cap.", "Fungi have no roots."], "y": "The visible part is just for spreading spores."},
     {"q": "How does yeast reproduce?", "r": "by budding", "w": ["by seeds", "by binary fission only", "by pollination"],
      "e": ["Fungi have no seeds.", "Yeast mainly buds.", "Fungi have no flowers."], "y": "A small bud grows from the parent cell and breaks off."}], SRC),
   bank("b3-18-yeast", 1, "{X.q}", [
     {"q": "What are the products of fermentation by yeast?", "r": "ethanol (alcohol) and carbon dioxide", "w": ["oxygen and water", "lactic acid only", "glucose and oxygen"],
      "e": ["Those are not products of fermentation.", "That is muscle anaerobic respiration.", "Glucose is the starting material."], "y": "Glucose → ethanol + carbon dioxide + energy."},
     {"q": "Which gas makes bread dough rise?", "r": "carbon dioxide", "w": ["oxygen", "nitrogen", "hydrogen"],
      "e": ["Yeast uses oxygen if available but does not release it.", "Nitrogen is not produced.", "Hydrogen is not produced."], "y": "Yeast releases CO₂ that is trapped in the dough."},
     {"q": "Why is palm wine sweet when freshly tapped but becomes alcoholic after a day?", "r": "Yeasts ferment its sugar into alcohol", "w": ["The sun turns sugar into alcohol", "Water evaporates and leaves alcohol", "Bacteria add alcohol from the air"],
      "e": ["Fermentation is done by microbes.", "Evaporation does not make alcohol.", "Yeasts, not added alcohol, are the cause."], "y": "Natural yeasts carry out fermentation."}], SRC),
   bank("b3-18-imp", 2, "{X.q}", [
     {"q": "Which is a useful fungus?", "r": "Penicillium, which produces the antibiotic penicillin", "w": ["the fungus causing ringworm", "the fungus causing black pod of cocoa", "a poisonous toadstool"],
      "e": ["Ringworm is a disease.", "Black pod destroys cocoa harvests.", "Poisonous fungi are harmful."], "y": "Penicillin saves lives by killing bacteria."},
     {"q": "Which disease of cocoa in Cameroon is caused by a fungus?", "r": "black pod disease", "w": ["malaria", "cholera", "measles"],
      "e": ["Malaria is a human disease caused by a protoctist.", "Cholera is a bacterial human disease.", "Measles is a viral human disease."], "y": "Black pod rots cocoa pods; farmers spray fungicides."},
     {"q": "How do fungi help keep soils fertile?", "r": "As decomposers they break down dead matter and release nutrients", "w": ["They photosynthesise", "They fix nitrogen in root nodules", "They eat insects"],
      "e": ["Fungi do not photosynthesise.", "That is done by bacteria.", "Most fungi do not eat insects."], "y": "Recycling nutrients for plants."}], SRC),
   bank("b3-18-safety", 3, "{X.q}", [
     {"q": "Why should you not eat wild mushrooms you cannot identify?", "r": "Some are poisonous and can kill", "w": ["All mushrooms are poisonous", "Mushrooms have no food value", "They are always bitter"],
      "e": ["Many are edible.", "Edible mushrooms are nutritious.", "Taste is no guide to safety."], "y": "Poisonous and edible species can look alike."},
     {"q": "Athlete's foot grows between the toes. Which advice helps prevent it?", "r": "Keep feet clean and dry and do not share towels", "w": ["Keep feet warm and damp", "Take antibiotics daily", "Wear the same wet socks"],
      "e": ["Damp warmth helps the fungus.", "Antibiotics do not treat fungi.", "Wet socks help the fungus."], "y": "Fungi need moisture to grow."},
     {"q": "Why is yeast added to bread dough with a little sugar and warm (not hot) water?", "r": "Warmth and sugar let yeast respire quickly; very hot water would kill it", "w": ["Hot water makes yeast grow faster", "Sugar kills yeast", "Yeast needs cold water"],
      "e": ["Too hot kills yeast.", "Sugar is its food.", "Cold slows yeast."], "y": "Yeast enzymes work best at warm temperatures."}], SRC)],
  learn=learn(
    [("The mushroom",
      "What we call a mushroom is only the fruiting body. It has a stalk and a cap; under the cap are thin gills where millions of spores form and drop into the wind.\n"
      "The main body of the fungus is a mycelium of hyphae spread through the soil or rotting wood, feeding on dead matter as a saprophyte."),
     ("Yeast",
      "Yeast is a single-celled fungus with oval cells. It reproduces by budding: a small bud grows out and breaks off.\n"
      "In sugar solution without oxygen it ferments: glucose → ethanol + carbon dioxide + energy.\n"
      "Bakers use the carbon dioxide to make dough rise; brewers and palm wine tappers rely on the alcohol."),
     ("Friends and foes",
      "Useful fungi: edible mushrooms; yeast for bread and fermentation; Penicillium, which gives the antibiotic penicillin; decomposers that recycle nutrients.\n"
      "Harmful fungi: ringworm, athlete's foot and thrush in people; black pod of cocoa and smuts of maize; moulds that spoil food; poisonous mushrooms.")],
    key_words=[("fruiting body", "the part of a fungus that produces spores"), ("budding", "reproduction by a small outgrowth that breaks off"),
               ("fermentation", "anaerobic respiration of sugar by yeast"), ("antibiotic", "a substance from a microbe that kills bacteria")],
    examples=["Bread: yeast makes CO₂", "Penicillin: from Penicillium mould", "Black pod: fungal disease of cocoa"],
    mistake=("Yeast makes bread rise by producing oxygen", "Yeast makes bread rise by producing carbon dioxide",
             "Fermentation releases carbon dioxide, which is trapped in the dough.")))

# ---------------------------------------------------------------- 19. Kingdom Plantae
L.lesson(D, S, 19, ("b3-19", "Kingdom Plantae: characteristics and classification"), [9],
  "Plants are multicellular eukaryotes with cellulose cell walls and chlorophyll; they make food by photosynthesis and store it as starch.\n"
  "Main groups:\n• Non-flowering plants: mosses (no true roots, damp places), ferns (roots, stems, leaves; spores under the leaves), conifers (cones, needle leaves, seeds not in fruits).\n"
  "• Flowering plants (angiosperms): reproduce by flowers and seeds enclosed in fruits. Two classes:\n  monocotyledons (one seed leaf; e.g. maize, rice, grasses, palms, bananas) and dicotyledons (two seed leaves; e.g. beans, groundnuts, mango, cocoa, hibiscus).",
  worked({},
         "Classify maize, a fern and a mango tree.",
         ["Maize: flowering plant with one seed leaf → monocotyledon.", "Fern: no flowers or seeds; spores under its leaves → non-flowering (fern).", "Mango: flowering plant with two seed leaves → dicotyledon."],
         "Maize: monocot; fern: non-flowering; mango: dicot"),
  [card("c3b19-1", "Plants photosynthesise and have cellulose cell walls.",
        ["All green plants make their own food."], "b3-19-char"),
   card("c3b19-2", "Non-flowering plants: mosses, ferns, conifers.",
        ["Ferns have spores under their leaves."], "b3-19-group"),
   card("c3b19-3", "Flowering plants are monocots (one seed leaf) or dicots (two).",
        ["Maize: monocot. Bean: dicot."], "b3-19-mono")],
  [bank("b3-19-char", 1, "{X.q}", [
     {"q": "Which feature do all plants share?", "r": "cellulose cell walls and chlorophyll", "w": ["flowers", "seeds", "woody stems"],
      "e": ["Mosses and ferns have no flowers.", "Mosses and ferns have no seeds.", "Many plants are not woody."], "y": "All plants photosynthesise."},
     {"q": "How do plants store food?", "r": "mainly as starch", "w": ["mainly as glycogen", "as chitin", "they cannot store food"],
      "e": ["Glycogen is stored by animals and fungi.", "Chitin is a fungal wall material.", "Cassava roots and maize grains are full of starch."], "y": "Starch is the plant storage carbohydrate."},
     {"q": "How are plants different from fungi?", "r": "Plants have chlorophyll and make their own food", "w": ["Plants have no cell walls", "Fungi have chlorophyll", "Plants are single-celled"],
      "e": ["Plants have cellulose walls.", "Fungi have none.", "Plants are multicellular."], "y": "Photosynthesis is the key difference."}], SRC),
   bank("b3-19-group", 1, "To which group does this plant belong? {X.q}", [
     {"q": "It has fronds with brown spore patches underneath and no flowers.", "r": "ferns", "w": ["mosses", "monocotyledons", "dicotyledons"],
      "e": ["Mosses are tiny with no true roots or fronds.", "Monocots have flowers.", "Dicots have flowers."], "y": "Ferns reproduce by spores under their leaves."},
     {"q": "It is a small, soft green plant of damp walls, with no true roots.", "r": "mosses", "w": ["ferns", "conifers", "monocotyledons"],
      "e": ["Ferns have true roots.", "Conifers are trees.", "Monocots have flowers and roots."], "y": "Mosses have rhizoids, not true roots."},
     {"q": "It has needle-shaped leaves and seeds in cones.", "r": "conifers", "w": ["ferns", "mosses", "monocotyledons"],
      "e": ["Ferns have no seeds.", "Mosses have no seeds.", "Monocots make seeds in fruits."], "y": "Conifers bear naked seeds in cones."}], SRC),
   bank("b3-19-mono", 2, "Is this plant a monocot or a dicot? {X.q}", [
     {"q": "maize", "r": "monocotyledon", "w": ["dicotyledon", "fern", "conifer"],
      "e": ["Maize has one seed leaf.", "Maize has flowers and seeds.", "Maize has no cones."], "y": "Grasses and cereals are monocots."},
     {"q": "groundnut", "r": "dicotyledon", "w": ["monocotyledon", "moss", "fern"],
      "e": ["The groundnut seed splits into two halves: two seed leaves.", "It has flowers.", "It has flowers and seeds."], "y": "Beans and groundnuts are dicots."},
     {"q": "oil palm", "r": "monocotyledon", "w": ["dicotyledon", "conifer", "fern"],
      "e": ["Palms have one seed leaf and parallel-veined leaves.", "Palms have fruits, not cones.", "Palms have flowers and seeds."], "y": "Palms are monocots."},
     {"q": "cocoa", "r": "dicotyledon", "w": ["monocotyledon", "fern", "moss"],
      "e": ["Cocoa beans have two seed leaves.", "Cocoa flowers.", "Cocoa is a tree with seeds."], "y": "Cocoa is a dicot tree."}], SRC),
   bank("b3-19-why", 3, "{X.q}", [
     {"q": "Why can mosses grow only in damp places?", "r": "They have no true roots or water-carrying tissue and need water for reproduction", "w": ["They need darkness", "They are fungi", "They have large roots that need mud"],
      "e": ["Light is not the reason.", "Mosses are plants.", "They have no true roots."], "y": "Water must be close at hand."},
     {"q": "What makes flowering plants different from conifers?", "r": "Their seeds are enclosed in fruits", "w": ["They have no seeds", "They have no leaves", "They reproduce only by spores"],
      "e": ["Both have seeds.", "Both have leaves.", "Both make seeds."], "y": "Angiosperm means 'seed in a vessel'."},
     {"q": "Which is the best evidence that a plant is a monocot?", "r": "its seed has only one cotyledon", "w": ["it is tall", "it has green leaves", "it grows near water"],
      "e": ["Height does not decide it.", "All plants have green leaves.", "Habitat does not decide it."], "y": "Monocot means one seed leaf."}], SRC)],
  learn=learn(
    [("What makes a plant",
      "Plants are multicellular organisms whose cells have nuclei, cellulose walls and chloroplasts. They make their own food by photosynthesis and store it as starch: think of cassava roots, yam tubers and maize grains.\n"
      "They are fixed in one place and grow throughout their lives."),
     ("Plants without flowers",
      "• Mosses: small, soft plants of damp walls and tree trunks; no true roots (only rhizoids), no flowers, reproduce by spores.\n"
      "• Ferns: true roots, stems and leaves (fronds); brown spore patches under the fronds; no flowers or seeds.\n"
      "• Conifers: trees with needle-like leaves; seeds are carried in cones, not inside fruits."),
     ("Flowering plants",
      "Flowering plants reproduce with flowers, and their seeds are enclosed in fruits. They are divided by the number of seed leaves (cotyledons) in the seed:\n"
      "• monocotyledons, one: maize, rice, sorghum, grasses, oil palm, banana, onion;\n• dicotyledons, two: beans, groundnuts, mango, cocoa, coffee, hibiscus.\n"
      "Next lesson compares them in detail.")],
    key_words=[("cotyledon", "a seed leaf"), ("monocotyledon", "flowering plant with one seed leaf"), ("dicotyledon", "flowering plant with two seed leaves"),
               ("angiosperm", "a flowering plant with seeds in fruits")],
    examples=["Moss: damp walls", "Fern: spores under fronds", "Maize: monocot", "Mango: dicot"],
    mistake=("Ferns reproduce by seeds", "Ferns reproduce by spores",
             "Ferns have no flowers and no seeds; spores form under their fronds.")))

# ---------------------------------------------------------------- 20. Dicots: the bean plant; monocots vs dicots
L.lesson(D, S, 20, ("b3-20", "Dicotyledons: the bean plant, and differences from monocotyledons"), [19],
  "A bean plant (dicot): taproot with lateral roots and root nodules (nitrogen-fixing bacteria); stem carrying leaves, flowers and pods; broad leaves with net (reticulate) veins; seeds with two cotyledons.\n"
  "Functions: roots anchor the plant and absorb water and minerals; the stem supports and transports; leaves photosynthesise; flowers make seeds; pods protect and spread seeds.\n"
  "Monocot vs dicot:\n• seed leaves: one vs two; • leaf veins: parallel vs net;\n• roots: fibrous vs taproot; • flower parts: in threes vs in fours or fives;\n"
  "• vascular bundles in the stem: scattered vs in a ring.",
  worked({},
         "A plant has broad leaves with net veins, a taproot and flowers with five petals. Is it a monocot or a dicot?",
         ["Net veins → dicot.", "Taproot → dicot.", "Flower parts in fives → dicot."], "Dicotyledon"),
  [card("c3b20-1", "Each part of the bean plant has a job.",
        ["Root nodules contain nitrogen-fixing bacteria."], "b3-20-func"),
   card("c3b20-2", "Dicots have net veins and taproots; monocots parallel veins and fibrous roots.",
        ["Bean: net veins. Maize: parallel veins."], "b3-20-diff"),
   card("c3b20-3", "Dicot flower parts are in fours or fives; monocot parts in threes.",
        ["Hibiscus has {5} petals."], "b3-20-id")],
  [bank("b3-20-func", 1, "What is the main function of this part of a bean plant? {X.q}", [
     {"q": "Root", "r": "anchoring the plant and absorbing water and minerals", "w": ["making food", "producing seeds", "carrying out gas exchange only"],
      "e": ["Leaves make food.", "Flowers produce seeds.", "Leaves are the main site of gas exchange."], "y": "Roots hold the plant and take in water."},
     {"q": "Leaf", "r": "photosynthesis", "w": ["absorbing water from soil", "anchoring the plant", "storing seeds"],
      "e": ["Roots absorb water.", "Roots anchor.", "Pods hold seeds."], "y": "Leaves have the most chloroplasts."},
     {"q": "Root nodule", "r": "housing nitrogen-fixing bacteria", "w": ["storing water", "making flowers", "photosynthesis"],
      "e": ["Nodules are not water stores.", "Flowers form on the stem.", "Nodules are underground."], "y": "The bacteria make nitrogen compounds for the plant."},
     {"q": "Pod", "r": "protecting the seeds and helping to disperse them", "w": ["absorbing water", "photosynthesis only", "anchoring the plant"],
      "e": ["Roots absorb water.", "Leaves are the main photosynthetic organs.", "Roots anchor."], "y": "The pod is the fruit; it splits to release seeds."}], SRC),
   bank("b3-20-diff", 1, "{X.q}", [
     {"q": "What kind of veins does a dicot leaf have?", "r": "a network of branching veins", "w": ["parallel veins", "no veins", "veins only at the edge"],
      "e": ["Parallel veins are monocot.", "All leaves have veins.", "Veins run through the whole leaf."], "y": "Net (reticulate) venation."},
     {"q": "What kind of root system does maize have?", "r": "fibrous roots", "w": ["a taproot", "root nodules", "no roots"],
      "e": ["Taproots are dicot.", "Nodules are typical of legumes.", "Maize has roots."], "y": "Monocots have many similar fibrous roots."},
     {"q": "In which plants are the flower parts usually in threes?", "r": "monocotyledons", "w": ["dicotyledons", "ferns", "mosses"],
      "e": ["Dicot flowers have parts in fours or fives.", "Ferns have no flowers.", "Mosses have no flowers."], "y": "Lilies and onions: parts in threes."}], SRC),
   bank("b3-20-id", 2, "Monocot or dicot? {X.q}", [
     {"q": "Long narrow leaves with parallel veins and fibrous roots", "r": "monocotyledon", "w": ["dicotyledon", "fern", "conifer"],
      "e": ["Dicots have net veins and taproots.", "Ferns do not have these features.", "Conifers have needles."], "y": "Parallel veins and fibrous roots: monocot."},
     {"q": "A flower with 5 petals and leaves with a network of veins", "r": "dicotyledon", "w": ["monocotyledon", "moss", "fern"],
      "e": ["Monocot flowers are in threes, with parallel veins.", "Mosses have no flowers.", "Ferns have no flowers."], "y": "Five petals and net veins: dicot."},
     {"q": "A stem with vascular bundles scattered all through it", "r": "monocotyledon", "w": ["dicotyledon", "conifer", "moss"],
      "e": ["Dicot bundles are in a ring.", "Conifers have bundles in a ring.", "Mosses have no vascular bundles."], "y": "Scattered bundles: monocot."}], SRC),
   bank("b3-20-compare", 3, "{X.q}", [
     {"q": "Why do farmers often plant beans or groundnuts between rows of maize?", "r": "Their root nodules add nitrogen to the soil", "w": ["They shade out weeds completely", "They make the maize grow faster by photosynthesis", "They repel all insects"],
      "e": ["Shading is a small benefit, not the main one.", "They do not photosynthesise for maize.", "They do not repel all insects."], "y": "Legumes improve soil fertility."},
     {"q": "Which pair shows one monocot feature and one dicot feature?", "r": "parallel veins (monocot); taproot (dicot)", "w": ["net veins (monocot); fibrous roots (dicot)", "one cotyledon (dicot); two cotyledons (monocot)", "parts in threes (dicot); parts in fives (monocot)"],
      "e": ["Net veins are dicot; fibrous roots are monocot.", "Monocots have one cotyledon; dicots two.", "Threes are monocot; fives are dicot."], "y": "Match each feature to its group."},
     {"q": "A seed splits easily into two halves. What does this tell you?", "r": "It is a dicot seed with two cotyledons", "w": ["It is a monocot seed", "It is a spore", "It has no embryo"],
      "e": ["Monocot seeds have one cotyledon.", "Spores are tiny single cells.", "The embryo lies between the halves."], "y": "The two halves are the two cotyledons."}], SRC)],
  learn=learn(
    [("The bean plant",
      "A bean plant is a typical dicot. It has:\n• a taproot with side roots and small swellings (nodules) holding nitrogen-fixing bacteria;\n"
      "• a stem that holds up the leaves and flowers and carries water and food;\n• broad leaves with a network of veins, where photosynthesis happens;\n"
      "• flowers that develop into pods (fruits) containing seeds, each seed with two cotyledons."),
     ("Monocots and dicots compared",
      "• Seed leaves: one (monocot) vs two (dicot).\n• Leaf veins: parallel vs net.\n• Leaf shape: often long and narrow vs broad.\n• Roots: fibrous vs taproot.\n"
      "• Flower parts: in threes vs in fours or fives.\n• Vascular bundles in the stem: scattered vs in a ring.\n"
      "Maize, rice and palm are monocots; beans, mango and cocoa are dicots."),
     ("Why it matters on the farm",
      "Knowing the group helps farmers. Legumes (beans, groundnuts, soya) are dicots whose nodules add nitrogen to the soil, so they are rotated or intercropped with maize.\n"
      "Some weedkillers kill broad-leaved dicot weeds but not monocot grasses like maize: knowing the difference avoids killing the crop.")],
    key_words=[("taproot", "one main root with side roots"), ("fibrous roots", "many similar thin roots"), ("net venation", "a branching network of veins"),
               ("legume", "a plant of the bean family with nitrogen-fixing nodules")],
    examples=["Bean: dicot, taproot, net veins", "Maize: monocot, fibrous roots, parallel veins", "Hibiscus: {5} petals, dicot"],
    mistake=("Maize has net veins like beans", "Maize has parallel veins",
             "Parallel veins are a monocot feature; maize is a monocot.")))

# ---------------------------------------------------------------- 21. Bony fish: Tilapia
L.lesson(D, S, 21, ("b3-21", "Kingdom Animalia: the bony fish (Tilapia)"), [9],
  "Tilapia is a bony fish of rivers, lakes and fish ponds. Body: head, trunk and tail, streamlined.\n"
  "External features and functions: scales (protection, reduce friction), mucus (smooth surface), operculum (gill cover), gills (gas exchange), fins (dorsal and anal: stability; pectoral and pelvic: steering, braking, balance; caudal/tail fin: forward thrust), lateral line (senses vibrations and pressure changes), eyes without eyelids, nostrils (smell), mouth.\n"
  "Internal: swim bladder (adjusts buoyancy), bony skeleton.\n"
  "Adaptations: streamlined shape, overlapping backward-pointing scales, gills with large surface area, swim bladder, lateral line.\n"
  "Economic importance: cheap protein food, income for fishermen and fish farmers (fish ponds, Lagdo and Mape dams), fish meal; controlling mosquito larvae.",
  worked({},
         "Explain how the gills of a tilapia are adapted for gas exchange.",
         ["Many thin gill filaments give a very large surface area.", "They have a rich blood supply close to the surface, so the distance for diffusion is short.",
          "Water flows over them all the time, keeping a steep concentration gradient for oxygen."], "Large surface area, thin walls, good blood supply, constant water flow"),
  [card("c3b21-1", "Fins: the tail fin pushes the fish forward; the others steer and balance.",
        ["Pectoral fins act as brakes."], "b3-21-fin"),
   card("c3b21-2", "Gills exchange gases with the water.",
        ["Oxygen diffuses into the blood in the gill filaments."], "b3-21-part"),
   card("c3b21-3", "Tilapia is an important cheap source of protein and income.",
        ["Fish ponds in the West and North regions"], "b3-21-econ")],
  [bank("b3-21-fin", 1, "What is the main function of the {X.q}?", [
     {"q": "caudal (tail) fin", "r": "pushing the fish forward", "w": ["steering only", "breathing", "detecting vibrations"],
      "e": ["Paired fins do the steering.", "Gills are for breathing.", "The lateral line detects vibrations."], "y": "Side-to-side beats of the tail drive the fish."},
     {"q": "pectoral fins", "r": "steering, balancing and braking", "w": ["forward thrust", "gas exchange", "protecting the gills"],
      "e": ["The tail gives thrust.", "Gills exchange gases.", "The operculum protects the gills."], "y": "Paired fins near the head control direction."},
     {"q": "dorsal fin", "r": "keeping the fish upright (stopping rolling)", "w": ["pushing forward", "breathing", "sensing smell"],
      "e": ["The tail pushes.", "Gills breathe.", "Nostrils smell."], "y": "Like a keel, it stops the fish rolling over."}], SRC),
   bank("b3-21-part", 1, "{X.q}", [
     {"q": "What is the function of the operculum?", "r": "covering and protecting the gills", "w": ["moving the fish forward", "detecting vibrations", "storing air"],
      "e": ["The tail fin does that.", "The lateral line does that.", "The swim bladder holds gas."], "y": "The gill cover also helps pump water over the gills."},
     {"q": "What does the lateral line detect?", "r": "vibrations and pressure changes in the water", "w": ["light", "taste", "oxygen"],
      "e": ["The eyes detect light.", "Taste buds detect taste.", "Gills take in oxygen; the lateral line does not detect it."], "y": "It helps the fish sense movement nearby."},
     {"q": "What is the swim bladder for?", "r": "adjusting buoyancy so the fish can float at different depths", "w": ["digesting food", "breathing air", "laying eggs"],
      "e": ["The gut digests food.", "Tilapia breathes with gills.", "The ovaries make eggs."], "y": "Changing the gas in it changes the fish's density."}], SRC),
   bank("b3-21-adapt", 2, "{X.q}", [
     {"q": "Why is a streamlined body useful to a fish?", "r": "It reduces water resistance, so the fish swims with less effort", "w": ["It makes the fish heavier", "It helps the fish breathe air", "It keeps the fish warm"],
      "e": ["Shape does not add weight.", "Fish breathe dissolved oxygen through gills.", "Fish are cold-blooded."], "y": "Smooth tapered shape cuts through water."},
     {"q": "Why do a fish's scales overlap and point backwards?", "r": "They protect the body and let water flow smoothly over it", "w": ["They help the fish climb", "They store food", "They are used for breathing"],
      "e": ["Fish do not climb.", "Scales do not store food.", "Gills are for breathing."], "y": "Backward-pointing scales reduce friction."},
     {"q": "Why do the gill filaments have a large surface area?", "r": "To absorb enough oxygen from water, which holds little oxygen", "w": ["To catch food only", "To make the fish lighter", "To sense vibrations"],
      "e": ["Gill rakers trap food; filaments are for gas exchange.", "Surface area does not reduce weight.", "The lateral line senses vibrations."], "y": "More surface, more diffusion."}], SRC),
   bank("b3-21-econ", 3, "{X.q}", [
     {"q": "Why is fish farming of tilapia encouraged in Cameroon?", "r": "It provides cheap protein and income for farmers", "w": ["Tilapia cannot live in ponds", "Fish are not eaten in Cameroon", "Tilapia removes all water from ponds"],
      "e": ["Tilapia grows well in ponds.", "Fish is an important food.", "Fish do not remove water."], "y": "Fish ponds supply local markets with protein."},
     {"q": "How can tilapia in fish ponds help reduce malaria?", "r": "They eat mosquito larvae in the water", "w": ["They bite adult mosquitoes", "They make the water salty", "They produce insecticide"],
      "e": ["They feed in water, not on flying adults.", "They do not change salinity.", "They do not make chemicals."], "y": "Fewer larvae, fewer mosquitoes."},
     {"q": "Which human activity can reduce fish numbers in a lake?", "r": "overfishing with very small-meshed nets", "w": ["planting trees on the banks", "keeping the water clean", "fishing only adult fish"],
      "e": ["Trees protect banks and water.", "Clean water helps fish.", "Leaving young fish lets stocks recover."], "y": "Catching young fish stops the population replacing itself."}], SRC)],
  learn=learn(
    [("A fish built for water",
      "Tilapia lives in rivers, lakes and fish ponds across Cameroon. Its body has a head, a trunk and a tail, and is streamlined: smooth and tapering at both ends, so it moves through water easily.\n"
      "Overlapping scales point backwards and are covered with slimy mucus, which protects the fish and reduces friction."),
     ("Parts and their jobs",
      "• Gills, under a bony cover (operculum): water enters the mouth and passes over the gills; oxygen diffuses into the blood.\n"
      "• Fins: the tail (caudal) fin pushes forward; dorsal and anal fins keep the fish upright; paired pectoral and pelvic fins steer, balance and brake.\n"
      "• Lateral line: a line of sense organs along each side that detects vibrations.\n• Swim bladder: a gas-filled sac inside that lets the fish float at any depth.\n• Eyes (no eyelids), nostrils and a mouth for feeding."),
     ("Fish and people",
      "Tilapia is a cheap, rich source of protein. Fishermen on rivers and lakes, and fish farmers with ponds (and at dams such as Lagdo and Mape), earn their living from it.\n"
      "Fish also give fish meal for animal feed, and tilapia eat mosquito larvae. Overfishing and pollution threaten fish stocks.")],
    key_words=[("streamlined", "shaped to move through water or air with little resistance"), ("operculum", "the bony gill cover"),
               ("lateral line", "sense organ along the side that detects vibrations"), ("swim bladder", "gas-filled sac controlling buoyancy")],
    examples=["Caudal fin: thrust", "Gills: gas exchange", "Swim bladder: buoyancy"],
    mistake=("Fish breathe by taking air into lungs", "Fish breathe by gills that absorb oxygen dissolved in water",
             "Water flows over the gills, and oxygen diffuses into the blood.")))
