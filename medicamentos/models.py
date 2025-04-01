from django.db import models
from pacientes.models import Paciente  # Ajusta el nombre si tu app de pacientes se llama diferente
from django.utils import timezone

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='medicamentos')
    nombre_farmaco = models.CharField(max_length=100)
    nombre_generico = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=50)
    duracion = models.CharField(max_length=100)
    via = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre_farmaco} para {self.paciente.nombre}"

