
from django.urls import path
from .views import update_location, get_positions, map_view

urlpatterns = [
    path("update_location/", update_location, name="update_location"),
    path("get_positions/", get_positions, name="get_positions"),
    path("", map_view, name="map"),          # /map/ ga render
]