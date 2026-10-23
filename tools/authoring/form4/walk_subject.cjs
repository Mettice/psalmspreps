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
  if (!subject?.startsWith('f4-')) throw Error('Pass a Form Four subject id');
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  try {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 }, reducedMotion: 'reduce' });
    const dir = path.join(root, 'tools/prototype');
    let found = false;
    for (const file of fs.readdirSync(dir).filter((f) => /^form4-term-1(?:-part-\d+)?\.html$/.test(f))) {
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
    await page.evaluate(fs.readFileSync(path.join(root, 'tools/authoring/walk.js'), 'utf8'));
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
      const labels = subject === 'f4-french' ? ['Ton objectif et les liens', 'À la fin', 'Acquis mobilisés :', 'Pour la suite :'] : ['Your goal and connections', 'By the end', 'Builds on:', 'Leads to:'];
      for (const label of labels) {
        if (!text.includes(label)) throw Error(`${subject}:${n}: missing visible ${label}`);
      }
    }
    await page.evaluate((id) => openLesson(id, LESSONS[id][0]), subject);
    const shot = path.join(os.tmpdir(), `${subject}-goal.png`);
    await page.screenshot({ path: shot, fullPage: true });
    console.log('Goal screenshot: ' + shot);
    if (subject === 'f4-french') {
      await page.evaluate((id) => openLesson(id, 4), subject);
      await page.getByRole('button', { name: 'Suivant', exact: true }).click();
      await page.getByRole('button', { name: 'Suivant', exact: true }).click();
      if (await page.getByRole('img', { name: /Scène scolaire inventée/ }).count() !== 1) throw Error('Missing French classroom scene');
      const sceneShot = path.join(os.tmpdir(), `${subject}-scene.png`);
      await page.screenshot({ path: sceneShot, fullPage: true });
      console.log('Scene screenshot: ' + sceneShot);
    }
    if (subject === 'f4-geography') {
      for (const [n, name, suffix] of [[3, /Illustrative soil profile/, 'profile'], [5, /Classroom erosion priority map/, 'erosion'], [11, /Invented monthly rainfall chart/, 'rainfall']]) {
        await page.evaluate(({id,n}) => openLesson(id,n), {id:subject,n});
        await page.getByRole('button', { name: 'Next', exact: true }).click();
        await page.getByRole('button', { name: 'Next', exact: true }).click();
        if (await page.getByRole('img', { name }).count() !== 1) throw Error('Missing Geography figure: '+suffix);
        const figureShot=path.join(os.tmpdir(), `${subject}-${suffix}.png`);
        await page.screenshot({ path:figureShot, fullPage:true });
        console.log('Geography screenshot: '+figureShot);
      }
    }
    if (subject === 'f4-history') {
      await page.evaluate((id) => openLesson(id, 14), subject);
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      const text = await page.locator('body').innerText();
      for (const label of ['General Assembly', 'Trusteeship Council', 'petitions']) if (!text.includes(label)) throw Error('Missing trusteeship distinction: ' + label);
      const historyShot = path.join(os.tmpdir(), `${subject}-trusteeship.png`);
      await page.screenshot({ path: historyShot, fullPage: true });
      console.log('Trusteeship screenshot: ' + historyShot);
    }
    if (subject === 'f4-english') {
      await page.evaluate((id) => openLesson(id, 19), subject);
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      const text = await page.locator('body').innerText();
      for (const label of ['chair', 'judge', '/tʃ/', '/dʒ/']) if (!text.includes(label)) throw Error('Missing pronunciation model: ' + label);
      const phoneticShot = path.join(os.tmpdir(), `${subject}-sounds.png`);
      await page.screenshot({ path: phoneticShot, fullPage: true });
      console.log('Sound model screenshot: ' + phoneticShot);
    }
    if (subject === 'f4-logic') {
      await page.evaluate((id) => openLesson(id, 6), subject);
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      if (await page.getByRole('img', { name: /Categorical Venn diagram/ }).count() !== 1) throw Error('Missing Venn diagram');
      const diagramShot = path.join(os.tmpdir(), `${subject}-venn.png`);
      await page.screenshot({ path: diagramShot, fullPage: true });
      console.log('Venn screenshot: ' + diagramShot);
    }
    if (subject === 'f4-economics') {
      await page.evaluate((id) => openLesson(id, 7), subject);
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      await page.getByRole('button', { name: 'Next', exact: true }).click();
      if (await page.getByRole('img', { name: /Classroom capital reconciliation/ }).count() !== 1) throw Error('Missing capital table');
      const capitalShot = path.join(os.tmpdir(), `${subject}-capital.png`);
      await page.screenshot({ path: capitalShot, fullPage: true });
      console.log('Capital screenshot: ' + capitalShot);
    }
  } finally { await browser.close(); }
})().catch((e) => { console.error(e); process.exitCode = 1; });
