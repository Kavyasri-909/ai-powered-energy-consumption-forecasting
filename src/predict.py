import pickle
import pandas as pd

model = pickle.load(open("models/model.pkl", "rb"))

def predict(hour, day, month):
    data = pd.DataFrame([[hour, day, month]],
                        columns=['hour', 'day', 'month'])
    return model.predict(data)[0]