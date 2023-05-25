import streamlit as st
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

movies_dict = pickle.load(open("movie_dict.pkl","rb"))
movies_matrix = pickle.load(open("movie_matrix.pkl","rb"))
movies = pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")
recommended_movies = []

def recommend(movie):
    query_index = int(np.where(movies.index == movie)[0])
    model_knn = NearestNeighbors(metric="cosine", algorithm="brute")
    model_knn.fit(movies_matrix)
    dist, indices = model_knn.kneighbors(movies.iloc[query_index,:].values.reshape(1, -1), n_neighbors=6)
    for i in range(1,len(dist.flatten())):
        recommended_movies.append(movies.index[indices.flatten()[i]])
    return recommended_movies


movie_selected = st.selectbox("Select A Movie", movies.index)

if st.button('Recommend'):
    recommend(movie_selected)
    for i in recommended_movies:
        st.write(i)
