from django.db import models
from pacientes.models import Paciente  # Ajusta esto según cómo hayas nombrado tu modelo de paciente

FRECUENCIA_CHOICES = [
    ('dia', 'Día'),
    ('semana', 'Semana'),
    ('mes', 'Mes'),
    ('nunca', 'Nunca'),
]

class HabitoAlimenticio(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    alimento = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField(default=0)
    frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_CHOICES)

    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente} - {self.alimento} ({self.cantidad} - {self.frecuencia})"
