# Generated by Django 3.2.8 on 2021-11-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionDatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('establecimiento', models.CharField(max_length=80)),
                ('identificacion', models.CharField(max_length=10)),
                ('contraseña', models.CharField(max_length=9)),
            ],
        ),
    ]
