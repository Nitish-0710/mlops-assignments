# Assignment 8: Model Monitoring using Prometheus and Grafana

## 1. Objective

The objective of this assignment is to implement a machine learning model monitoring system using **Prometheus and Grafana**.

A Random Forest classifier is trained on the Wine Quality dataset and deployed through a FastAPI application. Prometheus collects application metrics, while Grafana visualizes these metrics through a monitoring dashboard.

The assignment demonstrates model training, API deployment, metrics instrumentation, monitoring, and visualization.

## 2. Technologies Used

- **Programming language:** Python
- **Machine learning:** pandas, scikit-learn
- **Model serialization:** joblib
- **API framework:** FastAPI
- **ASGI server:** Uvicorn
- **Metrics instrumentation:** prometheus-client
- **Metrics collection:** Prometheus
- **Monitoring dashboard:** Grafana
- **Dataset:** UCI Wine Quality — Red Wine

## 3. Dataset

The project uses the red wine dataset from the UCI Machine Learning Repository.

- **Dataset file:** `data/winequality-red.csv`
- **Total samples:** 1,599
- **Total columns:** 12
- **Input features:** 11 physicochemical properties
- **Target:** Binary wine quality classification

The original quality scores are converted into two classes:

| Class | Condition | Label |
|---|---|---|
| 0 | Quality score below 6 | Bad |
| 1 | Quality score greater than or equal to 6 | Good |

The dataset is divided into training and testing sets using an 80:20 stratified split with `random_state=42`.

## 4. Model Development

A `RandomForestClassifier` is trained using the 11 input features. The original quality column is excluded from the input features to prevent target leakage.

### Model configuration

- Algorithm: Random Forest Classifier
- Number of estimators: 200
- Random state: 42
- Training samples: 1,279
- Testing samples: 320

### Model evaluation

The model achieved the following results on the test set:

| Metric | Score |
|---|---:|
| Accuracy | 0.8156 |
| Precision | 0.8373 |
| Recall | 0.8129 |
| F1-score | 0.8249 |
| ROC-AUC | 0.9057 |

The trained model is saved as `model/wine_quality_model.pkl` and loaded by the FastAPI application for predictions.

## 5. Project Structure

```text
Assignment-8-Prometheus-and-Grafana/
├── app/
│   └── main.py
├── data/
│   ├── winequality-red.csv
│   └── winequality.names
├── model/
│   └── wine_quality_model.pkl
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── wine_quality_dashboard.json
├── Assignment8.ipynb
└── README.md
```

## 6. FastAPI Application

The trained model is served through a FastAPI application implemented in `app/main.py`.

### Available endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| POST | `/predict` | Predicts wine quality from input features |
| GET | `/docs` | Opens the interactive Swagger API documentation |

The prediction endpoint accepts 11 numerical input features and returns the predicted class, quality label, and prediction confidence.

### Example prediction request

```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.70,
  "citric_acid": 0.00,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11.0,
  "total_sulfur_dioxide": 34.0,
  "density": 0.9978,
  "pH": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
```

Example response:

```json
{
  "prediction": 0,
  "quality_label": "Bad",
  "confidence": 0.99
}
```

The confidence represents the maximum class probability returned by the classifier.

## 7. Prometheus Integration

The application uses the `prometheus-client` library to expose metrics on port `8001`. The FastAPI service runs separately on port `8000`.

### Metrics implemented

| Metric | Type | Description |
|---|---|---|
| `model_prediction_requests_total` | Counter | Total prediction requests received |
| `model_prediction_success_total` | Counter | Total successful predictions |
| `model_prediction_errors_total` | Counter | Total prediction errors |
| `model_prediction_latency_seconds` | Histogram | Distribution of prediction latency |
| `model_prediction_confidence` | Gauge | Confidence of the latest prediction |

Prometheus also exposes standard Python runtime metrics.

### Prometheus configuration

The configuration is stored in `prometheus/prometheus.yml`:

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "wine-quality-model"
    static_configs:
      - targets: ["localhost:8001"]
