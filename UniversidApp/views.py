from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http import request
from django.http.request import HttpRequest
from django.template import Template, Context
import datetime
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib import messages
from UniversidApp import settings

from UniversidApp.forms import FormularioUsuario, login, calificacion, horario_asignaturas, horario_horas
from gestionDatos.models import registro, dias_semana, horas_semana, notas_usuarios
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import loader



def Inicio(request):
    return render(request,"Pagina Inicio.html")


def Signin_request(request):
    form = login()
    if request.method == "POST":
        form = login(request.POST)
        if form.is_valid():
            form= form.cleaned_data
            usuario = form['usuario']
            contraseña = form['contraseña']
            if registro.objects.filter(usuario=usuario,contraseña=contraseña):
                i={"user":usuario,"password":contraseña}
                request.session['ctx'] = i
                n={"n":"1"}
                request.session['n']=n
                #del request.session['ctx']
                return redirect('/UniProfile/')
            else:
                form=login()
                return render(request,"Malito.html",{"form":form})
        else:
                messages.error(request, "Usuario o Contraseña Incorrectos")

    return render(request,"Sign-in.html", {"form":form})


class FormularioUsuarioView(HttpRequest):

        def index(request):
            usuario = FormularioUsuario()
            return render(request,"Registro.html", {"form":usuario})
        
        def error(request):
            usuario = FormularioUsuario()
            return render(request,"Registro copy.html", {"form":usuario})

        def procesar_formulario(request):
            usuario = FormularioUsuario(request.POST)
            #if usuario.is_valid():
                #usuario=usuario.cleaned_data
                #nombre= usuario['nombre']
                #apellido=usuario['apellido']
                #i={"name":nombre,"surname":apellido}
                #request.session['ctx']= i
                #usuario=FormularioUsuario(request.POST)
                
            subject = "¡Bienvenido a UniversidApp!"
            message = loader.render_to_string('Plantilla_email.html')
            email_from = settings.EMAIL_HOST_USER
            mail = EmailMultiAlternatives(subject, message, email_from, [request.POST["correo"]])
            mail.attach_alternative(message, "text/html")
            mail.send()
            if usuario.is_valid():
                usuario.save()
                usuario = FormularioUsuario()
                return redirect('/Inicio Sesion/')
            else:
                return redirect("/error/")



def Signout_request(request):
    #logout(request)
    #del request.session['n']
    n={"n":"0"}
    request.session['n']=n

    return redirect("Home")
#if n == 1:
def Grafico(request):
    return render(request,"Grafico Circular.html")
        


