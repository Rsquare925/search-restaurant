from django.db import models


# Create your models here.
class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.JSONField()
    lat_long = models.CharField(max_length=255)
    full_details = models.JSONField()

    def __str__(self):
        return self.name
