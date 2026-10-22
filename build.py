"""Builds index.html for the RJ Tasks homepage (GitHub Pages).
Run after dropping a new release zip into downloads/:  python3 build.py
"""
import json, os, glob
from illustrations import ILL_DOWNLOAD, ILL_EXTRACT, ILL_ADDRESS, ILL_DEVMODE, ILL_LOAD, ILL_PIN

VERSION = "1.1.0"
UPDATED = "October 22, 2026"
ZIP = f"rj-tasks-{VERSION}.zip"
FOLDER = f"rj-tasks-{VERSION}"
size_kb = round(os.path.getsize(f"downloads/{ZIP}") / 1024)

html = open("template.html").read()
for k, v in {
    "{{ILL_DOWNLOAD}}": ILL_DOWNLOAD, "{{ILL_EXTRACT}}": ILL_EXTRACT, "{{ILL_ADDRESS}}": ILL_ADDRESS,
    "{{ILL_DEVMODE}}": ILL_DEVMODE, "{{ILL_LOAD}}": ILL_LOAD, "{{ILL_PIN}}": ILL_PIN,
    "{{VERSION}}": VERSION, "{{UPDATED}}": UPDATED, "{{ZIP}}": ZIP, "{{FOLDER}}": FOLDER, "{{ZIPKB}}": str(size_kb),
}.items():
    html = html.replace(k, v)
assert "{{" not in html, "unfilled placeholder"
open("index.html", "w").write(html)
print("index.html", len(html), "bytes;", ZIP, size_kb, "KB")