def UniProfile(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        info= request.session.get('ctx')
        user=info['user']
        return render(request,"Pagina Usuario.html",{"name":user})
    else:
        return redirect('/UniversidApp/')


def Pagina_Uni(request):
    return render(request,"Pagina_universidades.html")

def Prueba(request):
    return render(request,"Selector_dinamico.html")

def Prueba_2(request):
    return render(request,"Selector_ponderaciones.html")

def Terminos(request):
    return render(request,"Terminos y Condiciones.html")

def Mantencion(request):
    return render(request,"En Mantencion.html")

def chat(request):
    return render(request,"chatango.html")

def UniversiChat(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        return render(request,"UniversiChat.html")
    else:
        return redirect("Home")

def UniRegist(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        lista_asig=[]
        lista_nota=[]
        lista_tipo=[]
        ctx= request.session.get('ctx')
        name= ctx['user']
        a = notas_usuarios.objects.all().filter(usuario=name)
        for i in a:
            asig= str(i.asignatura)
            ev= str(i.tipo_evaluacion)
            nota= str(i.promedio)
            lista_asig.append(asig)
            lista_nota.append(nota)
            lista_tipo.append(ev)
            dicc = {"nombre":name,"asig":lista_asig,"tipo":lista_tipo,"nota":lista_nota,"range":range(10)}
        return render(request,"registros_notas.html",dicc)
    else:
        return redirect('/UniversidApp/')    

def Brython(request):
    return render(request,"Brython.html")

def UniCalendar(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        ctx= request.session.get('ctx')#cambia al juntar los proyectos
        name= ctx['user']#cambia al juntar los proyectos
        #rut=ctx['rut']
        n= [0,1,2,3,4,5,6,7]
        if dias_semana.objects.filter(username=name):
            a= dias_semana.objects.all().filter(username=name)
            b= horas_semana.objects.all().filter(username=name)
        for i in a:
           lunes= str(i.lunes)
           martes= str(i.martes)
           miercoles= str(i.miercoles)
           jueves= str(i.jueves)
           viernes= str(i.viernes)
           if len(lunes) and len(martes) and len(miercoles) and len(jueves) and len(viernes) > 13 and "," not in lunes and martes and miercoles and jueves and viernes:
                return render(request,"horarioxdee.html")
           lunes=funcion(lunes)
           martes=funcion(martes)
           miercoles=funcion(miercoles)
           jueves=funcion(jueves)
           viernes=funcion(viernes)
        for i in b:
           lunes_hora= str(i.lunes_hora)
           martes_hora= str(i.martes_hora)
           miercoles_hora= str(i.miercoles_hora)
           jueves_hora= str(i.jueves_hora)
           viernes_hora= str(i.viernes_hora)
           if len(lunes_hora) and len(martes_hora) and len(miercoles_hora) and len(jueves_hora) and len(viernes_hora) > 4 and "," not in lunes_hora and martes_hora and miercoles_hora and jueves_hora and viernes_hora:
                return render(request,"horarioxdee.html")
           lunes_hora=funcion2(lunes_hora)
           martes_hora=funcion2(martes_hora)
           miercoles_hora=funcion2(miercoles_hora)
           jueves_hora=funcion2(jueves_hora)
           viernes_hora=funcion2(viernes_hora)
                               
           contexto={"nombre":name,"lunes":lunes,"martes":martes,"miercoles":miercoles,"jueves":jueves,"viernes":viernes,
                    "lunes_hora":lunes_hora,"martes_hora":martes_hora,"miercoles_hora":miercoles_hora,"jueves_hora":jueves_hora,"viernes_hora":viernes_hora,
                    "list":n
           }
           return render(request,"UniCalendar.html",contexto)
        else:
            return render(request,"no.html")
    else:
        return redirect("Home")

def natbar(request):
    return render(request,"natbar.html")

def UniCalculate(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        inf= request.session.get('ctx')
        user= inf['user']
        formulario = calificacion()
        if request.method== "POST":
            formulario=calificacion(request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"UniCalculate.html", {"form":formulario,"user":user})
    else:
        return redirect('/UniversidApp/')

def creador_horario(request):
    p= request.session.get('n')
    o= p['n']
    if o=="1":
        ct= request.session.get('ctx')#cambia al juntar el proyecto
        user = ct['user']#cambia al juntar el proyecto
        if not dias_semana.objects.filter(username=user):
            asig= horario_asignaturas()
            hora= horario_horas()
            ctx = {"asignatura":asig,"horas":hora}
            if request.method == "POST":
                asig= horario_asignaturas(request.POST)
                hora= horario_horas(request.POST)
                if asig.is_valid() and hora.is_valid():
                    asig= asig.cleaned_data
                    hora= hora.cleaned_data
                    if not dias_semana.objects.filter(username=user):
                        dias_semana.objects.create(username=user,lunes=asig['lunes'],martes=asig['martes'],miercoles=asig['miercoles'],jueves=asig['jueves'],viernes=asig['viernes'])
                        horas_semana.objects.create(username=user,lunes_hora=hora['lunes_hora'],martes_hora=hora['martes_hora'],miercoles_hora=hora['miercoles_hora'],jueves_hora=hora['jueves_hora'],viernes_hora=hora['viernes_hora'])
                        

                        
                        return redirect('/UniCalendar/')     
                    else:
                        return redirect('/UniCalendar/')
                else:
                    return request(request,"malito.html")
                
            return render(request,"horarioxde.html",ctx)
        else:
            return redirect('/UniCalendar/')
    else:
        return redirect("Home")


def funcion(dias):
    dias= str(dias)
    lista=[]
    e= dias
    i = dias.count(',')
    if ',' in dias:
        n= 0
        while n < i:
            no= dias.find(',')
            primera= dias[0:no]
            no+=1
            dias= dias[no:]
            n+=1
            lista.append(primera)
        lista.append(dias)
        p= len(lista)
        while p < 8:
            l=str()
            lista.append(l)
            p+=1

        
        return lista    

    else:
        lista.append(e)
        m=0
        while m < 8:
            l=str()
            lista.append(l)
            m+=1
        return lista







def funcion2(dias):
    dias= str(dias)
    lista=[]
    e= dias
    i = dias.count(',')
    if ',' in dias:
        n= 0
        while n < i:
            no= dias.find(',')
            primera= dias[0:no]
            no+=1
            dias= dias[no:]
            n+=1
            lista.append(primera)
        lista.append(dias)
        p= len(lista)
        while p < 8:
            l=str()
            lista.append(l)
            p+=1

        
        return lista    

    else:
        lista.append(e)
        m=0
        while m < 8:
            l=str()
            lista.append(l)
            m+=1
        return lista




   



                

