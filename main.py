from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and features
model = joblib.load("xgb_model.pkl")
features = joblib.load("feature_names.pkl")

app = FastAPI(title="XGBoost Salary Predictor", version="1.0")

class InputData(BaseModel):
    Age: int
    Gender: str
    Department: str
    JobLevel: int
    MonthlyIncome: float
    OverTime: str
    WorkLifeBalance: int
    JobSatisfaction: int
    YearsAtCompany: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the prediction API. Go to /docs to test."}

@app.post("/predict")
def predict(data: InputData):
    input_data = data.dict()
    input_list = [input_data.get(feature, 0) for feature in features]
    X = np.array(input_list).reshape(1, -1)
    prediction = model.predict(X)
    return {"prediction": float(prediction[0])}

