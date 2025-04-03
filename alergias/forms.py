from django import forms
from django.core.exceptions import ValidationError
from .models import Alergia

class AlergiaForm(forms.ModelForm):
    class Meta:
        model = Alergia
        exclude = ['paciente']
        widgets = {
            'fecha_diagnostico': forms.DateInput(attrs={'type': 'date'},
                format='%Y-%m-%d')
        }
        
    def clean_nombre(self):
            valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ')

            nombre = self.cleaned_data.get('nombre')
            if not nombre or nombre.strip() == "":
                raise ValidationError("El Nombre es obligatorio.")

            nombre = nombre.strip()
            if len(nombre) < 3:
                raise ValidationError("El Nombre debe tener al menos 3 caracteres.")

            for char in nombre:
                if char.upper() not in valid_chars and char != " ":
                    raise ValidationError("El Nombre no debe contener caracteres especiales o números.")
            return nombre
        
    def clean_reaccion(self):

            reaccion = self.cleaned_data.get('reaccion')
            if not reaccion or reaccion.strip() == "":
                raise ValidationError("La descripción de la reaccion es obligatoria.")

            reaccion = reaccion.strip()
            if len(reaccion) < 3:
                raise ValidationError("La descripción de la reaccion debe tener al menos 3 caracteres.")
            return reaccion
    
    def clean_gravedad(self):

            gravedad = self.cleaned_data.get('gravedad')
            if not gravedad or gravedad.strip() == "":
                raise ValidationError("Es obligatorio seleccionar la gravedad de la alergia.")

            #gravedad = gravedad.strip()
            #if len(gravedad) < 3:
            #    raise ValidationError("La descripción de la gravedad debe tener al menos 3 caracteres.")
            return gravedad