from django.db import models
from django.contrib.auth.models import User
from datetime import  date

class Vaga(models.Model):
    # escolaridade = (
    #     ("ENSINO FUNDAMENTAL","Ensino fundamental"),
    #     ("ENSINO MÉDIO","Ensino médio"),
    #     ("TECNÓLOGO","Tecnólogo"),
    #     ("ENSINO SUPERIOR","Ensino Superior"),
    #     ("PÓS / MBA / MESTRADO","Pós / MBA / Mestrado"),
    #     ("DOUTORADO","Doutorado"),
    # )

    # salario = (
    #     ("ATÉ 1.000","Até 1.000"),
    #     ("DE 1.000 a 2.000","De 1.000 a 2.000"),
    #     ("DE 2.000 a 3.000","De 2.000 a 3.000"),
    #     ("ACIMA de 3.000","Acima de 3.000"),
    # )

    cargo_vaga = models.CharField(max_length=100, null = False, blank=False)
    descricao_vaga = models.TextField(null=False, blank=False, default='')
    faixa_salarial = models.CharField(max_length=100)
    escolaridade_vaga = models.TextField(max_length=100)
    publicada = models.BooleanField(default=True)
    data_publicada = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete= models.SET_NULL,
        null= True,
        blank=False,
        related_name="user",
        
    )

    def __str__(self):
        return self.cargo_vaga 
        # return f"Cargo: {self.cargo_vaga}, Descricao: {self.descricao_vaga}, faixa_salarial: {self.faixa_salarial}, escolaridade: {self.escolaridade}"

