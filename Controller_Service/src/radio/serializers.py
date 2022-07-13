from rest_framework import serializers

from .models import Radio

class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio
        fields = '__all__'