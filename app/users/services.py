from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

from app.services import GenericModelService

from .data import UserRegistrationData
from .models import User


class UserService:
    def __init__(self):
        self.generic_model_service = GenericModelService(model=User)

    def get_by_email(self, email: str) -> User | None:
        return self.generic_model_service.get_by_filters(email=email)


class UserRegistrationService:
    def __init__(self):
        self.generic_model_service = GenericModelService(model=User)

    def create_user_and_get_token(self, user_data: UserRegistrationData) -> str:
        user_data['password'] = make_password(user_data['password'])
        user = self.generic_model_service.create(**user_data)
        return self.get_auth_token(user=user)

    def get_auth_token(self, user: User):
        token, _ = Token.objects.get_or_create(user_id=user.id)
        return token.key

    def get_auth_token_by_user_data(self, user_data: UserRegistrationData) -> str:
        user = self.generic_model_service.get_by_filters(email=user_data['email'])
        return self.get_auth_token(user)
