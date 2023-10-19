from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import libro
from .forms import LibroForm

# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Hola mundo</h1>")


def nosotros(request):
    return render(request, "paginas/nosotros.html")
 

def listar(request):
    libros = libro.objects.all()
    return render(request, "libros/index.html", {'libros': libros})

def crear(request):
    formulario =LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar')
    return render(request, "libros/crear.html", {'formulario': formulario})


def editar(request):
    return render(request, "libros/editar.html")


def eliminar(request, id):
    Libro = libro.objects.get(id=id)
    Libro.delete()
    return redirect('listar')