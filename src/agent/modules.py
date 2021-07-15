"""Agent Modules."""

# Standard Python Libraries
import logging
from typing import List

# Third-Party Libraries
from bs4 import BeautifulSoup
import requests


def visit_webpage(url: str) -> List[str]:
    """Visit a webpage returning all urls in a list."""
    logging.info("Visiting a webpage.")
    logging.debug(f"visiting {url}")
    response: requests.models.Response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    links: List[str] = []
    for link in soup.find_all("a"):
        if link.get("href").startswith("http"):
            logging.debug(f"saving link: {link.get('href')}")
            links.append(link.get("href"))
        else:
            logging.debug(f"skipping link: {link.get('href')}")

    logging.info(f"{len(links)} links found.")
    return links
