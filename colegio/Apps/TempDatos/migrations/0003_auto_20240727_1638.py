# Generated by Django 2.1 on 2024-07-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DocenteCurso', '0004_auto_20240726_1524'),
        ('TempDatos', '0002_tempdatos_aula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempdatos',
            name='Aula',
        ),
        migrations.AddField(
            model_name='tempdatos',
            name='Docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DocenteCurso.DocenteCurso'),
        ),
    ]
