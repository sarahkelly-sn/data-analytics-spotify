# Altere os itens ########### por seus dados particulares.

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
import time

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="###########",
    client_secret="###########",
    redirect_uri="http://###########",
    scope="user-library-read user-top-read user-read-recently-played playlist-read-private"
))

user_data = sp.current_user()
user_id = user_data['id']
print("Usuário autenticado:", user_data['display_name'])

top_tracks = []
limit = 50
offset = 0
total_tracks = 0

print("\nColetando músicas do usuário...")

response = sp.current_user_top_tracks(limit=limit, offset=0)
total_tracks = response['total']
top_tracks.extend(response['items'])
print(f"Dados coletados: {len(top_tracks)}/{total_tracks} | Total até agora: {len(top_tracks)} faixas")

start_time = time.time()
while True:
    response = sp.current_user_top_tracks(limit=limit, offset=offset)
    top_tracks.extend(response['items'])
    offset += limit

    elapsed_time = time.time() - start_time
    print(f"Dados coletados: {len(top_tracks)}/{total_tracks} | Total até agora: {len(top_tracks)} faixas | Tempo de execução total: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")

    if len(response['items']) < limit:  
        break

print(f"Total de faixas coletadas: {len(top_tracks)}\n")

playlists = []
offset = 0
total_playlists = 0

print("Coletando playlists do usuário...")

response = sp.current_user_playlists(limit=limit, offset=0)
total_playlists = response['total']
print(f"Total de playlists disponíveis: {total_playlists}") 
playlists.extend(response['items'])
print(f"Dados coletados: {len(playlists)}/{total_playlists} | Total até agora: {len(playlists)} playlists")

while True:
    response = sp.current_user_playlists(limit=limit, offset=offset)
    playlists.extend(response['items'])
    offset += limit

    elapsed_time = time.time() - start_time
    print(f"Dados coletados: {len(playlists)}/{total_playlists} | Total até agora: {len(playlists)} playlists | Tempo de execução total: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")

    if len(response['items']) < limit:  
        break


print(f"Total de playlists coletadas: {len(playlists)}\n")

df_user = pd.DataFrame([{
    'id_usuario': user_data['id'],
    'nome': user_data['display_name'],
    'email': user_data.get('email', None),
    'pais': user_data.get('country', None),
    'tipo_usuario': user_data.get('product', None),
    'seguidores': user_data['followers']['total'],
    'seguindo': user_data.get('following', None), 
    'url_perfil': user_data['external_urls']['spotify'], 
    'imagem_url': user_data['images'][0]['url'] if user_data['images'] else None,
    'data_coleta': pd.Timestamp.now(),
    'data_nascimento': user_data.get('birthdate', None),  
    'genero': user_data.get('gender', None),  
    'numero_playlists': user_data.get('playlists', None),  
    'qualidade_streaming': user_data.get('playback_quality', None), 
    'generos_favoritos': None  
}])

print(f"DataFrame de usuários criado com {df_user.shape[0]} registros.\n")

df_tracks = pd.DataFrame([{
    'id_musica': track['id'],
    'nome_musica': track['name'],
    'id_album': track['album']['id'],
    'id_artista': track['artists'][0]['id'],
    'popularidade': track['popularity'],
    'url_capa': track['album']['images'][0]['url'] if track['album']['images'] else None,
    'data_primeira_reproducao': track.get('first_release_date', None),
    'data_ultima_reproducao': track.get('last_played_date', None),
    'contagem_reproducao': 1,
    'duracao': track['duration_ms'],
    'data_coleta': pd.Timestamp.now(),
    'hora_ultima_reproducao': None
} for track in top_tracks])

print(f"DataFrame de faixas criado com {df_tracks.shape[0]} registros.\n")

df_playlists = pd.DataFrame([{
    'id_playlist': playlist['id'],
    'nome_playlist': playlist['name'],
    'total_musicas': playlist['tracks']['total'],
    'data_criacao': playlist.get('created', None), 
    'data_ultima_atualizacao': playlist.get('updated', None),  
    'id_usuario': user_id,
    'descricao': playlist.get('description', None),
    'tipo_playlist': 'pública' if playlist['public'] else 'privada',
    'data_coleta': pd.Timestamp.now()
} for playlist in playlists])

print(f"DataFrame de playlists criado com {df_playlists.shape[0]} registros.\n")

df_playback_history = pd.DataFrame([{
    'id_reproducao': f"replay_{i}",
    'id_usuario': user_id,
    'id_musica': track['id'],
    'data_reproducao': pd.Timestamp.now().date(),
    'hora_reproducao': pd.Timestamp.now().time(),
    'duracao': track['duration_ms'],
    'tipo_reproducao': 'normal'
} for i, track in enumerate(top_tracks)])

print(f"DataFrame de histórico de reprodução criado com {df_playback_history.shape[0]} registros.\n")

output_dir = r'C:\###########",'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df_user.to_csv(os.path.join(output_dir, 'usuarios.csv'), index=False)
df_tracks.to_csv(os.path.join(output_dir, 'faixas.csv'), index=False)
df_playlists.to_csv(os.path.join(output_dir, 'playlists.csv'), index=False)
df_playback_history.to_csv(os.path.join(output_dir, 'historico_reproducao.csv'), index=False)

print("Dados exportados com sucesso para a pasta:", output_dir)
