import streamlit as st
from datetime import datetime
import pickle
import pandas as pd

model = pickle.load(open("../models/model.pkl", "rb"))

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