from typing import TypeVar

import pytest
from django.db import models
from mixer.backend.django import mixer

GenericModelForMixer = TypeVar('GenericModelForMixer', models.Model, str)


@pytest.fixture()
def generic_model_factory():
    def factory(
        model: GenericModelForMixer,
        **kwargs,
    ) -> models.Model:
        return mixer.blend(model, **kwargs)

    return factory