```

Prometheus scrapes the application's metrics endpoint every five seconds. Prometheus uses port **9090** by default.

## 8. Grafana Dashboard

The dashboard is named **Wine Quality Model Monitoring** and its exported configuration is stored at `grafana/wine_quality_dashboard.json`.

The dashboard contains five panels:

1. **Total Prediction Requests** — total number of prediction requests.
2. **Successful Predictions** — number of successful predictions.
3. **Prediction Errors** — number of prediction errors.
4. **Latest Prediction Confidence** — confidence of the latest prediction.
5. **Prediction Latency** — average prediction latency over time.

The latency panel uses the following PromQL expression:

```promql
rate(model_prediction_latency_seconds_sum[5m])
/
rate(model_prediction_latency_seconds_count[5m])
```

This calculates average prediction latency over a five-minute window when sufficient observations are available.

### Service URLs

| Service | URL |
|---|---|
| FastAPI | `http://localhost:8000` |
| Swagger documentation | `http://localhost:8000/docs` |
| Application metrics | `http://localhost:8001/metrics` |
| Prometheus | `http://localhost:9090` |
| Prometheus targets | `http://localhost:9090/targets` |
| Grafana | `http://localhost:3000` |

### Grafana data source

For a standard local setup where Grafana and Prometheus are both accessible from the host, configure the Prometheus data source URL as:

`http://localhost:9090`

If Grafana itself runs inside Docker, use `http://host.docker.internal:9090` to reach Prometheus running on the Windows host. During dashboard import, map the dashboard's `prometheus-1` data-source input to the configured Prometheus data source.

## 9. Installation and Execution

### Prerequisites

Install Python, Prometheus, and Grafana. These instructions use Windows Command Prompt (CMD) and assume Prometheus and Grafana are installed or configured to run locally.

Run the Python commands from the repository root unless otherwise stated.

### Step 1: Activate the Python environment

If the repository's `.mlops` environment already exists:

```bat
.mlops\Scripts\activate
```

Otherwise, create and activate it:

```bat
python -m venv .mlops
.mlops\Scripts\activate
```

### Step 2: Install dependencies

From the repository root:

```bat
python -m pip install -r requirements.txt
```

The repository-level `requirements.txt` contains the shared Python dependencies, including `prometheus-client`.

### Step 3: Start the FastAPI application

Change to the Assignment 8 directory:

```bat
cd Assignment-8-Prometheus-and-Grafana
```

Start the API:

```bat
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Keep this terminal running.

Open Swagger UI at `http://localhost:8000/docs`. The metrics endpoint should be available at `http://localhost:8001/metrics`.

### Step 4: Start Prometheus

Open a second CMD terminal and navigate to the directory containing your `prometheus.exe`. Start Prometheus with the assignment configuration and a dedicated storage directory.

If the Prometheus executable and the assignment folder are in separate directories, replace the paths below with the actual locations on your computer:

```bat
prometheus.exe --config.file="D:\path\to\Assignment-8-Prometheus-and-Grafana\prometheus\prometheus.yml" --storage.tsdb.path="D:\path\to\Assignment-8-Prometheus-and-Grafana\prometheus-data"
```

Prometheus uses port `9090` by default. Open `http://localhost:9090/targets` and confirm that the `wine-quality-model` target is **UP**.

> The `prometheus-data` directory stores local time-series data and should not be committed to Git.

### Step 5: Configure Grafana

1. Open `http://localhost:3000`.
2. Add a Prometheus data source.
3. Set the URL to `http://localhost:9090` for a standard local setup.
4. Click **Save & test** and confirm that the connection succeeds.
5. Import `grafana/wine_quality_dashboard.json` if the dashboard is not already present.
6. During import, map the dashboard's `prometheus-1` data-source input to the configured Prometheus data source.
7. Save the dashboard.

### Step 6: Generate prediction requests

Open `http://localhost:8000/docs`, expand `POST /predict`, select **Try it out**, enter the example JSON from Section 6, and click **Execute**.

Repeat the request several times to generate metric observations. Return to Grafana to observe the request and success counters, prediction errors, latest confidence, and latency graph.

## 10. Results and Observations

During the observed test session, the metrics endpoint reported:

- Total prediction requests: 6
- Successful predictions: 6
- Prediction errors: 0
- Latest prediction confidence: 0.99
- Total recorded prediction latency: approximately 0.4414 seconds

These values represent the observed test session and may differ after additional requests or when the application is restarted.

The Grafana dashboard displays the collected metrics and helps monitor prediction activity and latency.

## 11. Conclusion

This assignment demonstrates an end-to-end machine learning monitoring workflow. A Random Forest classifier is trained on the Wine Quality dataset and deployed using FastAPI. Prometheus collects application-level metrics, while Grafana provides a visual dashboard for monitoring requests, prediction errors, confidence, and latency.

The implementation illustrates how monitoring tools can be integrated with a machine learning API to improve visibility into application behaviour and support operational monitoring.

## References

- UCI Machine Learning Repository — Wine Quality Dataset: https://archive.ics.uci.edu/dataset/186/wine+quality
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Prometheus Documentation: https://prometheus.io/docs/
- Grafana Documentation: https://grafana.com/docs/
