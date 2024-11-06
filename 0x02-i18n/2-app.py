#!/usr/bin/env python3
"""Flask application with Babel for
internationalization and locale selection."""
from flask import Flask, render_template, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select the best language based on the user's preferences."""
    lang = request.accept_languages.best_match(['en', 'es', 'fr'])
    g.lang = lang
    return lang


@app.route('/')
def index():
    """Render the index page."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
