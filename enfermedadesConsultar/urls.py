from django.urls import path
from . import views
app_name = 'enfermedadesConsultar'
urlpatterns = [
    path('consultar/enfermedades/registrar/', views.registrar_enfermedad, name='registrar_enfermedad'),
    path('consultar/enfermedades/listar/', views.listar_enfermedades, name='listar_enfermedades'),
    path('consultar/enfermedades/editar/<int:enfermedad_id>/', views.editar_enfermedad, name='editar_enfermedad'),

]
