from airflow.sdk import dag, task


@dag(schedule=None, start_date=None, catchup=False)
def student_attendance_workflow():

    @task
    def collect_data():
        print("Step 1: Collecting student data...")
        total_students = 100
        print(f"Total Students: {total_students}")
        return total_students

    @task
    def calculate_attendance(total_students):
        print("Step 2: Calculating attendance...")
        present_students = 85
        attendance = (present_students / total_students) * 100
        print(f"Present Students: {present_students}")
        print(f"Attendance: {attendance}%")
        return attendance

    @task
    def generate_report(attendance):
        print("Step 3: Generating report...")

        report = f"""STUDENT ATTENDANCE REPORT
Attendance: {attendance}%
Status: {"GOOD" if attendance >= 75 else "LOW"}
Report Generated Successfully!
"""

        print(report)

        output_file = "/mnt/d/College/3rd_Year/MLOPS/Assignment-4-Airflow/output/student_report.txt"

        with open(output_file, "w") as file:
            file.write(report)

        print(f"Report saved to: {output_file}")


    total_students = collect_data()
    attendance = calculate_attendance(total_students)
    generate_report(attendance)


student_attendance_workflow()