from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Station, Favourites

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favourites
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Favourites.objects.all(),
                fields=['station_id', 'user_id']
            )
        ]