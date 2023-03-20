import os

import requests

from flask import Flask, request

from messages import make_response
import config

app = Flask(__name__)


@app.route('/', methods=["GET"])
def health_check():
    payload = {
        "message": "Welcome to the microservice master",
        "status": "success"
    }
    return make_response(payload, 200)


@app.route('/predict_disease', methods=["POST"])
def predict_disease():
    sector = request.get_json()['sector']
    payload = {
        "sector": sector
    }
    response = requests.post(f'http://{config.PD_HOST}:{config.PD_PORT}/predict_disease', json=payload)
    return make_response(response.json())


@app.route('/read_temperature/<sector>', methods=["GET"])
def get_temp_readings(sector):
    response = requests.get(f'http://{config.TH_HOST}:{config.TH_PORT}/read_temperature/' + sector)
    return make_response(response.json())


@app.route('/read_humidity/<sector>', methods=["GET"])
def get_humidity_readings(sector):
    response = requests.get(f'http://{config.TH_HOST}:{config.TH_PORT}/read_humidity/' + sector)
    return make_response(response.json())


if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host=config.MASTER_HOST, port=config.MASTER_PORT
    )
