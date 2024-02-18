from typing import TypedDict


class UserData(TypedDict):
    email: str
    patronymic: str


class UserRegistrationData(TypedDict):
    email: str
    password: str
