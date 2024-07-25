from django.urls import path
from colegio.Apps.Aulas.views import *

urlpatterns = [
    path("index/aulas/", index, name="app_index_aulas"),
    path("store/aulas/", store, name="app_store_aulas"),
    path("edit/aulas/<id_aula>", edit, name="app_edit_aulas"),
    path("update/aulas/", update, name="app_update_aulas"),
]
