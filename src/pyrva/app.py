from flask import Flask, redirect, render_template
from werkzeug.wrappers import Response

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("pages/index.html")


@app.route("/faq")
def faq() -> str:
    return render_template("pages/faq.html")


@app.route("/meeting")
def meeting() -> str:
    return render_template("pages/meeting.html")


@app.route("/sponsors")
def sponsors() -> str:
    return render_template("pages/sponsors.html")


@app.route("/meetup")
def meetup() -> Response:
    return redirect("https://www.meetup.com/PyRVAUserGroup/")


@app.route("/discord")
def discord() -> Response:
    return redirect("https://discord.com/invite/fSGW7Jra4T")


@app.route("/youtube")
def youtube() -> Response:
    return redirect("https://youtube.com/@pyrva")


if __name__ == "__main__":
    app.run()
