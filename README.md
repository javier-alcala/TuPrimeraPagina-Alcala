# TuPrimeraPagina-Alcala

Una vez creado el entorno virtual, descargar las versiones explicitadas en requirements.txt

Al correr el servidor, llegan a la página de inicio de la página Blog.

Las tres clases del modelo son: Perfil, Post y Comentario. Los formularios para agregar datos a cada clase son ingresando a:
http://127.0.0.1:8000/perfilFormulario/
http://127.0.0.1:8000/postFormulario/
http://127.0.0.1:8000/comentarioFormulario/

El formulario para buscar los posts por autor es en:
http://127.0.0.1:8000/buscarAutor/
Recomiendo buscar pablo o juan.


El estilo de la página es de un blog con estética de comienzo de los años 2000.
Funcionalidades que podrían incluirse más adelante:
    Mostrar los posts en el muro de explorar, así como en el perfil mostrar los posts propios.
    Configurar los comentarios para que se realicen sobre un posteo
    En la clase 'Perfil' del modelo, usar el usuario configurado en el panel de Django como base y extenderlo con los atributos configurados en models.py