// Form Four phone-width browser check using the repository's walker.
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createRequire } = require('node:module');
const req = createRequire('C:/Users/efuet/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/entry.js');
const { chromium } = req('playwright');
const root = path.resolve(__dirname, '../../..');
(async () => {
  const subject = process.argv[2];
  if (subject !== 'f2-french') throw Error('Pass f2-french');
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  try {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 }, reducedMotion: 'reduce' });
    const dir = path.join(root, 'tools/prototype');
    let found = false;
    for (const file of fs.readdirSync(dir).filter((f) => /^form2-term-3(?:-part-\d+)?\.html$/.test(f))) {
      await page.goto(pathToFileURL(path.join(dir, file)).href);
      if (await page.evaluate((id) => typeof LESSONS !== 'undefined' && LESSONS[id]?.length > 0, subject)) { found = true; break; }
    }
    if (!found) throw Error(`No built Term Three page contains ${subject}`);
    await page.evaluate(() => {
      window.__overflowScreens = [];
      new MutationObserver(() => {
        if (document.documentElement.scrollWidth > 362 && window.__overflowScreens.length < 20)
          window.__overflowScreens.push(document.body.innerText.slice(0, 180));
      }).observe(document.body, { childList: true, subtree: true, characterData: true });
    });
    await page.evaluate((id) => { window.__only = [id]; }, subject);
    // Keep the shared walker untouched. Miss every first try, but answer later
    // card retries correctly so the app's two-missed-card stop guard stays intact.
    // The first card and every practice item still show the full reveal path.
    const cardRetry = `
      const flow = C()?.flow, step = flow?.steps[flow.step];
      const visibleOptions = [...document.querySelectorAll('button.option')];
      if (step?.kind === 'card' && step.card > 0 && flow.phase === 'check' && flow.attempt === 1 && visibleOptions.length) {
        const prompt = document.querySelector('.prompt')?.textContent;
        const texts = visibleOptions.map((b) => b.textContent).sort().join('|');
        let answer;
        for (let offset = 0; offset < 500; offset++) {
          const candidate = teach.itemQuestion(L(), { ...flow, seed: flow.seed + offset }, LIB());
          if (candidate.prompt === prompt && candidate.options?.map((o) => o.text).sort().join('|') === texts) {
            answer = candidate.answer; break;
          }
        }
        const correct = visibleOptions.find((b) => b.textContent === answer);
        if (!correct) throw Error('Cannot resolve the visible card retry');
        correct.click(); continue;
      }
    `;
    const walk = fs.readFileSync(path.join(root, 'tools/authoring/walk.js'), 'utf8')
      .replace('const inp = document.querySelector', cardRetry + '\nconst inp = document.querySelector');
    await page.evaluate(walk);
    await page.waitForFunction(() => window.__walk && !window.__walk.running, null, { timeout: 300000 });
    const result = await page.evaluate(() => window.__walk.result);
    console.log(subject + ': ' + result);
    if (!/^(\d+)\/\1 lessons clean\nerrors 0\s*$/.test(result)) throw Error('Browser walk failed');
    const overflow = await page.evaluate(() => window.__overflowScreens);
    if (overflow.length) throw Error('Phone-width overflow: ' + JSON.stringify(overflow));
    console.log('All walked screens fit the phone viewport');
    for (const n of await page.evaluate((id) => LESSONS[id], subject)) {
      await page.evaluate(({ id, n }) => openLesson(id, n), { id: subject, n });
      const text = await page.locator('body').innerText();
      const labels = ['f2-french'].includes(subject) ? ['Ton objectif et les liens', 'À la fin', 'Acquis mobilisés :', 'Pour la suite :'] : ['Your goal and connections', 'By the end', 'Builds on:', 'Leads to:'];
      for (const label of labels) {
        if (!text.includes(label)) throw Error(`${subject}:${n}: missing visible ${label}`);
      }
    }
    await page.evaluate((id) => openLesson(id, LESSONS[id][0]), subject);
    const shot = path.join(os.tmpdir(), `${subject}-goal.png`);
    await page.screenshot({ path: shot, fullPage: true });
    console.log('Goal screenshot: ' + shot);
    await page.evaluate((id) => openLesson(id, 75), subject);
    await page.getByRole('button', { name: 'Suivant', exact: true }).click();
    await page.getByRole('button', { name: 'Suivant', exact: true }).click();
    const soundText = await page.locator('body').innerText();
    for (const word of ['parfum', 'commun', '[ɛ̃]', '[œ̃]']) if (!soundText.includes(word)) throw Error('Missing sound model: '+word);
    const soundsShot=path.join(os.tmpdir(),`${subject}-nasal-model.png`);
    await page.screenshot({path:soundsShot,fullPage:true});
    console.log('Nasal model screenshot: '+soundsShot);
  } finally { await browser.close(); }
})().catch((e) => { console.error(e); process.exitCode = 1; });
