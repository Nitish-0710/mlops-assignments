# Assignment 6: Create REST API Using FastAPI

## Overview

This assignment demonstrates how to deploy a machine learning model through a REST API built using FastAPI.

A Random Forest classifier is trained on the Iris dataset and exposed through HTTP endpoints. The API accepts JSON input, validates requests, and returns predicted flower species and class probabilities.

## Objectives

- Understand REST API development.
- Build endpoints using FastAPI.
- Train and serialize a machine learning model.
- Validate requests using Pydantic.
- Serve single and batch predictions.
- Test endpoints using pytest.
- Explore automatic API documentation using Swagger UI.

## Technology Stack

- Python
- FastAPI
- Uvicorn
- scikit-learn
- NumPy
- Joblib
- Pydantic
- pytest
- HTTPX

## Project Structure

```text
Assignment-6-REST-API/
├── app/
│   ├── __init__.py
│   └── main.py
├── model/
│   └── iris_model.joblib
├── scripts/
│   └── train_model.py
├── tests/
│   └── test_api.py
└── README.md
```

## Setup

Activate your Python virtual environment and install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Train the Model

```bash
python scripts/train_model.py
```

This generates `model/iris_model.joblib`.

## Run the API

```bash
python -m uvicorn app.main:app --reload
```

The API runs at:

http://127.0.0.1:8000

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

Alternative ReDoc documentation:

http://127.0.0.1:8000/redoc

## Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | `/`              | API welcome message |
| GET    | `/health`        | Service health      |
| GET    | `/model-info`    | Model metadata      |
| POST   | `/predict`       | Single prediction   |
| POST   | `/predict/batch` | Batch prediction    |

## Example Request

POST `/predict`

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Run Tests

```bash
python -m pytest -v
```

## Concepts Demonstrated

- RESTful API design
- HTTP GET and POST methods
- JSON request and response handling
- Pydantic validation
- Machine learning model serialization
- Model inference through an API
- Automated API testing
- OpenAPI documentation

## Conclusion

This assignment demonstrates how a trained machine learning model can be exposed through a REST API using FastAPI. It provides a foundation for integrating machine learning inference into larger MLOps workflows.
