# Generated by Django 2.1 on 2024-07-26 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DocenteCurso', '0004_auto_20240726_1524'),
        ('Notas', '0003_notascomp_aulas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notascomp',
            name='Aulas',
        ),
        migrations.AddField(
            model_name='notascomp',
            name='DocenteCurso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DocenteCurso.DocenteCurso'),
        ),
    ]
