import pytest
from users.models import User

pytestmark = [pytest.mark.django_db]


def test_create(get_user_data, generic_model_factory, assert_model_and_expected_data):
    data = get_user_data()
    user = generic_model_factory(model=User, **data)
    assert_model_and_expected_data(user, data)
