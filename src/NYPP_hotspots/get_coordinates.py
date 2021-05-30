#   Companion scripts
from soupify_webpage import parse_html
from write_to_csv import write_to_csv
from exception_handler import exception_handler

import pandas as pd
# read csv (use pandas)
# pull list of endpoints
# for each endpoint:


def pull_urls_from_csv(input_file):
    url_df = pd.read_csv(input_file, usecols=[4], names=["urls"], header=None)
    url_lst = url_df.urls.to_list()
    print(len(url_lst))
    return url_lst


def pull_location_data(coordinates_container):
    coordinates = coordinates_container[0].find_all('input')[1]["value"]
    coordinates = coordinates.replace('(', ', ')
    coordinates = coordinates.replace(')', '')
    coordinates_lst = coordinates.split(',')
    latitude.append(coordinates_lst[0])
    longitude.append(coordinates_lst[1])
    relative_location.append(coordinates_lst[2])


def pull_facilities_data(facilities_container):
    temp = 0
    for a in facilities_container[0].find_all('a'):
        if (a.find("img")["alt"] == "Bathrooms") and (temp == 0) :
            bathrooms_bool.append("Yes")
            temp += 1
        else:
            bathrooms_bool.append("Not listed on website")
            temp += 1

def create_new_csv(input_file, output_file):
    # a_dict = {"relative location": relative_location,
    #           "latitude": latitude,
    #           "longitude": longitude}
    # df_pulled_data = pd.DataFrame(a_dict)
    df = pd.read_csv(input_file, header=None)
    df.columns = ["Name", "Area", "Type",
                  "Provider", "Website"]
    # df_concat = pd.concat([df_old_data, df_pulled_data], ignore_index=True, axis=1)
    df["Relative location"] = relative_location
    df["Latitude"] = latitude
    df["Longitude"] = longitude
    # df.reset_index()
    # df["bathroom available"] = bathrooms_bool
    df.to_csv(output_file, index=False, header=False)


@exception_handler
def main():
    print("Pulling urls...")
    website_urls = pull_urls_from_csv(input_file)
    print("Parsing data...")
    for url in website_urls:
        page_soup = parse_html(url)
        facilities_container = page_soup.findAll("div", {"id": "park_facilities_side"})
        coordinates_container = page_soup.findAll("div", {"class": "actions"})
        try:
            pull_location_data(coordinates_container)
        except:
            latitude.append("NaN")
            longitude.append("NaN")
            relative_location.append("NaN")
            print("Couldn't find location data from {}".format(url))
        try:
            pull_facilities_data(facilities_container)
        except:
            bathrooms_bool.append("NaN")
            print("Couldn't find bathroom data from {}".format(url))
    print("Writing to csv...")
    create_new_csv(input_file, output_file)

if __name__ == "__main__":
    input_file = "../NYPP_hotspots/output/nypp_wifi_05052021.csv"
    output_file = "../NYPP_hotspots/output/nypp_wifi_complete_05302021.csv"
    relative_location = []
    latitude = []
    longitude = []
    bathrooms_bool = []
    main()