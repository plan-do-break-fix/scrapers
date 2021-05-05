#!/bin/python3
from typing import List

from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}


def collect_tags(page: int) -> List:
    """Return all tags from tag listing page number <page>."""
    if not 0 < pages < 1799:  # 1798 pages as of 2021.05.05
        raise RuntimeError
        url = "https://stackoverflow.com/tags?page={page}&tab=popular"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            raise RuntimeError
        soup = BeautifulSoup(resp.content)
        return [card.find("div", {"class": "grid"}).find("a").text
                for card in soup.find_all("div", {"class": "s-card"})]
        