from django.shortcuts import render, get_object_or_404, redirect
from app.models import Vaga
from app.forms import *
from django.contrib import messages

import json

def index(request):
    acesso = Vaga.objects.order_by('data_publicada')
    return render(request, 'app/index.html', {'cards': acesso})

def descricao(request, descricao_id):
    vaga = get_object_or_404(Vaga, pk=descricao_id)
    return render(request, 'app/descricao.html', {'vaga': vaga})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuario não logado")
        return redirect('login')
    acessos = Vaga.objects.order_by('data_publicada').filter(publicada=True)
    if "buscar" in request.GET:
          nome_a_buscar = request.GET['buscar']
          if nome_a_buscar:
               acessos = acessos.filter(cargo_vaga__icontains=nome_a_buscar)

    return render(request, 'app/buscar.html', {"cards": acessos})


def cadastro_vagas(request):
     form = CadastroVaga()
     data = Vaga.objects.all()

     context = {
          'form': form,
          'vagas': data,
     }

     if request.method == 'POST':
          form = CadastroVaga(request.POST)
          
          if form.is_valid():
                cargo_vaga = form['cargo_vaga'].value()
                descricao_vaga = form['descricao_vaga'].value()
                salario = form['faixa_salarial'].value()
                escolaridade = form['escolaridade_vaga'].value()

                vaga = Vaga(
                    cargo_vaga=cargo_vaga,
                    descricao_vaga=descricao_vaga, 
                    faixa_salarial=salario,
                    escolaridade_vaga=escolaridade,
                )

                vaga.save()

     return render(request, 'app/cadastrar_vaga.html', context={ "data": context})


# def cadastro_vagas(request):
#     if not request.user.is_authenticated:
#         messages.error(request,"Usuario não logado")
#         return redirect('login')
    
#     form = CadastroVaga()
#     data = Vaga.objects.all()
   

#     if request.method == 'POST':
#         form = CadastroVaga(request.POST)
#         if form.is_valid():
#             cargo_vaga = form.cleaned_data['cargo_vaga']
#             descricao_vaga = form.cleaned_data['descricao_vaga']
#             faixa_salarial = form.cleaned_data['faixa_salarial']
#             escolaridade_vaga = form.cleaned_data['escolaridade_vaga']

#             vaga = Vaga.objects(
#                 cargo_vaga=cargo_vaga,
#                 descricao_vaga=descricao_vaga, 
#                 faixa_salarial=faixa_salarial,
#                 escolaridade_vaga=escolaridade_vaga,
#             )
#             vaga.save()

#     context = {
#         'form': form,
#         'vagas': data,
#     }

#     return render(request, 'app/cadastrar_vaga.html', context)