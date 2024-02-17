import pytest
from users.models import User
from dictionaries.models import City
from app.services import GenericModelService

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize('model', [City, User])
def test_generic_service_get_by_filter(generic_model_factory, model):
    object = generic_model_factory(model=model)
    generic_service = GenericModelService(model=model)
    assert object == generic_service.get_by_filters(id=object.id)


@pytest.mark.parametrize(
    ('model', 'model_field', 'fake_data'),
    [
        (City, 'name', 'city'),
        (User, 'email', 'person.email'),
    ],
)
def test_get_queries_by_filters(
    generic_model_factory, fake, model, model_field, fake_data
):
    data = {model_field: fake(fake_data)}
    object = generic_model_factory(model=model, **data)
    generic_service = GenericModelService(model=model)
    assert object in generic_service.get_queries_by_filters(**data)


@pytest.mark.parametrize(
    ('model', 'model_field', 'fake_data'),
    [
        (City, 'name', 'city'),
        (User, 'email', 'person.email'),
    ],
)
def test_create(assert_model_and_expected_data, fake, model, model_field, fake_data):
    data = {model_field: fake(fake_data)}
    generic_service = GenericModelService(model=model)
    object = generic_service.create(**data)
    assert_model_and_expected_data(object, data)


@pytest.mark.parametrize('model', [City, User])
def test_delete(generic_model_factory, model):
    object = generic_model_factory(model=model)
    generic_service = GenericModelService(model=model)
    generic_service.delete_by_id(id=object.id)
    assert generic_service.get_by_filters(id=object.id) is None
