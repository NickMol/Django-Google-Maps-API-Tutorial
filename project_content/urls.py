from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='my_home_view')
    #path("geocoding", GeocodingView.as_view(), name='my_geocoding_view')

]