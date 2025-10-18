import sys
import os
import pandas as pd
import holoviews as hv
import colorcet as cc
import hvplot.pandas

from src.preprocessing import preprocess_data
from src.preprocessing import STATS_COLS, INFO_COLS, Z_SCORE_COLS
import panel as pn

from bokeh.models.widgets.tables import NumberFormatter, BooleanFormatter


pn.extension("tabulator")

N_TEAMS = 12
BUDGET_PER_TEAM = 200
TOTAL_BUDGET = BUDGET_PER_TEAM * N_TEAMS


raw_data = pd.read_csv("./data/parsed_fantasy_projection_2024_2025.csv")
data = preprocess_data(raw_data)

formatters = {
    "base_value": NumberFormatter(format="0.0"),
    "adjusted_value": NumberFormatter(format="0.0"),
}


def calculate_value_scaling(stats_to_scale: pd.Series, total_budget: float) -> float:
    is_positive = stats_to_scale > 0
    total_stats = stats_to_scale[is_positive].sum()
    n_positive = is_positive.sum()
    value_per_stat = total_budget / total_stats
    print(f"\nThere are {n_positive} players with positive stats")
    print(f"Total Z-score for positive values players are {total_stats}")
    print(f"Each Z-score is equivalent to {value_per_stat}")
    return value_per_stat


def get_player_value(stats_to_scale: pd.Series, value_per_stat: float) -> pd.Series:
    scaled_value = stats_to_scale * value_per_stat
    scaled_value[scaled_value < 0] = 0
    return scaled_value


scaler_injury_free = calculate_value_scaling(data["TOTAL"], total_budget=TOTAL_BUDGET)
data["base_value"] = get_player_value(data["TOTAL"], value_per_stat=scaler_injury_free)
data["health_factor"] = data["GP"] / 82
data["health_factor_total"] = data["health_factor"] * data["TOTAL"]
scaler_health_related = calculate_value_scaling(
    data["health_factor_total"], total_budget=TOTAL_BUDGET
)
data["adjusted_value"] = get_player_value(
    data["health_factor_total"], value_per_stat=scaler_health_related
)

data["injury_risk_delta"] = data["adjusted_value"] - data["base_value"]

# * -------- visualization ---------

injury_delta_scatters = data.hvplot.scatter(
    x="injury_risk_delta",
    y="adjusted_value",
    s=150,
    c="injury_risk_delta",
    cmap=cc.m_bwy_r,
    hover_cols=[
        "PLAYER",
        "GP",
        "health_factor",
        "base_value",
    ],
)
plot_opts = dict(width=600, height=400, show_grid=True, show_legend=True)
pane_injury = injury_delta_scatters.opts(
    xlabel="injury_risk_delta",
    ylabel="adjusted_value",
    title="Risk adjustment to player value",
    **plot_opts,
)

value_cols = ["adjusted_value", "base_value", "injury_risk_delta"]
display_cols = value_cols + INFO_COLS 

tabulator_config = [
    {"field": "PLAYER", "title": "Player", "headerFilter": True},
    {"field": "POS", "title": "Position", "headerFilter": True},
    {"field": "TEAM", "title": "Team", "headerFilter": True},
]

sorters = [{"field": "adjusted_value", "dir": "desc"}]

draft_board = pn.widgets.Tabulator(
    data[display_cols],
    pagination="remote",
    page_size=30,
    sizing_mode="stretch_width",
    height=1000,
    formatters=formatters,
    sorters=sorters,
)


# Get the list of player names
player_names = data["PLAYER"].tolist()

# Create the AutocompleteInput widget
player_search = pn.widgets.AutocompleteInput(
    name="Search Player",
    options=player_names,
    placeholder="Type player name...",
    case_sensitive=False,
    min_characters=1,
    width=300,
    search_strategy="includes",
)


# Define the function to display player information
@pn.depends(player_search)
def show_player_info(player_name):
    if player_name in data["PLAYER"].values:
        # Get the player's data
        player_data = data[data["PLAYER"] == player_name]
        # Select columns to display (you can customize this list)
        columns_to_show = [
            "PLAYER",
            "POS",
            "adjusted_value",
            "base_value",
            "FG%",
            "FT%",
            "3PM",
            "PTS",
            "TREB",
            "AST",
            "STL",
            "BLK",
        ]

        player_info = player_data[columns_to_show]
        player_z_score = player_data[Z_SCORE_COLS]
        pane_player_info = pn.widgets.Tabulator(
            player_info,
            sizing_mode="stretch_width",
            disabled=True,
            show_index=False,
            formatters=formatters,
        )
        z_score_max = data[Z_SCORE_COLS].abs().max().max()
        pane_player_z_score = player_z_score.hvplot.barh().opts(
            ylim=(-z_score_max, z_score_max), show_grid=True
        )

        return pn.Column(pane_player_info, pane_player_z_score)

    else:
        return pn.pane.Markdown(
            "**Player not found. Please select a player from the list.**"
        )


dashboard = pn.Column(player_search, show_player_info, draft_board, pane_injury)
dashboard.servable()
