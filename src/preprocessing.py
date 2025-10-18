import pandas as pd

STATS_COLS = [
    "FG%",
    "FT%",
    "PTS",
    "TREB",
    "AST",
    "STL",
    "BLK",
    "3PM",
]

Z_SCORE_COLS = [
    "FG%_z_score",
    "FT%_z_score",
    "PTS_z_score",
    "TREB_z_score",
    "AST_z_score",
    "STL_z_score",
    "BLK_z_score",
    "3PM_z_score",
]

OTHER_COLS = [
    "FGM",
    "FGA",
    "FTM",
    "FTA",
]

INFO_COLS = [
    "ADP",
    "PLAYER",
    "POS",
    "TEAM",
    "GP",
    "MPG",
    "TOTAL",
]


def preprocess_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    all_cols = INFO_COLS + STATS_COLS + Z_SCORE_COLS + OTHER_COLS
    data = raw_data[all_cols].copy()
    data["Rank"] = data.index + 1
    return data
