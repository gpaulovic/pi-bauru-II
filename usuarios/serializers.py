from django.utils import timezone
from rest_framework import serializers

from ecopontos.models import Ecopontos
from usuarios.models import Usuarios


class UsuariosSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_blank=True)
    name = serializers.CharField(allow_blank=True)
    document = serializers.CharField(allow_blank=True)
    date_joined = serializers.DateTimeField(default=timezone.now)
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    ecoponto = serializers.CharField(source='ecoponto.id', allow_blank=True)

    class Meta:
        model = Usuarios
        fields = '__all__'

    def create(self, validated_data):
        ecoponto_data = validated_data.pop('ecoponto')
        ecoponto = Ecopontos.objects.get(id=ecoponto_data['id'])

        usuario = Usuarios.objects.create(**validated_data, ecoponto=ecoponto)
        return usuario

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.document = validated_data.get('document', instance.document)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
