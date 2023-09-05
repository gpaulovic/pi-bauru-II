from rest_framework import serializers

from .models import Descartadores


class DescartadoresSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(allow_blank=True)
    documento = serializers.IntegerField(validators=[])
    email = serializers.CharField(allow_blank=True)
    endereco = serializers.CharField(allow_blank=True)

    class Meta:
        model = Descartadores
        fields = ['nome', 'documento', 'email', 'endereco']
