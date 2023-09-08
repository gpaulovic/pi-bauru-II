from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ecopontos.models import Ecopontos
from .models import Descartes, Descartadores
from .serializers import DescartesSerializer


class DescartesTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.descartador_data = {
            'nome': 'descartador Teste',
            'documento': '12345'
        }
        self.descartador = Descartadores.objects.create(**self.descartador_data)

        self.ecoponto_data = {
            'id': '1',
        }
        self.ecoponto = Ecopontos.objects.create(**self.ecoponto_data)

        self.descarte_data = {
            'descartador': self.descartador,
            'ecoponto': self.ecoponto,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 1,
            'id': 1
        }
        self.descarte = Descartes.objects.create(**self.descarte_data)

    def test_list_descartes(self):
        response = self.client.get(reverse('get-all-descartes'))
        descarte = Descartes.objects.all()
        serializer = DescartesSerializer(descarte, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_descarte(self):
        new_descarte_data = {
            'descartador': self.descartador.documento,
            'ecoponto': self.ecoponto.id,
            'nome': 'Novo Descarte',
            'tipo': 'Novo Tipo',
            'quantidade': 5,
        }
        response = self.client.post(reverse('save-descartes'), new_descarte_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_descarte(self):
        response = self.client.get(reverse('get-descartes', kwargs={'id': self.descarte.id}))
        descarte = Descartes.objects.get(id=self.descarte.id)
        serializer = DescartesSerializer(descarte)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_descarte(self):
        updated_data = {
            'nome': 'Novo Nome',
            'tipo': 'Novo Tipo',
            'quantidade': 20,
        }
        response = self.client.patch(reverse('update-descartes', kwargs={'id': self.descarte.id}), updated_data,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_descarte(self):
        response = self.client.delete(reverse('delete-descartes', kwargs={'id': self.descarte.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Descartes.objects.filter(id=self.descarte.id).exists())
