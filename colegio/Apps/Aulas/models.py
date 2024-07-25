from django.db import models
from colegio.Apps.Nivel.models import *
from colegio.Apps.Grado.models import *
from colegio.Apps.Seccion.models import *
from colegio.Apps.AnoAcademico.models import *

class Aulas(models.Model):
    AnoAcademico = models.ForeignKey(AnoAcademico,null=True,blank=True, verbose_name=("Año Academico"), on_delete=models.CASCADE)
    Nivel = models.ForeignKey(Nivel,null=False,blank=False, verbose_name=("Nivel Académico"), on_delete=models.CASCADE)
    Grado = models.ForeignKey(Grado,null=False,blank=False, verbose_name=("Grado Académico"), on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, null=False,blank=False, verbose_name=("Sección Académico"), on_delete=models.CASCADE)
