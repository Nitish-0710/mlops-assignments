from pathlib import Path
import pandas as pd
import requests

BASE_DIR = Path(__file__).resolve().parent.parent

raw = pd.read_csv(BASE_DIR / "data" / "house_prices.csv")

sample = (
    raw.iloc[0]
    .drop(labels=["Id", "SalePrice"])
    .to_dict()
)

sample = {
    k: (
        None
        if pd.isna(v)
        else v.item() if hasattr(v, "item") else v
    )
    for k, v in sample.items()
}

payload = {
    "features": sample
}

print("Number of fields:", len(sample))

BASE_URL = "http://127.0.0.1:8000"

r = requests.get(BASE_URL + "/health")
print("\nHealth:", r.status_code)
print(r.json())

r = requests.get(BASE_URL + "/model-info")
print("\nModel info:", r.status_code)
print(r.json())

r = requests.post(
    BASE_URL + "/predict",
    json=payload
)

print("\nPrediction:", r.status_code)
print(r.json())