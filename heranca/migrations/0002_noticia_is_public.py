# Generated by Django 3.2 on 2023-08-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heranca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]