from pyexpat import model
from django.shortcuts import redirect, render
from colegio.Apps.Curso.models import Curso
from colegio.Apps.Competencias.models import Competencias,CompetenciaCurso
from colegio.Apps.Competencias.forms import CompetenciasForm
from django.views.generic import CreateView

def GrabarCompetencias(request,curso_id):
	nombre_curso=Curso.objects.get(id=curso_id)
	lista_competencias=CompetenciaCurso.objects.filter(Curso__id=curso_id)
	#print(nombre_curso.Nivel)
	compe=Competencias.objects.filter(nivel=nombre_curso.Nivel)
	
	contexto={'compe':compe,'nombre_curso':nombre_curso,'lista_competencias':lista_competencias}
	if request.method=='POST':
		graba_comp=CompetenciaCurso()
		idcompetencia=request.POST.get('Competencias')

		graba_comp.Curso_id=curso_id
		graba_comp.Competencias_id=idcompetencia
		graba_comp.save()

		return render(request,'competencias/asignar_competencias.html',contexto)
	else:	
		return render(request,'competencias/asignar_competencias.html',contexto)

def ListarCompetencias(request):
	lista_competencias=Competencias.objects.all()
	return render(request,'competencias/listar_competencias.html',{'lista_competencias':lista_competencias})
def EliminarCompetencias(request,id):
	Competencias.objects.filter(id=id).delete()
	lista_competencias=Competencias.objects.all()
	return render(request,'competencias/listar_competencias.html',{'lista_competencias':lista_competencias})
def EditarCompetencias(request,id):
	# ide=id
	# nombre=Competencias.objects.get(id=id)
	# contexto={'ide':ide,'nombre':nombre}
	compe = Competencias.objects.get(id=id)

	if request.method=='POST':
		form = CompetenciasForm(request.POST,instance=compe)
		if form.is_valid():
			form.save()
		lista_competencias=Competencias.objects.all()
		return render(request,'competencias/listar_competencias.html',{'lista_competencias':lista_competencias})
	else:
		form = CompetenciasForm(instance=compe)
		contexto={'form':form}
		return render(request,'competencias/editar_competencias.html',contexto)

# def EliminarCursoCompetencia(idcomcur):
# 	CompetenciaCurso.objects.filter(id=idcomcur).delete()
# 	return render('competencias/listar_competencias.html')
	
	#return redirect('app_lista_curso')
	
class NuevaCompetencia(CreateView):
	model=Competencias
	form_class= CompetenciasForm
	template_name='competencias/nueva_competencia.html'
	success_url='/competencias/nueva_competencia/'
