# Generated by Django 3.0.8 on 2020-08-18 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_currency_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['id'], 'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
    ]
