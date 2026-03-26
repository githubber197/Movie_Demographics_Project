import streamlit as st
from queries.queries import get_genres_by_age_group, get_countries_by_genre, get_avg_rating_by_age_group

st.title("MovieLens Dashboard")
st.header("Top Genres by Age Group")
age_group = st.selectbox("Select Age Group", options=["13-17","18-25", "26-35", "36-45", "46-60", "60+"])
df = get_genres_by_age_group(age_group)
st.bar_chart(df.set_index("genre")["count"])

st.header("Top Countries by Genre")
genre = st.selectbox("Select Genre", options=["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"])
df = get_countries_by_genre(genre)
st.bar_chart(df.set_index("country")["count"])

st.header("Average Movie Rating by Age Group")
df = get_avg_rating_by_age_group()
st.bar_chart(df.set_index("age_group")["average_rating"])