from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Host, Season, PodcastCategory, Episode, PlayList, PlayListEpisodes, Favourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Favourites.objects.all(),
                fields=['episode_id', 'user_id']
            )
        ]

class PlayListEpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayListEpisodes
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListEpisodes.objects.all(),
                fields=['playlist_id', 'episode_id']
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

class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = '__all__'

class PodcastCategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PodcastCategory
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Host
        fields = '__all__'