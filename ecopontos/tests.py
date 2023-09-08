from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Ecopontos
from .serializers import EcopontosSerializer


class EcopontosTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ecopontos_data = {
            'cep': 'CEP Teste',
            'bairro': 'Bairro Teste',
            'endereco': 'Endereço Teste',
            'situacao': 'Situação',
        }
        self.ecopontos = Ecopontos.objects.create(**self.ecopontos_data)

    def test_list_ecopontos(self):
        response = self.client.get(reverse('home-ecopontos'))
        ecopontos = Ecopontos.objects.all()
        serializer = EcopontosSerializer(ecopontos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ecoponto(self):
        response = self.client.post(reverse('save-ecoponto'), self.ecopontos_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_ecoponto(self):
        response = self.client.get(reverse('get-ecoponto', kwargs={'id': self.ecopontos.pk}))
        ecoponto = Ecopontos.objects.get(pk=self.ecopontos.pk)
        serializer = EcopontosSerializer(ecoponto)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_ecoponto(self):
        updated_data = {
            'cep': 'Novo CEP',
            'bairro': 'Novo Bairro',
            'endereco': 'Novo Endereço',
            'situacao': 'Nova Situa',
        }
        response = self.client.patch(reverse('update-ecoponto', kwargs={'id': self.ecopontos.id}), updated_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ecoponto(self):
        response = self.client.delete(reverse('delete-ecoponto', kwargs={'id': self.ecopontos.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ecopontos.objects.filter(pk=self.ecopontos.pk).exists())
