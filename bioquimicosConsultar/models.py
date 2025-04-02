from django.db import models

class Bioquimico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor_inferior_normal = models.FloatField()
    valor_superior_normal = models.FloatField()
    tratamiento_deficiente = models.TextField()
    tratamiento_superior = models.TextField()
    bibliografia = models.TextField()

    def __str__(self):
        return self.nombre
