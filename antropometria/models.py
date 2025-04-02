from django.db import models
from pacientes.models import Paciente

class Antropometria(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cadera = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    relacion_cc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_corporal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    masa_muscular = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('paciente', 'fecha')


    def __str__(self):
        return f'Antropometría de {self.paciente.nombre} ({self.fecha})'