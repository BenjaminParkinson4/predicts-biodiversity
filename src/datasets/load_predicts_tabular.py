import pandas as pd


def load_predicts_extended(path="src/data/processed/predicts_extended.csv"):
    df = pd.read_csv(path)
    return df
