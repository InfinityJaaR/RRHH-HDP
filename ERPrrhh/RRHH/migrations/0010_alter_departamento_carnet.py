# Generated by Django 5.0.2 on 2024-05-31 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0009_remove_area_encargados_area_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='carnet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='RRHH.empleado'),
        ),
    ]
