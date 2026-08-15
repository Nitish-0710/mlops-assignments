# Assignment 3 – Feature Engineering and ML Pipeline

## Objective

To understand and implement feature engineering and machine learning pipelines for a classification problem, while tracking experiments and models using MLflow.

The assignment uses the **Adult Income Dataset** to predict whether an individual's income is `<=50K` or `>50K`.

The implementation demonstrates:

- Feature engineering
- Numerical and categorical preprocessing
- Custom Scikit-learn transformers
- ML pipelines
- Hyperparameter experimentation
- MLflow experiment tracking
- MLflow dataset tracking
- MLflow model logging and loading
- Model reproducibility verification
- Evaluation artifact logging
- DVC-based dataset tracking

---

## Dataset

**Dataset:** Adult Income Dataset

### Dataset Shape

```text
48,842 rows × 15 columns
```

### Target Column

```text
income
```

### Target Classes

```text
<=50K
>50K
```

### Input Features

The dataset contains 14 input features.

#### Numerical Features

```text
age
fnlwgt
educational-num
capital-gain
capital-loss
hours-per-week
```

#### Categorical Features

```text
workclass
education
marital-status
occupation
relationship
race
gender
native-country
```

### Unknown Values

The dataset contains `?` values in:

```text
workclass
occupation
native-country
```

These are handled during preprocessing.

---

## Train-Test Split

The dataset is divided into training and testing sets using:

```text
Training samples : 39,073 (80%)
Testing samples  : 9,769 (20%)
```

Stratified splitting is used to maintain the target-class distribution.

---

# Feature Engineering

Three new features were created.

### 1. capital-net

Calculated as:

```text
capital-net = capital-gain - capital-loss
```

### 2. age-group

Age is converted into categorical groups:

```text
Young Adult
Adult
Middle-aged
Senior
```

### 3. work-hours-category

`hours-per-week` is converted into categorical work-hour groups such as:

```text
Part-time
Full-time
```

The engineered dataset contains:

```text
Original features    : 14
Engineered features  : 17
```

---

# Preprocessing

Separate preprocessing pipelines are used for numerical and categorical features.

## Numerical Features

The numerical pipeline applies:

```text
Median Imputation
        ↓
StandardScaler
```

## Categorical Features

The categorical pipeline applies:

```text
Most-Frequent Imputation
        ↓
OneHotEncoder(handle_unknown="ignore")
```

A `ColumnTransformer` combines both preprocessing pipelines.

---

# Machine Learning Models

Two classification algorithms are evaluated.

## Logistic Regression

Hyperparameter configurations tested:

```text
C = 0.1
C = 1.0
C = 10.0
```

## Random Forest

Configurations tested:

```text
50 trees
100 trees
200 trees
```

The selected configurations used for the complete pipelines are:

```text
Logistic Regression : C = 1.0
Random Forest       : 200 trees
```

---

# Model Performance

The final pipeline models produced the following results.

| Model               | Accuracy | Precision | Recall |   F1-Score |    ROC-AUC |
| ------------------- | -------: | --------: | -----: | ---------: | ---------: |
| Logistic Regression |   0.8552 |    0.7438 | 0.6022 |     0.6656 | **0.9096** |
| Random Forest       |   0.8576 |    0.7369 | 0.6300 | **0.6793** |     0.9059 |

## Final Selected Model

The final model was selected using **ROC-AUC as the primary metric**, with F1-score and recall considered as supporting metrics.

```text
Model         : Logistic Regression
Configuration : C = 1.0
ROC-AUC       : 0.9096
F1-Score      : 0.6656
Recall        : 0.6022
Accuracy      : 0.8552
```

---

# MLflow Tracking

MLflow is used for experiment tracking and model management.

### MLflow Experiment

```text
Assignment 3: Feature Engineering and Pipeline
```

MLflow tracks:

* Dataset information
* Feature engineering configuration
* Model parameters
* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Evaluation artifacts
* Final pipeline models

The final Logistic Regression and Random Forest pipelines are logged as MLflow models.

---

# MLflow Pipeline Verification

