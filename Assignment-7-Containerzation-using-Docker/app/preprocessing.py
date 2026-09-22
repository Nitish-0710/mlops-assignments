import pandas as pd


def feature_engineering(X):
    X = X.copy()

    # Handle categorical features whose missing values represent absence
    absence_categorical = [
        "Alley",
        "BsmtQual",
        "BsmtCond",
        "BsmtExposure",
        "BsmtFinType1",
        "BsmtFinType2",
        "FireplaceQu",
        "GarageType",
        "GarageFinish",
        "GarageQual",
        "GarageCond",
        "PoolQC",
        "Fence",
        "MiscFeature"
    ]

    for col in absence_categorical:
        if col in X.columns:
            X[col] = X[col].fillna("None")

    # Feature engineering
    X["HouseAge"] = X["YrSold"] - X["YearBuilt"]

    X["RemodAge"] = X["YrSold"] - X["YearRemodAdd"]

    X["TotalSF"] = (
        X["TotalBsmtSF"]
        + X["1stFlrSF"]
        + X["2ndFlrSF"]
    )

    X["TotalBathrooms"] = (
        X["FullBath"]
        + 0.5 * X["HalfBath"]
        + X["BsmtFullBath"]
        + 0.5 * X["BsmtHalfBath"]
    )

    X["TotalPorchSF"] = (
        X["OpenPorchSF"]
        + X["3SsnPorch"]
        + X["EnclosedPorch"]
        + X["ScreenPorch"]
        + X["WoodDeckSF"]
    )

    # Treat these originally numerical columns as categorical
    if "MSSubClass" in X.columns:
        X["MSSubClass"] = X["MSSubClass"].astype(str)

    if "MoSold" in X.columns:
        X["MoSold"] = X["MoSold"].astype(str)

    return X