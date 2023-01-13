import streamlit as st
from src.data import get_data

import plost


def main():
    st.title("US Counties | Education vs. Per Capita Personal Income")

    df = get_data()

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

    req_data = df.nlargest(n=top_n_values, columns=formatted_year)

    plost.bar_chart(
        title=formatted_year.title().replace("_", " "),
        data=req_data,
        bar="county",
        value=formatted_year,
        direction='horizontal',
    )

    with st.expander("Display full pandas DataFrame"):
        st.dataframe(df)

    with st.expander("Display custom pandas DataFrame"):
        st.dataframe(req_data)

    st.write("---")


if __name__ == "__main__":
    main()
