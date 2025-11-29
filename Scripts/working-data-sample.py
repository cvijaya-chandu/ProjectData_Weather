from os import pread

weather_data = {'coord': {'lon': 24.9355, 'lat': 60.1695}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}],
 'base': 'stations', 'main': {'temp': 5.1, 'feels_like': -1.51, 'temp_min': 4.44, 'temp_max': 5.98, 'pressure': 1003, 'humidity': 98,
'sea_level': 1003, 'grnd_level': 1001}, 'visibility': 4500, 'wind': {'speed': 15.65, 'deg': 206,
'gust': 18.78}, 'clouds': {'all': 75}, 'dt': 1764306144, 'sys': {'type': 2, 'id': 2011913, 'country': 'FI', 'sunrise': 1764312624,
'sunset': 1764336386}, 'timezone': 7200, 'id': 658225, 'name': 'Helsinki', 'cod': 200}

print(weather_data)
print(weather_data['main']['pressure'])
print(weather_data['main']['temp'])

print(weather_data['sys']['country'])
print(weather_data['name'])