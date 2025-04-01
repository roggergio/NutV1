from django import forms

class MedicamentoForm(forms.Form):
    nombre_farmaco = forms.CharField()
    nombre_generico = forms.CharField()
    presentacion = forms.CharField()
    dosis = forms.CharField()
    frecuencia = forms.CharField()
    duracion = forms.CharField()
    via = forms.CharField()
    observaciones = forms.CharField(required=False)
