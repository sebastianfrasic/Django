from django.db import models

class Pregunta(models.Model):
    fechaPublicacion = models.DateTimeField('Fecha publicacion')
    textoPregunta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoPregunta


class Respuesta(models.Model):
    preguntaAsociada = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textoRespuesta = models.CharField(max_length=200)

    def __str__(self):
        return self.textoRespuesta
