from pathlib import Path


class Config:
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = PROJECT_ROOT / "data"

    SOCIALS = {
        "meetup": "https://www.meetup.com/PyRVAUserGroup/",
        "discord": "https://discord.com/invite/fSGW7Jra4T",
        "youtube": "https://www.youtube.com/@pyrva",
        "github": "https://github.com/pyrva",
    }

    UPCOMING_EVENTS = 3
