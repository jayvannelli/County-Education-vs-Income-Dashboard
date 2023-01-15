import streamlit as st
from src.data import get_data


def main():
    st.title("Education Data by State")

    df = get_data()

    left_column, right_column = st.columns(2)
    with left_column:
        state_selection = st.selectbox("Select state:", options=df['state'].unique())
        state_df = df.loc[df['state'] == state_selection]

    with right_column:
        display_type = st.selectbox("Display value as:", options=["Percentage", "Numbers"])

    st.write("---")

    st.subheader(f"{state_selection} Associate Degree Data")

    if display_type == "Percentage":
        st.bar_chart(state_df, x="county", y="associate_degree_percentage_2016_2020")
    else:
        st.bar_chart(state_df, x="county", y="associate_degree_numbers_2016_2020")

    st.subheader(f"{state_selection} Bachelor Degree Data")

    if display_type == "Percentage":
        st.bar_chart(state_df, x="county", y="bachelor_degree_percentage_2015_2019")
    else:
        st.bar_chart(state_df, x="county", y="bachelor_degree_numbers_2016_2020")

    associate_degree_numbers = df['associate_degree_numbers_2016_2020']
    bachelor_degrees_numbers = df['bachelor_degree_numbers_2016_2020']

    associate_degree_percentage = df['associate_degree_percentage_2016_2020']
    bachelor_degree_percentage = df['bachelor_degree_percentage_2015_2019']

    st.subheader("Associate Degree")
    st.dataframe(associate_degree_numbers)
    st.dataframe(associate_degree_percentage)

    st.subheader("Bachelor Degree")
    st.dataframe(bachelor_degrees_numbers)
    st.dataframe(bachelor_degree_percentage)


if __name__ == "__main__":
    main()
