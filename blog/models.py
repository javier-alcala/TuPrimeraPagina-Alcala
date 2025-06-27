from django.db import models

class Perfil(models.Model):
    usuario = models.CharField(max_length=100)
    biografia = models.TextField()

class Post(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)