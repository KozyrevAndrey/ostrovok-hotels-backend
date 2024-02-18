from typing import Any
from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer[Hotel]):

    class Meta:
        model = Hotel
        fields = ['name', 'address', 'phone_number', 'city']


class HotelFilterSerializer(serializers.Serializer[dict[str, Any]]):

    city_id = serializers.IntegerField(required=False)
    from_id = serializers.IntegerField(required=False)
