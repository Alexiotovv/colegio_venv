from ast import For, If
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from openpyxl import Workbook,load_workbook
from django.db import connection ##permite conectar directamente a la base de datos

from colegio.Apps.Matricula.models import Matricula
from colegio.Apps.Alumno.models import Alumno
from colegio.Apps.Curso.models import Curso
from colegio.Apps.Notas.models import Notas,NotasComp
from colegio.Apps.AvanceNotas.models import AvanceNotas
from colegio.Apps.AvanceNotas.models import AvanceNotasComp
from colegio.Apps.AnoAcademico.models import AnoAcademico
from colegio.Apps.Docente.models import Docente
from colegio.Apps.PeriodoAcademico.models import PAcademico
from colegio.Apps.Competencias.models import CompetenciaCurso


from colegio.Apps.Matricula.forms import MatriculaForm
from colegio.Apps.Notas.forms import NotasForm
from colegio.Apps.Alumno.forms import AlumnoForm
from colegio.Apps.Docente.forms import DocenteForm
from colegio.Apps.Curso.forms import CursoForm
from colegio.Apps.PeriodoAcademico.forms import PAcademicoForm
from colegio.Apps.AnoAcademico.forms import AnoAcademicoForm
from math import *
from datetime import *
from django.contrib.auth.decorators import login_required


#funcion que devuelve los nombres de las columnas
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def OpcionImprimir(request):
	return render(request,'libretas/opcion_imprimir.html')

def ImprimirAvanceNotasPrimaria(request):
    aac = AnoAcademico.objects.all().order_by('-Ano')
    pac = PAcademico.objects.all().order_by('Nombre')
    contexto = {'aac':aac,'pac':pac}#para filtro
    
    if  request.method=='POST':
        #aactual= date.today().year#AÑO
        gradonivel = request.POST.get("Grado")
        seccion = request.POST.get("Seccion")
        ano = request.POST.get("Ano")#El año que manda del form
        paca=request.POST.get("Pac")
        nivel=str(gradonivel)[1:len(gradonivel)] #extrae solo PRIM
        if nivel=='PRIM':
            nivel='PRIMARIO'
        else:
            nivel='SECUNDARIO'
        
        #########################################################SE LE PUSO -1 PARA QUE NO SUME EL CALIFICATIVO DE ÁREA
        result = Curso.objects.raw('SELECT 1 as id,ccur."Curso_id" as IDCURSO,Count(*)-1 as NUM_COMPE FROM "Competencias_competenciacurso" as ccur GROUP BY ccur."Curso_id" ORDER BY ccur."Curso_id"')
        
        notas=AvanceNotasComp.objects.filter(PAcademico__Nombre=paca,Matricula__AnoAcademico__Ano=ano,Matricula__Grado=gradonivel,Matricula__Seccion=seccion).order_by('Curso__Orden','Competencias__Orden')
        tutor=Docente.objects.filter(TutorGrado=gradonivel,TutorSeccion=seccion).last()
        matricula = Matricula.objects.filter(Grado=gradonivel,Seccion=seccion,AnoAcademico__Ano=ano).order_by('Alumno__ApellidoPaterno','Alumno__ApellidoMaterno','Alumno__Nombres')
        
        contexto2={'result':result,'tutor':tutor,'matricula':matricula,'nivel':nivel,'paca':paca,'ano':ano,'gradonivel':gradonivel,'seccion':seccion,'notas':notas}#para libreta de avance
        return render(request,'libretas/LibretaAvancePrimaria.html',contexto2)
    else:
        return render(request,'otras_opciones/imprimir_avances_primaria.html',contexto)

def ImprimirAvanceNotasSecundaria(request):
    aac = AnoAcademico.objects.all().order_by('-Ano')
    pac = PAcademico.objects.all().order_by('Nombre')
    contexto = {'aac':aac,'pac':pac}#para filtro
    
    if  request.method=='POST':
        #aactual= date.today().year#AÑO
        #aactual= date.today().year#AÑO
        gradonivel = request.POST.get("Grado")
        seccion = request.POST.get("Seccion")
        ano = request.POST.get("Ano")#El año que manda del form
        paca=request.POST.get("Pac")
        nivel=str(gradonivel)[1:len(gradonivel)] #extrae solo PRIM
        #cursos=Curso.objects.filter(Nivel=nivel)
        if nivel=='PRIM':
            nivel='PRIMARIO'
        else:
            nivel='SECUNDARIO'
        
        result = Curso.objects.raw('SELECT 1 as id,ccur."Curso_id" as IDCURSO,Count(*)-1 as NUM_COMPE FROM "Competencias_competenciacurso" as ccur GROUP BY ccur."Curso_id" ORDER BY ccur."Curso_id"')

        notas=AvanceNotasComp.objects.filter(PAcademico__Nombre=paca,Matricula__AnoAcademico__Ano=ano,Matricula__Grado=gradonivel,Matricula__Seccion=seccion).order_by('Curso__Orden','Competencias__Orden')
        tutor=Docente.objects.filter(TutorGrado=gradonivel,TutorSeccion=seccion).last()
        matricula = Matricula.objects.filter(Grado=gradonivel,Seccion=seccion,AnoAcademico__Ano=ano).order_by('Alumno__ApellidoPaterno','Alumno__ApellidoMaterno','Alumno__Nombres')
        
        contexto2={'result':result,'tutor':tutor,'matricula':matricula,'nivel':nivel,'paca':paca,'ano':ano,'gradonivel':gradonivel,'seccion':seccion,'notas':notas}#para libreta de avance
        return render(request,'libretas/LibretaAvanceSecundaria.html',contexto2)
    else:
        return render(request,'otras_opciones/imprimir_avances_secundaria.html',contexto)

