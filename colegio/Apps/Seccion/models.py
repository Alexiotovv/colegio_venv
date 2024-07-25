from django.db import models
from colegio.Apps.AnoAcademico.models import AnoAcademico

class Seccion(models.Model):
	AnoAcademico=models.ForeignKey(AnoAcademico,blank=False,null=False, verbose_name=("Año Académico"), on_delete=models.CASCADE)
	Nombre = models.CharField(max_length=2)
	
	def __str__(self):
		return self.Nombre	