# Assignment 5 – Practice: CI/CD for Student Placement Prediction

## 📌 Objective

The objective of this practice assignment is to understand the basic workflow of **Continuous Integration (CI) and Continuous Deployment (CD)** for a Machine Learning application.

A Student Placement Prediction model is developed using Python and scikit-learn. **GitHub Actions** is used to automatically validate the dataset, train the model, run automated tests, perform code-quality checks, and execute a deployment stage when all CI checks pass.

---

## 🎯 Problem Statement

Develop a Machine Learning model that predicts whether a student will be placed based on academic and skill-related features.

The project demonstrates how CI/CD can be applied to a Machine Learning workflow so that changes pushed to GitHub are automatically validated and tested.

The CI pipeline must ensure that:

- The dataset is valid.
- The model can be trained successfully.
- Model accuracy satisfies the required threshold.
- The trained model file is generated.
- Automated tests pass.
- Predictions are valid.
- Source code satisfies the configured code-quality checks.

The CD stage is executed only after the CI stage succeeds.

---

## 📊 Dataset

The project uses a small custom Student Placement dataset.

### Features

| Feature | Description |
|---------|-------------|
| CGPA | Student's CGPA |
| Attendance | Attendance percentage |
| CodingScore | Coding assessment score |
| Projects | Number of completed projects |
| Internship | Internship status (`1 = Yes`, `0 = No`) |
| Placement | Target variable (`1 = Placed`, `0 = Not Placed`) |

The dataset is stored at:

```text
data/student_placement.csv
````

---

## 🤖 Machine Learning Model

A **Logistic Regression** classifier from scikit-learn is used for student placement prediction.

The dataset is divided into training and testing sets using:

```text
test_size = 0.25
random_state = 42
stratify = y
```

The model is trained using:

```python
LogisticRegression(max_iter=1000)
```

### Model Performance

The model achieved:

```text
Test Accuracy: 1.0
```

The CI pipeline requires:

```text
Accuracy >= 80%
```

The achieved accuracy therefore satisfies the configured quality gate.

> Note: The dataset contains only 12 records. Therefore, the 100% test accuracy should be interpreted as satisfying the practical assignment's quality threshold rather than as evidence of production-level model performance.

---

## 📂 Project Structure

```text
Assignment-5-CI-CD-Practice/
│
├── data/
│   └── student_placement.csv
│
├── placement_model.pkl
├── predict.py
├── requirements.txt
├── test_model.py
└── train.py
```

The GitHub Actions workflow is maintained at the repository level:

```text
.github/
└── workflows/
    └── ml-ci-cd-practice.yml
```

This is required because GitHub Actions discovers workflows from the repository-level `.github/workflows/` directory.

---

## ⚙️ Requirements

The Assignment 5 dependencies are defined in:

```text
requirements.txt
```

They include:

```text
pandas
scikit-learn
pytest
flake8
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project Locally

### 1. Train the Model

From the Assignment 5 directory:

```bash
python train.py
```

Expected output:

```text
Model Training Completed
Test Accuracy: 1.0
Accuracy requirement satisfied: >= 80%
Model saved as placement_model.pkl
```

---

### 2. Run the Prediction Program

```bash
python predict.py
```

The program accepts:

* CGPA
* Attendance
* Coding Score
* Number of Projects
* Internship status

Example:

```text
Enter CGPA: 8.5
Enter Attendance (%): 92
Enter Coding Score: 85
Enter Number of Projects: 3
Enter Internship (1 = Yes, 0 = No): 1

Predicted Result: PLACED
```

---

## 🧪 Automated Testing

Pytest is used for automated model validation.

Run:

```bash
python -m pytest
```

The project contains five automated tests covering:

* Model file existence
* Model loading
* Prediction validity
* Placed student prediction
* Not-placed student prediction

Final local test result:

```text
5 passed
```

---

## 🔍 Code Quality

Flake8 is used to perform a basic code-quality check.

Run:

```bash
python -m flake8 train.py predict.py test_model.py
```

The final source code passes the configured Flake8 checks without errors.

---

# 🔄 CI/CD Pipeline

GitHub Actions is used to automate the CI/CD workflow.

The workflow file is:

```text
.github/workflows/ml-ci-cd-practice.yml
```

The workflow is triggered on:

* Pushes to the `main` branch
* Pull requests targeting the `main` branch

