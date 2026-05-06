from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("gb_booking_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    arr = np.array([data])
    prediction = model.predict(arr)[0]
    return jsonify({"prediction": int(prediction)})

app.run(debug=True)