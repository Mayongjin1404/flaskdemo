# Flask + Wikipedia Demo (Modified)

This is a modified version to satisfy CP1404 prac tasks.

## What I changed

- Added a base template `layout.html` with a simple navigation bar.
- Implemented a proper **About** page (`about.html`) and linked it in the nav.
- On the results page, the **page title is now displayed** (as required), with a link opening in a new tab.
- Improved error handling:
  - Empty search term shows a message on the form
  - If there is no term in the session, `/results` redirects back to `/search`
  - Disambiguation: we select the next-most-likely title
  - Missing pages: we fall back to a random valid page
- Enabled debug mode in `app.run(debug=True)` for easier development.

## Quick start

```bash
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install flask wikipedia
.\.venv\Scripts\python flaskdemo.py
# Visit http://127.0.0.1:5000/
```

## Files

- `flaskdemo.py` – main app
- `templates/layout.html`, `templates/home.html`, `templates/search.html`, `templates/results.html`, `templates/about.html`
- `static/styles.css`
