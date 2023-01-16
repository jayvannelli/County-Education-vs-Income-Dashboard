import streamlit as st
from src.states import get_state_abbreviations, state_counties


def main():
    st.title("State Specific Data")

    all_state_abbvs = get_state_abbreviations()

    state_selection = st.selectbox("Select state", options=all_state_abbvs)
    selected_state_counties = state_counties(state_selection)

    county_selections = st.multiselect(label="Select county/counties",
                                       options=selected_state_counties,
                                       default=selected_state_counties[:5])

    st.write(county_selections)
    st.write(selected_state_counties)


if __name__ == "__main__":
    main()
