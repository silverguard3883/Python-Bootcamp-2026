import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "api.openweathermap.org/data/2.5/forecast"

"""
Below are fake alphanumeric ids. These are for demo purposes only. Better to use environment variables.

API_KEY = "bd9c26981ec16844c4e7d8592d1e3d19"
ACCOUNT_SID = "6f8614b8f0821b101d37c8e667e22251"
AUTH_TOKEN = "9b2d49d6f70d0319fecdf2d5ae2b8fbc"
"""

api_key = os.environ.get("OWM_API_KEY")
account = os.environ.get("ACCOUNT_SID")
token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 40.71,
    "lon": -73.99,
    "app_id": API_KEY,
    "cnt": 4,                                               #Checks weather in 12 hour increments
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(response.json()["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    weather_condition = hour_data["weather"][0]["id"]
    if int(weather_condition) < 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body= "Bring an umbrella", from= "+1234567890", to= "+1234567890",)

