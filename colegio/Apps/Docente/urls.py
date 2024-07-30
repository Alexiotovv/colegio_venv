from django.urls import path, include
from django.views.generic.base import TemplateView
from colegio.Apps.Docente.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('docentes/nuevo/<id_user>', login_required(DocenteNew), name='app_docente_nuevo'),
    path('docentes/listar/', login_required(DocenteList), name='app_docente_listar'),
    path('docentes/editar/<id_docente>', login_required(DocenteUpdate), name='app_docente_editar'),
    path('docentes/edit/<id_docente>', login_required(DocenteEdit), name='app_docente_edit'),
    path('docentes/update/', login_required(DocenteUpdates), name='app_docente_update'),
	path('docentes/eliminar/', login_required(DocenteDelete), name='app_docente_delete'),
	path('docentes/detalle/<pk>', login_required(DocenteDetalle.as_view()), name='app_docente_detalle'),		
]