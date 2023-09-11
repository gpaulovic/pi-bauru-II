from django.db import models
from django.utils import timezone

from ecopontos.models import Ecopontos


class Usuarios(models.Model):
    name = models.CharField(default='-', max_length=30)
    document = models.CharField(default='-', max_length=15)
    email = models.CharField(default='-', max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default='false', max_length=30)
    is_active = models.BooleanField(default='true', max_length=30)
    ecoponto = models.ForeignKey(Ecopontos, on_delete=models.CASCADE)

