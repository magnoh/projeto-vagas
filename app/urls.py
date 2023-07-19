from django.contrib import admin
from  app.views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('descricao/<int:descricao_id>', descricao, name='descricao'),
    path('buscar', buscar, name='buscar'),
    path('cadastro_vaga', cadastro_vagas, name='cadastro_vaga'),

]

