from django.contrib import admin
from .models import Estudios_cv, Experiencias_cv, Proyecto, Descripcion_cv
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Descripcion_cv)
admin.site.register(Estudios_cv)
admin.site.register(Experiencias_cv)