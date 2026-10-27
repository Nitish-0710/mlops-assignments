
from pathlib import Path
from typing import Annotated

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field


ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_DIR / "model" / "iris_model.joblib"

app = FastAPI(
    title="Iris Classification API",
    description=(
        "A machine learning REST API built using FastAPI. "
        "It predicts Iris flower species from four measurements."
    ),
    version="1.0.0",
)

# Load the model once when the application starts.
if not MODEL_PATH.exists():
    raise RuntimeError(
        "Model artifact not found. Run "
        "'python scripts/train_model.py' first."
    )

artifact = joblib.load(MODEL_PATH)
model = artifact["model"]
class_names = artifact["class_names"]
feature_names = artifact["feature_names"]


class FlowerFeatures(BaseModel):
    """Input schema for one Iris flower."""

    model_config = ConfigDict(extra="forbid")

    sepal_length: Annotated[float, Field(gt=0, le=10)]
    sepal_width: Annotated[float, Field(gt=0, le=10)]
    petal_length: Annotated[float, Field(gt=0, le=10)]
    petal_width: Annotated[float, Field(gt=0, le=10)]


class BatchPredictionRequest(BaseModel):
    """Input schema for multiple flowers."""

    model_config = ConfigDict(extra="forbid")

    samples: Annotated[
        list[FlowerFeatures],
        Field(min_length=1, max_length=100),
    ]


def predict_one(features: FlowerFeatures) -> dict:
    """Run inference for a single flower."""
    values = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]

    input_array = np.array([values], dtype=float)

    predicted_index = int(model.predict(input_array)[0])
    probabilities = model.predict_proba(input_array)[0]

    return {
        "prediction": class_names[predicted_index],
        "class_id": predicted_index,
        "probabilities": {
            class_names[i]: round(float(probabilities[i]), 4)
            for i in range(len(class_names))
        },
    }


@app.get("/", tags=["General"])
def root():
    """Return API information."""
    return {
        "message": "Welcome to the Iris Classification API",
        "docs": "/docs",
        "health": "/health",
        "prediction_endpoint": "/predict",
    }


@app.get("/health", tags=["General"])
def health_check():
    """Check whether the API and model are available."""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


@app.get("/model-info", tags=["Model"])
def model_info():
    """Return metadata about the trained model."""
    return {
        "model_type": artifact["model_type"],
        "dataset": artifact["dataset"],
        "feature_names": feature_names,
        "class_names": class_names,
        "test_accuracy": artifact["test_accuracy"],
        "sklearn_version": artifact["sklearn_version"],
    }


@app.post("/predict", tags=["Predictions"])
def predict(features: FlowerFeatures):
    """Predict the species of one Iris flower."""
    try:
        return predict_one(features)
    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Prediction could not be completed: {exc}",
        ) from exc


@app.post("/predict/batch", tags=["Predictions"])
def predict_batch(request: BatchPredictionRequest):
    """Predict species for multiple flowers."""
    try:
        predictions = [
            predict_one(sample)
            for sample in request.samples
        ]
        return {
            "count": len(predictions),
            "predictions": predictions,
        }
    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Batch prediction could not be completed: {exc}",
        ) from exc
