from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib import messages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from .forms import ArtistNamesForm

from .models import Information
from .search_info import search_info, chart_tracks, distance 

def index(request):
  context = {'form': ArtistNamesForm()}
  return render(request, 'YML/index.html', context)
  #return HttpResponse("Hello, world. You're at the polls index.")

def NameForm(request):
  form = ArtistNamesForm(request.POST)
  if form.is_valid():
    name = form.cleaned_data['artist_name']
    return HttpResponseRedirect(reverse('YML:spotify', args=(name,)))
  print("errro")
  form.add_error(None, "Please try again.")
  return render(request, 'YML/index.html', {'form': form})
  """
  if request.method == 'POST':
    name = request.POST['artist_name']
    return HttpResponseRedirect(reverse('YML:spotify', args=(name,)))
  else:
    context = {'form1': ArtistNamesForm(), 'error_message': [], 'name':""}
    return render(request, 'YML/index.html', context)
  """

def spotify(request, name):
  try:
    artist_info = search_info(name)
  except:
    messages.error(request,'There is no artist named {}. Please try again.'.format(name))
    return HttpResponseRedirect(reverse('YML:index', args=()))
  try:
    song_info = chart_tracks()
  except:
    messages.error(request, 'There is an error processing chart tracks. Please try again.')
    return HttpResponseRedirect(reverse('YML:index', args=()))
  try:
    song_name, artist_names, image_uri, uri = distance(artist_info, song_info)
  except:
    messages.error(request, "Couldn't find a song you may like. Please try with other artist.")
    return HttpResponseRedirect(reverse('YML:index', args=()))

  context = {
    'song_name': song_name,
    'artist_names': artist_names,
    'image_uri': image_uri,
    'uri': uri,
  }
  return render(request, 'YML/spotify.html', context)
