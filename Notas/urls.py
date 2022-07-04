from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from colegio.Apps.Notas.views import NotasNuevoComp, NotasNuevoSave, ListaNotas, NotasDelete, NotasEdit, OpcionNotas,NotasNuevoSaveUno,DeleteNotasxCurso, NotasNuevoBimestre, NotasNuevoSaveBimestre,NotasNuevoSaveComp,ConsolidadoNotas
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('notas/notas_nuevo_save_uno/',login_required(NotasNuevoSaveUno),name='app_nota_nuevo_save_uno'),
path('notas/notas_nuevo_bimestre/',login_required(NotasNuevoBimestre),name='app_nota_nuevo_bimestre'),
path('notas/notas_nuevo_save_bimestre/',login_required(NotasNuevoSaveBimestre),name='app_nota_nuevo_save_bimestre'),
path('notas/notas_nuevo_comp/',login_required(NotasNuevoComp),name='app_nota_nuevo_comp'),
path('notas/notas_nuevo_save/',login_required(NotasNuevoSaveComp),name='app_nota_nuevo_save_comp'),
path('notas/eliminar/<pk>',login_required(NotasDelete.as_view()),name='app_notas_delete'),
path('notas/editar/<id_notas>',login_required(NotasEdit),name='app_notas_edit'),
path('notas/listar/',login_required(ListaNotas),name='app_listar_notas'),
path('notas/opcion_notas/',login_required(OpcionNotas),name='app_opcion_notas'),
path('notas/eliminarxcurso/',login_required(DeleteNotasxCurso),name='app_delete_notasxcurso'),
path('otras_opciones/consolidado_libretas/',login_required(ConsolidadoNotas),name='app_consolidado_libretas'),
]
