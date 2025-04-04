from django.db import models
from pacientes.models import Paciente

# Enfermedades fijas relacionadas con síndrome metabólico
ENFERMEDADES_BASE = [
    ('diabetes', 'Diabetes'),
    ('hipertension', 'Hipertensión'),
    ('colesterolemia', 'Colesterolemia'),
    ('trigliceridemia', 'Trigliceridemia'),
    ('obesidad', 'Obesidad'),
]

FAMILIARES = [
    ('paciente', 'Paciente'),
    ('padre', 'Padre'),
    ('madre', 'Madre'),
    ('abuelos_paternos', 'Abuelos paternos'),
    ('abuelos_maternos', 'Abuelos maternos'),
    ('hermanos', 'Hermanos'),
]

class AntecedentePatologico(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name='antecedentes')

    # Campos para enfermedades base
    diabetes = models.JSONField(default=dict)
    hipertension = models.JSONField(default=dict)
    colesterolemia = models.JSONField(default=dict)
    trigliceridemia = models.JSONField(default=dict)
    obesidad = models.JSONField(default=dict)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Antecedentes de {self.paciente}"


class OtraEnfermedad(models.Model):
    antecedente = models.ForeignKey(AntecedentePatologico, on_delete=models.CASCADE, related_name='otras_enfermedades')
    nombre = models.CharField(max_length=100)
    presencia = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.nombre} - {self.antecedente.paciente}"
