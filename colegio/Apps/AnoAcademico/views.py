from django.shortcuts import render,redirect
from colegio.Apps.AnoAcademico.models import AnoAcademico
from colegio.Apps.Matricula.models import Matricula
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from colegio.Apps.AnoAcademico.forms import AnoAcademicoForm

class AnoAcademicoList(ListView):
	model = AnoAcademico
	template_name = 'academico/listar_academico.html' #template_name es un atributo de la clase

def AnoAcademicoNew(request):
	ano=AnoAcademico()
	#mat=Matricula()
	#anoultimo = AnoAcademico.objects.last()
	#matri_list = Matricula.objects.filter(AnoAcademico__Ano=anoultimo.Ano)
	object_list = AnoAcademico.objects.all()

	contexto = {'object_list':object_list}
	if request.method=='POST':
		AnoAcademico.objects.filter(Activo=True).update(Activo=False)#primero ponemos a todos False para poner True a este
		ano.Ano = request.POST.get('ano')
		ano.FechaInicio = request.POST.get('fechainicio')
		ano.FechaFinal = request.POST.get('fechafinal')
		ano.activo = True
		ano.save()
		return render(request,'academico/listar_academico.html',contexto)
	else:
		return render(request,'academico/create_academico.html')

def edit(request,id):
	ano = AnoAcademico.objects.get(id=id)
	fecha_inicio = ano.FechaInicio.strftime('%Y-%m-%d')
	fecha_final = ano.FechaFinal.strftime('%Y-%m-%d')
	return render(request,'academico/edit_academico.html',{'ano':ano,'fecha_final':fecha_final,'fecha_inicio':fecha_inicio})

def update(request):
	if request.method=='POST':
		idanoacademico=request.POST.get('idanoacademico')
		nombreano=request.POST.get('nombre')
		fechainicio=request.POST.get('fechainicio')
		fechafinal=request.POST.get('fechafinal')
		activo=request.POST.get('activo')
		
		if activo=='on':
			activo_guardar=True
		else:
			activo_guardar=False
			
		AnoAcademico.objects.filter(Activo=True).update(Activo=False)#primero ponemos a todos False para poner True a este
		
		ano = AnoAcademico.objects.get(id=idanoacademico)
		ano.Ano=nombreano
		ano.FechaInicio=fechainicio
		ano.FechaFinal=fechafinal
		ano.Activo=activo_guardar
		ano.save()

		return redirect('app_academico_listar')

class AnoAcademicoUpdate(UpdateView):
	model=AnoAcademico
	form_class=AnoAcademicoForm
	template_name='academico/update_academico.html'
	success_url = '/academico/listar/'

class AnoAcademicoDelete(DeleteView):
	model=AnoAcademico
	template_name='academico/delete_academico.html'
	success_url = '/academico/listar/'

class AnoAcademicoDetalle(DeleteView):
	model=AnoAcademico
	template_name='academico/detalle_academico.html'
	success_url = '/academico/detalle_academico/'
