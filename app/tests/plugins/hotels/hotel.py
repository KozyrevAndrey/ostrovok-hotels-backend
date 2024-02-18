import pytest
from typing import Unpack
from hotels.data import HotelData


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
