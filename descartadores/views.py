from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Descartadores
from .serializers import DescartadoresSerializer


class DescartadoresPartialUpdateView(generics.UpdateAPIView):
    queryset = Descartadores.objects.all()
    serializer_class = DescartadoresSerializer


@api_view(['GET'])
def getAll(request):
    vdescartadores = Descartadores.objects.all()
    serializer = DescartadoresSerializer(vdescartadores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get(request, documento):
    try:
        vdescartador = Descartadores.objects.get(documento=documento)
        serializer = DescartadoresSerializer(vdescartador)
        return Response(serializer.data)
    except Descartadores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# redirect function
@login_required
def home(request):
    user = request.user.username
    vdescartadores = Descartadores.objects.all()
    return render(request, "descartadores.html", {"descartadores": vdescartadores, "username": user})


@api_view(['POST'])
def save(request):
    serializer = DescartadoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update(request, documento, *args, **kwargs):
    descartador = Descartadores.objects.get(documento=documento)

    for campo, valor in request.data.items():
        if not valor == '':
            setattr(descartador, campo, valor)

    json_descartador = DescartadoresSerializer(descartador)
    serializer = DescartadoresSerializer(data=json_descartador.data, partial=True)
    if serializer.is_valid():
        serializer.update(descartador, serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# redirect function
def editar(request, documento):
    user = request.user.username
    vdescartador = Descartadores.objects.get(documento=documento)
    return render(request, "descartadores-update.html", {"descartador": vdescartador, "username": user})


@api_view(['GET', 'DELETE'])
def delete(request, documento):
    try:
        vdescartador = Descartadores.objects.get(documento=documento)
    except Descartadores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    vdescartador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# redirect function
def deleteConfirm(request, documento):
    descartador = Descartadores.objects.get(documento=documento)
    return render(request, "descartadores-delete-confirm.html", {"descartador": descartador})
