# Assignment 4 – Automated ML Training Pipeline Using Apache Airflow

## Objective

To build an automated Machine Learning training pipeline using **Apache Airflow** that orchestrates data preprocessing, model training, and model evaluation as a scheduled workflow.

The pipeline demonstrates how Airflow can be used in MLOps to automate and monitor the execution of Machine Learning tasks.

---

## Problem Statement

Machine Learning workflows often involve multiple dependent steps such as data preprocessing, model training, and model evaluation. Running these steps manually can be time-consuming and error-prone.

This assignment implements an automated ML pipeline where Apache Airflow schedules and executes the complete workflow in the correct order.

---

## Technologies Used

- Python 3.14
- Apache Airflow 3.3.0
- Jupyter Notebook
- Jupyter nbconvert
- Scikit-learn
- Pandas
- Joblib
- WSL 2
- Ubuntu
- VS Code

---

## Dataset

The **Breast Cancer Wisconsin Dataset** provided by `scikit-learn` is used for this assignment.

The dataset contains:

- **569 samples**
- **30 features**
- **1 target variable**

The dataset is saved locally as:

```text
data/dataset.csv
````

---

## Machine Learning Model

The pipeline uses **Logistic Regression** for binary classification.

The dataset is divided into:

```text
Training samples: 455
Testing samples : 114
```

---

## ML Pipeline

The Machine Learning workflow consists of three notebooks:

```text
data_preprocessing.ipynb
          ↓
model_training.ipynb
          ↓
model_evaluation.ipynb
```

### 1. Data Preprocessing

The `data_preprocessing.ipynb` notebook:

* Loads the dataset.
* Separates features and target.
* Splits the dataset into training and testing data.
* Saves the processed datasets for the next stage.

### 2. Model Training

The `model_training.ipynb` notebook:

* Loads the training data.
* Trains a Logistic Regression model.
* Saves the trained model using Joblib.

Output:

```text
models/trained_model.pkl
```

### 3. Model Evaluation

The `model_evaluation.ipynb` notebook:

* Loads the trained model.
* Evaluates it using the test dataset.
* Calculates accuracy and classification metrics.
* Generates the final training report.

Output:

```text
output/training_report.txt
```

---

# Airflow Automation

Apache Airflow is used to orchestrate the complete ML workflow.

## DAG Name

```text
automated_ml_training_workflow
```

## DAG Workflow

```text
                  Airflow Scheduler
                         │
                    @daily schedule
                         ↓
                ┌─────────────────┐
                │ preprocess_data │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │   train_model   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ evaluate_model  │
                └────────┬────────┘
                         ↓
                 Model + Report
```

The task dependencies ensure that each stage runs only after the previous stage completes successfully.

---

## Airflow Tasks

### 1. `preprocess_data`

Executes:

```text
data_preprocessing.ipynb
```

This task prepares the data required for model training.

### 2. `train_model`

Executes:

```text
model_training.ipynb
```

This task trains the Logistic Regression model and generates:

```text
models/trained_model.pkl
```

### 3. `evaluate_model`

Executes:

```text
model_evaluation.ipynb
```

This task evaluates the trained model and generates:

```text
output/training_report.txt
```

---

## Automation

The DAG uses:

```python
schedule="@daily"
```

Therefore, the workflow is scheduled to execute automatically every day.

The DAG uses:

```python
catchup=False
```

to prevent Airflow from executing previously missed scheduled runs.

The DAG is configured to run:

```text
preprocess_data
        ↓
train_model
        ↓
evaluate_model
```

automatically without requiring a manual trigger.

---

## Project Structure

```text
Assignment-4-Airflow/

│
├── dags/
│   └── ml_training_workflow.py
│
├── data/
│   ├── dataset.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
│
├── models/
│   └── trained_model.pkl
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── output/
│   └── training_report.txt
│
└── README.md
```

---

# Model Performance

The final Logistic Regression model achieved:

| Metric           |              Result |
| ---------------- | ------------------: |
| Model            | Logistic Regression |
| Training samples |                 455 |
| Testing samples  |                 114 |
| Accuracy         |          **98.25%** |
| Precision        |                ~98% |
| Recall           |                ~98% |
| F1-score         |                ~98% |

### Classification Report

```text
              precision    recall  f1-score   support

           0       0.98      0.98      0.98        42
           1       0.99      0.99      0.99        72

    accuracy                           0.98       114
   macro avg       0.98      0.98      0.98       114
weighted avg       0.98      0.98      0.98       114
```

---

## Output

The automated pipeline generates:

### Trained Model

```text
models/trained_model.pkl
```

### Evaluation Report

```text
output/training_report.txt
```

The final report contains the model name, accuracy, precision, recall, F1-score, and classification report.

---

# Running the Project

### 1. Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/Nitish-0710/mlops-assignments
cd Assignment-4-Airflow
```

### 2. Activate the Airflow Virtual Environment

Activate the Python virtual environment containing Apache Airflow and the required dependencies.

For example, if the virtual environment is located at `~/airflow_venv`:

```bash
source ~/airflow_venv/bin/activate
```

### 3. Configure the Airflow DAG Folder

Set the DAG folder relative to the current project directory:

```bash
export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags"
```

This avoids using a machine-specific absolute path.

### 4. Start Airflow

```bash
airflow standalone
```

### 5. Open the Airflow Web UI

Open:

```text
http://localhost:8080
```

### 6. Enable the DAG

Find:

```text
automated_ml_training_workflow
```

and make sure the DAG is **unpaused**.

Once enabled, Airflow's scheduler automatically executes the workflow according to its daily schedule.

---

## Result

The automated ML training pipeline was successfully implemented using Apache Airflow.

The workflow automatically executes:

```text
Data Preprocessing
        ↓
Model Training
        ↓
Model Evaluation
```

All tasks execute in the correct order, and the trained model and evaluation report are generated successfully.

---

## Conclusion

This assignment demonstrates the use of **Apache Airflow for Machine Learning workflow orchestration and automation**.

The project shows how individual Machine Learning notebooks can be connected into a scheduled pipeline where Airflow manages task dependencies, execution, scheduling, logging, and monitoring.

The implementation provides a basic MLOps workflow that reduces manual intervention and establishes a foundation for more advanced automated ML pipelines.

```

