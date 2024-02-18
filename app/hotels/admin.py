from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin[Hotel]):
    list_display = (
        'id',
        'name',
        'address',
        'phone_number',
        'get_city_name',
    )

    @admin.display(description='City Name')
    def get_city_name(self, obj: Hotel) -> str:
        return obj.city.name
