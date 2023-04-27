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
        'ENGINE':'django.db.backends.mysql.1.43.0' 
    
    }
}

#todo:
#averiguar la version de mysql 
#averiguar el hosting gratis  https://cloud.google.com/solutions/web-hosting?utm_source=google&utm_medium=cpc&utm_campaign=latam-CO-all-es-dr-SKWS-all-all-trial-e-dr-1605194-LUAC0014807&utm_content=text-ad-none-any-DEV_c-CRE_517752295400-ADGP_Hybrid%20%7C%20SKWS%20-%20EXA%20%7C%20Txt%20~%20App-Modernization_Host-KWID_43700063329284571-kwd-89020569&utm_term=KW_hosting%20gratis-ST_hosting%20gratis&gclid=CjwKCAjwuqiiBhBtEiwATgvixL4TR5ApPjwyF7h7W9fb_wyG9yJM3ooUX01Ix86ibcUSlYjUwfpArRoCtVkQAvD_BwE&gclsrc=aw.ds
#montar esto en github
#hacer la base de datos 
#hacer los formularios