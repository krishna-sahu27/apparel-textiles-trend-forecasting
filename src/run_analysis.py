"""Run the complete demonstration analysis from the repository root."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from data_analysis import load_data, summary_table
from forecasting import build_forecasts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main():
    df = load_data(ROOT / "data" / "sample_monthly_market_data.csv")
    summary_table(df).to_csv(OUT / "descriptive_summary.csv")
    forecasts, metrics, _ = build_forecasts(df, "demand_index", 12)
    forecasts.to_csv(OUT / "demand_forecast_12_months.csv", index=False)
    pd.DataFrame([metrics]).to_csv(OUT / "model_evaluation.csv", index=False)

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(df.date, df.demand_index, label="Historical sample", linewidth=2)
    ax.plot(forecasts.date, forecasts.linear_trend_forecast, label="Linear trend forecast", linestyle="--")
    ax.plot(forecasts.date, forecasts.three_month_moving_average, label="3-month moving-average baseline", linestyle=":")
    ax.set(title="Illustrative apparel demand index: history and 12-month forecasts", xlabel="Month", ylabel="Index (synthetic)")
    ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
    fig.savefig(OUT / "demand_forecast.png", dpi=160); plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 5))
    for col in ["export_value_index", "cotton_cost_index"]:
        ax.plot(df.date, df[col], label=col.replace("_", " "))
    ax.set(title="Illustrative export and cotton-cost indices", xlabel="Month", ylabel="Index (synthetic)")
    ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
    fig.savefig(OUT / "market_indicators.png", dpi=160); plt.close(fig)
    print("Analysis complete. See outputs/ for CSV tables and PNG charts.")
    print("IMPORTANT: input data is synthetic; outputs are demonstration only.")
    print(metrics)

if __name__ == "__main__":
    main()
