# EV Range Prediction — Interpretation Summary

## Test-set performance
- **MAE:** 16.07 miles
- **RMSE:** 23.32 miles
- **R²:** 0.8973

## What the plots suggest
- Predicted vs Actual: points close to the diagonal indicate good fit; outliers show worst misses.
- Absolute error distribution: shows typical error and tail risk (rare large misses).
- MAE by brand/year: highlights segments where the model generalizes poorly (often data scarcity or unusual models).

## Limitations (important for credibility)
- Some models/brands have low support → higher uncertainty.
- EPA range can differ from real-world range; model predicts the dataset’s target definition.

## Next steps
- Add more features (battery kWh, weight, efficiency) if available.
- Try a stronger model / tuning, or calibrate predictions for high-range vehicles.
