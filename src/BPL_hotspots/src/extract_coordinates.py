# Col 5 and 6 contain lat and long
# Output csv file to add a layer to arcgis map

import pandas as pd

lat_long_df = pd.read_csv("../output/bpl_wifi_05052021.csv", usecols=[5,6], names=['lat', 'long'], header=None)
# print(lat_long_df.head(5))
lat_long_df.to_csv('../output/bpl_wifi_coordinates_05052021_dataset.csv')