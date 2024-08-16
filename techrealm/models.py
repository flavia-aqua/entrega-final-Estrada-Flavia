from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    
    niveles = {
        "1": "Básico",
        "2": "Intermedio",
        "3": "Avanzado"
    }
    nivel = models.CharField(
        max_length = 1,
        choices = niveles,
        default = "1"
    )

    fecha = models.DateField()

class Blogs(models.Model):

    titulo = models.CharField(max_length=100)
    
    subtitulo = models.CharField(max_length=60)
    
    temas = {
        "1":"GTM",
        "2":"GA4",
        "3":"BQ"
    }
    tema = models.CharField(
        max_length = 1,
        choices = temas,
        default = "1"
    )

    cuerpo = models.TextField(null=True, blank= True)

    autor = models.CharField(max_length=100)

    fecha = models.DateTimeField(auto_now_add=True)

    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")


class Libros(models.Model):
    nombre = models.CharField(max_length=100)

    temas = {
        "1":"GTM",
        "2":"GA4",
        "3":"BQ"
    }
    tema = models.CharField(
        max_length= 1,
        choices = temas,
        default = "1"
    )

    codigo = models.CharField(max_length=30)
