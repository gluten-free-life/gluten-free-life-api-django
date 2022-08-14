from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    distributor = models.CharField(max_length=100)
    # price = models.CharField(max_length=100)
    # evaluation = models.CharField(max_length=100)

class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    distributor = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    evaluation = models.CharField(max_length=100)
    
    material = models.TextField(default="material")
    nutrition = models.TextField(default="nutrition")
    description = models.TextField(default="description")
    img = models.TextField(default="img")
    imgfile = models.TextField(default="imgfile")

    
