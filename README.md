# Spotify AI Recommender

## Overview

The **Spotify AI Recommender** is a Python script that leverages the Spotify API to analyze the attributes of songs within a set of playlists and recommend the top 30 songs that are most similar to the input playlists. This tool is designed to help users discover new music that aligns with their existing music preferences.

## Prerequisites

Before using this script, you will need to ensure that you have the following prerequisites installed and set up:

1. **Python**: This script is written in Python, so you need to have Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Spotify Developer Account**: You must have a Spotify Developer Account to access the Spotify API. You can sign up for one at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

3. **Spotify API Credentials**: Once you have a Spotify Developer Account, create a Spotify App in the Developer Dashboard to obtain your API credentials (Client ID and Client Secret). You'll need these credentials to authenticate with the Spotify API.

4. **Python Libraries**: Install the necessary Python libraries using pip:

   ```bash
   pip install spotipy numpy
   ```

## Getting Started

1. Clone or download this repository to your local machine.

2. Open the `a_download_data.py` file and replace the placeholders with your Spotify API credentials:

   ```python
   cid= 'your_client_id_here'
   secret = 'your_client_secret_here'
   ```
   
3. Modify the playlist URIs:
   ```python
   my_playlists_id_dict = {
        1: 'spotify:playlist: #COMPLETE', 
        2: 'spotify:playlist: #COMPLETE', 
        3: 'spotify:playlist: #COMPLETE', 
    }
   ```
   
4. Save the `a_download_data.py` file with your credentials.

5. Run the scripts:

   ```bash
   python spotify_ai_recommender.py
   python spotify_ai_recommender.py
   ```

## Usage

1. When you run the script, it will prompt you to authenticate with your Spotify account. Follow the provided link and grant access to the script.

2. After authentication, you will be asked to provide the URLs of the playlists you want to analyze. You can find the playlist URL by right-clicking on a playlist in the Spotify app and selecting "Copy Playlist Link."

3. Enter the playlist URLs one by one. The script will retrieve the song attributes for each playlist.

4. Once the analysis is complete, you can provide a list of songs to get song recommendations based on the analyzed playlists.

5. The script will return the top 30 songs that are most similar to the input playlists, sorted by similarity score.

## Additional Notes

- The similarity between playlists is calculated based on the audio attributes of the songs, including features like danceability, energy, acousticness, and more.

- The script uses the Spotipy library to interact with the Spotify API. Make sure to respect Spotify's terms of use and API rate limits.

- You can customize the number of recommended songs and the weighting of audio features in the `spotify_ai_recommender.py` script.

## Disclaimer

This script is intended for educational purposes and personal use. Please respect Spotify's terms of service and API usage guidelines. Use this script responsibly and consider the implications of data privacy and copyright when accessing and using Spotify data.
