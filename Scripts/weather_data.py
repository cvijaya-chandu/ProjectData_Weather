
import requests
from datetime import datetime
#API_KEY = "e594d7f8c36c7d8ba95ce1f167dd7f31"
API_KEY = ""
INTERVAL_SECONDS = 10
URL = "https://api.openweathermap.org/data/2.5/weather"
SIM_TEMP = 25.0
SIM_HUMIDITY = 60
SIM_PRESSURE = 1010
SIM_WIND = 5.0
def get_weather_from_api(city,key):
    params = {
        'q': city,
        'appid': key,
        'units': 'metric'

    }
    print("Calling API for weather data")
    response = requests.get(URL, params=params, timeout=5)
    data = response.json()
    return data

def get_simulated_data(city):
    now = datetime.now()
    dt_val = int(now.timestamp())
    return {
        "dt": dt_val,
        "main":{
            "temp": SIM_TEMP,
            "humidity": SIM_HUMIDITY,
            "pressure": SIM_PRESSURE,
        },
        "wind": {
                "speed": SIM_WIND
            }
        }

def get_weather_data(city,api_key):
    if api_key:
        return get_weather_from_api(city, api_key)
    else:
        print("API Key is missing, Printing simulated data")
        return get_simulated_data(city)

# city = input("Enter city: ")
# print("\n--- Weather for:", city, "---")
#
# weather_data = get_weather_data(city,API_KEY)
# dt = weather_data["dt"]
# readable_time = datetime.fromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S")
# print("API Timestamp:", readable_time)
# print("Temperature:", weather_data["main"]["temp"], "°C")
# print("Humidity:", weather_data["main"]["humidity"], "%")
# print("Pressure:", weather_data["main"]["pressure"], "hPa")
# print("Wind:", weather_data["wind"]["speed"], "m/s")