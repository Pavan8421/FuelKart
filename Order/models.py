from django.db import models

# Create your models here.

class Orders(models.Model):
  CustomerName = models.CharField(max_length=255)
  VehicleNumber = models.CharField(max_length=20)
  StartReading = models.IntegerField()
  EndReading = models.IntegerField()