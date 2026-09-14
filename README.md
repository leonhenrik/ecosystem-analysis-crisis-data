# Ecosystem Analysis: Crisis Data Funding

Research repository analyzing the crisis data funding ecosystem — organizations,
assets/projects, and donors supporting crisis/humanitarian data initiatives, based on
data from the [Crisis Data Funding Compass](https://crafd.io) (CRAF'd).

## Repository Structure

```
.
├── paper/                  # LaTeX manuscript
│   ├── main.tex
│   ├── sections/           # one .tex file per section
│   ├── bibliography/references.bib
│   └── figures/            # figures included directly in the paper
├── data/
│   ├── raw/                # original CSV exports (read-only, versioned)
│   └── processed/          # cleaned tables produced by analysis scripts
├── analysis/
│   ├── scripts/            # reusable data loading/cleaning/analysis code
│   ├── notebooks/          # exploratory analysis, figure generation
│   └── requirements.txt
├── results/
│   ├── figures/            # generated figures (source of truth for paper/figures)
│   └── tables/             # generated tables (e.g., LaTeX/CSV summary tables)
└── README.md
```

## Getting Started

1. Set up the analysis environment:
   ```bash
   cd analysis
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Load and clean the data:
   ```bash
   python scripts/load_data.py
   ```
3. Explore in `analysis/notebooks/`; export figures/tables to `results/`.
4. Build the paper:
   ```bash
   cd paper
   latexmk -pdf main.tex
   ```

## Data

See [data/README.md](data/README.md) for the data dictionary and provenance. Raw data is
sourced from CRAF'd's Crisis Data Funding Compass and is subject to expansion/correction.

## Citing

TODO: add citation instructions / `CITATION.cff` once the paper is published.

## License

Code is licensed under the MIT License (see [LICENSE](LICENSE)). Paper text and figures
are © the authors; see `paper/` for details once finalized.
