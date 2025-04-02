from .models import Antropometria
from django import forms
from django.core.exceptions import ValidationError

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