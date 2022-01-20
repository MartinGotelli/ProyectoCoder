from django.shortcuts import render, redirect

from django.http import HttpResponse

from AppCoder.forms import CursoForm, ProfesorForm

from .models import Curso, Profesor

from django.forms.models import model_to_dict

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.urls import reverse_lazy

def crear_curso(request, camada):
    curso = Curso(nombre='Python', camada=camada)
    curso.save()

    return HttpResponse(f'Curso creado! {camada}')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html',
    {'cursos': Curso.objects.all()})

def profesores(request):
    return render(request, 'AppCoder/profesores.html',
    {'profesores': Profesor.objects.all()})

def estudiantes(request):
    return HttpResponse('estudiantes')

def entregables(request):
    return HttpResponse('entregables')

def cursos_formulario(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Curso.objects.create(nombre=data['curso'], camada=data['camada'])
            return redirect('cursos')
    else:
        formulario = CursoForm()
    return render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})

def busqueda_camada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    camada = request.GET.get("camada")
    
    if camada:
        cursos = Curso.objects.filter(camada=camada)

        return render(request, 'AppCoder/buscar.html',
            {'cursos': cursos, 'camada': camada})
    else:
        return HttpResponse('No se envió una camada válida')

def crear_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Profesor.objects.create(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            return redirect('profesores')
    else:
        formulario = ProfesorForm()
    return render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})

def borrar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    return redirect('profesores')

def modificar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            profesor.nombre=data['nombre']
            profesor.apellido=data['apellido']
            profesor.email=data['email']
            profesor.profesion=data['profesion']

            profesor.save()
            return redirect('profesores')
    else:
        formulario = ProfesorForm(model_to_dict(profesor))
    return render(request, 'AppCoder/cursosFormulario.html', {'formulario': formulario})


class ProfesorListView(ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html'
    context_object_name = 'profesores'
    

class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = 'AppCoder/cursosFormulario.html'
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorUpdateView(UpdateView):
    model = Profesor
    template_name = 'AppCoder/cursosFormulario.html'
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'AppCoder/cursosFormulario.html'
    success_url = reverse_lazy('profesores')

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'AppCoder/cursosFormulario.html'