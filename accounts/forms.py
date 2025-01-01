from django import forms
from .models import Account
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Password',
        'class' : 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Password',
        'class' : 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone_number','email','password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args,**kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'ingrese apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'ingrese telefono'
        self.fields['email'].widget.attrs['placeholder'] = 'ingrese email'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


    def validate_password_strength(password):
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
            raise forms.ValidationError("El password no coincide.")

        # Validar la fortaleza de la contraseña
        try:
            validate_password_strength(password)
        except ValidationError as e:
            self.add_error('password', e)

        return cleaned_data
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email.lower()


