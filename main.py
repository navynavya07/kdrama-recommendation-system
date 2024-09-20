import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv("D:\PyCharm Projects\kdrama.csv")
    return df

df = load_data()


def filter_kdramas(df, genre, actor, year):
    filtered_df = df[df['Genre'].str.contains(genre, case=False, na=False)]

    if actor:
        filtered_df = filtered_df[filtered_df['Actors'].str.contains(actor, case=False, na=False)]

    if year:
        filtered_df = filtered_df[filtered_df['Year'] == int(year)]

        # Sort by Rating in descending order
    filtered_df = filtered_df.sort_values(by='Rating', ascending=False)

    return filtered_df



st.title("K-Drama Recommendation System")

genre = st.text_input("Enter your preferred genre (e.g., Romance, Action, Comedy):")
actor = st.text_input("Enter your preferred actor/actress (or leave blank if no preference):")
year = st.text_input("Enter the release year (or leave blank if no preference):")

if st.button('Get Recommendations'):
    if genre:
        recommendations = filter_kdramas(df, genre, actor, year)

        if recommendations.empty:
            st.write("No K-Dramas found with the given preferences.")
        else:
            st.write("Recommended K-Dramas Based on the ratings (high to low):")
            st.dataframe(recommendations[['Drama Name', 'Genre', 'Year', 'Actors']])
    else:
        st.write("Please enter at least a genre.")
