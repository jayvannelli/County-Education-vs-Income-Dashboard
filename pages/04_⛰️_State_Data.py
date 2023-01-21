import streamlit as st
import pandas as pd

from src.data import get_data
from src.states import get_state_abbreviations, state_counties


def main():
    st.title("State Specific Data")

    df = get_data()

    all_state_abbvs = get_state_abbreviations()

    state_selection = st.selectbox("Select state", options=all_state_abbvs)
    state_df = df.loc[df['state'] == state_selection]
    st.dataframe(state_df)


if __name__ == "__main__":
    main()
