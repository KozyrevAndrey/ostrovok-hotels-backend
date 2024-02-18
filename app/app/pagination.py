from collections import OrderedDict

from django.db.models.query import QuerySet
from rest_framework import serializers, views
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.response import Response


def get_paginated_response(
    *,
    pagination_class: LimitOffsetPagination,
    serializer_class: serializers,
    queryset: QuerySet,
    request: Request,
    view: views,
) -> Response:
    paginator = pagination_class()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(
            instance=page,
            many=True,
            context={'request': request},
        )
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(
        queryset,
        many=True,
        context={'request': request},
    )

    return Response(data=serializer.data)


class CustomOffsetPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 100

    def get_paginated_data(self, data) -> OrderedDict:
        return OrderedDict(
            [
                ('limit', self.limit),
                ('offset', self.offset),
                ('count', self.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
                ('results', data),
            ],
        )

    def get_paginated_response(self, data) -> Response:
        """
        We redefine this method in order to return `limit` and `offset`.
        This is used by the frontend to construct the pagination itself.
        """
        return Response(
            OrderedDict(
                [
                    ('limit', self.limit),
                    ('offset', self.offset),
                    ('count', self.count),
                    ('next', self.get_next_link()),
                    ('previous', self.get_previous_link()),
                    ('results', data),
                ],
            ),
        )
