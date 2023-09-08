from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Descartadores
from .serializers import DescartadoresSerializer


class DescartadoresTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.descartador_data = {
            'nome': 'Nome Teste',
            'documento': 12345,
            'email': 'teste@example.com',
            'endereco': 'Endereço Teste'
        }
        self.response = self.client.post(
            reverse('save-descartadores'),
            self.descartador_data,
            format='json'
        )

    def test_create_descartador(self):
        new_descartador_data = {
            'nome': 'Nome Teste',
            'documento': 3435,
            'email': 'teste@example.com',
            'endereco': 'Endereço Teste'
        }
        response = self.client.post(reverse('save-descartadores'), new_descartador_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_descartadores(self):
        response = self.client.get(reverse('get-all-descartadores'))
        descartadores = Descartadores.objects.all()
        serializer = DescartadoresSerializer(descartadores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_descartador_detail(self):
        descartador = Descartadores.objects.get(documento=self.descartador_document)
        response = self.client.get(
            reverse('delete-descartadores', kwargs={'documento': descartador.documento}))
        serializer = DescartadoresSerializer(descartador)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
