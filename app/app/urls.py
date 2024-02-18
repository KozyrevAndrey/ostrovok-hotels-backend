from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('yasg.urls')),
    path('api/', include('hotels.urls')),
    path('api/', include('users.urls')),
    path('health/', include('health_check.urls')),
]
