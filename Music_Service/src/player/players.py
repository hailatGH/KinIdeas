from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Album, Genre, PlayListTracks, Track, Lyrics, PlayList, Favourites

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

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