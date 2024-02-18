from typing import Unpack

import pytest

from users.data import UserData
from users.services import UserRegistrationService, UserService


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


@pytest.fixture()
def user_service() -> UserService:
    return UserService()


@pytest.fixture()
def user_registration_service() -> UserRegistrationService:
    return UserRegistrationService()
