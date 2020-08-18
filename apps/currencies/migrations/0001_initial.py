# Generated by Django 3.0.8 on 2020-08-17 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=20, unique=True)),
                ('currency_ar', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=3, unique=True)),
            ],
        ),
    ]
