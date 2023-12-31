# Generated by Django 4.2.7 on 2023-11-28 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Element',
            },
        ),
        migrations.CreateModel(
            name='Rune',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Density', models.IntegerField()),
                ('Image', models.CharField(max_length=200)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RuneApp.category')),
                ('Element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RuneApp.element')),
            ],
            options={
                'db_table': 'Rune',
            },
        ),
    ]
