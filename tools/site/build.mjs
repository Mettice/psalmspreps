// Builds the public site in site/ (published by GitHub Pages). Every page is a folder's index.html,
// so links never end in .html:
//   site/index.html           https://psalmspreps.vercel.app/          (start here: Maths and English)
//   site/lesson3/index.html   https://psalmspreps.vercel.app/lesson3/  (old link, same app, kept so it still works)
//   node tools/site/build.mjs
import { execFileSync } from "node:child_process";
import { copyFileSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const ROOT = new URL("../../", import.meta.url);
const path = (p) => fileURLToPath(new URL(p, ROOT));

execFileSync(process.execPath, [path("tools/prototype/build.mjs")], { stdio: "inherit" });
rmSync(path("site"), { recursive: true, force: true });  // no leftovers from older layouts
mkdirSync(path("site/lesson3"), { recursive: true });
copyFileSync(path("tools/prototype/form1.html"), path("site/index.html"));
copyFileSync(path("tools/prototype/form1.html"), path("site/lesson3/index.html"));
writeFileSync(path("site/.nojekyll"), "");  // serve files as they are
console.log("site/ ready: index.html, lesson3/index.html");
