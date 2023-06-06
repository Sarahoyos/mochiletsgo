from pathlib import Path
import os
from django.conf import settings

BASE_DIR=Path(__file__).resolve().parent.parent # Vamos a utilizar la liberia de path enlanzar con una plataforma para subirlo a un hosting

SECRET_KEY='django-insecure-3+po359r5(0ui)(vvczfb7$gh+fo5=6c2j%e93dz#v!zz&+jnv' #TOKEN 

DEBUG=True # seguridad para que nos de accesso a la pagina 

ALLOWED_HOSTS = [
    'localhost',
    'mochiletsgo.herokuapp.com'
]

INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.request',
    'django.contrib.debug',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.users_app',
    "mochiletsgo",
]

CSRF_TRUSTED_ORIGINS=['https://mochiletsgo.herokuapp.com/'] # aqui necesitamos un hosting para poder enlazar la pagina

ROOT_URL_CONFIG='https://mochiletsgo.herokuapp.com/home/' # estamos llamando el codigo que contiene todo el home de la pagina , la direcion principal donde siempre nos va llevar

TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # un template donde voy a volver a utilizarlo
        'DIRS': [],                                 # si tenemos paginas axuliares la pones aqui
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #le vamos a dar las funcionlidades con el request
                'django.template.context_processors.admin',
                'django.template.context_processors.auth',
                'django.template.context_processors.messages',
                'django.template.context_processors.sessions',
                'django.template.context_processors.date',
            ]
        }
    }
]

DATABASE={
    'default':{
        'ENGINE':'django.db.backends.SQLite', # estamos haciendo enlance
        'USER':'root',
        'HOST':'https://mochiletsgo.herokuapp.com/',
        'PORT':"5800"
    }
}
#unit test
AUTH_PASSWORD_VALIDATORS=[
    {
        'VALIDATOR_NUMERICPASSWORD':'django.contrib.auth.password_validation.NumericPasswordValidator', #Validar que dentro de la contrasena tenga numeros
        'VALIDATOR_LENGTHOFPASSWORD':'django.contrib.auth.password_validation.MinNumLengthValidator', # Validar la longitud de la contrasena
        'VALIDATOR_EMAIL':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  #Validar que sea similiar con el correo (user)
        'VALIDATOR_ALPHANUMERIC': 'django.contrib.auth.password_validation.AlphabetValidator',         #Validar que tenga numeros y letas
        'VALIDATOR_CAPS_LOWER': 'django.contrib.auth.password_validation.CapsLowerValidator',          # Validar si contrasena tiene caps or lower case letters
    }
]
LANGUAGUE_CODE='es'

TIME_ZONE='America/Bogota'

DATE='GMT -5'
DATE=True

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' 

STATIC_URL='/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')] # administra todo los comandos que tenemos en el desplegue

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField' # Esta haciendo un auto field de los campos en la base de datos

#todo
# conectar html enlazarlo con el back 
# conectar el booking html con la base de datos
# sql
# hacer otro main para añadir un formulario de profile
# button de ver mi reserva
# hacer unittest