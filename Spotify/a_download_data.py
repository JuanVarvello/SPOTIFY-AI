import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify Developer Account Credentials
cid = '' #MODIFY
secret = '' #MODIFY

# Number columns, used for the recommender
number_cols = ['valence', 'acousticness', 'danceability', 'duration_ms', 'energy',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


def convert_json_into_df(results, sp):
    """
    Converts the downloaded results json from Spotify into a DataFrame

    Parameters
    ----------
    results: dict
        Dictionary containing song information from a playlist
    sp: spotipy.client.Spotify
        Spotify client used to download information

    Returns
    -------
    final_df: pd.DataFrame
        Dataframe with features for every song in a playlist
    """
    # create a list of song ids
    ids = []

    for item in results['tracks']['items']:
        track = item['track']['id']
        ids.append(track)

    #Guardo de cada cancion los siguientes datos
    song_meta = {'id': [], 'album': [], 'name': [],
                 'artist': [], 'explicit': [], 'popularity': []}

    for song_id in ids:
        # get song's meta data
        meta = sp.track(song_id)


        song_meta['id'].append(meta['id'])
        song_meta['album'].append(meta['album'])
        song_meta['name'].append(meta['name'])
        song_meta['artist'].append(meta['artists'])
        song_meta['explicit'].append(meta['explicit'])
        song_meta['popularity'].append(meta['popularity'])        
        # COMPLETAR: Llenar las listas del diccionario con lo que ven en meta

 
    song_meta_df = pd.DataFrame(song_meta) # COMPLETAR: crear un df a partir del diccionario song_meta

    # check the song feature
    
    
    features = sp.audio_features(tracks= ids) # COMPLETAR: Buscar como traer los audio_features a partir de la lista id de song meta
    # change dictionary to dataframe
    
    
    features_df = pd.DataFrame(features) # COMPLETAR: crear un df a partir del diccionario features


    # combine two dataframe
    final_df = song_meta_df.merge(features_df) # COMPLETAR: mergear features_df y song_meta_df
    return final_df


def download_information(playlist_dict, sp):
    """
    Downloads information for all playlists in playlist_dict

    Parameters
    ----------
    playlist_dict: dict
        Dictionary of playlists that we want to download. Each key is the name of the playlist and the values represent
        the Spotify URI of that playlist
    sp: spotipy.client.Spotify
        Spotify client used to download information

    Returns
    -------
    df: pd.DataFrame
        Dataframe with info of all songs of all playlists that were downloaded
    """
    # Create an empty output dataframe
    df = pd.DataFrame()

    # Download information from every playlist
    for i in playlist_dict.keys():
        print(f"Downloading information for playlist {i}")
        df_aux = convert_json_into_df(results=sp.playlist(playlist_dict[i]), sp=sp)
        df_aux.loc[:, 'Playlist Name'] = i
        df = pd.concat([df, df_aux], ignore_index=True)
        print(f"Finished Downloading information for playlist {i}")
    return df


def main():
    # Connect to API
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Download results from Top 100 songs from each year
    my_playlists_id_dict = {
        1: 'spotify:playlist:37i9dQZEVXbMMy2roB9myp', #TOP 50 ARG
        2: 'spotify:playlist:4JEwJPzigydrndyf3nsBWg', #Fran Agiro
        3: 'spotify:playlist:37i9dQZF1DXe1ikyKZnRtc', #This is Duki
        4: 'spotify:playlist:37i9dQZF1DXbqDp0KLPlRg', #This is Maria Becerra
        5: 'spotify:playlist:37i9dQZF1DXe0nmj2KyjW1' #This is Tini
    }

    # Download information from my Top 100 songs by year
    df_my_songs = download_information(playlist_dict=my_playlists_id_dict, sp=sp)
    df_my_songs.to_csv('./3 - Spotify Recommender/inputs/my_playlists_info.csv', index=False, encoding='utf-8 sig')


if __name__ == '__main__':
    main()
