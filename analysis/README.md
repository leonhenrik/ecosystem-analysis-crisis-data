# Analysis

Python-based data analysis for the crisis data funding ecosystem paper.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Structure

- `scripts/load_data.py` — loads raw CSVs from `../data/raw`, splits semicolon-delimited
  multi-value fields, and writes tidy tables to `../data/processed`.
- `notebooks/` — exploratory analysis and figure generation notebooks. Save final figures
  to `../results/figures` and tables to `../results/tables`.

## Reproducing

```bash
python scripts/load_data.py
jupyter lab notebooks/
```
