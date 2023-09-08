from django.views.generic import ListView,FormView
from django.views import View
from django.shortcuts import render
from .models import *
import googlemaps
from django.conf import settings
import json

class HomeView(ListView):
    template_name = "project_content/home.html"
    context_object_name = 'mydata'
    model = Locations
    #form_class = EmailForm
    success_url = "/"


class GeocodingView(View):
    template_name = "project_content/geocoding.html"

    def get(self, request, pk):
        location = Locations.objects.get(pk=pk)
        # Perform calculations or any other logic here

        # check whether we have the data in the database that we need to calculate the geocode
        if location.adress and location.country and location.zipcode and location.city != None: 
            # creating string of existing location data in database
            adress_string = str(location.adress)+", "+str(location.zipcode)+", "+str(location.city) +", "+str(location.country)
            print(adress_string)
            gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
            intermediate = json.dumps(gmaps.geocode(str(adress_string))) 
            intermediate2 = json.loads(intermediate)
            latitude = intermediate2[0]['geometry']['location']['lat']
            longitude = intermediate2[0]['geometry']['location']['lng']
            place_id = intermediate2[0]['place_id']
            #print(latitude)
            #print(longitude)

        context = {
            'location': location,
            'latitude': latitude, 
            'longitude': longitude, 
            'place_id':place_id,
            'geocoded_data': intermediate2,
        }
        return render(request, self.template_name, context)
