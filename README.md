# movie-recommender-system

A basic content based movie recommender system which recommends movie using cosine similarity.
The pkl files were huge in size and so were not uploaded in git

## Datasets
The datasets were downloaded from kaggle https://www.kaggle.com/tmdb/tmdb-movie-metadata

## Implementation

There are 2 files: movie_recommender_system.ipynb, app.py

## movie_recommender_system.ipynb
In this file, a complete analysis, data cleaning and movie recommendations based on the selections were handled. 
The final dataframe and result were then pickled to be used by app.py

steps
1. download dataset and create dfs
2. merge them and analyse the columns to be considered for recommendation
3. Use nltk to stem the words, clean them
4. Use count vectorizer to convert them into vectors
5. calculate cosine similarity for each movie against each other
6. get the outputs as pickles

## app.py
This file contains code to deploy the id and movie recommendations in streamlit.
tmdb api's were used for displaying posters

#Reference:
The project was practiced by following the youtube video https://www.youtube.com/watch?v=1xtrIEwY_zY&list=PLKnIA16_RmvY5eP91BGPa0vXUYmIdtfPQ. My sincere thanks to Mr. Nitish Singh for simple and easy to understand solution