---

## 🔧 Continuous Integration (CI)

The CI job performs the following steps:

```text
Checkout Code
      ↓
Setup Python
      ↓
Install Dependencies
      ↓
Validate Dataset
      ↓
Train Model
      ↓
Verify Model File
      ↓
Run Automated Tests
      ↓
Check Prediction
      ↓
Code Quality Check
```

### Dataset Validation

The pipeline checks that:

* Required columns exist.
* The dataset is not empty.
* Required fields do not contain missing values.

### Model Quality Gate

During training, the model accuracy is checked against:

```text
Accuracy >= 80%
```

If the requirement is not satisfied, the CI pipeline fails.

### Model Artifact Check

The pipeline verifies that:

```text
placement_model.pkl
```

is generated successfully.

### Automated Tests

The pipeline executes:

```bash
python -m pytest
```

### Prediction Check

The trained model is loaded and tested with a sample student record.

### Code Quality Check

The pipeline executes:

```bash
python -m flake8 train.py predict.py test_model.py
```

---

# 🚀 Continuous Deployment (CD)

The CD job represents the deployment stage of the ML application.

It is configured with:

```yaml
needs: test
```

Therefore, the CD job runs only when the complete CI job succeeds.

The current deployment stage is a **simulated deployment** used for the practice assignment.

---

# ❌ CI Failure Demonstration

To verify that the CI/CD pipeline correctly handles failures, an intentional error was introduced into the automated tests.

The placed-student test was temporarily changed from:

```python
assert prediction == 1
```

to:

```python
assert prediction == 0
```

The change was committed and pushed to GitHub.

GitHub Actions then produced:

```text
❌ CI - Validate, Train and Test Model
⏭️ CD - Deploy Application
```

The CI pipeline failed because the automated test produced a non-zero exit code.

The CD stage did not run because it depends on the successful completion of the CI job.

This demonstrated the quality-gate behavior:

```text
Code Push
    ↓
CI
    ↓
Test Failure
    ↓
❌ CI Failed
    ↓
⏭️ CD Blocked
```

---

# ✅ Pipeline Recovery

After demonstrating the failure, the test was restored to:

```python
assert prediction == 1
```

The fix was committed and pushed to GitHub.

The pipeline then completed successfully:

```text
✅ CI - Validate, Train and Test Model
        ↓
✅ CD - Deploy Application
```

This demonstrated the complete CI/CD lifecycle:

```text
Successful Code
      ↓
      CI
      ↓
   Testing
      ↓
    Deploy
```

and:

```text
Incorrect Code
      ↓
      CI
      ↓
   Test Failure
      ↓
  Deployment Blocked
      ↓
     Fix
      ↓
      CI
      ↓
    Deploy
```

---

# 📈 Final Results

| Check                          | Result         |
| ------------------------------ | -------------- |
| Dataset validation             | ✅ Passed       |
| Model training                 | ✅ Passed       |
| Test accuracy                  | **100%**       |
| Accuracy requirement           | ✅ >= 80%       |
| Model file generation          | ✅ Passed       |
| Automated tests                | ✅ 5/5 Passed   |
| Prediction validation          | ✅ Passed       |
| Flake8 code-quality check      | ✅ Passed       |
| CI pipeline                    | ✅ Passed       |
| CD pipeline                    | ✅ Passed       |
| CI failure handling            | ✅ Demonstrated |
| Deployment blocking on failure | ✅ Demonstrated |
| Pipeline recovery              | ✅ Demonstrated |

---

# 🎓 Learning Outcomes

This assignment demonstrates practical understanding of:

* Continuous Integration
* Continuous Deployment
* GitHub Actions
* Automated Machine Learning testing
* Dataset validation
* Model quality gates
* Model artifact validation
* Automated prediction testing
* Code-quality checking
* CI failure handling
* Deployment dependency management
* Reproducible ML workflows

---

# 📌 Conclusion

This practice assignment demonstrates how a Machine Learning project can be integrated into a CI/CD workflow.

Every push to the `main` branch can trigger automated validation, model training, testing, prediction checks, and code-quality checks. Deployment is allowed only after the CI stage successfully completes.

The project also demonstrates failure handling by intentionally introducing a failing test, verifying that deployment is blocked, and subsequently restoring the test to achieve a successful CI/CD run.