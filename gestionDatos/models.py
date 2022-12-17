import django
from django.db import models



    
class registro(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    usuario=models.CharField(max_length=30, unique= True)
    correo=models.EmailField(unique= True)
    establecimiento=models.CharField(max_length=80)
    identificacion=models.CharField(max_length=10, unique= True)
    contraseña=models.CharField(max_length=9) 

class dias_semana(models.Model):
    username= models.CharField(max_length=40,blank=False,null=False,default='')
    lunes= models.CharField(max_length=40,blank=False,null=False)
    martes= models.CharField(max_length=40,blank=False,null=False)
    miercoles= models.CharField(max_length=40,blank=False,null=False)
    jueves= models.CharField(max_length=40,blank=False,null=False)
    viernes= models.CharField(max_length=40,blank=False,null=False)

class horas_semana(models.Model):
    username= models.CharField(max_length=40,blank=False,null=False,default='')
    lunes_hora= models.CharField(max_length=40,blank=False,null=False)
    martes_hora= models.CharField(max_length=40,blank=False,null=False)
    miercoles_hora= models.CharField(max_length=40,blank=False,null=False)
    jueves_hora= models.CharField(max_length=40,blank=False,null=False)
    viernes_hora= models.CharField(max_length=40,blank=False,null=False)

class notas_usuarios(models.Model):
    usuario= models.CharField(max_length=30)
    asignatura= models.CharField(max_length=30)
    tipo_evaluacion= models.CharField(max_length=30)
    promedio= models.CharField(max_length=30)
    
