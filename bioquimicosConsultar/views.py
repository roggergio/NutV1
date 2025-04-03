from django.views.generic import ListView, DetailView
from .models import Bioquimico
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Bioquimico

@login_required
def listar_bioquimicos(request):
    bioquimicos = Bioquimico.objects.all()
    return render(request, 'bioquimicosConsultar/listarBioquimicos.html', {'bioquimicos': bioquimicos})

@login_required
def detalle_bioquimico(request, bioquimico_id):
    bioquimico = get_object_or_404(Bioquimico, pk=bioquimico_id)
    return render(request, 'bioquimicosConsultar/detalleBioquimico.html', {'bioquimico': bioquimico})

