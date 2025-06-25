from django.shortcuts import render,redirect
from . models import Libros

# Create your views here.
def index(request):
    libros = Libros.objects.all()
    return render(request,'index.html',{'libros':libros})

def crear_libro(request):
    titulo = request.POST['titulo']
    precio = request.POST['precio']
    autor = request.POST['autor']
    libro = Libros(titulo=titulo,precio=precio,autor=autor)
    libro.save()
    return redirect('/')

def editar_libro(request,id):
    libro = Libros.objects.get(id=id)
    return render(request,'editar_libro.html',{'libro':libro})



def actualizar_libro(request,id):
    libro=Libros.objects.get(id=id)
    libro.titulo=request.POST['titulo']
    libro.precio=request.POST['precio']
    libro.autor=request.POST['autor']
    libro.save()
    return redirect('/')

def eliminar_libro(request,id):
    libro = Libros.objects.get(id=id)
    libro.delete()
    return redirect('/')

def agregar_libro(request):
    return redirect(request,'agregar_libro.html')
