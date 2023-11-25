from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recette(models.Model):
    title = models.CharField(max_length=200)
    dureePreparation = models.IntegerField(null=True)
    image_url = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    ingredients = models.CharField(max_length=1000, null=True)
    etapePreparation = models.CharField(max_length=500, default='')




