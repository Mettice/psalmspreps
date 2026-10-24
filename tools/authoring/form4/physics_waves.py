"""Form 4 Physics, Term 1, rows 8-15: properties of waves, wave phenomena, stationary waves, sound, vibrating
strings. Run: python tools/authoring/form4/physics_waves.py
Speed of sound in air taken as 340 m/s unless a question gives another value (TEACHER-REVIEW TR-P4-4)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order, match
from common import goal, bank

L.use_class("form-4", "Form 4")
D, S = "physics", "physics"
SRCW, SRCP, SRCS = ["waves"], ["wave-phenomena"], ["sound"]

# ---------------------------------------------------------------- 8. Classifying waves
KINDS = [
    {"q": "What is a wave?", "r": "A travelling disturbance that carries energy without carrying the material along",
     "w": ["A flow of matter from one place to another", "A store of energy that stays in one place", "A kind of force"],
     "e": ["A cork on water bobs up and down and stays in place, so the water is not carried along.",
           "A wave travels; it does not stay in one place.",
           "A wave carries energy; a force is a push or a pull."],
     "y": "Each particle vibrates about its own position and passes the energy on to the next."},
    {"q": "Which wave needs a material medium to travel through?", "r": "A sound wave",
     "w": ["A light wave", "A radio wave", "An X-ray"],
     "e": ["Light is electromagnetic and crosses the vacuum of space.",
           "Radio waves are electromagnetic and reach us from satellites through space.",
           "X-rays are electromagnetic and also cross a vacuum."],
     "y": "Sound is mechanical: it needs particles to pass the vibration on, so it cannot cross a vacuum."},
    {"q": "In a transverse wave, how do the particles move?", "r": "At right angles to the direction the wave travels",
     "w": ["Along the direction the wave travels", "In circles around the source", "They do not move at all"],
     "e": ["That describes a longitudinal wave, such as sound.",
           "The particles vibrate about a fixed position, backwards and forwards or up and down.",
           "The particles do move; it is the wave that carries energy through them."],
     "y": "Water ripples and light are transverse: the vibration is across the direction of travel."},
    {"q": "In a longitudinal wave, how do the particles move?", "r": "Backwards and forwards along the direction the wave travels",
     "w": ["At right angles to the direction of travel", "They travel along with the wave", "They stay completely still"],
     "e": ["That describes a transverse wave, such as a water ripple.",
           "The particles vibrate about fixed positions; only the energy travels on.",
           "The particles vibrate; otherwise no energy would be passed along."],
     "y": "Sound in air is longitudinal: the air is squeezed into compressions and stretched into rarefactions."},
    {"q": "Which list contains only mechanical waves?", "r": "Sound, water ripples and waves on a spring",
     "w": ["Light, radio and X-rays", "Sound, light and water ripples", "Radio, microwaves and sound"],
     "e": ["Those three are electromagnetic: they need no medium.",
           "Light is electromagnetic, not mechanical.",
           "Radio and microwaves are electromagnetic."],
     "y": "A mechanical wave needs a medium; sound, water ripples and spring waves all do."},
    {"q": "A sound wave travels through air. What is a compression?", "r": "A region where the air particles are pushed closer together",
     "w": ["A region where the particles are further apart than usual", "A point where the wave stops",
           "The highest point of the wave"],
     "e": ["That is a rarefaction, the opposite of a compression.",
           "The wave does not stop; compressions travel along with it.",
           "Highest and lowest points belong to a transverse wave, not to sound in air."],
     "y": "A longitudinal wave is a series of compressions and rarefactions passing through the medium."},
]

MEDIUM = [
    {"q": "A ringing electric bell is inside a glass jar and the air is slowly pumped out. What happens?",
     "r": "The sound fades away, but the bell can still be seen ringing",
     "w": ["The sound gets louder as the air is removed", "Both the sound and the light disappear", "Nothing changes"],
     "e": ["Fewer particles carry less sound, so it gets quieter, not louder.",
           "Light needs no medium: it still passes through the vacuum.",
           "Removing the air removes the medium that the sound needs."],
     "y": "Sound needs particles to pass the vibration on; light is electromagnetic and crosses a vacuum."},
    {"q": "Two astronauts stand side by side on the Moon, which has no atmosphere. Can they talk to each other directly?",
     "r": "No: there is no air to carry the sound, so they must use radio",
     "w": ["Yes, because they are very close together", "Yes, because sound travels faster in a vacuum",
           "No, because the Moon is too cold for sound"],
     "e": ["Distance is not the problem: there is no medium at all.",
           "Sound cannot travel in a vacuum at any speed.",
           "Temperature changes the speed of sound a little, but the real problem is that there is no air."],
     "y": "Sound is mechanical; radio waves are electromagnetic and cross the vacuum."},
    {"q": "Why can a diver under water hear a boat engine?",
     "r": "Water is a medium, and sound travels through it even faster than through air",
     "w": ["Sound travels only through air, so the diver hears it when surfacing", "The sound travels through the vacuum between the boat and the diver",
           "Water blocks sound completely"],
     "e": ["Liquids carry sound well; the diver hears it under water.",
           "There is no vacuum between a boat and a diver; the water is the medium.",
           "Water carries sound better than air does."],
     "y": "A mechanical wave travels through any medium with particles, and faster where they are closer together."},
    {"q": "Which of these could NOT reach us from a distant star?",
     "r": "The sound of the star",
     "w": ["Light from the star", "Radio waves from the star", "X-rays from the star"],
     "e": ["Light is electromagnetic and crosses the near-vacuum of space.",
           "Radio waves are electromagnetic and are received by radio telescopes.",
           "X-rays are electromagnetic and are detected by satellites."],
     "y": "Only electromagnetic waves cross space; sound needs a material medium."},
]

ENERGY = [
    {"q": 'A boat rocks as waves pass under it, but it does not travel towards the shore. What does this show?', "r": 'A wave carries energy along, while the water itself only vibrates about one place',
     "w": ['The waves have no energy', 'The water travels to the shore but the boat does not', 'The boat is too heavy to be moved by waves'],
     "e": ['The rocking of the boat shows that energy is arriving.', 'If the water flowed to the shore, the boat would be carried with it.', 'A light cork behaves in the same way: it bobs without travelling.'],
     "y": 'Each part of the water moves up and down and passes the energy to the next part.'},
    {"q": 'A loud sound shakes a window pane across the room. What has crossed the room?', "r": 'Energy, carried by the sound wave through the air',
     "w": ['Air blown from the source to the window', 'Particles shot out by the source', 'Nothing: the window shakes by itself'],
     "e": ['The air vibrates in place; it does not blow across the room.', 'No particles leave the source; the air already there passes the vibration on.', 'The window shakes only when the sound is made, so something reaches it.'],
     "y": 'A wave carries energy without carrying the medium along with it.'},
    {"q": 'Two waves on a pond have the same wavelength, but one is twice as tall. What does the taller one carry?', "r": 'More energy, because the energy of a wave grows with its amplitude',
     "w": ['Less energy, because it moves more slowly', 'The same energy, because the wavelength is the same', 'The same energy, but at a higher frequency'],
     "e": ['Both travel at the same speed in the same water; height does not slow a wave.', 'Wavelength is not what decides the energy; amplitude is.', 'Equal wavelength at equal speed means equal frequency.'],
     "y": 'A bigger amplitude means a bigger disturbance, and so more energy carried.'},
    {"q": 'Sunlight warms a roof. How has the energy reached it?', "r": 'As an electromagnetic wave, which needs no medium',
     "w": ['As hot air blown from the Sun', 'As a mechanical wave through space', 'By conduction along the atmosphere'],
     "e": ['No air travels from the Sun; space between is nearly empty.', 'A mechanical wave needs particles, and space has almost none.', 'There is nothing between the Sun and the atmosphere to conduct along.'],
     "y": 'Light is a wave that carries energy across a vacuum.'},
]

L.lesson(D, S, 8, ("p4-8", "Classify waves by the medium they need and by how the particles move"), [],
  "A wave is a travelling disturbance that carries energy from place to place without carrying the material along. "
  "Each particle vibrates about its own position and passes the energy on.\n"
  "By medium:\n"
  "• Mechanical waves need a material medium: sound, water ripples, waves on a rope or a spring.\n"
  "• Electromagnetic waves need no medium and cross a vacuum: light, radio, microwaves, X-rays.\n"
  "By the direction of vibration:\n"
  "• Transverse: particles vibrate at right angles to the direction of travel. Water ripples, light, a wave on a rope.\n"
  "• Longitudinal: particles vibrate along the direction of travel, making compressions and rarefactions. Sound, a wave along a spring.",
  worked({"z": 1},
         "Classify a sound wave travelling through air in two ways, and give a reason for each.",
         ["By medium: sound needs particles to pass the vibration on, so it cannot cross a vacuum. It is mechanical.",
          "By the direction of vibration: the air is squeezed and stretched along the direction the sound travels.",
          "That makes compressions (particles close together) and rarefactions (particles far apart)."],
         "a mechanical, longitudinal wave",
         checks=[]),
  [card("c4p8-1", "A wave carries energy, not matter: each particle vibrates about its own place.",
        ["a cork on a pond bobs up and down as the ripple passes; it is not carried to the shore"], "p4-8-kind"),
   card("c4p8-2", "Mechanical waves need a medium; electromagnetic waves cross a vacuum.",
        ["sound dies in a vacuum jar; light still passes through it"], "p4-8-medium"),
   card("c4p8-3", "Transverse: vibration across the travel. Longitudinal: vibration along it.",
        ["a rope wave is transverse; a sound wave is longitudinal"], "p4-8-direction")],
  [bank("p4-8-kind", 1, "{X.q}", KINDS, SRCW),
   bank("p4-8-medium", 1, "{X.q}", MEDIUM, SRCW),
   mcq("p4-8-direction", 2, "Classify {W.n} by the direction in which its particles vibrate.",
       "{W.t ? 'Transverse: the vibration is at right angles to the direction of travel' : 'Longitudinal: the vibration is along the direction of travel'}",
       [("{W.t ? 'Longitudinal: the vibration is along the direction of travel' : 'Transverse: the vibration is at right angles to the direction of travel'}", "swap"),
        ("Neither: the particles travel with the wave", "travel"), ("Both at the same time", "both")],
       ["{W.y}", "So the answer is: {answer}."],
       vars={"W": {"pick": [
           {"n": "a ripple on the surface of a pond", "t": True, "y": "A floating leaf moves up and down while the ripple moves outwards."},
           {"n": "a sound wave in air", "t": False, "y": "The air is squeezed and stretched along the direction the sound travels."},
           {"n": "a wave sent along a rope by shaking one end up and down", "t": True, "y": "Each part of the rope moves up and down while the wave runs along it."},
           {"n": "a wave sent along a spring by pushing one end in and out", "t": False, "y": "The coils bunch together and spread apart along the spring."},
           {"n": "a light wave", "t": True, "y": "Light is an electromagnetic wave, and its fields vibrate across the direction of travel."}]}},
       misc=[("swap", "{W.y}"), ("travel", "The particles vibrate about fixed positions; only the energy travels on."),
             ("both", "A wave is one or the other, not both.")],
       sources=SRCW),
   match("p4-8-match", 2, "Match each wave to the kind it is.",
         [("Sound in air", "Mechanical and longitudinal"), ("A ripple on water", "Mechanical and transverse"),
          ("Light from the Sun", "Electromagnetic and transverse"), ("A wave along a stretched rope", "Mechanical and transverse"),
          ("Radio waves from a mast", "Electromagnetic and transverse")],
         pick=3, sources=SRCW),
   bank("p4-8-energy", 3, "{X.q}", ENERGY, SRCW)],
  learn=learn(
    [goal("say what a wave carries, and classify any wave as mechanical or electromagnetic and as transverse or longitudinal.",
          "Form Three energy and the idea of vibration.",
          "Lesson {9} (the quantities that describe a wave) and Lesson {13} (sound as a longitudinal wave)."),
     ("Energy, not matter",
      "Drop a stone in a pond and ripples spread out. A cork floating on the water bobs up and down but stays where it is: "
      "the water is not carried to the edge. What travels is the disturbance, and with it the energy.\n"
      "In every wave, each particle vibrates about its own position and passes the energy to the next particle.\n"
      "Waves need a source that vibrates, and most need something to travel through."),
     ("Two ways to sort waves",
      "By the medium:\n"
      "• Mechanical waves need a material medium. Sound, water ripples and waves on a rope or spring are mechanical. "
      "A bell ringing in a jar goes silent as the air is pumped out.\n"
      "• Electromagnetic waves need no medium and cross a vacuum: light, radio, microwaves, X-rays. "
      "That is how sunlight reaches the Earth.\n"
      "By the direction of the vibration:\n"
      "• Transverse: the particles vibrate at right angles to the direction of travel. Ripples, rope waves and light.\n"
      "• Longitudinal: the particles vibrate along the direction of travel, making compressions (particles close together) "
      "and rarefactions (particles far apart). Sound in air, and a wave pushed along a spring.")],
    key_words=[("wave", "a travelling disturbance that carries energy without carrying matter"),
               ("mechanical wave", "a wave that needs a material medium"),
               ("transverse", "vibration at right angles to the direction of travel"),
               ("longitudinal", "vibration along the direction of travel"),
               ("compression", "a region where particles are pushed close together")],
    examples=["sound: mechanical, longitudinal", "light: electromagnetic, transverse", "a ripple: mechanical, transverse"],
    mistake=("sound can travel through space from a satellite", "sound needs a medium, so it cannot cross a vacuum",
             "Radio waves carry the message through space; a loudspeaker makes the sound in the air at the other end.")))

# ---------------------------------------------------------------- 9. Period, frequency, amplitude
L.lesson(D, S, 9, ("p4-9", "Use a displacement-time graph to find period, frequency and amplitude"), [8],
  "A displacement-time graph shows how one particle moves as time passes.\n"
  "• Amplitude a: the greatest displacement from the rest position, in metres (or cm). It is measured from the middle line to a crest, not from crest to trough.\n"
  "• Period T: the time for one complete vibration, in seconds. On the graph it is the time from one crest to the next.\n"
  "• Frequency f: the number of complete vibrations each second, in hertz (Hz).\n"
  "f = 1/T and T = 1/f.\n"
  "The energy a wave carries grows with its amplitude; a louder sound or a brighter light has a larger amplitude.",
  worked({"a": 4, "T": 0.2},
         "A displacement-time graph of a vibrating particle is shown. Find its amplitude, period and frequency.",
         ["Amplitude: the greatest displacement from the middle line is {a} cm.",
          "Period: one complete wave takes {T} s, read from one crest to the next.",
          "Frequency: f = {1} ÷ T = {1} ÷ {T}."],
         "amplitude {a} cm, period {T} s, frequency {waveT(T)} Hz",
         figure="waveFig(a, T, 2, 'Time', 's')",
         checks=["waveT(T) == 5"]),
  [card("c4p9-1", "Amplitude is measured from the middle line to a crest, not from crest to trough.",
        ["a graph reaching {4} cm above and {4} cm below the line has amplitude {4} cm"], "p4-9-amp"),
   card("c4p9-2", "The period is the time for one complete vibration; read it from crest to crest.",
        ["two complete waves in {0.4} s means T = {0.2} s"], "p4-9-period"),
   card("c4p9-3", "f = {1}/T and T = {1}/f; frequency is in hertz.",
        ["T = {0.2} s gives f = {5} Hz"], "p4-9-freq")],
  [num("p4-9-amp", 1, "From the displacement-time graph, what is the amplitude of the vibration, in cm?",
       "a",
       ["Amplitude is the greatest displacement from the middle line.", "The graph reaches {a} cm above the line, so the amplitude is {answer} cm."],
       vars={"a": {"int": [2, 8]}, "T": {"pick": [0.2, 0.4, 0.5, 1, 2]}},
       figure="waveFig(a, T, 2, 'Time', 's')",
       misc=[("peak2peak", "2 * a", "That is the distance from a crest to a trough: the amplitude is half of it."),
             ("period", "T", "{T} s is the period, read along the time axis.")],
       sources=SRCW, unit="cm"),
   num("p4-9-period", 1, "From the graph, what is the period of the vibration, in seconds?",
       "T",
       ["The period is the time for one complete wave.", "The graph shows {2} complete waves in {2 * T} s, so T = {answer} s."],
       vars={"a": {"int": [2, 8]}, "T": {"pick": [0.2, 0.25, 0.4, 0.5, 1, 2]}},
       figure="waveFig(a, T, 2, 'Time', 's')",
       misc=[("two", "2 * T", "{2 * T} s is the time for TWO complete waves; one takes half of it."),
             ("amp", "a", "{a} cm is the amplitude, read up the displacement axis.")],
       sources=SRCW, unit="s"),
   num("p4-9-freq", 1, "A vibration has a period of {T} s. Find its frequency, in hertz.",
       "waveT(T)",
       ["f = {1} ÷ T.", "f = {1} ÷ {T} = {answer} Hz."],
       vars={"T": {"pick": [0.01, 0.02, 0.025, 0.05, 0.1, 0.2, 0.25, 0.5, 2, 4]}},
       misc=[("same", "T", "Frequency is the reciprocal of the period, not the period itself."),
             ("times", "roundTo(T * 100, 0.01)", "Divide {1} by the period; do not multiply.")],
       sources=SRCW, unit="Hz"),
   num("p4-9-period2", 2, "A tuning fork vibrates at {f} Hz. Find its period, in seconds.",
       "roundTo(waveT(f), 0.00001)",
       ["T = {1} ÷ f.", "T = {1} ÷ {f} = {answer} s."],
       vars={"f": {"pick": [2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200, 250, 500]}},
       misc=[("same", "f", "The period is the reciprocal of the frequency."),
             ("sixty", "roundTo(60 / f, 0.00001)", "Frequency is counted per second, so divide {1} by it, not {60}.")],
       sources=SRCW, unit="s"),
   num("p4-9-count", 3, "A particle makes {n} complete vibrations in {t} seconds. Find its frequency, in hertz.",
       "n / t",
       ["Frequency is the number of complete vibrations each second.", "f = {n} ÷ {t} = {answer} Hz."],
       vars={"t": {"pick": [2, 4, 5, 8, 10, 20]}, "f0": {"pick": [2, 3, 4, 5, 10, 15, 20, 25]}, "n": {"expr": "f0 * t"}},
       misc=[("swap", "t / n", "Divide the number of vibrations by the time, not the other way round."),
             ("period", "roundTo(t / n, 0.0001)", "That is the period, the time for ONE vibration.")],
       sources=SRCW, unit="Hz")],
  learn=learn(
    [goal("read amplitude and period from a displacement-time graph and change between period and frequency.",
          "Lesson {8} (what a wave is) and Form Three measurement of time.",
          "Lesson {10}, where wavelength and the equation v = fλ are added."),
     ("Reading the graph",
      "A displacement-time graph follows one particle as time passes. Time runs across; displacement from the rest "
      "position runs up and down.\n"
      "• Amplitude a is the greatest displacement from the middle line. If the curve reaches {4} cm above and {4} cm below, "
      "the amplitude is {4} cm, not {8} cm.\n"
      "• Period T is the time for one complete vibration: from one crest to the next crest, or from one trough to the next. "
      "If {2} complete waves take {0.4} s, then T = {0.2} s.\n"
      "A bigger amplitude means the wave carries more energy: a louder sound, a brighter light, a taller sea wave."),
     ("Period and frequency",
      "Frequency f is the number of complete vibrations each second, measured in hertz (Hz). One hertz is one vibration per second.\n"
      "Period and frequency are reciprocals:\n"
      "• f = {1} ÷ T  • T = {1} ÷ f\n"
      "Examples:\n"
      "• T = {0.2} s gives f = {1} ÷ {0.2} = {5} Hz.\n"
      "• f = {50} Hz gives T = {1} ÷ {50} = {0.02} s.\n"
      "If a particle makes {60} vibrations in {4} s, then f = {60} ÷ {4} = {15} Hz, and T = {1} ÷ {15} s.")],
    key_words=[("amplitude", "the greatest displacement from the rest position"),
               ("period (T)", "the time for one complete vibration, in seconds"),
               ("frequency (f)", "vibrations per second, in hertz"),
               ("displacement", "how far a particle is from its rest position, and in which direction")],
    examples=["T = {0.5} s → f = {2} Hz", "f = {25} Hz → T = {0.04} s", "crest {3} cm above the line → amplitude {3} cm"],
    mistake=("amplitude = the height from a crest to a trough", "amplitude = from the middle line to a crest",
             "Crest to trough is twice the amplitude.")))

# ---------------------------------------------------------------- 10. Wavelength, wave speed, v = fλ
L.lesson(D, S, 10, ("p4-10", "Find wavelength and wave speed; use v = fλ"), [9],
  "A displacement-distance graph (a wave profile) is a snapshot of the whole wave at one instant: distance runs across.\n"
  "Wavelength λ is the distance between two successive points in step, for example crest to crest, in metres.\n"
  "Wave speed v is how fast the wave travels, in m/s.\n"
  "In one period the wave moves one wavelength, so v = λ/T, that is v = fλ.\n"
  "Rearranged: f = v/λ and λ = v/f.\n"
  "In a ripple tank a vibrating bar makes straight wavefronts and a dipper makes circular ones. A wavefront joins points in step, "
  "and the distance between two neighbouring wavefronts is one wavelength.",
  worked({"f": 50, "lam": 0.4},
         "A wave has a frequency of {f} Hz and a wavelength of {lam} m. Find its speed.",
         ["v = fλ.", "v = {f} × {lam}.", "= {waveSpeed(f, lam)} m/s."],
         "{waveSpeed(f, lam)} m/s",
         checks=["waveSpeed(f, lam) == 20"]),
  [card("c4p10-1", "Wavelength is the distance from one crest to the next, read off a displacement-distance graph.",
        ["crests {2} m apart means λ = {2} m"], "p4-10-lambda"),
   card("c4p10-2", "v = fλ: speed = frequency × wavelength.",
        ["f = {50} Hz and λ = {0.4} m give v = {20} m/s"], "p4-10-v"),
   card("c4p10-3", "Rearranged: f = v/λ and λ = v/f.",
        ["v = {340} m/s and f = {170} Hz give λ = {2} m"], "p4-10-lam")],
  [num("p4-10-lambda", 1, "From the displacement-distance graph, what is the wavelength, in metres?",
       "lam",
       ["Wavelength is the distance from one crest to the next.", "The graph shows {2} complete waves in {2 * lam} m, so λ = {answer} m."],
       vars={"a": {"int": [2, 6]}, "lam": {"pick": [0.4, 0.5, 1, 2, 2.5, 4]}},
       figure="waveFig(a, lam, 2, 'Distance', 'm')",
       misc=[("two", "2 * lam", "{2 * lam} m covers TWO complete waves."),
             ("amp", "a", "{a} cm is the amplitude, measured up the displacement axis.")],
       sources=SRCW, unit="m"),
   num("p4-10-v", 1, "A wave of frequency {f} Hz has wavelength {lam} m. Find its speed, in m/s.",
       "waveSpeed(f, lam)",
       ["v = fλ.", "v = {f} × {lam} = {answer} m/s."],
       vars={"f": {"pick": [2, 4, 5, 10, 20, 25, 50, 100, 200, 500]}, "lam": {"pick": [0.2, 0.4, 0.5, 1, 1.5, 2, 3, 4]}},
       misc=[("div", "roundTo(waveFreq(f, lam), 0.001)", "Multiply the frequency by the wavelength."),
             ("add", "f + lam", "v = fλ is a product, not a sum.")],
       sources=SRCW, unit="m/s"),
   # audible frequencies only (about 20 Hz to 20 kHz), paired with the speed in that medium
   num("p4-10-lam", 2, "A sound of frequency {f} Hz travels through {V.n} at {V.v} m/s. Find its wavelength, in metres.",
       "waveLen(V.v, f)",
       ["v = fλ, so λ = v ÷ f.", "λ = {V.v} ÷ {f} = {answer} m."],
       vars={"V": {"pick": [{"n": "air", "v": 330}, {"n": "air", "v": 340}, {"n": "sea water", "v": 1500}]},
             "f": {"pick": [20, 25, 30, 40, 50, 60, 75, 100, 125, 150, 170, 200, 250, 300, 375, 500, 750, 1000]}},
       misc=[("mult", "waveSpeed(f, V.v)", "Divide the speed by the frequency."),
             ("swap", "roundTo(f / V.v, 0.0001)", "λ = v ÷ f, not f ÷ v.")],
       sources=SRCW, unit="m", where=["V.v % f == 0"]),
   num("p4-10-f", 2, "A wave travels at {v} m/s with a wavelength of {lam} m. Find its frequency, in hertz.",
       "waveFreq(v, lam)",
       ["v = fλ, so f = v ÷ λ.", "f = {v} ÷ {lam} = {answer} Hz."],
       vars={"lam": {"pick": [0.5, 1, 2, 2.5, 4, 5]}, "f0": {"pick": [2, 5, 10, 20, 40, 50, 100, 170]}, "v": {"expr": "waveSpeed(f0, lam)"}},
       misc=[("mult", "waveSpeed(v, lam)", "Divide the speed by the wavelength."),
             ("swap", "roundTo(lam / v, 0.0001)", "f = v ÷ λ, not λ ÷ v.")],
       sources=SRCW, unit="Hz"),
   num("p4-10-tank", 3, "In a ripple tank a bar vibrates {n} times in {t} s and the wavefronts are {lam} cm apart. Find the speed of the ripples, in cm/s.",
       "waveSpeed(n / t, lam)",
       ["Frequency f = {n} ÷ {t} = {n / t} Hz.", "The distance between neighbouring wavefronts is the wavelength, {lam} cm.",
        "v = fλ = {n / t} × {lam} = {answer} cm/s."],
       vars={"t": {"pick": [2, 4, 5, 10]}, "f0": {"pick": [4, 5, 8, 10, 12, 20]}, "n": {"expr": "f0 * t"}, "lam": {"pick": [1.5, 2, 2.5, 3, 4, 5]}},
       misc=[("nof", "waveSpeed(n, lam)", "{n} is the number of vibrations in {t} s: divide by the time to get the frequency."),
             ("div", "roundTo(waveFreq(n / t, lam), 0.001)", "v = fλ is a product.")],
       sources=SRCW, unit="cm/s")],
  learn=learn(
    [goal("read a wavelength from a wave profile and use v = fλ to find speed, frequency or wavelength.",
          "Lesson {9} (period, frequency and amplitude).",
          "Lesson {11} (what happens when waves meet an obstacle) and Lesson {14} (the speed of sound)."),
     ("Wavelength and wave profile",
      "A displacement-time graph follows one particle. A displacement-distance graph, or wave profile, is a photograph of "
      "the whole wave at one instant, with distance running across.\n"
      "Wavelength λ is the distance between two successive points that are in step: crest to crest, or trough to trough. "
      "It is measured in metres.\n"
      "In a ripple tank, a vibrating bar makes straight wavefronts and a vibrating dipper makes circular ones. "
      "A wavefront joins points that are in step, such as the tops of the ripples, and neighbouring wavefronts are one wavelength apart."),
     ("The wave equation",
      "In one period T the wave moves forward exactly one wavelength λ.\n"
      "speed = distance ÷ time = λ ÷ T, and since f = {1} ÷ T:\n"
      "v = fλ.\n"
      "Rearranged: f = v ÷ λ and λ = v ÷ f.\n"
      "Examples:\n"
      "• f = {50} Hz, λ = {0.4} m: v = {50} × {0.4} = {20} m/s.\n"
      "• Sound at {340} m/s with f = {170} Hz: λ = {340} ÷ {170} = {2} m.\n"
      "Keep the units together: metres with hertz give metres per second.")],
    key_words=[("wavelength (λ)", "the distance between two successive points in step, such as crest to crest"),
               ("wave speed (v)", "how fast the wave travels, in m/s"),
               ("wavefront", "a line joining points of a wave that are in step"),
               ("ripple tank", "a shallow tank of water used to show wave behaviour")],
    examples=["v = {2} × {3} = {6} m/s", "λ = {340} ÷ {85} = {4} m", "f = {20} ÷ {0.5} = {40} Hz"],
    mistake=("v = f + λ", "v = fλ",
             "Speed is the frequency MULTIPLIED by the wavelength: one wavelength for every vibration each second.")))

# ---------------------------------------------------------------- 11. Reflection, refraction, diffraction, interference
PHEN = [
    {"q": "Straight water waves hit a straight barrier at an angle. What happens?", "r": "They are reflected, with the angle of reflection equal to the angle of incidence",
     "w": ["They pass straight through the barrier", "They stop at the barrier and disappear", "They bend around the barrier and carry on"],
     "e": ["A solid barrier does not let the waves through.",
           "The energy is turned back, not destroyed.",
           "Bending round an obstacle is diffraction, which needs a gap or an edge, not a long straight barrier."],
     "y": "At a reflection the wavelength and frequency stay the same; only the direction changes."},
    {"q": "Water waves pass from deep water into shallow water. What happens to them?", "r": "They slow down, the wavelength gets shorter and they bend towards the normal",
     "w": ["They speed up and the wavelength gets longer", "The frequency changes but the speed does not", "Nothing changes"],
     "e": ["Waves travel more slowly in shallow water, not faster.",
           "The frequency is set by the source and does not change; the speed does.",
           "The change of depth changes the speed, so something must change."],
     "y": "Refraction: f stays the same, v falls, so λ = v ÷ f falls too, and the waves bend."},
    {"q": "What is diffraction?", "r": "The spreading of waves as they pass through a gap or around an obstacle",
     "w": ["The bouncing of waves off a barrier", "The bending of waves when their speed changes", "The joining of two waves to make a bigger one"],
     "e": ["That is reflection.", "That is refraction.", "That is interference."],
     "y": "Diffraction spreads the wave; it is greatest when the gap is about the same size as the wavelength."},
    {"q": "When is diffraction through a gap greatest?", "r": "When the width of the gap is about the same as the wavelength",
     "w": ["When the gap is much wider than the wavelength", "When the gap is much narrower than the wavelength", "The width of the gap makes no difference"],
     "e": ["A wide gap lets most of the wave through almost straight, with only the edges spreading.",
           "A very narrow gap lets through little energy, though what passes does spread.",
           "The width of the gap compared with the wavelength is exactly what decides it."],
     "y": "Gap ≈ wavelength gives the widest spreading, which is why sound (long waves) bends round a doorway but light does not."},
    {"q": "Two waves meet crest to crest. What happens at that point?", "r": "Constructive interference: the displacements add, making a bigger wave",
     "w": ["Destructive interference: they cancel out", "The waves bounce off each other", "The waves stop"],
     "e": ["Cancelling happens when a crest meets a trough.",
           "Waves pass through each other; they do not bounce off each other.",
           "After meeting, each wave carries on as before."],
     "y": "Where two crests meet, the displacements add: that is constructive interference."},
    {"q": "Two identical waves meet crest to trough. What is heard or seen at that point?", "r": "Destructive interference: they cancel, giving a quiet or dark point",
     "w": ["A louder sound or a brighter light", "No change at all", "The waves change frequency"],
     "e": ["Louder or brighter is constructive interference, where crest meets crest.",
           "A crest meeting an equal trough gives zero displacement, which is a definite change.",
           "Interference does not change the frequency of either wave."],
     "y": "Equal and opposite displacements add to zero: a quiet point in sound, a dark fringe in light."},
]

DIFFRACT = [
    {"q": 'Why can you hear someone talking round the corner of a corridor, but not see them?', "r": "Sound has a wavelength about the size of the opening, so it diffracts strongly; light's wavelength is far smaller",
     "w": ['Sound travels faster than light', 'Light is absorbed by the wall but sound is not', 'Sound waves are longitudinal and light waves are not'],
     "e": ['Light travels nearly a million times faster than sound; speed is not what decides diffraction.', 'Both are stopped by a solid wall; the difference is how much each spreads at the corner.', 'Transverse waves diffract too: water ripples are transverse and diffract well.'],
     "y": 'Diffraction is greatest when the gap or obstacle is about the size of the wavelength.'},
    {"q": 'Straight water waves pass through a gap much wider than their wavelength. What is seen beyond the gap?', "r": 'The waves go through almost straight, with a little spreading only at the edges',
     "w": ['The waves spread out in a wide semicircle', 'The waves stop at the gap', 'The waves change their wavelength'],
     "e": ['Wide spreading needs a gap about the size of the wavelength.', 'The waves pass through; the barrier only blocks what hits it.', 'Diffraction changes the shape of the wavefronts, not the wavelength.'],
     "y": 'A wide gap diffracts little; the spreading grows as the gap narrows towards one wavelength.'},
    {"q": 'The gap in a ripple tank barrier is narrowed until it is about one wavelength wide. What happens to the ripples beyond it?', "r": 'They spread out in almost semicircular wavefronts',
     "w": ['They keep their straight shape', 'They are reflected back', 'They travel faster'],
     "e": ['Straight wavefronts pass a wide gap; a narrow gap spreads them.', 'The part that hits the barrier is reflected, but what goes through the gap spreads out.', 'The depth is unchanged, so the speed is unchanged.'],
     "y": 'Gap ≈ wavelength gives the widest diffraction, and the gap acts almost like a new source.'},
    {"q": 'Why does a radio with long waves work better than a television behind a hill?', "r": 'The longer radio waves diffract round the hill, while the shorter television waves do not',
     "w": ['Radio waves are stronger than television waves', 'Television waves are absorbed by soil', 'Radio waves travel faster than television waves'],
     "e": ['Strength is not what decides it; the wavelength compared with the obstacle is.', 'Both are reflected and absorbed at a hill; it is the diffraction that differs.', 'All electromagnetic waves travel at the same speed in air.'],
     "y": 'An obstacle diffracts a wave most when the wavelength is comparable with its size.'},
]

INTERFERE = [
    {"q": 'Two loudspeakers play the same steady note. Walking in front of them, a pupil hears loud and quiet places. Why?', "r": 'The two sound waves interfere: crest on crest gives a loud place, crest on trough a quiet one',
     "w": ['One speaker is louder than the other', 'The sound is reflected off the walls only', 'The speakers change frequency as the pupil walks'],
     "e": ['A louder speaker would make one side louder everywhere, not give a pattern of places.', 'The pattern is heard outdoors too, where there is little echo.', 'The note is steady; it is the difference in path length that changes as the pupil moves.'],
     "y": 'Sound from the two speakers travels different distances to each point, so it arrives in step or out of step.'},
    {"q": 'At a point, a crest from one wave arrives together with a crest from another. What happens there?', "r": 'Constructive interference: the displacements add, giving a bigger disturbance',
     "w": ['Destructive interference: they cancel out', 'The waves bounce off each other', 'The waves stop'],
     "e": ['Cancelling happens when a crest meets a trough.', 'Waves pass through each other; they do not bounce off each other.', 'After meeting, each wave carries on as before.'],
     "y": 'Where two waves arrive in step, their displacements add.'},
    {"q": 'Two identical waves arrive at a point exactly out of step, crest meeting trough. What is observed?', "r": 'Destructive interference: they cancel, giving a quiet or dark point',
     "w": ['A louder sound or a brighter light', 'No change at all', 'The waves change frequency'],
     "e": ['Louder or brighter is constructive interference, crest on crest.', 'A crest meeting an equal trough gives zero displacement, which is a definite change.', 'Interference does not change the frequency of either wave.'],
     "y": 'Equal and opposite displacements add to zero.'},
    {"q": 'What must be true of two sources if a steady interference pattern is to be seen?', "r": 'They must have the same frequency and keep a steady phase relationship',
     "w": ['They must have different frequencies', 'They must be at the same point', 'They must face in opposite directions'],
     "e": ['Different frequencies make a pattern that changes all the time, so nothing steady is seen.', 'Two sources at the same point cannot give different path lengths.', 'The direction they face does not decide whether the waves interfere.'],
     "y": 'Sources with the same frequency and a steady phase relationship are called coherent.'},
]

L.lesson(D, S, 11, ("p4-11", "Describe reflection, refraction, diffraction and interference of waves"), [10],
  "Reflection: a wave meets a barrier and is turned back. The angle of reflection equals the angle of incidence; "
  "the speed, frequency and wavelength do not change.\n"
  "Refraction: a wave crosses into a medium where it travels at a different speed. The frequency stays the same, "
  "so the wavelength changes (λ = v/f) and the wave bends, unless it meets the boundary along the normal. "
  "Water waves slow down in shallow water and bend towards the normal.\n"
  "Diffraction: a wave spreads out as it passes through a gap or round an obstacle. It is greatest when the gap is "
  "about the same width as the wavelength. Sound diffracts round a doorway; light hardly does, because its wavelength is tiny.\n"
  "Interference: two waves meeting add their displacements. Crest on crest gives a larger wave (constructive); "
  "crest on trough cancels (destructive).",
  worked({"z": 1},
         "Water waves travel from deep water into shallow water. Say what happens to the speed, the frequency, the wavelength and the direction.",
         ["The frequency is set by the source, so it does not change.",
          "Waves travel more slowly in shallow water, so the speed falls.",
          "From v = fλ, with f fixed and v smaller, the wavelength must get shorter.",
          "The part of each wavefront that reaches the shallow water first slows first, so the wavefront swings round towards the normal."],
         "f unchanged, v smaller, λ shorter, and the waves bend towards the normal",
         checks=[]),
  [card("c4p11-1", "Reflection turns a wave back: angle of reflection = angle of incidence, and λ and f are unchanged.",
        ["straight water waves hitting a straight barrier come back at the same angle"], "p4-11-which"),
   card("c4p11-2", "Refraction: f stays the same, v and λ change, and the wave bends.",
        ["in shallow water the ripples slow down and the wavefronts come closer together"], "p4-11-refract"),
   card("c4p11-3", "Diffraction spreads a wave through a gap; it is greatest when the gap ≈ the wavelength.",
        ["sound bends round a doorway; light does not, because its wavelength is far smaller"], "p4-11-diffract")],
  [bank("p4-11-which", 1, "{X.q}", PHEN, SRCP),
   num("p4-11-refract", 2, "Water waves of frequency {f} Hz travel at {v1} m/s in deep water. In shallow water the speed falls to {v2} m/s. Find the wavelength in the shallow water, in metres.",
       "waveLen(v2, f)",
       ["The frequency does not change at a boundary: it is still {f} Hz.", "λ = v ÷ f = {v2} ÷ {f}.", "λ = {answer} m."],
       vars={"f": {"pick": [2, 4, 5, 10, 20]}, "v1": {"pick": [20, 30, 40, 50, 60]}, "v2": {"pick": [10, 12, 15, 20, 24]}},
       misc=[("deep", "waveLen(v1, f)", "{v1} m/s is the speed in the DEEP water; use the shallow-water speed {v2} m/s."),
             ("freq", "roundTo(waveFreq(v2, f), 0.001)", "λ = v ÷ f: divide the speed by the frequency.")],
       sources=SRCP, unit="m", where=["v2 < v1", "waveLen(v2, f) != waveLen(v1, f)"]),
   bank("p4-11-diffract", 2, "{X.q}", DIFFRACT, SRCP),
   bank("p4-11-interfere", 2, "{X.q}", INTERFERE, SRCP),
   match("p4-11-match", 3, "Match each effect to what happens to the wave.",
         [("Reflection", "The wave is turned back; λ, f and v stay the same"),
          ("Refraction", "The speed changes, so λ changes and the wave bends"),
          ("Diffraction", "The wave spreads out through a gap or round an obstacle"),
          ("Constructive interference", "Two crests meet and the displacements add"),
          ("Destructive interference", "A crest meets a trough and they cancel")],
         pick=3, sources=SRCP)],
  learn=learn(
    [goal("describe what reflection, refraction, diffraction and interference do to a wave, and say which quantities change.",
          "Lesson {10} (v = fλ) and Form Three reflection of light.",
          "Lesson {12} (stationary waves, made by interference) and Lesson {13} (sound)."),
     ("Reflection and refraction",
      "Reflection: the wave meets a barrier and is turned back. The angle of reflection equals the angle of incidence. "
      "Nothing else changes: the speed, frequency and wavelength are the same as before.\n"
      "Refraction: the wave crosses into a medium where its speed is different. In a ripple tank, deep water to shallow "
      "water slows the ripples down.\n"
      "The frequency is fixed by the source and never changes at a boundary. So from v = fλ, if v falls then λ falls too: "
      "the wavefronts come closer together. If the wave meets the boundary at an angle, one end of each wavefront slows first "
      "and the wave bends, towards the normal when it slows down."),
     ("Diffraction and interference",
      "Diffraction: a wave spreads out as it passes through a gap or round the edge of an obstacle. "
      "The spreading is greatest when the gap is about the same width as the wavelength.\n"
      "Sound has wavelengths of about a metre, so it spreads round a doorway and you hear someone round a corner. "
      "Light has a wavelength of less than a thousandth of a millimetre, so it spreads far too little to see.\n"
      "Interference: where two waves meet, their displacements add.\n"
      "• Crest on crest, or trough on trough: constructive interference, a bigger wave. A loud sound or a bright fringe.\n"
      "• Crest on trough: destructive interference, and if the waves are equal they cancel. A quiet place or a dark fringe.")],
    key_words=[("reflection", "a wave turned back at a barrier"),
               ("refraction", "a wave bending because its speed changes"),
               ("diffraction", "spreading through a gap or round an obstacle"),
               ("interference", "two waves meeting and adding their displacements"),
               ("normal", "the line at right angles to a surface")],
    examples=["shallow water: v and λ fall, f stays", "sound round a doorway: diffraction", "two speakers: loud and quiet places"],
    mistake=("when a wave is refracted its frequency changes", "the frequency stays the same; the speed and wavelength change",
             "The source sets the frequency. At the boundary, v and λ change together so that v = fλ still holds.")))

# ---------------------------------------------------------------- 12. Stationary waves
STAND = [
    {"q": 'How does a stationary wave differ from a progressive wave?', "r": 'A stationary wave has fixed nodes and carries no energy along; a progressive wave carries energy forward',
     "w": ['A stationary wave has a higher frequency', 'A stationary wave has no amplitude', 'There is no difference; the names mean the same thing'],
     "e": ['The two waves that make a stationary wave have the same frequency as it does.', 'The antinodes have a large amplitude; only the nodes do not move.', 'They behave quite differently: one carries energy away, the other does not.'],
     "y": 'In a stationary wave the pattern stays where it is, with the energy stored in the vibration.'},
    {"q": 'What is needed to make a stationary wave?', "r": 'Two waves of the same frequency and amplitude travelling in opposite directions',
     "w": ['Two waves of different frequencies travelling the same way', 'One wave of very large amplitude', 'Two waves travelling the same way at different speeds'],
     "e": ['Different frequencies give a pattern that will not stay still.', 'A single wave travelling along is a progressive wave, however large.', 'Waves going the same way cannot make fixed nodes.'],
     "y": 'Usually a wave and its own reflection meet and interfere, giving fixed nodes and antinodes.'},
    {"q": 'In a stationary wave, how does the amplitude vary along the string?', "r": 'It is zero at the nodes and greatest at the antinodes',
     "w": ['It is the same everywhere, as in a progressive wave', 'It is greatest at the nodes', 'It falls steadily from one end to the other'],
     "e": ['Equal amplitude everywhere is what happens in a progressive wave.', 'A node is a point that never moves, so its amplitude is zero.', 'The amplitude rises and falls repeatedly along the string.'],
     "y": 'Nodes are points of destructive interference and antinodes points of constructive interference.'},
    {"q": 'Why does a stationary wave on a string carry no energy along the string?', "r": 'The nodes never move, so no energy can pass through them',
     "w": ['The string is too short to carry energy', 'The energy is destroyed at the nodes', 'The wave has no amplitude anywhere'],
     "e": ['Length is not the reason; a long string behaves the same way.', 'Energy is never destroyed; here it stays stored in the vibrating loops.', 'The antinodes vibrate with a large amplitude.'],
     "y": 'Energy is stored in each loop, moving between kinetic and potential, but it does not travel past a node.'},
]

L.lesson(D, S, 12, ("p4-12", "Describe stationary waves, harmonics and overtones"), [11],
  "A stationary (standing) wave is made when two waves of the same frequency and amplitude travel in opposite directions and interfere, "
  "usually a wave and its own reflection.\n"
  "Nodes are points that never move (destructive interference). Antinodes are points that vibrate most (constructive interference).\n"
  "The distance between two neighbouring nodes is half a wavelength: λ = 2 × (node-to-node distance).\n"
  "On a string of length L fixed at both ends there must be a node at each end, so L = nλ/2, that is λ = 2L/n with n = 1, 2, 3, …\n"
  "n = 1 is the fundamental or first harmonic, with frequency f₁. n = 2 is the second harmonic (first overtone), with frequency 2f₁, and so on.\n"
  "Unlike a progressive wave, a stationary wave carries no energy along the string.",
  worked({"L": 0.6, "n": 3},
         "A string of length {L} m fixed at both ends vibrates in {n} loops. Find the wavelength.",
         ["Each loop is half a wavelength long.",
          "{n} loops fill the length, so {n} × (λ ÷ {2}) = {L}.",
          "λ = {2} × {L} ÷ {n}."],
         "{harmonicLen(L, n)} m",
         figure="harmonicFig(n)",
         checks=["harmonicLen(L, n) == 0.4"]),
  [card("c4p12-1", "A node never moves; an antinode vibrates most. Neighbouring nodes are half a wavelength apart.",
        ["nodes {0.2} m apart means λ = {0.4} m"], "p4-12-nodes"),
   card("c4p12-2", "On a string fixed at both ends, λ = {2}L/n, where n is the number of loops.",
        ["L = {0.6} m with {3} loops: λ = {0.4} m"], "p4-12-lambda"),
   card("c4p12-3", "The nth harmonic has frequency n × the fundamental.",
        ["f₁ = {100} Hz gives a third harmonic of {300} Hz"], "p4-12-harm")],
  [num("p4-12-nodes", 1, "On a stationary wave, two neighbouring nodes are {d} cm apart. Find the wavelength, in cm.",
       "2 * d",
       ["The distance between neighbouring nodes is half a wavelength.", "λ = {2} × {d} = {answer} cm."],
       vars={"d": {"pick": [5, 10, 12, 15, 20, 25, 30]}},
       misc=[("same", "d", "{d} cm is only half a wavelength."),
             ("half", "roundTo(d / 2, 0.01)", "Multiply by {2}: node to node is HALF a wavelength.")],
       sources=SRCW, unit="cm"),
   num("p4-12-lambda", 1, "A string of length {L} m fixed at both ends vibrates in {n} loops. Find the wavelength, in metres.",
       "harmonicLen(L, n)",
       ["Each loop is half a wavelength, and {n} loops fill the string.", "λ = {2}L ÷ n = {2} × {L} ÷ {n} = {answer} m."],
       vars={"L": {"pick": [0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2]}, "n": {"int": [1, 5]}},
       figure="harmonicFig(n)",
       misc=[("nohalf", "roundTo(L / n, 0.001)", "Each loop is HALF a wavelength, so λ = {2}L ÷ n."),
             ("whole", "2 * L", "That is the wavelength of the fundamental, with one loop. Here there are {n}.")],
       sources=SRCW, unit="m", where=["n > 1 || harmonicLen(L, n) != 2 * L"]),
   num("p4-12-harm", 2, "A string has a fundamental frequency of {f1} Hz. Find the frequency of its {n}{n == 2 ? 'nd' : n == 3 ? 'rd' : 'th'} harmonic, in hertz.",
       "n * f1",
       ["The nth harmonic has n times the fundamental frequency.", "f = {n} × {f1} = {answer} Hz."],
       vars={"f1": {"pick": [50, 80, 100, 110, 120, 150, 200, 256]}, "n": {"int": [2, 6]}},
       misc=[("div", "roundTo(f1 / n, 0.01)", "A higher harmonic has a HIGHER frequency: multiply."),
             ("over", "(n + 1) * f1", "The {n}th harmonic is {n} × f₁. ({n} × f₁ is also called the {n - 1}{n - 1 == 1 ? 'st' : n - 1 == 2 ? 'nd' : n - 1 == 3 ? 'rd' : 'th'} overtone.)")],
       sources=SRCW, unit="Hz"),
   mcq("p4-12-count", 2, "The diagram shows a string fixed at both ends vibrating as a stationary wave. How many nodes and antinodes are there?",
       "{n + 1} nodes and {n} antinodes",
       [("{n} nodes and {n + 1} antinodes", "swap"), ("{n} nodes and {n} antinodes", "equal"), ("{2 * n} nodes and {n} antinodes", "double")],
       ["Each loop has one antinode in the middle, so there are {n} antinodes.",
        "There is a node at each end and one between each pair of loops: {n} + {1} = {n + 1}.", "So the answer is: {answer}."],
       vars={"n": {"int": [1, 5]}},
       figure="harmonicFig(n)",
       misc=[("swap", "The ends are fixed, so they are nodes: there is always one node more than the number of loops."),
             ("equal", "Count the ends: a string fixed at both ends has a node at each end."),
             ("double", "Neighbouring loops share a node, so they are not counted twice.")],
       sources=SRCW),
   bank("p4-12-compare", 3, "{X.q}", STAND, SRCW)],
  learn=learn(
    [goal("explain how a stationary wave is formed, find λ from the node spacing or the number of loops, and name the harmonics.",
          "Lesson {11} (interference and reflection) and Lesson {10} (v = fλ).",
          "Lesson {15} (vibrating strings) and the notes made by musical instruments."),
     ("Nodes, antinodes and loops",
      "Send a wave along a string fixed at the far end. The reflected wave meets the wave still going forward. "
      "Where they are always out of step, the string never moves: a node. Where they are always in step, it vibrates most: an antinode.\n"
      "The pattern stays in one place, so it is a stationary wave. Unlike a progressive wave, it carries no energy along the string.\n"
      "Each loop between two nodes is half a wavelength long, so:\n"
      "λ = {2} × (distance from one node to the next).\n"
      "A string fixed at both ends must have a node at each end, so a whole number of loops must fit: L = nλ ÷ {2}, that is λ = {2}L ÷ n."),
     ("Harmonics and overtones",
      "With n = {1}, the string vibrates as one loop. This is the fundamental, or first harmonic: λ₁ = {2}L and f₁ = v ÷ ({2}L).\n"
      "• n = {2}: two loops, λ = L, frequency {2}f₁. Second harmonic, also called the first overtone.\n"
      "• n = {3}: three loops, λ = {2}L ÷ {3}, frequency {3}f₁. Third harmonic, second overtone.\n"
      "So the nth harmonic has n loops, n + {1} nodes, n antinodes and frequency n × f₁.\n"
      "A plucked guitar string vibrates in several of these at once; the mixture gives the instrument its quality.")],
    key_words=[("stationary wave", "a wave pattern that stays in place, made by two waves meeting"),
               ("node", "a point that never moves"), ("antinode", "a point that vibrates most"),
               ("fundamental", "the lowest frequency, with one loop"),
               ("harmonic", "a frequency that is a whole number times the fundamental")],
    examples=["nodes {15} cm apart → λ = {30} cm", "L = {1} m, {4} loops → λ = {0.5} m", "f₁ = {120} Hz → third harmonic {360} Hz"],
    mistake=("the distance between neighbouring nodes is one wavelength", "it is half a wavelength",
             "A full wave has two loops: one above the line and one below.")))

# ---------------------------------------------------------------- 13. Production and characteristics of sound
SOUND = [
    {"q": "What produces a sound?", "r": "A vibrating object",
     "w": ["A hot object", "A moving object of any kind", "A bright object"],
     "e": ["Heat alone makes no sound; a hot stone is silent.",
           "An object can move smoothly and silently; it is vibration that makes sound.",
           "Light and sound are different; a lamp is silent."],
     "y": "Every source of sound vibrates: a drum skin, a string, vocal cords, a loudspeaker cone."},
    {"q": "How does a sound wave travel through air?", "r": "As compressions and rarefactions passing through the air",
     "w": ["As crests and troughs of the air moving sideways", "By the air itself blowing from the source to the ear",
           "As a beam of particles shot out by the source"],
     "e": ["Crests and troughs belong to a transverse wave; sound in air is longitudinal.",
           "The air does not travel from the source to the ear; it vibrates in place.",
           "No particles are shot out; the existing air passes the vibration on."],
     "y": "The vibrating source pushes the air into compressions and leaves rarefactions between them."},
    {"q": "Two notes have the same loudness but one sounds higher. What differs?", "r": "The frequency: the higher note has the greater frequency",
     "w": ["The amplitude", "The speed of the sound in air", "The wavelength only, with the frequency unchanged"],
     "e": ["Amplitude decides loudness, which is said to be the same here.",
           "All sounds travel at the same speed in the same air.",
           "If the speed is fixed and the wavelength changes, the frequency changes too."],
     "y": "Pitch depends on frequency: more vibrations each second gives a higher note."},
    {"q": "Two notes have the same pitch but one is louder. What differs?", "r": "The amplitude: the louder note has the greater amplitude",
     "w": ["The frequency", "The speed in air", "The quality only"],
     "e": ["Equal pitch means equal frequency.",
           "The speed in the same air is the same for both.",
           "Quality is about the mixture of overtones, not about loudness."],
     "y": "Loudness depends on amplitude, which is the energy the wave carries."},
    {"q": "The same note is played on a flute and on a guitar, and they sound different. What is this difference called?", "r": "Quality (timbre), caused by the mixture of overtones",
     "w": ["Pitch", "Loudness", "Speed"],
     "e": ["The pitch is the same: both play the same note.",
           "They can be played equally loudly and still sound different.",
           "Both sounds travel at the same speed in air."],
     "y": "Each instrument produces the fundamental with a different mixture of overtones, and that mixture is its quality."},
    {"q": "Through which does sound travel fastest?", "r": "A steel rail",
     "w": ["Air", "Water", "A vacuum"],
     "e": ["Sound travels slowest of these in air, about {340} m/s.",
           "Sound travels faster in water than in air, but faster still in a solid.",
           "Sound cannot travel through a vacuum at all."],
     "y": "The particles of a solid are closest together, so they pass the vibration on fastest."},
]

QUALITY = [
    {"q": 'The same note is played on a guitar and on a flute, equally loudly. Which statement is true?', "r": 'They have the same pitch and loudness but different quality, because of their different overtones',
     "w": ['They have different pitches', 'The flute sound travels faster', 'They are identical sounds'],
     "e": ["Playing 'the same note' means the same fundamental frequency, so the pitch is the same.", 'All sounds travel at the same speed in the same air.', 'They are easy to tell apart, which is why quality is a separate characteristic.'],
     "y": 'Each instrument adds its own mixture of overtones to the fundamental, and that mixture is its quality.'},
    {"q": "What makes one person's voice sound different from another's, even on the same note?", "r": 'The mixture of overtones each voice produces, which is its quality',
     "w": ['The speed of the sound each makes', 'The pitch of the note', 'The loudness of the voice'],
     "e": ['All voices travel at the same speed in the same air.', 'Singing the same note means the same pitch for both.', 'Both can sing equally loudly and still sound different.'],
     "y": 'Quality, or timbre, comes from the overtones present along with the fundamental.'},
    {"q": 'A tuning fork and a violin both sound a note of {256} Hz. Why does the fork sound plainer?', "r": 'A tuning fork gives almost only the fundamental, with few overtones',
     "w": ['A tuning fork is quieter', 'A tuning fork gives a higher pitch', 'A tuning fork makes a longitudinal wave and the violin a transverse one'],
     "e": ['A fork can be struck hard and still sound plain.', 'Both sound {256} Hz, so the pitch is the same.', 'Both make longitudinal sound waves in the air.'],
     "y": 'A nearly pure note has little beyond the fundamental; the extra overtones of a violin give it a richer quality.'},
    {"q": 'Which characteristic of a sound depends on the amplitude of the wave?', "r": 'Its loudness',
     "w": ['Its pitch', 'Its quality', 'Its speed'],
     "e": ['Pitch depends on the frequency.', 'Quality depends on the mixture of overtones.', "The speed depends on the medium, not on the wave's amplitude."],
     "y": 'A larger amplitude carries more energy, and the sound is louder.'},
]

SPEEDMED = [
    {"q": 'A pupil puts an ear to a long steel rail and a friend taps the far end once. What is heard?', "r": 'Two sounds: the one through the steel first, then the one through the air',
     "w": ['Only one sound, through the air', 'Only one sound, through the steel', 'No sound at all'],
     "e": ['The rail carries sound too, and faster than the air does.', 'The air also carries the sound, arriving a little later.', 'Both the steel and the air are media that carry sound.'],
     "y": 'Sound travels much faster in a solid, where the particles are closest together.'},
    {"q": 'In which does sound travel fastest?', "r": 'In a steel bar',
     "w": ['In air', 'In water', 'In a vacuum'],
     "e": ['Sound is slowest of these in air, about {340} m/s.', 'Sound is faster in water than in air, but faster still in a solid.', 'Sound cannot travel through a vacuum at all.'],
     "y": 'The closer the particles, the faster the vibration is passed on: solids, then liquids, then gases.'},
    {"q": 'Why does sound travel faster in water than in air?', "r": 'The particles of water are much closer together, so the vibration is passed on more quickly',
     "w": ['Water is colder than air', 'Water is a transverse medium', 'Sound is louder under water'],
     "e": ['Temperature changes the speed a little, but the spacing of the particles matters far more.', 'Sound is longitudinal in water as it is in air.', 'How loud a sound is does not change how fast it travels.'],
     "y": 'Sound travels at about {340} m/s in air and about {1500} m/s in water.'},
    {"q": 'A thunderclap is heard several seconds after the lightning is seen. Why?', "r": 'Light travels far faster than sound, so the sound arrives much later',
     "w": ['The thunder happens after the lightning', 'The sound is reflected by the clouds first', 'Sound slows down in damp air'],
     "e": ['The flash and the clap happen together; it is the travel times that differ.', 'The delay is there even for a direct path; the difference in speed causes it.', 'Damp air changes the speed only slightly, far too little to explain seconds of delay.'],
     "y": 'Light crosses a few kilometres almost at once, while sound takes about {3} s for each kilometre.'},
]

L.lesson(D, S, 13, ("p4-13", "Explain how sound is produced and transmitted, and its characteristics"), [8],
  "Sound is produced by a vibrating object: a drum skin, a guitar string, vocal cords, a loudspeaker cone.\n"
  "It travels as a longitudinal wave: the source pushes the air into compressions (particles close together) with "
  "rarefactions (particles spread out) between them. The vibration is passed from particle to particle, so sound needs a medium "
  "and cannot cross a vacuum.\n"
  "Sound travels fastest in solids, slower in liquids and slowest in gases, because the particles are closer together in a solid. "
  "In air it is about 340 m/s.\n"
  "Characteristics:\n"
  "• Loudness depends on amplitude.\n• Pitch depends on frequency.\n"
  "• Quality (timbre) depends on the mixture of overtones, and is why the same note sounds different on different instruments.\n"
  "A healthy young person hears about 20 Hz to 20 000 Hz.",
  worked({"f1": 256, "f2": 512},
         "A tuning fork of {f1} Hz and one of {f2} Hz are struck equally hard. Compare the two sounds.",
         ["Both are struck equally hard, so the amplitudes are about the same: the sounds are about equally loud.",
          "{f2} Hz is {f2 / f1} times {f1} Hz, so the second fork vibrates more often each second.",
          "Pitch depends on frequency, so the {f2} Hz fork sounds higher.",
          "In the same air both travel at the same speed, so the higher note has the shorter wavelength."],
         "about equally loud, but the {f2} Hz fork sounds higher",
         checks=["f2 == 2 * f1"]),
  [card("c4p13-1", "Sound is made by something vibrating, and travels as compressions and rarefactions.",
        ["a drum skin pushes the air into compressions as it moves out"], "p4-13-which"),
   card("c4p13-2", "Loudness depends on amplitude; pitch depends on frequency.",
        ["hitting a drum harder: louder, same pitch. A tighter skin: higher pitch"], "p4-13-pitch"),
   card("c4p13-3", "Quality (timbre) comes from the mixture of overtones.",
        ["the same note on a flute and a guitar sounds different"], "p4-13-quality")],
  [bank("p4-13-which", 1, "{X.q}", SOUND, SRCS),
   mcq("p4-13-pitch", 1, "A drum is hit {how}. What happens to the sound?",
       "{H.r}",
       [("{H.w1}", "w1"), ("{H.w2}", "w2"), ("{H.w3}", "w3")],
       ["{H.y}", "So the answer is: {answer}."],
       vars={"H": {"pick": [
           {"q": "harder than before", "r": "It is louder, because the skin vibrates with a greater amplitude",
            "w1": "It is higher in pitch, because the skin vibrates faster", "w2": "It is quieter, because more energy is lost",
            "w3": "Nothing changes", "y": "Hitting harder gives the skin more energy, so it vibrates with a bigger amplitude, and amplitude decides loudness."},
           {"q": "after its skin has been tightened", "r": "It is higher in pitch, because the skin vibrates more often each second",
            "w1": "It is louder, because the skin is tighter", "w2": "It is lower in pitch, because the skin is stiffer",
            "w3": "Nothing changes", "y": "A tighter skin vibrates at a higher frequency, and frequency decides pitch."},
           {"q": "very softly", "r": "It is quieter, because the skin vibrates with a smaller amplitude",
            "w1": "It is lower in pitch, because the skin vibrates more slowly", "w2": "It is louder, because less energy is wasted",
            "w3": "Nothing changes", "y": "A gentle hit gives little energy, so the amplitude is small and the sound is quiet; the pitch is unchanged."}]},
             "how": {"expr": "H.q"}},
       misc=[("w1", "{H.y}"), ("w2", "{H.y}"), ("w3", "{H.y}")],
       sources=SRCS),
   num("p4-13-lam", 2, "A note of frequency {f} Hz travels through air at {340} m/s. Find its wavelength, in metres.",
       "roundTo(waveLen(340, f), 0.001)",
       ["λ = v ÷ f.", "λ = {340} ÷ {f} = {answer} m."],
       vars={"f": {"pick": [20, 40, 50, 68, 85, 100, 170, 200, 340, 425, 680, 850]}},
       misc=[("mult", "waveSpeed(340, f)", "Divide the speed by the frequency."),
             ("swap", "roundTo(f / 340, 0.0001)", "λ = v ÷ f, not f ÷ v.")],
       sources=SRCS, unit="m"),
   bank("p4-13-quality", 2, "{X.q}", QUALITY, SRCS),
   bank("p4-13-medium", 3, "{X.q}", SPEEDMED, SRCS)],
  learn=learn(
    [goal("explain how sound is produced and carried, and link loudness, pitch and quality to amplitude, frequency and overtones.",
          "Lesson {8} (longitudinal waves) and Lesson {9} (amplitude and frequency).",
          "Lesson {14} (measuring the speed of sound) and Lesson {15} (notes from vibrating strings)."),
     ("Production and transmission",
      "Every sound starts with something vibrating: a drum skin, a string, the vocal cords, a loudspeaker cone.\n"
      "As the surface moves outwards it pushes the air particles together, making a compression. As it moves back it leaves them "
      "spread out, making a rarefaction. These pass from particle to particle through the air, so sound is a longitudinal wave.\n"
      "Because particles must pass the vibration on, sound needs a medium: a bell in a vacuum jar cannot be heard.\n"
      "The closer the particles, the faster the vibration is passed on: sound travels fastest in solids, slower in liquids and "
      "slowest in gases. In air it is about {340} m/s; in water about {1500} m/s; in steel about {5000} m/s."),
     ("Loudness, pitch and quality",
      "• Loudness depends on the amplitude. Hitting a drum harder gives a bigger amplitude and a louder sound, at the same pitch.\n"
      "• Pitch depends on the frequency. More vibrations each second gives a higher note. Tightening a drum skin or shortening "
      "a guitar string raises the frequency and so the pitch.\n"
      "• Quality, or timbre, depends on the mixture of overtones present with the fundamental. It is why the same note on a "
      "flute and on a guitar sounds different.\n"
      "A healthy young person hears from about {20} Hz to about {20000} Hz. Above that is ultrasound, used to look inside the body "
      "and to find the depth of the sea.")],
    key_words=[("compression", "a region where the particles are pushed together"),
               ("rarefaction", "a region where the particles are spread apart"),
               ("pitch", "how high or low a note sounds; it depends on frequency"),
               ("loudness", "how loud a sound is; it depends on amplitude"),
               ("quality (timbre)", "what makes the same note sound different on different instruments")],
    examples=["hit harder: louder, same pitch", "tighter string: higher pitch", "{340} ÷ {170} = {2} m wavelength"],
    mistake=("a higher note travels faster through the air", "all sounds travel at the same speed in the same air",
             "A higher frequency goes with a shorter wavelength, because v = fλ and v is fixed.")))

# ---------------------------------------------------------------- 14. Speed of sound; echoes
L.lesson(D, S, 14, ("p4-14", "Measure the speed of sound and use echoes"), [13],
  "An echo is a sound reflected from a large surface such as a cliff or a wall.\n"
  "Echo method: stand a measured distance d from a wall, clap, and time the echo. The sound travels to the wall and back, "
  "a distance of 2d, in time t, so v = 2d/t.\n"
  "Gun-firing method: an observer a measured distance d away starts a stopwatch when the flash is seen and stops it when the "
  "bang is heard. Light arrives almost instantly, so v = d/t.\n"
  "Echo sounding (sonar) finds the depth of the sea: a pulse is sent down and the time for its return is measured, so depth = vt/2. "
  "It is also used to find shoals of fish and, as ultrasound, to look inside the body.\n"
  "In air, sound travels at about 340 m/s; it goes faster in warmer air.",
  worked({"d": 170, "t": 1},
         "A pupil claps {d} m from a cliff and hears the echo {t} s later. Find the speed of sound in air.",
         ["The sound travels to the cliff and back, so the distance is {2} × {d} = {2 * d} m.",
          "speed = distance ÷ time.", "v = {2 * d} ÷ {t}."],
         "{echoSpeed(d, t)} m/s",
         checks=["echoSpeed(d, t) == 340"]),
  [card("c4p14-1", "An echo is a reflected sound; the sound covers twice the distance to the surface.",
        ["a clap {170} m from a cliff returns after {1} s: v = {340} ÷ {1} = {340} m/s"], "p4-14-echo"),
   card("c4p14-2", "Echo method: v = {2}d ÷ t. Gun method: v = d ÷ t, because the flash arrives almost at once.",
        ["flash seen, bang heard {2} s later, {680} m away: v = {340} m/s"], "p4-14-gun"),
   card("c4p14-3", "Echo sounding: depth = v × t ÷ {2}.",
        ["a pulse at {1500} m/s returning after {0.4} s: depth {300} m"], "p4-14-depth")],
  [num("p4-14-echo", 1, "A pupil claps {d} m from a wall and hears the echo after {t} s. Find the speed of sound, in m/s.",
       "echoSpeed(d, t)",
       ["The sound goes to the wall and back: {2} × {d} = {2 * d} m.", "v = {2 * d} ÷ {t} = {answer} m/s."],
       vars={"t": {"pick": [0.5, 1, 1.5, 2, 2.5]}, "v0": {"pick": [320, 330, 340, 350]}, "d": {"expr": "v0 * t / 2"}},
       misc=[("oneway", "roundTo(d / t, 0.1)", "The sound covers the distance TWICE: there and back."),
             ("double", "roundTo(4 * d / t, 0.1)", "The total path is {2}d, not {4}d.")],
       sources=SRCS, unit="m/s"),
   num("p4-14-gun", 1, "A gun is fired {d} m away. The flash is seen, and the bang is heard {t} s later. Find the speed of sound, in m/s.",
       "roundTo(d / t, 0.1)",
       ["Light reaches the observer almost at once, so the time measured is the time for the sound.",
        "The sound travels {d} m one way.", "v = {d} ÷ {t} = {answer} m/s."],
       vars={"t": {"pick": [0.5, 1, 1.5, 2, 2.5, 3]}, "v0": {"pick": [320, 330, 340, 350]}, "d": {"expr": "v0 * t"}},
       misc=[("echo", "roundTo(2 * d / t, 0.1)", "There is no echo here: the sound travels one way only."),
             ("swap", "roundTo(t / d, 0.0001)", "Speed = distance ÷ time.")],
       sources=SRCS, unit="m/s"),
   num("p4-14-dist", 2, "A clap is heard as an echo {t} s after it is made. Taking the speed of sound as {v} m/s, how far away is the reflecting wall, in metres?",
       "echoDist(v, t)",
       ["In {t} s the sound covers {v} × {t} = {v * t} m.", "That is to the wall and back, so the wall is half as far.",
        "d = {v * t} ÷ {2} = {answer} m."],
       vars={"v": {"pick": [330, 340, 350]}, "t": {"pick": [0.4, 0.6, 1, 1.2, 1.6, 2, 2.4]}},
       misc=[("full", "roundTo(waveSpeed(v, t), 0.1)", "{v * t} m is the whole path there and back: halve it."),
             ("quarter", "roundTo(v * t / 4, 0.1)", "The path is twice the distance to the wall, so halve it once only.")],
       sources=SRCS, unit="m"),
   num("p4-14-depth", 2, "A ship sends a sound pulse to the sea bed and receives the echo {t} s later. Sound travels at {v} m/s in sea water. Find the depth, in metres.",
       "echoDist(v, t)",
       ["The pulse travels down and back, so the total path is {v} × {t} = {v * t} m.", "The depth is half of that: {answer} m."],
       vars={"v": {"pick": [1400, 1500, 1600]}, "t": {"pick": [0.2, 0.4, 0.5, 0.8, 1, 1.5, 2]}},
       misc=[("full", "roundTo(waveSpeed(v, t), 0.1)", "That is the whole path down and back; the depth is half."),
             ("swap", "roundTo(t / v * 2, 0.0001)", "distance = speed × time.")],
       sources=SRCS, unit="m"),
   num("p4-14-delay", 3, "A man stands {d} m from a cliff. Taking the speed of sound as {v} m/s, how long after his shout does he hear the echo, in seconds?",
       "roundTo(2 * d / v, 0.01)",
       ["The sound travels to the cliff and back: {2} × {d} = {2 * d} m.", "time = distance ÷ speed = {2 * d} ÷ {v} = {answer} s."],
       vars={"v": {"pick": [330, 340, 350]}, "d": {"int": [50, 600]}},
       misc=[("oneway", "roundTo(d / v, 0.01)", "The echo has to come back as well: use {2}d."),
             ("swap", "roundTo(v / (2 * d), 0.01)", "time = distance ÷ speed.")],
       sources=SRCS, unit="s", where=["roundTo(2 * d / v, 0.01) >= 0.3", "abs(2 * d / v * 1000 - round(2 * d / v * 1000)) > 0.01 || abs(round(2 * d / v * 1000)) % 10 != 5"])],
  learn=learn(
    [goal("measure the speed of sound by the echo and gun-firing methods, and use echoes to find a distance or a depth.",
          "Lesson {13} (how sound travels) and Form Three speed, distance and time.",
          "ultrasound scanning and sonar, and the wave calculations of Form Five."),
     ("Two ways to measure the speed",
      "Echo method: measure the distance d from a large wall or cliff. Clap, and time the gap until the echo returns. "
      "The sound travels to the wall and back, a distance of {2}d, so\n"
      "v = {2}d ÷ t.\n"
      "Clapping in a steady rhythm so that each clap falls with the echo, and timing many claps, makes the result more reliable.\n"
      "Gun-firing method: an observer stands a measured distance away, starts a stopwatch on seeing the flash and stops it on "
      "hearing the bang. Light travels so fast that its own travel time can be ignored, so\n"
      "v = d ÷ t.\n"
      "Both give about {340} m/s in air, and sound travels a little faster in warmer air."),
     ("Using echoes",
      "If the speed is known, the same idea gives a distance:\n"
      "• A shout returns from a cliff after {2} s, with v = {340} m/s. The sound covered {680} m there and back, so the cliff is {340} m away.\n"
      "• Echo sounding on a ship: a pulse is sent to the sea bed and the echo timed. depth = v × t ÷ {2}. "
      "At {1500} m/s, an echo after {0.4} s means a depth of {300} m.\n"
      "The same method finds shoals of fish, and as ultrasound it is used to look inside the body.\n"
      "Always remember to halve: the sound covers the distance twice.")],
    key_words=[("echo", "a sound reflected back from a surface"),
               ("echo sounding", "finding a depth or distance by timing a reflected pulse"),
               ("ultrasound", "sound above about {20000} Hz, too high to hear")],
    examples=["{170} m from a wall, echo after {1} s: v = {340} m/s", "echo after {0.5} s at {1500} m/s: depth {375} m"],
    mistake=("echo {2} s after a clap {340} m away gives v = {340} ÷ {2} = {170} m/s", "v = {2} × {340} ÷ {2} = {340} m/s",
             "The sound travels to the wall and back, so the distance is {2}d.")))

# ---------------------------------------------------------------- 15. Vibrating strings
L.lesson(D, S, 15, ("p4-15", "Relate the frequency of a vibrating string to its length, mass per unit length and tension"), [12],
  "The fundamental frequency of a stretched string depends on three things:\n"
  "• Length L: f is inversely proportional to L. Halving the length doubles the frequency.\n"
  "• Mass per unit length µ: f is inversely proportional to √µ. A thicker, heavier string gives a lower note.\n"
  "• Tension T: f is proportional to √T. Tightening the string raises the note.\n"
  "Together: f = (1/2L)√(T/µ).\n"
  "This is why a guitarist presses a string against a fret (shorter L, higher note), why the low strings are thick, "
  "and why a string is tuned by turning a peg to change the tension.\n"
  "The sonometer is the laboratory instrument used to check these relations.",
  worked({"f1": 200, "k": 2},
         "A string of length L vibrates at {f1} Hz. It is pressed down so that only {1}/{k} of its length can vibrate, with the tension unchanged. Find the new frequency.",
         ["Frequency is inversely proportional to the vibrating length: f ∝ {1}/L.",
          "The length is divided by {k}, so the frequency is multiplied by {k}.",
          "f = {k} × {f1}."],
         "{k * f1} Hz",
         checks=["k * f1 == 400"]),
  [card("c4p15-1", "f is inversely proportional to the length: halve the length and the frequency doubles.",
        ["{200} Hz on a full string becomes {400} Hz on half of it"], "p4-15-length"),
   card("c4p15-2", "f is proportional to √T: to double the frequency the tension must be {4} times as great.",
        ["tension × {4} gives frequency × {2}"], "p4-15-tension"),
   card("c4p15-3", "f is inversely proportional to √µ: a thicker, heavier string gives a lower note.",
        ["µ × {4} gives frequency ÷ {2}"], "p4-15-mass")],
  [num("p4-15-length", 1, "A string {L} cm long gives a note of {f1} Hz. The vibrating length is changed to {L2} cm, with everything else the same. Find the new frequency, in hertz.",
       "f1 * L / L2",
       ["f is inversely proportional to L, so f₁L₁ = f₂L₂.", "f₂ = {f1} × {L} ÷ {L2} = {answer} Hz."],
       vars={"f1": {"pick": [100, 120, 150, 200, 240, 300]}, "L": {"pick": [40, 60, 80, 90, 100, 120]}, "r": {"pick": [2, 3, 4]}, "L2": {"expr": "L / r"}},
       misc=[("direct", "roundTo(f1 * L2 / L, 0.1)", "A SHORTER string gives a HIGHER note: f is inversely proportional to L."),
             ("same", "f1", "Changing the vibrating length changes the frequency.")],
       sources=SRCW, unit="Hz", where=["L % r == 0"]),
   num("p4-15-tension", 2, "A string vibrates at {f1} Hz. The tension is increased to {k * k} times its old value, with the length and the string unchanged. Find the new frequency, in hertz.",
       "k * f1",
       ["f is proportional to √T.", "√{k * k} = {k}, so the frequency is multiplied by {k}.", "f = {k} × {f1} = {answer} Hz."],
       vars={"f1": {"pick": [80, 100, 120, 150, 200, 250]}, "k": {"int": [2, 4]}},
       misc=[("direct", "k * k * f1", "The frequency goes with the SQUARE ROOT of the tension: × {k}, not × {k * k}."),
             ("down", "roundTo(f1 / k, 0.1)", "A tighter string gives a HIGHER note.")],
       sources=SRCW, unit="Hz"),
   num("p4-15-mass", 2, "A string vibrates at {f1} Hz. It is replaced by one of the same length and tension but with {k * k} times the mass per unit length. Find the new frequency, in hertz.",
       "f1 / k",
       ["f is inversely proportional to √µ.", "√{k * k} = {k}, so the frequency is divided by {k}.", "f = {f1} ÷ {k} = {answer} Hz."],
       vars={"k": {"int": [2, 4]}, "q": {"pick": [30, 40, 50, 60, 80, 100]}, "f1": {"expr": "q * k"}},
       misc=[("up", "f1 * k", "A heavier string gives a LOWER note."),
             ("square", "roundTo(f1 / (k * k), 0.1)", "Use the square root of the mass per unit length: ÷ {k}, not ÷ {k * k}.")],
       sources=SRCW, unit="Hz"),
   mcq("p4-15-which", 2, "A guitarist {act}. What happens to the note?",
       "{G.r}",
       [("{G.w1}", "w1"), ("{G.w2}", "w2"), ("{G.w3}", "w3")],
       ["{G.y}", "So the answer is: {answer}."],
       vars={"G": {"pick": [
           {"q": "presses a string against a fret nearer the middle of the neck", "r": "It becomes higher, because the vibrating length is shorter",
            "w1": "It becomes lower, because the string is shorter", "w2": "It becomes louder but keeps its pitch", "w3": "Nothing changes",
            "y": "f is inversely proportional to the vibrating length, so a shorter length gives a higher frequency."},
           {"q": "turns a peg to tighten a string", "r": "It becomes higher, because the tension is greater",
            "w1": "It becomes lower, because the string is stretched", "w2": "It becomes louder but keeps its pitch", "w3": "Nothing changes",
            "y": "f is proportional to √T, so more tension gives a higher frequency."},
           {"q": "plays the thickest string instead of the thinnest, at the same length and tension", "r": "It is lower, because the mass per unit length is greater",
            "w1": "It is higher, because a thick string carries more energy", "w2": "It is the same, because the length is the same", "w3": "It is louder but the same pitch",
            "y": "f is inversely proportional to √µ, so a heavier string gives a lower frequency."},
           {"q": "plucks the same string harder, changing nothing else", "r": "It is louder, with the same pitch",
            "w1": "It is higher in pitch", "w2": "It is lower in pitch", "w3": "Nothing changes",
            "y": "Plucking harder increases the amplitude, which changes the loudness; the frequency is set by L, T and µ."}]},
             "act": {"expr": "G.q"}},
       misc=[("w1", "{G.y}"), ("w2", "{G.y}"), ("w3", "{G.y}")],
       sources=SRCW),
   num("p4-15-formula", 3, "A string of vibrating length {L} m carries a wave of speed {v} m/s. Find its fundamental frequency, in hertz.",
       "roundTo(v / (2 * L), 0.01)",
       ["For the fundamental, λ = {2}L = {2} × {L} = {2 * L} m.", "f = v ÷ λ = {v} ÷ {2 * L}.", "f = {answer} Hz."],
       vars={"L": {"pick": [0.25, 0.4, 0.5, 0.6, 0.8, 1]}, "v": {"pick": [100, 120, 150, 200, 240, 300, 400]}},
       misc=[("nohalf", "roundTo(v / L, 0.01)", "For the fundamental the wavelength is {2}L, not L."),
             ("swap", "roundTo(2 * L / v, 0.0001)", "f = v ÷ λ.")],
       sources=SRCW, unit="Hz")],
  learn=learn(
    [goal("say how the frequency of a vibrating string depends on its length, tension and mass per unit length, and use the formula for its fundamental frequency.",
          "Lesson {12} (stationary waves on a string) and Lesson {13} (pitch and frequency).",
          "the tuning of musical instruments, and resonance in Form Five."),
     ("Three things that change the note",
      "A stretched string sounds its fundamental, with one loop and λ = {2}L.\n"
      "• Length L: f is inversely proportional to L. Halve the vibrating length and the frequency doubles, so the note rises by an octave. "
      "That is what a guitarist does by pressing a string against a fret.\n"
      "• Tension T: f is proportional to √T. To double the frequency, the tension must be made {4} times as great. "
      "A string is tuned by turning a peg to change T.\n"
      "• Mass per unit length µ: f is inversely proportional to √µ. A thick, heavy string vibrates more slowly, "
      "which is why the low strings of a guitar are the thickest."),
     ("The formula and the sonometer",
      "Putting the three together:\n"
      "f = ({1} ÷ {2}L) × √(T ÷ µ).\n"
      "The same result follows from v = fλ: for the fundamental λ = {2}L, so f = v ÷ ({2}L), and the speed of the wave on the string "
      "depends on T and µ.\n"
      "A sonometer is used to check these relations in the laboratory: a wire is stretched over two bridges by a known weight, "
      "and the bridges are moved to change the vibrating length. Keeping two of the three quantities fixed and changing the third "
      "shows each relation in turn.")],
    key_words=[("fundamental frequency", "the lowest frequency of a vibrating string, with one loop"),
               ("tension", "the stretching force in the string, in newtons"),
               ("mass per unit length (µ)", "the mass of one metre of the string, in kg/m"),
               ("sonometer", "an instrument for studying the vibration of a stretched wire")],
    examples=["half the length → double the frequency", "{4} times the tension → double the frequency", "{4} times µ → half the frequency"],
    mistake=("doubling the tension doubles the frequency", "the tension must be {4} times as great",
             "f is proportional to the SQUARE ROOT of the tension, and √{4} = {2}.")))
