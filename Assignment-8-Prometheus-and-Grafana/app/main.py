from pathlib import Path
import time

import joblib
import pandas as pd
from fastapi import FastAPI
from prometheus_client import Counter, Gauge, Histogram, start_http_server
from pydantic import BaseModel


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "model" / "wine_quality_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)

# Create FastAPI application
app = FastAPI(
    title="Wine Quality Prediction API",
    description="API for predicting wine quality using a trained Random Forest model.",
    version="1.0.0",
)


# Prometheus metrics
prediction_requests = Counter(
    "model_prediction_requests_total",
    "Total number of prediction requests",
)

prediction_success = Counter(
    "model_prediction_success_total",
    "Total number of successful predictions",
)

prediction_errors = Counter(
    "model_prediction_errors_total",
    "Total number of prediction errors",
)

prediction_latency = Histogram(
    "model_prediction_latency_seconds",
    "Time taken to generate a prediction",
)

prediction_confidence = Gauge(
    "model_prediction_confidence",
    "Confidence of the latest model prediction",
)


class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


@app.on_event("startup")
def start_metrics_server():
    start_http_server(8001)


@app.get("/")
def root():
    return {
        "message": "Wine Quality Prediction API is running.",
        "model": "RandomForestClassifier",
    }


@app.post("/predict")
def predict(features: WineFeatures):
    prediction_requests.inc()

    start_time = time.perf_counter()

    try:
        input_data = pd.DataFrame(
            [
                {
                    "fixed acidity": features.fixed_acidity,
                    "volatile acidity": features.volatile_acidity,
                    "citric acid": features.citric_acid,
                    "residual sugar": features.residual_sugar,
                    "chlorides": features.chlorides,
                    "free sulfur dioxide": features.free_sulfur_dioxide,
                    "total sulfur dioxide": features.total_sulfur_dioxide,
                    "density": features.density,
                    "pH": features.pH,
                    "sulphates": features.sulphates,
                    "alcohol": features.alcohol,
                }
            ]
        )

        prediction = int(model.predict(input_data)[0])
        probabilities = model.predict_proba(input_data)[0]
        confidence = float(max(probabilities))

        label = "Good" if prediction == 1 else "Bad"

        prediction_success.inc()
        prediction_confidence.set(confidence)

        return {
            "prediction": prediction,
            "quality_label": label,
            "confidence": confidence,
        }

    except Exception:
        prediction_errors.inc()
        raise

    finally:
        prediction_latency.observe(time.perf_counter() - start_time)