def ImprimirNotasPrimaria(request):
    aac = AnoAcademico.objects.all().order_by('-Ano')
    pac = PAcademico.objects.all().order_by('Nombre')
    contexto = {'aac':aac,'pac':pac}#para filtro
    cursor = connection.cursor()
    if  request.method=='POST':
        #aactual= date.today().year#AÑO
        gradonivel = request.POST.get("Grado")
        seccion = request.POST.get("Seccion")
        ano = request.POST.get("Ano")#El año que manda del form
        paca=request.POST.get("Pac")
        nivel=str(gradonivel)[1:len(gradonivel)] #extrae solo PRIM
        grado=str(gradonivel)[0:1] #extrae solo 1 el grado
        nivelcorto=''
        if nivel=='PRIM':
            nivel='PRIMARIO'
            nivelcorto='PRIM'
        else:
            nivel='SECUNDARIO'
            nivelcorto='SEC'

        result = Curso.objects.raw('SELECT 1 as id,ccur."Curso_id" as IDCURSO,Count(*) as NUM_COMPE FROM "Competencias_competenciacurso" as ccur GROUP BY ccur."Curso_id" ORDER BY ccur."Curso_id"')
        tutor=Docente.objects.filter(TutorGrado=gradonivel,TutorSeccion=seccion).last()
        matricula = Matricula.objects.filter(Grado=gradonivel,Seccion=seccion,AnoAcademico__Ano=ano).order_by('Alumno__ApellidoPaterno','Alumno__ApellidoMaterno','Alumno__Nombres')
        
        #Envia solamente para la apreciación del tutor
        apreciaciones=NotasComp.objects.filter(Matricula__AnoAcademico__Ano=ano,Matricula__Grado=gradonivel,Matricula__Seccion=seccion).order_by('PAcademico__id')
        
        bim1="select n1.* from notas_primaria_ibimestre n1 WHERE n1.Ano=%s and n1.grado=%s and n1.seccion=%s and n1.nivelcurso=%s"
        cursor.execute(bim1,[ano,gradonivel,seccion,'PRIM'])
        notas = dictfetchall(cursor)
        
        bim2="select n2.* from notas_primaria_iibimestre n2 WHERE n2.Ano=%s and n2.grado=%s and n2.seccion=%s and n2.nivelcurso=%s"
        cursor.execute(bim2,[ano,gradonivel,seccion,'PRIM'])
        notas2 = dictfetchall(cursor)
        
        bim3="select n3.* from notas_primaria_iiibimestre n3 WHERE n3.Ano=%s and n3.grado=%s and n3.seccion=%s and n3.nivelcurso=%s"
        cursor.execute(bim3,[ano,gradonivel,seccion,'PRIM'])
        notas3 = dictfetchall(cursor)

        bim4="select n4.* from notas_primaria_ivbimestre n4 WHERE n4.Ano=%s and n4.grado=%s and n4.seccion=%s and n4.nivelcurso=%s"
        cursor.execute(bim4,[ano,gradonivel,seccion,'PRIM'])
        notas4 = dictfetchall(cursor)

       #recorre cada vista consultada en cada bimestre y coloca en el objectlist la nota que le corresponde
        for n in notas:
            for n2 in notas2:
                if n['competencia']==n2['competencia'] and  n['curso']==n2['curso'] and n['matricula']==n2['matricula']:                    
                    n['nota2']=n2['nota']

        for n in notas:
            for n3 in notas3:
                if n['competencia']==n3['competencia'] and  n['curso']==n3['curso'] and n['matricula']==n3['matricula']:                    
                    n['nota3']=n3['nota']

        for n in notas:
            for n4 in notas4:
                if n['competencia']==n4['competencia'] and  n['curso']==n4['curso'] and n['matricula']==n4['matricula']:                    
                    n['nota4']=n4['nota']

        contexto2={'apreciaciones':apreciaciones,'notas':notas,'result':result,'tutor':tutor,'matricula':matricula,'nivel':nivel,'paca':paca,'ano':ano,'gradonivel':gradonivel,'seccion':seccion,'grado':grado,'nivelcorto':nivelcorto}#para libreta de avance
        return render(request,'libretas/LibretaPrimaria.html',contexto2)
    else:
        return render(request,'otras_opciones/imprimir_libreta_primaria.html',contexto)



