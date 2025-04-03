import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Sample dataset
data = {
    'amount': [100, 50, 200, 5000, 300, 30, 7000],  # One large transaction (fraud)
    'transaction_type': [1, 0, 1, 1, 0, 0, 1],  # Encoded categories
}

df = pd.DataFrame(data)

# Train Isolation Forest
model = IsolationForest(contamination=0.2)
model.fit(df)

# Save the model
joblib.dump(model, "fraud_model.pkl")  # Save in the current directory
