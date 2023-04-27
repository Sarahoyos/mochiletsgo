from django.conf import settings
from django.db import migrations, models

# Aqui estamos haciendo toda la configurations de la dependencies de la pagina

class migrations(migrations.Migration):
    inicial=True
    dependencies=[migrations.swappable_dependency(settings.auth_user_model)] # permite configurar cualquiere pagina , objetos o titulos de la pagina.
    operations=[
        migrations.create.model(
            fields=[
                ('user', models.BigAutoField) # configurar el user se puede modificar un user , autocambiar el campo , editar campos
                ('title', models.CharField(max_length=25)) # aqui podemos modificar el titulos de la pagina 
                ('validation', models.DateTimeField(null=True)) # aqui podemos validar la fecha y hora de la pagina
                ('buttons', models.ManyToManyField(on_delete=settings.auth_user_model)) #
            ]
        )
    ]
    

