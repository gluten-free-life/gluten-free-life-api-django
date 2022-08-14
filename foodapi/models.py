from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    distributor = models.CharField(max_length=100)
    # price = models.CharField(max_length=100)
    # evaluation = models.CharField(max_length=100)



    
