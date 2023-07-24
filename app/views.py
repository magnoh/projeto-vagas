from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from app.models import Vaga
from app.forms import *
from django.contrib import messages


def is_authenticated(func):

    def verify(request):
        if not request.user.is_authenticated:
            messages.error(request,"Usuario não logado")
            return redirect('login')
        return func(request)
     
    return verify

def index(request):
    acesso = Vaga.objects.order_by('data_publicada')
    return render(request, 'app/index.html', {'cards': acesso})

def descricao(request, descricao_id):
    vaga = get_object_or_404(Vaga, pk=descricao_id)
    return render(request, 'app/descricao.html', {'vaga': vaga})

def buscar(request):
    acessos = Vaga.objects.order_by('data_publicada')
    if "buscar" in request.GET:
          nome_a_buscar = request.GET['buscar']
          if nome_a_buscar:
               acessos = acessos.filter(cargo_vaga__icontains=nome_a_buscar)

    return render(request, 'app/buscar.html', {"cards": acessos})

@is_authenticated
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


def candidato_vaga(request):
     return render (request, 'app/candidato_vaga.html')


@is_authenticated
def editar_vaga(request):
     pass

@is_authenticated
def deletar_vaga(request):
     pass
