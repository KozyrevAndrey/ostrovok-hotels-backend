from typing import Unpack
import pytest
from mixer.backend.django import mixer
from users.data import UserData


@pytest.fixture()
def get_user_data(fake_schema, fake):
    def factory(**kwargs: Unpack[UserData]):
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
