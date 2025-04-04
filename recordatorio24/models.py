from django.db import models
from pacientes.models import Paciente  # si ya tienes pacientes registrados

class Recordatorio24(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    horario = models.TimeField()
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.fecha} - {self.horario}"
