import requests
from math import radians, cos, sin, asin, sqrt

def find_furthest_country(user_country):
    country_url = f"https://restcountries.com/v3.1/name/{user_country}?fullText=true"
    response = requests.get(country_url).json()
    user_lat = response[0]["latlng"][0]
    user_long = response[0]["latlng"][1]
    
    max_distance = 0
    furthest_country = ""
    all_countries_url = "https://restcountries.com/v3.1/all"

    for country in requests.get(all_countries_url).json():
        lat = country["latlng"][0]
        long = country["latlng"][1]

        #turn lat and lon into radians
        lon1 = radians(user_long)
        lon2 = radians(long)
        lat1 = radians(user_lat)
        lat2 = radians(lat)
            
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers
        r = 6378.1

        distance = c * r

        if distance > max_distance:
            max_distance = distance
            furthest_country = country["name"]["common"]

    return furthest_country

user_country = input("Enter a country name: ")
print(f"The country the furthest away from {user_country} is: {find_furthest_country(user_country)}")
