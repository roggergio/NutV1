from django import forms
from .models import Toxicomania

class ToxicomaniaForm(forms.ModelForm):
    class Meta:
        model = Toxicomania
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        alcohol = cleaned_data.get('alcohol')
        tabaco = cleaned_data.get('tabaco')
        otro_check = cleaned_data.get('otro_check')

        if not (alcohol or tabaco or otro_check):
            raise forms.ValidationError("Debes seleccionar al menos una opción (alcohol, tabaco u otro).")
