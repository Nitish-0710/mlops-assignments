# Assignment 2 – ML Experiment Tracking using MLflow

## Objective

The objective of this assignment is to understand how to track machine learning experiments using **MLflow**.

In this assignment, the **Iris dataset** is used with a Logistic Regression model. Different hyperparameter values are tested and the experiments are tracked using MLflow.

## Dataset

The **Iris dataset** is used for this assignment.

It contains 150 samples of iris flowers belonging to three classes:

* Setosa
* Versicolor
* Virginica

The dataset contains four features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

## Tools and Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* MLflow
* Matplotlib
* Jupyter Notebook

## Steps Performed

1. Loaded the Iris dataset.
2. Explored the dataset and checked for missing values.
3. Separated features and target variable.
4. Split the dataset into training and testing sets using an 80:20 ratio.
5. Applied feature scaling using `StandardScaler`.
6. Created an MLflow experiment named `Iris_Classification_Experiments`.
7. Trained a baseline Logistic Regression model.
8. Tested different values of the `C` parameter:

   * `0.1`
   * `1.0`
   * `10.0`
9. Tested different values of `max_iter`:

   * `50`
   * `100`
   * `200`
10. Logged model parameters, accuracy, and trained models using MLflow.
11. Compared the experiment runs.
12. Visualized the experiment results.
13. Selected the best-performing experiment.
14. Evaluated the final model.
15. Viewed the experiment runs using the MLflow web interface.

## Experiment Results

### Effect of C

| C Value | Test Accuracy |
| ------: | ------------: |
|     0.1 |        86.67% |
|     1.0 |        93.33% |
|    10.0 |       100.00% |

### Effect of max_iter

| max_iter | Test Accuracy |
| -------: | ------------: |
|       50 |        93.33% |
|      100 |        93.33% |
|      200 |        93.33% |

## Best Model

The best-performing experiment used:

* **Model:** Logistic Regression
* **C:** 10.0
* **max_iter:** 200
* **Test Accuracy:** 100%

The model correctly classified all 30 samples in the test set.

## MLflow Tracking

MLflow was used to track:

* Experiment runs
* Model parameters
* Accuracy metrics
* Trained model artifacts

The MLflow UI was opened locally to view and compare the experiment runs.

## Conclusion

This assignment demonstrated how MLflow can be used to track machine learning experiments. Different hyperparameter values were tested and their results were recorded and compared.

The best-performing Logistic Regression model achieved **100% test accuracy** with `C = 10.0`.

MLflow makes it easier to organize, track, and compare machine learning experiments.

## Files

```text
Assignment-2-MLFlow/
│
├── README.md
│
└── notebooks/
    └── Assignment2.ipynb
```