# Week 5 – Apparel & Textiles Trend Analysis and Forecasting

A reproducible data analytics project for exploring historical apparel and textile market indicators, applying moving-average and linear-regression forecasting, visualizing trends, and translating results into business recommendations.

## Project scope
- Market focus: India apparel and textiles sector.
- Analytical workflow: data preparation → exploratory trend analysis → forecasting → model evaluation → market interpretation.
- Methods: 3-month and 6-month moving averages, linear trend regression, and optional seasonal decomposition when enough observations are available.
- Outputs: cleaned data, forecast tables, evaluation metrics, and charts.

## Important data note
The included `data/sample_monthly_market_data.csv` is **synthetic demonstration data**, not official Indian market statistics. It exists so the complete workflow runs immediately and so that the modelling steps can be reproduced. Do not present its values or forecasts as actual market facts. For a real submission, replace it with a documented public dataset and record the source, download date, units, coverage, and any transformations.

## Repository structure
```text
 data/       sample data and source notes
 notebooks/  notebook workflow guide
 src/        reusable analysis and forecasting scripts
 outputs/    generated charts and forecast tables
 report/     standalone report in Markdown
```

## Quick start
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/run_analysis.py
```

Generated files are written to `outputs/` (created automatically).

## Methods
1. **Moving average:** smooths short-term fluctuations and provides a transparent baseline.
2. **Linear regression:** estimates a time trend using month index as the predictor; useful as a simple trend benchmark, not a causal model.
3. **Holdout evaluation:** the final 6 months are held out where the dataset is sufficiently long; MAE and RMSE are reported.
4. **Forecast interpretation:** projections are conditional on historical patterns continuing. Structural changes, policy, input costs, exchange rates, weather, and consumer behaviour can invalidate them.

## Suggested real-data sources to investigate
- Ministry of Textiles, Government of India: annual reports, policy and sector publications.
- Office of the Economic Adviser: Index of Industrial Production and Wholesale Price Index series.
- Directorate General of Commercial Intelligence and Statistics (DGCI&S): trade statistics.
- RBI Database on Indian Economy: exchange rates and macroeconomic indicators.
- UN Comtrade / World Bank WITS: product-level international trade data.
- Public company annual reports and investor presentations: firm-level context.

Use consistent product classifications and units when combining sources. Monthly data should not be mixed with annual observations without an explicit aggregation method.

## Limitations
This is an educational forecasting exercise, not investment advice or an official industry outlook. Synthetic data demonstrates the code only. Real forecasts require verified observations, source citations, appropriate frequency alignment, and back-testing.

## Author
Week 5 Internship Project – Apparel & Textiles Data Analytics