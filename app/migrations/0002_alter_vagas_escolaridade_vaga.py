# Generated by Django 4.2.3 on 2023-07-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='escolaridade_vaga',
            field=models.TextField(choices=[('ENSINO FUNDAMENTAL', 'Ensino fundamental'), ('ENSINO MÉDIO', 'Ensino médio'), ('TECNÓLOGO', 'Tecnólogo'), ('ENSINO SUPERIOR', 'Ensino Superior'), ('PÓS / MBA / MESTRADO', 'Pós / MBA / Mestrado'), ('DOUTORADO', 'Doutorado')], default='', max_length=100),
        ),
    ]