def ImprimirNotasSecundaria(request):
    aac = AnoAcademico.objects.all().order_by('-Ano')
    pac = PAcademico.objects.all().order_by('Nombre')
    contexto = {'aac':aac,'pac':pac}#para filtro
    cursor = connection.cursor()
    if  request.method=='POST':
        #aactual= date.today().year#AÑO
        gradonivel = request.POST.get("Grado")
        seccion = request.POST.get("Seccion")
        ano = request.POST.get("Ano")#El año que manda del form
        paca=request.POST.get("Pac")
        nivel=str(gradonivel)[1:len(gradonivel)] #extrae solo PRIM
        grado=str(gradonivel)[0:1] #extrae solo PRIM
        nivelcorto=''
        if nivel=='SEC':
            nivel='SECUNDARIO'
            nivelcorto='SEC'
        else:
            nivel='PRIMARIO'
            nivelcorto='PRIM'

        result = Curso.objects.raw('SELECT 1 as id,ccur."Curso_id" as IDCURSO,Count(*) as NUM_COMPE FROM "Competencias_competenciacurso" as ccur GROUP BY ccur."Curso_id" ORDER BY ccur."Curso_id"')
        tutor=Docente.objects.filter(TutorGrado=gradonivel,TutorSeccion=seccion).last()
        matricula = Matricula.objects.filter(Grado=gradonivel,Seccion=seccion,AnoAcademico__Ano=ano).order_by('Alumno__ApellidoPaterno','Alumno__ApellidoMaterno','Alumno__Nombres')
        
        #Envia solamente para la apreciación del tutor
        apreciaciones=NotasComp.objects.filter(Matricula__AnoAcademico__Ano=ano,Matricula__Grado=gradonivel,Matricula__Seccion=seccion).order_by('PAcademico__id')
        
        bim1="select n1.* from notas_primaria_ibimestre n1 WHERE n1.Ano=%s and n1.grado=%s and n1.seccion=%s and n1.nivelcurso=%s"
        cursor.execute(bim1,[ano,gradonivel,seccion,'SEC'])
        notas = dictfetchall(cursor)
        
        bim2="select n2.* from notas_primaria_iibimestre n2 WHERE n2.Ano=%s and n2.grado=%s and n2.seccion=%s and n2.nivelcurso=%s"
        cursor.execute(bim2,[ano,gradonivel,seccion,'SEC'])
        notas2 = dictfetchall(cursor)
        
        bim3="select n3.* from notas_primaria_iiibimestre n3 WHERE n3.Ano=%s and n3.grado=%s and n3.seccion=%s and n3.nivelcurso=%s"
        cursor.execute(bim3,[ano,gradonivel,seccion,'SEC'])
        notas3 = dictfetchall(cursor)

        bim4="select n4.* from notas_primaria_ivbimestre n4 WHERE n4.Ano=%s and n4.grado=%s and n4.seccion=%s and n4.nivelcurso=%s"
        cursor.execute(bim4,[ano,gradonivel,seccion,'SEC'])
        notas4 = dictfetchall(cursor)

       #recorre cada vista consultada en cada bimestre y coloca en el objectlist la nota que le corresponde
        for n in notas:
            for n2 in notas2:
                if n['competencia']==n2['competencia'] and  n['curso']==n2['curso'] and n['matricula']==n2['matricula']:                    
                    n['nota2']=n2['nota']

        for n in notas:
            for n3 in notas3:
                if n['competencia']==n3['competencia'] and  n['curso']==n3['curso'] and n['matricula']==n3['matricula']:                    
                    n['nota3']=n3['nota']

        for n in notas:
            for n4 in notas4:
                if n['competencia']==n4['competencia'] and  n['curso']==n4['curso'] and n['matricula']==n4['matricula']:                    
                    n['nota4']=n4['nota']

        contexto2={'apreciaciones':apreciaciones,'notas':notas,'result':result,'tutor':tutor,'matricula':matricula,'nivel':nivel,'paca':paca,'ano':ano,'gradonivel':gradonivel,'seccion':seccion,'grado':grado,'nivelcorto':nivelcorto}#para libreta de avance
        return render(request,'libretas/LibretaSecundaria.html',contexto2)
    else:
        return render(request,'otras_opciones/imprimir_libreta_secundaria.html',contexto)


