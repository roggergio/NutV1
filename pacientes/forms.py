from django import forms
from .models import Paciente, Antropometria

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

    def clean_apellido_paterno(self):
        apellido = self.cleaned_data.get('apellido_paterno')
        if not apellido:
            raise forms.ValidationError("El apellido paterno es obligatorio.")
        return apellido

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        return nombre

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if not fecha:
            raise forms.ValidationError("La fecha de nacimiento es obligatoria.")
        return fecha

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            raise forms.ValidationError("El número de teléfono es obligatorio.")
        if not telefono.isdigit() or len(telefono) != 10:
            raise forms.ValidationError("El número de teléfono debe contener exactamente 10 dígitos numéricos.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El email es obligatorio.")

        # Si el formulario está editando un paciente existente
        if self.instance and self.instance.pk:
            if Paciente.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este email ya está registrado para otro paciente.")
        else:
            if Paciente.objects.filter(email=email).exists():
                raise forms.ValidationError("Este email ya está registrado para otro paciente.")
        
        return email


    def clean_genero(self):
        genero = self.cleaned_data.get('genero')
        if not genero:
            raise forms.ValidationError("El género es obligatorio.")
        return genero
    
    
    
class AntropometriaForm(forms.ModelForm):
    class Meta:
        model = Antropometria
        fields = ['peso', 'estatura', 'cintura', 'cadera', 'grasa_corporal', 'masa_muscular']
        widgets = {
            'peso': forms.NumberInput(attrs={'step': '0.01'}),
            'estatura': forms.NumberInput(attrs={'step': '0.1'}),
            'cintura': forms.NumberInput(attrs={'step': '0.1'}),
            'cadera': forms.NumberInput(attrs={'step': '0.1'}),
            'grasa_corporal': forms.NumberInput(attrs={'step': '0.1'}),
            'masa_muscular': forms.NumberInput(attrs={'step': '0.1'}),
        }