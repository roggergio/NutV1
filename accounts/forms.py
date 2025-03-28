from django import forms
from .models import Account
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Password',
        'class': 'form-control',
    }))

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese teléfono (10 dígitos)',
            'class': 'form-control',
            'maxlength': '10',
            'type': 'number',
        }),
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="El número de teléfono debe tener exactamente 10 dígitos."
            )
        ],
    )

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'email',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        array = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'Ñ','Á','É','Í','Ó','Ú','Ü'
        ]

        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError("El nombre es obligatorio.")
        if len(first_name) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        for char in first_name:
            if char.upper() not in array:
                raise ValidationError("Nombre no se acepta carateres especiales")
        return first_name

    def clean_last_name(self):
        array = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'Ñ','Á','É','Í','Ó','Ú','Ü'
        ]
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError("El apellido es obligatorio.")
        if len(last_name) < 3:
            raise ValidationError("El apellido debe tener al menos 3 caracteres.")
        for char in last_name:
            if char.upper() not in array:
                raise ValidationError("Apellido no se acepta carateres especiales")
        return last_name

    def validate_password_strength(self, password):
        if len(password) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if not any(char.isdigit() for char in password):
            raise ValidationError('La contraseña debe incluir al menos un número.')
        if not any(char.isalpha() for char in password):
            raise ValidationError('La contraseña debe incluir al menos una letra.')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "El password no coincide.")

        # Validar la fortaleza de la contraseña
        try:
            self.validate_password_strength(password)
        except ValidationError as e:
            self.add_error('password', e)

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise ValidationError("El email ya está registrado.")
        return email.lower()
