# get-connected-2.0

A project that curates information from the web related to free Wi-Fi and libray-based programs available to the community members of Manhattan's Lower East Side.  
![alt text](https://github.com/space-isa/get-connected-2.0/blob/main/docs/images/test-mysql-tableau-connect.png?raw=true)

---
## Table of Contents 
1. [Motivation](#motivation) 
2. [Requirements](#requirements)
3. [How to use?](#how-to-use) 
4. [Features](#features) 
5. [Tests](#tests)
6. [Future Development](#future-development)
7. [Author](#author)

---

## Motivation 
"Where can I get Wi-Fi to access the resources I need?" The original idea behind GetConnected–a project developed as part of the 2021 Valtech Hackathon–was to create a list of free, accessible Wi-Fi hubs available through the New York Public Library systems as well as New York Public Parks. You can learn more about the original project [here](https://docs.google.com/presentation/d/1WGnWsrTT71dQXkPMeNkUDvsj775XcF3k-BXl8jDQxYI/edit) and view the origial GitHub repository [here](https://github.com/space-isa/get-connected)

The code in this repository showcases how to acquire (via web-scraping) and transform raw input data (leaving the original source unchanged) and export it to a given destination. As an exercise, the NYPL information was loaded onto a MySQL database on Amazon RDS and vizualized using Tableau (see above figure).

### Project requirements

- Input
   - Output filename  (e.g., `bpl_wifi.csv`)

- Output file
   - Data should be output to a csv file (e.g., `bpl_wifi.csv`) in the following order:
        - Place name (e.g., Brighton Beach Library)
        - Address [Street, City, State, Zip Code]
        - Latitude
        - Longitude
        - Program name (e.g., Bklyn Reach)
        - Hours active (e.g., 24/7)
        - Website
   - Example csv output:    
      ```
      Brighton Beach Library,"16 Brighton 1st Rd., Brooklyn, New York ,11235",40.5761358,-73.96679206365367,Bklyn  Reach,24/7,https://www.bklynlibrary.org/locations/brighton-beach
      Brownsville Library,"61 Glenmore Ave., Brooklyn, New York ,11212",40.67150425,-73.90859604303299,Bklyn Reach,24/7,https://www.bklynlibrary.org/locations/brownsville
      Bushwick Library,"340 Bushwick Avenue, Brooklyn, New York ,11206",40.7045433,-73.93964337120033,Bklyn Reach,24/7,https://www.bklynlibrary.org/locations/bushwick
      ...
      ...
      ```
 

---

## Requirements
This code was developed and tested using Python 3.8.6.
Install before use: 
- BeautifulSoup 
- Geopy

---

## How to use? 

--- 
Feel free to fork this repo! 

In ```/BPL_hotspots/src/``` you'll find the script ```find_bpl_hotspots.py```. Running this script will access and scrape and store data from NY Public Libraries currently participating in the [Bklyn Reach](https://www.bklynlibrary.org/reach/) Wi-Fi program.

## Features 

- An exception handling decorator: 
   ```python
   @exception_handler
   def main(output_filename=None):
   ...
   ```

### Other features 
- Seperate scripts for web-scraping: e.g., `soupify_webpage.py`, and writing to output csv file: `write_to_csv.py`. 


## Future Development

- Adding a `failed` subdirectory where failed csv files for failed data extractions can be rerouted.  
- Improve output file naming system: 
   - Implement code for generating failed report filenames
- Expand functionality of `exception_handler.py`.
- Adding a timeit decorator
- Utilizing a job scheduler to regularly check and update program infomration

---

## Author 
Isabel J. Rodriguez 
