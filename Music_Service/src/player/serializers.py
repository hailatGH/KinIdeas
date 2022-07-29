from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Album, Artist, Track, Genre, Lyrics, MusicPlayList, PlayListTracks, MusicFavourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MusicFavourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=MusicFavourites.objects.all(),
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
        model = MusicPlayList
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=MusicPlayList.objects.all(),
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