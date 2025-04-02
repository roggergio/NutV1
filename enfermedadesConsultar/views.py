from django.shortcuts import render, redirect
from .forms import EnfermedadForm
from django.contrib.auth.decorators import login_required
from .models import Enfermedad

@login_required
def registrar_enfermedad(request):
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid():
            enfermedad = form.save(commit=False)
            enfermedad.nutriologo = request.user  # Relacionar con el nutriólogo logueado
            enfermedad.save()
            return redirect('enfermedades_listar')  # Cambia esta URL si necesitas otro destino
    else:
        form = EnfermedadForm()
    
    return render(request, 'enfermedadesConsultar/registrarEnfermedad.html', {'form': form})

@login_required
def listar_enfermedades(request):
    enfermedades = Enfermedad.objects.filter(nutriologo=request.user)
    return render(request, 'enfermedadesConsultar/listaEnfermedades.html', {'enfermedades': enfermedades})

@login_required
def editar_enfermedad(request, enfermedad_id):
    enfermedad = Enfermedad.objects.get(id=enfermedad_id, nutriologo=request.user)
    if request.method == 'POST':
        form = EnfermedadForm(request.POST, instance=enfermedad)
        if form.is_valid():
            form.save()
            return redirect('enfermedadesConsultar:listar_enfermedades')
    else:
        form = EnfermedadForm(instance=enfermedad)

    return render(request, 'enfermedadesConsultar/editarEnfermedad.html', {'form': form})


