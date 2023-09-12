import time

from django.utils import timezone
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Usuarios
from ecopontos.models import Ecopontos
from .serializers import UsuariosSerializer


class UsuariosTests(APITestCase):
    def setUp(self):
        self.ecoponto_data = {
            'id': '1',
        }
        self.ecoponto = Ecopontos.objects.create(**self.ecoponto_data)
        self.usuario_data = {
            'id': 1,
            'name': 'Usuário Test',
            'document': '45412164877',
            'email': 'usuarioTest@example.com',
            'date_joined': '2023-09-11',
            'is_staff': True,
            'is_active': True,
            'ecoponto': self.ecoponto,
        }
        self.usuario = Usuarios.objects.create(**self.usuario_data)
        self.url = reverse('save-usuarios')

    def test_list_usuarios(self):
        response = self.client.get(reverse('get-all-usuarios'))
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_usuario(self):
        data = {
            'name': 'Novo Usuário',
            'document': '98765432109',
            'email': 'novo_usuario@example.com',
            'date_joined': '2023-09-11',
            'is_staff': False,
            'is_active': True,
            'ecoponto': self.ecoponto.id,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_usuario(self):
        response = self.client.get(reverse('get-usuarios', kwargs={'id': self.usuario.id}))
        usuario = Usuarios.objects.get(id=self.usuario.id)
        serializer = UsuariosSerializer(usuario)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_usuario(self):
        url = reverse('update-usuarios', args=[self.usuario.id])
        data = {
            'name': 'Novo Usuário',
            'document': '98765432109',
            'email': 'novo_usuario@example.com',
            'date_joined': '2023-09-11',
            'is_staff': False,
            'is_active': True,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_usuario(self):
        url = reverse('delete-usuarios', args=[self.usuario.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
