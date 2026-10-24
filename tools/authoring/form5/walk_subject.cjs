// Form Five phone-width browser check using the repository's walker.
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
  if (!subject?.startsWith('f5-')) throw Error('Pass a Form Five subject id');
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  try {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 }, reducedMotion: 'reduce' });
    const dir = path.join(root, 'tools/prototype');
    let found = false;
    for (const file of fs.readdirSync(dir).filter((f) => /^form5-term-1(?:-part-\d+)?\.html$/.test(f))) {
      await page.goto(pathToFileURL(path.join(dir, file)).href);
      if (await page.evaluate((id) => typeof LESSONS !== 'undefined' && LESSONS[id]?.length > 0, subject)) { found = true; break; }
    }
    if (!found) throw Error(`No built Term One page contains ${subject}`);
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
      const labels = ['f5-french','f5-francais-intensif'].includes(subject) ? ['Ton objectif et les liens', 'À la fin', 'Acquis mobilisés :', 'Pour la suite :'] : ['Your goal and connections', 'By the end', 'Builds on:', 'Leads to:'];
      for (const label of labels) {
        if (!text.includes(label)) throw Error(`${subject}:${n}: missing visible ${label}`);
      }
    }
    await page.evaluate((id) => openLesson(id, LESSONS[id][0]), subject);
    const shot = path.join(os.tmpdir(), `${subject}-goal.png`);
    await page.screenshot({ path: shot, fullPage: true });
    console.log('Goal screenshot: ' + shot);
    if (subject === 'f5-english') {
      await page.evaluate((id) => openLesson(id, 12), subject);
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      const text = await page.locator('body').innerText();
      for (const label of ['pin/bin', 'fan/van', '/p/', '/v/']) if (!text.includes(label)) throw Error('Missing sound model: '+label);
      const soundShot=path.join(os.tmpdir(), `${subject}-sounds.png`);
      await page.screenshot({path:soundShot,fullPage:true});
      console.log('Sound screenshot: '+soundShot);
    }
    if (subject === 'f5-logic') {
      await page.evaluate((id) => openLesson(id, 5), subject);
      await page.getByRole('button', {name:'Next',exact:true}).click();
      await page.getByRole('button', {name:'Next',exact:true}).click();
      if (await page.getByRole('img', {name:/Square of opposition assuming S exists/}).count() !== 1) throw Error('Missing square');
      const squareShot=path.join(os.tmpdir(), `${subject}-square.png`);
      await page.screenshot({path:squareShot,fullPage:true});
      console.log('Square screenshot: '+squareShot);
    }
    if (subject === 'f5-economics') {
      for (const [n,label] of [[5,/Invented fixed stationery basket/],[12,/Invented bank balance sheet/],[15,/Invented three-bank/]]) {
        await page.evaluate(({id,n}) => openLesson(id,n), {id:subject,n});
        await page.getByRole('button', {name:'Next',exact:true}).click();
        await page.getByRole('button', {name:'Next',exact:true}).click();
        if (await page.getByRole('img', {name:label}).count()!==1) throw Error('Missing record '+n);
        const tableShot=path.join(os.tmpdir(), `${subject}-record-${n}.png`);
        await page.screenshot({path:tableShot,fullPage:true});
        console.log('Record screenshot: '+tableShot);
      }
    }
  } finally { await browser.close(); }
})().catch((e) => { console.error(e); process.exitCode = 1; });
