from django.urls import path

from AppCoder.views import ProfesorCreateView, ProfesorDeleteView, ProfesorDetailView, ProfesorListView, ProfesorUpdateView, borrar_profesor, buscar, busqueda_camada, crear_curso, crear_profesor, cursos, cursos_formulario, inicio, modificar_profesor, profesores

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio, name='inicio'),
    path('cursos', cursos, name='cursos'),
    path('cursosFormulario', cursos_formulario, name='cursos_formulario'),
    path('busquedaCamada', busqueda_camada, name='busqueda_camada'),
    path('buscar', buscar, name='buscar'),
    path('profesores', ProfesorListView.as_view(), name='profesores'),
    path('profesores/add', ProfesorCreateView.as_view(), name='profesor_add'),
    path('profesores/delete/<pk>', ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('profesores/update/<pk>', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/view/<pk>', ProfesorDetailView.as_view(), name='profesor_view'),
]