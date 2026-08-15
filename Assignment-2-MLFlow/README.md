# Assignment 2 – ML Experiment Tracking using MLflow

## Objective

The objective of this assignment is to understand how to track machine learning experiments using **MLflow**.

In this assignment, the **Iris dataset** is used with a Logistic Regression model. Different hyperparameter values are tested and the experiments are tracked using MLflow.

## Dataset

The **Iris dataset** is used for this assignment.

It contains 150 samples of iris flowers belonging to three classes:

* Setosa
* Versicolor
* Virginica

The dataset contains four features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

## Tools and Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* MLflow
* Matplotlib
* Jupyter Notebook

## Steps Performed

1. Loaded the Iris dataset.
2. Explored the dataset and checked for missing values.
3. Separated features and target variable.
4. Split the dataset into training and testing sets using an 80:20 ratio.
5. Applied feature scaling using `StandardScaler`.
6. Created an MLflow experiment named `Assignment 2: Iris Classification Experiments`.
7. Registered the Iris dataset with MLflow.
8. Trained a baseline Logistic Regression model.
9. Tested different values of the `C` parameter:
   * `0.1`
   * `1.0`
   * `10.0`
10. Tested different values of `max_iter`:
   * `50`
   * `100`
   * `200`
11. Logged the dataset, model parameters, accuracy, and trained models using MLflow.
12. Compared the experiment runs.
13. Visualized the experiment results.
14. Selected the best-performing experiment.
15. Evaluated the final model.
16. Viewed the experiment runs using the MLflow web interface.

## Experiment Results

### Effect of C

| C Value | Test Accuracy |
| ------: | ------------: |
|     0.1 |        86.67% |
|     1.0 |        93.33% |
|    10.0 |       100.00% |

### Effect of max_iter

| max_iter | Test Accuracy |
| -------: | ------------: |
|       50 |        93.33% |
|      100 |        93.33% |
|      200 |        93.33% |

## Best Model

The best-performing experiment used:

* **Model:** Logistic Regression
* **C:** 10.0
* **max_iter:** 200
* **Test Accuracy:** 100%

The model correctly classified all 30 samples in the test set.

## MLflow Tracking

MLflow was used to track:

* Experiment runs
* Dataset information
* Model parameters
* Accuracy metrics
* Trained model artifacts

The MLflow UI was opened locally to view and compare the experiment runs.

## How to Run

### Prerequisites

Make sure the following are installed:

- Python 3.x
- Git
- Jupyter Notebook or VS Code

The project also contains a `requirements.txt` file with the required Python packages.

### 1. Clone the Repository

Clone the repository:

```bash
git clone https://github.com/Nitish-0710/mlops-assignments

# Navigate to root folder 
cd mlops-assignments
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows

```cmd
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

The required Python packages are provided in the project's `requirements.txt` file.

From the mlops-assignments, run:

```bash
pip install -r requirements.txt
```

### 5. Start the MLflow Tracking Server

From the MLOps project root, start the MLflow tracking server:

```bash
mlflow server --port 5000
```

The MLflow UI will be available at:

```text
http://127.0.0.1:5000
```

Keep the MLflow server running while executing the notebook.

## 6. Open the Notebook

Open the following notebook:

```text
Assignment-2-MLFlow/
└── notebooks/
    └── Assignment2.ipynb
```

Open it using Jupyter Notebook or VS Code.

## 7. Run the Notebook

Run all cells in `Assignment2.ipynb` sequentially.

The notebook performs:

```text
Iris Dataset Loading
        ↓
Dataset Exploration
        ↓
Feature and Target Separation
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
MLflow Dataset Registration
        ↓
Baseline Model
        ↓
C Hyperparameter Experiments
        ↓
max_iter Experiments
        ↓
MLflow Run Comparison
        ↓
Result Visualization
        ↓
Best Model Selection
        ↓
Final Model Evaluation
```

## 8. View Results in MLflow

After running the notebook, open:

```text
http://127.0.0.1:5000
```

Navigate to:

```text
Assignment 2: Iris Classification Experiments
```

The experiment contains the tracked:

* Dataset
* Model parameters
* Accuracy metrics
* Model artifacts
* Experiment runs

## 9. Stop the MLflow Server

After completing the assignment, return to the terminal where the MLflow server is running and press:

```text
Ctrl + C
```

This stops the MLflow tracking server.

---

## Files

```text
Assignment-2-MLFlow/
│
├── README.md
│
└── notebooks/
    └── Assignment2.ipynb
```

--- 
## Conclusion

This assignment demonstrated how MLflow can be used to track machine learning experiments. Different hyperparameter values were tested and their results were recorded and compared.

The best-performing Logistic Regression model achieved **100% test accuracy** with `C = 10.0`.

MLflow makes it easier to organize, track, and compare machine learning experiments.

---