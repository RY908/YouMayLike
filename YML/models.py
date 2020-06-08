from django.db import models

# Create your models here.
class Information(models.Model):
  """
  Stores infromation about an artist.

  Attributes
  ----------
  name: char
    artist name
  acousticness: float
    acousticness of the artist
  danceability: float
    danceability of the artist
  energy: float
    energy of the artist
  instrumentalness: float
    instrumentalness of the artist
  key: float
    key of the artist
  liveness: float
    liveness of the artist
  loudness: float
    loudness of the artist
  speechiness: float
    speechiness of the artist
  tempo: float
    tempo of the artist
  time_signature: float
    time signature of the artist
  valence: float
    valence of the artist
  """
  name = models.CharField(max_length=200)
  acousticness = models.FloatField(default=0, null=True)
  danceability = models.FloatField(default=0, null=True)
  energy = models.FloatField(default=0, null=True)
  instrumentalness = models.FloatField(default=0, null=True)
  key = models.FloatField(default=0, null=True)
  liveness = models.FloatField(default=0, null=True)
  loudness = models.FloatField(default=0, null=True)
  speechiness = models.FloatField(default=0, null=True)
  tempo = models.FloatField(default=0, null=True)
  time_signature = models.FloatField(default=0, null=True)
  valence = models.FloatField(default=0, null=True)

  def __str__(self):
    return self.name