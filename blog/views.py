from django.shortcuts import render
from .models import Perfil, Post, Comentario
from .forms import PerfilFormulario, PostFormulario, ComentarioFormulario
from django.http import HttpResponse

def inicio(request):
    return render(request, 'blog/inicio.html')

def perfil(request):
    return render(request, 'blog/perfil.html')

def explorar(request):
    return render(request, 'blog/explorar.html')

def perfilFormulario(request):
    if request.method == 'POST':
        miFormulario = PerfilFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            post = Perfil(usuario=informacion['usuario'],edad=informacion['edad'],biografia=informacion['biografia'])
            post.save()
            return render(request, 'blog/perfil.html')
    else:
        miFormulario = PerfilFormulario()
    
    return render(request, 'blog/formulario/perfilFormulario.html', {'miFormulario': miFormulario})


def postFormulario(request):
    if request.method == 'POST':
        miFormulario = PostFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            post = Post(autor=informacion['autor'],contenido=informacion['contenido'])
            post.save()
            return render(request, 'blog/explorar.html')
    else:
        miFormulario = PostFormulario()
    
    return render(request, 'blog/formulario/postFormulario.html', {'miFormulario': miFormulario})


def comentarioFormulario(request):
    if request.method == 'POST':
        miFormulario = ComentarioFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            post = Comentario(autor=informacion['autor'],contenido=informacion['contenido'])
            post.save()
            return render(request, 'blog/explorar.html')
    else:
        miFormulario = ComentarioFormulario()
    
    return render(request, 'blog/formulario/comentarioFormulario.html', {'miFormulario': miFormulario})


def buscarAutor(request):
    return render(request, "blog/formulario/buscarAutor.html")


def buscar(request):
    if request.GET['autor']:
        autor = request.GET['autor']
        posts = Post.objects.filter(autor__icontains=autor)

        return render(request, "blog/formulario/resultadosBusqueda.html", {"posts": posts, "autor": autor})

    else:
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)