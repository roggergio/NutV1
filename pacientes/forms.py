from django import forms
from django.core.exceptions import ValidationError
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ['nutriologo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'},
                format='%Y-%m-%d'),
            'telefono': forms.TextInput(attrs={
            'class': 'form-control',
            'maxlength': '10'
        }),
            'email': forms.EmailInput()
        }

    def clean_apellido_paterno(self):
        valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ')

        apellido = self.cleaned_data.get('apellido_paterno')
        if not apellido:
            raise ValidationError("El apellido Paterno es obligatorio.")

        apellido = apellido.strip()
        if len(apellido) < 3:
            raise ValidationError("El Apellido Paterno debe tener al menos 3 caracteres.")

        for char in apellido:
            if char.upper() not in valid_chars and char != " ":
                raise ValidationError("El Apellido Paterno no debe contener caracteres especiales.")
        return apellido

    def clean_apellido_materno(self):
        valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ')

        apellido_materno = self.cleaned_data.get('apellido_materno')
        if not apellido_materno:
            raise ValidationError("El apellido Materno es obligatorio.")

        apellido_materno = apellido_materno.strip()
        if len(apellido_materno) < 3:
            raise ValidationError("El Apellido Materno debe tener al menos 3 caracteres.")

        for char in apellido_materno:
            if char.upper() not in valid_chars and char != " ":
                raise ValidationError("El Apellido Materno no debe contener caracteres especiales.")
        return apellido_materno

    def clean_nombre(self):
        valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ')

        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError("El Nombre es obligatorio.")

        nombre = nombre.strip()
        if len(nombre) < 3:
            raise ValidationError("El Nombre debe tener al menos 3 caracteres.")

        for char in nombre:
            if char.upper() not in valid_chars and char != " ":
                raise ValidationError("El Nombre no debe contener caracteres especiales.")
        return nombre

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if not fecha:
            raise forms.ValidationError("La fecha de nacimiento es obligatoria.")
        return fecha

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            raise ValidationError("El número de teléfono es obligatorio.")
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValidationError("El número de teléfono debe contener exactamente 10 dígitos.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        return email

    def clean_motivo_consulta(self):
        motivo_consulta = self.cleaned_data.get('motivo_consulta')
        if not motivo_consulta:
            raise ValidationError("Debe incluir el motivo de la consulta.")
        if len(motivo_consulta) <= 2:
            raise ValidationError("El motivo de la consulta debe ser especifico.")
        return motivo_consulta