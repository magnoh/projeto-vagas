# Generated by Django 4.2.3 on 2023-07-04 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_vagas_vaga'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='data_publicada',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
