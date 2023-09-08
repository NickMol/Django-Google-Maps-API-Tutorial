from django.db import models

class Locations(models.Model):
    club = models.CharField(max_length=500,blank=True, null=True)
    name = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    place_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name
    

class Distances(models.Model):
    from_location = models.ForeignKey(Locations, related_name = "from_location", on_delete=models.CASCADE)
    to_location = models.ForeignKey(Locations, related_name = "to_location", on_delete=models.CASCADE)
    mode = models.CharField(max_length=200,blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    duration_mins = models.DecimalField(max_digits=10, decimal_places=2)
    duration_traffic_mins = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
