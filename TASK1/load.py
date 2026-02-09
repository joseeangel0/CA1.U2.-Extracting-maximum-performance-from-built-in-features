import collections
import csv
import datetime
import sys
import requests

# URL Template from the text
TEMPLATE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access/{year}/{station}.csv"
TEMPLATE_FILE = "station_{station}_{year}.csv"

def download_data(station, year):
    my_url = TEMPLATE_URL.format(station=station, year=year)
    req = requests.get(my_url)
    if req.status_code != 200:
        return # not found
    
    with open(TEMPLATE_FILE.format(station=station, year=year), "wt") as w:
        w.write(req.text)

def download_all_data(stations, start_year, end_year):
    for station in stations:
        for year in range(start_year, end_year + 1):
            download_data(station, year)

def get_file_temperatures(file_name):
    with open(file_name, "rt") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            try:
                station = row[header.index("STATION")]
                tmp = row[header.index("TMP")]
                temperature, status = tmp.split(",")
                if status != "1":
                    continue
                temperature = int(temperature) / 10
                yield temperature
            except (ValueError, IndexError):
                continue

def get_all_temperatures(stations, start_year, end_year):
    temperatures = collections.defaultdict(list)
    for station in stations:
        for year in range(start_year, end_year + 1):
            try:
                for temperature in get_file_temperatures(TEMPLATE_FILE.format(station=station, year=year)):
                    temperatures[station].append(temperature)
            except FileNotFoundError:
                pass
    return temperatures

def get_min_temperatures(all_temperatures):
    return {station: min(temperatures) for station, temperatures in all_temperatures.items() if temperatures}

if __name__ == "__main__":
    # Parsing arguments as described in the text
    stations = sys.argv[1].split(",")
    years = [int(year) for year in sys.argv[2].split("-")]
    start_year = years[0]
    end_year = years[1]

    download_all_data(stations, start_year, end_year)
    all_temperatures = get_all_temperatures(stations, start_year, end_year)
    min_temperatures = get_min_temperatures(all_temperatures)
    print(min_temperatures)