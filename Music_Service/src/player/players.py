from functools import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MusicArtist, MusicAlbum, MusicGenre, MusicPlayListTracks, MusicTrack, MusicLyrics, MusicPlayList, MusicFavourites

@api_view(['GET'])
def play_single_track(request):
    track_data = {}
    
    try:
        track_obj = MusicTrack.objects.filter(id=request.query_params['track']).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
        "genre_id")
        track_id = track_obj[0]['id']
        track_name = track_obj[0]['track_name']
        track_file = track_obj[0]['track_file']
        artist_id = track_obj[0]['artist_id']
        artist_name = MusicArtist.objects.filter(id=track_obj[0]['artist_id']).values('artist_name')[0]['artist_name']
        album_id = track_obj[0]['album_id']
        album_title = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_title')[0]['album_title']
        album_cover = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_cover')[0]['album_cover']
        genre_id = track_obj[0]['genre_id']
        genre_title = MusicGenre.objects.filter(id=track_obj[0]['genre_id']).values('genre_title')[0]['genre_title']
        try:
            lyrics_id = MusicLyrics.objects.filter(track_id=track_id).values('id')[0]['id']
            lyrics_detail = MusicLyrics.objects.filter(track_id=track_id).values('lyrics_detail')[0]['lyrics_detail']
        except:
            lyrics_id = None
            lyrics_detail = None
        
        for variable in ["track_id", "track_name", "track_file", "artist_id", "artist_name", "album_id",\
            "album_title", "album_cover", "genre_id", "genre_title", "lyrics_id", "lyrics_detail"]:
            track_data[variable] = eval(variable)

    except:
        track_data = None

    return Response({"TrackData": track_data})

@api_view(['GET'])
def play_album_tracks(request):
    album_data = {}
    tracks = {}

    try:
        album_obj = MusicAlbum.objects.filter(id=request.query_params['album']).values('id', 'album_title', 'album_cover', 'artist_id')
    
        album_id = album_obj[0]['id']
        album_title = album_obj[0]['album_title']
        album_cover = album_obj[0]['album_cover']
        artist_id = album_obj[0]['artist_id']
        artist_name = MusicArtist.objects.filter(id=artist_id).values('artist_name')[0]['artist_name']

        for variable in ["album_id", "album_title", "album_cover", "artist_id", "artist_name"]:
            album_data[variable] = eval(variable)

        track_obj = MusicTrack.objects.filter(album_id=album_id).values('id', 'track_name', 'track_file', 'genre_id')
        
        for i in range(len(track_obj)):
            track_data = {}

            track_id = track_obj[i]['id']
            track_name = track_obj[i]['track_name']
            track_file = track_obj[i]['track_file']
            genre_id = track_obj[i]['genre_id']
            genre_name = MusicGenre.objects.filter(id=genre_id).values('genre_title')[0]['genre_title']
            try:
                lyrics_id = MusicLyrics.objects.filter(track_id=track_id).values('id')[0]['id']
                lyrics_detail = MusicLyrics.objects.filter(track_id=track_id).values('lyrics_detail')[0]['lyrics_detail']
            except:
                lyrics_id = None
                lyrics_detail = None

            for variable in ["track_id", "track_name", "track_file", "genre_id", "genre_name", "lyrics_id", "lyrics_detail"]:
                track_data[variable] = eval(variable)

            tracks["Track_" + str(i)] = track_data

    except:
        album_data = None
        tracks = None

    album_data["Tracks"] = tracks

    return Response({"AlbumData": album_data})

