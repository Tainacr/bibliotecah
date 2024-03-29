# Generated by Django 5.0.3 on 2024-03-18 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_emprestimo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'verbose_name': 'Empréstimo', 'verbose_name_plural': 'Empréstimos'},
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='devolucao',
            field=models.CharField(max_length=100, verbose_name='Data de devolução'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='emprestimo',
            field=models.CharField(max_length=100, verbose_name='Data de empréstimo'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro', verbose_name='Nome do livro'),
        ),
    ]
