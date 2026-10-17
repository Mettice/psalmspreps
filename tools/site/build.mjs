// Builds the public site in site/ (published by Vercel and GitHub Pages). Every page is a folder's index.html,
// so links never end in .html:
//   site/index.html           https://psalmspreps.vercel.app/          the installable app (2026-10-17): a small core page,
//   site/subjects/<id>.js                                                one file per subject, a service worker for offline use,
//   site/sw.js, manifest.webmanifest, icons/                             a manifest and icons
//   site/offline.html         https://psalmspreps.vercel.app/offline   one self-contained file to share (Bluetooth, flash drive)
//   site/lesson3/index.html   https://psalmspreps.vercel.app/lesson3/  old link: sends the visitor to the app
//   node tools/site/build.mjs
import { execFileSync } from "node:child_process";
import { cpSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const ROOT = new URL("../../", import.meta.url);
const path = (p) => fileURLToPath(new URL(p, ROOT));

execFileSync(process.execPath, [path("tools/prototype/build.mjs")], { stdio: "inherit" });
rmSync(path("site"), { recursive: true, force: true });  // no leftovers from older layouts
cpSync(path("tools/prototype/pwa"), path("site"), { recursive: true });
mkdirSync(path("site/lesson3"), { recursive: true });
writeFileSync(path("site/lesson3/index.html"),
  '<!doctype html><meta charset="utf-8"><title>Form One Lessons</title><meta http-equiv="refresh" content="0; url=../"><a href="../">Open the Form One lessons</a>\n');
writeFileSync(path("site/.nojekyll"), "");  // serve files as they are
console.log("site/ ready: the installable app (index.html, subjects/, sw.js, manifest, icons), offline.html, lesson3/");
