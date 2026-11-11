
import requests

import os
from dotenv import load_dotenv

load_dotenv()


class Weather:
    def __init__(self, city, temperature, humidity):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity

    def display(self):
        print("===== WEATHER REPORT =====")
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature} °C")
        print(f"Humidity: {self.humidity} %")
        print("==========================")



url = os.getenv("WEATHER_API_URL")

parameters = {
    "latitude": float(os.getenv("LATITUDE")),
    "longitude": float(os.getenv("LONGITUDE")),
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": "Africa/Cairo"
}


response = requests.get(url, params=parameters, timeout=10)
response.raise_for_status()
data = response.json()

weather = Weather(
    city=os.getenv("CITY"),
    temperature=data["current"]["temperature_2m"],
    humidity=data["current"]["relative_humidity_2m"]
)

weather.display()
