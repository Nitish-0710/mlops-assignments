# Practice Assignment - Dataset Versioning using DVC

## 📌 Objective

The objective of this practice assignment is to understand the basic workflow of **Dataset Versioning using Data Version Control (DVC)**.

A custom **Student Dataset** is created and maintained through multiple versions. The dataset is tracked using **DVC** while Git is used to manage the project source code and version history.

---

## 🛠️ Technologies Used

- Python 3
- Jupyter Notebook
- Pandas
- Git
- DVC (Data Version Control)

---

## 📂 Project Structure

```
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

---

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

---

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

---

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

---

# 🔄 DVC Workflow

The following workflow was followed for every dataset version.

```
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

---

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

---

# 📈 Dataset Evolution

| Version | Changes |
|---------|----------|
| Version 1 | Initial student dataset containing 10 records |
| Version 2 | Added three new student records (13 total records) |

---

# 🎯 Learning Outcomes

After completing this practice assignment, the following concepts were understood:

- Creating custom datasets
- Saving datasets as CSV files
- Tracking datasets using DVC
- Managing datasets with Git
- Creating multiple dataset versions
- Restoring previous dataset versions
- Understanding the basic DVC workflow

---

# 📌 Conclusion

This practice assignment successfully demonstrates the basic workflow of **Dataset Versioning using DVC**. A custom student dataset was created and evolved through two versions. The initial dataset contained **10 student records**, and a second version was created by adding **three new student records**. Each version was tracked using **Data Version Control (DVC)** and committed using **Git**, illustrating how datasets can be versioned and restored efficiently in Machine Learning projects.