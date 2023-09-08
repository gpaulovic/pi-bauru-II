from rest_framework import serializers

from ecopontos.models import Ecopontos


class EcopontosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecopontos
        fields = '__all__'
