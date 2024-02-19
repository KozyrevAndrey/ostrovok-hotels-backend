from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer[City]):
    class Meta:
        model = City
        fields = [
            'id',
            'name',
        ]
