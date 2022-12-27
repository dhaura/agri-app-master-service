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


if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host=config.MASTER_HOST, port=os.getenv('PORT', config.MASTER_PORT)
    )
