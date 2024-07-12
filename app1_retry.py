import streamlit as st
import pandas as pd
import requests
from data_loader import download_and_load_pkl

# Dropbox direct links to the files
movies_dict_url = 'https://dl.dropboxusercontent.com/scl/fi/o59q8xhgybblpyttotqvu/similarity.pkl?rlkey=npdkocmybk9zyv80naew1kalc&st=nouj8wlt&dl=0'
similarity_url = 'https://dl.dropboxusercontent.com/scl/fi/nl6mmkelvfl1i9pwqxinq/movies.pkl?rlkey=tjpa5j72efoduwiw4op2m3zuc&st=uv3w081h&dl=0'

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=95e46887ed550a125465fcfa804d2ada&language=en-US')
    print(movie_id)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data from Dropbox
movies_dict = download_and_load_pkl(movies_dict_url)
similarity = download_and_load_pkl(similarity_url)

if movies_dict is not None and similarity is not None:
    movies = pd.DataFrame(movies_dict)

    st.title('Movie Recommender System')

    selected_movie_name = st.selectbox('How would you?', movies['title'].values)

    if st.button('Recommend'):
        names, posters = recommend(selected_movie_name)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])
else:
    st.error("Failed to load data from Dropbox")
