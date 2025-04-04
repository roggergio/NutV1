from django.shortcuts import render, redirect, get_object_or_404
from .models import Recordatorio24
from .forms import Recordatorio24Form
from django.forms import modelformset_factory
from pacientes.models import Paciente  # Asegúrate de importar el modelo

def registrar_r24(request, paciente_id):
    RecordatorioFormSet = modelformset_factory(Recordatorio24, form=Recordatorio24Form, extra=1, can_delete=True)

    paciente = Paciente.objects.get(id=paciente_id)  # 

    if request.method == 'POST':
        formset = RecordatorioFormSet(request.POST, queryset=Recordatorio24.objects.none())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.paciente = paciente
                instance.save()
            return redirect('alguna_url')  # Puedes redirigir a 'datos_paciente' también si lo deseas
    else:
        formset = RecordatorioFormSet(queryset=Recordatorio24.objects.none())

    return render(request, 'recordatorio24/r24Form.html', {
        'formset': formset,
        'paciente': paciente  # 👈 Incluye el paciente en el contexto
    })

def ver_r24(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    registros = Recordatorio24.objects.filter(paciente=paciente).order_by('-fecha', '-horario')
    return render(request, 'recordatorio24/verR24.html', {
        'paciente': paciente,
        'registros': registros
    })