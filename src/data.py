import streamlit as st
import pandas as pd


DATA_FILEPATH: str = "data/US_counties_results_20221227_213216.csv"


@st.cache(allow_output_mutation=True)
def get_data() -> pd.DataFrame:
    _df = pd.read_csv(DATA_FILEPATH)
    return _df
