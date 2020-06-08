import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import math
import os
import sys

sys.path.append('../')
try:
    from s1.settings import *
except ImportError:
    pass

def chart_tracks():
  """
  collect information about the song on global top 50 chart
  """
  client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)

  # connect to spotify
  spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


  id_list = [] # ids of songs from chart
  playlist_id = '37i9dQZEVXbMDoHDwVN2tF' # chart id
  playlist = spotify.playlist(playlist_id) # get 
  for item in playlist['tracks']['items']: 
    track = item['track']
    id_list.append(track['id'])

  features = spotify.audio_features(id_list)
  song_infos = []
  for f in features:
    tmp = {'acousticness': f['acousticness'], 'danceability': f['danceability'], 'energy': f['energy'], 
            'instrumentalness': f['instrumentalness'], 'key': f['key'], 'liveness': f['liveness'], 
            'loudness': f['loudness'], 'speechiness': f['speechiness'], 'tempo': f['tempo'], 
            'time_signature': f['time_signature'], 'valence': f['valence'], 'uri': f['uri']}
    song_infos.append(tmp)

  return song_infos

def search_info(name):
  client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)

  # make Spotify instance
  spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
  
  # seach artist whose name include 'name'
  try:
    information = spotify.search(q=['artist:'+name], limit=20, offset=0, type='track', market=None)
  except spotipy.oauth2.SpotifyOauthError as e:
    return e

  # track ids
  id_list = []
  artist_name = ""
  for track in information['tracks']['items']:
    # if artist name is the same as before, it's ok.
    if artist_name == "":
      artist_name = track['album']['artists'][0]['name']
      id_list.append(track['id'])
    elif artist_name == track['album']['artists'][0]['name']:
      id_list.append(track['id'])
    else:
      break
  # track features
  features = []
  try:
    features = spotify.audio_features(id_list)
  except TypeError as e:
    return e


  artist_info = {'artist_name': name,
                  'acousticness': 0.0,
                  'danceability': 0.0,
                  'energy': 0.0,
                  'instrumentalness': 0.0,
                  'key': 0.0,
                  'liveness': 0.0,
                  'loudness': 0.0,
                  'speechiness': 0.0,
                  'tempo': 0.0,
                  'time_signature': 0.0,
                  'valence': 0.0}

  for song_info in features:
    for key in artist_info.keys():
      if key != 'artist_name': 
        artist_info[key] += song_info[key]

  for key in artist_info.keys():
    if key != 'artist_name':
      artist_info[key] /= len(features)  

  return artist_info


def distance(artist_info, song_info):
  client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)

  # make Spotify instance
  spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  uri = ""
  dis = float('inf')
  category = ['acousticness', 'danceability', 'energy',
              'instrumentalness', 'key', 'liveness',
              'loudness', 'speechiness','tempo',
              'time_signature','valence']

  # make minmax scaler
  minmax = {'acousticness': [0, 0],
            'danceability': [0, 0],
            'energy': [0, 0],
            'instrumentalness': [0, 0],
            'key': [0, 0],
            'liveness': [0, 0],
            'loudness': [0, 0],
            'speechiness': [0, 0],
            'tempo': [0, 0],
            'time_signature': [0, 0],
            'valence': [0, 0]}

  for song in song_info:
    for cat in category:
      minmax[cat][0] = min(minmax[cat][0], song[cat])
      minmax[cat][1] = max(minmax[cat][1], song[cat])

  for cat in category:
    minmax[cat][0] = min(minmax[cat][0], artist_info[cat])
    minmax[cat][1] = max(minmax[cat][1], artist_info[cat])

  # calculate euclid distance and search the nearest song 
  for song in song_info:
    tmp = 0 
    for cat in category:
      # minmax scaler
      scaled_artist_info = (artist_info[cat]-minmax[cat][0])/(minmax[cat][1]-minmax[cat][0])
      scaled_song_info = (song[cat]-minmax[cat][0])/(minmax[cat][1]-minmax[cat][0])
      tmp += pow(scaled_artist_info - scaled_song_info, 2)
    tmp = math.sqrt(tmp)
    if tmp < dis:
      dis = tmp
      uri = song['uri']
      res = song

  # get track_id
  track_id = uri.split(':')[-1]
  # information about the track
  detected_song_info = spotify.track(track_id)
  # get song name
  song_name = detected_song_info['name']
  detected_song_info = detected_song_info['album']
  # get artist names
  artist_names = []
  for info in detected_song_info['artists']:
    artist_names.append(info['name'])
  artist_names = ', '.join(artist_names)
  # get track image
  image_uri = detected_song_info['images'][1]['url']

  return song_name, artist_names, image_uri, uri
