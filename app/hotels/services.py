from typing import Any
from app.services import GenericModelService
from .models import Hotel

from .data import HotelFilterData
from .serializers import HotelSerializer
from rest_framework.utils.serializer_helpers import ReturnDict


class HotelService:
    def __init__(self):
        self.generic_service = GenericModelService(model=Hotel)

    def get_hotels_by_filters(
        self, filters: dict | None = None
    ) -> ReturnDict[Any, Any]:
        '''
        We can use django-filter,
        but for this you need queryset with .all()
        and after this you filter this queryset.
        This decision gives you slow query
        '''
        if filters:
            hotel_filters = self.parse_hotel_filters(filters)
            hotels = self.generic_service.get_queries_by_filters(**hotel_filters)
        else:
            hotels = self.generic_service.get_queries_by_filters()
        serializer = HotelSerializer(instance=hotels, many=True)
        return serializer.data

    def parse_hotel_filters(self, filters: dict[str, Any]) -> HotelFilterData:
        hotel_filters = HotelFilterData()  # No error!
        for key, value in filters.items():
            if key == 'from_id':
                hotel_filters['id__gte'] = value
            else:
                hotel_filters[key] = value
        return hotel_filters
