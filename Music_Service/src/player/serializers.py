from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Album, Artist, Track, Genre, Lyrics, PlayList, PlayListTracks, Favourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Favourites.objects.all(),
                fields=['track_id', 'user_id']
            )
        ]

class PlayListTracksSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayListTracks
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListTracks.objects.all(),
                fields=['playlist_id', 'track_id']
            )
        ]

class PlayListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayList
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayList.objects.all(),
                fields=['playlist_name', 'user_id']
            )
        ]

class LyricsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lyrics
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

     class Meta:
        model = Genre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = '__all__'