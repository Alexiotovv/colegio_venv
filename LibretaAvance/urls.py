from django.urls import path, include
from django.views.generic.base import TemplateView
from colegio.Apps.LibretaAvance.views import ImprimirAvanceNotasPrimaria,ImprimirAvanceNotasSecundaria,OpcionImprimir,ImprimirNotasPrimaria,ImprimirNotasSecundaria
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('libretas/libretas_avances_prim_comp/', login_required(ImprimirAvanceNotasPrimaria), name='app_imprimir_avances_prim_comp'),
    path('libretas/libretas_avances_sec_comp/', login_required(ImprimirAvanceNotasSecundaria), name='app_imprimir_avances_sec_comp'),
    path('libretas/libretas_prim_comp/', login_required(ImprimirNotasPrimaria), name='app_imprimir_prim_comp'),
    path('libretas/libretas_sec_comp/', login_required(ImprimirNotasSecundaria), name='app_imprimir_sec_comp'),
    path('libretas/opcion_imprimir/', login_required(OpcionImprimir), name='app_opcion_imprimir_comp'),
]
