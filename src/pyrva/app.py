"""
Main flask application for the PyRVA website.

Ensure endpoints have trailing slashes to avoid errors when building the site.
"""

import json

from config import Config
from flask import Flask, render_template

app = Flask(__name__)


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
        url="https://www.meetup.com/PyRVAUserGroup/",
    )


@app.route("/discord/")
def discord() -> str:
    return render_template(
        "pages/redirect.html",
        name="Discord",
        url="https://discord.com/invite/fSGW7Jra4T",
    )


@app.route("/youtube/")
def youtube() -> str:
    return render_template(
        "pages/redirect.html",
        name="YouTube",
        url="https://youtube.com/@pyrva",
    )


if __name__ == "__main__":
    app.run()
