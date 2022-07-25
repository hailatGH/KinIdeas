from rest_framework import serializers
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .models import Artist, Album, Genre, Track, Lyrics, PlayList, FavouriteList

# Serializers

class LyricsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lyrics
        fields = [
            'id',
            'lyrics_detail',
        ]

class TrackSerializer(serializers.ModelSerializer):

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

class SingleMusicPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        t_id = self.request.query_params['id']
        ar_id = Track.objects.filter(id=t_id).values('artist_id')[0]['artist_id']
        al_id = Track.objects.filter(id=t_id).values('album_id')[0]['album_id']
        ge_id = Track.objects.filter(id=t_id).values('genre_id')[0]['genre_id']

        querylist = (
            {'queryset': Artist.objects.filter(id=ar_id), 'serializer_class': ArtistSerializer},
            {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
            {'queryset': Genre.objects.filter(id=ge_id), 'serializer_class': GenreSerializer},
            {'queryset': Track.objects.filter(id=t_id), 'serializer_class': TrackSerializer},
            {'queryset': Lyrics.objects.filter(track_id=t_id), 'serializer_class': LyricsSerializer},
        )

        return querylist

class AlbumMusicsPlayer(ObjectMultipleModelAPIViewSet):
    def get_querylist(self):
        al_id = self.request.query_params['id']
        t_id = Track.objects.filter(album_id=al_id).values('id')
        ar_id = Album.objects.filter(id=al_id).values('artist_id')[0]['artist_id']
        # ge_id = Track.objects.filter(id=t_id).values('genre_id')[0]['genre_id']
        print(al_id)
        print(t_id)
        print(ar_id)
        querylist = (
            # {'queryset': Artist.objects.filter(id=al_id), 'serializer_class': ArtistSerializer},
            {'queryset': Album.objects.filter(id=al_id), 'serializer_class': AlbumSerializer},
            # {'queryset': Genre.objects.filter(id=ge_id), 'serializer_class': GenreSerializer},
            # {'queryset': Track.objects.filter(id=t_id), 'serializer_class': TrackSerializer},
            # {'queryset': Lyrics.objects.filter(track_id=t_id), 'serializer_class': LyricsSerializer},
        )

        return querylist

