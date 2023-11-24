from flask import Flask, jsonify
import requests
import json
from tqdm import tqdm


app = Flask(__name__)


# Fetch weather forecasts for each district
def fetch_weather_forecast(latitude, longitude):
    endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=temperature_2m_min&timezone=GMT"
    response = requests.get(endpoint)

    if response.status_code == 200:
        forecast_data = response.json()
        return forecast_data
    else:
        print(f"Failed to fetch data for coordinates: {latitude}, {longitude}")
        return None


# Read the JSON file containing districts' latitude and longitude
file_path = "./task_1/bd-districts.json"
with open(file_path, "r", encoding="utf-8") as file:
    districts_data = json.load(file)
districts = districts_data["districts"]
hashMap = {}
for district in tqdm(districts):
    district_name = district["name"]
    latitude = district["lat"]
    longitude = district["long"]
    res = 0
    district_forecasts = fetch_weather_forecast(latitude, longitude)
    if district_forecasts is not None:
        temperatures = district_forecasts["hourly"]["temperature_2m"]
        for temperature in temperatures[
            14::24
        ]:  # 14 means 2 p.m., 24 means every 24 hours later we get 2 p.m.
            res += float(temperature)
        weekly_2pm_avg = res / 7
        hashMap[district_name] = weekly_2pm_avg
    else:
        print(f"No data available for {district_name}")


# fetch coolest 10 districts from the hashMap of district_name keys and temperature values
forecast_coolest_10 = sorted(hashMap.items(), key=lambda x: x[1])[:10]


@app.route("/coolest_10", methods=["GET"])
def get_coolest_districts():
    return jsonify(forecast_coolest_10)


# endpoint-> http://127.0.0.1:5000/coolest_10
if __name__ == "__main__":
    app.run(debug=True)
