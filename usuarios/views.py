from django.shortcuts import render,redirect

from usuarios.forms import *

from django.contrib.auth.models import User

from django.contrib import auth, messages

from django.contrib.auth import authenticate, login, logout


def login(request):
    form = LoginUsuarioForms()

    if request.method == 'POST':
        form = LoginUsuarioForms(request.POST)

        if form.is_valid():
            nome = form['nome_usuario_login'].value()
            senha = form['senha_usuario_login'].value()
        
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha,
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request,f"{nome} logado com sucesso!")
            return redirect('cadastro_vaga')
        else:
            messages.error(request, "Erro a o efetuar login")
            return redirect('login')

    return render(request, "usuarios/login.html", {'form': form})


def cadastro(request):
    form = CadastroUsuarioForms()

    if request.method == 'POST':
        form = CadastroUsuarioForms(request.POST)

        if form.is_valid():
            if form["senha_usuario_1"].value() != form["senha_usuario_2"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')
            
            nome=form["nome_cadastro"].value()
            email=form["email_usuario"].value()
            senha=form["senha_usuario_1"].value()

            if User.objects.filter(username=nome).first():
                messages.error(request, "Usuário ja existente")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')
            

    return render(request, "usuarios/cadastro.html", {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')
    