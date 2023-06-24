from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm    # Formulario de creación y autenticación de usuarios importados desde Django. 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate # Platillas de Django preexistentes usadas para el ingreso a la aplicación
from django.db import IntegrityError
#from .forms import TaskForm       # Formulario creado por el desarrollador para las tareas
#from .models import Task           # Modelo creado por el desarrollador para la tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required  #Formulario Django
#from django.http import HttpResponse
import os,django
ENVIRONMENT_VARIABLE = "DJANGO_SETTINGS_MODULE"

# Create your views here.


def home(request):                         #Si se presiona Home en la navegación se carga el inicio de nuestra página de planificador de tareas
    return render(request, 'home.html')


def signup(request):                  #Función para el registro de usuarios nuevos en la aplicación

    if request.method == 'GET':                  #Si se obtienen datos, cargue el formulario de Singup (Registro)
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:                 # Si los datos ingresados en los campos de contraseña y confimar
            try:                                                                   #contraseña coinciden se registra el usuario y se direacciona a la
                # registrar usuario                                                #página de Tasks
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:                                   #Se despliega los mensajes de error si se trata de registrar un usuario que ya se
                return render(request, 'login.html', {              #encontraba registrado en la base de datos con un mensaje de advertencia: "El usuario"
                    'form': UserCreationForm,                        #ya existe y de igual manera si la contraseña ingresada no coincide al confirmarse
                    "error": 'Username already exists'               #le advierte al usuario que revise.
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password does not match'
        })

def signup(request):
    if request.method == 'GET':
        return render(request, 'invalid',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    user = authenticate(request, username=request.GET['sarah1'], password=request.GET['password33'])

@login_required

def sign_out(request):
    logout(request)
    return redirect('home')
