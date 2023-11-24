from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


forcast = pd.read_csv("./task_2/forcast.csv")


# API endpoint to get temperature for a given date
@app.route("/get_temperature", methods=["GET"])
def get_temperature():
    date = request.args.get("date")

    if date is None:
        return jsonify({"error": "Date parameter is missing"}), 400

    try:
        temperature = forcast.loc[forcast["ds"] == date, "yhat1"].values[0]
        return jsonify({"date": date, "temperature": float(temperature)})
    except IndexError:
        return jsonify({"error": "Date not found in data"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# endpoint-> http://127.0.0.1:5000/get_temperature?date=2024-11-30
if __name__ == "__main__":
    app.run(debug=True)
