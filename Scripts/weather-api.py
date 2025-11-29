"""This File includes the FLASK and Weather API"""

from flask import Flask, request,jsonify
from datetime import datetime
from weather_data import get_weather_data


app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    api_key = request.args.get("apiKey")
    if not city:
        return jsonify({"error": "city is required"}), 400

    data = get_weather_data(city,api_key)
    # print(data)
    dt = datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
    response = {
        "description": f"Simulated weather data of {city}" if not api_key == "" else f"Live weather data of {city}",
        "city": city,
        "timestamp": dt,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"]
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
