# Generated by Django 5.0.3 on 2024-11-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_exercicio_treino_treino_exercicio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treino',
            name='exercicio',
        ),
        migrations.AddField(
            model_name='treino',
            name='exercicios',
            field=models.ManyToManyField(related_name='treinos', to='app.exercicio'),
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='descricao_execucao',
            field=models.TextField(default='etc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='nome',
            field=models.CharField(default='teste', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treino',
            name='data_fim',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='treino',
            name='data_inicio',
            field=models.DateField(),
        ),
    ]
