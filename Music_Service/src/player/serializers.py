from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import MusicAlbum, MusicArtist, MusicTrack, MusicGenre, MusicLyrics, MusicPlayList, MusicPlayListTracks, MusicFavourites

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
        model = MusicPlayListTracks
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=MusicPlayListTracks.objects.all(),
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
        model = MusicLyrics
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicTrack
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

     class Meta:
        model = MusicGenre
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicAlbum
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MusicArtist
        fields = '__all__'