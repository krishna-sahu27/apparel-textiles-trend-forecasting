"""Simple, transparent forecasting methods for monthly market indicators."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def build_forecasts(df: pd.DataFrame, target: str = "demand_index", horizon: int = 12):
    """Return fitted historical series, future forecasts and holdout metrics.

    Uses a final-six-month holdout (when possible), a 3-month moving-average
    baseline and a linear trend regression. Forecasts are conditional, not
    causal predictions.
    """
    data = df[["date", target]].dropna().sort_values("date").copy()
    if len(data) < 12:
        raise ValueError("At least 12 monthly observations are required.")
    data["time_index"] = np.arange(len(data))
    split = max(6, len(data) - 6)
    train, test = data.iloc[:split], data.iloc[split:]
    model = LinearRegression().fit(train[["time_index"]], train[target])
    pred_test = model.predict(test[["time_index"]])
    metrics = {
        "holdout_months": int(len(test)),
        "linear_trend_MAE": float(mean_absolute_error(test[target], pred_test)),
        "linear_trend_RMSE": float(np.sqrt(mean_squared_error(test[target], pred_test))),
        "note": "Metrics are in target-index units; use only as a simple benchmark."
    }
    all_model = LinearRegression().fit(data[["time_index"]], data[target])
    future_idx = np.arange(len(data), len(data) + horizon)
    future_dates = pd.date_range(data["date"].max() + pd.offsets.MonthBegin(1), periods=horizon, freq="MS")
    trend = all_model.predict(future_idx.reshape(-1, 1))
    ma_value = float(data[target].tail(3).mean())
    out = pd.DataFrame({
        "date": future_dates,
        "linear_trend_forecast": trend,
        "three_month_moving_average": ma_value,
    })
    historical = data[["date", target]].copy()
    historical["series"] = "actual"
    forecast_long = out[["date", "linear_trend_forecast"]].rename(columns={"linear_trend_forecast": target})
    forecast_long["series"] = "linear trend forecast"
    combined = pd.concat([historical, forecast_long], ignore_index=True)
    return out, metrics, combined
