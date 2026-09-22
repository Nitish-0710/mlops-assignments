from pathlib import Path
import json
import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.preprocessing import feature_engineering

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "house_price_pipeline.joblib"
METADATA_PATH = BASE_DIR / "model" / "model_metadata.json"


app = FastAPI(
    title="House Price Prediction API",
    version="1.0.0"
)

model = None
metadata = {}


class HouseFeatures(BaseModel):
    features: dict


@app.on_event("startup")
def load_model():
    global model, metadata

    model = joblib.load(MODEL_PATH)

    if METADATA_PATH.exists():
        with open(METADATA_PATH) as f:
            metadata = json.load(f)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.get("/model-info")
def model_info():
    return metadata


@app.post("/predict")
def predict(request: HouseFeatures):

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded"
        )

    try:
        input_df = pd.DataFrame([request.features])

        prediction = model.predict(input_df)[0]

        return {
            "predicted_sale_price": float(prediction)
        }

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )