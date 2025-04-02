from django.urls import path
from . import views

urlpatterns = [
    path('consultar/bioquimicos/listar/', views.listar_bioquimicos, name='listar_bioquimicos'),
    path('consultar/bioquimicos/<int:bioquimico_id>/', views.detalle_bioquimico, name='detalle_bioquimico'),
]
