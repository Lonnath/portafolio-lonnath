from django.db import models

class Proyecto (models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    url_proyecto = models.TextField()
    descripcion = models.TextField()
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_proyecto, self.url_proyecto)
class Descripcion_cv (models.Model):
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion)
class Estudios_cv (models.Model):
    anio_entrada = models.DateField()
    anio_finalizacion = models.DateField()
    nombre_curso = models.CharField(max_length=50)
    academia = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        texto = "{0} ({1}) - {2}"
        return texto.format(self.nombre_curso, str(self.anio_entrada)+" - "+str(self.anio_finalizacion), self.academia)
class Experiencias_cv(models.Model):
    anio_entrada = models.DateField()
    anio_finalizacion = models.DateField()
    nombre_cargo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        texto = "{0} ({1}) - {2}"
        return texto.format(self.nombre_cargo, str(self.anio_entrada)+" - "+str(self.anio_finalizacion), self.empresa)
