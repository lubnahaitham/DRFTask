from django.db import models

# Create your models here.
   
class Price(models.Model):
    price = models.IntegerField()

class Pet(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.OneToOneField(Price, on_delete=models.CASCADE, primary_key = True)

    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, default=False)
    
        
