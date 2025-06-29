from django.urls import path
from .views import inicio, perfil, explorar, perfilFormulario, postFormulario, comentarioFormulario, buscar, buscarAutor

urlpatterns = [
    path('', inicio, name='inicio'),
    path('explorar/', explorar, name='explorar'),
    path('perfil/', perfil, name='perfil'),

    path('perfilFormulario/', perfilFormulario, name='perfilFormulario'),
    path('postFormulario/', postFormulario, name='postFormulario'),
    path('comentarioFormulario/', comentarioFormulario, name='comentarioFormulario'),

    path('buscar/', buscar, name='buscar'),
    path('buscarAutor/', buscarAutor, name='buscarAutor'),
]
