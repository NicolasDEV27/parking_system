from django.db import models
from django.utils import timezone


class CarrosDentro(models.Model):
    id = models.BigAutoField(primary_key=True)
    placa = models.CharField(unique=True, max_length=6)
    ultima_entrada = models.DateTimeField(default=timezone.now)

class RegistroHistorico(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    car_placa = models.CharField(unique=True, max_length=6, null=False)
    status = models.SmallIntegerField(default=1)
    ultima_entrada = models.DateTimeField(default=timezone.now)
    
