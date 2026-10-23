"""Form 3 Computer Science, Term 1, rows 8-13 (processor, processor cycle, primary and secondary storage, internal components, ports).
Run: python tools/authoring/form3/cs_a3.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"
SRC = ["hardware"]

# ---------------------------------------------------------------- 8. The processor
L.lesson(D, S, 8, ("s3-8", "The processor (CPU): parts and performance"), [],
  "The central processing unit (CPU, processor) carries out the instructions of programs. Main parts:\n"
  "• Control unit (CU): fetches instructions, decodes them and directs the other parts.\n• Arithmetic and logic unit (ALU): does calculations and comparisons.\n"
  "• Registers: tiny, very fast memory locations inside the CPU (e.g. program counter, accumulator).\n• Cache: small fast memory holding data the CPU uses often.\n"
  "Performance depends on: clock speed (in GHz: 1 GHz = 1 000 000 000 cycles per second), the number of cores (each core can process instructions at the same time), and cache size.",
  worked({"g": 2.5, "c": 4},
         "A laptop has a {c}-core processor running at {g} GHz. How many clock cycles does each core make in one second?",
         ["{1} GHz = {1000000000} cycles per second.", "{g} GHz = {g} × {1000000000} = {g * 1000000000} cycles per second for each core."],
         "{g * 1000000000} cycles per second", checks=["g * 1000000000 == 2500000000"]),
  [card("c3s8-1", "The CU directs; the ALU calculates and compares.",
        ["Adding two numbers is done in the ALU."], "s3-8-part"),
   card("c3s8-2", "Clock speed is measured in GHz: billions of cycles per second.",
        ["{3} GHz = {3000000000} cycles each second"], "s3-8-ghz"),
   card("c3s8-3", "More cores and more cache can make a computer faster.",
        ["A quad-core processor has {4} cores."], "s3-8-perf")],
  [bank("s3-8-part", 1, "Which part of the CPU does this? {X.q}", [
     {"q": "It carries out calculations and comparisons.", "r": "the arithmetic and logic unit (ALU)", "w": ["the control unit", "the hard disk", "the monitor"],
      "e": ["The CU directs; it does not calculate.", "The hard disk stores data.", "The monitor is an output device."], "y": "ALU: arithmetic (add, subtract) and logic (compare)."},
     {"q": "It fetches and decodes instructions and directs the other parts.", "r": "the control unit (CU)", "w": ["the ALU", "the cache", "the keyboard"],
      "e": ["The ALU calculates.", "Cache stores data.", "The keyboard is an input device."], "y": "The CU is like a manager."},
     {"q": "They are tiny, very fast storage locations inside the CPU.", "r": "registers", "w": ["RAM chips", "USB drives", "hard disks"],
      "e": ["RAM is outside the CPU.", "USB drives are external storage.", "Hard disks are slow secondary storage."], "y": "Registers hold the data being worked on right now."}], SRC),
   num("s3-8-ghz", 1, "A processor runs at {g} GHz. How many clock cycles does it make each second? (Give the number in millions of cycles, MHz.)", "g * 1000",
       ["{1} GHz = {1000} MHz.", "{g} GHz = {g} × {1000} = {answer} MHz (million cycles per second)."],
       vars={"k": {"int": [10, 45]}, "g": {"expr": "k / 10"}},
       misc=[("div", "g / 1000", "GHz is bigger than MHz: multiply by {1000}.")],
       unit="MHz", sources=SRC),
   bank("s3-8-perf", 2, "{X.q}", [
     {"q": "Which change would most likely make a computer run programs faster?", "r": "a processor with a higher clock speed and more cores", "w": ["a bigger monitor", "a louder speaker", "a longer cable"],
      "e": ["Screen size does not affect processing speed.", "Speakers are output devices.", "Cable length is irrelevant."], "y": "More cycles and more cores process more instructions."},
     {"q": "What is cache memory?", "r": "small, fast memory that holds data the CPU uses often", "w": ["the main storage for all files", "a type of printer", "the computer's case"],
      "e": ["That is secondary storage.", "Printers are output devices.", "The case holds the parts."], "y": "Cache saves time fetching from RAM."},
     {"q": "A dual-core processor has…", "r": "two cores that can process instructions at the same time", "w": ["two screens", "two keyboards", "double the RAM"],
      "e": ["Cores are inside the CPU.", "Cores are inside the CPU.", "RAM is separate."], "y": "Dual means two."}], SRC),
   num("s3-8-compare", 3, "Processor A runs at {a} GHz with {ca} cores; processor B at {b} GHz with {cb} cores. Assuming each core does one instruction per cycle, how many more billion instructions per second can the faster one do?", "abs(roundTo(a * ca - b * cb, 0.01))",
       ["A: {a} × {ca} = {roundTo(a * ca, 0.01)} billion per second.", "B: {b} × {cb} = {roundTo(b * cb, 0.01)} billion per second.", "Difference = {answer} billion."],
       vars={"ka": {"int": [15, 40]}, "kb": {"int": [15, 40]}, "a": {"expr": "ka / 10"}, "b": {"expr": "kb / 10"}, "ca": {"pick": [2, 4, 8]}, "cb": {"pick": [2, 4, 8]}},
       misc=[("speed", "abs(roundTo(a - b, 0.01))", "Multiply each clock speed by its number of cores first.")],
       sources=SRC, where=["roundTo(a * ca, 0.01) != roundTo(b * cb, 0.01)", "ca != cb", "abs(roundTo(a - b, 0.01)) != abs(roundTo(a * ca - b * cb, 0.01))"])],
  learn=learn(
    [("The brain of the computer",
      "The central processing unit (CPU), or processor, carries out the instructions of every program. It is a chip on the motherboard, usually under a fan and heat sink because it gets hot.\n"
      "Its main parts:\n• Control unit (CU): fetches each instruction from memory, decodes it, and directs the rest.\n• Arithmetic and logic unit (ALU): does calculations and comparisons.\n"
      "• Registers: tiny stores inside the CPU for the data being worked on now.\n• Cache: small, fast memory close to the CPU for data used often."),
     ("Clock speed",
      "The CPU works in steps timed by a clock. Clock speed is measured in hertz (cycles per second): {1} GHz (gigahertz) = {1000} MHz = {1000000000} cycles per second.\n"
      "A {3} GHz processor has three billion clock cycles each second. A higher clock speed usually means faster processing."),
     ("Cores and cache",
      "Modern processors have several cores, each able to process instructions at the same time: dual-core ({2}), quad-core ({4}), octa-core ({8}).\n"
      "More cores help when running many programs at once. A bigger cache means the CPU waits less for data from RAM.\n"
      "So performance depends on clock speed, number of cores and cache size together.")],
    key_words=[("CPU", "the central processing unit, which carries out instructions"), ("ALU", "arithmetic and logic unit"), ("control unit", "part that fetches, decodes and directs"),
               ("clock speed", "number of cycles per second, in GHz"), ("core", "a processing unit inside the CPU")],
    examples=["{2.4} GHz = {2400} MHz", "Quad-core: {4} cores", "ALU compares two numbers"],
    mistake=("The CPU stores all your files", "Files are kept in secondary storage; the CPU processes instructions",
             "Registers and cache are tiny; long-term storage is on disks.")))

# ---------------------------------------------------------------- 9. The processor cycle
L.lesson(D, S, 9, ("s3-9", "The fetch-decode-execute cycle"), [8],
  "The CPU repeats the fetch-decode-execute cycle billions of times a second:\n"
  "• Fetch: the control unit gets the next instruction from main memory (RAM), using the address in the program counter (PC); the PC then increases to point to the next instruction.\n"
  "• Decode: the control unit works out what the instruction means.\n"
  "• Execute: the instruction is carried out, e.g. the ALU adds two numbers and the result goes into the accumulator, or data is stored in memory.\n"
  "Then the cycle starts again with the next instruction. Programs and data are both kept in memory (the stored-program idea).",
  worked({},
         "Describe what happens in one cycle when the instruction 'ADD {5}' is processed.",
         ["Fetch: the CU reads the instruction 'ADD {5}' from the RAM address held in the program counter; the PC moves on by one.",
          "Decode: the CU recognises an addition instruction.", "Execute: the ALU adds {5} to the value in the accumulator and stores the result there."],
         "Fetch, decode, execute (ALU adds and stores the result)"),
  [card("c3s9-1", "Fetch → decode → execute, repeated.",
        ["Billions of cycles every second"], "s3-9-order"),
   card("c3s9-2", "The program counter holds the address of the next instruction.",
        ["After a fetch it increases by {1}."], "s3-9-pc"),
   card("c3s9-3", "The ALU executes calculations; the result goes to the accumulator.",
        ["ADD, SUBTRACT, COMPARE"], "s3-9-stage")],
  [order("s3-9-order", 1, "Put the stages of the processor cycle in order.",
         ["Fetch the instruction from memory.", "Decode the instruction.", "Execute the instruction.", "Fetch the next instruction."],
         hint="Get it, understand it, do it.", sources=SRC, review="authored"),
   bank("s3-9-pc", 1, "{X.q}", [
     {"q": "What does the program counter (PC) hold?", "r": "the memory address of the next instruction", "w": ["the result of a calculation", "the number of programs installed", "the clock speed"],
      "e": ["That is the accumulator.", "That is not a register's job.", "That is a property of the clock."], "y": "The PC points to where the next instruction is."},
     {"q": "What happens to the program counter after an instruction is fetched?", "r": "It increases to point to the next instruction", "w": ["It is set to zero", "It is deleted", "It stores the answer"],
      "e": ["Only at the start of a program.", "Registers are not deleted.", "The accumulator stores answers."], "y": "It moves on so the next fetch gets the next instruction."},
     {"q": "Where are instructions fetched from?", "r": "main memory (RAM)", "w": ["the keyboard", "the printer", "the monitor"],
      "e": ["The keyboard is an input device.", "The printer is an output device.", "The monitor is an output device."], "y": "Programs are loaded into RAM to run."}], SRC),
   bank("s3-9-stage", 2, "In which stage of the cycle does this happen? {X.q}", [
     {"q": "The ALU adds two numbers.", "r": "execute", "w": ["fetch", "decode", "store the program on disk"],
      "e": ["Fetching only collects the instruction.", "Decoding works out what to do.", "That is not part of the cycle."], "y": "Carrying out the instruction is execution."},
     {"q": "The control unit works out what the instruction means.", "r": "decode", "w": ["fetch", "execute", "input"],
      "e": ["Fetch collects it.", "Execute carries it out.", "Input is from devices."], "y": "Decoding interprets the instruction."},
     {"q": "The instruction is copied from RAM into the CPU.", "r": "fetch", "w": ["decode", "execute", "output"],
      "e": ["Decoding comes after.", "Execution comes last.", "Output goes to devices."], "y": "Fetching brings the instruction into the CPU."}], SRC),
   num("s3-9-count", 3, "A simple processor completes one fetch-decode-execute cycle every clock cycle. At {g} GHz, how many million instructions can it complete in {t} milliseconds?", "g * t",
       ["{g} GHz = {g * 1000} million cycles per second.", "{t} ms = {t} ÷ {1000} s.", "Instructions = {g * 1000} × {t / 1000} = {answer} million."],
       vars={"k": {"int": [1, 4]}, "g": {"expr": "k"}, "t": {"int": [1, 10]}},
       misc=[("sec", "g * 1000", "That is for a whole second. Multiply by {t} ÷ {1000}.")],
       sources=SRC)],
  learn=learn(
    [("One instruction at a time",
      "A program is a list of instructions stored in main memory (RAM). The CPU carries them out one after another in a repeating cycle: fetch, decode, execute.\n"
      "At {3} GHz, a core can repeat this cycle billions of times every second."),
     ("The three stages",
      "• Fetch: the control unit looks at the program counter (PC), which holds the address of the next instruction, and copies that instruction from RAM into the CPU. The PC then increases by one.\n"
      "• Decode: the control unit works out what the instruction means and what is needed.\n"
      "• Execute: the instruction is carried out: the ALU may add or compare numbers and put the result in the accumulator, or data may be moved to or from memory."),
     ("Why it matters",
      "Everything a computer does, from showing a letter on the screen to playing a video, is built from millions of these simple cycles.\n"
      "Because programs and data are both stored in memory, the computer can switch from one program to another just by loading different instructions: this is the stored-program idea.")],
    key_words=[("fetch", "copy the next instruction from memory into the CPU"), ("decode", "work out what the instruction means"),
               ("execute", "carry out the instruction"), ("program counter", "register holding the address of the next instruction"), ("accumulator", "register that holds results from the ALU")],
    examples=["ADD: executed in the ALU", "PC: {100} → {101} after a fetch", "Cycle repeated billions of times a second"],
    mistake=("The CPU decodes before fetching", "The order is fetch, decode, execute",
             "The CPU must first get the instruction before it can understand it.")))

# ---------------------------------------------------------------- 10. Primary storage
L.lesson(D, S, 10, ("s3-10", "Primary storage: RAM and ROM; storage units"), [8],
  "Primary (main) storage is directly accessed by the CPU.\n"
  "• RAM (random access memory): holds the programs and data in use; it can be read and written; it is volatile (contents lost when power goes off). More RAM lets more programs run smoothly.\n"
  "• ROM (read-only memory): holds the start-up instructions (BIOS/firmware); it can only be read; it is non-volatile.\n"
  "Units: 8 bits = 1 byte; 1 KB = 1024 bytes; 1 MB = 1024 KB; 1 GB = 1024 MB; 1 TB = 1024 GB.",
  worked({"v": 4},
         "How many megabytes are in {v} GB of RAM?",
         ["{1} GB = {1024} MB.", "{v} GB = {v} × {1024} = {storageConvert(v, 'GB', 'MB')} MB."], "{storageConvert(v, 'GB', 'MB')} MB", checks=["storageConvert(v, 'GB', 'MB') == 4096"]),
  [card("c3s10-1", "RAM is volatile and holds programs in use; ROM is non-volatile and read-only.",
        ["A power cut erases unsaved work in RAM."], "s3-10-rr"),
   card("c3s10-2", "{8} bits = {1} byte; each larger unit is {1024} times the previous.",
        ["{1} KB = {1024} bytes"], "s3-10-units"),
   card("c3s10-3", "More RAM lets more programs run at once without slowing down.",
        ["{8} GB RAM vs {2} GB RAM"], "s3-10-more")],
  [bank("s3-10-rr", 1, "{X.q}", [
     {"q": "What happens to the contents of RAM when the computer is switched off?", "r": "They are lost (RAM is volatile)", "w": ["They are saved forever", "They move to ROM", "They are printed"],
      "e": ["RAM needs power to keep data.", "ROM cannot be written to.", "Nothing is printed."], "y": "Save your work to secondary storage."},
     {"q": "What is stored in ROM?", "r": "the start-up instructions (BIOS/firmware)", "w": ["the document you are typing", "your photos", "the web page you are viewing"],
      "e": ["That is in RAM while you type.", "Photos are in secondary storage.", "That is in RAM."], "y": "ROM holds instructions needed to start the computer."},
     {"q": "Which memory can the user's programs both read and write?", "r": "RAM", "w": ["ROM", "a CD-ROM", "the BIOS chip"],
      "e": ["ROM is read-only.", "A CD-ROM is read-only.", "The BIOS is in ROM."], "y": "RAM is read-write memory."}], SRC),
   num("s3-10-units", 1, "Convert {v} {X.f} to {X.t}.", "storageConvert(v, X.f, X.t)",
       ["{1} {X.f} = {storageFactor(X.f, X.t)} {X.t}.", "{v} {X.f} = {answer} {X.t}."],
       vars={"v": {"int": [2, 16]}, "X": {"pick": [{"f": "KB", "t": "byte"}, {"f": "MB", "t": "KB"}, {"f": "GB", "t": "MB"}, {"f": "TB", "t": "GB"}, {"f": "byte", "t": "bit"}]}},
       misc=[("thousand", "X.f == 'byte' ? v * 10 : v * 1000", "{X.f == 'byte' ? 'One byte has ' + 8 + ' bits.' : 'Storage units go up in steps of ' + 1024 + ', not ' + 1000 + '.'}")],
       sources=SRC),
   num("s3-10-files", 2, "A song file is {s} MB. How many such songs fit in {v} GB?", "floor(v * 1024 / s)",
       ["{v} GB = {v} × {1024} = {v * 1024} MB.", "{v * 1024} ÷ {s} = {roundTo(v * 1024 / s, 0.01)}, so {answer} whole songs fit."],
       vars={"v": {"pick": [1, 2, 4, 8]}, "s": {"int": [3, 9]}},
       misc=[("thousand", "floor(v * 1000 / s)", "{1} GB = {1024} MB, not {1000}.")],
       sources=SRC, where=["(v * 1024) % s != 0"]),
   bank("s3-10-more", 3, "{X.q}", [
     {"q": "A computer becomes very slow when many programs are open. Which upgrade helps most?", "r": "more RAM", "w": ["a bigger screen", "more ROM", "a new mouse"],
      "e": ["Screen size does not affect speed.", "ROM holds start-up code only.", "A mouse is an input device."], "y": "More RAM holds more programs and data at once."},
     {"q": "Why is ROM needed at all, if RAM is faster to change?", "r": "The computer needs instructions that survive power-off to start up", "w": ["ROM stores games", "ROM is bigger than the hard disk", "RAM cannot be read"],
      "e": ["Games are stored on disks.", "ROM is small.", "RAM can be read and written."], "y": "Non-volatile start-up code."},
     {"q": "Why is primary storage called 'primary'?", "r": "The CPU accesses it directly", "w": ["It is the largest storage", "It is the cheapest", "It is used only first thing in the morning"],
      "e": ["Secondary storage is larger.", "It is relatively expensive.", "Not related to time of day."], "y": "Data must be in primary storage for the CPU to use it."}], SRC)],
  learn=learn(
    [("Memory the CPU uses directly",
      "Primary storage is memory the CPU can access directly. There are two kinds.\n"
      "• RAM (random access memory) holds the programs and data you are using now: the document you are typing, the browser, the game. It can be read and written. It is volatile: when the power goes off, its contents are lost.\n"
      "• ROM (read-only memory) holds instructions needed to start the computer (BIOS/firmware). It can only be read, and it is non-volatile."),
     ("Storage units",
      "• {8} bits = {1} byte (enough for one character).\n• {1} kilobyte (KB) = {1024} bytes.\n• {1} megabyte (MB) = {1024} KB.\n• {1} gigabyte (GB) = {1024} MB.\n• {1} terabyte (TB) = {1024} GB.\n"
      "Each unit is {1024} ({2} to the power {10}) times the one before, because computers count in binary."),
     ("How much RAM?",
      "If RAM is full, the computer moves data to the much slower disk, and everything slows down. More RAM lets more programs run at once smoothly.\n"
      "A phone might have {4} GB of RAM; a laptop {8} GB or more.\n"
      "Always save your work: unsaved work in RAM is lost in a power cut.")],
    key_words=[("RAM", "volatile read-write memory for programs and data in use"), ("ROM", "non-volatile read-only memory for start-up instructions"),
               ("volatile", "loses its contents when the power is off"), ("byte", "{8} bits")],
    examples=["{2} GB = {2048} MB", "{3} bytes = {24} bits", "Power cut: unsaved RAM data lost"],
    mistake=("{1} MB = {1000} KB", "{1} MB = {1024} KB",
             "Computer storage units go up in powers of {2}: {1024} = {2} to the power {10}.")))

# ---------------------------------------------------------------- 11. Secondary storage
L.lesson(D, S, 11, ("s3-11", "Secondary storage: types and choosing a device"), [10],
  "Secondary storage keeps programs and data permanently (non-volatile), even when the computer is off.\n"
  "• Magnetic: hard disk drive (HDD) — large capacity, cheap per GB, has moving parts.\n"
  "• Solid state: SSD, USB flash drive, memory card — no moving parts, fast, robust, more expensive per GB.\n"
  "• Optical: CD (about 700 MB), DVD (about 4.7 GB), Blu-ray (25 GB or more) — read by a laser.\n"
  "• Cloud storage: files kept on remote servers, reached through the internet.\n"
  "Choose by capacity, speed, cost, portability, durability and reliability.",
  worked({"f": 650, "n": 12},
         "A school wants to give each of {n} pupils a {f} MB video. Will one {4.7} GB DVD hold a copy for all of them?",
         ["Total = {n} × {f} = {n * f} MB.", "{4.7} GB = {4.7} × {1024} ≈ {roundTo(4.7 * 1024, 1)} MB.", "{n * f} MB is more than {roundTo(4.7 * 1024, 1)} MB, so one DVD is not enough."],
         "No: {n * f} MB > {roundTo(4.7 * 1024, 1)} MB", checks=["n * f > 4.7 * 1024"]),
  [card("c3s11-1", "Secondary storage is permanent (non-volatile).",
        ["Files on a USB drive stay after unplugging."], "s3-11-type"),
   card("c3s11-2", "Magnetic, solid state, optical and cloud are the main types.",
        ["HDD: magnetic; SSD: solid state; DVD: optical"], "s3-11-fit"),
   card("c3s11-3", "Choose a device by capacity, speed, cost and portability.",
        ["Backing up many photos: an external hard disk"], "s3-11-choose")],
  [bank("s3-11-type", 1, "What type of storage is this? {X.q}", [
     {"q": "a USB flash drive", "r": "solid state", "w": ["magnetic", "optical", "primary (RAM)"],
      "e": ["It has no magnetic disk.", "No laser reads it.", "It keeps data without power."], "y": "Flash memory chips: solid state."},
     {"q": "a DVD", "r": "optical", "w": ["magnetic", "solid state", "primary (ROM)"],
      "e": ["No magnetism is used.", "It has no chips.", "It is removable secondary storage."], "y": "A laser reads pits on the disc."},
     {"q": "a hard disk drive (HDD)", "r": "magnetic", "w": ["optical", "solid state", "cloud"],
      "e": ["No laser is used.", "It has spinning platters.", "It is inside or attached to the computer."], "y": "Data is stored magnetically on spinning platters."}], SRC),
   num("s3-11-fit", 2, "How many {f} MB photos can be stored on a {v} GB memory card?", "floor(v * 1024 / f)",
       ["{v} GB = {v * 1024} MB.", "{v * 1024} ÷ {f} = {roundTo(v * 1024 / f, 0.01)}: {answer} whole photos."],
       vars={"v": {"pick": [2, 4, 8, 16]}, "f": {"int": [3, 7]}},
       misc=[("thousand", "floor(v * 1000 / f)", "{1} GB = {1024} MB.")],
       sources=SRC, where=["(v * 1024) % f != 0", "floor(v * 1000 / f) != floor(v * 1024 / f)"]),
   bank("s3-11-choose", 2, "Which storage is best? {X.q}", [
     {"q": "Carrying homework between home and school every day", "r": "a USB flash drive", "w": ["a desktop hard disk", "a stack of DVDs", "ROM"],
      "e": ["Too big to carry daily.", "DVDs are slow to write and scratch easily.", "ROM cannot be written."], "y": "Small, light, robust, rewritable."},
     {"q": "Backing up thousands of family photos cheaply", "r": "an external hard disk", "w": ["a single CD", "RAM", "the CPU cache"],
      "e": ["A CD holds only about 700 MB.", "RAM is volatile.", "Cache is tiny and volatile."], "y": "Large capacity at low cost per GB."},
     {"q": "Opening files from any computer in the world with internet", "r": "cloud storage", "w": ["a hard disk inside one PC", "a CD in a drawer", "ROM"],
      "e": ["It stays in one computer.", "It must be carried.", "ROM is read-only."], "y": "Files are on remote servers reached online."}], SRC),
   bank("s3-11-compare", 3, "{X.q}", [
     {"q": "Why do many new laptops use an SSD instead of an HDD?", "r": "An SSD is faster and has no moving parts, so it is more robust", "w": ["An SSD is always cheaper per GB", "An SSD holds data only while switched on", "An HDD cannot store files"],
      "e": ["SSDs usually cost more per GB.", "SSDs are non-volatile.", "HDDs store files well."], "y": "Speed and durability."},
     {"q": "Which is a disadvantage of cloud storage in places with poor internet?", "r": "Files may be slow or impossible to reach without a connection", "w": ["It cannot store photos", "It is volatile", "It is made of magnetic tape"],
      "e": ["It stores any files.", "Cloud data is kept permanently.", "Users do not see the hardware."], "y": "Cloud needs a reliable internet connection."},
     {"q": "Why is a DVD a poor choice for daily backups?", "r": "It holds little, is slow to write and many cannot be rewritten", "w": ["It holds more than a hard disk", "It loses data without power", "It cannot be read by a laser"],
      "e": ["It holds much less.", "Optical discs are non-volatile.", "That is exactly how it is read."], "y": "Capacity and convenience matter for backups."}], SRC)],
  learn=learn(
    [("Keeping data for later",
      "RAM forgets everything when the power goes off, so computers also need secondary storage: devices that keep programs and files permanently (non-volatile). Your installed programs, documents, photos and videos live there."),
     ("Types of secondary storage",
      "• Magnetic: the hard disk drive (HDD) stores data on spinning platters. Large and cheap, but has moving parts that can break if dropped.\n"
      "• Solid state: SSDs, USB flash drives and memory cards use chips with no moving parts. Fast, light and robust, but cost more per GB.\n"
      "• Optical: CDs (about {700} MB), DVDs (about {4.7} GB) and Blu-ray discs are read by a laser.\n"
      "• Cloud: files stored on remote servers, reached through the internet."),
     ("Choosing a device",
      "Ask: How much must it hold (capacity)? How fast? How much does it cost? Does it need to be carried (portability)? Will it survive knocks (durability)?\n"
      "• Homework between home and school: a USB flash drive.\n• Big family photo backup: an external hard disk.\n• Sharing with others anywhere: the cloud (if the internet is good).")],
    key_words=[("secondary storage", "non-volatile storage for programs and data"), ("HDD", "hard disk drive, magnetic"), ("SSD", "solid-state drive, flash chips"),
               ("cloud storage", "storage on remote servers reached online"), ("capacity", "how much data a device can hold")],
    examples=["USB drive: solid state, portable", "DVD: optical, about {4.7} GB", "External HDD: cheap backup"],
    mistake=("A CD can store {100} GB of videos", "A CD holds about {700} MB",
             "Optical discs are small in capacity compared with hard disks.")))
