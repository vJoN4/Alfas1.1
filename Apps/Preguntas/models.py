from django.db import models
from ..Usuario.models import User

# Create your models here.
CATEGORIAS = [
    ("Software","Software"),
    ("Hardware","Hardware"),
    ("Windows","Windows"),
    ("GNU/Linux","GNU/Linux"),
    ("Programación","Programación"),
    ("Desarrollo Web","Desarrollo Web"),
    ("GIT","GIT"),
]


class pregunta(models.Model):
    contenido = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now=True, auto_now_add=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

class respuesta(models.Model):
    contenido = models.TextField()
    fecha = models.DateField(auto_now=True, auto_now_add=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey('pregunta', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
