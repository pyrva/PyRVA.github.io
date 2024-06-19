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

    DONATE_LINK = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=35"

    UPCOMING_EVENTS = 3

    MEETUP_DT_FORMAT = "%a, %b %d, %Y, %I:%M %p"
    EVENT_DT_FORMAT = "%a, %B %d, %-I:%M %p"
