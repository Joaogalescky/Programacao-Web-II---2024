# Generated by Django 5.0.3 on 2024-10-13 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_livro_ano_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='livro',
        ),
        migrations.AddField(
            model_name='livro',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='livros', to='app.tag'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='arquivo_pdf',
            field=models.FileField(upload_to='livros/'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='app.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
