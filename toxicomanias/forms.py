import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Toxicomania

class ToxicomaniaForm(forms.ModelForm):
    class Meta:
        model = Toxicomania
        exclude = ['paciente']
        widgets = {
            'alcohol_veces': forms.TextInput(attrs={'type': 'text'}),
            'tabaco_veces': forms.TextInput(attrs={'type': 'text'}),
            'otro_veces': forms.TextInput(attrs={'type': 'text'}),
        }

    def clean_alcohol_veces(self):
        return self.validar_veces('alcohol', 'alcohol_veces')
    
    def clean_tabaco_veces(self):
        return self.validar_veces('tabaco', 'tabaco_veces')

    def clean_otro_veces(self):
        return self.validar_veces('otro_check', 'otro_veces')

    def clean_otro(self):
        return self.validar_otro_check('otro')

    def validar_veces(self, nombre_check, nombre_veces):
        check = self.cleaned_data.get(nombre_check)
        veces = self.cleaned_data.get(nombre_veces)

        if check:
            if veces is None or not str(veces).isdigit() or int(veces) < 1:
                raise ValidationError(f"El número de veces de {nombre_check} debe ser un número mayor a 0.")
            return int(veces)
        return veces

    def validar_otro_check(self, nombre_campo):
        valor = self.cleaned_data.get(nombre_campo)
        if valor:
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ ]+$', valor):
                raise ValidationError(f"El campo {nombre_campo} solo puede contener letras y espacios, sin caracteres especiales.")
            if len(valor) < 3:
                raise ValidationError("El campo otro debe tener al menos 3 caracteres.")
        return valor

    #def validar_frecuencia(self, nombre_check, nombre_frec):
    #    check = self.cleaned_data.get(nombre_check)
    #    frecuencia = self.cleaned_data.get(nombre_frec)
    #    
    #    if check and (not frecuencia or frecuencia == 'nunca'):
    #        raise ValidationError(f"Selecciona una frecuencia válida para {nombre_check}.")
    #    return frecuencia
