import streamlit as st
from src.data import get_data


def main():
    st.title("Education Data")

    df = get_data()
    st.dataframe(df)

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
