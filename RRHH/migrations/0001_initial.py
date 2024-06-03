# Generated by Django 5.0.2 on 2024-05-31 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=50)),
                ('descripcion_area', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cargo', models.CharField(max_length=50)),
                ('descripcion_cargo', models.TextField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos', to='RRHH.area')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('carnet', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('dui', models.CharField(max_length=9)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('fechanacimiento', models.DateField()),
                ('direccion', models.TextField()),
                ('salariobase', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='RRHH.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=50)),
                ('carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='RRHH.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('horas_trabajadas', models.IntegerField()),
                ('horas_extras_diurnas', models.IntegerField()),
                ('horas_extras_nocturnas', models.IntegerField()),
                ('mes_asistencia', models.DateField()),
                ('carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='RRHH.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='encargados',
            field=models.ManyToManyField(blank=True, related_name='areas_encargadas', to='RRHH.empleado'),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='RRHH.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('codigo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('bono', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalpagar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('afp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('renta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechapago', models.TimeField()),
                ('carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='RRHH.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('codigo_permiso', models.AutoField(primary_key=True, serialize=False)),
                ('fechasolicitud', models.DateField()),
                ('fechainicio', models.DateField()),
                ('fechafinal', models.DateField()),
                ('justificacion', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permisos', to='RRHH.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='RRHH.empleado')),
            ],
        ),
    ]