The assignment verifies that the complete pipelines produce the same results as the manually implemented preprocessing and models.

The following checks were performed:

```text
FeatureEngineer verification       : PASSED
LR pipeline equivalence            : PASSED
RF pipeline equivalence            : PASSED
LR MLflow reproducibility          : PASSED
RF MLflow reproducibility          : PASSED
```

Both predictions and prediction probabilities were compared.

---

# MLflow Model Reproducibility

The logged pipeline models were loaded back from MLflow and evaluated again.

The following were verified:

```text
Original vs MLflow-loaded predictions
Original vs MLflow-loaded probabilities
```

Results matched for both:

```text
Logistic Regression : PASSED
Random Forest       : PASSED
```

This verifies that the complete preprocessing and feature-engineering logic is preserved inside the logged pipeline.

---

# Evaluation Artifacts

Evaluation artifacts were logged for both final pipeline models.

Artifacts include:

* Classification report
* Confusion matrix

The final models therefore contain both the trained pipeline and its evaluation information in MLflow.

---

# DVC

DVC is used to track the dataset version for reproducibility.

The dataset is tracked using DVC rather than committing the dataset directly to Git.

DVC-related files are included in the repository so that the dataset version can be reproduced.

---

# Project Structure

```text
Assignment-3-Feature-Engineering-Pipeline/
│
├── README.md
│
├── data/
│   ├── .gitignore
│   ├── adult.csv
│   └── adult.csv.dvc
│
└── notebooks/
    └── Assignment3.ipynb
```
The exact files may vary depending on the local setup.

---

# Tools and Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* MLflow
* DVC
* Jupyter Notebook

---

# How to Run

## Prerequisites

Make sure the following is/are installed:

- Python 3.x

## 1. Clone the Repository

```bash
git clone https://github.com/Nitish-0710/mlops-assignments
cd MLOPS/Assignment-3-Feature-Engineering-Pipeline
```

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

## 3. Activate the Virtual Environment

### Windows

```cmd
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 5. Restore the Dataset Using DVC

The Adult Income dataset is tracked using DVC.

Run:

```bash
dvc pull
```

This restores:

```text
data/adult.csv
```

from the configured DVC storage.

## 6. Start the MLflow Tracking Server

From the MLOps project root, start the MLflow server:

```bash
mlflow server --port 5000
```

The MLflow UI will be available at:

```text
http://127.0.0.1:5000
```

Keep the MLflow server running while executing the notebook.

## 7. Open the Notebook

Open the following notebook:

```text
Assignment-3-Feature-Engineering-Pipeline/
└── notebooks/
    └── Assignment3.ipynb
```

Open it using Jupyter Notebook or VS Code.

## 8. Run the Notebook

Run all cells in `Assignment3.ipynb` sequentially.

The notebook performs:

```text
Dataset Loading
      ↓
Train-Test Split
      ↓
Feature Engineering
      ↓
Feature Preprocessing
      ↓
Model Experiments
      ↓
Pipeline Creation
      ↓
Pipeline Verification
      ↓
MLflow Model Logging
      ↓
MLflow Model Loading
      ↓
Reproducibility Verification
      ↓
Evaluation Artifact Logging
      ↓
Final Model Comparison
```

## 9. View Results in MLflow

After running the notebook, open:

```text
http://127.0.0.1:5000
```

Navigate to:

```text
Assignment 3: Feature Engineering and Pipeline
```

The experiment contains the tracked model runs, metrics, parameters, models, and evaluation artifacts.

--- 

# Conclusion

This assignment demonstrates how feature engineering can be integrated into a complete machine learning workflow using Scikit-learn pipelines.

The Logistic Regression pipeline achieved a ROC-AUC of **0.9096**, while the Random Forest pipeline achieved **0.9059**.

The assignment also demonstrates MLflow-based experiment tracking, model logging, model loading, evaluation artifact tracking, and reproducibility verification.

The final implementation ensures that feature engineering and preprocessing are included within the machine learning pipeline, reducing the risk of inconsistent transformations during model deployment or reuse.
