import streamlit as st
import joblib
import os

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "models", "model.pkl")

model = joblib.load(model_path)

st.title("Energy Consumption Predictor")

hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)

if st.button("Predict"):
    prediction = model.predict([[hour, day, month]])
    st.success(f"Predicted Energy Consumption: {prediction[0]}")