import csv
import json
import logging
import os
import requests
import time

logging.basicConfig(level="INFO", format="%(asctime)s - %(levelname)s - %(message)s")

NOMINATIM_ENDPOINT="https://nominatim.openstreetmap.org/search"
DELAY=1
ISTAT_FOLDER="istat"
JSON_OUTPUT="comuni.json"

def build_query(city: str) -> str:
    """
    Return the Nominatim query
    """
    return f"{NOMINATIM_ENDPOINT}?city={city}&country=Italy&format=json"

def main() -> None:
    start_time=time.time()
    logging.info("Geocoding job started")

    istat_file_name=os.listdir(ISTAT_FOLDER)[0]
    istat_file_path=os.path.join(ISTAT_FOLDER, istat_file_name)
    logging.info(f"Input file: {istat_file_path}")

    city_names=[]

    with open(istat_file_path, encoding="ISO 8859-1") as csvfile:
        for row in csv.DictReader(csvfile, delimiter=";"):
            city_names.append(row["Denominazione in italiano"])

    city_names=[n.strip() for n in city_names] #Just in case
    city_names.sort()

    logging.info(f"Extracted {len(city_names)} city names")

    geocoded_cities=[]
    done=0

    for city in city_names:

        try:
            r=requests.get(build_query(city), headers={
                "User-Agent": "Little geocoding job" #Be honest with Nominatim
            })
            response=r.json()
        except Exception as e:
            logging.error(f"Error during the request for {city}: {e}")
            continue

        #Check if response is an empty list. This means Nominatim can't find the city.
        if not response:
            logging.error(f"Empty response for {city}")
            continue

        latitude=response[0]["lat"]
        longitude=response[0]["lon"]

        logging.info(f"City: {city} Lat: {latitude} Lon: {longitude}")    
        geocoded_cities.append(
            {
                "name": city,
                "lat": latitude,
                "lon": longitude
            }
        )

        done+=1
        time.sleep(DELAY) #Not too many requests

    logging.info(f"Geocoded {done}/{len(city_names)} cities")

    with open(JSON_OUTPUT, "w") as jsonfile:
        jsonfile.write(json.dumps(geocoded_cities, indent=4, ensure_ascii=False))

    logging.info(f"Output written on {JSON_OUTPUT}")

    elapsed_time=time.time()-start_time
    logging.info(f"Job completed in {elapsed_time} seconds")

if __name__ == "__main__":
    main()