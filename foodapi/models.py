from django.db import models

# Create your models here.


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

# Create your models here.
class User(models.Model):
    uid = models.CharField(unique=True,max_length=255)
    
 # Create your models here.
class Wishlist(models.Model):
    user_uid = models.CharField(max_length=255)
    food_id = models.IntegerField()

