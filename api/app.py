from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import shap

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
BACKGROUND_PATH = os.path.join(BASE_DIR, "models", "shap_background.csv")

# -----------------------------
# Load Model + Scaler + SHAP
# -----------------------------
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
background = pd.read_csv(BACKGROUND_PATH)
explainer = shap.Explainer(model, background)

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="Fraud Detection API")

# -----------------------------
# Input Schema
# -----------------------------
class Transaction(BaseModel):
    Time: float
    Amount: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}

# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(transaction: Transaction):
    try:
        # Convert to DataFrame
        data = transaction.dict()
        df = pd.DataFrame([data])

        # Scale Amount + Time (same as training)
        df[['Amount', 'Time']] = scaler.transform(df[['Amount', 'Time']])

        # Fix column order
        df = df[model.feature_names_in_]

        # Predict
        prob = model.predict_proba(df)[0][1]
        pred = model.predict(df)[0]

        # -----------------------------
        # SHAP Explainability
        # -----------------------------
        shap_values = explainer(df)
        shap_dict = {}

        for i, val in enumerate(shap_values.values[0]):
            shap_dict[df.columns[i]] = float(val)

        top_features = dict(
            sorted(shap_dict.items(), key=lambda x: abs(x[1]), reverse=True)[:5]
        )

        return {
            "fraud_probability": float(prob),
            "prediction": "FRAUD" if pred == 1 else "LEGIT",
            "top_features": top_features
        }

    except Exception as e:
        return {"error": str(e)}
