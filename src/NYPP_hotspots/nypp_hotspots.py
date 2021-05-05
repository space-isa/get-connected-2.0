#   Standard Python library imports
import csv
import sys
import time

#   Companion scripts
from write_to_csv import write_to_csv
from exception_handler import exception_handler
from soupify_webpage import parse_html

from bs4 import BeautifulSoup as soup
import urllib.request
from functools import reduce 


def pull_wifi_data():
    # fetch html
    page_soup = parse_html(nyc_parks_url + wifi_endpoint)

    containers = page_soup.findAll("div", {"class":"tab-content"})
    tables = [td.get_text(strip=True) for td in containers[0].div.table.find_all('td')]

    web_containers = containers[0].div.table
    park_website_endpoints = []
    for a in containers[0].div.table.find_all('a', href=True):
        if a['href'] != "#wifi-type-defs":
            park_website_endpoints.append(a['href'])

    return tables, park_website_endpoints

def reshape(bulk_list, shape):
    return list(reduce(lambda x, y: map(list, zip(*y*(x,))), (iter(bulk_list), *shape[1:]))) 


def compile_nypp_data():
    tables, park_website_endpoints = pull_wifi_data()

    tables_shape = [-1,4]
    wifi_endpoints_shape = [-1,1]

    tables_sorted = reshape(tables, tables_shape)
    wifi_endpoints_sorted = reshape(park_website_endpoints, wifi_endpoints_shape)

    for i in range(len(wifi_endpoints_sorted)):
        wifi_endpoints_sorted[i][0] = nyc_parks_url + wifi_endpoints_sorted[i][0]

    compiled_table = []
    for i in range(len(tables_sorted)):
        new_row = tables_sorted[i] + wifi_endpoints_sorted[i]
        compiled_table.append(new_row)

    return compiled_table

@exception_handler
def main():
    compiled_table = compile_nypp_data()
    print(compiled_table)
    write_to_csv(output_filename=output_filename,
                 output_folder=output_folder,
                 output=compiled_table)

if __name__ == "__main__":
    nyc_parks_url = "https://www.nycgovparks.org"
    wifi_endpoint = "/facilities/wifi"
    date = time.strftime("%m%d%Y")
    output_folder = "./output/"
    output_filename = "nypp_wifi_{}.csv".format(date)
    main()


# print(full_table)

# Park downhill: 'tables' is a single array with all values. 
# It has 4 columns: park, location, wi-fi type, wi-fi povider,
# e.g., ['Alfred E. Smith Playground', 'Playground area', 'Limited Free', 'Spectrum',...]
# need to reshape!
# note that parks have duplicate names but different locations. keep them all!
# ensure order is preserved when reshaping so that websites can be added. 
# we also need the main webpage, these are just endpoints
# then we need to go to those endpoints and figure out if theres a bathroom!