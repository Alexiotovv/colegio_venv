from django import forms
from colegio.Apps.Seccion.models import Seccion

class SeccionForm(forms.ModelForm):
	class Meta:
		model=Seccion
		fields=[
		'Nombre',
		'AnoAcademico'
		]
		widgets={
		'Nombre':forms.TextInput(attrs={'class':'form-control'}),
		'AnoAcademico':forms.Select(attrs={'class':'form-select'}),
		}
		