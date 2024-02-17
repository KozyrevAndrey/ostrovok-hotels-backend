from django.contrib import admin

from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin[City]):
    list_display = (
        'id',
        'name',
    )
    search_fields = ['name']
