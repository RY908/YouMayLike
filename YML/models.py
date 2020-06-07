from django.db import models

# Create your models here.
class Information(models.Model):
  name = models.CharField(max_length=200)
  acousticness = models.IntegerField(default=0, null=True)
  danceability = models.IntegerField(default=0, null=True)
  energy = models.IntegerField(default=0, null=True)
  instrumentalness = models.IntegerField(default=0, null=True)
  key = models.IntegerField(default=0, null=True)
  liveness = models.IntegerField(default=0, null=True)
  loudness = models.IntegerField(default=0, null=True)
  speechiness = models.IntegerField(default=0, null=True)
  tempo = models.IntegerField(default=0, null=True)
  time_signature = models.IntegerField(default=0, null=True)
  valence = models.IntegerField(default=0, null=True)

  def __str__(self):
    return self.name