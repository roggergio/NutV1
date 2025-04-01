from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from pacientes.models import Paciente
from django.core.exceptions import PermissionDenied

def registrar_medicamentos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")

    if request.method == 'POST':
        nombres = request.POST.getlist('nombre_farmaco[]')
        genericos = request.POST.getlist('nombre_generico[]')
        presentaciones = request.POST.getlist('presentacion[]')
        dosis = request.POST.getlist('dosis[]')
        frecuencias = request.POST.getlist('frecuencia[]')
        duraciones = request.POST.getlist('duracion[]')
        vias = request.POST.getlist('via[]')
        observaciones = request.POST.getlist('observaciones[]')

        for i in range(len(nombres)):
            Medicamento.objects.create(
                paciente=paciente,
                nombre_farmaco=nombres[i],
                nombre_generico=genericos[i],
                presentacion=presentaciones[i],
                dosis=dosis[i],
                frecuencia=frecuencias[i],
                duracion=duraciones[i],
                via=vias[i],
                observaciones=observaciones[i] if observaciones[i] else ""
            )

        return redirect('detalle_paciente', paciente_id=paciente.id)  # O la vista que desees

    return render(request, 'medicamentos/formulario_medicamentos.html', {'paciente': paciente})

def lista_medicamentos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")
    medicamentos = paciente.medicamentos.all().order_by('-fecha_registro')  # si agregamos fecha
    return render(request, 'medicamentos/lista_medicamentos.html', {
        'paciente': paciente,
        'medicamentos': medicamentos
    })