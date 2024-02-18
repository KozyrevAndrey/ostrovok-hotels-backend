from typing import TypedDict
from dictionaries.models import City


class HotelData(TypedDict):
    name: str
    address: str
    phone_number: str
    city: int | City
