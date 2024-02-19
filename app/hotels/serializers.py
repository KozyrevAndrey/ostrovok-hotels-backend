from typing import Any

from rest_framework import serializers

from dictionaries.serializers import CitySerializer

from .models import Hotel


class HotelSerializer(serializers.ModelSerializer[Hotel]):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'phone_number', 'city']


class HotelFilterSerializer(serializers.Serializer[dict[str, Any]]):
    city_id = serializers.IntegerField(required=False)
    from_id = serializers.IntegerField(required=False)
