import datetime
import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

DATE_FORMAT: str = "%b %d, %Y"
TIME_FORMAT: str = "%I:%M %p"
GROUP_NAME = "pyrvausergroup"


class Event:
    def __init__(self, soup: Tag) -> None:
        self.soup = soup

    def __str__(self) -> str:
        return self.soup.prettify()

    @property
    def url(self) -> str:
        element = self.soup.select_one("a")
        if element is None:
            raise ValueError("No URL found")
        return str(element["href"])

    @property
    def title(self) -> str:
        element = self.soup.select_one("[class*=utils_cardTitle]")
        if element is None:
            raise ValueError("No title found")
        return element.text

    @property
    def location(self) -> str:
        element = self.soup.select_one("[class*=utils_cardTitle] + div")
        if element is None:
            raise ValueError("No location found")
        return element.text

    @property
    def image(self) -> str:
        element = self.soup.select_one("img")
        if element is None:
            raise ValueError("No image found")
        return str(element["src"])

    @property
    def description(self) -> str:
        element = self.soup.select_one("[class*=utils_cardDescription]")
        if element is None:
            raise ValueError("No description found")
        return element.prettify()

    @property
    def datetime(self) -> datetime.datetime:
        element = self.soup.select_one("time")
        if element is None:
            raise ValueError("No datetime found")
        # Remove the timezone to prevent parsing issues
        time_str = " ".join(element.text.split()[:-1])
        return datetime.datetime.strptime(time_str, "%a, %b %d, %Y, %I:%M %p")

    @property
    def rsvps(self) -> int:
        spans = self.soup.select("span")
        attendees = next(s.text for s in spans if s.text.endswith("attendees"))
        return int(attendees.split()[0])

    @property
    def info(self) -> dict[str, str | int | dict]:
        dt = self.datetime

        return {
            "url": self.url,
            "title": self.title,
            "location": self.location,
            "rsvps": self.rsvps,
            "description": self.description,
            "image": self.image,
            "date": {
                "str": dt.strftime(DATE_FORMAT),
                "dow": {
                    "full": dt.strftime("%A"),
                    "abbr": dt.strftime("%a"),
                    "num": int(dt.strftime("%w")),
                },
                "month": {
                    "full": dt.strftime("%B"),
                    "abbr": dt.strftime("%b"),
                    "num": int(dt.strftime("%m")),
                },
                "day": int(dt.strftime("%d")),
                "year": int(dt.strftime("%Y")),
            },
            "time": {
                "str": dt.strftime(TIME_FORMAT),
                "hour": dt.strftime("%H"),
                "minute": dt.strftime("%M"),
            },
        }


if __name__ == "__main__":
    page = requests.get(f"https://www.meetup.com/{GROUP_NAME}/events/", timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")

    events = [Event(e) for e in soup.select("[id^=e-]")]

    project_root = Path(__file__).resolve().parents[1]
    json_file = project_root / "data" / "events.json"
    json_file.write_text(json.dumps([e.info for e in events], indent=4))
