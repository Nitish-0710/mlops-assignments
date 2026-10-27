
from pathlib import Path

import joblib
import sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT_DIR / "model"
MODEL_PATH = MODEL_DIR / "iris_model.joblib"


def train_model():
    """Train and save a Random Forest classifier on Iris data."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42,
                ),
            ),
        ]
    )

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    artifact = {
        "model": pipeline,
        "class_names": iris.target_names.tolist(),
        "feature_names": iris.feature_names,
        "model_type": "RandomForestClassifier",
        "dataset": "Iris",
        "test_accuracy": float(accuracy),
        "sklearn_version": sklearn.__version__,
    }

    joblib.dump(artifact, MODEL_PATH)

    print("Model training completed successfully.")
    print(f"Dataset: Iris")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