@api_view(['GET'])
def play_playlist_tracks(request):
    playlist_data = {}
    tracks = {}

    try:
        playlist_obj = MusicPlayList.objects.filter(id=request.query_params['playlist']).values('id', 'playlist_name', 'user_id')
        playlist_id = playlist_obj[0]['id']
        playlist_name = playlist_obj[0]['playlist_name']
        user_id = playlist_obj[0]['user_id']

        for variable in ["playlist_id", "playlist_name", "user_id"]:
            playlist_data[variable] = eval(variable)

        playlist_tracks_obj = MusicPlayListTracks.objects.filter(playlist_id=playlist_id).values('playlist_id', 'track_id')

        for i in range(len(playlist_tracks_obj)):
            track_data = {}
        
            track_obj = MusicTrack.objects.filter(id=playlist_tracks_obj[i]['track_id']).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
                "genre_id")
            track_id = track_obj[0]['id']
            track_name = track_obj[0]['track_name']
            track_file = track_obj[0]['track_file']
            artist_id = track_obj[0]['artist_id']
            artist_name = MusicArtist.objects.filter(id=track_obj[0]['artist_id']).values('artist_name')[0]['artist_name']
            album_id = track_obj[0]['album_id']
            album_title = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_title')[0]['album_title']
            album_cover = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_cover')[0]['album_cover']
            genre_id = track_obj[0]['genre_id']
            genre_title = MusicGenre.objects.filter(id=track_obj[0]['genre_id']).values('genre_title')[0]['genre_title']
            try:
                lyrics_id = MusicLyrics.objects.filter(track_id=track_id).values('id')[0]['id']
                lyrics_detail = MusicLyrics.objects.filter(track_id=track_id).values('lyrics_detail')[0]['lyrics_detail']
            except:
                lyrics_id = None
                lyrics_detail = None

            for variable in ["track_id", "track_name", "track_file", "artist_id", "artist_name", "album_id",\
                "album_title", "album_cover", "genre_id", "genre_title", "lyrics_id", "lyrics_detail"]:
                track_data[variable] = eval(variable)
            
            tracks["Track_" + str(i)] = track_data

    except:
        playlist_data = None
        tracks = None

    playlist_data["Tracks"] = tracks

    return Response({"PlaylistData": playlist_data})

@api_view(['GET'])
def play_favourite_tracks(request):
    favourite_data = {}
    tracks = {}

    try:
        favourite_obj = MusicFavourites.objects.filter(user_id=request.query_params['user']).values('user_id', 'track_id')
        user_id = favourite_obj[0]['user_id']
        favourite_data["User"] = user_id

        for i in range(len(favourite_obj)):
            track_data = {}
        
            track_obj = MusicTrack.objects.filter(id=favourite_obj[i]['track_id']).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
                "genre_id")
            track_id = track_obj[0]['id']
            track_name = track_obj[0]['track_name']
            track_file = track_obj[0]['track_file']
            artist_id = track_obj[0]['artist_id']
            artist_name = MusicArtist.objects.filter(id=track_obj[0]['artist_id']).values('artist_name')[0]['artist_name']
            album_id = track_obj[0]['album_id']
            album_title = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_title')[0]['album_title']
            album_cover = MusicAlbum.objects.filter(id=track_obj[0]['album_id']).values('album_cover')[0]['album_cover']
            genre_id = track_obj[0]['genre_id']
            genre_title = MusicGenre.objects.filter(id=track_obj[0]['genre_id']).values('genre_title')[0]['genre_title']
            try:
                lyrics_id = MusicLyrics.objects.filter(track_id=track_id).values('id')[0]['id']
                lyrics_detail = MusicLyrics.objects.filter(track_id=track_id).values('lyrics_detail')[0]['lyrics_detail']
            except:
                lyrics_id = None
                lyrics_detail = None

            for variable in ["track_id", "track_name", "track_file", "artist_id", "artist_name", "album_id",\
                "album_title", "album_cover", "genre_id", "genre_title", "lyrics_id", "lyrics_detail"]:
                track_data[variable] = eval(variable)
            
            tracks["Track_" + str(i)] = track_data

    except:
        favourite_data = None
        tracks = None

    favourite_data["Tracks"] = tracks
        
    return Response({"FavouriteData": favourite_data})