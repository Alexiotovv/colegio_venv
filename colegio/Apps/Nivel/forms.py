from django import forms
from colegio.Apps.Nivel.models import Nivel

class NivelForm(forms.ModelForm):
	class Meta:
		model = Nivel
		fields = [
		'Nombre',
		'AnoAcademico'
		]
		widgets = {
		'Nombre':forms.TextInput(attrs={'class':'form-control'}),
		'AnoAcademico':forms.Select(attrs={'class':'form-select'}),
		} 
		
		