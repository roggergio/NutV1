from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm
from django.db.models import Q

@login_required
def lista_pacientes(request):
    query = request.GET.get('q')
    if query:
        pacientes = Paciente.objects.filter(
            Q(nutriologo=request.user) &
            (
                Q(nombre__icontains=query) |
                Q(apellido_paterno__icontains=query) |
                Q(apellido_materno__icontains=query) |
                Q(email__icontains=query)
            )
        )
    else:
        pacientes = Paciente.objects.filter(nutriologo=request.user)

    return render(request, 'pacientes/lista_pacientes.html', {
        'pacientes': pacientes,
        'query': query,
    })

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.nutriologo = request.user  # Asignar el nutriólogo actual
            paciente.save()
            messages.success(request, 'Paciente registrado correctamente.')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, nutriologo=request.user)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.nutriologo = request.user
            paciente.save()
            messages.success(request, 'Paciente actualizado correctamente.')
            return redirect('lista_pacientes')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'pacientes/crear_paciente.html', {'form': form, 'paciente': paciente})

@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, nutriologo=request.user)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado correctamente.')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirmar_eliminar.html', {'paciente': paciente})
