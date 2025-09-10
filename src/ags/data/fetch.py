"""
Data fetching utilities for Any Given Sunday.
Uses nfl_data_py to pull historical game and play data.
"""

import nfl_data_py as nfl
import pandas as pd


def fetch_games(years: list[int]) -> pd.DataFrame:
    games = nfl.import_schedules(years)
    return games


if __name__ == "__main__":
    # Quick smoke test
    df_games = fetch_games([2023])
    print(df_games.head())
