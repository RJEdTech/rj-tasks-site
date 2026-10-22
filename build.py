"""Builds index.html for the RJ Tasks homepage (GitHub Pages).
Run after dropping a new release zip into downloads/:  python3 build.py
"""
import hashlib, os
from illustrations import ILL_DOWNLOAD, ILL_EXTRACT, ILL_ADDRESS, ILL_DEVMODE, ILL_LOAD, ILL_PIN

VERSION = "1.1.1"
UPDATED = "October 22, 2026"
ZIP = f"rj-tasks-{VERSION}.zip"
FOLDER = f"rj-tasks-{VERSION}"
size_kb = round(os.path.getsize(f"downloads/{ZIP}") / 1024)
SHA256 = hashlib.sha256(open(f"downloads/{ZIP}", "rb").read()).hexdigest()
FORM_URL = ("https://forms.cloud.microsoft/Pages/ResponsePage.aspx?"
            "id=4SwuQZc-CEClZjjFdYLisQzihhIB-7hPp9L3AOSeJONUMko2MlZGRzNET1YyTU8wNUM1SjUzN01LSC4u")
open("downloads/SHA256SUMS.txt", "w").write(f"{SHA256}  {ZIP}\n")

import re
ills = {k: re.sub(r"rj-tasks-\d+\.\d+\.\d+", FOLDER, v) for k, v in {
    "{{ILL_DOWNLOAD}}": ILL_DOWNLOAD, "{{ILL_EXTRACT}}": ILL_EXTRACT, "{{ILL_ADDRESS}}": ILL_ADDRESS,
    "{{ILL_DEVMODE}}": ILL_DEVMODE, "{{ILL_LOAD}}": ILL_LOAD, "{{ILL_PIN}}": ILL_PIN}.items()}
html = open("template.html").read()
for k, v in ills.items():
    html = html.replace(k, v)
for k, v in {
    "{{ILL_DOWNLOAD}}": ILL_DOWNLOAD, "{{ILL_EXTRACT}}": ILL_EXTRACT, "{{ILL_ADDRESS}}": ILL_ADDRESS,
    "{{ILL_DEVMODE}}": ILL_DEVMODE, "{{ILL_LOAD}}": ILL_LOAD, "{{ILL_PIN}}": ILL_PIN,
    "{{VERSION}}": VERSION, "{{UPDATED}}": UPDATED, "{{ZIP}}": ZIP, "{{FOLDER}}": FOLDER, "{{ZIPKB}}": str(size_kb), "{{SHA256}}": SHA256, "{{FORM_URL}}": FORM_URL.replace("&", "&amp;"),
}.items():
    html = html.replace(k, v)
assert "{{" not in html, "unfilled placeholder"
open("index.html", "w").write(html)
print("index.html", len(html), "bytes;", ZIP, size_kb, "KB")
