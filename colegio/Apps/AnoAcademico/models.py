from email.policy import default
from django.db import models
from datetime import date
class AnoAcademico (models.Model):
	Ano = models.CharField(max_length=4)
	FechaInicio = models.DateField()
	FechaFinal = models.DateField()
	Activo = models.BooleanField(default=False)

	def __str__(self):
		return self.Ano
