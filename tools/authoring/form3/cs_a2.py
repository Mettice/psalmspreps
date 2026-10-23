"""Form 3 Computer Science, Term 1, rows 3-6 (impact of AI, prompts, robots, control systems, VR and AR). Run: python tools/authoring/form3/cs_a2.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"
SRC = ["computing-society"]

# ---------------------------------------------------------------- 3. Societal impact and challenges of AI
L.lesson(D, S, 3, ("s3-3", "Societal impact and challenges of applied AI"), [2],
  "Benefits of AI: faster diagnosis, better crop yields, help for disabled people (speech-to-text), saving time on routine work, new jobs (data scientists, AI trainers).\n"
  "Challenges:\n• Jobs: some routine jobs may be replaced; workers need new skills.\n• Privacy: AI uses large amounts of personal data, which can be misused.\n"
  "• Bias and fairness: AI trained on biased data can treat groups unfairly.\n• Misinformation: AI can create fake images, voices and videos (deepfakes) and convincing false text.\n"
  "• Over-dependence and errors: people may trust wrong answers; AI uses a lot of energy.\n"
  "Responsible use: protect personal data, check AI outputs, keep humans responsible for important decisions, follow laws and school rules.",
  worked({},
         "Give one benefit and one risk of using AI face recognition at the entrance of a school.",
         ["Benefit: it can quickly check who enters, improving security.", "Risk: it stores pupils' faces (personal data), which could be stolen or misused, and it may make mistakes with some faces."],
         "Benefit: security; risk: privacy and errors"),
  [card("c3s3-1", "AI brings benefits such as faster diagnosis and help for disabled people.",
        ["Speech-to-text helps people who cannot type."], "s3-3-benefit"),
   card("c3s3-2", "AI raises challenges: jobs, privacy, bias and fake content.",
        ["Deepfake videos can spread lies."], "s3-3-risk"),
   card("c3s3-3", "Use AI responsibly: protect data and check results.",
        ["Do not upload other people's photos without permission."], "s3-3-resp")],
  [bank("s3-3-benefit", 1, "{X.q}", [
     {"q": "Which is a benefit of AI to society?", "r": "Helping doctors detect diseases earlier", "w": ["Spreading fake videos", "Collecting private data without permission", "Replacing all teachers"],
      "e": ["That is a harm.", "That is a harm.", "That is not a benefit, nor realistic."], "y": "Early diagnosis saves lives."},
     {"q": "How can AI help a blind person?", "r": "By reading text aloud and describing images", "w": ["By making screens brighter", "By removing all sounds", "By deleting e-mails"],
      "e": ["Brightness does not help a blind person.", "Sound is what helps.", "That does not help."], "y": "Text-to-speech and image description give access."},
     {"q": "Which new job has grown because of AI?", "r": "data scientist", "w": ["typewriter repairer", "telegram operator", "lamplighter"],
      "e": ["Typewriters are rarely used.", "Telegrams have almost disappeared.", "Street lamps are electric."], "y": "People who prepare data and build models are in demand."}], SRC),
   bank("s3-3-risk", 1, "{X.q}", [
     {"q": "What is a deepfake?", "r": "A fake video, image or voice made with AI to look real", "w": ["A very deep swimming pool", "A computer virus", "A broken hard disk"],
      "e": ["Not a pool.", "A virus is malicious software, not fake media.", "Not hardware."], "y": "Deepfakes can spread misinformation."},
     {"q": "Why is privacy a concern with AI?", "r": "AI systems collect and use large amounts of personal data", "w": ["AI makes computers slower", "AI uses no data", "AI only works offline"],
      "e": ["Speed is not the issue.", "AI depends on data.", "Many AI services run online."], "y": "Personal data can be leaked or misused."},
     {"q": "Which workers are most likely to be affected by automation with AI?", "r": "those doing routine, repetitive tasks", "w": ["no one", "only artists", "only farmers"],
      "e": ["Some jobs do change.", "Routine work is most affected.", "Routine work in many sectors is affected."], "y": "Learning new skills helps workers adapt."}], SRC),
   bank("s3-3-resp", 2, "{X.q}", [
     {"q": "Which is responsible use of AI tools by a student?", "r": "Using AI to explain a topic, then checking and writing in your own words", "w": ["Copying an AI essay and handing it in as your own", "Sharing classmates' private photos with an AI app", "Believing every AI answer without checking"],
      "e": ["That is cheating.", "That breaks others' privacy.", "AI can be wrong."], "y": "Use AI as a helper, honestly, and verify."},
     {"q": "A video of a politician saying shocking things spreads on WhatsApp. What should you do?", "r": "Check reliable news sources before sharing; it may be a deepfake", "w": ["Share it at once", "Believe it because it looks real", "Edit it to make it funnier"],
      "e": ["Sharing fakes spreads lies.", "Deepfakes look real.", "That spreads it further."], "y": "Verify before you share."},
     {"q": "Why should humans stay responsible for important AI decisions, such as who gets a loan?", "r": "AI can be biased or wrong, and people must be accountable", "w": ["Humans are always faster", "AI cannot read numbers", "Loans are not important"],
      "e": ["Speed is not the point.", "AI reads numbers well.", "Loans matter to people's lives."], "y": "Accountability and fairness need human oversight."}], SRC),
   bank("s3-3-bias", 3, "{X.q}", [
     {"q": "A face-recognition system works well for some groups of people but often fails for others. What is the most likely cause?", "r": "It was trained mostly on photos of some groups", "w": ["The camera is too new", "Faces cannot be recognised", "The system is too fast"],
      "e": ["Newness is not the cause.", "It works for some faces.", "Speed does not cause unfairness."], "y": "Unbalanced training data gives biased results."},
     {"q": "How can AI bias be reduced?", "r": "Train it on fair, balanced data and test it on many groups", "w": ["Use less data from fewer people", "Never test it", "Hide how it works from everyone"],
      "e": ["Less varied data increases bias.", "Testing finds bias.", "Openness helps find problems."], "y": "Balanced data and careful testing."},
     {"q": "Which law-related step protects people when AI uses their data?", "r": "Asking for permission and keeping the data secure", "w": ["Selling the data", "Publishing everyone's data", "Keeping data forever without reason"],
      "e": ["Selling without consent is misuse.", "That breaks privacy.", "Data should be kept only as needed."], "y": "Consent and security protect privacy."}], SRC)],
  learn=learn(
    [("The good side",
      "AI can save time and lives: it helps doctors detect disease early, farmers protect crops, banks stop fraud, and people with disabilities use phones and computers (speech-to-text, text-to-speech, image description).\n"
      "It also creates new jobs, such as data scientists and people who train and check AI systems."),
     ("The challenges",
      "• Jobs: some routine jobs may disappear or change; workers need to learn new skills.\n"
      "• Privacy: AI needs lots of data, often personal; it can be leaked, sold or misused.\n"
      "• Bias: AI trained on unbalanced data may treat some groups unfairly.\n"
      "• Fake content: deepfake videos, cloned voices and false articles can spread quickly.\n• Over-trust: AI can be confidently wrong; and big AI systems use a lot of electricity."),
     ("Using AI responsibly",
      "• Protect personal information: yours and other people's.\n• Check AI answers against reliable sources.\n• Do not present AI work as your own.\n"
      "• Verify shocking videos before sharing them.\n• Keep humans responsible for important decisions about people.")],
    key_words=[("privacy", "the right to control your personal information"), ("bias", "unfair treatment caused by unbalanced data or design"),
               ("deepfake", "fake media made with AI to look real"), ("automation", "machines doing work that people used to do")],
    examples=["Benefit: speech-to-text", "Risk: deepfake videos", "Responsible: verifying before sharing"],
    mistake=("AI is always neutral and fair", "AI can be biased if its data is biased",
             "AI learns patterns from data, including unfair ones.")))

# ---------------------------------------------------------------- 4. Prompts
L.lesson(D, S, 4, ("s3-4", "Writing appropriate prompts for AI tools"), [1],
  "A prompt is the instruction or question you give to an AI tool. Better prompts give better answers.\n"
  "A good prompt is:\n• clear and specific about the task;\n• gives context (who you are, what level, what for);\n• says the format you want (a list, a table, 100 words, steps);\n"
  "• may give an example or a role ('Explain as a Form 3 teacher…').\n"
  "Improve by iterating: read the answer, then refine the prompt.\n"
  "Never put passwords or private information in a prompt, and always check the answer.",
  worked({},
         "Improve this prompt: 'tell me about photosynthesis'.",
         ["Add the level and purpose: 'I am a Form {3} student revising for a test.'", "Make the task specific: 'Explain photosynthesis in simple words.'",
          "Give the format: 'Use five bullet points and include the word equation.'"],
         "'I am a Form {3} student revising for a test. Explain photosynthesis in simple words in five bullet points, including the word equation.'"),
  [card("c3s4-1", "Be clear and specific about the task.",
        ["'List three causes of soil erosion' beats 'erosion'."], "s3-4-best"),
   card("c3s4-2", "Give context and the format you want.",
        ["'For Form {3}, in a table with two columns'"], "s3-4-part"),
   card("c3s4-3", "Never include passwords or private data in a prompt.",
        ["Do not paste your mobile-money PIN."], "s3-4-safe")],
  [bank("s3-4-best", 1, "Which prompt is best? {X.q}", [
     {"q": "(You want help revising the water cycle.)", "r": "Explain the water cycle for a Form 3 student in four short steps.", "w": ["water", "Tell me everything.", "Do my homework."],
      "e": ["One word gives no task.", "Too vague: no topic.", "That is not a learning task and is dishonest."], "y": "Clear task, level and format."},
     {"q": "(You want a short summary of a story.)", "r": "Summarise this story in 50 words for a classmate.", "w": ["story", "Write something.", "Make it long."],
      "e": ["No task.", "Too vague.", "That is the opposite of a summary."], "y": "Task, length and audience are given."},
     {"q": "(You want practice questions on fractions.)", "r": "Give me five practice questions on adding fractions, with answers at the end.", "w": ["maths", "Questions.", "Fractions are hard."],
      "e": ["No task.", "Not specific.", "That is a comment, not a request."], "y": "Topic, number and format are clear."}], SRC),
   bank("s3-4-part", 1, "{X.q}", [
     {"q": "Which part of a prompt gives context?", "r": "'I am a Form 3 student preparing for a test'", "w": ["'in a table'", "'five points'", "'Explain'"],
      "e": ["That gives the format.", "That gives the length.", "That is the task verb."], "y": "Context tells the AI who you are and why."},
     {"q": "Which part of a prompt sets the format?", "r": "'as a numbered list'", "w": ["'I am a teacher'", "'about volcanoes'", "'please'"],
      "e": ["That is context.", "That is the topic.", "That is politeness."], "y": "Format tells the AI how to present the answer."},
     {"q": "What does it mean to iterate a prompt?", "r": "Read the answer and improve the prompt to get a better result", "w": ["Type the same prompt again and again", "Delete the answer", "Use capital letters"],
      "e": ["Repeating unchanged rarely helps.", "Deleting does not improve.", "Capitals do not help."], "y": "Refining step by step improves the output."}], SRC),
   bank("s3-4-safe", 2, "{X.q}", [
     {"q": "Which should you NEVER put in a prompt?", "r": "your password or PIN", "w": ["the topic you are studying", "the format you want", "your class level"],
      "e": ["Topics are fine.", "Format is fine.", "Class level is fine."], "y": "Prompts may be stored and seen by others."},
     {"q": "An AI tool gives a date for an event in history. What should you do?", "r": "Check it in your textbook or another reliable source", "w": ["Trust it completely", "Ignore your textbook", "Share it without reading"],
      "e": ["AI can be wrong.", "Your textbook is a reliable source.", "Read and check first."], "y": "Verify important facts."},
     {"q": "Is it honest to hand in an AI-written essay as your own?", "r": "No: it is plagiarism; use AI to learn, then write yourself", "w": ["Yes, the AI does not mind", "Yes, if you change one word", "Yes, if no one finds out"],
      "e": ["Honesty is about your work, not the AI's feelings.", "Still not your work.", "Being caught is not the point."], "y": "Present only your own work as yours."}], SRC),
   bank("s3-4-improve", 3, "Which change improves this prompt most? {X.q}", [
     {"q": "'Write about Cameroon.'", "r": "'Write 100 words about the main rivers of Cameroon for a Form 3 geography lesson.'", "w": ["'WRITE ABOUT CAMEROON!'", "'Write about Cameroon please.'", "'Cameroon.'"],
      "e": ["Capitals do not add detail.", "Politeness does not add detail.", "Less detail is worse."], "y": "Topic, length, level and purpose are now clear."},
     {"q": "'Help me with maths.'", "r": "'Show me step by step how to solve 3x + 5 = 20, then give me two similar questions.'", "w": ["'Help me with maths now.'", "'Maths is difficult.'", "'Help.'"],
      "e": ["Urgency adds no detail.", "That is a comment.", "Less detail is worse."], "y": "A specific task and a clear format."},
     {"q": "'Explain computers.'", "r": "'Explain, for a Form 3 student, the job of the CPU, RAM and hard disk, in a short table.'", "w": ["'Explain computers again.'", "'Explain computers in English.'", "'Computers?'"],
      "e": ["Repeating adds nothing.", "Language alone does not narrow the task.", "Less detail is worse."], "y": "Specific topic, level and format."}], SRC)],
  learn=learn(
    [("What a prompt is",
      "When you use a chatbot or other AI tool, the instruction you type is the prompt. The AI's answer can only be as good as the prompt allows.\n"
      "'Erosion' alone could mean many things. 'List three causes of soil erosion on farms in the North West region, with one way to prevent each' gets a useful answer."),
     ("Parts of a good prompt",
      "• Task: a clear verb, such as explain, list, compare or summarise.\n• Context: who you are and why ('I am a Form {3} student revising').\n"
      "• Format and length: bullet points, a table, {100} words, steps.\n• Role or example: 'Answer as a patient teacher', or show the style you want.\n"
      "If the answer is not right, iterate: change the prompt and try again."),
     ("Safe and honest prompting",
      "• Never type passwords, PINs, ID numbers or other people's private details.\n• Check answers: AI can invent facts.\n"
      "• Use AI to learn and practise, not to do your work for you. Handing in AI-written work as your own is dishonest.")],
    key_words=[("prompt", "the instruction or question given to an AI tool"), ("context", "background information that guides the answer"),
               ("iterate", "improve step by step"), ("plagiarism", "presenting someone else's (or an AI's) work as your own")],
    examples=["'Summarise in {50} words'", "'Explain for Form {3}'", "'Give the answer as a table'"],
    mistake=("Typing one word and expecting a perfect answer", "Write a clear task with context and format",
             "The AI cannot guess what you need; tell it.")))

# ---------------------------------------------------------------- 5. Robots
L.lesson(D, S, 5, ("s3-5", "Robots and their applications"), [1],
  "A robot is a programmable machine that can sense its surroundings and carry out actions automatically.\n"
  "Main parts: sensors (detect light, distance, touch, sound…), a controller/processor running a program, actuators (motors, grippers, wheels) and a power supply.\n"
  "Applications: manufacturing (welding, painting cars), medicine (surgical robots), homes (robot vacuum cleaners), agriculture (harvesting, spraying drones), exploration (Mars rovers, deep-sea robots), dangerous work (bomb disposal), warehouses and deliveries.\n"
  "Advantages: work non-stop, accurate, do dangerous or boring work. Disadvantages: expensive, need maintenance and power, may replace some jobs, cannot handle every unexpected situation.",
  worked({},
         "Explain how a robot vacuum cleaner avoids a chair.",
         ["Its sensors (bump or distance sensors) detect the chair in front.", "The processor runs its program and decides to turn.", "The actuators (wheel motors) turn it away and it carries on cleaning."],
         "Sensor detects, processor decides, actuators act"),
  [card("c3s5-1", "A robot senses, decides with a program and acts.",
        ["Sensor → processor → actuator"], "s3-5-part"),
   card("c3s5-2", "Robots are used in factories, hospitals, farms and exploration.",
        ["A Mars rover explores another planet."], "s3-5-use"),
   card("c3s5-3", "Robots do dangerous, repetitive or precise work.",
        ["Bomb-disposal robots keep people safe."], "s3-5-adv")],
  [bank("s3-5-part", 1, "{X.q}", [
     {"q": "Which part of a robot detects its surroundings?", "r": "sensors", "w": ["actuators", "the battery", "the body frame"],
      "e": ["Actuators produce movement.", "The battery gives power.", "The frame holds the parts."], "y": "Sensors detect light, distance, touch and more."},
     {"q": "Which part of a robot makes it move?", "r": "actuators such as motors", "w": ["sensors", "the program only", "the camera"],
      "e": ["Sensors detect.", "The program decides but cannot move anything itself.", "A camera is a sensor."], "y": "Motors, grippers and wheels are actuators."},
     {"q": "What is the role of the robot's program?", "r": "To decide what to do from the sensor information", "w": ["To provide electricity", "To detect light", "To grip objects"],
      "e": ["The power supply does that.", "Sensors do that.", "Grippers do that."], "y": "The controller runs the program."}], SRC),
   bank("s3-5-use", 1, "Which kind of robot is this? {X.q}", [
     {"q": "It welds car bodies on a factory line, day and night.", "r": "an industrial robot", "w": ["a medical robot", "a domestic robot", "an exploration robot"],
      "e": ["It is not in a hospital.", "It is not in a home.", "It is not exploring."], "y": "Factory robots do repetitive, precise work."},
     {"q": "It helps a surgeon make very small, precise cuts.", "r": "a medical robot", "w": ["an industrial robot", "a domestic robot", "a toy robot"],
      "e": ["It is not in a factory.", "It is not a home helper.", "It is a serious medical tool."], "y": "Surgical robots improve precision."},
     {"q": "It drives over the surface of Mars, taking photos and samples.", "r": "an exploration robot (rover)", "w": ["a domestic robot", "a medical robot", "an industrial robot"],
      "e": ["It is far from any home.", "It is not medical.", "It is not in a factory."], "y": "Rovers explore places people cannot easily reach."}], SRC),
   bank("s3-5-adv", 2, "{X.q}", [
     {"q": "Which is an advantage of robots in factories?", "r": "They can work continuously with high accuracy", "w": ["They never need repairs", "They cost nothing", "They can do every job better than people"],
      "e": ["They need maintenance.", "They are expensive.", "They cannot handle every task."], "y": "Consistent, non-stop work."},
     {"q": "Which is a disadvantage of using robots?", "r": "They are expensive and may replace some workers", "w": ["They are always too slow", "They cannot be programmed", "They never make products"],
      "e": ["Many are fast.", "They are programmable by definition.", "They make many products."], "y": "Costs and job changes are real concerns."},
     {"q": "Why are robots used for bomb disposal?", "r": "They keep people away from danger", "w": ["They enjoy it", "Bombs cannot hurt robots", "They are cheaper than a broom"],
      "e": ["Robots have no feelings.", "A bomb can destroy a robot, but no life is lost.", "That is not the reason."], "y": "Dangerous work is a key use of robots."}], SRC),
   order("s3-5-loop", 3, "Put the steps of a delivery robot avoiding an obstacle in order.",
         ["The distance sensor detects an object ahead.", "The processor compares the distance with a set limit.", "The program decides to turn.",
          "The motors turn the wheels.", "The robot continues towards its destination."], hint="Sense, process, decide, act.", sources=SRC, review="authored")],
  learn=learn(
    [("What makes a robot",
      "A robot is a machine that can be programmed to sense what is around it and act on its own.\n"
      "• Sensors detect the surroundings: light, distance, touch, sound, temperature, cameras.\n• A controller (processor) runs a program that decides what to do.\n"
      "• Actuators carry out actions: motors, wheels, arms, grippers.\n• A power supply (battery or mains) runs it all.\n"
      "Sense → decide → act, again and again."),
     ("Where robots work",
      "• Industry: welding, painting and assembling cars, packing goods.\n• Medicine: surgical robots, robots that carry medicines in hospitals.\n"
      "• Homes: robot vacuum cleaners and lawn mowers.\n• Agriculture: drones that spray crops, harvesting robots.\n"
      "• Exploration and danger: Mars rovers, deep-sea robots, bomb-disposal robots, robots inside damaged nuclear plants."),
     ("For and against",
      "Advantages: they work without rest, very accurately, and can do dangerous, dirty or boring jobs.\n"
      "Disadvantages: they are expensive to buy, run and repair; they need power; they may replace some workers; and they can fail in situations their program did not expect.")],
    key_words=[("robot", "a programmable machine that senses and acts automatically"), ("sensor", "a device that detects something in the surroundings"),
               ("actuator", "a part that produces movement"), ("controller", "the processor running the robot's program")],
    examples=["Car-factory welding robot", "Robot vacuum cleaner", "Mars rover", "Crop-spraying drone"],
    mistake=("A robot must look like a human", "Most robots do not look human; they are built for their job",
             "What makes a robot is sensing, deciding and acting, not its shape.")))

# ---------------------------------------------------------------- 6. Control systems, VR and AR
L.lesson(D, S, 6, ("s3-6", "Control systems, virtual reality and augmented reality"), [5],
  "A computer control system uses sensors to monitor conditions, a processor to compare readings with a set value, and actuators to make changes; the cycle repeats (feedback).\n"
  "Examples: automatic doors, traffic lights, air conditioning and thermostats, greenhouse watering, automatic street lights.\n"
  "Virtual reality (VR): a fully computer-generated world that the user enters with a headset; used for games, training pilots and surgeons, virtual tours.\n"
  "Augmented reality (AR): computer information placed on top of the real world, usually through a phone camera or smart glasses; used for navigation arrows, furniture apps, educational models, games.",
  worked({"set": 24},
         "Describe how an air-conditioning control system keeps a room at {set} °C.",
         ["A temperature sensor measures the room temperature.", "The processor compares it with the set value of {set} °C.",
          "If it is higher, the processor switches the cooling on (actuator); if lower, it switches it off.", "The sensor keeps measuring, so the loop repeats (feedback)."],
         "Sensor → compare with {set} °C → switch cooling on or off → repeat"),
  [card("c3s6-1", "Control systems: sensor → processor (compare) → actuator, repeated.",
        ["A street light switches on when the light sensor reads 'dark'."], "s3-6-loop"),
   card("c3s6-2", "VR replaces the real world with a computer-made one.",
        ["A headset shows a {3}-D virtual classroom."], "s3-6-vrar"),
   card("c3s6-3", "AR adds computer information to the real world.",
        ["A phone shows arrows on the street for directions."], "s3-6-which")],
  [bank("s3-6-loop", 1, "{X.q}", [
     {"q": "In an automatic door, what is the sensor?", "r": "a motion (infrared) sensor above the door", "w": ["the motor that opens the door", "the door handle", "the glass"],
      "e": ["The motor is the actuator.", "A handle is manual.", "Glass does not sense."], "y": "It detects a person approaching."},
     {"q": "What does the processor do in a control system?", "r": "Compares sensor readings with set values and decides what to do", "w": ["Measures the temperature", "Moves the parts", "Supplies the power"],
      "e": ["Sensors measure.", "Actuators move.", "The power supply does that."], "y": "It is the decision-maker."},
     {"q": "Why is a control system called a feedback loop?", "r": "The result of each action is measured again by the sensor", "w": ["It feeds people", "It only works once", "It has no sensors"],
      "e": ["It is not about food.", "It repeats continuously.", "Sensors are essential."], "y": "Measure, act, measure again."}], SRC),
   bank("s3-6-vrar", 1, "Is this VR or AR? {X.q}", [
     {"q": "A trainee pilot wears a headset and flies in a fully computer-made sky.", "r": "virtual reality (VR)", "w": ["augmented reality (AR)", "neither", "a control system"],
      "e": ["AR keeps the real world in view.", "It is a computer-made world.", "No sensors control a device here."], "y": "Fully virtual surroundings: VR."},
     {"q": "A phone camera shows the street with arrows drawn on it to guide you.", "r": "augmented reality (AR)", "w": ["virtual reality (VR)", "neither", "a robot"],
      "e": ["The real street is still visible.", "Information is added to the real view.", "Nothing moves by itself."], "y": "Information on top of the real world: AR."},
     {"q": "An app places a 3-D model of a heart on your desk through the phone camera.", "r": "augmented reality (AR)", "w": ["virtual reality (VR)", "a control system", "a deepfake"],
      "e": ["Your real desk is still seen.", "Nothing is being controlled.", "It is not fake news; it is a learning model."], "y": "A virtual object added to the real scene."}], SRC),
   bank("s3-6-which", 2, "Which control system fits? {X.q}", [
     {"q": "Plants in a greenhouse need water when the soil is dry.", "r": "a moisture sensor that switches on a water pump", "w": ["a light sensor that switches on a fan", "a sound sensor that opens a door", "a motion sensor that switches on a radio"],
      "e": ["Light is not the problem.", "Sound is not relevant.", "Motion is not relevant."], "y": "Measure soil moisture; act with a pump."},
     {"q": "Street lights in Limbe should come on at dusk.", "r": "a light sensor that switches on the lamps when it gets dark", "w": ["a temperature sensor", "a moisture sensor", "a weight sensor"],
      "e": ["Temperature does not show dusk reliably.", "Moisture is not relevant.", "Weight is not relevant."], "y": "Light level decides when to switch."},
     {"q": "A room must not get warmer than 26 °C.", "r": "a temperature sensor controlling a fan or air conditioner", "w": ["a light sensor controlling the lamps", "a motion sensor controlling the door", "a moisture sensor controlling a pump"],
      "e": ["Light does not measure temperature.", "Doors do not control heat directly.", "Moisture is not temperature."], "y": "Sense temperature; act by cooling."}], SRC),
   bank("s3-6-adv", 3, "{X.q}", [
     {"q": "Why is VR useful for training surgeons?", "r": "They can practise many times without risk to real patients", "w": ["It replaces medical school", "Patients prefer it", "It is cheaper than any book"],
      "e": ["It supports, not replaces, training.", "Patients are not involved.", "That is not the main reason."], "y": "Safe, repeatable practice."},
     {"q": "Which is a disadvantage of VR headsets?", "r": "Some users feel dizzy and they can be expensive", "w": ["They show nothing", "They only work outdoors", "They make phones faster"],
      "e": ["They show a virtual world.", "They work indoors.", "That is not related."], "y": "Motion sickness and cost are common problems."},
     {"q": "Why are computer control systems used for traffic lights?", "r": "They react to traffic and work all day without a person", "w": ["They stop all cars", "They need a police officer at each light", "They work only at night"],
      "e": ["They manage traffic, not stop it.", "They work automatically.", "They work all the time."], "y": "Sensors can detect queues and change timings."}], SRC)],
  learn=learn(
    [("Computers in control",
      "Many everyday machines are run by computer control systems:\n• sensors measure a condition (temperature, light, movement, moisture);\n"
      "• a processor compares the reading with a set (target) value and decides;\n• actuators make a change (switch a fan, motor, pump or lamp on or off).\n"
      "The sensor keeps measuring, so the system checks the effect of its own action: this is feedback. Examples: automatic doors, traffic lights, thermostats, greenhouse watering, automatic street lights."),
     ("Virtual reality (VR)",
      "VR replaces what you see and hear with a computer-made world. You wear a headset with a screen for each eye and often hold controllers.\n"
      "It is used for games, training pilots, drivers and surgeons safely, and visiting places you cannot travel to. Some people feel dizzy, and headsets can be expensive."),
     ("Augmented reality (AR)",
      "AR keeps the real world in view and adds computer information on top, usually through a phone camera or smart glasses.\n"
      "Examples: navigation arrows on the street, apps that show how a sofa would look in your room, {3}-D models of the heart on your desk, and games that place characters in your surroundings.\n"
      "Remember: VR = a new world; AR = extra information on the real world.")],
    key_words=[("control system", "a system that senses, decides and acts automatically"), ("feedback", "measuring the result of an action and using it to decide the next action"),
               ("virtual reality", "a fully computer-generated world"), ("augmented reality", "computer information added to the real world")],
    examples=["Thermostat: temperature sensor + air conditioner", "VR: pilot training", "AR: navigation arrows on the phone camera"],
    mistake=("AR and VR are the same", "VR replaces the real world; AR adds to it",
             "In AR you still see your real surroundings.")))
