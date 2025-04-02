from django.db import models
from pacientes.models import Paciente

FRECUENCIA_CHOICES = [
    ('nunca', 'Nunca'),
    ('diario', 'Diario'),
    ('semana', 'Semanal'),
    ('mes', 'Mensual'),
    ('año', 'Anual'),
]

class Toxicomania(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    alcohol = models.BooleanField(default=False)
    alcohol_veces = models.IntegerField(null=True, blank=True)
    #alcohol_veces = models.CharField(max_length=10, null=True, blank=True)
    alcohol_frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES, default='nunca', blank=True)
    
    tabaco = models.BooleanField(default=False)
    tabaco_veces = models.IntegerField(null=True, blank=True)
    tabaco_frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES, default='nunca', blank=True)

    otro = models.CharField(max_length=100, blank=True)
    otro_check = models.BooleanField(default=False)
    otro_veces = models.IntegerField(null=True, blank=True)
    otro_frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES, default='nunca', blank=True)

    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Toxicomanías de {self.paciente.nombre}"
