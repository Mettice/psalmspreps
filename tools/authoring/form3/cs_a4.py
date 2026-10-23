"""Form 3 Computer Science, Term 1, rows 12-13 (other internal components, ports). Run: python tools/authoring/form3/cs_a4.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"
SRC = ["hardware"]

# ---------------------------------------------------------------- 12. Other internal components
L.lesson(D, S, 12, ("s3-12", "Other internal components: motherboard, power supply, cards, cooling"), [8],
  "Inside the system unit:\n"
  "• Motherboard: the main circuit board; it connects the CPU, RAM, storage and expansion cards through buses (pathways for data).\n"
  "• Power supply unit (PSU): converts mains AC electricity into the low DC voltages the parts need.\n"
  "• Expansion cards: graphics card (GPU, for images and video), sound card, network interface card (NIC, for wired or wireless networking).\n"
  "• Cooling: heat sinks and fans (or liquid cooling) carry heat away from the CPU and GPU.\n"
  "• CMOS battery: keeps the clock and BIOS settings when the computer is off.",
  worked({},
         "A computer's fan stops working. What problem may follow, and why?",
         ["The CPU produces heat when it works.", "Without the fan, heat is not carried away, so the CPU gets too hot.", "It may slow down to protect itself, freeze, or be damaged."],
         "Overheating: slowing down, crashing or damage"),
  [card("c3s12-1", "The motherboard connects all the parts.",
        ["CPU, RAM and cards plug into it."], "s3-12-part"),
   card("c3s12-2", "The power supply changes mains AC into low-voltage DC.",
        ["Mains is about {220} V; parts use {12} V or less."], "s3-12-psu"),
   card("c3s12-3", "Fans and heat sinks stop the processor overheating.",
        ["Dust in the fans makes a computer hot and slow."], "s3-12-cool")],
  [bank("s3-12-part", 1, "Which component does this? {X.q}", [
     {"q": "It is the main circuit board that connects all the other parts.", "r": "motherboard", "w": ["power supply unit", "graphics card", "hard disk"],
      "e": ["The PSU provides power.", "The graphics card makes images.", "The hard disk stores data."], "y": "Everything plugs into the motherboard."},
     {"q": "It processes images and video for the screen.", "r": "graphics card (GPU)", "w": ["sound card", "network card", "CMOS battery"],
      "e": ["The sound card handles audio.", "The network card handles connections.", "The CMOS battery keeps settings."], "y": "Gamers and video editors need a good GPU."},
     {"q": "It lets the computer connect to a network.", "r": "network interface card (NIC)", "w": ["graphics card", "power supply unit", "heat sink"],
      "e": ["The GPU handles graphics.", "The PSU provides power.", "The heat sink cools the CPU."], "y": "Wired (Ethernet) or wireless (Wi-Fi) connections."}], SRC),
   bank("s3-12-psu", 1, "{X.q}", [
     {"q": "What does the power supply unit do?", "r": "Changes mains AC electricity into low-voltage DC for the components", "w": ["Stores files", "Makes images", "Cools the processor"],
      "e": ["Storage devices store files.", "The graphics card makes images.", "Fans and heat sinks cool."], "y": "Components need steady low-voltage DC."},
     {"q": "Why does a desktop computer keep the right time after being switched off?", "r": "A small CMOS battery on the motherboard powers the clock", "w": ["The hard disk counts the time", "The mouse remembers it", "The monitor stores it"],
      "e": ["The disk stores files, not a running clock.", "The mouse is an input device.", "The monitor is an output device."], "y": "The coin battery keeps the clock and settings."},
     {"q": "What is a bus on the motherboard?", "r": "a set of pathways that carry data between components", "w": ["a vehicle for computers", "a type of virus", "a cooling fan"],
      "e": ["It is not a vehicle.", "Not malware.", "Not a fan."], "y": "Data travels along buses between CPU, RAM and devices."}], SRC),
   bank("s3-12-cool", 2, "{X.q}", [
     {"q": "Why does a CPU have a heat sink and fan?", "r": "To carry away heat so the CPU does not overheat", "w": ["To make the computer louder", "To store data", "To charge the battery"],
      "e": ["Noise is a side effect.", "They do not store data.", "They do not charge anything."], "y": "Overheating slows or damages the CPU."},
     {"q": "A computer in a dusty room often shuts down suddenly. A likely cause is…", "r": "dust blocking the fans, causing overheating", "w": ["too much RAM", "a new keyboard", "a clean screen"],
      "e": ["More RAM does not cause shutdowns.", "Keyboards do not cause this.", "A clean screen is not a cause."], "y": "Clean the fans and vents regularly."},
     {"q": "Which part would a video editor most likely upgrade for smoother video?", "r": "the graphics card", "w": ["the CMOS battery", "the case colour", "the power cable length"],
      "e": ["The CMOS battery keeps the clock.", "Colour does not affect performance.", "Cable length is irrelevant."], "y": "The GPU processes images and video."}], SRC),
   bank("s3-12-fault", 3, "Which component is most likely faulty? {X.q}", [
     {"q": "The computer shows no lights and no fans spin when switched on, although the socket works.", "r": "the power supply unit", "w": ["the graphics card", "the hard disk", "the keyboard"],
      "e": ["A faulty GPU would still let fans spin.", "Fans would still spin.", "A keyboard fault does not stop power."], "y": "No power to any part points to the PSU."},
     {"q": "The date and time reset to the year 2000 every time the computer is turned on.", "r": "the CMOS battery", "w": ["the CPU", "the monitor", "the mouse"],
      "e": ["A CPU fault would stop the computer.", "The monitor only displays.", "The mouse is an input device."], "y": "A flat CMOS battery loses the clock settings."},
     {"q": "The computer works, but there is no Wi-Fi or network connection on any website.", "r": "the network interface card (or its driver)", "w": ["the RAM", "the power supply", "the fan"],
      "e": ["RAM faults cause crashes, not just no network.", "The computer has power.", "The fan does not affect networking."], "y": "Networking depends on the NIC."}], SRC)],
  learn=learn(
    [("The motherboard and buses",
      "Open a desktop computer's case and the biggest circuit board is the motherboard. The CPU, RAM, storage connectors and expansion slots are all on it.\n"
      "Buses are sets of tiny copper pathways carrying data, addresses and control signals between these parts. A small CMOS battery keeps the clock and start-up settings."),
     ("Power and cards",
      "The power supply unit (PSU) takes mains electricity (about {220} V AC in Cameroon) and turns it into the low, steady DC voltages the parts need. A surge protector or UPS protects it from power cuts and spikes.\n"
      "Expansion cards add abilities:\n• graphics card (GPU): images, video and games;\n• sound card: audio;\n• network interface card (NIC): wired or Wi-Fi connections."),
     ("Keeping cool",
      "The CPU and GPU produce a lot of heat. Heat sinks (metal fins) and fans carry it away; some computers use liquid cooling.\n"
      "If the fans are blocked by dust, the computer overheats, slows down, freezes or shuts off. Keep vents clear and clean dust regularly.")],
    key_words=[("motherboard", "the main circuit board connecting all components"), ("bus", "a set of pathways carrying data between components"),
               ("power supply unit", "converts mains AC to low-voltage DC"), ("expansion card", "a board added to give extra abilities"), ("heat sink", "metal fins that carry heat away")],
    examples=["GPU: games and video", "NIC: Wi-Fi", "PSU: power", "CMOS battery: clock"],
    mistake=("The power supply stores files when the computer is off", "The power supply only provides electricity; files are on storage devices",
             "Each component has its own job.")))

# ---------------------------------------------------------------- 13. Ports
L.lesson(D, S, 13, ("s3-13", "Computer ports and connectors"), [12],
  "A port is a socket where a device is connected to the computer.\n"
  "• USB (Universal Serial Bus): keyboards, mice, flash drives, printers, phones; USB-C is small and reversible and can also charge.\n"
  "• HDMI: high-definition video and sound to monitors, TVs and projectors. VGA: older analogue video port.\n"
  "• Ethernet (RJ45): wired network/internet cable.\n• Audio jacks (3.5 mm): headphones and microphones.\n• Power port: connects the charger or power cable.\n"
  "Data transfer speed is measured in bits or bytes per second; transfer time = file size ÷ transfer speed.",
  worked({"f": 600, "r": 40},
         "A {f} MB video is copied to a flash drive through a USB port that transfers {r} MB/s. How long does it take?",
         ["Time = size ÷ speed.", "= {f} ÷ {r} = {f / r} s."], "{f / r} s", checks=["f / r == 15"]),
  [card("c3s13-1", "Each port is designed for certain connections.",
        ["HDMI to the projector; USB to the flash drive"], "s3-13-which"),
   card("c3s13-2", "USB connects many devices and can charge them.",
        ["Phones, printers, keyboards"], "s3-13-usb"),
   card("c3s13-3", "Transfer time = file size ÷ transfer speed.",
        ["{100} MB at {20} MB/s: {5} s"], "s3-13-time")],
  [bank("s3-13-which", 1, "Which port would you use? {X.q}", [
     {"q": "To connect a laptop to a projector for a class presentation with sound.", "r": "HDMI", "w": ["Ethernet", "3.5 mm audio jack", "power port"],
      "e": ["Ethernet is for networking.", "The audio jack carries sound only.", "The power port is for charging."], "y": "HDMI carries video and sound."},
     {"q": "To plug in a network cable from the school router.", "r": "Ethernet (RJ45)", "w": ["HDMI", "USB", "VGA"],
      "e": ["HDMI is for video.", "USB is for devices.", "VGA is old video."], "y": "Wired networking uses Ethernet."},
     {"q": "To connect a flash drive.", "r": "USB", "w": ["HDMI", "Ethernet", "audio jack"],
      "e": ["HDMI is for displays.", "Ethernet is for networks.", "The audio jack is for sound."], "y": "Flash drives use USB."}], SRC),
   bank("s3-13-usb", 1, "{X.q}", [
     {"q": "What does USB stand for?", "r": "Universal Serial Bus", "w": ["Universal System Battery", "United Storage Board", "Ultra Speed Byte"],
      "e": ["Not a battery.", "Not a board.", "Not a unit."], "y": "A universal way to connect many devices."},
     {"q": "Which is an advantage of USB-C?", "r": "It is reversible and can carry data, video and power", "w": ["It only works with mice", "It is the oldest kind of port", "It cannot charge devices"],
      "e": ["It works with many devices.", "It is newer.", "It can charge."], "y": "One small connector for many uses."},
     {"q": "Which device usually connects through a 3.5 mm jack?", "r": "headphones", "w": ["a printer", "a projector", "a network cable"],
      "e": ["Printers use USB or Wi-Fi.", "Projectors use HDMI or VGA.", "Network cables use Ethernet."], "y": "The jack carries audio."}], SRC),
   num("s3-13-time", 2, "A {f} MB file is copied at {r} MB/s. How many seconds does it take?", "f / r",
       ["Time = size ÷ speed = {f} ÷ {r}.", "= {answer} s."],
       vars={"r": {"pick": [10, 20, 25, 40, 50]}, "k": {"int": [2, 40]}, "f": {"expr": "r * k"}},
       misc=[("mult", "f * r", "Time = size ÷ speed: divide.")],
       unit="s", sources=SRC),
   num("s3-13-gb", 3, "A {g} GB film is copied through a USB port at {r} MB/s. How many seconds does it take? (Use {1} GB = {1024} MB.)", "g * 1024 / r",
       ["{g} GB = {g * 1024} MB.", "Time = {g * 1024} ÷ {r} = {answer} s."],
       vars={"g": {"pick": [1, 2, 4]}, "r": {"pick": [16, 32, 64, 128]}},
       misc=[("nounit", "g / r", "Change GB to MB first."), ("thousand", "g * 1000 / r", "{1} GB = {1024} MB.")],
       unit="s", sources=SRC)],
  learn=learn(
    [("Ports connect devices",
      "Look at the side of a laptop or the back of a desktop: the sockets are ports. Each type of port is shaped for a certain kind of plug and job, so devices cannot easily be connected wrongly."),
     ("Common ports",
      "• USB: keyboards, mice, flash drives, printers, phones. USB-C is small, reversible and can carry data, video and power.\n"
      "• HDMI: digital video and sound to a monitor, TV or projector. VGA is an older video port still found on some projectors.\n"
      "• Ethernet ({'RJ45'}): a network cable to a router or switch.\n• Audio jacks ({3.5} mm): headphones and microphones.\n• Power or charging port."),
     ("How fast?",
      "Ports and cables move data at different speeds, measured in megabytes per second (MB/s) or megabits per second.\n"
      "Transfer time = file size ÷ transfer speed. A {600} MB video at {40} MB/s takes {15} s; the same file at {10} MB/s takes {60} s.\n"
      "Change units first: {1} GB = {1024} MB.")],
    key_words=[("port", "a socket for connecting a device"), ("USB", "Universal Serial Bus, for many devices"), ("HDMI", "a port for video and sound"),
               ("Ethernet", "a port for a wired network cable"), ("transfer speed", "how much data moves each second")],
    examples=["Flash drive: USB", "Projector: HDMI", "Router cable: Ethernet", "{200} MB at {50} MB/s: {4} s"],
    mistake=("Time = file size × speed", "Time = file size ÷ speed",
             "A faster port must give a shorter time, so divide by the speed.")))
