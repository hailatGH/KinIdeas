from rest_framework import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .models import Artist, Album, Genre, Track, Lyrics, PlayList, FavouriteList

# Serializers

class GenreSerializer(serializers.ModelSerializer):

     class Meta:
        model = Genre
        fields = [
            'id',
            'genre_title',
        ]

class LyricsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lyrics
        fields = [
            'id',
            'lyrics_detail',
        ]

class TrackSerializer(serializers.ModelSerializer):
    lyrics = LyricsSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = [
            'id',
            'track_name',
            'track_file',
            'lyrics',
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
        ]

class FavouriteListSerializer(serializers.ModelSerializer):
    # favouritelist = TrackSerializer(many=True, required=False)

    class Meta:
        model = FavouriteList
        fields = [
            'id',
            'user_id',
            # 'favouritelist',
        ]

class PlayListSerializer(serializers.ModelSerializer):  
    # playlist = TrackSerializer(many=True, required=False)

    class Meta:
        model = PlayList
        fields = [
            'id',
            'playlist_name',
            # 'playlist',
        ]

# Views

class AlbumMusicsPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        al_id = self.request.query_params['id']
        ar_id = Album.objects.filter(id=al_id).values('artist_id')[0]['artist_id']
        
        querylist = (
            {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
            {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
        )

        return querylist

