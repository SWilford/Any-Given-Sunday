import pandas as pd
from ags.data import fetch


def test_fetch_games_returns_dataframe():
    df = fetch.fetch_games([2023])
    assert isinstance(df, pd.DataFrame)
    assert "season" in df.columns
    assert df["season"].nunique() == 1
    assert df["season"].iloc[0] == 2023
