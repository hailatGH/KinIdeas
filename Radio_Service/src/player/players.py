from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Station, Favourites

@api_view(['GET'])
def play_single_track(request):
    station_data = {}
    
    station_obj = Station.objects.filter(id=request.query_params['station']).values('id', 'station_name', 'station_frequency', 'station_url', 'station_cover')
    station_id = station_obj[0]['id']
    station_name = station_obj[0]['station_name']
    station_frequency = station_obj[0]['station_frequency']
    station_url = station_obj[0]['station_url']
    station_cover = station_obj[0]['station_cover']

    for variable in ["station_id", "station_name", "station_frequency", "station_url", "station_cover"]:
        station_data[variable] = eval(variable)

    return Response({"Track Data": station_data})

@api_view(['GET'])
def play_favourite_tracks(request):
    favourite_data = {}
    stations = {}

    favourite_obj = Favourites.objects.filter(user_id=request.query_params['user']).values('user_id', 'station_id')
    user_id = favourite_obj[0]['user_id']
    favourite_data["User"] = user_id

    for i in range(len(favourite_obj)):
        station_data = {}
        
        station_obj = Station.objects.filter(id=request.query_params['station']).values('id', 'station_name', 'station_frequency', 'station_url', 'station_cover')
        station_id = station_obj[0]['id']
        station_name = station_obj[0]['station_name']
        station_frequency = station_obj[0]['station_frequency']
        station_url = station_obj[0]['station_url']
        station_cover = station_obj[0]['station_cover']

        for variable in ["station_id", "station_name", "station_frequency", "station_url", "station_cover"]:
            station_data[variable] = eval(variable)
            
        stations["Station: " + str(i)] = station_data

    favourite_data["Stations"] = stations
        
    return Response({"Favourite Data": favourite_data})