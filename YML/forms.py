from django import forms

class ArtistNamesForm(forms.Form):
  artist_name = forms.CharField(max_length=100)

  