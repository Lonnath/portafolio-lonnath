from django.db import models

class Proyectos (models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    url_proyecto = models.TextField()
    descripcion = models.TextField()
