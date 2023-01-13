import streamlit as st
from src.data import get_data
import plost


def main():
    st.title("Personal Income Data")

    df = get_data()
    state_selection = st.selectbox(label="Select state:",
                                   options=df['state'].unique())

    state_df = df.loc[df['state'] == state_selection]
    # st.dataframe(state_df)

    year_selection = st.selectbox("Select year to display:", options=[2019, 2020, 2021])

    plost.bar_chart(
        data=state_df,
        title=f"{state_selection} Per Capita Personal Income ({year_selection})",
        bar="county",
        value=f"per_capita_personal_income_{year_selection}",
        direction='horizontal'
    )


if __name__ == "__main__":
    main()
