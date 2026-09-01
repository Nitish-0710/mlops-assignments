import pickle
import pandas as pd


# Load trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)


# Take student input
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter Attendance (%): "))
coding_score = float(input("Enter Coding Score: "))
projects = int(input("Enter Number of Projects: "))
internship = int(input("Enter Internship (1 = Yes, 0 = No): "))


# Create input with the same feature names used during training
student = pd.DataFrame([{
    "CGPA": cgpa,
    "Attendance": attendance,
    "CodingScore": coding_score,
    "Projects": projects,
    "Internship": internship
}])


# Make prediction
prediction = model.predict(student)[0]


# Display result
if prediction == 1:
    print("Predicted Result: PLACED")
else:
    print("Predicted Result: NOT PLACED")
