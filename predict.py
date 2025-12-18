from pathlib import Path
from sklearn.pipeline import Pipeline

import json
import joblib
import pandas as pd
import warnings

warnings.filterwarnings(
    "ignore",
    message=r"Skipping features without any observed values.*",
    category=UserWarning
)

warnings.filterwarnings(
    "ignore",
    message="Skipping features without any observed values"
)

# -------------------------------
# Resolve project root
# -------------------------------
CWD = Path.cwd()
PROJECT_ROOT = CWD if (CWD / "data").exists() else CWD.parent

MODEL_PATH = PROJECT_ROOT / "models" / "ev_range_model.joblib"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

# -------------------------------
# Load model
# -------------------------------
model = joblib.load(MODEL_PATH)

if not isinstance(model, Pipeline):
    raise TypeError("Loaded model is not a sklearn Pipeline.")

print(f"✅ Model loaded from: {MODEL_PATH}")

# -------------------------------
# Predict from JSON
# -------------------------------
example_path = DATA_PROCESSED / "example_prediction.json"

with open(example_path) as f:
    payload = json.load(f)

input_features = payload["input_features"]

# Convert to DataFrame (single-row inference)
X = pd.DataFrame([input_features])

prediction = model.predict(X)[0]

print("🔮 Predicted EV range (miles):", round(float(prediction), 2))