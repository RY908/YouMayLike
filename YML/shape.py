from .models import Information

def shape_data(artist_info=None, data=None, from_data=False):
  """
  get infromation form database or save data to database.

  Parameters
  ----------
  artist_info: dict
    artist information by spotify
  data: class
    artist information saved on database
  from_data: bool
    when retrieving data from database, set True
  """
  if from_data:
    artist_info = {'artist_name': data.name,
                  'acousticness': data.acousticness,
                  'danceability': data.danceability,
                  'energy': data.energy,
                  'instrumentalness': data.instrumentalness,
                  'key': data.key,
                  'liveness': data.liveness,
                  'loudness': data.loudness,
                  'speechiness': data.speechiness,
                  'tempo': data.tempo,
                  'time_signature': data.time_signature,
                  'valence': data.valence}

    return artist_info
  else:
    artist_data = Information(name=artist_info['artist_name'],
                                acousticness=artist_info['acousticness'],
                                danceability=artist_info['danceability'],
                                energy=artist_info['energy'],
                                instrumentalness=artist_info['instrumentalness'],
                                key=artist_info['key'],
                                liveness=artist_info['liveness'],
                                loudness=artist_info['loudness'],
                                speechiness=artist_info['speechiness'],
                                tempo=artist_info['tempo'],
                                time_signature=artist_info['time_signature'],
                                valence=artist_info['valence']
                                )
    artist_data.save()
    return