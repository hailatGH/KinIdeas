from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Album, Genre, PlayListTracks, Track, Lyrics, PlayList, Favourites

@api_view()
def hello_world(request):
    track_data = {}
    
    track_obj = Track.objects.filter(id=request.GET['track']).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
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

    return Response(track_data)

# class SingleMusicPlayer(views):
#     def get_query(self):
#         t_id = self.request.query_params['id']
#         ar_id = Track.objects.filter(id=t_id).values('artist_id')[0]['artist_id']
#         al_id = Track.objects.filter(id=t_id).values('album_id')[0]['album_id']

#         querylist = (
#             {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
#             {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
#             {'queryset': Track.objects.filter(id=t_id), 'serializer_class': TrackSerializer},
#             {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
#         )

#         return querylist