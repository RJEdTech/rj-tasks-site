"""Builds site/index.html: the RJ Tasks for Students install page.

Edge screens are drawn as SVG illustrations (labelled as such on the page)
so they contain no one's real extensions, tabs or accounts. The Canvas images
are real screenshots of RJ Tasks for Students running against the mock Canvas.
Run: python3 build_page.py  ->  index.html
"""

FONT = "Segoe UI, system-ui, -apple-system, sans-serif"

# Edge light-theme colours used only inside the illustrations (they depict a screen).
E = {
    "frame": "#e9eaee", "tab": "#ffffff", "bar": "#ffffff", "field": "#f2f3f5",
    "text": "#1b1b1b", "muted": "#5f6368", "line": "#d6d8dd", "blue": "#0f6cbd",
    "page": "#f7f7f8", "hl": "#e8590c", "toggleoff": "#8a8886",
}


def chrome(w, h, url, body, tab="New tab", puzzle_active=False):
    """An Edge window with tab strip, address bar and toolbar."""
    p = []
    p.append(f'<rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="{E["frame"]}"/>')
    # tab
    p.append(f'<rect x="12" y="8" width="190" height="30" rx="7" fill="{E["tab"]}"/>')
    p.append(f'<circle cx="28" cy="23" r="6" fill="{E["blue"]}" opacity=".85"/>')
    p.append(f'<text x="42" y="27.5" font-size="12" fill="{E["text"]}">{tab}</text>')
    p.append(f'<text x="214" y="28" font-size="16" fill="{E["muted"]}">+</text>')
    # toolbar
    p.append(f'<rect x="0" y="38" width="{w}" height="44" fill="{E["bar"]}"/>')
    p.append(f'<text x="16" y="66" font-size="16" fill="{E["muted"]}">←  →  ↻</text>')
    p.append(f'<rect x="96" y="47" width="{w-200}" height="28" rx="14" fill="{E["field"]}"/>')
    p.append(f'<text x="114" y="66" font-size="13" fill="{E["text"]}" font-family="Consolas, monospace">{url}</text>')
    # puzzle (Extensions) button
    px = w - 88
    if puzzle_active:
        p.append(f'<rect x="{px-8}" y="47" width="30" height="28" rx="6" fill="#dfe6f3"/>')
    p.append(puzzle(px, 52, E["text"]))
    p.append(f'<text x="{w-46}" y="67" font-size="16" fill="{E["muted"]}">⋯</text>')
    p.append(f'<rect x="0" y="82" width="{w}" height="{h-82}" fill="{E["page"]}"/>')
    p.append(f'<path d="M0 82 H{w} V{h-10} a10 10 0 0 1 -10 10 H10 a10 10 0 0 1 -10 -10 Z" fill="{E["page"]}"/>')
    p.append(body)
    return p


def puzzle(x, y, color):
    # simple puzzle-piece glyph, ~16px
    return (f'<path transform="translate({x},{y})" fill="none" stroke="{color}" stroke-width="1.6" '
            'd="M3 4h3.2a2 2 0 1 1 3.6 0H13v3.2a2 2 0 1 1 0 3.6V14H9.8a2 2 0 1 0-3.6 0H3v-3.2a2 2 0 1 0 0-3.6Z"/>')


def toggle(x, y, on, highlight=False):
    out = []
    if highlight:
        out.append(f'<rect x="{x-8}" y="{y-8}" width="56" height="36" rx="18" fill="none" stroke="{E["hl"]}" stroke-width="3"/>')
    out.append(f'<rect x="{x}" y="{y}" width="40" height="20" rx="10" fill="{E["blue"] if on else "#ffffff"}" stroke="{E["blue"] if on else E["toggleoff"]}" stroke-width="1.5"/>')
    cx = x + 30 if on else x + 10
    out.append(f'<circle cx="{cx}" cy="{y+10}" r="6" fill="{"#ffffff" if on else E["toggleoff"]}"/>')
    return "".join(out)


def callout(x, y, n):
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="{E["hl"]}"/>'
            f'<text x="{x}" y="{y+5}" font-size="14" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')


