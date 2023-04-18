# Generated by Django 4.2 on 2023-04-17 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarrosDentro',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=6, unique=True)),
                ('ultima_entrada', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroHistorico',
            fields=[
                ('car_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('car_placa', models.CharField(max_length=6, unique=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('ultima_entrada', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
