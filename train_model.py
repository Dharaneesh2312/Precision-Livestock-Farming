
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Simulated training data
data = pd.DataFrame({
    'temperature': [38.5, 39.0, 38.2, 41.2, 37.8],
    'heartbeat': [70, 72, 69, 90, 65],
    'motion': [1, 1, 0, 1, 0]
})

# Train model
model = IsolationForest(contamination=0.2)
model.fit(data)

# Save model
joblib.dump(model, 'health_model.pkl')
