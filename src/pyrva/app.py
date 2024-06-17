"""
Main flask application for the PyRVA website.

Ensure endpoints have trailing slashes to avoid errors when building the site.
"""

import json

from config import Config
from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_context() -> dict:
    """Context to be added to all templates."""
    return {
        "socials": Config.SOCIALS,
    }


@app.route("/")
def index() -> str:
    events = json.loads((Config.DATA_DIR / "events.json").read_text())
    organizers = json.loads((Config.DATA_DIR / "organizers.json").read_text())

    return render_template(
        "pages/index.html",
        events=events,
        organizers=organizers,
    )


@app.route("/faq/")
def faq() -> str:
    return render_template("pages/faq.html")


@app.route("/meeting/")
def meeting() -> str:
    return render_template("pages/meeting.html")


@app.route("/sponsors/")
def sponsors() -> str:
    return render_template("pages/sponsors.html")


@app.route("/meetup/")
def meetup() -> str:
    return render_template(
        "pages/redirect.html",
        name="Meetup",
        url=Config.SOCIALS["meetup"],
    )


@app.route("/discord/")
def discord() -> str:
    return render_template(
        "pages/redirect.html",
        name="Discord",
        url=Config.SOCIALS["discord"],
    )


@app.route("/youtube/")
def youtube() -> str:
    return render_template(
        "pages/redirect.html",
        name="YouTube",
        url=Config.SOCIALS["youtube"],
    )


if __name__ == "__main__":
    app.run()
