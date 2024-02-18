from typing import Unpack

import pytest

from hotels.data import HotelData
from hotels.services import HotelService


@pytest.fixture()
def get_hotel_data(fake_schema, fake):
    def factory(**kwargs: Unpack['HotelData']):
        schema = fake_schema(
            schema=lambda: {
                'name': fake('text.title'),
                'address': fake('address.address'),
                'phone_number': fake('person.phone_number'),
            },
            iterations=1,
        )
        return {
            **schema.create()[0],  # type: ignore[misc]
            **kwargs,
        }

    return factory


@pytest.fixture()
def hotel_service() -> HotelService:
    return HotelService()
