import streamlit as st
from src.data import get_data


def main():
    st.title("US Counties | Education vs. Per Capita Personal Income")

    df = get_data()
    st.dataframe(df)


if __name__ == "__main__":
    main()
