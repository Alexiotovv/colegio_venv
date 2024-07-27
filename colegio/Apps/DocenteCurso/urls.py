from django.urls import path, include
from django.views.generic.base import TemplateView
from colegio.Apps.DocenteCurso.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('docentecurso/create/<id_docente>',login_required(DocenteCursoCreate),name='app_docentecurso_create'),
	path('docentecurso/delete/<pk>',login_required(DocenteCursoDelete.as_view()),name='app_docentecurso_delete'),
	path('docentecurso/update/',login_required(DocenteCursoUpdate),name='app_docentecurso_update'),
    path('docentecurso/store/',login_required(DocenteCursoStore),name='app_docentecurso_store'),
    path('docentecurso/edit/<id_docentecurso>',login_required(DocenteCursoEdit),name='app_docentecurso_edit'),
    path('docentecurso/destroy/',login_required(DocenteCursoDestroy),name='app_docentecurso_destroy'),
	path('docentecurso/listar_asginaciones/',login_required(DocenteListarAsginaciones),name='app_docente_listar_asignaciones'),
]