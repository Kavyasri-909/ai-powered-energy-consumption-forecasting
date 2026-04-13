import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

from data_preprocessing import load_data, preprocess

df = load_data("data/raw/energy.csv")
df = preprocess(df)

X = df[['hour', 'day', 'month']]
y = df['Energy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")