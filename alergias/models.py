from django.db import models
from pacientes.models import Paciente  # Asegúrate de importar correctamente tu modelo de paciente

class Alergia(models.Model):
    GRAVEDAD_CHOICES = [
        ('leve', 'Leve'),
        ('moderada', 'Moderada'),
        ('grave', 'Grave'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='alergias')
    nombre = models.CharField(max_length=100)
    reaccion = models.TextField(blank=True, null=True)
    gravedad = models.CharField(max_length=10, choices=GRAVEDAD_CHOICES)
    fecha_diagnostico = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.paciente.nombre}"
