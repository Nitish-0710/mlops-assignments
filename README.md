# MLOps Assignments

A collection of **Machine Learning Operations (MLOps)** assignments completed as part of university coursework. This repository demonstrates the practical implementation of MLOps concepts, tools, and workflows using Python, Git, DVC, MLflow, Apache Airflow, GitHub Actions, and other supporting technologies.

---

## 📌 Repository Objectives

The primary objectives of this repository are to:

- Learn and implement core MLOps concepts.
- Understand data and model versioning.
- Build reproducible Machine Learning workflows.
- Gain hands-on experience with industry-standard MLOps tools.
- Implement automated testing and CI/CD workflows.
- Maintain well-documented assignments with proper version control.

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Git
- GitHub
- DVC (Data Version Control)
- Pandas
- NumPy
- MLflow
- Apache Airflow
- Scikit-learn
- Pytest
- Flake8
- GitHub Actions

Additional technologies such as Docker, FastAPI, Kubernetes, Kubeflow, and model monitoring may be explored in future assignments and projects.

---

# 📂 Repository Structure

```text
MLOPS/
│
├── .github/
│   └── workflows/
│       └── ml-ci-cd-practice.yml
│
├── Assignment-1-DVC-Practice/
│
├── Assignment-1-Employee/
│
├── Assignment-2-MLFlow/
│
├── Assignment-3-Feature-Engineering-Pipeline/
│
├── Assignment-4-Airflow-Practice/
│
├── Assignment-4-Airflow/
│
├── Assignment-5-CI-CD-Practice/
│   ├── data/
│   ├── placement_model.pkl
│   ├── predict.py
│   ├── requirements.txt
│   ├── test_model.py
│   └── train.py
│
├── .gitignore
├── .dvcignore
├── README.md
└── requirements.txt
````

---

# 📚 Assignments

| Assignment              | Topic                                               | Status      |
| ----------------------- | --------------------------------------------------- | ----------- |
| Assignment 1 (Practice) | Dataset Versioning using DVC                        | ✅ Completed |
| Assignment 1            | Dataset Versioning using DVC                        | ✅ Completed |
| Assignment 2            | Experiment Tracking using MLflow                    | ✅ Completed |
| Assignment 3            | Feature Engineering Pipeline                        | ✅ Completed |
| Assignment 4 (Practice) | Airflow Workflow                                    | ✅ Completed |
| Assignment 4            | Automated ML Training Pipeline using Apache Airflow | ✅ Completed |
| Assignment 5            | CI/CD for Student Placement Prediction              | ✅ Completed |

---

# 🎯 Assignment Topics

This repository covers practical implementations of:

* Version Control using Git
* Dataset Versioning using DVC
* Experiment Tracking using MLflow
* Feature Engineering
* Machine Learning Pipelines
* Workflow Orchestration using Apache Airflow
* Automated Testing using Pytest
* Code Quality Checking using Flake8
* Continuous Integration & Continuous Deployment (CI/CD)
* Model Training and Evaluation
* Model Artifact Management
* Reproducibility in Machine Learning

Future assignments and projects may extend these concepts to model deployment, containerization, monitoring, and scalable MLOps systems.

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/Nitish-0710/mlops-assignments.git
```

---

## 2. Navigate to the Repository

```bash
cd mlops-assignments
```

---

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 5. Install Required Packages

```bash
pip install -r requirements.txt
```

Individual assignments may contain their own `requirements.txt` files when assignment-specific dependencies are required.

---

# 📖 Assignment Structure

Each assignment is organized according to its requirements and may contain different files such as:

```text
Assignment-X/
│
├── data/
├── notebooks/          # If required
├── scripts/
├── models/
├── tests/
├── README.md
└── additional files
```

Assignment-specific documentation may include:

* Objective
* Dataset
* Implementation
* Configuration
* Results
* Testing
* MLOps workflow
* Assignment-specific documentation

---

# 🔄 MLOps Learning Progression

The assignments progressively cover different stages of an MLOps workflow:

```text
Data Versioning
       ↓
Experiment Tracking
       ↓
Feature Engineering & ML Pipelines
       ↓
Workflow Orchestration
       ↓
CI/CD Automation
```

This progression provides hands-on experience with managing machine learning assets, experiments, workflows, and automated software delivery.

---

# 📈 Learning Outcomes

Through these assignments, the following concepts are practiced:

* Version control using Git and GitHub
* Dataset versioning using DVC
* Experiment tracking using MLflow
* Feature engineering and pipeline development
* Workflow orchestration using Apache Airflow
* Automated testing using Pytest
* Code quality checking using Flake8
* Continuous Integration and Continuous Deployment
* Model training and evaluation
* Managing Machine Learning artifacts
* Reproducible Machine Learning workflows
* Maintaining organized technical documentation

---

# 🚀 Future Enhancements

Future work may include:

* Docker for ML Applications
* FastAPI Model Deployment
* Kubernetes
* Kubeflow
* Model Monitoring
* End-to-End MLOps Projects
* Cloud-based ML deployment

---

# 👨‍💻 Author

**Nitish Sahu**

B.Tech Computer Science & Engineering (Artificial Intelligence)

Vishwakarma Institute of Technology (VIT), Pune

---

# 📄 License

This repository is maintained for **educational and learning purposes** as part of university MLOps coursework.