import json
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup

GROUP_NAME = "pyrvausergroup"


class Event:
    def __init__(self, data: dict, event_key: str) -> None:
        self.data = data
        self.event = data[event_key]

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)

    @property
    def image(self) -> str:
        img_ref = self.event["featuredEventPhoto"]["__ref"]
        return self.data[img_ref]["highResUrl"]

    @property
    def info(self) -> dict[str, str | int | dict]:
        return {
            "url": self.event["eventUrl"],
            "title": self.event["title"],
            "rsvps": self.event["going"]["totalCount"],
            "description": self.event["description"],
            "image": self.image,
            "datetime": self.event["dateTime"][:-6],
        }


def extract_meetup_data(soup: BeautifulSoup) -> dict[str, Any]:
    data = json.loads(soup.select_one("script#__NEXT_DATA__").string)
    data = data["props"]["pageProps"]["__APOLLO_STATE__"]
    return data


def extract_event_keys(data: dict) -> list[str]:
    return [k for k in data.keys() if k.startswith("Event:")]


if __name__ == "__main__":
    page = requests.get(f"https://www.meetup.com/{GROUP_NAME}/events/", timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    data = extract_meetup_data(soup)
    event_keys = extract_event_keys(data)

    events = [Event(data, e) for e in event_keys]

    project_root = Path(__file__).resolve().parents[1]
    html_file = project_root / "data" / "events.html"
    query_file = project_root / "data" / "query.json"
    json_file = project_root / "data" / "events.json"

    html_file.write_text(soup.prettify())
    query_file.write_text(json.dumps(data, indent=4))
    json_file.write_text(json.dumps([e.info for e in events], indent=4))
