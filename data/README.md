# Data

## Source

Raw exports from the **Crisis Data Funding Compass**, maintained by the Complex Risk
Analytics Fund (CRAF'd, https://crafd.io). See `raw/README.txt` for the original export
notes.

## Directory Layout

- `raw/` — untouched original export (CSV + original README). Do not edit; treat as
  read-only. Re-export from the Compass and drop new dated files here if the source data
  changes.
- `processed/` — cleaned/tidied data produced by `analysis/scripts/load_data.py`
  (gitignored; regenerate locally, or remove from `.gitignore` if you want processed
  data version-controlled).

## Files

### `raw/organizations-*.csv`
Organization Name, Organization Type, Description, Supporting Donors (`;`-separated).

### `raw/assets-*.csv`
Asset Name, Organization Name, Asset Types, Supporting Donors
(`;`-separated where multi-valued), Description, Website.

## Summary (as of 2026-09-14 export)

- Total Organizations: 92
- Total Assets/Projects: 243
- Unique Donor Countries: 76

## Notes

- Multiple values in a single field are separated by semicolons (`;`).
- Empty fields indicate information was not available at export time.
- For assets without asset-level donor information, organization-level donors are used.
