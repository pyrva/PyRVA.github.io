"""
script to freeze the pyrva website

This leverages `Frozen-Flask` to freeze the website into static files.
https://frozen-flask.readthedocs.io/en/latest/
"""

from flask_frozen import Freezer
from pyrva.app import app

app.config["FREEZER_DESTINATION"] = "../../docs"
app.config["FREEZER_DESTINATION_IGNORE"] = ["CNAME"]
freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
