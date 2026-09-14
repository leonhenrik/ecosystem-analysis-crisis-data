
from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

MULTI_VALUE_SEP = ";"


def _split_multi_value(series: pd.Series) -> pd.Series:
    return series.fillna("").apply(
        lambda v: [s.strip() for s in v.split(MULTI_VALUE_SEP) if s.strip()]
    )


def load_organizations(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
    path = next(raw_dir.glob("organizations-*.csv"))
    df = pd.read_csv(path)
    df["Supporting Donors"] = _split_multi_value(df["Supporting Donors"])
    return df


def load_assets(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
    path = next(raw_dir.glob("assets-*.csv"))
    df = pd.read_csv(path)
    for col in ("Investment Types", "Investment Themes", "Supporting Donors"):
        if col in df.columns:
            df[col] = _split_multi_value(df[col])
    return df


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    load_organizations().to_pickle(PROCESSED_DIR / "organizations.pkl")
    load_assets().to_pickle(PROCESSED_DIR / "assets.pkl")
    print(f"Wrote processed tables to {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
