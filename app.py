import streamlit as st
import pickle
import pandas as pd
import requests


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=4e1c124d3272830345e8d1c4b674a96c'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    return 'https://image.tmdb.org/t/p/w92/'+data['poster_path']


def recommend_movie(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    sorted_list = sorted(list(enumerate(similarity[movie_index])), key=lambda x: x[1], reverse=True)
    recommended_movies = []
    recommended_movie_posters = []
    for i in sorted_list[1:6]:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters


st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'Select your favourite movie',
    (movies_list['title'].values))


if st.button('Recommend'):
    names, posters = recommend_movie(selected_movie)
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
