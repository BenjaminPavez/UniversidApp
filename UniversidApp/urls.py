"""UniversidApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gestionDatos.models import registro
from .import views
from UniversidApp.views import Brython, FormularioUsuarioView, Grafico, Inicio, Mantencion, Prueba, Prueba_2, Terminos, UniCalculate, Pagina_Uni, Signin_request, UniCalendar, UniProfile, Signout_request, UniRegist, chat, UniversiChat, creador_horario
from django.views.generic import TemplateView
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib.auth import login,logout




urlpatterns = [
    path('admin/', admin.site.urls),
    path("UniversidApp/",Inicio, name="Home"),
    path("Grafico/",Grafico, name="Grafico"),
    path("UniCalculate/",UniCalculate, name="UniCalculate"),
    path("UniRegist/",UniRegist, name="UniRegist"),
    
    path("UniProfile/" ,UniProfile, name="pagina_usuario"),
    path("Universidades/",Pagina_Uni, name="Universidades"),
    path("Terminos y Condiciones/", Terminos, name="terminos"),
    path("Mantencion/", Mantencion, name="Mantencion"),

    path("Inicio Sesion/",Signin_request, name="login"),
    path("Cierre Sesion/",Signout_request, name="logout"),
    path("UniversiChat/",chat, name="unichat"),
    path("UniversiChatCo/",UniversiChat, name="chatango"),
    path("UniCalendar/",UniCalendar, name="UniCalendar"),
    path("Brython/",Brython, name="bry"),

    path("prueba/",Prueba, name="ejemplo"),
    path("prueba2/",Prueba_2, name="ejemplo2"),
    path("Nueva Cuenta/", FormularioUsuarioView.index, name="Nuevo UniversidApp ID"),
    path("guardarUsuario/", FormularioUsuarioView.procesar_formulario, name="guardarUsuario"),
    path("Creacion Horario/", creador_horario, name="creadorhorario" ),
    path("error/",FormularioUsuarioView.error, name="XD" )
]
