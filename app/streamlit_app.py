import streamlit as st
from datetime import datetime
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

model = pickle.load(open(model_path, "rb"))


st.title("⚡ Energy Consumption Forecasting System")

date = st.date_input("Select Date")
hour = st.slider("Select Hour", 0, 23)

if st.button("Predict"):

    day = date.day
    month = date.month

    data = pd.DataFrame([[hour, day, month]],
                        columns=['hour', 'day', 'month'])

    prediction = model.predict(data)[0]

    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")