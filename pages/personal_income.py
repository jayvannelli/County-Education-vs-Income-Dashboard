import streamlit as st
from src.data import get_data
import plost


def main():
    st.title("Personal Income Data")

    df = get_data()

    single_state_tab, multi_state_tab = st.tabs([
        "Single State", "Multi-State"
    ])

    with single_state_tab:
        state_selection = st.selectbox(label="Select state:",
                                       options=df['state'].unique())

        state_df = df.loc[df['state'] == state_selection]

        year_selection = st.selectbox("Select year to display:", options=[2019, 2020, 2021])

        plost.bar_chart(
            data=state_df,
            title=f"{state_selection} Per Capita Personal Income by County ({year_selection})",
            bar="county",
            value=f"per_capita_personal_income_{year_selection}",
            direction='horizontal',
        )

    with multi_state_tab:
        with st.form("multi_state_selection_form"):
            state_selections = st.multiselect(label="Select states:",
                                              options=df['state'].unique(),
                                              default=df['state'].unique()[:5])
            submit_button = st.form_submit_button("Load data")

        if submit_button:
            for state in state_selections:
                st.subheader(f"Pandas DataFrame for state: {state}")

                single_state_df = df.loc[df['state'] == state]
                st.dataframe(single_state_df)

    st.write("---")

    with st.expander(f"Display {state_selection} DataFrame"):
        st.dataframe(state_df)


if __name__ == "__main__":
    main()
