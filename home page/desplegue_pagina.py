from pathlib import Path
import os

BASE_DIR=Path(__file__).resolve().parent.parent # Vamos a utilizar la liberia de path enlanzar con una plataforma para subirlo a un hosting

SECRET_KEY='django-insecure-3+po359r5(0ui)(vvczfb7$gh+fo5=6c2j%e93dz#v!zz&+jnv' #TOKEN 

DEBUG=True # seguridad para que nos de accesso a la pagina 

INSTALLED_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.request',
    'django.contrib.debug'
    'users_app'
]

CSRF_TRUSTED_ORIGINS=['https.local/mochiletsgo.com'] # aqui necesitamos un hosting para poder enlazar la pagina

ROOT_URL_CONFIG='home.urls' # estamos llamando el codigo que contiene todo el home de la pagina , la direcion principal donde siempre nos va llevar

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
                'django.template.context_processors.sessions'
            ]
        }
    }
]

DATABASE={
    'default':{
        'ENGINE':'django.db.backends.mysql.1.43.0',
        'NAME': BASE_DIR/'db.mysql.1.43.0',
        'USER':'root',
        'PASSWORD':'Mochiletsgo2023',
        'HOST':'HTTPS:/local/mochiletsgo.com/',
        'PORT':"5800"
    }
}

AUTH_PASSWORD_VALIDATORS=[
    {
        'VALIDATOR_NUMERICPASSWORD':'django.contrib.auth.password_validation.NumericPasswordValidator', #Validar que dentro de la contrasena tenga numeros
        'VALIDATOR_LENGTHOFPASSWORD':'django.contrib.auth.password_validation.MinNumLengthValidator', # Validar la longitud de la contrasena
        'VALIDATOR_EMAIL':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  #Validar que sea similiar con el correo (user)
        'VALIDATOR_ALPHANUMERIC': 'django.contrib.auth.password_validation.AlphabetValidator',         #Validar que tenga numeros y letas
        'VALIDATOR_CAPS_LOWER': 'django.contrib.auth.password_validation.CapsLowerValidator',           # Validar si contrasena tiene caps or lower case letters
    }
]
LANGUAGUE_CODE='es'

TIME_ZONE='America/Bogota'

DATE='GMT -5'
DATE=True

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' 

STATIC_URL='/static/'
STATICFILES_DIRS=[os.Path]