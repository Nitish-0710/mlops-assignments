# Assignment 1 - Dataset Versioning using DVC

## 📌 Objective

The objective of this assignment is to implement **Dataset Versioning** using **Data Version Control (DVC)**. A custom employee salary dataset is created and modified through multiple versions. Each version is tracked using DVC and committed using Git, allowing previous dataset versions to be restored whenever required.


## 🛠️ Technologies Used

- Python 3
- Jupyter Notebook
- Pandas
- Git
- DVC (Data Version Control)


## 📂 Project Structure

```text
Assignment-1-Employee/
│
├── data/
│   ├── employees.csv
│   └── employees.csv.dvc
│
├── notebooks/
│   └── Assignment1.ipynb
│
└── README.md
```


## 📊 Dataset Description

The project uses a custom **Employee Salary Dataset**.

### Initial Columns

| Column | Description |
|----------|-------------|
| Employee_ID | Unique employee identifier |
| Employee_Name | Name of the employee |
| Department | Employee department |
| Salary | Monthly salary |

Additional columns are introduced in later versions to demonstrate dataset schema evolution.


# 📌 Dataset Version History

## ✅ Version 1 – Initial Dataset

Created the initial employee salary dataset containing:

- Employee_ID
- Employee_Name
- Department
- Salary

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 1: Initial employee salary dataset"
```


## ✅ Version 2 – Salary Increment

Updated every employee's salary by **10%**.

### Changes

- Increased salary values.
- Saved updated dataset.
- Tracked using DVC.

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 2: Increased all employee salaries by 10%"
```


## ✅ Version 3 – Added Years of Experience

Added a new column:

- Years_of_Experience

### Changes

- Dataset schema updated.
- New employee attribute added.

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 3: Added Years_of_Experience column"
```


## ✅ Version 4 – Added Performance Rating

Added another column:

- Performance_Rating

Possible values:

- Excellent
- Very Good
- Good
- Average

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 4: Added Performance_Rating column"
```

## ✅ Version 5 – Added New Employees

Added three new employee records.

### Changes

- Increased dataset size.
- Preserved existing schema.

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 5: Added new employee records"
```


## ✅ Version 6 – Updated Department Names

Modified department names to reflect organizational restructuring.

### Department Mapping

| Old Name | New Name |
|-----------|----------|
| HR | Human Resources |
| IT | Engineering |
| Finance | Accounts & Finance |
| Marketing | Business Development |
| Sales | Sales & Marketing |
| Operations | Business Operations |

### DVC Command

```bash
dvc add Assignment-1-Employee/data/employees.csv
git add .
git commit -m "Version 6: Updated department names"
```


# 🔄 DVC Workflow

The following workflow was followed for each dataset version:

```text
Create / Modify Dataset
        │
        ▼
Save CSV File
        │
        ▼
dvc add employees.csv
        │
        ▼
git add .
        │
        ▼
git commit
```


# ♻️ Restoring Previous Dataset Versions

View commit history:

```bash
git log --oneline
```

Switch to an older version:

```bash
git checkout <commit-id>
```

Restore the corresponding dataset:

```bash
dvc checkout
```

Return to the latest version:

```bash
git checkout main
dvc checkout
```


# 📈 Summary of Dataset Evolution

| Version | Changes |
|---------|----------|
| Version 1 | Initial employee salary dataset |
| Version 2 | Increased employee salaries by 10% |
| Version 3 | Added Years_of_Experience column |
| Version 4 | Added Performance_Rating column |
| Version 5 | Added three new employee records |
| Version 6 | Updated department names |


# 🚀 How to Run

## Prerequisites

Make sure the following are installed:

- Python 3.x
- Git
- DVC
- Jupyter Notebook or VS Code


## 1. Clone the Repository

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

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main packages required for this assignment are:

```text
pandas
jupyter
dvc
```


## 5. Verify DVC

Check that DVC is installed correctly:

```bash
dvc version
```


## 6. Navigate to Assignment 1

Navigate to the assignment directory:

```bash
cd Assignment-1-Employee
```

The assignment contains:

```text
Assignment-1-Employee/
│
├── data/
│   ├── employees.csv
│   └── employees.csv.dvc
│
├── notebooks/
│   └── Assignment1.ipynb
│
└── README.md
```


## 7. Open the Notebook

Open the following notebook using Jupyter Notebook or VS Code:

```text
Assignment-1-Employee/
└── notebooks/
    └── Assignment1.ipynb
```

For Jupyter Notebook, run:

```bash
jupyter notebook
```

## 8. Run the Notebook

Run all cells in `Assignment1.ipynb` sequentially.

The notebook demonstrates the following workflow:

```text
Create Initial Dataset
   ↓
Version 1
   ↓
Increase Salaries by 10%
   ↓
Version 2
   ↓
Add Years of Experience
   ↓
Version 3
   ↓
Add Performance Rating
   ↓
Version 4
   ↓
Add New Employees
   ↓
Version 5
   ↓
Update Department Names
   ↓
Version 6
```

Each version is saved as `employees.csv` and tracked using DVC.


# ✅ Learning Outcomes

After completing this assignment, the following concepts were understood:

- Creating custom datasets
- Versioning datasets using DVC
- Tracking datasets with Git
- Managing multiple dataset versions
- Handling dataset value modifications
- Handling dataset schema changes
- Adding new records to an existing dataset
- Restoring previous dataset versions
- Understanding the relationship between Git and DVC
- Maintaining reproducible datasets for Machine Learning projects


# 📌 Conclusion

This assignment successfully demonstrates **Dataset Versioning using DVC**. A custom employee salary dataset was created and evolved through six versions. Each version introduced meaningful modifications such as salary updates, schema changes, additional records, and department restructuring.

Every dataset version was tracked using **Data Version Control (DVC)** and committed with **Git**, enabling reproducibility and easy restoration of previous dataset versions.