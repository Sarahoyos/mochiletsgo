# registro de login
# registro de reserva
# registro de sign up

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from mochiletsgo.views import Home


#formilario de reserva 
urlpatterns=  [
    path('admin/',admin.site.urls), # aqui vamos asignar , el frontend tiene  que asignar el orden de el despligue de la plataforma
    path('firstname/',include('django.contrib.auth.urls')), # el campo name y  el command include esta enlazando el desplegue que ya esta
    path('lastname/',include('django.contrib.auth.urls')),
    path('email/',include('user_app.urls'),username='users'), # el campo de username va ser el email 
    path('date/',include('auth_views.DATE.complete'('template_date'))),
    path('register of person',include('auth_views.user.conf.views')), # aqui el registro por ruta va ser unico , cada persona se debe de registrar indivualmente
    
    path('user',include('base_app.urls')),  # le estamos la funcionalidad de llenar el formulario donde quiera que este user or admin
    path('firstname/',include('django.contrib.auth.urls')), # el campo name y  el command include esta enlazando el desplegue que ya esta
    path('lastname/',include('django.contrib.auth.urls')),
    path('email/',include('user_app.urls'),username='users'), # el campo de username va ser el email 
    path('date/',include('auth_views.DATE.complete'('template_date'))),
    path('register of person/',include('auth_views.user.conf.views')), # aqui el registro por ruta va ser unico , cada persona se debe de registrar indivualmente
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# formulario de login
urlpatterns=  [
    path('admin/',admin.site.urls), # aqui vamos asignar , el frontend tiene  que asignar el orden de el despligue de la plataforma
    path('username/',include('user_app.urls'),username='users'), # el campo de username va ser el email 
    path('password/',include('auth_views.DATE.complete'('template_date'))),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#formulario de sign up
urlpatterns=  [
    path('admin/',admin.site.urls), # aqui vamos asignar , el frontend tiene  que asignar el orden de el despligue de la plataforma
    path('username/',include('user_app.urls'),username='users'), # el campo de username va ser el email 
    path('password/',include('auth_views.DATE.complete'('template_date'))),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
   path('', Home.as_view())
]
