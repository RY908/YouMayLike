from django.urls import path

from . import views

app_name = 'YML'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /YML/artist_name/results/
    path('<str:name>/results/', views.spotify, name='spotify'),
    path('form/', views.NameForm, name='form'),
]