# Generated by Django 5.1.3 on 2024-11-08 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_treino_objetivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercicio',
            name='treino',
        ),
        migrations.AddField(
            model_name='treino',
            name='exercicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='app.exercicio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='descricao_execucao',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='nome',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
