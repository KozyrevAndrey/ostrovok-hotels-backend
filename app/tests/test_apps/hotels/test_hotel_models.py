import pytest
from dictionaries.models import City
from hotels.models import Hotel

pytestmark = [pytest.mark.django_db]


def test_create(
    get_city_data, get_hotel_data, generic_model_factory, assert_model_and_expected_data
):
    city_data = get_city_data()
    city = generic_model_factory(City, **city_data)
    hotel_data = get_hotel_data(city=city)
    hotel = generic_model_factory(Hotel, **hotel_data)
    assert_model_and_expected_data(hotel, hotel_data)


@pytest.mark.parametrize(
    ('phone_number', 'validated_phone_number'),
    [
        ('+16044011234', '+16044011234'),
        ('+799212421', '+799212421'),
    ],
)
def test_check_phone_number_validation(
    get_city_data,
    get_hotel_data,
    generic_model_factory,
    assert_model_and_expected_data,
    phone_number,
    validated_phone_number,
):
    city_data = get_city_data()
    city = generic_model_factory(City, **city_data)
    hotel_data = get_hotel_data(city=city, phone_number=phone_number)
    hotel = generic_model_factory(Hotel, **hotel_data)
    assert hotel.phone_number == validated_phone_number
    assert_model_and_expected_data(hotel, hotel_data)


@pytest.mark.parametrize(
    ('phone_number'),
    ['16044011234', '1', 'fsafw', '+111111111111111111111111111111111111111111111111'],
)
def test_check_phone_number_validation_failed(
    get_city_data,
    get_hotel_data,
    generic_model_factory,
    phone_number,
):
    city_data = get_city_data()
    city = generic_model_factory(City, **city_data)
    hotel_data = get_hotel_data(city=city, phone_number=phone_number)

    hotel = generic_model_factory(Hotel, **hotel_data)
    assert hotel.phone_number.is_valid() is False
