from django.db import models

class Guitar(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()