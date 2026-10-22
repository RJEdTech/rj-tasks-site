# RJ Tasks homepage

Public homepage and download for **RJ Tasks**, the Regis Jesuit Microsoft Edge extension that shows students what's due and what to work on next in Canvas.

Live at: https://rjedtech.github.io/rj-tasks-site/

The extension source is kept in a separate private repository. This repo holds only the page, screenshots and the release zip.

## Publish a new version
1. Copy the new `rj-tasks-<version>.zip` into `downloads/`.
2. Update `VERSION` and `UPDATED` at the top of `build.py`.
3. Run `python3 build.py` to regenerate `index.html`, then commit and push.

The Edge screens on the page are drawn illustrations (`illustrations.py`). The Canvas screenshots in `assets/` are real RJ Tasks screens with sample classes and assignments.

## Security
- Static files only. The page loads nothing from other hosts (fonts are self-hosted) and collects nothing.
- A Content-Security-Policy meta tag allows only this site's own scripts, styles, images and fonts; no inline script or style.
- `downloads/SHA256SUMS.txt` lists the hash of the release zip. `build.py` regenerates it.
- Ideas and problem reports go to an RJ-only Microsoft Form, never to this site.
