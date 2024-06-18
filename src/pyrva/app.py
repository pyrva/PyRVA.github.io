"""
Main flask application for the PyRVA website.

Ensure endpoints have trailing slashes to avoid errors when building the site.
"""

from datetime import datetime, timedelta

from flask import Flask, render_template

from .config import Config
from .data import get_data

app = Flask(__name__)


@app.context_processor
def inject_context() -> dict:
    """Context to be added to all templates."""
    return {
        "socials": Config.SOCIALS,
    }


@app.route("/")
def index() -> str:
    return render_template(
        "pages/index.html",
        events=get_data("events.json"),
        organizers=get_data("organizers.json"),
    )


@app.route("/about/")
def about() -> str:
    return render_template("pages/about.html")


@app.route("/meeting/")
def meeting() -> str:
    events = get_data("events.json")
    icebreakers = next(
        v
        for k, v in get_data("icebreakers.json").items()
        if datetime.strptime(k, "%Y-%m-%d") >= datetime.now() - timedelta(days=1)
    )

    return render_template(
        "pages/meeting.html",
        event=events[0],
        upcoming=events[1 : Config.UPCOMING_EVENTS + 1],
        sponsors=get_data("sponsors.json"),
        icebreakers=icebreakers,
    )


@app.route("/sponsors/")
def sponsors() -> str:
    return render_template(
        "pages/sponsors.html",
        sponsors=get_data("sponsors.json"),
        perks=get_data("sponsor_perks.json"),
        donate_link=Config.DONATE_LINK,
    )


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
