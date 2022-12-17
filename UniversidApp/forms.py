from django import forms
from django.db.models import fields
from django.forms import widgets
from UniversidApp.uni import universidades
from gestionDatos.models import registro, dias_semana, horas_semana, notas_usuarios

class FormularioUsuario(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput, max_length=9)
    choices= universidades
    establecimiento= forms.ChoiceField(choices=choices)
    
    class Meta:
        model = registro
        fields = '__all__'

class login(forms.Form):
    usuario= forms.CharField()
    contraseña= forms.CharField(widget=forms.PasswordInput)

class calificacion(forms.ModelForm):
    class Meta:
        model = notas_usuarios
        fields= '__all__'


class horario_asignaturas(forms.ModelForm):
    class Meta:
        model = dias_semana
        fields= ['lunes','martes','miercoles','jueves','viernes']

class horario_horas(forms.ModelForm):
    class Meta:
        model = horas_semana
        fields=['lunes_hora','martes_hora','miercoles_hora','jueves_hora','viernes_hora']
