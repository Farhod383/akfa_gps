from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tracking.urls")),  # /api/update_location, /api/get_positions
    path("map/", include("tracking.urls")),  # /map/
]