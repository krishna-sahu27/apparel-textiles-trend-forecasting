"""Data checks and descriptive summaries."""
import pandas as pd

REQUIRED = ["date", "demand_index", "export_value_index", "cotton_cost_index"]

def load_data(path="data/sample_monthly_market_data.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df = df.sort_values("date").drop_duplicates("date")
    for col in REQUIRED[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def summary_table(df):
    return df[REQUIRED[1:]].describe().round(2)
