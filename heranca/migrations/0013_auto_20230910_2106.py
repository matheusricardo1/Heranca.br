# Generated by Django 3.2 on 2023-09-11 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heranca', '0012_auto_20230908_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='conteudo_en',
        ),
        migrations.RemoveField(
            model_name='new',
            name='conteudo_pt_br',
        ),
        migrations.RemoveField(
            model_name='new',
            name='titulo_en',
        ),
        migrations.RemoveField(
            model_name='new',
            name='titulo_pt_br',
        ),
    ]