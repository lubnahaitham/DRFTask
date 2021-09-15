from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from task.models import Pet
import json
from task.serializers import PetSerializer


class PetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.response = self.client.get(reverse('pet-pet:listing-pet'))
        self.pet = Pet.objects.create(name='test', gender='male')

    def test_get_all_pet(self):
        self.response = self.client.get(reverse('pet-pet:listing-pet'))
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        self.assertEqual(self.response.data, serializer.data)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_create_valid_pet(self):
        self.valid_payload = {
            'name': 'test name',
            'gender': 'test gender',
        }
        self.response = self.client.post(reverse('pet-pet:listing-pet'),
                                         data=json.dumps(self.valid_payload),
                                         content_type='application/json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        self.invalid_payload = {
            'name': '',
            'gender': 'test gender',
        }
        self.response = self.client.post(reverse('pet-pet:listing-pet'),
                                         data=json.dumps(self.invalid_payload),
                                         content_type='application/json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        self.valid_payload_update = {
            'name': 'sss',
            'gender': 'female',
        }
        self.response = self.client.put(reverse('pet-pet:detail-pet', kwargs={'pk': '5'}),
                                        data=json.dumps(self.valid_payload_update),
                                        content_type='application/json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        self.invalid_payload_update = {
            'name': '',
            'gender': 'test male',
        }
        self.response = self.client.put(reverse('pet-pet:detail-pet', kwargs={'pk': '10'}),
                                        data=json.dumps(self.invalid_payload_update),
                                        content_type='application/json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

