from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Host, Season, PodcastCategory, Episode, PlayList, PlayListEpisodes, Favourites

@api_view(['GET'])
def play_single_episode(request):
    episode_data = {}
    
    episode_obj = Episode.objects.filter(id=request.query_params['episode']).values('id', 'episode_title', 'episode_file', 'host_id', 'season_id', \
        "podcast_category_id")
    episode_id = episode_obj[0]['id']
    episode_title = episode_obj[0]['episode_title']
    episode_file = episode_obj[0]['episode_file']
    host_id = episode_obj[0]['host_id']
    host_name = Host.objects.filter(id=host_id).values('host_name')[0]['host_name']
    season_id = episode_obj[0]['season_id']
    season_title = Season.objects.filter(id=season_id).values('season_title')[0]['season_title']
    season_cover = Season.objects.filter(id=season_id).values('season_cover')[0]['season_cover']
    podcast_category_id = episode_obj[0]['podcast_category_id']
    podcast_category_title = PodcastCategory.objects.filter(id=podcast_category_id).values('podcast_category_title')[0]['podcast_category_title']
    
    for variable in ["episode_id", "episode_title", "episode_file", "host_id", "host_name", "season_id",\
        "season_title", "season_cover", "podcast_category_id", "podcast_category_title"]:
        episode_data[variable] = eval(variable)

    return Response({"Episode Data": episode_data})

@api_view(['GET'])
def play_season_episodes(request):
    season_data = {}
    episodes = {}

    season_obj = Season.objects.filter(id=request.query_params['season']).values('id', 'season_title', 'season_cover', 'host_id')
    
    season_id = season_obj[0]['id']
    season_title = season_obj[0]['season_title']
    season_cover = season_obj[0]['season_cover']
    host_id = season_obj[0]['host_id']
    host_name = Host.objects.filter(id=host_id).values('host_name')[0]['host_name']

    for variable in ["season_id", "season_title", "season_cover", "host_id", "host_name"]:
        season_data[variable] = eval(variable)

    episode_obj = Episode.objects.filter(season_id=season_id).values('id', 'episode_title', 'episode_file', 'podcast_category_id')
    
    for i in range(len(episode_obj)):
        episode_data = {}

        episode_id = episode_obj[i]['id']
        episode_title = episode_obj[i]['episode_title']
        episode_file = episode_obj[i]['episode_file']
        podcast_category_id = episode_obj[i]['podcast_category_id']
        podcast_category_title = PodcastCategory.objects.filter(id=podcast_category_id).values('podcast_category_title')[0]['podcast_category_title']

        for variable in ["episode_id", "episode_title", "episode_file", "podcast_category_id", "podcast_category_title"]:
            episode_data[variable] = eval(variable)

        episodes["Episode: " + str(i)] = episode_data

    season_data["Episodes"] = episodes

    return Response({"Album Data": season_data})

@api_view(['GET'])
def play_playlist_episodes(request):
    playlist_data = {}
    episodes = {}

    playlist_obj = PlayList.objects.filter(id=request.query_params['playlist']).values('id', 'playlist_name', 'user_id')
    playlist_id = playlist_obj[0]['id']
    playlist_name = playlist_obj[0]['playlist_name']
    user_id = playlist_obj[0]['user_id']

    for variable in ["playlist_id", "playlist_name", "user_id"]:
        playlist_data[variable] = eval(variable)

    playlist_episodes_obj = PlayListEpisodes.objects.filter(playlist_id=playlist_id).values('playlist_id', 'episode_id')

    for i in range(len(playlist_episodes_obj)):
        episode_data = {}
    
        episode_obj = Episode.objects.filter(id=playlist_episodes_obj[i]['episode_id']).values('id', 'episode_title', 'episode_file', 'host_id', 'season_id', "podcast_category_id")
        episode_id = episode_obj[0]['id']
        episode_title = episode_obj[0]['episode_title']
        episode_file = episode_obj[0]['episode_file']
        host_id = episode_obj[0]['host_id']
        host_name = Host.objects.filter(id=episode_obj[0]['host_id']).values('host_name')[0]['host_name']
        season_id = episode_obj[0]['season_id']
        season_title = Season.objects.filter(id=episode_obj[0]['season_id']).values('season_title')[0]['season_title']
        season_cover = Season.objects.filter(id=episode_obj[0]['season_id']).values('season_cover')[0]['season_cover']
        podcast_category_id = episode_obj[0]['podcast_category_id']
        podcast_category_title = PodcastCategory.objects.filter(id=episode_obj[0]['genrpodcast_category_ide_id']).values('podcast_category_title')[0]['podcast_category_title']

        for variable in ["episode_id", "episode_title", "episode_file", "host_id", "host_name", "season_id", "season_title", "season_cover", "podcast_category_id", "podcast_category_title"]:
            episode_data[variable] = eval(variable)
        
        episodes["Episode: " + str(i)] = episode_data

    playlist_data["Episodes"] = episodes

    return Response({"Playlist Data": playlist_data})

@api_view(['GET'])
def play_favourite_episodes(request):
    favourite_data = {}
    episodes = {}

    favourite_obj = Favourites.objects.filter(user_id=request.query_params['user']).values('user_id', 'episode_id')
    user_id = favourite_obj[0]['user_id']
    favourite_data["User"] = user_id

    for i in range(len(favourite_obj)):
        episode_data = {}
    
        episode_obj = Episode.objects.filter(id=favourite_obj[i]['episode_id']).values('id', 'episode_title', 'episode_file', 'host_id', 'season_id', "podcast_category_id")
        episode_id = episode_obj[0]['id']
        episode_title = episode_obj[0]['episode_title']
        episode_file = episode_obj[0]['episode_file']
        host_id = episode_obj[0]['host_id']
        host_name = Host.objects.filter(id=episode_obj[0]['host_id']).values('host_name')[0]['host_name']
        season_id = episode_obj[0]['season_id']
        season_title = Season.objects.filter(id=episode_obj[0]['season_id']).values('season_title')[0]['season_title']
        season_cover = Season.objects.filter(id=episode_obj[0]['season_id']).values('season_cover')[0]['season_cover']
        podcast_category_id = episode_obj[0]['podcast_category_id']
        podcast_category_title = PodcastCategory.objects.filter(id=episode_obj[0]['genrpodcast_category_ide_id']).values('podcast_category_title')[0]['podcast_category_title']

        for variable in ["episode_id", "episode_title", "episode_file", "host_id", "host_name", "season_id", "season_title", "season_cover", "podcast_category_id", "podcast_category_title"]:
            episode_data[variable] = eval(variable)
        
        episodes["Episode: " + str(i)] = episode_data


    favourite_data["Episodes"] = episodes
        
    return Response({"Favourite Data": favourite_data})