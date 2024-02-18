from typing import Any

from django.db.models.query import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response

from app import pagination as custom_pagination
from app.services import GenericModelService

from .data import HotelFilterData
from .models import Hotel
from .serializers import HotelSerializer


class HotelService:
    def __init__(self):
        self.generic_service = GenericModelService(model=Hotel)

    def get_hotels_by_filters(self, filters: dict | None = None) -> QuerySet[Hotel]:
        '''
        We can use django-filter,
        but for this you need queryset with method .all()
        and after this you filter this queryset.
        This decision gives you slow query
        '''
        if filters:
            hotel_filters = self.parse_hotel_filters(filters)
            hotels = self.generic_service.get_queries_by_filters(**hotel_filters)
        else:
            hotels = self.generic_service.get_queries_by_filters()
        return hotels

    def get_response_for_hotel_filter_view(
        self, request: Request, filters: dict | None = None
    ) -> Response:
        hotels = self.get_hotels_by_filters(filters=filters)
        return custom_pagination.get_paginated_response(
            pagination_class=custom_pagination.CustomOffsetPagination,
            serializer_class=HotelSerializer,
            queryset=hotels,
            request=request,
            view=self,
        )

    def parse_hotel_filters(self, filters: dict[str, Any]) -> HotelFilterData:
        hotel_filters = HotelFilterData()  # No error!
        for key, value in filters.items():
            if key == 'from_id':
                hotel_filters['id__gte'] = value
            else:
                hotel_filters[key] = value
        return hotel_filters
