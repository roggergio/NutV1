from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Antropometria, Paciente
from .forms import PacienteForm, AntropometriaForm
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

@login_required
def datos_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/datosPaciente.html', {'paciente': paciente})



#---------------------------------------------------------------------------------------Antropometría
def registrar_antropometria(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if request.method == 'POST':
        peso = request.POST.get('peso')
        estatura = request.POST.get('estatura')
        cintura = request.POST.get('cintura')
        cadera = request.POST.get('cadera')
        grasa_corporal = request.POST.get('grasa_corporal')
        masa_muscular = request.POST.get('masa_muscular')

        # Calcular IMC y relación Cintura-Cadera
        imc = float(peso) / (float(estatura) / 100) ** 2
        if cintura and cadera:
            relacion_cc = float(cintura) / float(cadera)
        else:
            relacion_cc = None

        # Guardar los datos en la base de datos
        Antropometria.objects.create(
            paciente=paciente,
            peso=peso,
            estatura=estatura,
            imc=imc,
            cintura=cintura,
            cadera=cadera,
            relacion_cc=relacion_cc,
            grasa_corporal=grasa_corporal,
            masa_muscular=masa_muscular
        )

        return redirect('pacientes/datosPaciente.html', paciente_id=paciente.id)

    return render(request, 'antropometria.html', {'paciente': paciente})