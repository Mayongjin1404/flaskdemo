from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
# NOTE: For coursework convenience only. Do NOT hard-code secrets in real projects.
app.secret_key = "dev-only-change-me"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """Render the search form or save the term then redirect to results."""
    if request.method == "POST":
        term = request.form.get("search", "").strip()
        if not term:
            # Re-render the form with a gentle message
            return render_template("search.html", message="Please enter a search term.")
        session["search_term"] = term
        return redirect(url_for("results"))
    # GET
    return render_template("search.html")


@app.route("/results")
def results():
    """Perform the search and show results. Redirect to form if no term stored."""
    term = session.get("search_term")
    if not term:
        return redirect(url_for("search"))
    page = get_page(term)
    return render_template("results.html", page=page, term=term)


def get_page(search_term: str):
    """Return a wikipedia.page object for the given term.
    - If the page doesn't exist, try a random page.
    - If term is a disambiguation, pick the next most likely result.
    """
    try:
        return wikipedia.page(search_term, auto_suggest=True)
    except wikipedia.exceptions.PageError:
        # No such page; try a random real page title
        random_title = wikipedia.random()
        return wikipedia.page(random_title)
    except wikipedia.exceptions.DisambiguationError as e:
        # Choose the first option different from the original term (case-insensitive)
        for title in e.options:
            if title.lower() != search_term.lower():
                return get_page(title)
        # Fallback: just take the first option
        return get_page(e.options[0])


if __name__ == "__main__":
    app.run(debug=True)
