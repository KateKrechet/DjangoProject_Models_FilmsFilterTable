from django.db import models

# Create your models here.
class Movie(models.Model):
    country = models.CharField(max_length=15)
    title = models.CharField(max_length=20)
    year = models.IntegerField(max_length=4)