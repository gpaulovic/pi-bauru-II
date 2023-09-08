from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ecopontos
from .serializers import EcopontosSerializer


@api_view(['GET'])
def getAll(request):
    ecopontos = Ecopontos.objects.all()
    serializer = EcopontosSerializer(ecopontos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get(request, id):
    try:
        ecoponto = Ecopontos.objects.get(id=id)
        serializer = EcopontosSerializer(ecoponto, many=True)
        return Response(serializer.data)
    except Ecopontos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save(request):
    serializer = EcopontosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update(request, id, *args, **kwargs):
    ecoponto = Ecopontos.objects.get(id=id)

    for campo, valor in request.data.items():
        if not valor == '':
            setattr(ecoponto, campo, valor)

    json_descarte = EcopontosSerializer(ecoponto)
    serializer = EcopontosSerializer(data=json_descarte.data, partial=True)
    if serializer.is_valid():
        serializer.update(ecoponto, serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        ecoponto = Ecopontos.objects.get(id=id)
    except Ecopontos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ecoponto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# redirect function
@login_required
def home(request):
    user = request.user.username
    vecopontos = Ecopontos.objects.all()
    return render(request, "ecopontos.html", {"ecopontos": vecopontos, "username": user})


# redirect function
def editar(request, id):
    user = request.user.username
    ecoponto = Ecopontos.objects.get(id=id)
    return render(request, "ecopontos-update.html", {"ecoponto": ecoponto, "username": user})


# redirect function
def deleteConfirm(request, id):
    user = request.user.username
    ecoponto = Ecopontos.objects.get(id=id)
    return render(request, "ecoponto-delete-confirm.html", {"ecoponto": ecoponto, "username": user})


