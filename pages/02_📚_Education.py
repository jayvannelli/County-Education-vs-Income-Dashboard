import plost
import streamlit as st
from src.data import get_data


def main():
    st.title("Education Data by State")

    df = get_data()

    left_column, right_column = st.columns(2)
    with left_column:
        state_selection = st.selectbox("Select state:", options=df['state'].sort_values().unique())
        state_df = df.loc[df['state'] == state_selection]

    with right_column:
        display_type = st.selectbox("Display value as:", options=["Percentage", "Numbers"])
        _subheader_display_type = '%' if display_type == 'Percentage' else 'Quantity'

    st.write("---")

    st.subheader(f"Associate Degree by County ({_subheader_display_type})")

    if display_type == "Percentage":
        st.bar_chart(state_df, x="county", y="associate_degree_percentage_2016_2020")
    else:
        st.bar_chart(state_df, x="county", y="associate_degree_numbers_2016_2020")

    st.subheader(f"Bachelor Degree by County ({_subheader_display_type})")

    if display_type == "Percentage":
        st.bar_chart(state_df, x="county", y="bachelor_degree_percentage_2015_2019")
    else:
        st.bar_chart(state_df, x="county", y="bachelor_degree_numbers_2016_2020")


if __name__ == "__main__":
    main()
