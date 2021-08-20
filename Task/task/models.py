from django.db import models
from django.db.models.fields import AutoField, IntegerField

# Create your models here.

class Pet(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Price(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.IntegerField()
    pet_model = models.ManyToManyField(Pet, related_name='pets')
    
        