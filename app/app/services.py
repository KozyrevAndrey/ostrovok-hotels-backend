from typing import Any, TypeVar
from django.db.models.query import QuerySet
from django.db import models
from django.db.models.base import ModelBase

ModelFields = TypeVar('ModelFields', dict[str, Any], tuple[tuple[str, Any]])


class GenericModelService:
    def __init__(self, model: ModelBase) -> None:
        self.model = model

    def get_by_filters(self, **filters: ModelFields) -> models.Model | None:
        return self.model.objects.filter(**filters).first()

    def get_queries_by_filters(self, **filters: ModelFields) -> QuerySet[models.Model]:
        return self.model.objects.filter(**filters)

    def create(self, **kwargs: ModelFields) -> models.Model:
        return self.model.objects.create(**kwargs)

    def update_by_id_with_fields_and_values(
        self,
        object_id: int,
        **fields_values: ModelFields,
    ) -> models.Model:
        return self.model.objects.filter(id=object_id).update(**fields_values)

    def delete_by_id(self, object_id: int) -> tuple[int, dict[str, Any]]:
        return self.model.objects.filter(id=object_id).delete()
