from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import PodcastHost, PodcastSeason, PodcastCategory, PodcastEpisode, PodcastPlayList, PodcastPlayListEpisodes, PodcastFavourites

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PodcastFavourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PodcastFavourites.objects.all(),
                fields=['episode_id', 'user_id']
            )
        ]

class PlayListEpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastPlayListEpisodes
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PodcastPlayListEpisodes.objects.all(),
                fields=['playlist_id', 'episode_id']
            )
        ]

class PlayListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PodcastPlayList
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PodcastPlayList.objects.all(),
                fields=['playlist_name', 'user_id']
            )
        ]

class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastEpisode
        fields = '__all__'

class PodcastCategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PodcastCategory
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastSeason
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PodcastHost
        fields = '__all__'