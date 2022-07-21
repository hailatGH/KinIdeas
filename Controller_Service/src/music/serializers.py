from rest_framework import serializers

from .models import Album, Artist, Track, Genre, Lyrics

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    lyrics = LyricsSerializer(many=True, required=False)

    class Meta:
        model = Track
        fields = [
            'id',
            'track_name',
            'track_description',
            'track_file',
            'track_status',
            'track_release_date',
            'artist_id',
            'album_id',
            'genre_id',
            'user_id',
            'created_at',
            'updated_at',
            'lyrics',
        ]

class GenreSerializer(serializers.ModelSerializer):
    tracks_g = TrackSerializer(many=True, required=False)

    class Meta:
        model = Genre
        fields = [
            'id',
            'genre_title',
            'genre_cover',
            'genre_description',
            'user_id',
            'created_at',
            'updated_at',
            'tracks_g',
        ]

class AlbumSerializer(serializers.ModelSerializer):
    tracks_al = TrackSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = [
            'id',
            'album_title',
            'album_cover',
            'album_description',
            'artist_id',
            'user_id',
            'created_at',
            'updated_at',
            'tracks_al',
        ]

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, required=False)
    
    class Meta:
        model = Artist
        fields = [
            'id',
            'artist_name',
            'artist_title',
            'artist_cover',
            'artist_description',
            'user_id',
            'created_at',
            'updated_at',
            'albums',
        ]