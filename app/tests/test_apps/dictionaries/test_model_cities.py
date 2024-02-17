import pytest
from dictionaries.models import City

pytestmark = [pytest.mark.django_db]


def test_create(get_city_data, generic_model_factory, assert_model_and_expected_data):
    city_data = get_city_data()
    city = generic_model_factory(City, **city_data)
    assert_model_and_expected_data(city, city_data)
