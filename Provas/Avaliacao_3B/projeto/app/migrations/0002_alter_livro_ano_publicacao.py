# Generated by Django 5.1.2 on 2024-10-11 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano_publicacao',
            field=models.IntegerField(),
        ),
    ]