def svg(w, h, parts, label):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}" '
            f'font-family="{FONT}" xmlns="http://www.w3.org/2000/svg">' + "".join(parts) + "</svg>")


W, H = 640, 360

# 1 — download finished (Edge downloads flyout)
body = (
    f'<rect x="300" y="88" width="320" height="150" rx="8" fill="#fff" stroke="{E["line"]}"/>'
    f'<text x="318" y="114" font-size="14" font-weight="600" fill="{E["text"]}">Downloads</text>'
    f'<rect x="312" y="128" width="296" height="62" rx="6" fill="#f3f6fb"/>'
    f'<rect x="324" y="140" width="28" height="36" rx="3" fill="#ffe8a3" stroke="#c9a227"/>'
    f'<text x="331" y="163" font-size="9" fill="#7a5d00" font-weight="700">ZIP</text>'
    f'<text x="364" y="155" font-size="13" font-weight="600" fill="{E["text"]}">rj-tasks-1.1.0.zip</text>'
    f'<text x="364" y="174" font-size="12" fill="{E["muted"]}">198 KB · Done</text>'
    f'<text x="364" y="216" font-size="12.5" fill="{E["blue"]}">Show in folder</text>'
    f'<rect x="352" y="198" width="114" height="28" rx="6" fill="none" stroke="{E["hl"]}" stroke-width="3"/>'
    + callout(484, 212, "1")
    + f'<text x="24" y="130" font-size="13" fill="{E["muted"]}">After you save it, Edge shows</text>'
    + f'<text x="24" y="150" font-size="13" fill="{E["muted"]}">the file in its Downloads list.</text>'
)
ILL_DOWNLOAD = svg(W, H - 100, chrome(W, H - 100, "rjedtech.github.io/rj-tasks-site", body, tab="RJ Tasks for Students"), "Edge downloads list showing rj-tasks-1.1.0.zip with Show in folder highlighted")

# 2 — extract all (File Explorer)
fe = []
fe.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="10" fill="#f3f3f3"/>')
fe.append(f'<rect x="0" y="0" width="{W}" height="40" rx="10" fill="#e9eaee"/>')
fe.append(f'<text x="18" y="26" font-size="13" fill="{E["text"]}">📁  Downloads</text>')
fe.append(f'<rect x="0" y="40" width="150" height="{H-40}" fill="#f9f9f9"/>')
for i, t in enumerate(["Home", "Desktop", "Downloads", "Documents"]):
    fe.append(f'<text x="20" y="{72+i*26}" font-size="12.5" fill="{E["text"]}" font-weight="{600 if t=="Downloads" else 400}">{t}</text>')
fe.append(f'<rect x="166" y="58" width="300" height="30" rx="4" fill="#cce4f7"/>')
fe.append(f'<rect x="176" y="64" width="16" height="19" rx="2" fill="#ffe8a3" stroke="#c9a227"/>')
fe.append(f'<text x="202" y="78" font-size="12.5" fill="{E["text"]}">rj-tasks-1.1.0.zip</text>')
# context menu
fe.append(f'<rect x="300" y="84" width="230" height="166" rx="8" fill="#fff" stroke="{E["line"]}"/>')
items = ["Open", "Open with", "Extract All…", "Share", "Copy as path", "Properties"]
for i, t in enumerate(items):
    y = 110 + i * 25
    if t == "Extract All…":
        fe.append(f'<rect x="306" y="{y-17}" width="218" height="24" rx="4" fill="#eef4fb"/>')
        fe.append(f'<rect x="304" y="{y-19}" width="222" height="28" rx="5" fill="none" stroke="{E["hl"]}" stroke-width="3"/>')
    fe.append(f'<text x="322" y="{y}" font-size="12.5" fill="{E["text"]}" font-weight="{600 if t=="Extract All…" else 400}">{t}</text>')
fe.append(callout(548, 160, "2"))
fe.append(f'<text x="166" y="290" font-size="12.5" fill="{E["muted"]}">Right-click the file, choose Extract All…, then Extract.</text>')
fe.append(f'<text x="166" y="312" font-size="12.5" fill="{E["muted"]}">You get a folder named rj-tasks-1.1.0.</text>')
ILL_EXTRACT = svg(W, H, fe, "Windows File Explorer with the zip file right-clicked and Extract All highlighted")

