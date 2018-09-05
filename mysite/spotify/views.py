from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TokenForm
from .models import Token
import requests
from . import artists
from . import albums 
from . import affinity
from . import user 

def login(request):
    return redirect("https://accounts.spotify.com/authorize?client_id=ecdb3082299245ddbda171266200cf56&redirect_uri=http://spotifycompanion.pythonanywhere.com/prompt/&scope=user-read-private user-read-email user-follow-read user-top-read&response_type=token&state=123")

def index(request):
    return render(request, "spotify/index.html")

def prompt(request):
    form = TokenForm()
    return render(request, "spotify/prompt.html", {"form": form})

def home(request):
    token = TokenForm(request.POST)
    if token.is_valid():
        access_token = token.cleaned_data["key"].split("#")[1].split("&")[0].split("=")[1]
        user_name, user_img = user.getUser(access_token) 
        artist_ids = artists.getArtists(access_token) 
        artists_info = [albums.getAlbums(access_token, artist_id) for artist_id in artist_ids]
        artists_info = sorted([data for data in artists_info if data], key = lambda x: x[2], reverse = True)
        top_tracks_s = affinity.getAffinity(access_token, "tracks", "short_term")
        top_tracks_m = affinity.getAffinity(access_token, "tracks", "medium_term")
        top_tracks_l = affinity.getAffinity(access_token, "tracks", "long_term")
        top_artists_s = affinity.getAffinity(access_token, "artists", "short_term")
        top_artists_m = affinity.getAffinity(access_token, "artists", "medium_term")
        top_artists_l = affinity.getAffinity(access_token, "artists", "long_term")
        dic = {"user_name": user_name, "user_img": user_img, "artists_info": artists_info, "top_tracks_s": top_tracks_s, "top_tracks_m": top_tracks_m, "top_tracks_l": top_tracks_l, "top_artists_s": top_artists_s, "top_artists_m": top_artists_m, "top_artists_l": top_artists_l}
        return render(request, "spotify/home.html", dic)
    return render(request, "spotify/home.html")
