import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

numeric_variables = ['danceability', 'energy', 'key', 'loudness', 'acousticness', 'instrumentalness', 'liveness', 'valence']

if __name__ == '__main__':
    # Leer dataframe de sus canciones
    mis_canciones = pd.read_csv("/workspaces/Taller Coding/Spotify/inputs/my_playlists_info.csv", sep=',') #/3 - Spotify Recommender
    
    # Leer dataframe compartido
    df = pd.read_csv("/workspaces/Taller Coding/Spotify/inputs/kaggle_spotify_data/data.csv", sep = ',')
    
    # Crear un diccionario que tenga el promedio de cada variable en numeric_variables viendo sus canciones
    promedios = dict()
    
    for item in numeric_variables:
        promedios[item] = np.mean(mis_canciones[item])

    # Implementar una funcion que calcule la distancia de cada cancion en el df compartido contra el diccionario
    df.loc[:, 'Distance'] = 0
    
    for item in numeric_variables:
        df['Distance'] = df['Distance'] + abs(((df[item] - promedios[item])**2)/promedios[item])
    
    df['Distance'] = np.sqrt(df['Distance'])
    
    # Ver que 30 canciones tienen la menor distancia
    df = df.sort_values(by=['Distance'], ascending=True).reset_index()
    print(df)
    
    # Guardar el resultado
    res = df.iloc[:30]
    print(res)
    
    pass
