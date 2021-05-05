#   Web scraping imports
from bs4 import BeautifulSoup as soup
import urllib.request


def parse_html(url=None):
    if url is not None:

        # fetch url
        webpage = urllib.request.Request(url, 
                                        headers={'User-Agent': 'Mozila/5.0'})
        webpage_html = urllib.request.urlopen(webpage).read()
        webpage_soup = soup(webpage_html, "html.parser")

    return webpage_soup