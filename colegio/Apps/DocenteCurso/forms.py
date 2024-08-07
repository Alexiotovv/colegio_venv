from django import forms
from colegio.Apps.DocenteCurso.models import DocenteCurso

class DocenteCursoForm(forms.ModelForm):
	class Meta:
		model = DocenteCurso
		fields = [
		'Docente',
		'Curso',
		'Aulas'
		]
		widgets = {
		'Docente':forms.Select(attrs = {'class':'single-select'}),
		'Curso':forms.Select(attrs={'class':'single-select'}),
		'Aulas':forms.Select(attrs={'class':'single-select'}),
		}
		