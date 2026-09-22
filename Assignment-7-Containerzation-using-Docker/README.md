# Containerized ML Prediction Service using Docker

## House Price Prediction API

An end-to-end Machine Learning deployment assignment that trains a house price prediction model on the Ames Housing dataset, persists the complete ML pipeline, exposes it through a FastAPI REST API, and containerizes the application using Docker.

---

## 1. Assignment Overview

This assignment demonstrates the complete workflow from Machine Learning model development to containerized deployment.

The system performs:

- Data loading and exploratory analysis
- Missing-value handling
- Categorical feature encoding
- Numerical feature scaling
- Feature engineering
- Model training and comparison
- Hyperparameter tuning
- Model evaluation
- Model persistence using Joblib
- REST API development using FastAPI
- Docker containerization
- Containerized API testing

The final model is a `GradientBoostingRegressor` that predicts the `SalePrice` of a house.

---

## 2. Architecture

```text
                    Ames Housing Dataset
                            |
                            v
                 Data Cleaning & EDA
                            |
                            v
                  Feature Engineering
                            |
                            v
              Numerical / Categorical
                   Preprocessing
                            |
                            v
              Gradient Boosting Regressor
                            |
                            v
                 Model Persistence
                  (.joblib pipeline)
                            |
                            v
                       FastAPI
                 +----------+----------+
                 |          |          |
                 v          v          v
              /health   /model-info  /predict
                            |
                            v
                    Docker Container
                            |
                            v
                       Port 8000
```

---

## 3. Dataset

### Ames Housing / House Prices

The assignment uses the Ames Housing / House Prices dataset.

| Property               | Value       |
| ---------------------- | ----------- |
| Records                | 1,460       |
| Target                 | `SalePrice` |
| Problem Type           | Regression  |
| Raw API Input Features | 79          |

The dataset contains residential property characteristics including:

* Overall quality
* Living area
* Basement information
* Garage information
* Year built
* Remodeling year
* Neighborhood
* Porch/deck information
* Number of rooms and bathrooms
* Other property attributes

---

## 4. Machine Learning Pipeline

### Data Preprocessing

The pipeline performs:

1. Missing-value handling
2. Categorical feature encoding
3. Numerical feature scaling
4. Feature engineering

### Feature Engineering

The following features are generated automatically during inference:

* `HouseAge`
* `RemodAge`
* `TotalSF`
* `TotalBathrooms`
* `TotalPorchSF`

The feature engineering logic is included inside the persisted ML pipeline.

Therefore, the API accepts the original 79 raw input features.

```text
79 Raw Features
       |
       v
Feature Engineering
       |
       v
84 Processed Feature Groups
       |
       v
Preprocessing
       |
       v
Gradient Boosting
       |
       v
Prediction
```

---

## 5. Model

Several regression models were evaluated:

* Linear Regression
* Ridge Regression
* Random Forest Regressor
* Gradient Boosting Regressor

The final model is:

```text
GradientBoostingRegressor
```

### Final Hyperparameters

```text
n_estimators      = 300
learning_rate     = 0.05
max_depth         = 3
min_samples_split = 2
```

Hyperparameter tuning was performed using:

```text
GridSearchCV
Cross-validation: 5-fold
Scoring: Negative Root Mean Squared Error
```

---

## 6. Model Performance

Final performance on the held-out test set:

| Metric           |     Value |
| ---------------- | --------: |
| Training Samples |     1,168 |
| Testing Samples  |       292 |
| Best CV RMSE     | 28,390.88 |
| MAE              | 16,782.20 |
| RMSE             | 26,615.06 |
| R²               |    0.9076 |

---

## 7. Model Persistence

The complete preprocessing and prediction pipeline is saved using Joblib:

```text
model/house_price_pipeline.joblib
```

The pipeline contains:

```text
Feature Engineering
        +
Numerical Preprocessing
        +
Categorical Preprocessing
        +
Gradient Boosting Model
```

Model metadata is stored in:

```text
model/model_metadata.json
```

The saved pipeline was reloaded and verified successfully.

```text
Maximum prediction difference: 0.0
Verification successful.
```

---

## 8. FastAPI

The trained model is exposed through a FastAPI REST API.

### Available Endpoints

| Method | Endpoint      | Description                        |
| ------ | ------------- | ---------------------------------- |
| GET    | `/health`     | Checks API and model status        |
| GET    | `/model-info` | Returns model metadata             |
| POST   | `/predict`    | Generates a house price prediction |

---

## 9. API Health Check

Request:

```http
GET /health
```

Response:

```json
{
    "status": "healthy",
    "model_loaded": true
}
```

---

## 10. Model Information

Request:

```http
GET /model-info
```

The endpoint returns information such as:

* Dataset
* Target
* Problem type
* Training/testing samples
* Model
* Hyperparameters
* Evaluation metrics
* Model artifact

