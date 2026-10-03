# Progression sheets (not in the repository)

The official MINESEC 2026-27 Form 1 progression sheets (`progression_form-1_<subject>_annuel.pdf`)
are kept only on the maintainer's computer and are not published here.

Everything built from them **is** in the repository: `data/spine/raw/` (the parsed sheets),
`data/spine/*.json` (after the approved overrides) and `data/spine/issues.md`. The tests and the app
work without the PDFs.

To re-parse the sheets, put the PDFs in this folder and run:

```bash
pip install -r requirements.txt
python tools/spine/build.py
```
