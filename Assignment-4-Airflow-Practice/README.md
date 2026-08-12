# Assignment 4 – Airflow Practice DAG

## Objective

To understand the basics of workflow orchestration using Apache Airflow by creating a simple DAG with multiple dependent tasks.

## Tools Used

* Python 3.14
* Apache Airflow 3.3.0
* WSL 2
* Ubuntu
* VS Code

## Workflow

The practice DAG contains three tasks that execute in the following order:

```text
collect_data
      ↓
calculate_attendance
      ↓
generate_report
```

The task dependencies are managed by Apache Airflow.

## DAG Name

```text
student_attendance_workflow
```

## Tasks

### 1. collect_data

Collects the total number of students.

* Total students: 100
* Returns: `100`

### 2. calculate_attendance

Receives the total number of students from `collect_data` and calculates the attendance percentage.

* Total students: 100
* Present students: 85
* Attendance: 85%

The returned value is passed to the next task using Airflow's task communication mechanism (XCom).

### 3. generate_report

Receives the calculated attendance and generates the final attendance report.

The report contains:

```text
STUDENT ATTENDANCE REPORT
Attendance: 85%
Status: GOOD
Report Generated Successfully!
```

The report is saved as:

```text
output/student_report.txt
```

## Project Structure

```text
Assignment-4-Airflow-Practice/
│
├── dags/
│   └── student_workflow.py
│
├── output/
│   └── student_report.txt
│
└── README.md
```

## Running the DAG

### 1. Start WSL

Open Ubuntu through WSL.

### 2. Activate the Airflow virtual environment

```bash
source ~/airflow_venv/bin/activate
```

### 3. Navigate to the Assignment 4 directory

```bash
cd Assignment-4-Airflow-Practice
```

### 4. Set the DAG folder

```bash
export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags"
```

### 5. Start Airflow

```bash
airflow standalone
```

Keep this terminal running while using Airflow.

### 6. Open the Airflow Web UI

Open:

```text
http://localhost:8080
```

### 7. Run the DAG

1. Open `student_attendance_workflow`.
2. Open the DAG graph.
3. Trigger the DAG manually.
4. Wait for all three tasks to complete successfully.

## Output

After successful execution, the following file is generated:

```text
output/student_report.txt
```

Its contents are:

```text
STUDENT ATTENDANCE REPORT
Attendance: 85%
Status: GOOD
Report Generated Successfully!
```

## Result

The practice DAG was successfully executed using Apache Airflow.

All three tasks completed successfully in the correct order:

```text
collect_data
      ↓
calculate_attendance
      ↓
generate_report
```

The final attendance report was also generated successfully as a text file.

## Conclusion

This practice demonstrates the basic concepts of Apache Airflow, including DAGs, task dependencies, task execution, XCom data passing, logging, manual triggering, and workflow monitoring through the Airflow Web UI.
