from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import RadioStation, RadioStationFavourites

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioStation
        fields = '__all__'

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RadioStationFavourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=RadioStationFavourites.objects.all(),
                fields=['station_id', 'user_id']
            )
        ]