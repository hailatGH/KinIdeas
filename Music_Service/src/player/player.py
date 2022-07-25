from rest_framework import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .models import Artist, Album, Genre, PlayListTracks, Track, Lyrics, PlayList, FavouriteList

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
            'genre_id',
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

    class Meta:
        model = FavouriteList
        fields = [
            'id',
            'user_id',
        ]

class PlayListTracksSerializer(serializers.ModelSerializer):  

    class Meta:
        model = PlayListTracks
        fields = [
            # 'id',
            'track_id',
        ]

class PlayListSerializer(serializers.ModelSerializer):  

    class Meta:
        model = PlayList
        fields = [
            # 'id',
            'playlist_name',
            'user_id',
        ]

# Views

class SingleMusicPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        t_id = self.request.query_params['id']
        ar_id = Track.objects.filter(id=t_id).values('artist_id')[0]['artist_id']
        al_id = Track.objects.filter(id=t_id).values('album_id')[0]['album_id']

        querylist = (
            {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
            {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
            {'queryset': Track.objects.filter(id=t_id), 'serializer_class': TrackSerializer},
            {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
        )

        return querylist

class AlbumMusicsPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        al_id = self.request.query_params['id']
        ar_id = Album.objects.filter(id=al_id).values('artist_id')[0]['artist_id']
        
        querylist = (
            {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
            {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
            {'queryset': Track.objects.filter(album_id=al_id), 'serializer_class': TrackSerializer},
            {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
        )

        return querylist

class PlaylistMusicsPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        pl_id = self.request.query_params['id']
        
        querylist = (
            {'queryset': PlayList.objects.filter(id=pl_id), 'serializer_class': PlayListSerializer},
            {'queryset': PlayListTracks.objects.filter(playlist_id=pl_id), 'serializer_class': PlayListTracksSerializer},
            {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
        )

        return querylist

# class FavlistMusicsPlayer(ObjectMultipleModelAPIViewSet):
#     pass