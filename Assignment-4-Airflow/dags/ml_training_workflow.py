from datetime import datetime
from pathlib import Path

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


PROJECT_DIR = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = PROJECT_DIR / "notebooks"
EXECUTION_DIR = Path("/tmp/airflow_ml_pipeline")


with DAG(
    dag_id="automated_ml_training_workflow",
    start_date=datetime(2026, 8, 25),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "machine-learning", "automation"],
) as dag:

    preprocess_data = BashOperator(
        task_id="preprocess_data",
        bash_command=(
            f"mkdir -p {EXECUTION_DIR} && "
            f"jupyter nbconvert "
            f"--to notebook "
            f"--execute {NOTEBOOK_DIR}/data_preprocessing.ipynb "
            f"--output {EXECUTION_DIR}/data_preprocessing_executed.ipynb "
            f"--ExecutePreprocessor.kernel_name=airflow_venv"
        ),
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command=(
            f"mkdir -p {EXECUTION_DIR} && "
            f"jupyter nbconvert "
            f"--to notebook "
            f"--execute {NOTEBOOK_DIR}/model_training.ipynb "
            f"--output {EXECUTION_DIR}/model_training_executed.ipynb "
            f"--ExecutePreprocessor.kernel_name=airflow_venv"
        ),
    )

    evaluate_model = BashOperator(
        task_id="evaluate_model",
        bash_command=(
            f"mkdir -p {EXECUTION_DIR} && "
            f"jupyter nbconvert "
            f"--to notebook "
            f"--execute {NOTEBOOK_DIR}/model_evaluation.ipynb "
            f"--output {EXECUTION_DIR}/model_evaluation_executed.ipynb "
            f"--ExecutePreprocessor.kernel_name=airflow_venv"
        ),
    )

    preprocess_data >> train_model >> evaluate_model