from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('yasg.urls')),

    path('health/', include('health_check.urls')),
]
