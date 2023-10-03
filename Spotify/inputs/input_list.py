import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Define your Spotify API credentials
os.environ["SPOTIPY_CLIENT_ID"] = "your_client_id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "your_client_secret"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"  # Change to your redirect URI

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-read-private"))

def get_playlist_attributes(playlist_uri):
    try:
        # Extract playlist ID from URI
        playlist_id = playlist_uri.split(":")[-1]

        # Get playlist details
        playlist = sp.playlist_tracks(playlist_id)

        # Create lists to store song attributes
        song_names = []
        song_artists = []
        song_uris = []
        danceability = []
        energy = []
        acousticness = []
        instrumentalness = []
        valence = []

        # Loop through each track in the playlist
        for track in playlist["items"]:
            song = track["track"]
            song_names.append(song["name"])
            artists = ", ".join([artist["name"] for artist in song["artists"]])
            song_artists.append(artists)
            song_uris.append(song["uri"])

            # Get audio features for the track
            audio_features = sp.audio_features(song["uri"])[0]
            danceability.append(audio_features["danceability"])
            energy.append(audio_features["energy"])
            acousticness.append(audio_features["acousticness"])
            instrumentalness.append(audio_features["instrumentalness"])
            valence.append(audio_features["valence"])

        # Create a DataFrame to store song attributes
        df = pd.DataFrame({
            "Song Name": song_names,
            "Artist(s)": song_artists,
            "Spotify URI": song_uris,
            "Danceability": danceability,
            "Energy": energy,
            "Acousticness": acousticness,
            "Instrumentalness": instrumentalness,
            "Valence": valence,
        })

        return df

    except Exception as e:
        print("Error:", str(e))
        return None

def main():
    playlist_uri = input("Enter a Spotify Playlist URI: ")
    df = get_playlist_attributes(playlist_uri)

    if df is not None:
        output_file = "playlist_attributes.csv"
        df.to_csv(output_file, index=False)
        print(f"Song attributes saved to {output_file}")

if __name__ == "__main__":
    main()
