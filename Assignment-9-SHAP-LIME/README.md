# Assignment 9: Explainable AI Using SHAP and LIME

## Aim

To apply Explainable Artificial Intelligence (XAI) techniques—SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations)—to interpret predictions made by a machine learning model.

## Objectives

- Train a Random Forest classifier on the Breast Cancer Wisconsin Diagnostic dataset.
- Evaluate the model using standard classification metrics.
- Apply SHAP to analyze global feature importance and explain an individual prediction.
- Apply LIME to explain the same individual prediction.
- Compare the insights provided by SHAP and LIME.

## Dataset

The assignment uses the **Breast Cancer Wisconsin Diagnostic dataset** available through `scikit-learn`.

| Property           | Details                                 |
| ------------------ | --------------------------------------- |
| Dataset            | Breast Cancer Wisconsin Diagnostic      |
| Source             | `sklearn.datasets.load_breast_cancer()` |
| Total samples      | 569                                     |
| Features           | 30 numerical features                   |
| Classes            | Malignant and Benign                    |
| Training split     | 80%                                     |
| Testing split      | 20%                                     |
| Splitting strategy | Stratified train-test split             |

The original target encoding is retained throughout the notebook:

- `0` — Malignant
- `1` — Benign

## Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- SHAP
- LIME

## Model Implementation

A `RandomForestClassifier` is trained using the training dataset with the following configuration:

| Parameter            | Value       |
| -------------------- | ----------- |
| Number of estimators | 200         |
| Random state         | 42          |
| Class weight         | `balanced`  |
| Parallel processing  | `n_jobs=-1` |

The trained model is evaluated on the test dataset before applying the explainability techniques.

## Model Evaluation

The classifier is evaluated using:

- Accuracy
- Macro-averaged precision
- Macro-averaged recall
- Macro-averaged F1-score
- Classification report
- Confusion matrix

These metrics measure the model's classification performance across malignant and benign classes.

## Explainability Techniques

### 1. SHAP

SHAP is used to understand how individual features contribute to the model's output.

The notebook includes:

- **Global Feature Importance:** Ranks features using mean absolute SHAP values across the test set.
- **SHAP Summary Plot:** Shows the distribution, magnitude, and direction of feature contributions across test samples.
- **SHAP Waterfall Plot:** Explains the contributions of individual features for a selected test sample.

The SHAP analysis focuses on the malignant class (`class 0`).

### 2. LIME

LIME explains an individual prediction by perturbing the selected sample and fitting a locally interpretable surrogate model.

The notebook includes:

- A local explanation for the malignant class.
- Feature conditions and their corresponding LIME weights.
- An analysis of features supporting or opposing the malignant-class prediction.

Both SHAP and LIME use the same selected test sample to make their explanations easier to compare.

### 3. SHAP and LIME Comparison

The notebook compares global SHAP feature importance with local LIME feature contributions to identify features highlighted by both techniques.

SHAP summarizes feature contributions across the test set, while LIME focuses on one selected prediction. Their numerical scores have different meanings and should not be compared directly by magnitude.

## Project Structure

```text
Assignment-9-SHAP-LIME/
└── Assignment9_SHAP_LIME.ipynb
```

The assignment is implemented in a single Jupyter Notebook containing the data exploration, model training, evaluation, explainability visualizations, comparison, and conclusion.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Jupyter Notebook or JupyterLab
- pip

Install the required libraries:

```bash
python -m pip install numpy pandas matplotlib scikit-learn shap lime jupyter
```

### Running the Notebook

1. Open the assignment directory.
2. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open `Assignment9_SHAP_LIME.ipynb`.
4. Execute the notebook cells from top to bottom.

The dataset is loaded directly through scikit-learn, so no separate dataset download is required.

## Expected Outputs

After executing the notebook, the following outputs are generated:

- Dataset exploration and class distribution.
- Training and testing dataset information.
- Random Forest evaluation metrics and confusion matrix.
- SHAP global feature importance plot.
- SHAP summary beeswarm plot.
- SHAP waterfall plot for an individual prediction.
- LIME local explanation plot and feature contribution table.
- SHAP and LIME feature comparison plots and tables.
- Final observations and learning outcomes.

## Learning Outcomes

- Understood the importance of explainability in machine learning.
- Trained and evaluated a Random Forest classifier.
- Applied SHAP for global and local feature attribution.
- Used LIME to interpret an individual prediction.
- Compared global feature importance with local feature contributions.
- Recognized the limitations of model explanations.

## Limitations

SHAP and LIME explain the behavior of the trained model; they do not establish causal relationships or guarantee that a prediction is correct. Explanations may differ because the methods use different approaches and scales.

**Disclaimer:** This assignment is intended for educational purposes only. The dataset, model, and explanations must not be used for clinical diagnosis or medical decision-making.
