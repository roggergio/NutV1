from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'apellido_paterno', 'apellido_materno', 'nombre', 'fecha_nacimiento', 'telefono', 'email',
            'motivo_consulta', 'genero', 'escolaridad', 'ocupacion',
            'vegetariano', 'embarazo', 'deportista', 'adulto_mayor', 'pediatrico'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput(attrs={'maxlength': '10', 'type': 'number'}),
            'email': forms.EmailInput(),
        }
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit() or len(telefono) != 10:
            raise forms.ValidationError("El número de teléfono debe contener exactamente 10 dígitos.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Paciente.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado para otro paciente.")
        return email
