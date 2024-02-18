from django.urls import path

from . import views

urlpatterns = [
    path('hotels/', views.HotelFilterView.as_view()),
]
