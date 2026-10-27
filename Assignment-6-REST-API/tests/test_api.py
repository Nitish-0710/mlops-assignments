
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

VALID_FLOWER = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
}


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Welcome to the Iris Classification API"
    )


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True


def test_model_info_endpoint():
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()
    assert data["dataset"] == "Iris"
    assert data["model_type"] == "RandomForestClassifier"
    assert len(data["feature_names"]) == 4
    assert len(data["class_names"]) == 3


def test_single_prediction():
    response = client.post("/predict", json=VALID_FLOWER)

    assert response.status_code == 200

    data = response.json()
    assert data["prediction"] in [
        "setosa",
        "versicolor",
        "virginica",
    ]
    assert data["class_id"] in [0, 1, 2]
    assert set(data["probabilities"].keys()) == {
        "setosa",
        "versicolor",
        "virginica",
    }

    assert abs(sum(data["probabilities"].values()) - 1.0) < 0.001


def test_batch_prediction():
    response = client.post(
        "/predict/batch",
        json={
            "samples": [VALID_FLOWER, VALID_FLOWER],
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 2
    assert len(data["predictions"]) == 2


def test_missing_feature_returns_validation_error():
    invalid_flower = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
    }

    response = client.post("/predict", json=invalid_flower)

    assert response.status_code == 422


def test_invalid_measurement_returns_validation_error():
    invalid_flower = {
        **VALID_FLOWER,
        "sepal_length": -1,
    }

    response = client.post("/predict", json=invalid_flower)

    assert response.status_code == 422


def test_extra_field_is_rejected():
    invalid_flower = {
        **VALID_FLOWER,
        "unknown_feature": 123,
    }

    response = client.post("/predict", json=invalid_flower)

    assert response.status_code == 422


def test_empty_batch_is_rejected():
    response = client.post(
        "/predict/batch",
        json={"samples": []},
    )

    assert response.status_code == 422
