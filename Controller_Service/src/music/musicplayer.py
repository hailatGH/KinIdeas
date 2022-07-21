from rest_framework import serializers
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
    querylist = [
        {'queryset': Artist.objects.all(), 'serializer_class': ArtistSerializer},
        {'queryset': Album.objects.all(), 'serializer_class': AlbumSerializer},
        {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
        {'queryset': Track.objects.all(), 'serializer_class': TrackSerializer},
        {'queryset': Lyrics.objects.all(), 'serializer_class': LyricsSerializer},
    ]