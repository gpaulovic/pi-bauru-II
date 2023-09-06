from rest_framework import serializers

from descartadores.models import Descartadores
from ecopontos.models import Ecopontos
from .models import Descartes


class DescartesSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(allow_blank=True)
    tipo = serializers.CharField(allow_blank=True)
    quantidade = serializers.CharField(allow_blank=True)
    descartador = serializers.CharField(source='descartador.documento', allow_blank=True)
    ecoponto = serializers.CharField(source='ecoponto.id', allow_blank=True)

    class Meta:
        model = Descartes
        fields = '__all__'

    def create(self, validated_data):
        descartador_data = validated_data.pop('descartador')
        descartador = Descartadores.objects.get(**descartador_data)

        ecoponto_data = validated_data.pop('ecoponto')
        ecoponto = Ecopontos.objects.get(**ecoponto_data)

        descarte = Descartes.objects.create(**validated_data, descartador=descartador, ecoponto=ecoponto)
        return descarte

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.quantidade = validated_data.get('quantidade', instance.quantidade)
        instance.save()
        return instance
