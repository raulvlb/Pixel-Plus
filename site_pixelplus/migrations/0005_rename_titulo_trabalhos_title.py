# Generated by Django 4.0.6 on 2022-07-15 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_pixelplus', '0004_trabalhos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trabalhos',
            old_name='titulo',
            new_name='title',
        ),
    ]
