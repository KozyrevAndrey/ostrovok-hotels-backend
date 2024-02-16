import pytest
from typing import TypeVar
from mixer.backend.django import mixer
from django.db import models

GenericModelForMixer = TypeVar('GenericModelForMixer', models.Model, str)


@pytest.fixture()
def generic_model_factory():
    def factory(
        model: GenericModelForMixer,
        **kwargs,
    ) -> models.Model:
        return mixer.blend(model, **kwargs)

    return factory
