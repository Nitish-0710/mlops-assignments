import os
import pickle
import pandas as pd


MODEL_FILE = "placement_model.pkl"


def load_model():
    with open(MODEL_FILE, "rb") as file:
        return pickle.load(file)


def test_model_file_exists():
    assert os.path.exists(MODEL_FILE)


def test_model_can_be_loaded():
    model = load_model()
    assert model is not None


def test_model_prediction_is_valid():
    model = load_model()

    student = pd.DataFrame([{
        "CGPA": 8.5,
        "Attendance": 92,
        "CodingScore": 85,
        "Projects": 3,
        "Internship": 1
    }])

    prediction = model.predict(student)[0]

    assert prediction in [0, 1]


def test_placed_student_prediction():
    model = load_model()

    student = pd.DataFrame([{
        "CGPA": 8.5,
        "Attendance": 92,
        "CodingScore": 85,
        "Projects": 3,
        "Internship": 1
    }])

    prediction = model.predict(student)[0]

    assert prediction == 0


def test_not_placed_student_prediction():
    model = load_model()

    student = pd.DataFrame([{
        "CGPA": 5.9,
        "Attendance": 60,
        "CodingScore": 42,
        "Projects": 1,
        "Internship": 0
    }])

    prediction = model.predict(student)[0]

    assert prediction == 0
