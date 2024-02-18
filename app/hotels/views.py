from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HotelFilterSerializer, HotelSerializer
from .services import HotelService


class HotelFilterView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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
        return HotelService().get_response_for_hotel_filter_view(
            request=request, filters=query_serializer.data
        )

        # return Response(hotels_data, status=status.HTTP_200_OK)
