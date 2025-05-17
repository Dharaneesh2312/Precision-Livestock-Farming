
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("health_model.pkl")  # Pre-trained ML model

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    result = "Normal" if prediction == 0 else "Anomaly Detected"

    return jsonify({"status": "received", "prediction": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
