from bs4 import BeautifulSoup as BeautifulSoup
import urllib.request

nyc_parks_url = "https://www.nycgovparks.org"
wifi_endpoint = "/facilities/wifi"

page=urllib.request.Request(nyc_parks_url + wifi_endpoint, 
                            headers={'User-Agent': 'Mozila/5.0'})
page_html = urllib.request.urlopen(page).read()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"tab-content"})
tables = [td.get_text(strip=True) for td in containers[0].div.table.find_all('td')]

web_containers = containers[0].div.table
park_website_endpoints = []
for a in containers[0].div.table.find_all('a', href=True):
    if a['href'] != "#wifi-type-defs":
        park_website_endpoints.append(a['href'])


# Park downhill: 'tables' is a single array with all values. 
# It has 4 columns: park, location, wi-fi type, wi-fi povider,
# e.g., ['Alfred E. Smith Playground', 'Playground area', 'Limited Free', 'Spectrum',...]
# need to reshape!
# note that parks have duplicate names but different locations. keep them all!
# ensure order is preserved when reshaping so that websites can be added. 
# we also need the main webpage, these are just endpoints
# then we need to go to those endpoints and figure out if theres a bathroom!