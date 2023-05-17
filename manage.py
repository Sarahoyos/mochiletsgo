import os
import sys

#enlanzar las pagina de home con las paginas auxliares
def main():
    os.environ.setdefault('DJANGO_SETTING_MODULE','base_project.settings') # una variable de entorno que me enlace paginas 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'General error' # cuando le dio click una ruta me sale este error , tenemos que ver que sucede con la validacion
        ) from exc
    execute_from_command_line(sys.argv)
    
if __name__== '_main_': # si entro check si correcto si no muestreme el error , y redirrecionar a home 
    main()