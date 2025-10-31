from pathlib import Path
import pandas as pd

def load_orders(data_dir: str | Path) -> pd.DataFrame:
    data_dir = Path(data_dir)
    # load the most recent orders_YYYY-MM-DD.csv
    candidates = sorted(data_dir.glob("orders_*.csv"))
    if not candidates:
        raise FileNotFoundError("No orders_*.csv found in data/")
    orders = pd.read_csv(candidates[-1], parse_dates=["order_date"])
    return orders

def load_dim(path: str | Path, key: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if key not in df.columns:
        raise KeyError(f"Expected key column '{key}' in {path}")
    return df
