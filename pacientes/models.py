from django.db import models
from accounts.models import Account  # Importamos el modelo de usuario (nutriólogo)

class Paciente(models.Model):
    nutriologo = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='pacientes')
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True, null=True)
    motivo_consulta = models.TextField(blank=True, null=True)
    genero = models.CharField(
        max_length=1,
        choices=[('F', 'Femenino'), ('M', 'Masculino')],
        default='F'
    )
    escolaridad = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    
    # Características del paciente
    vegetariano = models.BooleanField(default=False)
    embarazo = models.BooleanField(default=False)
    deportista = models.BooleanField(default=False)
    adulto_mayor = models.BooleanField(default=False)
    pediatrico = models.BooleanField(default=False)
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} ({self.nutriologo.email})"
    
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

    def __str__(self):
        return f'Antropometría de {self.paciente.nombre} ({self.fecha})'