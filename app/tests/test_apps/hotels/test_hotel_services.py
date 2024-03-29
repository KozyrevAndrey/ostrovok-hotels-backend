import pytest

from dictionaries.models import City
from hotels.models import Hotel

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    ('filters', 'return_filters'),
    [
        ({'from_id': 1}, {'id__gte': 1}),
        ({'city_id': 1}, {'city_id': 1}),
        ({'city_id': 1, 'from_id': 1}, {'city_id': 1, 'id__gte': 1}),
    ],
)
def test_parse_hotel_filters(filters, return_filters, hotel_service):
    parsed_filters = hotel_service.parse_hotel_filters(filters)
    assert parsed_filters == return_filters


@pytest.mark.parametrize('cycle', [2, 5, 10])
def test_get_hotels_by_filters_no_filters(generic_model_factory, hotel_service, cycle):
    hotels = []
    for _ in range(cycle):
        hotel = generic_model_factory(Hotel)
        hotels.append(hotel)
    hotels_data_from_service_query = hotel_service.get_hotels_by_filters()
    for hotel in hotels:
        assert hotel in hotels_data_from_service_query


@pytest.mark.parametrize('cycle', [2, 5, 10])
def test_get_hotels_by_filters_city_id(generic_model_factory, cycle, hotel_service):
    city = generic_model_factory(City, name='Vise City')
    city_another = generic_model_factory(City, name='San Andreas')
    hotels_another = generic_model_factory(Hotel, city=city_another)
    hotels = []
    for _ in range(cycle):
        hotel = generic_model_factory(Hotel, city=city)
        hotels.append(hotel)
    hotels_data_from_service_query = hotel_service.get_hotels_by_filters(
        {'city_id': city.id}
    )
    for hotel in hotels:
        assert hotel in hotels_data_from_service_query
    assert hotels_another not in hotels_data_from_service_query


@pytest.mark.parametrize('cycle', [2, 5, 10])
def test_get_hotels_by_filters_from_id(generic_model_factory, cycle, hotel_service):
    city = generic_model_factory(City, name='Vise City')
    hotels = []
    for _ in range(cycle):
        hotel = generic_model_factory(Hotel, city=city)
        hotels.append(hotel)
    hotels_data_from_service_query = hotel_service.get_hotels_by_filters(
        {'from_id': hotels[1].id}
    )
    for hotel in hotels[1:]:
        assert hotel in hotels_data_from_service_query
    assert hotels[0] not in hotels_data_from_service_query
