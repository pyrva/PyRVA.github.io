"""
Main flask application for the PyRVA website.

Ensure endpoints have trailing slashes to avoid errors when building the site.
"""

import json
from datetime import datetime, timedelta

from config import Config
from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_context() -> dict:
    """Context to be added to all templates."""
    return {
        "socials": Config.SOCIALS,
    }


EVENTS = json.loads((Config.DATA_DIR / "events.json").read_text())
ORGANIZERS = json.loads((Config.DATA_DIR / "organizers.json").read_text())
SPONSORS = json.loads((Config.DATA_DIR / "sponsors.json").read_text())


@app.route("/")
def index() -> str:
    return render_template(
        "pages/index.html",
        events=EVENTS,
        organizers=ORGANIZERS,
    )


@app.route("/about/")
def about() -> str:
    return render_template("pages/about.html")


@app.route("/meeting/")
def meeting() -> str:
    icebreakers = json.loads((Config.DATA_DIR / "icebreakers.json").read_text())
    icebreakers = next(
        v
        for k, v in icebreakers.items()
        if datetime.strptime(k, "%Y-%m-%d") >= datetime.now() - timedelta(days=1)
    )

    return render_template(
        "pages/meeting.html",
        event=EVENTS[0],
        upcoming=EVENTS[1 : Config.UPCOMING_EVENTS + 1],
        sponsors=SPONSORS,
        icebreakers=icebreakers,
    )


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


@app.route("/github/")
def github() -> str:
    return render_template(
        "pages/redirect.html",
        name="Github",
        url=Config.SOCIALS["github"],
    )


if __name__ == "__main__":
    app.run()
