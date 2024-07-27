from django.shortcuts import render,redirect
from colegio.Apps.AnoAcademico.models import * 
from colegio.Apps.Aulas.models import * 
from colegio.Apps.Nivel.models import * 
from colegio.Apps.Grado.models import * 
from colegio.Apps.DocenteCurso.models import * 

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    anos=AnoAcademico.objects.all().order_by('-id')
    aulas = Aulas.objects.all()
    niveles=Nivel.objects.all()
    grados=Grado.objects.all()
    secciones=Seccion.objects.all()
    message = request.GET.get('message', None)

    return render(request,'aulas/index_aulas.html',{
        'aulas':aulas,
        'niveles':niveles,
        'grados':grados,
        'secciones':secciones,
        'anos':anos,
        'message':message})

def store(request):
    if request.method == 'POST':
        idanoacademico = request.POST.get('anoacademico')
        idnivel = request.POST.get('nivel')
        idgrado = request.POST.get('grado')
        idseccion = request.POST.get('seccion')

        if Aulas.objects.filter(
            AnoAcademico_id=idanoacademico,
            Nivel_id=idnivel,
            Grado_id=idgrado,
            Seccion_id=idseccion
        ).exists():
            return redirect('/index/aulas/?message=Este aula ya se ha registrado')

        
        aulas = Aulas(
            AnoAcademico_id=idanoacademico,
            Nivel_id=idnivel,
            Grado_id=idgrado,
            Seccion_id=idseccion
        )
        aulas.save()
        
        return redirect('/index/aulas/?message=Registro actualizado satisfactoriamente')

def update(request):
    if request.method == 'POST':
        idanoacademico = request.POST.get('anoacademico')
        idnivel = request.POST.get('nivel')
        idgrado = request.POST.get('grado')
        idseccion = request.POST.get('seccion')

        idaula=request.POST.get('id_aula')

        # if Aulas.objects.filter(
        #     AnoAcademico_id=idanoacademico,
        #     Nivel_id=idnivel,
        #     Grado_id=idgrado,
        #     Seccion_id=idseccion
        # ).exists():
        #     return redirect('/index/aulas/?message=Este aula ya se ha registrado')


        aula=Aulas.objects.get(id=idaula)
        aula.AnoAcademico_id=idanoacademico
        aula.Nivel_id=idnivel
        aula.Grado_id=idgrado
        aula.Seccion_id=idseccion
        aula.save()
        
        return redirect('/index/aulas/?message=Registro actualizado satisfactoriamente')

def destroy(request):
    if request.method=='POST':
        id_aula=request.POST.get('id_registro_eliminar')
        
        print(id_aula)

        existen_registros=DocenteCurso.objects.filter(Aulas_id=id_aula).exists()
        if existen_registros:
            return redirect('/index/aulas/?message=No se puede Eliminar este aula, contiene datos')
        else:
            Aulas.objects.get(id=id_aula).delete()

        return redirect('/index/aulas/?message=Aula eliminada correctamente')

def edit(request,id_aula):
    aula = Aulas.objects.get(id=id_aula)
    aula=model_to_dict(aula)
    return JsonResponse(aula,safe=False)