import json

from .config import Config


def get_data(filename: str) -> dict:
    """Load JSON data from a file."""
    return json.loads((Config.DATA_DIR / filename).read_text())
