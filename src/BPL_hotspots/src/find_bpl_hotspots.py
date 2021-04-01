#!/usr/bin/python3
# Tested with Python 3.8.6
#------------------------------------------------------------------------------
#    find_bpl_hotspots.py
#------------------------------------------------------------------------------
# Author: Isabel J. Rodriguez
# 2021.01.23
#------------------------------------------------------------------------------
"""
Scrape data from the Bklyn Reach website and generate a csv file containing
relevant information from participating libraries in the BPL system. 

INPUTS
------
    NONE
        Uses the existing Bklyn Reach url: https://www.bklynlibrary.org/reach/

OUTPUTS
-------
    Output file:
        "bpl_wifi.csv"

    Data included:
        LIBRARY
        ADDRESS
        WI-FI PROGRAM
        AVAILABILITY
        LIBRARY WEBSITE
"""

#   Standard Python library imports
import csv
import sys

#   Companion scripts
from write_to_csv import write_to_csv
from exception_handler import exception_handler
from soupify_webpage import parse_html

#    Geolocator
from geopy.geocoders import Nominatim

def pull_wifi_data():

    # fetch html
    bpl_reach_url= 'https://www.bklynlibrary.org/reach/'
    webpage_soup = parse_html(bpl_reach_url)

    #  parse html content
    containers = webpage_soup.findAll("div", {"class" : "panel-body"})

    # containers[0] has all active participating libraries
    # containers[1] libraries listed as having a program 'coming soon'
    list_active = containers[0].ul.findAll("li")

    return list_active

def geolocate_coordinates(street_address=None):

    if street_address is not None:
        try:
            geolocator = Nominatim(user_agent="bpl_wifi")
            location = geolocator.geocode(street_address)
            print(location.address)
            latitude = str(location.latitude)
            longitude = str(location.longitude)
        except AttributeError:
            latitude = 'NaN'
            longitude = 'NaN'

    return latitude, longitude


def pull_address_data(url=None):
    """
    Libraries with active extended wi-fi programs have their websites listed.
    Access websites and pull street address and zip code. If an street address 
    intersection is given e.g.,

                  "16 Brighton First Rd. at Brighton Beach Ave."
    
    remove the intersection and return e.g., "16 Brighton First Rd."
    """
    if url is not None:
        webpage_soup = parse_html(url)
        street_container = webpage_soup.findAll("div", {"class":"street-block"})
        zip_container = webpage_soup.findAll("div", {"class":"addressfield-container-inline locality-block country-US"})
 
        street_address = street_container[0].div.text
        zip_code = zip_container[0].findAll("span", {"class":"postal-code"})[0].text
        
        #  clean address data 
        split_address = street_address.split()
        
        stopwords = ['at', '(near', '(Near']
        #  remove street intersection
        for stopword in stopwords:
            if stopword in split_address:
                street_address = split_address[:split_address.index(stopword)]
                street_address = ' '.join(street_address)
            else:
                pass
        
        if 'First' in street_address:
            street_address = street_address.replace("First", "1st")
        else:
            pass
        
        #  grab geolocation data
        latitude, longitude = geolocate_coordinates(street_address=street_address + ', Brooklyn')

    return street_address, zip_code, latitude, longitude

def store_data(list_active):
    """
    Create a dictionary to store information for Brooklyn Public 
    Libraries participating in the Bklyn Reach extended wi-fi program.
    """

    # Bklyn Reach service details  
    wifi_range = '300 feet'
    wifi_availability = '24/7'
    wifi_program = 'Bklyn Reach'
    city_state = ' Brooklyn, New York '
    # create a storage container for BPL data
    bp_libraries = {list_active[i].text: {'ADDRESS' : '',
                                          'LATITUDE' : '',
                                          'LONGITUDE' : '',
                                          'WI-FI PROGRAM': wifi_program,
                                          'AVAILABILITY': wifi_availability,
                                          'WI-FI RANGE' : wifi_range,
                                          'LIBRARY WEBSITE': '' }
                    for i in range(len(list_active))} 

    print("Compiling data...")
    for i in range (len(list_active)):
        nested_dict = bp_libraries[list_active[i].text]

        street_address, zip_code, latitude, longitude = pull_address_data(list_active[i].a["href"])

        nested_dict['ADDRESS'] = street_address + ',' + city_state + ',' + zip_code
        nested_dict['LATITUDE'] = latitude
        nested_dict['LONGITUDE'] = longitude
        nested_dict['LIBRARY WEBSITE'] = list_active[i].a["href"]

    return bp_libraries


def write_data_to_csv(bp_libraries,
                      output_filename=None,
                      output_folder=None):
    """
    Pull data from storage dictionary into a list of lists, 
    and write to csv.

    ARGUMENTS
    ---------
        bp_libraries : dict
        output_filename : str
            e.g., "bpl_wifi.csv"
        output_folder : str

    RETURNS
    -------
        None
    """

    output = []

    #  Order and sort data into output container
    for key, val in bp_libraries.items():
        output.append([key,
                       val['ADDRESS'],
                       val['LATITUDE'],
                       val['LONGITUDE'],
                       val['WI-FI PROGRAM'],
                       val['AVAILABILITY'],
                       val['LIBRARY WEBSITE']])

    output.sort(key=lambda header: header[0])

    print("Compilation complete. Writing out to a csv file.")
    write_to_csv(output_filename=output_filename,
                 output_folder=output_folder,
                 output=output)

@exception_handler
def main(output_filename=None):
    """
    Contains a pipeline that accepts an input csv file, and
    outputs processed and sorted data into an output csv file.

    ARGUMENTS
    ---------
        output_filename : str
            e.g., "wifi.csv"
    RETURNS
    -------
        None
    """    

    list_active = pull_wifi_data()
    bp_libraries = store_data(list_active)
    write_data_to_csv(bp_libraries, 
                      output_filename=output_filename,
                      output_folder=output_folder)

if __name__ == "__main__":
    output_folder = "../output/"

    main(output_filename=sys.argv[1])
