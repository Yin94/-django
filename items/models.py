from django.db import models

# Create your models here.

# serializer decode http data structure to python data structure


class Item (models.Model):
    name = models.CharField(max_length=15)
    price = models.CharField(max_length=20)