---

## 11. Prediction API

Request:

```http
POST /predict
```

The request body has the following structure:

```json
{
    "features": {
        "MSSubClass": 60,
        "MSZoning": "RL",
        "LotFrontage": 65,
        "LotArea": 8450
    }
}
```

The complete request should contain the required raw house features.

Example response:

```json
{
    "predicted_sale_price": 206683.6112930261
}
```

---

## 12. Assignment Structure

```text
Assignment-7-Containerzation-using-Docker/
│
├── app/
│   ├── main.py
│   └── preprocessing.py
│
├── data/
│   └── house_prices.csv
│
├── model/
│   ├── house_price_pipeline.joblib
│   └── model_metadata.json
│
├── notebooks/
│   └── Assignment7.ipynb
│
├── scripts/
│   └── test_api.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 13. Requirements

The application uses:

```text
Python 3.12
FastAPI
Uvicorn
Pandas
NumPy
Scikit-learn
Joblib
Pydantic
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 14. Run Locally Without Docker

From the assignment root:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 15. Test the Local API

In another terminal:

```bash
python scripts/test_api.py
```

Expected result:

```text
Number of fields: 79

Health: 200
{'status': 'healthy', 'model_loaded': True}

Model info: 200
{...}

Prediction: 200
{'predicted_sale_price': 206683.6112930261}
```

---

# 16. Docker

## Docker Base Image

The assignment uses:

```dockerfile
FROM python:3.12-slim
```

This provides a lightweight Python environment suitable for deployment.

---

## 17. Build Docker Image

From the assignment rootent root:

```bash
docker build -t house-price-api .
```

Verify the image:

```bash
docker images
```

Expected image:

```text
house-price-api:latest
```

---

## 18. Run Docker Container

Run:

```bash
docker run -d \
  --name house-price-container \
  -p 8000:8000 \
  house-price-api
```

On Windows CMD, the same command can be written on one line:

```cmd
docker run -d --name house-price-container -p 8000:8000 house-price-api
```

---

## 19. Verify Running Container

Run:

```bash
docker ps
```

Expected:

```text
CONTAINER ID   IMAGE             STATUS       PORTS
...            house-price-api   Up           0.0.0.0:8000->8000/tcp
```

---

## 20. Test the Containerized API

Once the container is running:

```bash
python scripts/test_api.py
```

Expected:

```text
Health: 200
Model info: 200
Prediction: 200
```

The tested prediction was:

```text
206683.6112930261
```

---

## 21. Docker Logs

To view container logs:

```bash
docker logs house-price-container
```

Expected startup output includes:

```text
Application startup complete.
Uvicorn running on http://0.0.0.0:8000
```

---

## 22. Swagger Documentation

After starting the Docker container, open:

```text
http://localhost:8000/docs
```

The Swagger interface provides interactive access to:

```text
GET  /health
GET  /model-info
POST /predict
```

---

## 23. Docker Container Verification

The containerized service was successfully verified with:

```text
Health: 200
Model info: 200
Prediction: 200
```

The model successfully loaded inside the Docker container and generated a prediction.

---

## 24. Useful Docker Commands

### List images

```bash
docker images
```

### List running containers

```bash
docker ps
```

### View all containers

```bash
docker ps -a
```

### View container logs

```bash
docker logs house-price-container
```

### Stop container

```bash
docker stop house-price-container
```

### Start existing container

```bash
docker start house-price-container
```

### Remove container

```bash
docker rm house-price-container
```

### Remove image

```bash
docker rmi house-price-api
```

---

## 25. Troubleshooting

### Docker command not found

Make sure Docker Desktop is installed and running.

Verify:

```bash
docker --version
```

### Port 8000 already in use

Check running containers:

```bash
docker ps
```

Stop the container using the port or use another host port:

```bash
docker run -d --name house-price-container -p 8001:8000 house-price-api
```

### Check container logs

```bash
docker logs house-price-container
```

### Check container status

```bash
docker ps -a
```

---

## 26. Key Learning Outcomes

This assignment demonstrates:

* Building a complete ML preprocessing pipeline
* Feature engineering for tabular data
* Model comparison and hyperparameter tuning
* Model persistence
* REST API development with FastAPI
* Separation of training and inference environments
* Docker image creation
* Docker container execution
* Containerized ML model serving
* API testing and deployment verification
* Basic reproducibility practices in MLOps

---

## 27. Final Result

The Ames Housing house price prediction model was successfully:

```text
Trained
   ↓
Evaluated
   ↓
Persisted
   ↓
Exposed through FastAPI
   ↓
Containerized with Docker
   ↓
Executed inside Docker
   ↓
Tested successfully
```

The final Dockerized service successfully served predictions through the FastAPI `/predict` endpoint.