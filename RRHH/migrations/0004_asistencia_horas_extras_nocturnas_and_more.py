# Generated by Django 5.0.2 on 2024-05-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0003_alter_asistencia_mes_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='horas_extras_nocturnas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='horas_extras_diurnas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='horas_trabajadas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='mes_asistencia',
            field=models.CharField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], max_length=3),
        ),
    ]
