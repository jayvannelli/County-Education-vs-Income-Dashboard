import streamlit as st
from src.data import get_data


def main():
    st.title("US Counties | Education vs. Per Capita Personal Income")

    df = get_data()
    st.dataframe(df)
    state_selection = st.selectbox(label="Select state:",
                                   options=df['state'].unique())

    state_df = df.loc[df['state'] == state_selection]
    st.dataframe(state_df)

    st.bar_chart(state_df, x="county", y="per_capita_personal_income_2019")

    multiple_state_selection = st.multiselect(label="Select states:",
                                              options=df['state'].unique(),
                                              default=df['state'].unique()[:5])


if __name__ == "__main__":
    main()
