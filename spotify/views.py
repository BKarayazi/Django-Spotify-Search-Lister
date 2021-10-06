from django.shortcuts import render
from django.http import HttpResponseRedirect
from .credentials import CLIENT_ID, CLIENT_SECRET
import requests
import json
import random

# Create your views here.
def get_genres():
    with open("genres.json", "r") as read_file:
        genres = json.load(read_file)
    return genres

def get_access_token():
    data = {
    'grant_type' : 'client_credentials',
    'client_id' : CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    }
    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data)
    access_token = response.json()['access_token']
    return access_token


def get_songs(artist,access_token):
    query = {
     'type':'track',
     'q':f'artist:{artist}',
     'access_token': access_token,
     'token_type': 'Bearer',
     'limit':10,
     }
    response = requests.get('https://api.spotify.com/v1/search', params=query)
    return response.json()['tracks']['items']


def list_songs(request,reqGenre):
    try:
        genres= get_genres()
        artist = genres[reqGenre][random.randrange(0, len(genres[reqGenre]) )]
        access_token = get_access_token()
        songs=get_songs(artist,access_token)
        return render(request, 'song-table.html', {'songs': songs})
    except:
        return home(request)

def home(request):
        return render(request, 'hello.html')