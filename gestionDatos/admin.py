from django.contrib import admin
from gestionDatos.models import registro, dias_semana, horas_semana, notas_usuarios


# Register your models here.


class vistaresgistros(admin.ModelAdmin):
    list_display = ("nombre","apellido","usuario","correo","establecimiento","identificacion","contraseña")
admin.site.register(registro, vistaresgistros)

class vistadias(admin.ModelAdmin):
    list_display=("username","lunes","martes","miercoles","jueves","viernes")
admin.site.register(dias_semana, vistadias)
class vistahoras(admin.ModelAdmin):
    list_display=("username","lunes_hora","martes_hora","miercoles_hora","jueves_hora","viernes_hora")  
admin.site.register(horas_semana,vistahoras)

class vistanotas(admin.ModelAdmin):
    list_display = ("usuario","asignatura","tipo_evaluacion","promedio")
admin.site.register(notas_usuarios,vistanotas)