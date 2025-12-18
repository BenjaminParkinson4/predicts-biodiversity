from pathlib import Path
import pandas as pd

# repo_root/src/datasets/load_predicts_tabular.py -> repo_root
REPO_ROOT = Path(__file__).resolve().parents[2]

def load_predicts_extended() -> pd.DataFrame:
    path = REPO_ROOT / "src" / "data" / "processed" / "predicts_extended.csv"
    return pd.read_csv(path)

def load_predicts_cleaned() -> pd.DataFrame:
    path = REPO_ROOT / "src" / "data" / "processed" / "predicts_cleaned.csv"
    return pd.read_csv(path)
