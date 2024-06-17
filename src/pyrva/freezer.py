"""
script to freeze the pyrva website

This leverages `Frozen-Flask` to freeze the website into static files.
https://frozen-flask.readthedocs.io/en/latest/
"""

from app import app
from flask_frozen import Freezer

app.config["FREEZER_DESTINATION"] = "../../build"
freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()