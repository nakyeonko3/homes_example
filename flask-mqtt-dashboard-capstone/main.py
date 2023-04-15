# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify

import read_csvfile


app = Flask(__name__)
port = 5000
sensor_value = 0


@app.route("/")
def render_mainpage():
    return render_template("index.html", name="nakyeonko")


@app.route("/getTemperSeneorData")
def getTemperSeneorData():
    temper_sensor_value = read_csvfile.get_senor_data_last_value(
        file_name="temper_sensor.csv", name="temper"
    )
    temper_sensor_value = float(temper_sensor_value)
    return jsonify({"sensor_data": temper_sensor_value})


@app.route("/getPHSensorData")
def getPHSensorData():
    sensor_value = read_csvfile.get_senor_data_last_value(
        file_name="sensor.csv", name="ph"
    )
    sensor_value = float(sensor_value)
    return jsonify({"sensor_data": sensor_value})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
