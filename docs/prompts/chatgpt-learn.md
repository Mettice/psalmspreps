# Prompt for ChatGPT: Learn screens for one lesson

Copy everything between the lines into ChatGPT, then paste one lesson file (e.g. `content/biology/7.json`) at the end.
One lesson per message works best. Save the JSON it returns as `.handoff/learn/<subject>-<n>.json`.

---

You are writing the "Learn" screens for one lesson of an offline app that teaches the Cameroon anglophone
secondary curriculum (GCE board). For many pupils this app is their main teacher. The lesson already has a short
note, three key-idea cards, a worked example and practice questions (pasted below as JSON). Pupils said it goes too
fast from a short definition to the questions. Your Learn screens come first and must really teach the topic.

Return ONLY a JSON object, no commentary, in exactly this shape:

{
 "status": "draft",
 "sections": [
  {"heading": "...", "text": "..."},
  {"heading": "...", "text": "..."}
 ],
 "key_words": [{"word": "...", "meaning": "..."}],
 "examples": ["...", "..."],
 "mistake": {"wrong": "...", "right": "...", "why": "..."}
}

Rules:
1. 2 to 4 sections, each at most 120 words; everything together at most 450 words. Use "\n" for a new line and
   "• " to start a bullet.
2. Plain English for a pupil of the class in the lesson's "class" field (French for a lesson whose "language" is "fr",
   with French typography). Short sentences. Explain why, not only what. Build from what the pupil knows.
3. Teach exactly the lesson's topic and agree with its note, cards and worked example. Do not add harder content.
4. Cameroonian context: names like Bih, Ayuk, Ngozi, Tabe, Nfor; places like Buea, Bamenda, Douala, Yaoundé,
   Limbe; money in FCFA; local foods, crops, markets and weather.
5. NO DIGITS ANYWHERE (no 0–9) in any field. Write numbers in words ("three", "half", "twenty-five") or avoid them.
   If the topic needs numbers to explain (maths, science), still write them in words and keep them small; the
   app's maintainers will turn them into computed numbers. Units in words too ("metres", "grams").
6. Never use the characters { or }.
7. key_words: 3 to 6 important words of the lesson with a one-line meaning each. examples: 2 to 4 short,
   concrete examples. mistake: the most common pupil mistake on this topic, the correct version, and why.
8. Be factually correct for the Cameroon syllabus. If something is uncertain or differs between textbooks, say
   so plainly at the end of the relevant section ("Ask your teacher which ... your school uses.").

Here is the lesson JSON:

---
