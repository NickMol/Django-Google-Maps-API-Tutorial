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

    def __str__(self):
        return self.name
    
