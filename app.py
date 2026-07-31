import streamlit as st
import numpy as np
import pickle
import pandas as pd
import requests
import os
from requests.adapters import HTTPAdapter
from requests.adapters import Retry




session = requests.Session()
retry = Retry(
    total =3,
    backoff_factor=1,
    status_forcelist=[429,500,502,503,504]
)
adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon= "🎬",
)


movies = pickle.load(open('movies.pkl','rb'))
similarity  = pickle.load(open('similarity.pkl','rb'))

print(movies["movie_id"].dtype)
print(movies["movie_id"].head())

C = movies['vote_average'].mean()
m = movies['vote_count'].quantile(0.90)
def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']

    return (v/(v+m)*R) + (m/(v+m)*C)

def recommend(movie):
    movie = movie.lower()

    if movie not in movies['title'].str.lower().values:
        return ["Movie not found!"]

    movie_index = movies[movies['title'].str.lower() == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )

    candidate_movies = []

    for i in movies_list[1:51]:
        candidate_movies.append({
            'index': i[0],
            'similarity': i[1]
        })

    indices = [movie['index'] for movie in candidate_movies]

    candidate_df = movies.iloc[indices].copy()

    candidate_df['similarity'] = [
        movie['similarity'] for movie in candidate_movies
    ]

    candidate_df['weighted_rating'] = candidate_df.apply(weighted_rating, axis=1)

    candidate_df['normalized_rating'] = (candidate_df['weighted_rating'] - candidate_df['weighted_rating'].min()) / (candidate_df['weighted_rating'].max() - candidate_df['weighted_rating'].min())

    similarity_weight = 0.7
    rating_weight = 0.3

    candidate_df['final_score'] = (similarity_weight * candidate_df['similarity']+ rating_weight * candidate_df['normalized_rating'])

    candidate_df = candidate_df.sort_values(by='final_score',ascending=False)

    return candidate_df[['movie_id','title']].head(5)


@st.cache_data

def fetch_movie_details(movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    print(row['movie_id'],row['title'])
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    try:
        response = session.get(url, timeout=10,headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            poster = f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            poster =  "https://via.placeholder.com/500x750?text=No+Poster"

        rating = data.get("vote_average","N/A")
        overview = data.get("overview","No overview available")
        return poster, rating, overview
    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return (
            "https://via.placeholder.com/500x750?text=No+Poster",
            "N/A",
            "Movie details could not be loaded."
        )
    print(data.get("status_code"))
    print(data.get("status_message"))



st.title("🎬 Hybrid Movie Recomendation System")
st.markdown("Discover movies similar to your favourites using a hybrid recommendation engine.")

selected_movie = st.selectbox("🔍 Search for a Movie",movies['title'].values,index=None,placeholder="Type or Select a movie")

if st.button("🎬 Recommend Movies",use_container_width=True):
    with st.spinner("Finding similar movies ....."):
        recommendations = recommend(selected_movie)

    st.divider()
    st.subheader("Recommend Movies")
    
    col1,col2,col3,col4,col5 = st.columns(5)
    columns = [col1,col2,col3,col4,col5]

    for i, (_,row) in enumerate(recommendations.iterrows()):
        poster, rating, overview = fetch_movie_details(row['movie_id'])

        with columns[i]:
            st.image(poster)
            st.write(row['title'])
            st.markdown(f"⭐ **IMDB:** {rating}")
            st.expander("📖 Overview").write(overview)

