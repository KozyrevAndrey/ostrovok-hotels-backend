from typing import Any

from rest_framework import serializers


class UserRegistrationSerializer(serializers.Serializer[dict[str, Any]]):
    email = serializers.CharField()
    password = serializers.CharField()
