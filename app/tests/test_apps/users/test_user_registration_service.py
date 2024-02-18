import pytest

from users.data import UserRegistrationData
from users.models import User

pytestmark = [pytest.mark.django_db]


def test_create_user_and_get_token(
    user_service, user_registration_service, assert_model_and_expected_data, fake
):
    user_data = UserRegistrationData(
        email=fake('person.email'), password=fake('person.password')
    )
    user_token = user_registration_service.create_user_and_get_token(user_data)
    user = user_service.get_by_email(user_data['email'])
    assert isinstance(user_token, str)
    assert_model_and_expected_data(user, user_data)


def test_get_auth_token(generic_model_factory, user_registration_service):
    user = generic_model_factory(User)
    token = user_registration_service.get_auth_token(user)
    assert isinstance(token, str)


def test_get_auth_token_by_user_data(
    get_user_data, generic_model_factory, user_registration_service
):
    user_data = get_user_data()
    generic_model_factory(User, **user_data)
    token = user_registration_service.get_auth_token_by_user_data(user_data)
    assert isinstance(token, str)
