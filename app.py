import pandas as pd
import streamlit as st
import pickle
import numpy as np

# Load model (dictionary of songs and recommendations)
with open('final.pickle', 'rb') as f:
    song_recommendations = pickle.load(f)

# Extract the list of songs from the dictionary keys
loaded_data = list(song_recommendations.keys())

# Function to get recommendations
def get_recommendations(selected_song, recommendations_dict):
    return recommendations_dict.get(selected_song, [])

# Streamlit app
def main():
    st.title('Song Recommender')
    selected_song = st.selectbox('Select a song', loaded_data)
    if st.button('Show Recommendations'):
        recommendations = get_recommendations(selected_song, song_recommendations)
        st.subheader('Recommended Songs:')
        for i, song in enumerate(recommendations, 1):
            st.write(f'{i}. {song}')

if __name__ == "__main__":
    main()
