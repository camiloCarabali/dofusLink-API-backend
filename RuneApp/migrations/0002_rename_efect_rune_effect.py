# Generated by Django 4.2.7 on 2024-01-14 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RuneApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rune',
            old_name='Efect',
            new_name='Effect',
        ),
    ]