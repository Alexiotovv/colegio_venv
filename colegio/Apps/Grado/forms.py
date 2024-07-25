from django import forms
from colegio.Apps.Grado.models import Grado

class GradoForm(forms.ModelForm):
	class Meta:
		model = Grado
		fields = [
		'Nombre',
		'AnoAcademico'
		]
		widgets = {
		'Nombre':forms.TextInput(attrs={'class':'form-control'}),
		'AnoAcademico':forms.Select(attrs={'class':'form-select'}),
		}
