# get-connected-2.0

GetConnected 2.0 is an updated platform designed to create both a resouce hub for the community members of Manhattan's Lower East Side, as well as to curate a list of free, accessible wi-fi hubs available thorugh the New York Public Library systems as well as New York Public Parks.

---
## Table of Contents 
1. [Motivation](#motivation) 
2. [Solution Approach](#solution-approach)
3. [Requirements](#requirements)
4. [How to use?](#how-to-use) 
5. [Features](#features) 
6. [Tests](#tests)
7. [Future Development](#future-development)
8. [References](#references)
9. [Author](#author)

---

## Motivation 
As a data engineering project, this code primarily showcases how to transform raw input data (leaving the original source unchanged) and export it to a given destination. In a scaled-up version of this pipeline, data would be downloaded from a database and the transformed data directly uploaded to a database or a data warehouse. This would be a complete Extract-Transform-Load (ETL) process.

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

## Solution Approach 
 

---

## Requirements
This code was developed and tested using Python 3.8.6.
Install: BeautifulSoup and Geopy before use.

---

## How to use? 

--- 

## Features 

- An exception handling decorator: 
   ```python
   @exception_handler
   def main(output_filename=None):
   ...
   ```
- Seperate scripts for web-scraping: e.g., `soupify_webpage.py`, and writing to output csv file: `write_to_csv.py`. 

### Other features 


## Tests 

### Unit testing 


To run tests:

---

## Future Development

- Adding a `failed` subdirectory where failed csv files for failed data extractions can be rerouted.  
- Improve output file naming system: 
   - Implement code for generating failed report filenames
- Expand functionality of `exception_handler.py`.

## References

---

## Author 
Isabel J. Rodriguez 
