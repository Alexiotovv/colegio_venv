# Generated by Django 2.1 on 2024-04-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='Tipo',
            field=models.CharField(choices=[('CURSO', 'CURSO'), ('ACTITUDINAL', 'ACTITUDINAL'), ('INASISTENCIAS', 'INASISTENCIAS'), ('DEL PADRE DE FAMILIA', 'DEL PADRE DE FAMILIA'), ('APRECIACIÓN DEL TUTOR', 'APRECIACIÓN DEL TUTOR'), ('--', '--')], default='-', max_length=60),
        ),
    ]
