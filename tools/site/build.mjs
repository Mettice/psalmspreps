// Builds the public site in site/ (published by GitHub Pages):
//   site/index.html     the Lesson 3 prototype (readiness check → Lesson 3 → practice)
//   site/lesson3.html   the same page under its own name
//   node tools/site/build.mjs
import { execFileSync } from "node:child_process";
import { copyFileSync, mkdirSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const ROOT = new URL("../../", import.meta.url);
const path = (p) => fileURLToPath(new URL(p, ROOT));

execFileSync(process.execPath, [path("tools/prototype/build.mjs")], { stdio: "inherit" });
mkdirSync(path("site"), { recursive: true });
copyFileSync(path("tools/prototype/lesson3.html"), path("site/index.html"));
copyFileSync(path("tools/prototype/lesson3.html"), path("site/lesson3.html"));
writeFileSync(path("site/.nojekyll"), "");  // serve files as they are
console.log("site/ ready: index.html, lesson3.html");
