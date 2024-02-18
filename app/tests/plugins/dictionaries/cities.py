from typing import Unpack

import pytest

from dictionaries.data import CityData


@pytest.fixture()
def get_city_data(fake_schema, fake):
    def factory(**kwargs: Unpack['CityData']):
        schema = fake_schema(
            schema=lambda: {
                'email': fake('person.email'),
                'patronymic': fake('person.first_name'),
            },
            iterations=1,
        )
        return {
            **schema.create()[0],  # type: ignore[misc]
            **kwargs,
        }

    return factory
