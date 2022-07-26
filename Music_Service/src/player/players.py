from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Album, Genre, PlayListTracks, Track, Lyrics, PlayList, Favourites

@api_view()
def hello_world(request):
    track_id = request.GET['track']
    track_data = Track.objects.filter(id=track_id).values('id', 'track_name', 'track_file', 'artist_id', 'album_id', \
        "genre_id")

    print()
    artist_name = Artist.objects.filter(id=track_data[0]['artist_id']).values('artist_name')
    # artist_id = Track.objects.filter(id=track_id).values('artist_id')[0]['artist_id']
    # album_id = Track.objects.filter(id=track_id).values('album_id')[0]['album_id']
    # genre_id = Track.objects.filter(id=track_id).values('album_id')[0]['album_id']
    return Response({"Track_Data": artist_name})

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