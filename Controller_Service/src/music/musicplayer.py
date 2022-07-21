from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .models import Album, Artist, Track, Genre, Lyrics

# Serializers

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = [
            'id',
            'lyrics_title',
            'lyrics_detail',
        ]

class TrackSerializer(serializers.ModelSerializer):
    lyrics = LyricsSerializer(many=True, required=False)

    class Meta:
        model = Track
        fields = [
            'id',
            'track_name',
            'track_file',
            'lyrics',
        ]

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            'id',
            'genre_title',
        ]

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = [
            'id',
            'album_title',
            'album_cover',
        ]

class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = [
            'id',
            'artist_name',
            'artist_cover',
        ]

# Viewsets

class MusicPlayerAPIView(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        id = self.request.query_params['id']
        # ar_id = Track.objects.filter(id=id).values()
        # al_id = Track.objects.filter(id=id).values()
        # g_id = Track.objects.filter(id=id).values()

        print(id)

        querylist = [
            {'queryset': Track.objects.filter(id=id), 'serializer_class': TrackSerializer},
            # {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
            # {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
            # {'queryset': Genre.objects.filter(id=g_id), 'serializer_class': GenreSerializer},
        ]

        return querylist