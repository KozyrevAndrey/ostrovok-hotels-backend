from django.db.models.query import QuerySet
from django.db import models


class GenericModelService:

    def __init__(self, model: models.Model):
        self.model = model

    def get_by_filters(self, **filters) -> models.Model | None:
        return self.model.objects.filter(**filters).first()

    def get_queries_by_filters(self, **filters) -> QuerySet[models.Model]:
        return self.model.objects.filter(**filters)

    def create(self, **kwargs) -> models.Model:
        return self.model.objects.create(**kwargs)

    def update_by_id_with_fields_and_values(
        self,
        id: int,
        **fields_values,
    ) -> models.Model:
        return self.model.objects.filter(id=id).update(**fields_values)

    def delete_by_id(self, id: int) -> None:
        return self.model.objects.filter(id=id).delete()
