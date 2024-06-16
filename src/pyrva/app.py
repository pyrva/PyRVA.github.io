from flask import Flask, render_template
from werkzeug.wrappers import Response

app = Flask(__name__)


@app.route("/")
def hello_world() -> Response:
    return render_template("pages/index.html")


if __name__ == "__main__":
    app.run()
