from rest_framework import serializers

from .models import Season, Host, Episode, PodcastCategory

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = [
            'id',
            'episode_title',
            'episode_description',
            'episode_file',
            'episode_status',
            'episode_release_date',
            'podcast_category_id',
            'season_id',
            'user_id',
            'created_at',
            'updated_at',
        ]

class PodcastCategorySerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = PodcastCategory
        fields = [
            'id',
            'podcast_category_title',
            'podcast_category_cover',
            'podcast_category_description',
            'user_id',
            'created_at',
            'updated_at',
            'episode',
        ]

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, required=False)

    class Meta:
        model = Season
        fields = [
            'id',
            'season_title',
            'season_cover',
            'season_description',
            'host_id',
            'user_id',
            'created_at',
            'updated_at',
            'episodes',
        ]

class HostSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, required=False)
    
    class Meta:
        model = Host
        fields = [
            'id',
            'host_name',
            'host_title',
            'host_cover',
            'host_description',
            'user_id',
            'created_at',
            'updated_at',
            'seasons',
        ]