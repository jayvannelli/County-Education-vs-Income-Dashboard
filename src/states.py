import pandas as pd
from src.data import get_data

full_dataframe = get_data()


def get_state_abbreviations() -> pd.Series:
    """Returns all unique values in 'state' column (list of state abbreviations)."""
    return full_dataframe["state"].unique()


def state_counties(state_abbreviation: str) -> pd.Series | None:
    """Returns list of counties within passed state (by abbreviation)."""
    all_state_abbvs = get_state_abbreviations()

    if state_abbreviation not in all_state_abbvs:
        raise ValueError(
            f"Invalid state abbreviation: {state_abbreviation}."
            f"Valid state abbreviations include: {all_state_abbvs}."
        )

    state_df = full_dataframe.loc[full_dataframe['state'] == state_abbreviation]
    return state_df["county"].unique()
