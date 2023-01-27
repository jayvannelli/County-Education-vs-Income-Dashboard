import streamlit as st
from src.data import get_data
import plost


def main():
    st.title("Personal Income Data")

    df = get_data()

    single_state_tab, multi_state_tab = st.tabs(
        ["Single State", "Multi-State"]
    )

    with single_state_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            state_selection = st.selectbox(label="Select state:",
                                           options=df['state'].sort_values().unique())
        with right_column:
            year_selection = st.selectbox("Select year to display:", options=[2019, 2020, 2021])

        state_df = df.loc[df['state'] == state_selection]

        plost.bar_chart(
            data=state_df,
            title=f"{state_selection} Per Capita Personal Income by County ({year_selection})",
            bar="county",
            value=f"per_capita_personal_income_{year_selection}",
            direction='horizontal',
        )

        st.write("---")

        with st.expander(f"Display {state_selection} DataFrame"):
            st.dataframe(state_df)

    with multi_state_tab:
        state_selections = st.multiselect(label="Select states:",
                                          options=df['state'].sort_values().unique(),
                                          default=df['state'].sort_values().unique()[:5])

        # No state selected.
        if len(state_selections) == 0:
            st.info("Please select one, or multiple, state values from the multiselect box")

        # 0 < x < 10 states selected.
        elif 0 < len(state_selections) <= 10:
            state_selections_query = df.query("state == @state_selections")

            st.subheader("Basic chart")
            st.bar_chart(state_selections_query, x="county", y="per_capita_personal_income_2019")

            st.write("---")

            with st.expander("Display full DataFrame"):
                st.dataframe(state_selections_query)

        # 10+ states selected.
        else:
            st.warning("Cannot exceed 10 state selections.")


if __name__ == "__main__":
    main()
