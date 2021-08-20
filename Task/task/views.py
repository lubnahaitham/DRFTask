from rest_framework import viewsets
from rest_framework import permissions
from task.serializers import PetSerializer, PriceSerializer
from task.models import Pet, Price
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('name')
    serializer_class = PetSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
@csrf_exempt
def pet_list(request):
    """
    List all, or create a new 
    """
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def pet_detail(request, pk):
    """
    Retrieve, update or delete a code.
    """
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PetSerializer(pet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pet.delete()
        return HttpResponse(status=204)


class PriceViewSet(viewsets.ModelViewSet):
    
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
    
@csrf_exempt
def price_list(request):
    """
    List all, or create a new 
    """
    if request.method == 'GET':
        prices = Price.objects.all()
        serializer = PetSerializer(prices, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PriceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def price_detail(request, pk):
    """
    Retrieve, update or delete a code.
    """
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PriceSerializer(price)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PriceSerializer(price, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        price.delete()
        return HttpResponse(status=204)