# 3 — address bar
body = (f'<rect x="92" y="43" width="{W-192}" height="36" rx="18" fill="none" stroke="{E["hl"]}" stroke-width="3"/>'
        + callout(W - 80, 30, "3")
        + f'<rect x="96" y="90" width="300" height="34" rx="6" fill="#fff" stroke="{E["line"]}"/>'
        + f'<text x="112" y="112" font-size="12.5" fill="{E["text"]}">edge://extensions</text>'
        + f'<text x="290" y="112" font-size="11.5" fill="{E["muted"]}">Press Enter</text>'
        + f'<text x="24" y="190" font-size="13" fill="{E["muted"]}">Click the address bar, type the address, press Enter.</text>')
ILL_ADDRESS = svg(W, 220, chrome(W, 220, "edge://extensions", body), "Edge address bar with edge://extensions typed in")


def ext_page(dev_on, highlight_toggle, highlight_load, folder_dialog=False, card=False):
    b = []
    # left pane
    b.append(f'<rect x="0" y="82" width="200" height="{H-82}" fill="#fff"/>')
    b.append(f'<text x="20" y="114" font-size="17" font-weight="600" fill="{E["text"]}">Extensions</text>')
    b.append(f'<rect x="16" y="126" width="168" height="26" rx="13" fill="{E["field"]}"/>')
    b.append(f'<text x="30" y="143" font-size="11" fill="{E["muted"]}">Search installed extensions</text>')
    b.append(f'<rect x="12" y="160" width="176" height="26" rx="5" fill="#eef4fb"/>')
    b.append(f'<text x="24" y="177" font-size="12.5" fill="{E["text"]}">Extensions</text>')
    b.append(f'<text x="24" y="203" font-size="12.5" fill="{E["text"]}">Keyboard shortcuts</text>')
    b.append(f'<line x1="16" y1="220" x2="184" y2="220" stroke="{E["line"]}"/>')
    b.append(f'<text x="20" y="246" font-size="11.5" fill="{E["text"]}">Allow extensions from</text>')
    b.append(f'<text x="20" y="261" font-size="11.5" fill="{E["text"]}">other stores</text>')
    b.append(toggle(140, 242, False))
    b.append(f'<text x="20" y="306" font-size="12.5" font-weight="600" fill="{E["text"]}">Developer mode</text>')
    b.append(toggle(140, 292, dev_on, highlight_toggle))
    if highlight_toggle:
        b.append(callout(178, 336, "4"))
    # main
    b.append(f'<text x="226" y="116" font-size="16" font-weight="600" fill="{E["text"]}">Installed extensions</text>')
    if dev_on:
        x = 226
        for t, wdt in (("Load unpacked", 112), ("Pack extension", 112), ("Update", 64)):
            b.append(f'<rect x="{x}" y="130" width="{wdt}" height="28" rx="5" fill="#fff" stroke="{E["line"]}"/>')
            b.append(f'<text x="{x+wdt/2}" y="148.5" font-size="12" fill="{E["text"]}" text-anchor="middle">{t}</text>')
            if t == "Load unpacked" and highlight_load:
                b.append(f'<rect x="{x-4}" y="126" width="{wdt+8}" height="36" rx="7" fill="none" stroke="{E["hl"]}" stroke-width="3"/>')
                b.append(callout(x + wdt + 2, 168, "5"))
            x += wdt + 10
    if card:
        b.append(f'<rect x="226" y="176" width="300" height="92" rx="8" fill="#fff" stroke="{E["line"]}"/>')
        b.append(f'<rect x="240" y="190" width="32" height="32" rx="7" fill="#1e293b"/>')
        b.append(f'<path d="M248 206 l5 5 l10 -11" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
        b.append(f'<text x="284" y="204" font-size="13.5" font-weight="600" fill="{E["text"]}">RJ Tasks for Students  1.2.0</text>')
        b.append(f'<text x="284" y="222" font-size="11" fill="{E["muted"]}">See what\'s due and what to work on next…</text>')
        b.append(f'<text x="240" y="254" font-size="11.5" fill="{E["blue"]}">Details    Remove    Reload</text>')
        b.append(toggle(470, 240, True))
    if folder_dialog:
        b.append(f'<rect x="300" y="168" width="320" height="176" rx="8" fill="#fff" stroke="#9aa0a6" stroke-width="1.2"/>')
        b.append(f'<text x="316" y="192" font-size="12.5" font-weight="600" fill="{E["text"]}">Select the extension directory</text>')
        b.append(f'<text x="316" y="216" font-size="11.5" fill="{E["muted"]}">Downloads ›</text>')
        b.append(f'<rect x="312" y="226" width="296" height="26" rx="4" fill="#cce4f7"/>')
        b.append(f'<text x="324" y="243" font-size="12" fill="{E["text"]}">📁 rj-tasks-1.1.0</text>')
        b.append(f'<text x="324" y="270" font-size="12" fill="{E["muted"]}">🗜 rj-tasks-1.1.0.zip</text>')
        b.append(f'<rect x="512" y="306" width="96" height="28" rx="5" fill="{E["blue"]}"/>')
        b.append(f'<text x="560" y="324.5" font-size="12" fill="#fff" text-anchor="middle">Select Folder</text>')
        b.append(f'<rect x="508" y="302" width="104" height="36" rx="7" fill="none" stroke="{E["hl"]}" stroke-width="3"/>')
    return chrome(W, H, "edge://extensions", "".join(b), tab="Extensions")


ILL_DEVMODE = svg(W, H, ext_page(True, True, False), "Edge Extensions page with the Developer mode switch at the lower left turned on")
ILL_LOAD = svg(W, H, ext_page(True, False, True, folder_dialog=True), "Load unpacked button highlighted and the folder picker with rj-tasks-1.1.0 selected")
ILL_LOADED = svg(W, H, ext_page(True, False, False, card=True), "RJ Tasks for Students shown on the Extensions page, switched on")

# 6 — pin to toolbar
body = (
    f'<rect x="{W-300}" y="84" width="280" height="168" rx="8" fill="#fff" stroke="{E["line"]}"/>'
    f'<text x="{W-284}" y="110" font-size="14" font-weight="600" fill="{E["text"]}">Extensions</text>'
    f'<rect x="{W-292}" y="124" width="264" height="36" rx="5" fill="#f3f6fb"/>'
    f'<rect x="{W-282}" y="131" width="22" height="22" rx="5" fill="#1e293b"/>'
    f'<path d="M{W-277} 142 l4 4 l7 -8" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>'
    f'<text x="{W-250}" y="147" font-size="12.5" fill="{E["text"]}">RJ Tasks for Students</text>'
    # eye icon
    f'<g transform="translate({W-70},134)"><path d="M0 8 C4 1 14 1 18 8 C14 15 4 15 0 8Z" fill="none" stroke="{E["text"]}" stroke-width="1.5"/>'
    f'<circle cx="9" cy="8" r="3" fill="{E["text"]}"/></g>'
    f'<rect x="{W-78}" y="126" width="34" height="32" rx="6" fill="none" stroke="{E["hl"]}" stroke-width="3"/>'
    f'<text x="{W-284}" y="186" font-size="11.5" fill="{E["blue"]}">Manage extensions</text>'
    + callout(W - 30, 112, "6")
    + f'<rect x="{W-96}" y="45" width="34" height="32" rx="6" fill="none" stroke="{E["hl"]}" stroke-width="3"/>'
    + f'<text x="24" y="130" font-size="13" fill="{E["muted"]}">Click the puzzle piece, then the</text>'
    + f'<text x="24" y="150" font-size="13" fill="{E["muted"]}">eye next to RJ Tasks for Students.</text>'
)
ILL_PIN = svg(W, 270, chrome(W, 270, "rjhs.instructure.com", body, tab="Dashboard", puzzle_active=True), "Edge Extensions menu with the eye icon next to RJ Tasks for Students highlighted")

