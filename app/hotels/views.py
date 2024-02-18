from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from .serializers import HotelFilterSerializer, HotelSerializer
from .services import HotelService
from rest_framework.request import Request
from rest_framework import status


class HotelFilterView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        query_serializer=HotelFilterSerializer,
        responses={
            200: HotelSerializer(many=True),
            400: '{}',
            401: '{}',
        },
        operation_id='Get Hotels With Filters',
        operation_description='Get Hotels With Filters',
    )
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        query_serializer = HotelFilterSerializer(data=request.query_params)
        if not query_serializer.is_valid():
            return Response(
                {'error': 'Invalid query'}, status=status.HTTP_400_BAD_REQUEST
            )
        hotels_data = HotelService().get_hotels_by_filters(
            filters=query_serializer.data
        )
        return Response(hotels_data)
