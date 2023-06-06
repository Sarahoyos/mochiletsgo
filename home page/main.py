#!/usr/bin/env python
import importlib
import os 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm    # Formulario de creación y autenticación de usuarios importados desde Django. 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate # Platillas de Django preexistentes usadas para el ingreso a la aplicación
from django.db import IntegrityError
#from .forms import TaskForm       # Formulario creado por el desarrollador para las tareas
#from .models import Task           # Modelo creado por el desarrollador para la tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required  #Formulario Django


# Create your views here.

def home(request):                         


    def cerro_tusa(request):              # estamos defining el button de la imagenes de cada ruta     

        if request.method == 'GET':                  
            return render(request, 'Cerro Tusa.html', {
            'form': UserCreationForm
        })

        elif request.method == 'POST':
            
            def chorro_campanas(request):              # estamos defining el button de la imagenes de cada ruta     

                if request.method == 'GET':                  
                 return render(request, 'Chorro Campanas.html', {
            'form': UserCreationForm
        })

        elif request.method == 'POST':
            
            def rio_melcocho(request):              # estamos defining el button de la imagenes de cada ruta    

                if request.method == 'GET':                  
                    return render(request, 'Rio Melcocho.html', {
            'form': UserCreationForm
        })

        elif request.method == 'POST':
            
            def desierto_de_la_tatacoa(request):              # estamos defining el button de la imagenes de cada ruta    

                if request.method == 'GET':                  
                    return render(request, 'Desierto de la Tatacoa.html', {
            'form': UserCreationForm
        })

        elif request.method == 'POST':

             def jardin_7_cascadas(request):              # estamos defining el button de la imagenes de cada ruta    

                if request.method == 'GET':                  
                    return render(request, 'Jardin 7 Cascadas.html', {
            'form': UserCreationForm
        })

        elif request.method == 'POST':
    
            def nevado_santa_isabel(request):              # estamos defining el button de la imagenes de cada ruta    

                if request.method == 'GET':                  
                    return render(request, 'Nevado Santa Isabel.html', {
            'form': UserCreationForm
        })

            