from django.urls import path

from . import views

app_name = 'YML'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /YML/song_name/results/
    path('<str:name>/results/', views.spotify, name='spotify'),
    #path('result/', views.spotify, name='result'),
    path('form/', views.NameForm, name='form'),
]