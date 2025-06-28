from django.shortcuts import render

def inicio(request):
    return render(request, 'blog/inicio.html')

def perfil(request):
    return render(request, 'blog/perfil.html')

def explorar(request):
    return render(request, 'blog/explorar.html')