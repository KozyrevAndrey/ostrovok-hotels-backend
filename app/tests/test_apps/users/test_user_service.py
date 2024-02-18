import pytest

from users.models import User

pytestmark = [pytest.mark.django_db]


def test_get_by_email(
    user_service, get_user_data, generic_model_factory, assert_model_and_expected_data
):
    user_data = get_user_data()
    generic_model_factory(model=User, **user_data)
    assert_user = user_service.get_by_email(user_data['email'])
    assert_model_and_expected_data(assert_user, user_data)
