# Generated by Django 5.1.3 on 2024-11-08 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='treino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='app.treino'),
        ),
    ]
