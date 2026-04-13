import streamlit as st
import pickle
import os
import pandas as pd

# Get base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

# Load model safely
if not os.path.exists(model_path):
    st.error("❌ Model file not found. Run train_model.py first.")
    st.stop()

with open(model_path, "rb") as f:
    model = pickle.load(f)

# UI
st.title("⚡ Energy Consumption Forecasting System")

date = st.date_input("Select Date")
hour = st.slider("Select Hour", 0, 23)

# Prediction
if st.button("Predict"):

    day = date.day
    month = date.month

    data = pd.DataFrame(
        [[hour, day, month]],
        columns=['hour', 'day', 'month']
    )

    prediction = model.predict(data)[0]

    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")