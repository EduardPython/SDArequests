# https://data.world/petrsevcik/testproject/workspace/file?agentid=arthur&datasetid=banks&filename=top100banks2017-12-31.xlsx
import csv
from itertools import islice
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from os import path
# http://planecrashinfo.com/database.htm

#OK
def create_link_queue(from_year=1921, to_year=2021):
    """create list of url´s in range of years"""
    url_queue = []
    BASE_URL = "http://planecrashinfo.com/"
    for year in range(from_year, to_year+1):           #change from "to_year" to "to_year + 1" for reach end of the range
        url = f"{BASE_URL}{year}/{year}.htm"
        url_queue.append(url)
    return url_queue


def scrape_data_from_page(page_url):
    """scraping data from given url"""
    crash_data = []
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, "html.parser")
    table_rows = soup.find_all("tr")
    for row in islice(table_rows, 1, None):  # skip table headers
        table_fields = row.find_all("td")
        date = table_fields[0].text
        loc_operator = table_fields[1]
        location = loc_operator.next.next
        operator = loc_operator.next.next.next.next# changed method to separate "location" and "operator"
        aircraft_type_and_registration = table_fields[2].text
        fatalities = table_fields[3].text
        scraped_data = (date, location, operator, aircraft_type_and_registration, fatalities)
        crash_data.append(scraped_data)
    return crash_data


def format_date(date):
    d = datetime.strptime(date, '%d %b %Y')
    return d.strftime('%d-%m-%Y')

def format_location_and_state(loc):
    try:
        location, state = loc.split(",")
    except ValueError:
        location = "neznama"
        state = "neznama"
    return location, state


def format_aircraft_brand(aircraft_type_and_registration):
    a = aircraft_type_and_registration.split(" ")
    aircraft_brand = a[0]
    return aircraft_brand


def format_number_of_deaths(fatalities):
    f = fatalities.split("/")
    _survivors, _g_casualties = f[1].split("(")
    _ground_casualties = _g_casualties.replace(")","")
    try:
        number_of_deaths = int(f[0])
        survivors = int(_survivors) - number_of_deaths
        ground_casualties = int(_ground_casualties)
        return number_of_deaths, survivors, ground_casualties
    except ValueError:
        number_of_deaths = 0
        survivors = 0
        ground_casualties = 0
        return number_of_deaths, survivors, ground_casualties



def create_headers_in_csv_file():
    if not path.isfile("crash_data_honza.csv"):
        with open("crash_data_honza.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "location", "state", "airline", "aircraft_brand", "no_deaths", "no_survivors", "no_ground_casualties"])
        return "File Created!"
    return "File exists"


def write_data_to_csv(crash_data):
    with open("crash_data_honza.csv", "a") as file:
        writer = csv.writer(file)
        for _ in crash_data:
            # date, location, operator, aircraft_type_and_registration, fatalities
            d, loc, opera, type_reg, deaths = _
            date = format_date(d)
            location, state = format_location_and_state(loc)
            operator = opera.strip()# added new function "format_location"         # added new function "format_operator"
            brand = format_aircraft_brand(type_reg)
            no_deaths, no_suvivors, no_ground_casualties = format_number_of_deaths(deaths)
            writer.writerow([date, location, state, operator, brand, no_deaths, no_suvivors, no_ground_casualties])


links_2010_2021 = create_link_queue()
create_headers_in_csv_file()
for year_link in links_2010_2021:
    crash_data = scrape_data_from_page(year_link)
    write_data_to_csv(crash_data)