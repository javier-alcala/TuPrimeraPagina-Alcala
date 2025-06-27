from django.urls import path
from .views import inicio, perfil, explorar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('explorar/', explorar, name='explorar'),
    path('perfil/', perfil, name='perfil'),
]
