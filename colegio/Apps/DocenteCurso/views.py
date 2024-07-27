import json
from urllib import response
from django.shortcuts import render,redirect
from django.views.generic import DeleteView,UpdateView
from colegio.Apps.DocenteCurso.models import DocenteCurso
from colegio.Apps.DocenteCurso.forms import DocenteCursoForm
from colegio.Apps.Docente.models import Docente
from colegio.Apps.Curso.models import Curso
from colegio.Apps.Aulas.models import Aulas
from colegio.Apps.Notas.models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict


def DocenteListarAsginaciones(request):
	listar = DocenteCurso.objects.filter(Docente__User__is_active=True)
	return render(request,'docentecurso/listar_asignaciones.html',{'listar':listar})

def DocenteCursoCreate(request,id_docente):
	excluidos=[]
	docente_list = DocenteCurso.objects.filter(Docente__id=id_docente)
	for x in docente_list:
		excluidos.append(x.Curso_id)
	
	lista_cursos = Curso.objects.exclude(id__in=excluidos)
	aulas=Aulas.objects.object.filter(AnoAcademico__Activo=True)

	contexto = {'doce_list':docente_list,'lista_cursos':lista_cursos,'aulas':aulas}

	return render(request,'docentecurso/create_docentecurso.html',contexto)

def DocenteCursoStore(request):
	if request.method=='POST':
		
		id_docente=request.POST.get('docente_id')
		id_curso=request.POST.get("curso")
		id_aula=request.POST.get("aula")

		existe_registro=DocenteCurso.objects.filter(
			Curso_id=id_curso,
			Docente_id=id_docente,
			Aulas_id=id_aula
		).exists()

		if existe_registro:
			return redirect('/docentes/listar/?message=Esta combinación ya existe para este profesor'+'&status=warning')
		
		
		docecur=DocenteCurso()
		docecur.Curso_id=id_curso
		docecur.Docente_id = id_docente
		docecur.Aulas_id=id_aula
		docecur.save()
		
		return redirect('/docentes/listar/?message=Registro Guardado'+'&status=success')
	
def DocenteCursoEdit(request,id_docentecurso):
	docentecurso= DocenteCurso.objects.get(id=id_docentecurso)
	return JsonResponse(model_to_dict(docentecurso),safe=False)

def DocenteCursoDestroy(request):
	id_docentecurso=request.POST.get('id_registro_eliminar')
	
	notas=NotasComp.objects.filter(DocenteCurso_id=id_docentecurso).exists()
	if notas:
		return redirect('/docentes/listar/?message=No se puede eliminar este curso/aula porque contiene notas'+'&status=danger')

	DocenteCurso.objects.get(id=id_docentecurso).delete()
	return redirect('/docentes/listar/?message=Curso Eliminado'+'&status=success')
	



class DocenteCursoDelete(DeleteView):
	model = DocenteCurso
	template_name = 'docentecurso/delete_docentecurso.html'
	success_url = '/docentes/listar/'

def DocenteCursoUpdate(request):
	if request.method=='POST':
		id_docentecurso=request.POST.get('docentecurso_id')
		id_curso=request.POST.get('curso')
		id_aula=request.POST.get('aula')
		
		docentecurso=DocenteCurso.objects.get(id=id_docentecurso)
		if DocenteCurso.objects.filter(
			Docente_id=docentecurso.Docente_id,
			Curso_id=id_curso,
			Aulas_id=id_aula,
			).exists():
			return redirect('/docentes/listar/?message=No se puede actualizar esta combinación por que ya existe,'+'&status=warning')

		docentecurso.Curso_id=id_curso
		docentecurso.Aulas_id=id_aula
		docentecurso.save()
		return redirect('/docentes/listar/?message=Curso/Aula Actualizado'+'&status=success')
	