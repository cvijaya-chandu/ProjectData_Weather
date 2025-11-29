"""This file includes the CLI wrapper """


import argparse
from datetime import datetime
from weather_data import get_weather_data

parser = argparse.ArgumentParser()

parser.add_argument(
    "--city",
    type=str,
    required=True,
    help="City name to fetch weather for, mandatory parameter",
)
parser.add_argument(
    "--apikey",
    type=str,
    default="",
    help="API key for OpenWeatherMap, Optional parameter",
)
args = parser.parse_args()
city = args.city
API_KEY = args.apikey
weather_data = get_weather_data(city, API_KEY)

city = input("Enter city: ")
print("\n--- Weather for:", city, "---")

weather_data = get_weather_data(city,API_KEY)
dt = weather_data["dt"]
readable_time = datetime.fromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S")
print("API Timestamp:", readable_time)
print("Temperature:", weather_data["main"]["temp"], "°C")
print("Humidity:", weather_data["main"]["humidity"], "%")
print("Pressure:", weather_data["main"]["pressure"], "hPa")
print("Wind:", weather_data["wind"]["speed"], "m/s")