# Generated by Django 5.0.3 on 2024-03-18 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_emprestimo_options_alter_emprestimo_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.leitor', verbose_name='Nome do leitor'),
        ),
    ]
