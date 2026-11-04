# Notebook workflow

The full reproducible workflow is in `src/run_analysis.py`. To explore interactively, open a Jupyter notebook and run:

```python
import pandas as pd
from pathlib import Path
from src.forecasting import build_forecasts

df = pd.read_csv('data/sample_monthly_market_data.csv', parse_dates=['date'])
print(df.head())
print(df.describe())
forecasts, metrics = build_forecasts(df, target='demand_index')
print(forecasts.tail(12))
print(metrics)
```

Run from the repository root after installing `requirements.txt`. The dataset is synthetic demonstration data.