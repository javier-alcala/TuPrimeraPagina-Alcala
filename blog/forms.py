from django import forms

class PerfilFormulario(forms.Form):
    usuario = forms.CharField(max_length=100, label='Usuario')
    edad = forms.IntegerField(label='Edad')
    biografia = forms.CharField(widget=forms.Textarea, label='Biografía')

class PostFormulario(forms.Form):
    autor = forms.CharField(max_length=100, label='Autor')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')

class ComentarioFormulario(forms.Form):
    autor = forms.CharField(max_length=100, label='Autor')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')