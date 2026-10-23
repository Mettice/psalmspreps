"""Reproducible concept lessons for Codex's assigned Form Three subjects.

Each term has its own definition, concrete application, false claim and correction.
Distractor feedback identifies the alternative concept rather than revealing a key.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
import banks_en as EN
import banks_fr as FR

ROOT = Path(__file__).resolve().parents[3]
L.use_class("form-3", "Form 3")


def plain(text):
    """{1884} → 1884 and {'B3'} → B3: Learn text is rendered, the note is not."""
    return re.sub(r"\{'([^'{}]*)'\}|\{(\d+)\}", lambda m: m.group(1) if m.group(1) is not None else m.group(2), text)


def fact(term, meaning, example, error, correction):
    return dict(term=term, meaning=meaning, example=example, error=error, correction=correction)


def concept_lesson(subject, prefix, n, title, overview, application, method, facts, source,
                   prerequisites=(), language="en", replacement=None, paper=None,
                   worked_override=None, learn_figure=None, lesson_subject=None, sections_override=None):
    assert len(facts) >= 4
    b = FR if language == "fr" else EN
    ident = f"{prefix}{n}"
    keys = [f["term"] for f in facts]
    definitions, cases, interpretations = [], [], []
    for i, f in enumerate(facts):
        other = [x for j, x in enumerate(facts) if j != i][:3]
        definitions.append(dict(q=("Quel terme désigne : " if language == "fr" else "Which term means: ") + f["meaning"] + " ?",
            r=f["term"], w=[x["term"] for x in other],
            e=[(f"« {x['term']} » désigne {x['meaning']}. Ici, cherche {f['meaning']}." if language == "fr" else
                f"{x['term']} means {x['meaning']}; the question instead describes {f['meaning']}.") for x in other],
            y=f["meaning"].capitalize() + "."))
        cases.append(dict(q=f["example"] + ("\nQuel terme s’applique le mieux ?" if language == "fr" else "\nWhich term best fits this example?"),
            r=f["term"], w=[x["term"] for x in other],
            e=[(f"« {x['term']} » concerne {x['meaning']}. Le cas décrit plutôt {f['meaning']}." if language == "fr" else
                f"{x['term']} concerns {x['meaning']}. This case instead illustrates {f['meaning']}.") for x in other],
            y=f["example"] + " " + f["meaning"].capitalize() + "."))
        interpretations.append(dict(q=f["example"] + ("\nQuelle explication justifie le classement ?" if language == "fr" else "\nWhich explanation justifies the classification?"),
            r=f["meaning"].capitalize() + ".", w=[x["meaning"].capitalize() + "." for x in other],
            e=[(f"Cette explication correspond à « {x['term']} ». Compare les indices du cas avec sa définition." if language == "fr" else
                f"That explanation describes {x['term']}, rather than the relationship illustrated in this example.") for x in other],
            y=f["correction"]))
    questions = [b.QA(f"{ident}-terms", 1, "{X.q}", definitions, [source]),
                 b.QA(f"{ident}-cases", 1, "{X.q}", cases, [source]),
                 b.QA(f"{ident}-reason", 2, "{X.q}", interpretations, [source]),
                 b.MT(f"{ident}-link", 2, "Relie chaque terme à son exemple." if language == "fr" else "Match each term to its example.",
                      [(f["term"], f["example"]) for f in facts], [source], pick=3),
                 b.SP(f"{ident}-repair", 3, "Repère l’affirmation fausse." if language == "fr" else "Find the incorrect claim.",
                      [f["term"] + (" : " if language == "fr" else ": ") + f["meaning"] + "." for f in facts],
                      [(f["error"], f["correction"]) for f in facts], [source])]
    for statement, f in zip(questions[4]["pool"]["right"], facts):
        statement["explain"] = (f"Cette affirmation est correcte : {f['term']} désigne {f['meaning']}. Cherche une affirmation qui contredit sa définition." if language == "fr" else
                                f"This statement is correct: {f['term']} means {f['meaning']}. Look for a claim that conflicts with its definition.")
    if replacement:
        for index, q in replacement.items():
            questions[index] = q
    cards = [L.card(f"c{ident}-terms", "Distingue les notions avant de les appliquer." if language == "fr" else "Distinguish the lesson's concepts before applying them.",
                    [f["term"] + ": " + f["meaning"] + "." for f in facts], questions[0]["id"]),
             L.card(f"c{ident}-cases", "Classe à partir des indices, pas d’un mot isolé." if language == "fr" else "Classify a case by its features, rather than by a familiar word alone.",
                    [facts[0]["example"], facts[0]["term"] + ": " + facts[0]["meaning"] + "."], questions[1]["id"]),
             L.card(f"c{ident}-repair", "Vérifie la relation entre l’affirmation et sa justification." if language == "fr" else "Check that a claim agrees with the rule or definition it uses.",
                    [facts[0]["error"], facts[0]["correction"]], questions[4]["id"])]
    note = plain(overview)  # the summary screen shows the note as written, so no {…} fields
    if len(note.split()) > 145:
        raise ValueError(f"{ident}: summary too long")
    sections = sections_override or [("Comprendre les notions" if language == "fr" else "Understand the ideas", overview),
                ("Appliquer dans une situation" if language == "fr" else "Apply the ideas locally", application),
                ("Raisonner et vérifier" if language == "fr" else "Reason and check", method)]
    if learn_figure:
        sections[1] = (*sections[1], learn_figure)
    L.lesson(subject, lesson_subject or subject, n, (ident, title), prerequisites, note,
        worked_override or L.worked({}, facts[0]["example"] + (" Quelle notion s’applique ?" if language == "fr" else " Which concept applies?"),
            [("Relève les indices." if language == "fr" else "Identify the features of the case."), facts[0]["meaning"].capitalize() + ".", facts[0]["correction"]], facts[0]["term"]),
        cards, questions, paper=paper, lang=language,
        learn=L.learn(sections, key_words=[(f["term"], f["meaning"]) for f in facts],
                      examples=[f["example"] for f in facts[:3]],
                      mistake=(facts[0]["error"], facts[0]["term"] + ": " + facts[0]["meaning"] + ".", facts[0]["correction"])))


def write_sources(subject, sources):
    folder = ROOT / "content" / "form-3" / subject
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "sources.json").write_text(json.dumps(sources, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def paper(prompt, model, checklist):
    return dict(vars={}, prompt=prompt, model=model, checklist=checklist, checks=[])
