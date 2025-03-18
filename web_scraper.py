import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """Fetches and extracts clean text from a given URL."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL: {url}")

    soup = BeautifulSoup(response.text, "html.parser")
    return ' '.join([p.text for p in soup.find_all("p")])  # Extract paragraphs

