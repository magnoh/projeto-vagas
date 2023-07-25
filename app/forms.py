from django import forms
from .models import Vaga

escolaridade = [
        ("ENSINO FUNDAMENTAL","Ensino fundamental"),
        ("ENSINO MÉDIO","Ensino médio"),
        ("TECNÓLOGO","Tecnólogo"),
        ("ENSINO SUPERIOR","Ensino Superior"),
        ("PÓS / MBA / MESTRADO","Pós / MBA / Mestrado"),
        ("DOUTORADO","Doutorado"),
    ]

salario = [
        ("ATÉ 1.000","Até 1.000"),
        ("DE 1.000 a 2.000","De 1.000 a 2.000"),
        ("DE 2.000 a 3.000","De 2.000 a 3.000"),
        ("ACIMA de 3.000","Acima de 3.000"),
    ]

class CadastroVaga(forms.Form):
    cargo_vaga = forms.CharField(
        label="Cargo da Vaga", 
        required=True,  
        
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Informe qual cargo",
                "name": "usuario"
            }
        )
        
    )
    descricao_vaga = forms.CharField(
        label="Descrição da vaga", 
        required=True,  
        
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Informe a descrição da vaga",
                "name": "usuario",
                "rows": "7",
                "cols": "63",
                "class": "textfield color-white",
            }
        )
        
    )

    faixa_salarial = forms.ChoiceField(choices=salario)

    escolaridade_vaga = forms.ChoiceField(choices=escolaridade)


class VagasForms(forms.ModelForm):
    
    
    class Meta():
        model = Vaga
        fields = ['cargo_vaga', 'descricao_vaga','escolaridade_vaga', 'faixa_salarial','usuario',]
        exclude = ['publicada',]
        labels = {
            'descricao_vaga': 'Descrição',
            'data_publicada': 'Data de registro',
            'usuario':'Usuário',
        }
        widgets = {
            'cargo_vaga': forms.TextInput(attrs={'class':'form-control'}),
            'descricao_vaga': forms.Textarea(attrs={'class':'form-control'}),
            'data_publicada': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control',
                    }
                ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
    faixa_salarial = forms.ChoiceField(choices=salario)
    escolaridade_vaga = forms.ChoiceField(choices=escolaridade)