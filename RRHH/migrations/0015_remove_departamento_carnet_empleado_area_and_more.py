# Generated by Django 5.0.2 on 2024-06-01 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0014_alter_area_descripcion_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='carnet',
        ),
        migrations.AddField(
            model_name='empleado',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empleados_area', to='RRHH.area'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empleados_departamento', to='RRHH.departamento'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empleados_municipio', to='RRHH.municipio'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_cargo', to='RRHH.cargo'),
        ),
    ]
