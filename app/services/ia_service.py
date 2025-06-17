from app.database.mongo import db
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_moisture():
    data = list(db.sensor_data.find({}, {"soil_moisture": 1, "_id": 0}))
    X = np.array([[i] for i in range(len(data))])
    y = np.array([d["soil_moisture"] for d in data])
    model = LinearRegression().fit(X, y)
    pred = model.predict([[len(data)]])[0]
    return {"forecast": pred}
