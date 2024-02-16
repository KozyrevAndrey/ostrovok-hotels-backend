import pytest
from users.models import User

pytestmark = [pytest.mark.django_db]


def test_create_user(get_user_data, fake):
    data = get_user_data(password=fake('person.password'))
    user = User.objects.create_user(**data)
    assert user.email == data['email']
    assert user.patronymic == data['patronymic']
    assert user.check_password(data['password']) is True


def test_create_user_no_email(fake):
    with pytest.raises(ValueError):
        User.objects.create_user(email=None, password=fake('person.password'))


def test_create_superuser(get_user_data, fake):
    data = get_user_data(password=fake('person.password'))
    user = User.objects.create_superuser(**data)
    assert user.email == data['email']
    assert user.patronymic == data['patronymic']
    assert user.check_password(data['password']) is True


def test_create_superuser_not_staff(get_user_data, fake):
    data = get_user_data(password=fake('person.password'), is_staff=False)
    with pytest.raises(ValueError):
        User.objects.create_superuser(**data)


def test_create_superuser_not_superuser(get_user_data, fake):
    data = get_user_data(password=fake('person.password'), is_superuser=False)
    with pytest.raises(ValueError):
        User.objects.create_superuser(**data)
