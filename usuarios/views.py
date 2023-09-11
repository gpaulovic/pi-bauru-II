from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer


@api_view(['POST'])
def save(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAll(request):
    usuario = Usuarios.objects.all()
    serializer = UsuariosSerializer(usuario, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get(request, id):
    try:
        usuario = Usuarios.objects.get(id=id)
        serializer = UsuariosSerializer(usuario, many=True)
        return Response(serializer.data)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update(request, id, *args, **kwargs):
    usuario = Usuarios.objects.get(id=id)

    for campo, valor in request.data.items():
        if not valor == '':
            setattr(usuario, campo, valor)

    json_descarte = UsuariosSerializer(usuario)
    serializer = UsuariosSerializer(data=json_descarte.data, partial=True)
    if serializer.is_valid():
        serializer.update(usuario, serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        usuario = Usuarios.objects.get(id=id)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# redirect function
@login_required
def home(request):
    user = request.user.username
    vusuarios = Usuarios.objects.all()
    return render(request, "usuarios.html", {"usuarios": vusuarios, "username": user})


# redirect function
def editar(request, id):
    user = request.user.username
    vusuarios = Usuarios.objects.get(id=id)
    return render(request, "usuarios-update.html", {"usuario": vusuarios, "username": user})


# redirect function
def deleteConfirm(request, id):
    user = request.user.username
    usuario = Usuarios.objects.get(id=id)
    return render(request, "usuario-delete-confirm.html", {"usuario": usuario, "username": user})
