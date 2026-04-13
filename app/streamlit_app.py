import pandas as pd
import os
import pickle
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data/raw/energy.csv")

# Features
X = data[['hour', 'day', 'month']]
y = data['energy_consumption']

# Train model
model = LinearRegression()
model.fit(X, y)

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Save model properly
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully!")