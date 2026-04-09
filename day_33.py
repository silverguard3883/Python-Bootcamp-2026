"""Application Programming Interfaces"""

"""Set of commands, functions, protocols to interact with external systems"""

import requests
import datetime

"""ISS Location Data"""
iss_location_data = requests.get(url="http://api.open-notify.org/iss-now.json")
print(iss_location_data.json())

iss_location_data.raise_for_status()


"""Kanye Quote machine"""

quote = requests.get(url="https://api.kanye.rest/")
quote = quote.json()
print(quote["quote"])


"""Sunrise/Sunset API Call"""
lat = 40.7128
long = 74.0060

parameters = {
    "lat": lat,
    "lng": long,
    "formatted": 0,
}


sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun.raise_for_status()
sun = sun.json()

sunrise = sun["results"]["sunrise"]
sunset = sun["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

current_time = datetime.now()









