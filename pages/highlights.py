import streamlit as st
from src.data import get_data

import plost


def main():
    st.title("Highlights")

    df = get_data()

    st.subheader("Counties with Highest Per Capital Personal Income (Top 5)")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("2019")
        plost.bar_chart(
            data=df.nlargest(n=5, columns="per_capita_personal_income_2019"),
            bar="county",
            value="per_capita_personal_income_2019",
        )

    with middle_column:
        st.subheader("2020")
        plost.bar_chart(
            data=df.nlargest(n=5, columns="per_capita_personal_income_2020"),
            bar="county",
            value="per_capita_personal_income_2020",
        )

    with right_column:
        st.subheader("2021")
        plost.bar_chart(
            data=df.nlargest(n=5, columns="per_capita_personal_income_2021"),
            bar="county",
            value="per_capita_personal_income_2021",
        )

    st.write("---")

    biggest_increase_tab, biggest_decrease_tab = st.tabs([
        "Biggest YoY Increase", "Biggest YoY Decrease"
    ])

    df['income_delta_2020'] = df["per_capita_personal_income_2020"] - df["per_capita_personal_income_2019"]
    df['income_delta_2021'] = df["per_capita_personal_income_2021"] - df["per_capita_personal_income_2020"]

    df['change_income_2020'] = (df['income_delta_2020'] / df['per_capita_personal_income_2019']) * 100
    df['change_income_2021'] = (df['income_delta_2021'] / df['per_capita_personal_income_2020']) * 100

    with biggest_increase_tab:
        st.title("Highest YoY Percentage Increase in Per Capita Personal Income")

        plost.bar_chart(
            title="Top 30 Counties with Highest % Increase from 2019-2020",
            data=df.nlargest(n=30, columns="change_income_2020"),
            bar="county",
            value="change_income_2020",
        )

        plost.bar_chart(
            title="Top 30 Counties with Highest % Increase from 2020-2021",
            data=df.nlargest(n=30, columns="change_income_2021"),
            bar="county",
            value="change_income_2021",
        )

    with biggest_decrease_tab:
        st.title("Highest YoY Percentage Decrease in Per Capita Personal Income")

        plost.bar_chart(
            title="Top 30 Counties with Highest % Decrease from 2019-2020",
            data=df.nsmallest(n=30, columns="change_income_2020"),
            bar="county",
            value="change_income_2020",
        )

        plost.bar_chart(
            title="Top 30 Counties with Highest % Decrease from 2020-2021",
            data=df.nsmallest(n=30, columns="change_income_2021"),
            bar="county",
            value="change_income_2021",
        )


if __name__ == "__main__":
    main()
