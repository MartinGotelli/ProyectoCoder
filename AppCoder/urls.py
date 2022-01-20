from django.urls import path

from AppCoder.views import buscar, busqueda_camada, crear_curso, cursos, cursos_formulario, inicio

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio, name='inicio'),
    path('cursos', cursos, name='cursos'),
    path('cursosFormulario', cursos_formulario, name='cursos_formulario'),
    path('busquedaCamada', busqueda_camada, name='busqueda_camada'),
    path('buscar', buscar, name='buscar')
]