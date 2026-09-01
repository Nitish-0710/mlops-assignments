import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("data/student_placement.csv")

# Validate required columns
required_columns = [
    "CGPA",
    "Attendance",
    "CodingScore",
    "Projects",
    "Internship",
    "Placement"
]

if not all(column in data.columns for column in required_columns):
    raise ValueError("Dataset is missing required columns.")

# Check for missing values
if data[required_columns].isnull().any().any():
    raise ValueError("Dataset contains missing values.")

# Separate features and target
X = data.drop("Placement", axis=1)
y = data["Placement"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create and train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Training Completed")
print("Test Accuracy:", accuracy)

# Accuracy quality gate
if accuracy < 0.80:
    raise ValueError(f"Model accuracy {accuracy:.2f} is below 80%.")

print("Accuracy requirement satisfied: >= 80%")

# Save trained model
with open("placement_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as placement_model.pkl")
