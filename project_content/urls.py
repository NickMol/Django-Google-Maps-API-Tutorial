from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='my_home_view'), 
    path("geocoding/<int:pk>", GeocodingView.as_view(), name='my_geocoding_view'), 
    path("distance", DistanceView.as_view(), name='my_distance_view'), 
    path("map", MapView.as_view(), name='my_map_view'), 
   
   

]