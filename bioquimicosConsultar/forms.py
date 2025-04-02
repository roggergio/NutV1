from django import forms
from .models import Bioquimico
from django.db import models


class BioquimicoForm(forms.ModelForm):
    class Meta:
        model = Bioquimico
        fields = '__all__'
        widgets = {
            field.name: forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
            if isinstance(field, models.CharField) or isinstance(field, models.FloatField)
            else forms.Textarea(attrs={'readonly': 'readonly', 'class': 'form-control'})
            for field in Bioquimico._meta.fields
        }
