from django.test import TestCase
from .models import Information 
# Create your tests here.

# https://nwpct1.hatenablog.com/entry/how-to-write-unittest-on-django
class InformationAssertTest(TestCase):
  def assertInformationModel(self, actual_info, name, acousticness, 
                            danceability, energy, instrumentalness, 
                            key, liveness, loudness, speechiness, 
                            tempo, time_signature, valence):
    self.assertEqual(actual_info.name, name)
    self.assertEqual(actual_info.acousticness, acousticness)
    self.assertEqual(actual_info.danceability, danceability)
    self.assertEqual(actual_info.energy, energy)
    self.assertEqual(actual_info.instrumentalness, instrumentalness)
    self.assertEqual(actual_info.key, key)
    self.assertEqual(actual_info.liveness, loudness)
    self.assertEqual(actual_info.loudness, loudness)
    self.assertEqual(actual_info.speechiness, speechiness)
    self.assertEqual(actual_info.tempo, tempo)
    self.assertEqual(actual_info.time_signature, time_signature)
    self.assertEqual(actual_info.valence, valence)

class InformationModelTest(TestCase):
  def test_is_empty(self):
    saved_info = Information.objects.all()
    self.assertEqual(saved_info.count(), 0)

  def test_one(self):
    Information.objects.create(name='test')
    self.assertEqual(1, len(Information.objects.all()))

  def test_two(self):
    Information.objects.create(name='test')
    self.assertEqual(1, len(Information.objects.all()))

  def create_info_and_save(self, name=None, acousticness=None, 
                            danceability=None, energy=None, instrumentalness=None, 
                            key=None, liveness=None, loudness=None, 
                            speechiness=None, tempo=None, time_signature=None,
                            valence=None):
    info = Information()
    if name is not None:
      info.name = name
    if acousticness is not None:
      info.acousticness = acousticness
    if danceability is not None:
      info.danceability = danceability
    if energy is not None:
      info.energy = energy
    if instrumentalness is not None:
      info.instrumentalness = instrumentalness
    if key is not None:
      info.key = key
    if liveness is not None:
      info.liveness = liveness
    if loudness is not None:
      info.loudness = loudness
    if speechiness is not None:
      info.speechiness = speechiness
    if tempo is not None:
      info.tempo = tempo
    if time_signature is not None:
      info.time_signature = time_signature
    if valence is not None:
      info.valence = valence
    info.save()

  def test_saving_and_retrieving_info(self):
    name = 'test'
    acousticness = 1.0
    danceability = 1.0
    energy = 1.0
    instrumentalness = 1.0
    key = 1.0
    liveness = 1.0
    loudness = 1.0
    speechiness = 1.0
    tempo = 1.0
    time_signature = 1.0
    valence = 1.0  
    self.create_info_and_save(name, acousticness, danceability,
                              energy, instrumentalness, key, liveness,
                              loudness, speechiness, tempo,
                              time_signature, valence)

    saved_info = Information.objects.all()
    actual_info = saved_info[0]
    """
    for category in expected_info.keys():
      with self.subTest(name=category, expected=expected_info[category]):
        self.assertEqual(actual_info.category, expected_info[category])
    """
    self.assertEqual(actual_info.name, name)
    self.assertEqual(actual_info.acousticness, acousticness)
    self.assertEqual(actual_info.danceability, danceability)
    self.assertEqual(actual_info.energy, energy)
    self.assertEqual(actual_info.instrumentalness, instrumentalness)
    self.assertEqual(actual_info.key, key)
    self.assertEqual(actual_info.liveness, loudness)
    self.assertEqual(actual_info.loudness, loudness)
    self.assertEqual(actual_info.speechiness, speechiness)
    self.assertEqual(actual_info.tempo, tempo)
    self.assertEqual(actual_info.time_signature, time_signature)
    self.assertEqual(actual_info.valence, valence)
    

