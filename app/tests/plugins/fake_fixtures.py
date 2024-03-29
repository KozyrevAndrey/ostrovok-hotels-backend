import pytest
from mimesis import Field, Locale, Schema


@pytest.fixture()
def fake() -> Field:
    return Field(locale=Locale.RU)


@pytest.fixture()
def fake_schema() -> Schema:
    return Schema
