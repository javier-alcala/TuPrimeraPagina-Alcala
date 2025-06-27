from django.db import models

class Perfil(models.model):
    usuario = models.CharField(max_length=100)
    biografia = models.TextField()

class Post(models.model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)