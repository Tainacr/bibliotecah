# Generated by Django 5.0.3 on 2024-03-18 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_emprestimo_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='devolucao',
            new_name='fazerdevolucao',
        ),
        migrations.RenameField(
            model_name='emprestimo',
            old_name='emprestimo',
            new_name='fazeremprestimo',
        ),
    ]