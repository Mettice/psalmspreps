"""Form 3 Computer Science, Term 1, rows 1-13 (AI, robots, control systems, internal components). Run: python tools/authoring/form3/cs_a.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
from lessonlib import mcq, num, card, worked, learn, order
from common import bank

L.use_class("form-3", "Form 3")
D, S = "computer-science", "computer-science"
SRC = ["computing-society"]

# ---------------------------------------------------------------- 1. Introduction to AI
L.lesson(D, S, 1, ("s3-1", "Introduction to Artificial Intelligence"), [],
  "Artificial Intelligence (AI) is the ability of a computer system to do tasks that normally need human intelligence: recognising speech and images, understanding language, learning from examples, making decisions.\n"
  "• Machine learning: the system learns patterns from large amounts of data instead of being given every rule.\n"
  "• Narrow (weak) AI does one kind of task (a spam filter, a chess program, a voice assistant); general AI that can do any intellectual task like a person does not yet exist.\n"
  "• AI systems need data, algorithms and computing power; they can make mistakes and copy biases in their data.",
  worked({},
         "Is a calculator an example of AI? Explain.",
         ["A calculator follows fixed rules that a programmer wrote; it does not learn or adapt.", "AI systems learn patterns from data or handle tasks like recognising speech.", "So a calculator is not AI."],
         "No: it follows fixed rules and does not learn"),
  [card("c3s1-1", "AI: computers doing tasks that normally need human intelligence.",
        ["Recognising faces in photos"], "s3-1-def"),
   card("c3s1-2", "Machine learning: learning patterns from data.",
        ["A spam filter learns from many marked e-mails."], "s3-1-ml"),
   card("c3s1-3", "Today's AI is narrow: each system does one kind of task.",
        ["A chess program cannot drive a car."], "s3-1-narrow")],
  [bank("s3-1-def", 1, "{X.q}", [
     {"q": "What is Artificial Intelligence?", "r": "Computer systems doing tasks that normally need human intelligence", "w": ["Any machine with a screen", "A robot that looks like a person", "Storing data on the internet"],
      "e": ["A screen does not make a machine intelligent.", "AI does not need a body or a human shape.", "That is cloud storage."], "y": "Examples: understanding speech, recognising images, making decisions."},
     {"q": "Which is an example of AI?", "r": "A phone app that recognises spoken words", "w": ["A desk calculator", "A light switch", "A printed timetable"],
      "e": ["A calculator follows fixed rules.", "A switch has no intelligence.", "A timetable is just data."], "y": "Speech recognition is a typical AI task."},
     {"q": "Which three things does an AI system need?", "r": "data, algorithms and computing power", "w": ["only electricity", "a keyboard, mouse and printer", "a human operator at all times"],
      "e": ["Electricity alone does nothing.", "Those are input/output devices.", "Many AI systems run automatically."], "y": "AI learns from data using algorithms run on powerful computers."}], SRC),
   bank("s3-1-ml", 1, "{X.q}", [
     {"q": "What is machine learning?", "r": "A way for computers to learn patterns from data", "w": ["Teaching machines to walk", "Repairing computers", "Typing faster"],
      "e": ["That is robotics.", "That is maintenance.", "That is a keyboard skill."], "y": "The more good examples, the better it learns."},
     {"q": "A spam filter is trained with thousands of e-mails marked 'spam' or 'not spam'. What is this data for?", "r": "To let the filter learn the patterns of spam", "w": ["To delete all e-mails", "To slow the computer", "To make the e-mails longer"],
      "e": ["It sorts e-mails; it does not delete all.", "That is not the aim.", "It does not change the e-mails."], "y": "Labelled examples teach the system."},
     {"q": "Why can an AI system trained on poor or one-sided data give unfair results?", "r": "It learns whatever patterns, including biases, are in its data", "w": ["Computers are always fair", "Data has no effect on AI", "AI ignores its training"],
      "e": ["They copy patterns from data.", "Data shapes what AI learns.", "Training is how AI learns."], "y": "Biased data gives biased AI."}], SRC),
   bank("s3-1-narrow", 2, "{X.q}", [
     {"q": "What is narrow (weak) AI?", "r": "AI that does one specific kind of task", "w": ["AI that can do any task a person can", "AI that is very small", "AI that works without data"],
      "e": ["That would be general AI, which does not yet exist.", "Size is not meant.", "AI needs data."], "y": "Every AI in use today is narrow."},
     {"q": "Which is NOT a task usually done by AI today?", "r": "Feeling emotions like a human", "w": ["Translating text", "Recognising faces", "Recommending videos"],
      "e": ["Translation apps use AI.", "Face recognition uses AI.", "Recommendation systems use AI."], "y": "AI imitates some intelligent tasks; it does not feel."},
     {"q": "An AI chess program beats a champion. Can it therefore drive a car?", "r": "No: it was built and trained only for chess", "w": ["Yes, it is intelligent", "Yes, if it has wheels", "Only at night"],
      "e": ["Its intelligence is narrow.", "Driving needs different training and sensors.", "Time of day is irrelevant."], "y": "Narrow AI does not transfer to other tasks."}], SRC),
   bank("s3-1-limit", 3, "{X.q}", [
     {"q": "Why should people check answers given by AI tools?", "r": "AI can make mistakes and give confident but wrong answers", "w": ["AI is never wrong", "Checking slows the computer", "AI answers are always copied"],
      "e": ["AI makes errors.", "Checking is about accuracy, not speed.", "Not always."], "y": "Human judgement is still needed."},
     {"q": "Which shows the difference between a normal program and an AI system?", "r": "The AI system improves its results by learning from new data", "w": ["The AI system has no instructions", "A normal program uses no electricity", "The AI system always uses a robot"],
      "e": ["AI still runs on algorithms.", "All programs need power.", "Most AI is software only."], "y": "Learning from data is the key difference."},
     {"q": "Self-driving cars use AI. What do they mainly need to learn from?", "r": "Large amounts of sensor data from real driving", "w": ["Only the driver's voice", "Paper maps", "The colour of the car"],
      "e": ["Voice alone cannot steer.", "Paper maps are not live data.", "Colour is irrelevant."], "y": "Cameras and sensors provide examples of roads, signs and people."}], SRC)],
  learn=learn(
    [("Machines that seem to think",
      "Artificial Intelligence (AI) is the ability of computer systems to do tasks that normally need human intelligence: recognising speech, understanding and translating language, recognising faces and objects, playing games and making decisions.\n"
      "A voice assistant on a phone, a translation app and a spam filter all use AI."),
     ("Learning from data",
      "Most modern AI uses machine learning. Instead of writing every rule, programmers give the system a lot of examples (data) and an algorithm that finds the patterns.\n"
      "A spam filter learns from thousands of e-mails marked 'spam' or 'not spam'; then it can sort new e-mails.\n"
      "AI needs three things: data, algorithms and computing power."),
     ("What AI can and cannot do",
      "All AI in use today is narrow: each system does one kind of task. A chess program cannot drive a car. General AI, able to do any task like a person, does not exist yet.\n"
      "AI can make mistakes and can copy unfairness hidden in its data, so its results must be checked by people.")],
    key_words=[("artificial intelligence", "computer systems doing tasks that need human-like intelligence"), ("machine learning", "learning patterns from data"),
               ("data", "facts and examples used to train a system"), ("narrow AI", "AI designed for one kind of task")],
    examples=["Voice typing on a phone", "Face unlock", "Video recommendations"],
    mistake=("Every computer program is AI", "Only systems that learn or do intelligent tasks are AI",
             "A calculator follows fixed rules; it does not learn.")))

# ---------------------------------------------------------------- 2. Applications of AI
L.lesson(D, S, 2, ("s3-2", "Applications of Artificial Intelligence in society"), [1],
  "AI is used in many areas:\n"
  "• Health: reading X-rays and scans, predicting disease outbreaks, chatbots giving health information.\n"
  "• Agriculture: apps that identify crop diseases from a photo (e.g. cassava or cocoa leaves), weather prediction, drones monitoring fields.\n"
  "• Education: tutoring apps that adapt to the learner, automatic translation.\n"
  "• Business and banking: fraud detection in mobile money, customer-service chatbots, recommendations.\n"
  "• Transport and security: navigation apps, traffic control, face recognition, self-driving vehicles.\n"
  "• Daily life: voice assistants, spam filters, smartphone cameras.",
  worked({},
         "A farmer near Bafoussam photographs a spotted cassava leaf with a phone app, which names the disease. Explain how AI helps here.",
         ["The app was trained on thousands of labelled photos of healthy and diseased leaves.", "It compares the new photo with the patterns it learned.", "It gives a likely diagnosis quickly, without an expert on the farm."],
         "Image recognition trained on labelled leaf photos"),
  [card("c3s2-1", "AI helps health workers read scans and spot diseases.",
        ["Detecting tuberculosis on chest X-rays"], "s3-2-area"),
   card("c3s2-2", "Farmers use AI apps to identify crop diseases from photos.",
        ["Cassava mosaic disease"], "s3-2-farm"),
   card("c3s2-3", "Banks use AI to detect fraud.",
        ["An unusual mobile-money transfer is flagged."], "s3-2-bank")],
  [bank("s3-2-area", 1, "In which area is AI being used here? {X.q}", [
     {"q": "A program highlights signs of tuberculosis on chest X-rays.", "r": "health", "w": ["agriculture", "banking", "entertainment"],
      "e": ["Crops are not involved.", "No money is involved.", "It is a medical use."], "y": "AI supports doctors in diagnosis."},
     {"q": "An app names the disease on a photographed cocoa pod.", "r": "agriculture", "w": ["health", "transport", "banking"],
      "e": ["It is about a crop, not a person.", "Nothing is being moved.", "No money is involved."], "y": "AI helps farmers protect crops."},
     {"q": "A mobile-money company blocks a strange transfer at 3 a.m.", "r": "banking (fraud detection)", "w": ["education", "health", "agriculture"],
      "e": ["Nothing is being taught.", "No medical use.", "No crops involved."], "y": "AI spots unusual patterns in transactions."}], SRC),
   bank("s3-2-farm", 1, "{X.q}", [
     {"q": "Which AI application helps a farmer most directly?", "r": "an app that identifies crop pests and diseases from photos", "w": ["a music recommendation app", "a video game", "a face filter for selfies"],
      "e": ["Music does not help crops.", "Games are entertainment.", "Face filters are entertainment."], "y": "Early diagnosis saves harvests."},
     {"q": "How can AI help farmers plan planting?", "r": "By predicting the weather from large amounts of data", "w": ["By planting the seeds itself always", "By changing the rain", "By making soil"],
      "e": ["Some robots plant, but planning uses prediction.", "AI cannot control rain.", "AI cannot make soil."], "y": "Forecasts help choose planting dates."},
     {"q": "Drones with cameras fly over large farms. What can AI do with their pictures?", "r": "Spot areas with sick plants or missing water", "w": ["Water the fields by itself", "Sell the crops", "Make the plants grow faster directly"],
      "e": ["The drone camera only collects images.", "Selling is a business task.", "AI cannot make plants grow."], "y": "Image analysis finds problems early."}], SRC),
   bank("s3-2-bank", 2, "{X.q}", [
     {"q": "How does AI help detect fraud in mobile money?", "r": "It learns normal spending patterns and flags unusual transactions", "w": ["It reads customers' minds", "It stops all transfers", "It prints receipts"],
      "e": ["AI uses data, not mind-reading.", "Most transfers are normal.", "Receipts are not fraud detection."], "y": "Unusual patterns may be fraud."},
     {"q": "A company's website answers customers' questions automatically at night. This is…", "r": "an AI chatbot", "w": ["a printer", "an antivirus", "a spreadsheet"],
      "e": ["A printer outputs paper.", "Antivirus protects against malware.", "A spreadsheet calculates."], "y": "Chatbots use AI to understand and reply to text."},
     {"q": "A navigation app suggests a faster route around traffic in Yaoundé. Which AI ability is used?", "r": "predicting traffic from live data", "w": ["recognising faces", "translating languages", "detecting crop disease"],
      "e": ["Faces are not involved.", "No translation is needed.", "No crops are involved."], "y": "It learns traffic patterns from many phones."}], SRC),
   bank("s3-2-choose", 3, "{X.q}", [
     {"q": "Which problem is AI LEAST suited to solve on its own?", "r": "deciding a fair punishment in a court case", "w": ["sorting spam e-mails", "recognising handwriting", "translating a menu"],
      "e": ["Spam sorting is a typical AI task.", "Handwriting recognition is a typical AI task.", "Translation is a typical AI task."], "y": "Justice needs human values and judgement."},
     {"q": "A school wants to give pupils extra practice that adapts to each one's level. Which AI use fits?", "r": "an adaptive tutoring app", "w": ["a face-recognition camera", "a fraud detector", "a self-driving bus"],
      "e": ["Cameras do not tutor.", "Fraud detection is for banks.", "Transport is not tutoring."], "y": "Adaptive apps choose the next question from the pupil's answers."},
     {"q": "Why do AI health tools still need doctors?", "r": "AI can be wrong, and doctors decide treatment and talk with patients", "w": ["AI tools are always right", "Doctors are faster than computers at everything", "AI cannot read data"],
      "e": ["AI makes mistakes.", "Not at everything.", "Reading data is what AI does."], "y": "AI supports, it does not replace, professional judgement."}], SRC)],
  learn=learn(
    [("AI around us",
      "AI is already in many everyday tools: voice typing, phone cameras that sharpen photos, video and music recommendations, spam filters and translation apps.\n"
      "It works best where there is a lot of data and a clear task."),
     ("AI in Cameroon's key sectors",
      "• Health: programs that read X-rays and scans, help diagnose tuberculosis or malaria, and predict outbreaks.\n"
      "• Agriculture: phone apps that identify diseases of cassava, maize or cocoa from a photo; weather forecasting; drones watching large farms.\n"
      "• Education: tutoring apps that adapt to each learner; automatic translation between English and French.\n"
      "• Business and banking: fraud detection in mobile money; chatbots answering customers."),
     ("Transport, security and choices",
      "Navigation apps predict traffic; some cities use AI to control traffic lights; face recognition is used for security; self-driving vehicles are being tested.\n"
      "AI suits tasks with clear patterns. For decisions that need human values, such as justice, people must stay in charge.")],
    key_words=[("application", "a practical use"), ("chatbot", "a program that holds a conversation in text or speech"),
               ("fraud detection", "spotting dishonest transactions"), ("image recognition", "identifying what is in a picture")],
    examples=["Cassava disease app", "Mobile-money fraud alert", "English-French translation app"],
    mistake=("AI can replace doctors completely", "AI helps doctors, who still make the decisions",
             "AI can be wrong; professionals check its results and care for patients.")))
