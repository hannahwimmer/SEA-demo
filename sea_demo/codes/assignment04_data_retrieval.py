from sea_demo.config import settings
import openrouteservice
import json
import os 
import time

"""Data retrieval script for assignment 04.

important: this script needs an openroute service API key (free on: 
https://account.heigit.org/signup, if you're interested in trying it out yourself)

Run from the project root:
    python -m sea_demo.codes.assignment04_data_retrieval

"""

API_KEY = settings.API_KEY
client = openrouteservice.Client(key=API_KEY)


def get_geocode(city_name: str):
    """
    get the coordinates of a given city using openrouteservice.
    input:
        - city_name: target city name
    output:
        - target city's longitude and latitude
    """
    result = client.pelias_search(text=city_name + ", Austria")
    longitude, latitude = result["features"][0]["geometry"]["coordinates"]
    return (longitude, latitude)


def get_route(city_from: str, city_to: str, coordinates: dict):
    """
    fetch the route between two given cities using openrouteservice.
    inputs:
        - city_from: starting city
        - city_to: target city
        - coordinates: longitude and latitude of all fetched cities
    outputs:
        - distance_km: distance in km between both cities
        - duration_h: travel duration in h
        - file: path to the file where detailed information on the route is stored
    """
    filename = os.path.join(
        settings.routes_path,
        f"route_{city_from.replace(' ', '_')}_{city_to.replace(' ', '_')}.json"
    )
    filename_viceversa = os.path.join(
        settings.routes_path,
        f"route_{city_to.replace(' ', '_')}_{city_from.replace(' ', '_')}.json"
    )


    # check if route file already exists
    if os.path.exists(filename) or os.path.exists(filename_viceversa):
        print(f"Route file already exists: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            route = json.load(f)
        summary = route["features"][0]["properties"]["summary"]
        distance_km = summary["distance"] / 1000    # converts m to km
        duration_h = summary["duration"] / 3600     # converts s to h

    else:
        print(f"\nFetching route from {city_from} to {city_to} ...")
        try:
            route = client.directions(
                coordinates=[coordinates[city_from], coordinates[city_to]],
                profile='driving-car',
                format='geojson'  # return full geometry in GeoJSON
            )

            # save to json for later use
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(route, f, ensure_ascii=False, indent=2)

            # extract summary info
            summary = route["features"][0]["properties"]["summary"]
            distance_km = summary["distance"] / 1000    # convert m to km
            duration_h = summary["duration"] / 3600     # convert s to h

            print(f"{city_from} to {city_to}: {distance_km:.1f} km, {duration_h:.2f} h")
            # set up route details
                     
        except Exception as ex:
            print(f"Error fetching route: {ex}")
            return None
        
    route_details = {
            "distance_km": round(distance_km, 1),
            "duration_h": round(duration_h, 2),
            "file": filename
        }

    return route_details


def get_data(cities: list):
    coordinates = {city: get_geocode(city) for city in cities}
    print("Coordinates:")

    for city, (longitude, latitude) in coordinates.items():
        print(f"{city}: ({latitude:.4f}, {longitude:.4f})")
    
    routes = {}
    for i, city_from in enumerate(cities):
        for j, city_to in enumerate(cities):
            if i > j:  # avoid duplicates and self-routes
                routes[(city_from, city_to)] = get_route(city_from, city_to, coordinates)
                time.sleep(0.1)
                
    routes_jsonable = {
        f"{a}_to_{b}": data for (a, b), data in routes.items()
    }
    with open(settings.coordinates_path, "w", encoding="utf-8") as f:
        json.dump(coordinates, f, ensure_ascii=False, indent=2)
    with open(settings.summary_path, "w", encoding="utf-8") as f:
        json.dump(routes_jsonable, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    get_data(settings.cities)
