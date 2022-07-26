from rest_framework.decorators import api_view
from rest_framework.response import Response
from slugify import slugify

from .models import Artist, Album, Genre, PlayListTracks, Track, Lyrics, PlayList, Favourites

@api_view(['GET'])
def play_single_track(request):
    track_data = {}
    
    track_obj = Track.objects.filter(id=request.query_params['track']).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
        "genre_id")
    track_id = track_obj[0]['id']
    track_name = track_obj[0]['track_name']
    track_file = track_obj[0]['track_file']
    artist_id = track_obj[0]['artist_id']
    artist_name = Artist.objects.filter(id=track_obj[0]['artist_id']).values('artist_name')[0]['artist_name']
    album_id = track_obj[0]['album_id']
    album_title = Album.objects.filter(id=track_obj[0]['album_id']).values('album_title')[0]['album_title']
    album_cover = Album.objects.filter(id=track_obj[0]['album_id']).values('album_cover')[0]['album_cover']
    genre_id = track_obj[0]['genre_id']
    genre_title = Genre.objects.filter(id=track_obj[0]['genre_id']).values('genre_title')[0]['genre_title']
    lyrics_id = Lyrics.objects.filter(track_id=track_id).values('id')[0]['id']
    lyrics_detail = Lyrics.objects.filter(track_id=track_id).values('lyrics_detail')[0]['lyrics_detail']

    for variable in ["track_id", "track_name", "track_file", "artist_id", "artist_name", "album_id",\
        "album_title", "album_cover", "genre_id", "genre_title", "lyrics_id", "lyrics_detail"]:
        track_data[variable] = eval(variable)

    return Response({"Track Data": track_data})

@api_view(['GET'])
def play_album_tracks(request):
    album_data = {}
    tracks = {}

    album_obj = Album.objects.filter(id=request.query_params['album']).values('id', 'album_title', 'album_cover', 'artist_id')
    album_id = album_obj[0]['id']
    album_title = album_obj[0]['album_title']
    album_cover = album_obj[0]['album_cover']
    artist_id = album_obj[0]['artist_id']
    artist_name = Artist.objects.filter(id=artist_id).values('artist_name')[0]['artist_name']

    for variable in ["album_id", "album_title", "album_cover", "artist_id", "artist_name"]:
        album_data[variable] = eval(variable)

    track_obj = Track.objects.filter(album_id=album_obj[0]['id']).values('id', 'track_name', 'track_file', 'genre_id')
    
    for i in range(len(track_obj)):
        track_data = {}

        track_id = track_obj[i]['id']
        track_name = track_obj[i]['track_name']
        track_file = track_obj[i]['track_file']
        genre_id = track_obj[i]['genre_id']
        genre_name = Genre.objects.filter(id=genre_id).values('genre_title')[0]['genre_title']
        lyrics_id = Lyrics.objects.filter(id=track_id).values('id')[0]['id']
        lyrics_detail = Lyrics.objects.filter(id=track_id).values('lyrics_detail')[0]['lyrics_detail']

        for variable in ["track_id", "track_name", "track_file", "genre_id", "genre_name", "lyrics_id", "lyrics_detail"]:
            track_data[variable] = eval(variable)

        for i in range(len(track_obj)):
            tracks[i] = track_data

    return Response({"Album Data": album_data, "Tracks": tracks})

@api_view(['GET'])
def play_playlist_tracks(request):
   
    return Response({"Playlist Data": "Works"})

@api_view(['GET'])
def play_favourite_tracks(request):
    favourite_data = {}
    favourite_obj = Favourites.objects.filter(user_id=request.query_params['user']).values('id', 'user_id', 'track_id')
   
    return Response({"Favourite Data": favourite_data})