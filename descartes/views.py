from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Descartes
from .serializers import DescartesSerializer


@api_view(['GET'])
def getAll(request):
    vdescartes = Descartes.objects.all()
    serializer = DescartesSerializer(vdescartes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get(request, id):
    try:
        vdescarte = Descartes.objects.get(id=id)
        serializer = DescartesSerializer(vdescarte)
        return Response(serializer.data)
    except Descartes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save(request):
    serializer = DescartesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update(request, id, *args, **kwargs):
    descarte = Descartes.objects.get(id=id)

    for campo, valor in request.data.items():
        if not valor == '':
            setattr(descarte, campo, valor)

    json_descarte = DescartesSerializer(descarte)
    serializer = DescartesSerializer(data=json_descarte.data, partial=True)
    if serializer.is_valid():
        serializer.update(descarte, serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        descarte = Descartes.objects.get(id=id)
    except Descartes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    descarte.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# redirect function
@login_required
def home(request):
    user = request.user.username
    vdescartes = Descartes.objects.all()
    return render(request, "descartes.html", {"descartes": vdescartes, "username": user})


# redirect function
def editar(request, id):
    user = request.user.username
    vdescartes = Descartes.objects.get(id=id)
    return render(request, "descartes-update.html", {"descartes": vdescartes, "username": user})


# redirect function
def deleteConfirm(request, id):
    user = request.user.username
    descarte = Descartes.objects.get(id=id)
    return render(request, "descartes-delete-confirm.html", {"descarte": descarte, "username": user})

