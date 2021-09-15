from rest_framework import serializers
from task.models import Order, Pet, Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"

class PetSerializer(serializers.ModelSerializer):
    # pets = PriceSerializer()
    class Meta:
        model = Pet 
        fields = "__all__"

class OredrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = "__all__"



