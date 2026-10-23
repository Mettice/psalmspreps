// Real-browser check of an authored subject using the repository's supplied walker.
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { createRequire } = require('node:module');
const requireRuntime = createRequire('C:/Users/efuet/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/entry.js');
const { chromium } = requireRuntime('playwright');
const root = path.resolve(__dirname, '../../..');
(async () => {
  const subject = process.argv[2];
  if (!subject?.startsWith('f3-')) throw Error('Pass a Form Three subject id');
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  try {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 } });
    await page.emulateMedia({ reducedMotion: 'reduce' });
    const prototypeDir = path.join(root, 'tools/prototype');
    const candidates = fs.readdirSync(prototypeDir).filter((f) => /^form3-term-1(?:-part-\d+)?\.html$/.test(f));
    let found = false;
    for (const file of candidates) {
      await page.goto(pathToFileURL(path.join(prototypeDir, file)).href);
      if (await page.evaluate((id) => typeof LESSONS !== 'undefined' && Array.isArray(LESSONS[id]) && LESSONS[id].length > 0, subject)) {
        found = true;
        break;
      }
    }
    if (!found) throw Error(`No built Term One page contains ${subject}`);
    await page.evaluate((id) => { window.__only = [id]; }, subject);
    await page.evaluate(fs.readFileSync(path.join(root, 'tools/authoring/walk.js'), 'utf8'));
    await page.waitForFunction(() => window.__walk && !window.__walk.running, null, { timeout: 300000 });
    const result = await page.evaluate(() => window.__walk.result);
    console.log(subject + ': ' + result);
    if (!/^(\d+)\/\1 lessons clean\nerrors 0\s*$/.test(result)) throw Error('Browser walk failed');
    await page.evaluate((id) => openLesson(id, LESSONS[id][0]), subject);
    const shot = path.join(os.tmpdir(), `${subject}-learn.png`);
    await page.screenshot({ path: shot, fullPage: true });
    console.log('Learn screenshot: ' + shot);
  } finally { await browser.close(); }
})().catch((e) => { console.error(e); process.exitCode = 1; });
