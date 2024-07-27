from django.urls import path, include
from django.views.generic.base import TemplateView
from colegio.Apps.AnoAcademico.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('academico/nuevo/', login_required(AnoAcademicoNew), name='app_academico_nuevo'),
    path('academico/listar/', login_required(AnoAcademicoList.as_view()), name='app_academico_listar'),
    path('academico/update/', login_required(update), name='app_academico_update'),
    path('academico/edit/<id>', login_required(edit), name='app_academico_edit'),
	path('academico/eliminar/<pk>', login_required(AnoAcademicoDelete.as_view()), name='app_academico_delete'),
	path('academico/detalle/<pk>', login_required(AnoAcademicoDetalle.as_view()), name='app_academico_detalle'),		
]