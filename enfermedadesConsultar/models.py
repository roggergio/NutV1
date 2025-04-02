from django.db import models
from accounts.models import Account  # Tu modelo de nutriólogo

class Enfermedad(models.Model):
    nutriologo = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='enfermedades')
    nombre = models.CharField(max_length=100)
    descripcion_enfer = models.TextField()
    tratamiento_nut = models.TextField()
    bibliografia = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
