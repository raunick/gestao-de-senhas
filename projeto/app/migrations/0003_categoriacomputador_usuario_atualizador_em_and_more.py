# Generated by Django 4.2.4 on 2023-08-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_categoriacomputador_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriacomputador',
            name='usuario_atualizador_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='categoriacomputador',
            name='usuario_criador_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='chamada',
            name='usuario_atualizador_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='chamada',
            name='usuario_criador_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='computador',
            name='usuario_atualizador_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='computador',
            name='usuario_criador_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fila',
            name='usuario_atualizador_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fila',
            name='usuario_criador_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='localizacao',
            name='usuario_atualizador_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='localizacao',
            name='usuario_criador_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
