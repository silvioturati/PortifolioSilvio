# Generated by Django 3.1.4 on 2020-12-31 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=200)),
                ('descricao_projeto', models.TextField()),
                ('cliente', models.CharField(max_length=100)),
                ('data_conclusao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('website', models.CharField(max_length=200)),
                ('linguagem', models.CharField(max_length=50)),
                ('tags_projeto', models.TextField()),
                ('detalhes_projeto', models.TextField()),
            ],
        ),
    ]
