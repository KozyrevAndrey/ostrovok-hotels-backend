from typing import Sequence

import pytest
from django.db import models


@pytest.fixture()
def assert_model_and_expected_data():
    def factory(
        model: models.Model,
        expected: Sequence,
    ):
        for field_name, data_value in expected.items():
            assert getattr(model, field_name) == data_value

    return factory
