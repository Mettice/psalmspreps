// Browser walker: paste into the console of a built page (tools/prototype/form3-term-1.html …) at 360 px width.
// Set window.__only = ["f3-maths"] first to walk one subject. Answers every question wrongly or "I don't know",
// so every feedback, retry and working screen is shown. Read window.__walk.result when running is false.
window.__errs = []; window.addEventListener("error", (e) => window.__errs.push(String(e.message)));
window.__walk = { running: true };
(async () => {
  localStorage.clear(); state.readiness = { done: true };
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const PRI = ["I don't know", "Je ne sais pas", "Show the next step", "Voir l’étape suivante", "I'm ready for a question", "Je passe à la question", "Passe à l’activité", "Now try the activity", "Now practise", "À toi de t’exercer", "Now write", "Maintenant, écris", "I've written it", "J’ai écrit", "Terminé", "Now the key ideas", "Passons aux idées clés", "Done", "Try a new question", "Essayer une nouvelle question", "Let's try again", "A new question", "Continue", "Continuer", "Next", "Suivant", "Finish", "Terminer"];
  let total = 0, ok = 0; const out = [];
  for (const s of Object.keys(SUBJECTS).filter((k) => (window.__only || [k]).includes(k))) for (const n of LESSONS[s]) {
    total++; openLesson(s, n); let done = false, bad = null, alt = 0;
    for (let i = 0; i < 500; i++) {
      await sleep(1);
      const txt = document.body.innerText;
      if (txt.includes(`Lesson ${n} done`) || txt.includes(`Leçon ${n} terminée`)) { done = true; break; }
      if (/undefined|\bNaN\b|\[object|Infinity/.test(txt)) { bad = txt.match(/.{0,30}(undefined|NaN|\[object|Infinity).{0,30}/)[0]; break; }
      const inp = document.querySelector(".answer input");
      const chk = [...document.querySelectorAll("button")].find((b) => b.textContent === "Check" || b.textContent === "Vérifier");
      if (inp && chk && alt++ % 2 === 0) { inp.value = "999999"; chk.click(); continue; }
      const btns = [...document.querySelectorAll("button")]; let b = null;
      for (const p of PRI) { b = btns.find((x) => x.textContent.trim().startsWith(p) && !x.disabled); if (b) break; }
      if (!b) { bad = "stuck: " + btns.map((x) => x.textContent).join("/"); break; }
      b.click();
    }
    if (done && !bad && document.documentElement.scrollWidth <= 362) ok++; else out.push(`${s} ${n}: ${bad || (done ? "too wide" : "not done")}`);
    window.__walk.progress = `${s} ${n}`;
  }
  localStorage.clear();
  window.__walk = { running: false, result: [`${ok}/${total} lessons clean`, `errors ${window.__errs.length} ${[...new Set(window.__errs)].slice(0, 2).join(" | ")}`, ...out].join("\n") };
})();
"started"
