import streamlit as st
from src.data import get_data

import plost


def main():
    st.title("US Counties | Education vs. Per Capita Personal Income")

    df = get_data()

    top_left_column, top_right_column = st.columns([2, 1])
    with top_left_column:
        # These are for spacing to make logos on an even level.
        st.write("")
        st.write("")
        st.write("")
        st.image("images/streamlit-logo.png", width=400)
    with top_right_column:
        st.image("images/kaggle.png", width=250)

    with st.expander("Link to Kaggle Dataset"):
        st.write(
            """
            Data source: https://www.kaggle.com/datasets/ruddygunawan/per-capita-income-by-county-2021-vs-education
            """
        )

    st.subheader("Counties With Highest Personal Income")

    st.write("---")

    left_column, right_column = st.columns([3, 1])
    with left_column:
        top_n_values = st.slider(label="Display top ___ values:",
                                 min_value=10,
                                 max_value=50,
                                 step=1)

    with right_column:
        year = st.selectbox("Select year:", options=[2019, 2020, 2021])
        formatted_year = f"per_capita_personal_income_{year}"

    n_largest_data = df.nlargest(n=top_n_values, columns=formatted_year)

    plost.bar_chart(
        title=formatted_year.title().replace("_", " "),
        data=n_largest_data,
        bar="county",
        value=formatted_year,
        direction='horizontal',
    )

    with st.expander("Display full pandas DataFrame"):
        st.dataframe(df)

    with st.expander("Display custom pandas DataFrame"):
        st.dataframe(n_largest_data)

    st.write("---")


if __name__ == "__main__":
    main()
