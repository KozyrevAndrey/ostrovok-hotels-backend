from django.urls import path

from . import views

urlpatterns = [
    path('users/register/', views.UserRegisterView.as_view()),
    path('users/auth/', views.UserAuthToken.as_view()),
]
