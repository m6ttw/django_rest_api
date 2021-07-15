from django.db import models

class Guitar(models.Model):
    brand = models.CharField(max_length=30)
    price = models.IntegerField()