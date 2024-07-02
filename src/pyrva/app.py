"""
Main flask application for the PyRVA website.

Ensure endpoints have trailing slashes to avoid errors when building the site.
"""

from datetime import datetime, timedelta
from typing import TypeVar

from flask import Flask, render_template, url_for

from .config import Config
from .data import get_data

app = Flask(__name__)

T = TypeVar("T")


def get_next(data: dict[str, list[T]]) -> list[T]:
    return next(
        v
        for k, v in data.items()
        if datetime.strptime(k, "%Y-%m-%d") >= datetime.now() - timedelta(days=1)
    )


@app.template_filter()
def format_datetime(value: str, from_fmt: str, to_fmt: str) -> str:
    """Convert a datetime string from one format to another."""
    return datetime.strptime(value, from_fmt).strftime(to_fmt)


@app.context_processor
def inject_context() -> dict:
    """Context to be added to all templates."""
    return {
        "socials": Config.SOCIALS,
        "config": Config,
    }


@app.route("/")
def index() -> str:
    return render_template(
        "pages/index.html",
        events=get_data("events.json"),
        organizers=get_data("organizers.json"),
        sponsors=get_data("sponsors.json"),
        perks=get_data("sponsor_perks.json"),
        donate_link=Config.DONATE_LINK,
    )


@app.route("/meeting/")
def meeting() -> str:
    events = get_data("events.json")
    icebreakers = get_next(get_data("icebreakers.json"))
    food_sponsors = get_next(get_data("food_sponsors.json"))

    return render_template(
        "pages/meeting.html",
        event=events[0],
        upcoming=events[1 : Config.UPCOMING_EVENTS + 1],
        sponsors=get_data("sponsors.json"),
        icebreakers=icebreakers,
        food_sponsors=food_sponsors,
    )


@app.route("/sponsor/")
def sponsor() -> str:
    return render_template(
        "pages/redirect.html",
        name="Sponsor",
        url=url_for("index") + "#sponsor",
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
