# Practice Assignment - Dataset Versioning using DVC

## 📌 Objective

The objective of this practice assignment is to understand the basic workflow of **Dataset Versioning using Data Version Control (DVC)**.

A custom **Student Dataset** is created and maintained through multiple versions. The dataset is tracked using **DVC** while Git is used to manage the project source code and version history.


## 🛠️ Technologies Used

- Python 3
- Jupyter Notebook
- Pandas
- Git
- DVC (Data Version Control)

## 📂 Project Structure

```text
Assignment-1-DVC-Practice/
│
├── data/
│   ├── students.csv
│   └── students.csv.dvc
│
├── notebooks/
│   └── Assignment1.ipynb
│
└── README.md
```

## 📊 Dataset Description

The project uses a custom **Student Dataset**.

### Dataset Columns

| Column | Description |
|---------|-------------|
| Student_ID | Unique identifier for each student |
| Name | Student name |
| Age | Age of the student |
| Branch | Academic branch |
| CGPA | Current CGPA |

# 📌 Dataset Version History

## ✅ Version 1 – Initial Student Dataset

Created the initial dataset containing **10 student records**.

### Columns

- Student_ID
- Name
- Age
- Branch
- CGPA

### DVC Commands

```bash
dvc add Assignment-1-DVC-Practice/data/students.csv

git add .

git commit -m "Version 1: Initial student dataset"
```

## ✅ Version 2 – Added New Student Records

Added **three new student records** to the existing dataset.

### Changes

- Increased dataset size from **10** to **13** records.
- Saved the updated dataset.
- Tracked the updated dataset using DVC.

### DVC Commands

```bash
dvc add Assignment-1-DVC-Practice/data/students.csv

git add .

git commit -m "Version 2: Added three new student records"
```

# 🔄 DVC Workflow

The following workflow was followed for every dataset version.

```text
Create / Modify Dataset
        │
        ▼
Save Dataset as CSV
        │
        ▼
Track Dataset using DVC
        │
        ▼
dvc add students.csv
        │
        ▼
git add .
        │
        ▼
git commit
```

# ♻️ Restoring Previous Dataset Versions

View Git commit history:

```bash
git log --oneline
```

Switch to an older version:

```bash
git checkout <commit-id>
```

Restore the corresponding dataset version:

```bash
dvc checkout
```

Return to the latest version:

```bash
git checkout main
dvc checkout
```


# 📈 Dataset Evolution

| Version | Changes |
|---------|----------|
| Version 1 | Initial student dataset containing 10 records |
| Version 2 | Added three new student records (13 total records) |

# 🚀 How to Run

## Prerequisites

Make sure the following are installed:

- Python 3.x
- Git
- DVC
- Jupyter Notebook or VS Code

## 1. Clone the Repository

If the practice assignment is part of the main `mlops-assignments` repository:

```bash
git clone https://github.com/Nitish-0710/mlops-assignments.git

# Navigate to the root folder
cd mlops-assignments
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

Install the required packages:

```bash
pip install -r requirements.txt
```

## 5. Verify DVC Installation

Check that DVC is installed correctly:

```bash
dvc version
```

## 6. Navigate to the Practice Assignment

From the repository root:

```bash
cd Assignment-1-DVC-Practice
```

The assignment contains:

```text
Assignment-1-DVC-Practice/
│
├── data/
│   ├── students.csv
│   └── students.csv.dvc
│
├── notebooks/
│   └── Assignment1.ipynb
│
└── README.md
```

## 7. Open the Notebook

Open the following notebook using Jupyter Notebook or VS Code:

```text
Assignment-1-DVC-Practice/
└── notebooks/
    └── Assignment1.ipynb
```

## 8. Run the Notebook

Run all cells in `Assignment1.ipynb` sequentially.

The notebook demonstrates the following workflow:

```text
Create Initial Student Dataset
    ↓
Version 1
    ↓
Add Three New Students
    ↓
Version 2
    ↓
Save Dataset
    ↓
Verify Dataset
```

The dataset evolves from:

```text
Version 1 → 10 students
Version 2 → 13 students
```

# 🎯 Learning Outcomes

After completing this practice assignment, the following concepts were understood:

- Creating custom datasets
- Saving datasets as CSV files
- Tracking datasets using DVC
- Managing datasets with Git
- Creating multiple dataset versions
- Restoring previous dataset versions
- Understanding the relationship between Git and DVC
- Understanding the basic DVC workflow

# 📌 Conclusion

This practice assignment successfully demonstrates the basic workflow of **Dataset Versioning using DVC**.

A custom student dataset was created and evolved through two versions. The initial dataset contained **10 student records**, and a second version was created by adding **three new student records**, increasing the dataset size to **13 records**.

Each version was tracked using **Data Version Control (DVC)** and committed using **Git**, demonstrating how datasets can be versioned and restored efficiently in Machine Learning and MLOps projects.