from django import forms


class LoginUsuarioForms(forms.Form):
    nome_usuario_login = forms.CharField(
        label="Usuário", 
        required=False, 
        
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.: João Silva",
                "name": "usuario"
            }
        )
        
    )

    senha_usuario_login = forms.CharField(
        label="Senha", 
        required=False, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "name": "senha_usuario"
            }
        )  
    )


class CadastroUsuarioForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de login",
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
               
                "placeholder":"Ex.: John Smith"
            }
        )
        
    )
    email_usuario = forms.EmailField(
        label="Email",
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                
                "placeholder":"Ex.: johnsmith@mail.com"
            }
        )
    )
    senha_usuario_1 = forms.CharField(
        label="Senha de login",
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                
                "placeholder": "Digite sua senha"
            }
        )  
    )
    senha_usuario_2 = forms.CharField(
        label="Confirme sua senha",
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                
                "placeholder": "Digite sua senha novamente"
            }
        )  
    )


