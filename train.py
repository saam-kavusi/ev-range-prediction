"""
train.py

NOTE:
Model training for this project is intentionally performed in notebooks
(notebooks/02_model_training.ipynb) rather than in this script.

Reason:
The EPA vehicles dataset contains many post-processed and efficiency-derived
features that can indirectly encode EV range. Notebook-based training allows
explicit feature inspection and leakage control that would be difficult to
guarantee in a blind script-based retraining workflow.

This script exists to:
- Document the intended training entry point
- Prevent accidental retraining with leaked features
- Serve as a future refactor hook if feature engineering is redesigned
"""

from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parent
    model_path = project_root / "models" / "ev_range_model.joblib"
    notebook_path = project_root / "notebooks" / "02_model_training.ipynb"

    print("✅ Training is notebook-driven for leakage control.")
    print("➡️  Run the training notebook:", notebook_path)

    if model_path.exists():
        print("📦 Model already exists:", model_path)
    else:
        print("⚠️  Model not found yet. Run the notebook to generate it.")


if __name__ == "__main__":
    main()